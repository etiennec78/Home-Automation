"""Offline tests of the message template extracted from the blueprint.
Requires PyYAML and Jinja2; does not exercise notification delivery.
"""
from pathlib import Path
from types import SimpleNamespace as NS
import unittest
import yaml
from jinja2 import Environment, StrictUndefined
class Loader(yaml.SafeLoader): pass
Loader.add_constructor('!input', lambda loader,node: loader.construct_scalar(node))
DOC=yaml.load((Path(__file__).resolve().parents[1]/'Blueprints/Gate-Alerts/gate-alerts.yaml').read_text(encoding='utf-8'),Loader=Loader)
BRANCH=next(x for x in DOC['actions'] if x.get('alias')=='If gate paused or fully open, and supporting state transitions')
TEMPLATE=Environment(undefined=StrictUndefined).from_string(BRANCH['else'][0]['variables']['title_id'])
class MessageTests(unittest.TestCase):
    def test_confirmed_closure_vs_command(self):
        for domain,old,new,expected in [('binary_sensor','on','off','closed'),('cover','open','closed','closed'),('cover','opening','closed','closed'),('cover','open','closing','close'),('switch','on','off','close'),('input_boolean','on','off','close')]:
            with self.subTest(domain=domain,old=old,new=new):
                self.assertEqual(TEMPLATE.render(gate=domain+'.gate',trigger=NS(id='close',from_state=NS(state=old),to_state=NS(state=new)),notification_delay=0).strip(),expected)
    def test_other_messages_unchanged(self):
        for event,delay,expected in [('open',0,'open'),('open',1,'left_open'),('error',0,'error'),('offline',0,'offline'),('online',0,'online')]:
            with self.subTest(event=event):
                self.assertEqual(TEMPLATE.render(gate='cover.gate',trigger=NS(id=event),notification_delay=delay).strip(),expected)
if __name__=='__main__': unittest.main()
