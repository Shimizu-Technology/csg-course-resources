import json
raw = '{"item": "paper", "quantity": 3}'
request = json.loads(raw)
print(request['item'])
print(request['quantity'] + 2)
print(json.dumps(request, sort_keys=True))
