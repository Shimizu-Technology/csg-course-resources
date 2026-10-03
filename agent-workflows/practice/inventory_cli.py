"""Saved optional worked wrapper; inline fictional data only."""
from inventory import summarize_units

ROWS = [{"supply": " Ribbon ", "units": 2}, {"supply": "Ties", "units": 3}, {"supply": "", "units": 4}]
result = summarize_units(ROWS)
print("supply,units")
for supply, units in sorted(result["totals"].items()):
    print(f"{supply},{units}")
print(f"Invalid rows: {result['invalid_rows']}")
