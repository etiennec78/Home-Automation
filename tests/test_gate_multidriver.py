"""Offline tests of templates extracted from Automatic Gate.

These simulate state changes and interleavings, not the HA script scheduler,
device acknowledgements, real GPS, or the motor's physical safety system.
"""
from pathlib import Path
import itertools
import json
import unittest

import yaml
from jinja2 import StrictUndefined
from jinja2.nativetypes import NativeEnvironment


class Loader(yaml.SafeLoader):
    pass


class InputRef(str):
    """Distinguish an actual YAML tag from an accidental {input: name} map."""


Loader.add_constructor('!input', lambda loader, node: InputRef(loader.construct_scalar(node)))
PATH = Path(__file__).resolve().parents[1] / 'Blueprints/Automatic-Gate/automatic-gate.yaml'
DOC = yaml.load(PATH.read_text(encoding='utf-8'), Loader=Loader)


def find(value, alias):
    if isinstance(value, dict):
        if value.get('alias') == alias:
            return value
        for child in value.values():
            result = find(child, alias)
            if result is not None:
                return result
    elif isinstance(value, list):
        for child in value:
            result = find(child, alias)
            if result is not None:
                return result
    return None


def required(alias):
    result = find(DOC, alias)
    assert result is not None, alias
    return result


def from_json(value, default=None):
    try:
        return json.loads(value)
    except (ValueError, TypeError):
        return default


class World:
    def __init__(self, statuses, gate='open'):
        self.sensors = ['input_text.driver_' + str(i) for i in range(len(statuses))]
        self.records = {
            sensor: {'status': status, 'last_closed': float(i + 1)}
            for i, (sensor, status) in enumerate(zip(self.sensors, statuses))
        }
        self.gate = gate
        self.env = NativeEnvironment(undefined=StrictUndefined)
        self.env.filters['from_json'] = from_json
        self.env.filters['combine'] = lambda base, update: {**base, **update}
        self.env.tests['is_state'] = self.is_state

    def states(self, sensor):
        value = self.records[sensor]
        return value if isinstance(value, str) else json.dumps(value)

    def is_state(self, entity, wanted):
        state = self.gate if entity == 'cover.gate' else self.states(entity)
        return state in wanted if isinstance(wanted, list) else state == wanted

    def render(self, template, idx=0, **extra):
        return self.env.from_string(template).render(
            itinerary_sensors=self.sensors, gate=['cover.gate'],
            states=self.states, is_state=self.is_state, idx=idx,
            itinerary_sensor=self.sensors[idx], coordination_epoch=float(idx + 1),
            **extra)

    def snapshot(self, idx=0):
        return self.render(required('Recompute live closing participants')['variables']['coordination'], idx)

    def ready(self, idx):
        self.records[self.sensors[idx]]['status'] = 'waiting_for_others'

    def wait_completed(self):
        return self.render(required('Wait for itinerary completion or manual closing')['wait_template'])

    def elected(self, idx, snapshot=None):
        node = required('Elect one closing owner')
        snapshot = self.snapshot(idx) if snapshot is None else snapshot
        return all(self.render(c['value_template'], idx, coordination=snapshot) for c in node['if'])

    def claim(self, idx):
        self.records[self.sensors[idx]]['status'] = 'closing_gate'

    def allowed(self, idx):
        node = required('Only the current owner may command the gate')
        return all(self.render(c['value_template'], idx, coordination=self.snapshot(idx)) for c in node['if'])


