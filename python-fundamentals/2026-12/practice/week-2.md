# Week 2 practice

Follow the full instructions and submit your work in CSG Learn. These starting points match Lessons 4–6.

## Loop through prices

```python
prices = [12, 8, 15, 5]
total = 0
count_over_10 = 0

for price in prices:
    # Update total and count_over_10 here.
    pass

print("Total:", total)
print("Over 10:", count_over_10)
```

Trace the running total after each price. Then try `prices = []`.

## Expense records

```python
expenses = [
    {"description": "Groceries", "category": "Food", "amount": 42},
    {"description": "Bus pass", "category": "Transport", "amount": 18},
    {"description": "Lunch", "category": "Food", "amount": 13},
]

# Print each description and amount. Then count totals by category.
```

For the six-record version, use the [project starter](../starter/expense_summary.py). Check that a new valid record can be added without writing another hard-coded calculation.

## A function you can reuse

```python
def total_for_category(expenses, category):
    total = 0
    # Add amounts only when the category matches.
    return total
```

Call your function with `Food` and with a category that is absent. Explain the absent-category result in Learn.
