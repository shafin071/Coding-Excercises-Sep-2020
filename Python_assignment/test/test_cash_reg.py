import unittest
from cash_register import CashRegisterHandler
from config import test_data_file, test_result_file, object_columns


# Defining different test groups as list of tuples
# tuple[0]: code,  tuple[1]: total (exception for error cases)
test_cases = [('ABCD', 10.45), ('DCCBAABB', 15.0), ('BBBBBB', 2.0),
              ('ABABAB', 4.0), ('CCAABAA', 9.45), ('AABAABAABCDAABBA', 17.9)]
edge_cases = [('aaaa', 3.0), ('AaBcDD', 17.45)]
error_cases = [(6789789789, Exception), ('AB.CD', Exception), ('ABXCD', Exception)]


class TestCashRegister(unittest.TestCase):

    def test_cash_register(self):
        """
        Tests Cash Register program for regular cases to check if it calculates output correctly
        """
        for test_case in test_cases:
            cr = CashRegisterHandler(barcode=test_case[0], data=test_data_file, object_cols=object_columns)
            cr.call_cash_register()
            self.assertEqual(round(cr.total, 2), test_case[1])

    def test_edge_cases(self):
        """
        Tests Cash Register program for edge cases to check if it still calculates the correct total
        """
        for edge_case in edge_cases:
            cr = CashRegisterHandler(barcode=edge_case[0], data=test_data_file, object_cols=object_columns)
            cr.call_cash_register()
            self.assertEqual(round(cr.total, 2), edge_case[1])

    def test_error_cases(self):
        """
        Tests Cash Register program for error cases to check if exception was raised
        """
        for error_case in error_cases:
            cr = CashRegisterHandler(barcode=error_case[0], data=test_data_file, object_cols=object_columns)
            self.assertRaises(error_case[1], lambda: cr.call_cash_register())


if __name__ == '__main__':
    """
    Save result output in a text file in test/test_results folder
    """
    with open(test_result_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
