from functions import divide
from unittest import TestCase


class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_zero(self):
        dividend = 0
        divisor = 5
        expected_result = 0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_error_on_zero(self):
        #self.assertRaises(ValueError, lambda: divide(25,0)) #lambda since argument should be callable, not result of the function. Unless function doesn't take arguments.
        #or the same test can be achieved via context manager
        with self.assertRaises(ValueError): #Test will pass if error is triggered. If not - test will fail.
            divide(24,0)