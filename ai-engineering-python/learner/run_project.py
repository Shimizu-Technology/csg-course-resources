"""Provided runner wiring only. Your six student_triage functions remain TODO."""
import argparse
import hashlib
import json
import os
import getpass
import sys
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'project'))
from client import request_triage
from student_triage import evaluate_cases, summarize_attempts

parser=argparse.ArgumentParser()
parser.add_argument('--mode',choices=['fixture','live'],required=True)
parser.add_argument('--version',choices=['v1','v2'],required=True)
parser.add_argument('--cases',type=Path,default=Path(__file__).resolve().parents[1]/'project/heldout.json')
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args()
if args.output.exists():
    raise ValueError('Choose a new output filename; preserve earlier evidence')
if args.mode=='live':
    os.environ['CSG_TRIAGE_URL']=os.environ.get('CSG_TRIAGE_URL') or getpass.getpass('Private CSG HTTPS endpoint (hidden): ')
    os.environ['CSG_COURSE_TOKEN']=os.environ.get('CSG_COURSE_TOKEN') or getpass.getpass('Individual course token (hidden): ')
    input('Private entry complete. Resume recording if needed, then press Enter: ')
raw=args.cases.read_bytes();cases=json.loads(raw);attempts=[]

def observe(message):
    if args.mode=='fixture':
        # Deliberately fixed answer for plumbing tests, not a classifier or model.
        response={'status':'proposed','review_required':True,'result':{'category':'lesson','urgency':'routine','reason':'Fixed offline test value, not model inference.'},'metrics':{'model':'FIXED_OFFLINE_VALUE_NOT_AI','prompt_version':args.version,'latency_ms':0,'input_tokens':0,'output_tokens':0,'estimated_usd':0}}
    else:
        response=request_triage(message,args.version)
    attempts.append({'status':response['status'],'metrics':response.get('metrics',{})})
    return response

report={'mode':args.mode,'evidence_label':'FIXED OFFLINE VALUE — NOT MODEL ACCURACY' if args.mode=='fixture' else 'ACTUAL CSG ENDPOINT OBSERVATIONS','prompt_version':args.version,'cases_sha256':hashlib.sha256(raw).hexdigest(),'observed_at_utc':datetime.now(timezone.utc).isoformat() if args.mode=='live' else None,'evaluation':evaluate_cases(cases,observe),'metrics':summarize_attempts(attempts),'attempts':attempts}
args.output.parent.mkdir(parents=True,exist_ok=True)
with args.output.open('x') as handle:json.dump(report,handle,indent=2);handle.write('\n')
print(json.dumps(report,indent=2))
