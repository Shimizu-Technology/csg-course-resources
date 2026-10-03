# Python Automation

Learner preparation guide. Use the matching course in CSG Learn for recordings, submissions and questions. Recordings and admissions are pending; these files alone do not grant access. All practice data is fictional.

## Start here: environment and submission

Required

Create a dedicated Hafa Python worked project. Run `print("Automation starts with a repeatable input")`, change input to CSV, rerun, and submit changed source/output in Learn. Local Python and GitHub are optional. Entry skills: variables, conditions, loops, lists, dictionaries, functions, reading an error. Placement: group three item/amount dictionaries and explain an invalid row. The fictional Ribbon/Ties worked export differs from the independently assessed Notebook/Pen export. Predict, run, change, and save exact code/output; a mutable link alone is not a review copy. Use your enrollment's question route with the smallest fictional input and exact error.

## Lesson 1: Read a CSV without splitting commas yourself

Required

**Outcome:** Read a CSV without splitting commas yourself. Use the separate worked project and predict before Run.

We are helping a fictional community workshop in Guam check a supply-order export. Ribbon, bags, ties, and rope are teaching data. They are not a real shop's orders. Our job is to turn repeated manual checking into a program we can run again on the same input. Today we will only read the data. We will not trust or total it yet.

Look at the header: order ID, item, quantity, unit price, and status. Pause for ten seconds. Which two fields would you multiply to get a line amount? What do you think Python will call the quantity when it reads the file?

`StringIO` gives Python a file-like reader over text already in the browser. It does not open a file on your laptop. `csv.reader` understands CSV quoting. Splitting on every comma ourselves would break an item such as ribbon, blue inside quotes. `next(reader)` takes the first row as the list of column names. The remaining loop reads each data row.

`zip(headers, fields)` pairs the first header with the first value, then the next header with the next value. `dict` turns those pairs into a dictionary. Now we can use the name `qty` instead of remembering that quantity is column number three. We append each dictionary to `rows` so we can inspect it after reading.

The output contains the five headers in file order. The first item still has spaces around Ribbon, and the quantity is the string two. The exclamation mark r in our f-string displays the value's representation, so the quotes and spaces are visible. Nothing was cleaned automatically. That is useful: we can see what arrived before choosing a rule.

For E1 and E2, use your separate final-project fixture. Print its headers, then the first item's name and quantity. Explain why quantity is text. Save your exact code and output in Learn. Our worked file teaches the method; your submission uses the different Notebook and Pen file.

**Worked ending code, on different data from assessment:**
```python
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
```


## E1: find columns

Required

On the assessed fixture, print the five header names in file order. Submit code and output.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## E2: row lookup

Required

Print its first item and quantity: Notebook 2. Explain why quantity initially arrives as text.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Lesson 2: Normalize text, then route expected statuses

Required

**Outcome:** Normalize text, then route expected statuses. Use the separate worked project and predict before Run.

Two equivalent values can look different in an export. This item has spaces at the edges, and its status has uppercase letters. We need a deliberate rule before comparing them. I will remove edge spaces from item names. For status only, I will also use lowercase. I will not lowercase the item, because we have not chosen to merge differently capitalized item names.

Pause for ten seconds. What should `strip()` return for this item? What should `strip().lower()` return for this status?

It prints Ribbon and paid. `strip` removes spaces at the edges; it does not remove a space inside an item name. `lower` makes this status comparable with the string paid. We call those methods on each incoming status, rather than assuming only the first row is messy.

Now look at the loop. `skipped` starts at zero and `paid` starts as an empty list. When status is unpaid, we add one to the skipped count. `continue` goes to the next row, so this row does not fall through into the paid list. When it is paid, we append it. Those are route decisions, not money validation.

We routed five paid rows and skipped one unpaid row. That does not mean five rows are valid. The zero quantity and bad price are still in those five. We will validate them later. Unpaid is an expected state in this report, so skipping it is different from an error. An unknown status will need an error instead of quietly becoming paid.

For E3, show the padded Pen becoming Pen and PAID becoming paid. For E4, count the one unpaid row in your assessed fixture. Include the change in your code and explain the difference between skipping an expected unpaid record and rejecting a broken paid record.

**Worked ending code, on different data from assessment:**
```python
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
first_item = rows[0]["item"].strip()
first_status = rows[0]["status"].strip().lower()
print(first_item, first_status)
skipped = 0
paid = []
for row in rows:
    status = row["status"].strip().lower()
    if status == "unpaid":
        skipped += 1
        continue
    if status == "paid":
        paid.append(row)
print(f"routed paid={len(paid)} skipped={skipped}")
```


