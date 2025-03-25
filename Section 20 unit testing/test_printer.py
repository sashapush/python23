from unittest import TestCase
from printer import Printer

class TestPrinter(TestCase):
    def setUp(self):
        self.printer = Printer(pages_per_s=2.0, capacity=300) #It's not recommended to reuse the same object across all
        # tests unless specifically mentioned
    #If we want to run abovementioned method  not only once: (for example create a new printer for every test).
    #@classmethod
    #def setUpClass(cls) -> None:
    #   cls.printer = Printer(pages_per_s=2.0, capacity=300)

    #and then leave self.printer - it will work
    #def tearDown(self):(to destroy stuff)
    def test_print_within_capacity(self):
        message = self.printer.print(25)
        # if there's no error - all good with this test
        self.assertEqual(f"Printed 25 pages in 12.50 seconds", message)
