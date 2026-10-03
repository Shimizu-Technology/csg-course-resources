CASES = [
    {'id':'p1','text':'paper please','expected':'paper'},
    {'id':'p2','text':'a marker please','expected':'marker'},
    {'id':'p3','text':'a sheet please','expected':'paper'},
]

def predict(text):
    return 'paper' if 'paper' in text else 'marker'

def evaluate(cases, predict):
    if not cases:
        raise ValueError('Need labeled cases')
    rows = []
    for case in cases:
        answer = predict(case['text'])
        rows.append({'id':case['id'], 'match':answer == case['expected']})
    return {'count':len(rows), 'matches':sum(row['match'] for row in rows), 'failures':[row['id'] for row in rows if not row['match']]}

print('DETERMINISTIC SUPPLY FIXTURE — NOT AI')
print(evaluate(CASES, predict))