## E3: normalize

Required

Show padded " Pen " becoming Pen and "PAID" becoming paid with strip/lower. Preserve spaces inside a name and do not lowercase the item.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## E4: route

Required

Count its unpaid rows after status normalization: 1. Explain intentional skip versus invalid paid row.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Lesson 3: Convert quantity and price, and state the boundary

Required

**Outcome:** Convert quantity and price, and state the boundary. Use the separate worked project and predict before Run.

Our first worked order has quantity two and unit price one dollar fifty. Both arrived as text. Pause for ten seconds: calculate its line amount on paper before the program does it.

`int` converts the whole-number quantity. `Decimal` receives the price string directly. We do not turn it into a float first, because that could introduce binary rounding before Decimal sees it. Multiplying an integer by this Decimal produces a Decimal amount. Formatting with dot two f displays two decimal places; it does not replace the value we use for later addition.

The first amount is three dollars. The third row has quantity zero. For this fictional report, an order quantity must be a positive whole number. I will convert its zero and test less than or equal to zero. The message tells us that it violates our chosen rule.

That rule is different from the price rule. A free item with a price of zero can be valid. A negative price is rejected. We do not use a shortcut that treats every zero as missing. The value's meaning determines its boundary.

The good conversion works, and the zero-quantity check prints its message. This is not yet a safe loop: converting the word bad would raise an exception. We will catch that specific conversion failure next.

For Checkpoint A, use the supplied new Pencil row: three units at forty cents. Produce one dollar twenty using Decimal, reject a zero quantity, and explain why the input string goes straight into Decimal. You may look back at this worked method, but write and run the checkpoint on its different row yourself.

**Worked ending code, on different data from assessment:**
```python
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
row = rows[0]
qty = int(row["qty"])
price = Decimal(row["unit_price"])
print(row["item"].strip(), f"{qty * price:.2f}")
zero_qty = int(rows[2]["qty"])
if zero_qty <= 0:
    print("quantity must be positive")
```


## Checkpoint A: transfer

Required

Given A9, Pencil, 3, 0.40, paid, write a rerunnable program producing Pencil 1.20 using an integer and Decimal. Reject quantity zero, allow price zero, and explain why the original price string goes directly into Decimal. Submit source, both boundary results and reasoning.

## Lesson 4: Keep processing after one bad row, with physical line context

Required

**Outcome:** Keep processing after one bad row, with physical line context. Use the separate worked project and predict before Run.

We need a loop that can reject a bad paid row and still process the next good one. Before typing, find Rope in the fixture. Its price is bad. Predict what an unhandled Decimal conversion would do.

We use strict CSV reading. `reader.line_num` counts physical source lines that the CSV reader has consumed. I save that position before reading the next record. Its start line is the previous position plus one. This is more accurate than counting records: a quoted CSV item can occupy two physical lines. After the reader consumes the row, we update the previous position for the next one.

This early worked loop assumes the expected five fields. In the next clip, we will validate field counts before making the dictionary. Here we normalize the status and skip anything that is not paid so we can concentrate on numeric validation.

Only the conversions sit inside `try`. `ValueError` covers an invalid integer, and `InvalidOperation` covers an invalid Decimal string. We print the source start line and continue. We do not use a blank except that would also hide unrelated programming mistakes.

Ribbon three dollars prints first. Line four has zero quantity, so it produces a boundary error. Line five has bad price text, so it produces the conversion error. Then the later Ribbon and Ties rows still print. An error in one record did not erase the rest of the export.

The boundary also rejects an infinite or not-a-number Decimal and a negative price. We ask whether it is finite before comparing it with zero. A zero price remains valid. The format remains two decimal places.

For E5, handle an invalid price with a readable message. For E6, reject quantity zero and a negative price. Save the input that caused the error alongside your code and output. That gives an instructor a small reproducible problem rather than a screenshot without its source.

**Worked ending code, on different data from assessment:**
```python
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
```


## E5: safe conversion

Required

Convert "bad" with Decimal inside a specific InvalidOperation handler. Print invalid price without a traceback.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## E6: boundaries

Required

Reject quantity zero and a negative price, keep zero price valid. Identify zero-quantity fixture line5, then add a fresh A8 negative-price row in a private copy and show its line9 rejection.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Lesson 5: Refactor the loop into a parser with an explicit return contract

