import unittest
from inventory import summarize_units


class InventoryTests(unittest.TestCase):
    def test_zero_is_valid(self):
        self.assertEqual(summarize_units([{"supply": "Ribbon", "units": 0}]), {"totals": {"Ribbon": 0}, "invalid_rows": 0})

    def test_blank_and_negative_are_invalid(self):
        rows = [{"supply": "", "units": 3}, {"supply": "Ties", "units": -2}, {"supply": "Ribbon", "units": 5}]
        self.assertEqual(summarize_units(rows), {"totals": {"Ribbon": 5}, "invalid_rows": 2})

    def test_text_units_do_not_crash(self):
        self.assertEqual(summarize_units([{"supply": "Ribbon", "units": "five"}]), {"totals": {}, "invalid_rows": 1})

    def test_fractional_units_are_invalid(self):
        self.assertEqual(summarize_units([{"supply": "Ribbon", "units": 1.5}]), {"totals": {}, "invalid_rows": 1})


if __name__ == "__main__":
    unittest.main()
