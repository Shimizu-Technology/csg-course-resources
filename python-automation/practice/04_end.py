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

reader = csv.reader(StringIO(DEMO_CSV), strict=True)
headers = next(reader)
previous_line = reader.line_num
for fields in reader:
    source_line = previous_line + 1
    previous_line = reader.line_num
    row = dict(zip(headers, fields))
    if row["status"].strip().lower() != "paid":
        continue
    try:
        qty = int(row["qty"])
        price = Decimal(row["unit_price"])
    except (ValueError, InvalidOperation):
        print(f"line {source_line}: invalid quantity or price")
        continue
    if qty <= 0 or not price.is_finite() or price < 0:
        print(f"line {source_line}: quantity must be positive and price nonnegative")
        continue
    print(row["item"].strip(), f"{qty * price:.2f}")