Required

**Outcome:** Refactor the loop into a parser with an explicit return contract. Use the separate worked project and predict before Run.

The loop now works on this small example, but printing is not a reusable interface. The next part of our report needs records, errors, and a skipped count as values. I will put the logic into `parse_demo(source)`. The parameter lets us pass another text fixture later. The function returns three values in a fixed order: valid records, errors, then unpaid count.

First, required headers. `REQUIRED` is a set of the names we need. `issubset` asks whether every required name appears in the incoming header. Comparing the header length with the length of its set detects a duplicate name. A repeated header would make dictionary mapping ambiguous, so we reject it. `next(reader, None)` lets a completely empty source become a deliberate header error rather than an accidental StopIteration.

The function creates its own fresh lists, count, and seen-ID set on every call. Nothing from the previous run leaks into this one. The while loop reads one record at a time. StopIteration means we reached the end and should break. A CSV quoting error rejects this source with a ValueError. We distinguish a malformed file structure from a recoverable bad row.

We record the physical start line before asking for the next row. A blank physical row has no fields; it is ignored after we update the physical position. A row with the wrong number of fields adds an error and continues. Only then do we zip its fields with the verified headers. That prevents missing or extra fields from being silently mislabelled.

Unpaid still increments the intentional skip count. Unknown status adds an error. A paid record must have an ID and an item after trimming. The seen set contains only IDs already accepted. If this ID is already in it, we report a duplicate and do not add its amount again. We add an ID to the set only after every check passes, so an invalid first attempt does not block a corrected row later.

The conversions and finite/nonnegative checks are the same method we just built. The exponent check enforces our input-format rule: unit price may have at most two digits after the decimal point. Even one point five zero zero violates that format, although it represents the same number as one point five. We could choose another rule for another workflow; here it is part of the contract.

An accepted dictionary contains the ID, cleaned item, and Decimal amount. It does not carry an unexplained raw price into the next stage. The return sits outside the loop, so all rows have been considered before we hand back the three values.

Six data records: one unpaid, two invalid paid, so we expect three accepted records. Run it. We see valid three, skipped one, errors two, with source lines four and five. Our parser exposes errors to the caller instead of printing inside itself. E7 asks you to apply this contract to the different assessed export. Do not import a staff function. Your own parser is the code we will review.

**Worked ending code, on different data from assessment:**
```python
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
```


## E7: parser

Required

Implement parse_orders(source), returning (valid, errors, skipped). Accepted records contain order_id, cleaned item and Decimal amount. Validate structure before mapping fields. Assessed counts 4/2/1 with physical errors lines 5/6.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Lesson 6: Group Decimal amounts by the cleaned item

Required

**Outcome:** Group Decimal amounts by the cleaned item. Use the separate worked project and predict before Run.

We now have accepted amounts, so grouping no longer needs to decide whether a raw row is paid or valid. One function has that responsibility already. The next function accepts the validated records and produces one total per cleaned item.

Pause for ten seconds. Our worked Ribbon amounts are three dollars and one dollar fifty. Ties is one dollar. Write the two expected grouped totals before typing.

`totals` begins as an empty dictionary. For each record, the cleaned item is the key. `totals.get(item, Decimal("0.00"))` gives the previous total if the item exists, or a Decimal zero if this is its first record. We add the record's amount and store the result under the same key. On Ribbon's second occurrence, get returns three dollars, so the new value is four dollars fifty. It does not create a second Ribbon row.

We return a dictionary built from sorted item-total pairs. Sorting here gives the report a stable alphabetic order even if the export's input order changes. We have not invented a way to merge differently capitalized names; Ribbon and RIBBON would still be different keys. That is one assumption you should name in a final explanation.

Ribbon is four fifty and Ties is one dollar. We ignored the unused error list and skip count with underscore names for this narrow demonstration. They still exist; the final workflow will keep them.

For E8, call your own assessed parser and group its accepted Decimal amounts. Your Notebook total is thirteen fifty and Pen is six twenty-five. Checkpoint B asks for those grouped totals together with the four-valid, one-skipped, two-error counts. If an amount is wrong, inspect one accepted record before changing the addition. That separates a parser mistake from a grouping mistake.

**Worked ending code, on different data from assessment:**
```python
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


def group_items(records):
    totals = {}
    for record in records:
        item = record["item"]
        totals[item] = totals.get(item, Decimal("0.00")) + record["amount"]
    return dict(sorted(totals.items()))


valid, _, _ = parse_demo(DEMO_CSV)
for item, amount in group_items(valid).items():
    print(item, f"{amount:.2f}")
```


