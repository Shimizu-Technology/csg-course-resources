"""Authored visibly by the instructor before prompting, separate from supplied tests."""
import unittest
from inventory import summarize_units


class LocalContractTests(unittest.TestCase):
    def test_trim_and_combine(self):
        rows = [{"supply": " Ribbon ", "units": 2}, {"supply": "Ribbon", "units": 0}]
        self.assertEqual(summarize_units(rows), {"totals": {"Ribbon": 2}, "invalid_rows": 0})
