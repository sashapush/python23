from functions import divide, multiply
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
        # self.assertRaises(ValueError, lambda: divide(25,0)) #lambda since argument should be callable, not result of the function. Unless function doesn't take arguments.
        # or the same test can be achieved via context manager
        with self.assertRaises(ValueError):  # Test will pass if error is triggered. If not - test will fail.
            divide(24, 0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 16
        self.assertEqual(multiply(expected), expected)

    def test_multiply_single_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply_result(self):
        inputs = (3, 5)
        expected = 15
        self.assertEqual(multiply(*inputs), expected)  # *inputs passes arrayish data as individual args

    def test_multiply_result_with_zero(self):
        inputs = (3, 5, 0)
        expected = 0
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_negative(self):
        inputs = (3, -5, 2)
        expected = -30
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_floats(self):
        inputs = (3.0, 2)
        expected = 6.0
        self.assertEqual(multiply(*inputs), expected)

#lots of duplication, but with official documentation it can be improved, f.e hypothesis