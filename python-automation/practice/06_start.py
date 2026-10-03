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

REQUIRED = {"order_id", "item", "qty", "unit_price", "status"}


def parse_demo(source):
    reader = csv.reader(StringIO(source), strict=True)
    try:
        headers = next(reader, None)
    except csv.Error as error:
        raise ValueError(f"line {reader.line_num}: malformed CSV: {error}") from error
    if not headers or not REQUIRED.issubset(headers) or len(headers) != len(set(headers)):
        raise ValueError("Required headers must appear once")
    valid, errors, skipped, seen = [], [], 0, set()
    previous_line = reader.line_num
    while True:
        source_line = previous_line + 1
        try:
            fields = next(reader)
        except StopIteration:
            break
        except csv.Error as error:
            raise ValueError(f"line {source_line}: malformed CSV: {error}") from error
        previous_line = reader.line_num
        if not fields:
            continue
        if len(fields) != len(headers):
            errors.append(f"line {source_line}: wrong field count")
            continue
        row = dict(zip(headers, fields))
        status = row["status"].strip().lower()
        if status == "unpaid":
            skipped += 1
            continue
        if status != "paid":
            errors.append(f"line {source_line}: unknown status")
            continue
        order_id, item = row["order_id"].strip(), row["item"].strip()
        if not order_id or not item:
            errors.append(f"line {source_line}: ID and item required")
            continue
        if order_id in seen:
            errors.append(f"line {source_line}: duplicate {order_id}")
            continue
        try:
            qty, price = int(row["qty"]), Decimal(row["unit_price"])
        except (ValueError, InvalidOperation):
            errors.append(f"line {source_line}: invalid quantity or price")
            continue
        if qty <= 0 or not price.is_finite() or price < 0:
            errors.append(f"line {source_line}: quantity must be positive and price nonnegative")
            continue
        if price.as_tuple().exponent < -2:
            errors.append(f"line {source_line}: price needs at most two decimal places")
            continue
        seen.add(order_id)
        valid.append({"order_id": order_id, "item": item, "amount": qty * price})
    return valid, errors, skipped


valid, errors, skipped = parse_demo(DEMO_CSV)
print(f"valid={len(valid)} skipped={skipped} errors={len(errors)}")
for error in errors:
    print(error)