class MultiDriverTests(unittest.TestCase):
    def test_no_legacy_unbounded_wait_before_reactive_wait(self):
        coordinated = required('If someone is currently approaching or leaving')['then']
        self.assertIsNone(find(coordinated, 'Wait for manual gate closing'))
        wait = required('Wait for itinerary completion or manual closing')
        self.assertEqual(wait['timeout'], {'seconds': '{{ max(coordination_deadline - as_timestamp(now()), 0) }}'})
        self.assertTrue(wait['continue_on_timeout'])

    def test_every_coordination_wait_uses_the_same_deadline(self):
        world = World(['waiting_for_others'])
        for alias in ['Wait for itinerary completion or manual closing',
                      'Wait again if a new driver appeared during election',
                      'Keep the closing claim until the gate acknowledges',
                      'Wait for the owner or a manual closing']:
            timeout = required(alias)['timeout']
            for current, expected in [(100, 20), (120, 0), (130, 0)]:
                context = dict(coordination_deadline=120, now=lambda: current,
                               as_timestamp=lambda value: value, max=max)
                seconds = sum(world.render(template, **context) *
                              {'seconds': 1, 'minutes': 60}[unit]
                              for unit, template in timeout.items())
                self.assertEqual(seconds, expected, (alias, current))

    def test_blueprint_input_tags_survive_the_scoped_rewrite(self):
        tts = find(required('If someone is currently approaching or leaving')['then'], 'Notify over TTS')
        self.assertIsInstance(tts['enabled'], InputRef)
        self.assertEqual(tts['enabled'], 'phone_tts')
        self.assertIsInstance(tts['data']['data']['media_stream'], InputRef)
        self.assertEqual(tts['data']['data']['media_stream'], 'phone_tts_stream')

    def test_simultaneous_arrivals_close_only_after_both_ready(self):
        self.assert_completion_sequence(['on_approach', 'on_approach'])

    def test_simultaneous_departures_close_only_after_both_ready(self):
        self.assert_completion_sequence(['leaving', 'leaving'])

    def test_mixed_arrival_departure_retains_safety_priority(self):
        self.assert_completion_sequence(['on_approach', 'leaving'])

    def assert_completion_sequence(self, statuses):
        for order in itertools.permutations(range(2)):
            with self.subTest(statuses=statuses, order=order):
                world = World(statuses)
                world.ready(order[0])
                self.assertFalse(world.wait_completed())
                self.assertFalse(any(world.elected(i) for i in range(2)))
                world.ready(order[1])
                self.assertTrue(world.wait_completed())
                self.assertEqual([i for i in range(2) if world.elected(i)], [0])
                world.claim(0)
                self.assertTrue(world.allowed(0))
                self.assertFalse(world.allowed(1))

    def test_active_nearby_driver_never_releases_wait(self):
        for active in ['on_approach', 'leaving']:
            world = World(['waiting_for_others', active])
            self.assertFalse(world.wait_completed())
            self.assertFalse(world.elected(0))
            world.claim(0)  # A driver became active after an earlier election.
            self.assertFalse(world.allowed(0))

    def test_gps_loss_does_not_turn_an_active_itinerary_into_safe_to_close(self):
        # This protocol consumes itinerary readiness, not driving=off or GPS absence.
        # The existing per-driver loop owns GPS timeout/safety decisions.
        world = World(['waiting_for_others', 'on_approach'])
        self.assertFalse(world.wait_completed())
        self.assertFalse(world.elected(0))
        self.assertEqual(world.snapshot()['active'], [1])

    def test_invalid_or_unavailable_itinerary_holds_gate_on_timeout(self):
        for raw in ['unavailable', 'unknown', '{broken', 'null', '[]', '{}']:
            with self.subTest(raw=raw):
                world = World(['waiting_for_others', None])
                world.records[world.sensors[1]] = raw
                self.assertTrue(world.snapshot()['invalid'])
                self.assertFalse(world.wait_completed())
                self.assertFalse(world.elected(0))
                world.claim(0)
                self.assertFalse(world.allowed(0))

    def test_manual_closing_stops_wait_without_motor_command(self):
        for state in ['closing', 'closed']:
            world = World(['waiting_for_others', 'on_approach'], gate=state)
            self.assertTrue(world.wait_completed())
            self.assertFalse(any(world.elected(i) for i in range(2)))

    def test_all_three_ready_participants_have_one_owner_for_every_read_order(self):
        for order in itertools.permutations(range(3)):
            world = World(['waiting_for_others'] * 3)
            snapshots = {i: world.snapshot(i) for i in order}
            # Even if every run read before the first write, the same rank wins.
            winners = [i for i in order if world.elected(i, snapshots[i])]
            self.assertEqual(winners, [0])
            world.claim(0)
            self.assertEqual([i for i in range(3) if world.allowed(i)], [0])

    def test_unacknowledged_claim_prevents_followers_from_re_electing(self):
        world = World(['closing_gate', 'waiting_for_others'])
        for _ in range(5):
            self.assertTrue(world.wait_completed())
            self.assertFalse(world.elected(1))
        guard = required('Keep an unacknowledged claim rather than issue duplicate motor commands')
        self.assertTrue(guard['then'][0].get('stop'))

    def test_new_active_driver_after_election_blocks_command(self):
        world = World(['waiting_for_others', 'waiting_for_others', None])
        self.assertTrue(world.elected(0))
        world.claim(0)
        world.records[world.sensors[2]]['status'] = 'on_approach'
        self.assertFalse(world.allowed(0))

    def test_superseded_epoch_cannot_command_or_overwrite_new_itinerary(self):
        world = World(['closing_gate', 'waiting_for_others'])
        world.records[world.sensors[0]]['last_closed'] = 999
        self.assertFalse(world.allowed(0))
        guard = required('Do not overwrite a newer itinerary')
        self.assertTrue(world.render(guard['if'][0]['value_template']))

    def test_superseded_status_with_same_epoch_cannot_command_or_overwrite(self):
        for status in [None, 'arriving', 'on_approach', 'leaving']:
            with self.subTest(status=status):
                world = World(['closing_gate', 'waiting_for_others'])
                world.records[world.sensors[0]]['status'] = status
                self.assertFalse(world.allowed(0))
                guard = required('Do not overwrite a newer itinerary')
                self.assertTrue(world.render(guard['if'][0]['value_template']))

    def test_wait_observes_all_itinerary_sensors_and_current_gate(self):
        template = required('Wait for itinerary completion or manual closing')['wait_template']
        world = World(['waiting_for_others', 'on_approach'])
        seen = []
        old_states = world.states
        world.states = lambda entity: (seen.append(entity), old_states(entity))[1]
        self.assertFalse(world.render(template))
        self.assertEqual(seen, world.sensors)
        world.records[world.sensors[1]]['status'] = None
        self.assertTrue(world.render(template))


if __name__ == '__main__':
    unittest.main()
