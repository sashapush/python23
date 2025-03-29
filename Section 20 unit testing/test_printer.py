from unittest import TestCase
from printer import Printer, PrinterError


class TestPrinter(TestCase):
    def setUp(self):
        self.printer = Printer(pages_per_s=2.0,
                               capacity=300)  # It's not recommended to reuse the same object across all
        # tests unless specifically mentioned, that's why here it's created every time

    # If we want to run abovementioned method only once: and reuse the same printer object for all tests:
    # @classmethod
    # def setUpClass(cls) -> None:
    #   cls.printer = Printer(pages_per_s=2.0, capacity=300)

    # and then leave self.printer - it will work
    # def tearDown(self):(to destroy stuff)
    def test_print_within_capacity(self):
        message = self.printer.print(25)
        # if there's no error - all good with this test
        self.assertEqual(f"Printed 25 pages in 12.50 seconds.", message)

    def test_pring_outside_capacity(self):
        with self.assertRaises(PrinterError): #expect the error with the below action
            self.printer.print(301)

    def test_exact_capacity(self):
        self.printer.print(
            self.printer._capacity)  # private property _capacity; we print up to the capacity of the printer

    def test_printer_speed(self):
        pages = 10
        expected = "Printed 10 pages in 5.00 seconds."
        result = self.printer.print(pages)
        self.assertEqual(result, expected)

    def test_printer_created_arguments(self):
        self.assertEqual(self.printer.pages_per_s, 2.0)
        self.assertEqual(self.printer._capacity, 300)

    def test_printer_created_arguments(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        expected = "Printed 11 pages in 3.67 seconds."
        result = fast_printer.print(pages)
        self.assertEqual(result, expected)

    def test_multiple_runs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

    def test_multiple_runs_end_up_error(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)
        with self.assertRaises(PrinterError): #expect the error with the below action
            self.printer.print(1)

