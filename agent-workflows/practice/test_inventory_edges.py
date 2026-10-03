import unittest
from inventory import summarize_units


class InventoryEdgesTests(unittest.TestCase):
    def test_boolean_missing_and_non_dictionary(self):
        rows = [{"supply": "Ribbon", "units": True}, {}, None]
        self.assertEqual(summarize_units(rows), {"totals": {}, "invalid_rows": 3})

    def test_invalid_count_once_then_continue(self):
        rows = [{"supply": "", "units": -1}, {"supply": "Ties", "units": 3}]
        self.assertEqual(summarize_units(rows), {"totals": {"Ties": 3}, "invalid_rows": 1})

    def test_empty_and_large_units(self):
        self.assertEqual(summarize_units([]), {"totals": {}, "invalid_rows": 0})
        huge = 10 ** 400
        self.assertEqual(summarize_units([{"supply": "Ties", "units": huge}]), {"totals": {"Ties": huge}, "invalid_rows": 0})
