import importlib
import os
import unittest
report = importlib.import_module(os.getenv('CSG_REPORT_MODULE', 'report'))

class AcceptanceEdgesTest(unittest.TestCase):
    def test_trim_and_combine(self):
        self.assertEqual(report.summarize([{'category':' Food ', 'amount':2}, {'category':'Food', 'amount':0}]), {'totals':{'Food':2}, 'invalid_rows':0})
    def test_booleans_and_infinity(self):
        self.assertEqual(report.summarize([{'category':'Food', 'amount':True}, {'category':'Food', 'amount':float('inf')}, {'category':'Food', 'amount':float('-inf')}]), {'totals':{}, 'invalid_rows':3})
    def test_large_integer_and_non_dictionary_rows(self):
        huge = 10 ** 400
        self.assertEqual(report.summarize([None, [], {"category": " Demo ", "amount": huge}]), {"totals": {"Demo": huge}, "invalid_rows": 2})
    def test_missing_fields_and_empty(self):
        self.assertEqual(report.summarize([{}, {'category':'Food'}, {'amount':1}]), {'totals':{}, 'invalid_rows':3})
        self.assertEqual(report.summarize([]), {'totals':{}, 'invalid_rows':0})
if __name__ == '__main__': unittest.main()