## E8: group

Required

Total accepted Decimal amounts by cleaned item and sort: Notebook 13.50, Pen 6.25. Explain default zero and the running dictionary update.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Checkpoint B: integration

Required

Run your own parser/grouping on the independent fixture: four accepted paid rows, one unpaid skip, two errors with physical lines five and six, Notebook 13.50 and Pen 6.25. Submit exact source/output and explain why the invalid price did not stop later good rows.

## Lesson 7: Write actual CSV text with the standard writer

Required

**Outcome:** Write actual CSV text with the standard writer. Use the separate worked project and predict before Run.

We have totals as values. Now we need a repeatable output that another person can copy. I will write CSV text with a header and a stable row for each item. This worked browser project produces text; it does not automatically download a file to your computer.

Pause for ten seconds. Which item should come first, and what should the header say?

`StringIO` is now our output buffer instead of our input reader. `csv.writer` writes correctly quoted CSV fields into that buffer. The line terminator is explicitly newline, so our expected output is stable across the course's checking environments. `writerow` writes the two header fields. Then we iterate through the sorted dictionary's items. The amount is formatted to two decimal places only for display; the arithmetic has already used Decimal values.

If an item contains a comma, the writer can quote it. We do not build a row by joining an item and amount with a comma ourselves. That would produce an extra column for an item such as ribbon, blue. We return `output.getvalue()`, which is the complete CSV string, including its final newline.

The output is item comma total, Ribbon comma four point five zero, and Ties comma one point zero zero. `end=""` in print prevents print from adding another blank line to a string that already ends with newline.

E9 asks for the same output shape on your assessed items, with the trailing newline. In E10, add the supplied Eraser row in your own copy. It sorts before Notebook and raises that fixture's total to twenty fifty. Use the writer for escaping and sorting, then paste the CSV text and the code that created it into Learn. A browser Share link is optional context, not the saved review copy.

**Worked ending code, on different data from assessment:**
```python
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


def group_items(records):
    totals = {}
    for record in records:
        item = record["item"]
        totals[item] = totals.get(item, Decimal("0.00")) + record["amount"]
    return dict(sorted(totals.items()))


def write_totals(totals):
    output = StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["item", "total"])
    for item, amount in totals.items():
        writer.writerow([item, f"{amount:.2f}"])
    return output.getvalue()


valid, _, _ = parse_demo(DEMO_CSV)
print(write_totals(group_items(valid)), end="")
```


## E9: writer

Required

Emit item, total header and alphabetic rows with csv.writer, two displayed decimal places and a trailing newline. Submit generated text and exact source.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## E10: reorder

Required

In a private copy add A8, Eraser, 1, 0.75, paid. Eraser sorts first and grand total becomes 20.50. Leave the shared fixture unchanged.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Lesson 8: Compose the workflow and keep useful evidence

Required

**Outcome:** Compose the workflow and keep useful evidence. Use the separate worked project and predict before Run.

We can now connect functions whose jobs are clear. The parser returns accepted rows, errors, and intentional skips. Grouping returns sorted totals. The writer returns CSV text. A small coordinating function calls each one and keeps the evidence we need to explain the result.

Pause for ten seconds. What should happen to the two errors when we generate a successful item report? They should remain visible; successful output does not make invalid input disappear.

`build_demo_report` calls the parser once, then groups that returned valid list. The dictionary we return contains CSV text, valid count, unpaid skip count, errors, and total. The total is the sum of the grouped values. We provide Decimal zero as sum's start value, so even an empty result has a Decimal total instead of changing its type to integer zero.

The caller decides how to present that dictionary. We print CSV text, all counts, grand total, and every error message. Functions still return values; only this bottom block displays them. That is why we can reuse them in a test or an optional extension without scraping terminal text.

The report contains Ribbon four fifty and Ties one dollar, a total of five fifty. Three accepted records, one intentional skip, and two errors are all accounted for. We can run this same input again and expect exactly this result. Nothing writes a permanent file or sends a request.

Now work independently on `automation_starter.py`. It has the different Notebook and Pen fixture and three unfinished functions. Use the return keys stated in its contract: report_csv, valid, skipped, errors, and grand_total. Adapt the ideas rather than importing `parse_demo` or a staff solution. Submit your source, CSV, counts, error messages, and explanation. In the next clip, we will test small counterexamples before calling any automation reliable.

