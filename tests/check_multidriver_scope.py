"""Prove changes outside the coordination block are limited to metadata."""
from pathlib import Path
import subprocess,copy
from test_gate_multidriver import Loader,find
import yaml
p=Path(__file__).resolve().parents[1]
before=yaml.load(subprocess.run(['git','show','ce6aae5:Blueprints/Automatic-Gate/automatic-gate.yaml'],cwd=p,capture_output=True,check=True).stdout.decode('utf-8'),Loader=Loader)
after=yaml.load((p/'Blueprints/Automatic-Gate/automatic-gate.yaml').read_text(encoding='utf-8'),Loader=Loader)
for d in [before,after]:
    d['blueprint']['description']=None
    n=find(d,'If someone is currently approaching or leaving');n['then']=None
    find(d,'Get other drivers near the gate')['variables']['drivers_near_gate']=None
def differences(a,b,path=''):
    if type(a)!=type(b):return [path]
    if isinstance(a,dict):return [p for k in a.keys()|b.keys() for p in (differences(a[k],b[k],path+'/'+str(k)) if k in a and k in b else [path+'/'+str(k)])]
    if isinstance(a,list):return [path] if len(a)!=len(b) else [p for i,(x,y) in enumerate(zip(a,b)) for p in differences(x,y,path+'/'+str(i))]
    return [] if a==b else [path]
assert before==after,differences(before,after)
print('Scope verified: all other opening/closing branches, #314, #319 and #321 unchanged.')
