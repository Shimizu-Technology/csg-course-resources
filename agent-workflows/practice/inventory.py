"""Deliberately broken fictional community supply-unit tracker."""


def summarize_units(rows):
    totals = {}
    invalid = 0
    for row in rows:
        supply = row.get("supply", "")
        units = row.get("units")
        if not units or units < 0:
            invalid += 1
            continue
        totals[supply] = totals.get(supply, 0) + units
    return {"totals": totals, "invalid_rows": invalid}