**Worked ending code, on different data from assessment:**
```python
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


def group_items(records):
    totals = {}
    for record in records:
        item = record["item"]
        totals[item] = totals.get(item, Decimal("0.00")) + record["amount"]
    return dict(sorted(totals.items()))


def write_totals(totals):
    output = StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["item", "total"])
    for item, amount in totals.items():
        writer.writerow([item, f"{amount:.2f}"])
    return output.getvalue()


def build_demo_report(source):
    valid, errors, skipped = parse_demo(source)
    totals = group_items(valid)
    return {"csv": write_totals(totals), "valid": len(valid),
            "skipped": skipped, "errors": errors,
            "total": sum(totals.values(), Decimal("0.00"))}


result = build_demo_report(DEMO_CSV)
print(result["csv"], end="")
print(f"valid={result['valid']} skipped={result['skipped']} errors={len(result['errors'])}")
print(f"Grand total: {result['total']:.2f}")
for error in result["errors"]:
    print(error)
```


## Independent final project

Required

Independently complete automation_starter.py on the supplied fictional assessed export. Do not import a staff key or submit the unchanged worked demo. parse_orders(source) returns (valid, errors, skipped); accepted records contain order_id, cleaned item and Decimal amount. summarize returns alphabetic Decimal totals. make_report returns report_csv, valid, skipped, errors and Decimal grand_total. Validate unique required headers, field count, known status, required ID/item, repeated accepted IDs, positive whole quantity, finite nonnegative price and at most two decimal places. Skip unpaid intentionally, ignore blank physical lines, retain each CSV record's physical start. Invalid header/CSV structure raises ValueError; row errors retain other good data.

Sample report:
```text
item,total
Notebook,13.50
Pen,6.25
```
Keep its trailing newline. Four accepted, one skipped, two errors, grand total 19.75. Submit source, input, report, counts, all errors and a short explanation. Demonstrate original, header-only, duplicate A1, missing-header rejection and normal rerun after a change. Finish after Lesson 9's edge practice; this project opens earlier so you can start.

10-point rubric: 2 input/header/status; 2 recoverable row validation with lines; 2 Decimal/stable CSV; 2 original plus three edge cases; 1 readable functions; 1 limits/improvement. State case-sensitive grouping and deliberate skip/reject rules. Teaching amounts are not financial records. The optional extension does not replace this independent assessment.

### Automation project — 10 points

Assess the submitted source, reproducible runs and explanation; award partial credit for demonstrated behavior.

- **Input, headers and status — 2 points:** Validates source structure and routes record statuses according to the documented contract.
- **Recoverable validation and physical lines — 2 points:** Reports row errors with accurate physical record-start lines while retaining other valid records; rejects source-level errors.
- **Decimal amounts and stable CSV — 2 points:** Uses exact Decimal arithmetic, deterministic grouping/order and proper CSV writing.
- **Reproducible original and edge runs — 2 points:** Includes exact submitted source plus original, header-only, duplicate and missing-header input/output evidence.
- **Readable functions — 1 point:** Separates parsing, grouping and report composition into explainable functions with the required interface.
- **Limits and improvement — 1 point:** Explains a real limitation of this in-memory fictional workflow and a specific next improvement.

## Lesson 9: Test empty, duplicate, schema, and physical-line cases

Required

**Outcome:** Test empty, duplicate, schema, and physical-line cases. Use the separate worked project and predict before Run.

Checking only one happy input is too weak. We will use small inputs that challenge our assumptions while keeping the normal worked result unchanged. Each test has a prediction we can compare with a visible output.

First is header-only input. There are no data rows, but there is a valid schema. Pause for ten seconds: should it crash, produce a blank string, or produce the CSV header?

It produces the header and newline. Empty totals are a valid report. `repr` makes the newline visible as backslash n. Next append another D1 to the complete worked export. The duplicate is on physical line eight. It must become an error rather than another Ribbon amount.

Missing headers are different from an empty data set. The reader cannot map the required fields, so the whole source is rejected. Our caller catches ValueError and displays a readable message. We do not pretend the file was a zero-dollar successful report.

The fourth input contains a quoted item spanning two physical lines. Its good record starts on line two and finishes on line three. The next invalid record starts on line four. A record counter would misleadingly call that line three. Our physical-position tracking reports line four. That is why retaining source positions mattered.

