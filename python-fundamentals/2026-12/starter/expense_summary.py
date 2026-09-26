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
