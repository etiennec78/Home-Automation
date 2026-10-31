"""Offline regression tests rendering the templates extracted from the blueprint.

These checks are not Home Assistant schema validation or real notification tests.
Run with a Python providing PyYAML and Jinja2 (Device Builder on this laptop).
"""
from pathlib import Path
from types import SimpleNamespace as NS
import os
import unittest
import yaml
from jinja2 import Environment

PATH=Path(os.environ.get('GATE_BLUEPRINT',str(Path(__file__).resolve().parents[1]/'Blueprints/Gate-Alerts/gate-alerts.yaml')))
class Loader(yaml.SafeLoader): pass
Loader.add_constructor('!input',lambda loader,node: {'input':loader.construct_scalar(node)})
DOC=yaml.load(PATH.read_text(encoding='utf-8'),Loader=Loader)
ENV=Environment()
def find(alias):
    def walk(value):
        if isinstance(value,dict):
            if value.get('alias')==alias:return value
            for child in value.values():
                result=walk(child)
                if result is not None:return result
        elif isinstance(value,list):
            for child in value:
                result=walk(child)
                if result is not None:return result
    result=walk(DOC)
    assert result is not None,alias
    return result

def context(domain='binary_sensor',old='on',new='off',retain=False,current=None,stamp=1):
    gate=domain+'.gate'
    current=new if current is None else current
    current_state=NS(state=current,last_changed=stamp)
    return dict(gate=gate,retain_closed_confirmation=retain,
        trigger=NS(id='close',from_state=NS(state=old),to_state=NS(state=new,last_changed=1)),
        states={gate:current_state},is_state=lambda entity,wanted: current in wanted if isinstance(wanted,list) else current==wanted,
        notification_delay=0,MAX_INT=2147483647)

def render(template,ctx):return ENV.from_string(template).render(**ctx).strip()
def classified(ctx):
    ctx['is_closed_confirmation']=render(DOC['variables']['is_closed_confirmation'],ctx)=='True'
    ctx['completion_update']=render(DOC['variables']['completion_update'],ctx)=='True'
    return ctx