Header-only works; duplicate is rejected on line eight; missing headers are rejected; multiline diagnostics point to line four. Finally, the original worked total is still five fifty. An improvement did not silently change the first report.

E11 and E12 cover header-only and duplicate input in your assessed fixture. Your final submission also demonstrates missing-header rejection. Include the exact code and test inputs, not just the sentence tests passed. Explain what you intentionally skip, what you reject, why zero price can remain valid, and one limitation such as case-sensitive item grouping. Your instructor checks the submitted version, including a new fictional input. Similar-looking code on this small exercise is not proof of misconduct. What matters is that you can run, explain, and revise your own program.

**Worked ending code, on different data from assessment:**
```python
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


def group_items(records):
    totals = {}
    for record in records:
        item = record["item"]
        totals[item] = totals.get(item, Decimal("0.00")) + record["amount"]
    return dict(sorted(totals.items()))


def write_totals(totals):
    output = StringIO()
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["item", "total"])
    for item, amount in totals.items():
        writer.writerow([item, f"{amount:.2f}"])
    return output.getvalue()


def build_demo_report(source):
    valid, errors, skipped = parse_demo(source)
    totals = group_items(valid)
    return {"csv": write_totals(totals), "valid": len(valid),
            "skipped": skipped, "errors": errors,
            "total": sum(totals.values(), Decimal("0.00"))}


header_only = "order_id,item,qty,unit_price,status\n"
print("empty:", repr(build_demo_report(header_only)["csv"]))
duplicate = build_demo_report(DEMO_CSV + "D1,Ribbon,1,1.50,paid\n")
print("duplicate:", duplicate["errors"][-1])
try:
    build_demo_report("item,qty\nRibbon,2\n")
except ValueError as error:
    print("missing header:", error)
multiline = header_only + 'M1,"Blue\nribbon",1,1.00,paid\nM2,Ties,0,0.25,paid\n'
print("multiline:", build_demo_report(multiline)["errors"][0])
print("original:", f"{build_demo_report(DEMO_CSV)['total']:.2f}")
```


## E11: header-only

Required

Valid required header with no records gives item, total newline, zero counts and Decimal zero. A missing required header is a rejected source, not a successful empty report.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## E12: duplicate

Required

Append A1, Notebook, 1, 4.50, paid in a private assessed copy. Reject physical line9 and preserve 4 valid / 19.75. Rerun the unmodified fixture after your change.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Optional saved-example or agent extension

Optional

Only after your independent project is submitted: review the saved batch proposal or a change from an optional agent. Combine named fictional CSV text sources while preserving original 19.75. Expected extension: Notebook 18.00, Pen 8.75, total 26.75; 6 accepted, 1 unpaid, 3 errors. Inspect cross-source A1 and named rejected-header recovery. Save original/extended outputs, one reviewed line with a reason, and one duplicate/file-recovery test input/output. A saved-example review needs no AI account and does not affect required project points. Use a separate practice project and the supplied later-release examples.

Optional prompt: “Extend my working CSV report to combine named CSV text sources. Keep Decimal, physical record-start lines and recoverable row errors. Reject repeated accepted IDs across sources. A source with a missing/duplicate required header or malformed CSV must give a named file error and later good sources must run. Preserve the original report; show a diff and counterexample tests. Fictional data only.”

In the later-release saved example, use your reviewed parser and grouping functions. The extension keeps one seen-ID set outside the file loop. For each named source it calls the parser inside `try/except ValueError`. A source-level error adds `filename: file rejected: ...` and continues. Recoverable row errors gain filenames; accepted records with a previously accepted ID gain a cross-file duplicate error and are not added. Only remaining accepted rows are grouped and written.

Run the original source first: total 19.75, 4 accepted, 1 unpaid, 2 row errors. Add B1 Notebook quantity 1 at 4.50, B2 Pen quantity 2 at 1.25, and a repeated A1 Notebook quantity 1 at 4.50. The two-source report has Notebook 18.00 / Pen 8.75, total 26.75, 6 accepted, 1 unpaid and 3 errors; A1 is rejected across sources. Then put a missing-header source before the original: original total 19.75 and 4 accepted survive, with one named file rejection plus the original two row errors. A structurally malformed source is rejected as a whole.

Pause and trace the outer seen-ID set, the per-source exception handler, and the duplicate `continue`. Predict an empty batch: only the item,total header, no rows, zero total/counts/errors. Run that check in the separate practice project. Compare the visible report before interpreting any test status.
