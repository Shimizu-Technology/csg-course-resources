import importlib
import os
import unittest

report = importlib.import_module(os.getenv("CSG_REPORT_MODULE", "report"))


class ExpenseReportTest(unittest.TestCase):
    def test_zero_is_valid(self):
        self.assertEqual(report.summarize([{"category": "Food", "amount": 0}]), {"totals": {"Food": 0}, "invalid_rows": 0})

    def test_invalid_rows_do_not_create_categories(self):
        rows = [{"category": "", "amount": 3}, {"category": "Travel", "amount": -2}, {"category": "Food", "amount": 5}]
        self.assertEqual(report.summarize(rows), {"totals": {"Food": 5}, "invalid_rows": 2})

    def test_non_numeric_value_is_invalid(self):
        self.assertEqual(report.summarize([{"category": "Food", "amount": "five"}]), {"totals": {}, "invalid_rows": 1})

    def test_non_finite_amount_is_invalid(self):
        self.assertEqual(report.summarize([{"category": "Food", "amount": float("nan")}]), {"totals": {}, "invalid_rows": 1})


if __name__ == "__main__":
    unittest.main()
