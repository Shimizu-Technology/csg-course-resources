"""Learner starter. Paste the fictional CSV from orders.csv into RAW_CSV."""

import csv
from decimal import Decimal
from io import StringIO

RAW_CSV = """order_id,item,qty,unit_price,status
A1,Notebook,2,4.50,paid
A2,Pen,3,1.25,paid
A3,Marker,1,2.00,unpaid
A4,Paper,0,5.00,paid
A5,Clip,2,bad,paid
A6,Notebook,1,4.50,paid
A7,Pen,2,1.25,paid
"""


def parse_orders(source):
    """Return valid paid records, error messages, and unpaid count."""
    # TODO: verify headers and each row. Keep line numbers in errors.
    raise NotImplementedError


def summarize(valid):
    """Return item totals sorted by item name."""
    # TODO: use Decimal amounts to add money without float rounding.
    raise NotImplementedError


def make_report(source):
    """Return a CSV report and counts; see project rubric."""
    # TODO: call parse_orders and summarize, then use csv.writer.
    raise NotImplementedError


if __name__ == "__main__":
    print(make_report(RAW_CSV))
