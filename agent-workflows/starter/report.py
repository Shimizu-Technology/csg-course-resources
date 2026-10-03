"""Starter with deliberate bugs for the CSG agent workflow exercise."""


def summarize(rows):
    totals = {}
    invalid = 0
    for row in rows:
        category = row.get("category", "")
        amount = row.get("amount")
        if not amount or amount < 0:
            invalid += 1
            continue
        totals[category] = totals.get(category, 0) + amount
    return {"totals": totals, "invalid_rows": invalid}
