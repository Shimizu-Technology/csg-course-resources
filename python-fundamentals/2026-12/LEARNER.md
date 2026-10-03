# Python Fundamentals

Learner preparation guide. Use the matching course in CSG Learn for recordings, submissions and questions. Recordings and admissions are pending; these files alone do not grant access. All practice data is fictional.

## Orientation — your first run

Required

**You will:** Run one line of Python, change it, and send the result in CSG Learn.

You can start in your browser. Open [Hafa Code](https://code.shimizu-technology.com/), create a Python project, and enter:

```python
print("Hello from Guam")
```

Run it. The output should be `Hello from Guam`. Change `Guam` to a word you choose, run it again, and notice which part of the output changed. Keep the quotation marks and parentheses.

**Submit in Learn:** Paste your changed line and the output you saw into the orientation exercise. You may also add a Hafa Code share link, but the pasted code is the preserved review version. If you code locally later, you may add a GitHub repository link.

**If you get stuck:** Save your smallest code sample, error and expected result. Follow your enrollment's help instructions. Optional GitHub and local setup can wait; start Lesson1 in the browser.

**Done when:** You can run a changed line, paste it into Learn, and open Lesson 1.

## Lesson 1 — run, read, and change

Required

**You will:** Predict a small program's output, run it, and use an error message to fix one line.

Python follows the instructions you type. `print` shows a value. Text goes in quotation marks. A number without quotation marks can be used in arithmetic:

```python
print("Hello")
print(2 + 3)
print("2" + "3")
```

Before you run this, write down your guesses for the last two lines. One adds numbers; the other joins text. Run it and compare. A line beginning with `#` is a comment for a reader:

```python
# Change one line, then run again.
print("Hello")
```

If a run fails, read the final line of the error and the line number. Fix one thing and rerun. For example, a `SyntaxError` may mean a parenthesis is missing; a `NameError` may mean you used a name before giving it a value.

## E1 — predict, run, explain

Required

**E1 — predict, run, explain.** For each snippet, write your predicted output *before* running it, then record the actual output:

```python
print(4 + 2)
print("4" + "2")
print("A", "B")
```

Submit the three predictions, three actual results, and one sentence about any result that surprised you. If none surprised you, explain why numbers and quoted text behave differently.

## E2 — repair two errors

Required

**E2 — repair two errors.** Each snippet is a separate small program. Run each, save the error's last line, fix it, then submit the corrected code and a sentence explaining the fix:

```python
print("Hello"
```

```python
print(student_name)
```

For the second program, choose any sample student name. Define it in your code before printing it. **Done when:** both corrected programs run, and you can point to the line you changed.

## Lesson 2 — values, variables, and input

Required

**You will:** Store numbers under useful names and turn text that represents a number into a number.

A variable gives a value a name. `first = 12` stores the number 12. `first = "12"` stores two text characters. Python treats those differently:

```python
first = 12
second = 8
subtotal = first + second
fee = subtotal * 0.10
total = subtotal + fee
print(f"Total: ${total:.2f}")
```

The `f` before the quotation mark lets you insert values into the message. `:.2f` displays two digits after the decimal. The 10% service fee and amounts are fictional arithmetic examples, not Guam prices, tax rates or accounting software. A Guam household or small business could use the same steps to summarize supplied data; this example has no connection to a real payment system.

**Pause and predict:** What changes if `first` becomes 15? Calculate the new subtotal and total before you edit and run. Restore 12 afterward so the exercises use the same data.

Some inputs arrive as text. The expression `"12" + "3"` joins text. If you mean addition, convert both pieces with `int(...)`. An interactive `input()` line is optional in this course; all required tasks work with supplied values in Hafa Code.

## E3 — two-item receipt

Required

**E3 — two-item receipt.** Start with:

```python
first = 12
second = 8
fee_rate = 0.10
# Calculate subtotal, fee, and total below.
```

Print `Subtotal`, `Tax`, and `Total` with dollar signs and two decimal places. Submit your code and the three output lines. Check your arithmetic before running.

## E4 — number or text?

Required

**E4 — number or text?** This program joins two text values:

```python
first = "12"
second = "3"
print(first + second)
```

Change it so the result is the number 15. Submit corrected code, output, and one sentence explaining the original behavior. **Done when:** your E3 output matches your hand calculation and your E4 explanation distinguishes text from numbers.

## Lesson 3 — comparisons and choices

Required

**You will:** Make a program give different answers for an amount below, equal to, or above a budget.

An `if` statement runs its indented lines only when a condition is true. An `elif` checks another condition; `else` handles what remains:

```python
amount = 75
budget = 100

if amount < budget:
    print("Under budget")
elif amount == budget:
    print("On budget")
else:
    print("Over budget")
```

Run the code three times, changing `amount` to 75, 100, then 125. The equality case deserves its own test. If you change `<` to `<=`, what happens at exactly 100? Predict, run, then restore `<`.

## E5 — your budget decision

Required

**E5 — your budget decision.** Make a program with `budget = 100` that prints exactly `Under budget`, `On budget`, or `Over budget` for amounts 75, 100, and 125. Submit your code and a small table of input → output for all three tests. Change only `amount` between tests.

## E6 — find the boundary bug

Required

**E6 — find the boundary bug.** This program has a mistake. Run it with `amount = 100`, write down the wrong message, then fix it. Submit the failing input, old output, corrected code, and new output:

```python
amount = 100
budget = 100

if amount <= budget:
    print("Under budget")
elif amount == budget:
    print("On budget")
else:
    print("Over budget")
```

**Done when:** you have shown all three branches and can explain why `<=` made the equality branch unreachable.

## Checkpoint1 — budget decision

Required

Submit one clean version of your budget decision program. Include results for an amount below, equal to, and above the same budget. Add two sentences: what does your program do when the amount equals the budget, and what mistake did the equality test help you catch?

## Lesson 4 — loops and lists

Required

**You will:** Visit every number in a list, keep a running total, and count numbers above a threshold.

```python
prices = [12, 8, 15, 5]
total = 0

for price in prices:
    total = total + price

print(total)
```

Trace the loop before running it: after each item the total is 12, 20, 35, then 40. The `total = 0` line goes before the loop. If you put it inside the loop, the total starts over for every price. If `prices = []`, the loop runs zero times and the total stays zero.

Before E7, practice counting different data:

```python
quantities = [2, 7, 4]
count = 0
for quantity in quantities:
    if quantity > 3:
        count += 1
print("Over 3:", count)
```

Predict, then run: `Over 3: 2`. The count starts at zero and increases only when the condition is true. `count += 1` means `count = count + 1`; `total += price` is the same shorthand. Try an empty list: zero visits leave count zero. Use this pattern with E7's different data.

## E7 — total and count

Required

**E7 — total and count.** Start with `prices = [12, 8, 15, 5]`. Print the sum as `Total: ...` and the count of prices greater than 10 as `Over 10: ...`. Submit code, the two output lines, and what your program gives for an empty list. A price equal to 10 should not count as *over* 10.

## E8 — reset bug

Required

**E8 — reset bug.** Run and repair this code. Submit a four-row trace showing the running total after each price in the corrected version:

```python
prices = [12, 8, 15, 5]
for price in prices:
    total = 0
    total = total + price
print(total)
```

**Done when:** your result includes all four prices and an empty list does not cause an error.

## Lesson 5 — dictionaries and expense records

Required

**You will:** Read one expense record and summarize several records by category.

A dictionary stores named pieces of one item. A list can hold several dictionaries:

```python
expenses = [
    {"description": "Groceries", "category": "Food", "amount": 42},
    {"description": "Bus pass", "category": "Transport", "amount": 18},
    {"description": "Lunch", "category": "Food", "amount": 13},
]

for expense in expenses:
    print(expense["description"], expense["amount"])
```

The key spelling matters: `expense["amount"]` and `expense["Amount"]` are different keys. Practice grouping different fictional supplies before E10:

```python
packs = [
    {"group": "Food", "units": 2},
    {"group": "Water", "units": 4},
    {"group": "Food", "units": 3},
]
totals = {}
for pack in packs:
    group = pack["group"]
    units = pack["units"]
    totals[group] = totals.get(group, 0) + units
print(totals)
```

Predict, then run: `{'Food': 5, 'Water': 4}`. First Food starts at zero and becomes 2. Water starts its own entry at 4. The second Food reads 2 and adds 3. `get(group, 0)` reads an existing total or supplies zero when the key is new. We change the summary dictionary, not the source packs. Apply this pattern to expense categories and amounts.



The next exercises use this independent six-record expense fixture:

```python
EXPENSES = [
    {"description": "Groceries", "category": "Food", "amount": 42},
    {"description": "Bus pass", "category": "Transport", "amount": 18},
    {"description": "Lunch", "category": "Food", "amount": 13},
    {"description": "Notebook", "category": "Supplies", "amount": 9},
    {"description": "Fuel", "category": "Transport", "amount": 30},
    {"description": "Coffee", "category": "Food", "amount": 6},
]
BUDGET = 120
```

## E9 — itemized list

Required

**E9 — itemized list.** Use the three records above. Print one line per expense as `description: $amount`. Submit the code and three output lines.

## E10 — category totals

Required

**E10 — category totals.** Use the six-record fixture from the project starter (included below or in your enrollment instructions). Build and print a dictionary of totals by category. Do not edit the original records inside your loop. Submit code and each category total. Add one new valid record as a test and say which total changed.

**Done when:** the same loop handles three records or seven records without adding another hard-coded calculation.

Use these supplied records:

```python
EXPENSES = [
    {"description": "Groceries", "category": "Food", "amount": 42},
    {"description": "Bus pass", "category": "Transport", "amount": 18},
    {"description": "Lunch", "category": "Food", "amount": 13},
    {"description": "Notebook", "category": "Supplies", "amount": 9},
    {"description": "Fuel", "category": "Transport", "amount": 30},
    {"description": "Coffee", "category": "Food", "amount": 6},
]
BUDGET = 120
```

## Lesson 6 — functions and debugging

Required

**You will:** Put a repeated calculation in a function, return its result, and test a category that is missing.

```python
def total_for_category(expenses, category):
    total = 0
    for expense in expenses:
        if expense["category"] == category:
            total = total + expense["amount"]
    return total
```

The inputs in parentheses are parameters. `return` gives a value back to the calling code. `print` only displays a value; if a function prints without returning, the caller receives `None`. The function above naturally returns zero when no expense matches the category.



Six-record fixture for the exercises:

```python
EXPENSES = [
    {"description": "Groceries", "category": "Food", "amount": 42},
    {"description": "Bus pass", "category": "Transport", "amount": 18},
    {"description": "Lunch", "category": "Food", "amount": 13},
    {"description": "Notebook", "category": "Supplies", "amount": 9},
    {"description": "Fuel", "category": "Transport", "amount": 30},
    {"description": "Coffee", "category": "Food", "amount": 6},
]
BUDGET = 120
```

## E11 — reusable category function

Required

**E11 — reusable category function.** Use the six expenses in the project starter. Write your own `total_for_category(expenses, category)` function. Call it for `Food` and for `Health` (which is absent). Submit code and both results. Explain why an absent category returns zero.



Use these supplied records:

```python
EXPENSES = [
    {"description": "Groceries", "category": "Food", "amount": 42},
    {"description": "Bus pass", "category": "Transport", "amount": 18},
    {"description": "Lunch", "category": "Food", "amount": 13},
    {"description": "Notebook", "category": "Supplies", "amount": 9},
    {"description": "Fuel", "category": "Transport", "amount": 30},
    {"description": "Coffee", "category": "Food", "amount": 6},
]
BUDGET = 120
```

## E12 — printed instead of returned

Required

**E12 — printed instead of returned.** This caller needs a number it can use. Run the broken code, then repair the function so `doubled` is a number. Submit the before/after output and one sentence explaining the difference:

```python
def add_two_numbers(first, second):
    print(first + second)

result = add_two_numbers(4, 5)
print("Doubled:", result * 2)
```

**Done when:** another calculation can use the function's result, and you can trace a value through one call.

## Checkpoint2 — summarize records

Required

Use the six-record project fixture. Submit a script that prints the overall total and category totals, uses at least one function, and demonstrates either an empty-list case or a missing-category case. Paste the code and output into Learn. Explain in two sentences how one expense enters the correct category total.

```python
EXPENSES = [
    {"description": "Groceries", "category": "Food", "amount": 42},
    {"description": "Bus pass", "category": "Transport", "amount": 18},
    {"description": "Lunch", "category": "Food", "amount": 13},
    {"description": "Notebook", "category": "Supplies", "amount": 9},
    {"description": "Fuel", "category": "Transport", "amount": 30},
    {"description": "Coffee", "category": "Food", "amount": 6},
]
BUDGET = 120
```

## Lesson 7 — plan the expense summary

Required

**You will:** Turn a project request into small steps and expected outputs before writing the full program.

The input is a list of expense dictionaries and a budget. The output must show the overall total, totals by category, the largest expense (or `none` for an empty list), and whether the total is under, exactly on, or over budget. Use the six-record fixture and budget in the project starter (included below or in your enrollment instructions).

Before coding, write a five-step plan: calculate the total; calculate each category total; find the largest; compare total and budget; format the report. Choose at least two of those steps to make into functions. Work out the expected numbers for the six-record sample by hand. Also decide what the report should say if there are no expenses, and if the total equals the budget.

**Submit:** Your five steps, two proposed function names, sample expected results, empty-list result, and equality result. **Done when:** someone else could implement your plan without guessing what the output should contain.

Project fixture for the hand calculation:

```python
EXPENSES = [
    {"description": "Groceries", "category": "Food", "amount": 42},
    {"description": "Bus pass", "category": "Transport", "amount": 18},
    {"description": "Lunch", "category": "Food", "amount": 13},
    {"description": "Notebook", "category": "Supplies", "amount": 9},
    {"description": "Fuel", "category": "Transport", "amount": 30},
    {"description": "Coffee", "category": "Food", "amount": 6},
]
BUDGET = 120
```

## Lesson 8 — build and test

Required

**You will:** Complete the program one function at a time, run five useful cases, and save the exact code being reviewed.

Before the project, practice with a fictional Guam supply-packing list. Quantities are invented teaching data, not a stock or disaster-preparedness recommendation. `None` means no item selected. Select the first visited item, then replace it only if a later item has more units. An empty list visits nothing and leaves `None`.

```python
SUPPLIES = [
    {"label": "Water", "units": 6},
    {"label": "Rice", "units": 3},
    {"label": "Batteries", "units": 9},
]

def total_units(items):
    total = 0
    for item in items:
        total += item["units"]
    return total

def largest_item(items):
    largest = None
    for item in items:
        if largest is None or item["units"] > largest["units"]:
            largest = item
    return largest

def practice_report(items):
    total = total_units(items)
    largest = largest_item(items)
    if largest is None:
        largest_text = "none"
    else:
        largest_text = f"{largest['label']} ({largest['units']} units)"
    return f"Total units: {total}\nLargest pack: {largest_text}"

print(practice_report(SUPPLIES))
print(practice_report([]))
```

Pause and trace the selected item: Water, still Water, then Batteries. `or` checks its left condition first; when true, Python skips the right condition. That avoids reading a key from `None`. The normal output is `Total units: 18` and `Largest pack: Batteries (9 units)`; the empty output is `Total units: 0` and `Largest pack: none`. `practice_report` calls two functions, stores the returned values, chooses display text and returns one string. `\n` moves the next part to a new line. Print outside the function so its returned report can also be saved or tested. Explain the guard and both function calls before adapting the pattern to expenses.

## Independent expense-summary project

Required

Open the partial starter (included below or in your enrollment instructions). Finish `total_amount` first and run it against the six records. Then finish `category_totals`, `total_for_category`, `largest_expense`, `budget_status`, and `make_report`. You may use different function names if your program is clear and meets the rubric. Keep calculation and display separate where it helps you test. The six starter functions are a suggested structure; a clear alternative with at least two functions can meet the same outcome. This expense program is your independent work, not a staff solution to copy.

Run these five cases and record the output:

1. The supplied six expenses with budget 120.
2. An empty list with budget 120: total zero and no largest expense.
3. A request for category `Health`: zero because the sample has none.
4. The supplied expenses with budget 118: exactly on budget.
5. The supplied expenses with budget 100: over budget by $18.

If a test fails, write the input, what you expected, what appeared, and the one change you made. Check the normal case again after your fix.

**Submit:** Your complete code in Learn and the five results. A GitHub or Hafa link may be added, but paste the review version into Learn. **Done when:** the program produces the required report, handles the edge cases, and you can explain two functions.

Copy this unfinished learner starter, then build your own implementation:

```python
"""Learner starter for the Python Fundamentals expense-summary project.

Copy this into Hafa Code. Finish the TODO sections, run the sample, then test
an empty expense list, a missing category, and a budget exactly equal to 118.
These amounts are whole dollars for a programming exercise.
"""

EXPENSES = [
    {"description": "Groceries", "category": "Food", "amount": 42},
    {"description": "Bus pass", "category": "Transport", "amount": 18},
    {"description": "Lunch", "category": "Food", "amount": 13},
    {"description": "Notebook", "category": "Supplies", "amount": 9},
    {"description": "Fuel", "category": "Transport", "amount": 30},
    {"description": "Coffee", "category": "Food", "amount": 6},
]
BUDGET = 120


def total_amount(expenses):
    # TODO: add every expense amount and return the total.
    pass


def category_totals(expenses):
    # TODO: return a dictionary of totals, one entry per category.
    pass


def total_for_category(expenses, category):
    # TODO: return 0 when the requested category is absent.
    pass


def largest_expense(expenses):
    # TODO: return the largest expense, or None when the list is empty.
    pass


def budget_status(total, budget):
    # TODO: return an under, exactly-on, or over-budget message.
    pass


def make_report(expenses, budget):
    # TODO: use your functions to build a readable report.
    # Include the overall total, each category total, the largest expense
    # (or "none"), and the budget result.
    pass


if __name__ == "__main__":
    print(make_report(EXPENSES, BUDGET))
```

- [ ] Overall total and category totals are correct for the supplied six records.
- [ ] Largest expense is correct; an empty list says `none` or an equally clear result.
- [ ] Under, exactly-on, and over-budget conditions are handled.
- [ ] At least two small functions have clear names.
- [ ] Normal, empty-list, missing-category, exact-budget, and over-budget cases are included.
- [ ] Code, output, explanation, and revision are preserved in Learn.

The published rubric (included below or in your enrollment instructions) scores normal output (4), decisions and edge cases (3), structure and readability (2), and explanation/revision (1). Use it to check your own work. Guided passing requires 8/10, correct normal output, an empty report that does not crash, and all three budget branches. Decisions/edge-case points are one each for empty behavior, absent category, and the complete three-branch decision. Normal-output points are one each for total, categories, largest expense and readable report. A correct different implementation can meet the requirements. Instructor scoring, if included in your enrollment, is described in the guided addendum. Use the help route included in your enrollment if you cannot explain a result; include the smallest code example and the output you saw.

## Project rubric (10 points)
Normal output4: one point each for overall total, categories, largest item and readable complete report. Decisions/edge cases3: one each for non-crashing empty input, absent-category zero, and all three budget branches. Structure2: clear names and at least two small functions without unnecessary duplication. Explanation/revision1: explain a choice and make one focused improvement. Guided passing requires8/10, correct normal output, a non-crashing empty report and all three budget branches. Different correct implementations may pass. Shared self-paced learners use this for self-review; scored instructor review applies only if included in enrollment.

### Independent project review

Published point weights; scored feedback only when included in enrollment.

- **Normal output (4 points):** Show the correct overall total, category totals, largest expense, and a readable complete report on changed data.
- **Edge cases (3 points):** Handle empty input without crashing, return zero for an absent category, and correctly distinguish under, equal and over budget.
- **Structure (2 points):** Use clear names and at least two small functions without unnecessary duplication.
- **Explanation and revision (1 point):** Explain a code choice and make one focused improvement. Guided acceptance requires 8/10, correct normal output, empty handling and all budget branches.

## Lesson 9 — share and improve

Required

**You will:** Explain your program, read one review note, and make one focused revision.

Run your submitted version again. Be ready to show the normal report and explain what data the program expects. Ask yourself, “What happens when expenses is empty?” Use the project checklist to find one specific change to make. After changing the code, rerun the test that exposed the problem and the normal sample.

**Submit:** A short explanation of what your program does, one bug you fixed or choice you improved, one future improvement, your revised code, and the two test results. Keep the submitted copy in Learn. Your access and revision window are stated in your enrollment terms.

**Done when:** another person can run the submitted version and reproduce the five project cases.

## Optional — inspect an agent-assisted extension

Optional

Complete your independent expense-summary project and its five required cases first. This optional lesson shows how the same loop and dictionary ideas can support a larger monthly report. It does not change your project rubric or require a paid AI account.

**Try this:** Write a request for a monthly report that keeps the original six-expense result, groups records by `YYYY-MM`, skips invalid amounts or months, and tests a valid zero-dollar amount. If you have a coding agent you prefer, ask it for a proposed change and inspect the diff before accepting anything. You can also work entirely from the saved proposed extension (included below or in your enrollment instructions) and the recorded example. Do not paste personal spending data, credentials, or private student information into an AI tool.

Run the saved example. It should show December 2026 at $118, January 2027 at $60, two skipped invalid records, and the zero-dollar test `({'2027-01': 0}, 0)`. Now imagine a suggested validation condition `if not amount:`. Explain why it rejects a valid amount of zero. Compare the new monthly loop with the category-total loop you wrote yourself. Which parts are the same? Which checks are new?

**Optional submission:** Paste your prompt or change request, one line you accepted or rejected with your reason, the monthly outputs and zero-dollar test, and a sentence about how you checked that your original $118 report still works. A tool name or subscription is not part of the score. You can submit the review without using an AI tool.

Saved optional example (self-contained; no paid AI account):

```python
"""Optional learner review example. Use after completing your own expense report.

This file is a saved proposed extension to inspect and test. It does not contain
the solution to the required six-expense final project.
"""

EXAMPLE_RECORDS = [
    {"category": "Food", "amount": 42, "month": "2026-12"},
    {"category": "Transport", "amount": 18, "month": "2026-12"},
    {"category": "Food", "amount": 13, "month": "2026-12"},
    {"category": "Supplies", "amount": 9, "month": "2026-12"},
    {"category": "Transport", "amount": 30, "month": "2026-12"},
    {"category": "Food", "amount": 6, "month": "2026-12"},
    {"category": "Supplies", "amount": 25, "month": "2027-01"},
    {"category": "Transport", "amount": 12, "month": "2027-01"},
    {"category": "Food", "amount": 8, "month": "2027-01"},
    {"category": "Supplies", "amount": 15, "month": "2027-01"},
    {"category": "Food", "amount": -4, "month": "2027-01"},
    {"category": "Food", "amount": 5},
]


def monthly_summary(records):
    totals = {}
    skipped = 0
    for record in records:
        month = record.get("month")
        amount = record.get("amount")
        if (
            not isinstance(month, str)
            or not month.isascii()
            or len(month) != 7
            or month[4] != "-"
            or not month[:4].isdigit()
            or not month[5:].isdigit()
            or not 1 <= int(month[:4]) <= 9999
            or not 1 <= int(month[5:]) <= 12
            or type(amount) is not int
            or amount < 0
        ):
            skipped += 1
            continue
        totals[month] = totals.get(month, 0) + amount
    return totals, skipped


if __name__ == "__main__":
    totals, skipped = monthly_summary(EXAMPLE_RECORDS)
    for month in sorted(totals):
        print(f"{month}: ${totals[month]}")
    print(f"Skipped invalid records: {skipped}")
    print("Zero-dollar check:", monthly_summary([
        {"category": "Supplies", "amount": 0, "month": "2027-01"}
    ]))
```