class GateAlertsTests(unittest.TestCase):
    def test_yaml_root_and_upstream_inputs(self):
        self.assertIsInstance(DOC['actions'],list)
        self.assertEqual(set(DOC['blueprint']['input']['extra_actions']['input']),{'extra_actions'})
        inputs=DOC['blueprint']['input']['notification_settings']['input']
        self.assertFalse(inputs['retain_closed_confirmation']['default'])
        self.assertNotIn('notification_lifetime',inputs)

    def test_physical_closure_classification(self):
        for domain,old,new,expected in [
            ('binary_sensor','on','off',True),('binary_sensor','off','on',False),
            ('cover','open','closed',True),('cover','closing','closed',True),
            ('cover','opening','closed',True),('cover','open','closing',False),
            ('switch','on','off',False),('input_boolean','on','off',False)]:
            with self.subTest(domain=domain,old=old,new=new):
                self.assertEqual(classified(context(domain,old,new))['is_closed_confirmation'],expected)

    def test_non_state_triggers_do_not_become_confirmation(self):
        for kind in ['error','offline','online','blueprint_enabled','closed_confirmation_cleanup']:
            ctx=context();ctx['trigger']=NS(id=kind)
            self.assertFalse(classified(ctx)['is_closed_confirmation'])
        ctx=context();ctx['trigger']=NS(platform=None)
        self.assertFalse(classified(ctx)['is_closed_confirmation'])

    def test_confirmation_messages_vs_command(self):
        template=find('Set notification ids')['variables']['title_id']
        # There are two identically named blocks; the main else branch owns classification.
        branch=find('If gate paused or fully open, and supporting state transitions')
        template=branch['else'][0]['variables']['title_id']
        for domain,old,new,expected in [('binary_sensor','on','off','closed'),('cover','closing','closed','closed'),('switch','on','off','close'),('input_boolean','on','off','close')]:
            with self.subTest(domain=domain):self.assertEqual(render(template,classified(context(domain,old,new))),expected)

    def test_default_cover_completion_is_suppressed(self):
        template=DOC['conditions'][0]['value_template']
        self.assertEqual(render(template,context('cover','closing','closed')), 'False')
        self.assertEqual(render(template,context('cover','closing','closed',True)), 'True')
        self.assertEqual(render(template,context()),'True')

    def test_ignore_restore_transitions(self):
        for item in DOC['triggers']:
            if item['id'] in ['open','close']:
                self.assertEqual(set(item['not_from']),{'unknown','unavailable'})

    def test_obsolete_confirmation_is_not_sent(self):
        template=find('Reject an obsolete closure before sending its confirmation')['value_template']
        for current,stamp,expected in [('off',1,True),('on',2,False),('off',3,False),('unavailable',2,False)]:
            ctx=classified(context(current=current,stamp=stamp))
            self.assertEqual(render(template,ctx),str(expected))

    def test_lifetime_and_immediate_reopening(self):
        flow=find('Manage the physical closure confirmation independently of movement alerts')['then']
        for retain,expected in [(False,'30'),(True,'2147483647')]:
            self.assertEqual(render(flow[0]['timeout'],context(retain=retain)),expected)
        for current in ['on','unknown','unavailable']:
            self.assertEqual(render(flow[0]['wait_template'],context(current=current,stamp=2)),'True')
        self.assertEqual(render(flow[0]['wait_template'],context()),'False')

    def test_old_run_cannot_clear_new_closed_generation(self):
        template=find('An older execution must not clear a newer closure confirmation')['value_template']
        self.assertEqual(render(template,context(stamp=3)),'False')
        self.assertEqual(render(template,context()),'True')
        self.assertEqual(render(template,context(current='on',stamp=2)),'True')

    def test_cleanup_runs_without_open_notification_selection(self):
        cleanup=next(t for t in DOC['triggers'] if t['id']=='closed_confirmation_cleanup')
        self.assertIn('on',cleanup['to']);self.assertIn('unavailable',cleanup['to'])
        self.assertEqual(render(cleanup['enabled'],{'gate':'binary_sensor.test'}),'True')
        self.assertEqual(render(cleanup['enabled'],{'gate':'cover.test'}),'True')
        self.assertEqual(render(cleanup['enabled'],{'gate':'switch.test'}),'False')
        self.assertNotIn('notification_type',cleanup['enabled'])

    def test_confirmation_tag_is_distinct_and_scoped_to_automation(self):
        a=render(DOC['variables']['closed_confirmation_tag'],{'this':NS(attributes=NS(id='first'))})
        b=render(DOC['variables']['closed_confirmation_tag'],{'this':NS(attributes=NS(id='second'))})
        self.assertNotEqual(a,b);self.assertEqual(a,'gate-closed-first')
        flow=find('Physical closure replaces any previous movement alert')['then']
        self.assertEqual(flow[-1]['variables']['notification_tag'],'{{ closed_confirmation_tag }}')

    def test_completion_does_not_double_callbacks(self):
        ctx=classified(context('cover','closing','closed',True))
        self.assertTrue(ctx['completion_update'])
        extra=find('Exec user extra actions')
        self.assertEqual(render(extra['if']['value_template'],ctx),'False')
        ctx=classified(context())
        self.assertEqual(render(extra['if']['value_template'],ctx),'True')
        ctx=context('cover','closing','closed',True);ctx['notification_delay']=1
        self.assertFalse(classified(ctx)['completion_update'])

    def test_confirmation_can_be_dismissed(self):
        branch=find('If gate paused or fully open, and supporting state transitions')
        parallel=next(step['parallel'] for step in branch['else'] if 'parallel' in step)
        notify=parallel[0]['repeat']['sequence'][0]['variables']['notification_data']
        ctx=classified(context(retain=True))
        self.assertEqual(render(notify['sticky'],ctx),'False')
        self.assertEqual(render(notify['persistent'],ctx),'False')
        self.assertEqual(render(notify['timeout'],ctx),'2147483647')

if __name__=='__main__':unittest.main(verbosity=2)
