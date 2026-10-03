"""Worked example: fictional Guam community-workshop supply orders.
Separate worked dataset. No staff reference imports.
"""
import csv
from decimal import Decimal, InvalidOperation
from io import StringIO

DEMO_CSV = """order_id,item,qty,unit_price,status
D1, Ribbon ,2,1.50, PAID 
D2,Bags,3,0.80,unpaid
D3,Ties,0,0.25,paid
D4,Rope,2,bad,paid
D5,Ribbon,1,1.50,paid
D6,Ties,4,0.25,paid
"""

reader = csv.reader(StringIO(DEMO_CSV))
headers = next(reader)
rows = []
for fields in reader:
    rows.append(dict(zip(headers, fields)))
print(headers)
print(f"item={rows[0]['item']!r} qty={rows[0]['qty']!r}")
