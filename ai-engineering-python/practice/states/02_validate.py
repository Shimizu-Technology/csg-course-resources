import json

def validate_supply(raw):
    value = json.loads(raw) if isinstance(raw, str) else raw
    if not isinstance(value, dict) or set(value) != {'item', 'quantity'}:
        raise ValueError('Expected item and quantity only')
    if not isinstance(value['item'], str) or value['item'] not in {'paper', 'marker'}:
        raise ValueError('Unknown item')
    if type(value['quantity']) is not int or not 1 <= value['quantity'] <= 10:
        raise ValueError('Quantity must be a whole number from 1 to 10')
    return value

print(validate_supply('{"item":"paper","quantity":3}'))
try:
    validate_supply({'item':'paper','quantity':True})
except ValueError as error:
    print('Repair:', error)
