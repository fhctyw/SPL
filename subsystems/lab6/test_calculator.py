import unittest
import unittest.mock
from subsystems.lab2.calculator_oop.calculator import Calculator
from subsystems.lab2.calculator_oop.my_operators import PlusOperator, MinusOperator, MultOperator, DivOperator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Initialize the operators and the calculator
        self.plus = PlusOperator()
        self.minus = MinusOperator()
        self.mult = MultOperator()
        self.div = DivOperator()
        self.operators = [self.plus, self.minus, self.mult, self.div]
        self.calculator = Calculator(self.operators)

    def test_plus_operator(self):
        # Test the addition operator
        result = self.calculator.calculate('PlusOperator', 1, 2, 3)
        self.assertEqual(result, 6, "Expected sum of 1, 2, 3 to be 6")

    def test_minus_operator(self):
        # Test the subtraction operator
        result = self.calculator.calculate('MinusOperator', 10, 1, 3)
        self.assertEqual(result, 6, "Expected result of 10 - 1 - 3 to be 6")

    def test_mult_operator(self):
        # Test the multiplication operator
        result = self.calculator.calculate('MultOperator', 2, 3, 4)
        self.assertEqual(result, 24, "Expected product of 2, 3, 4 to be 24")

    def test_div_operator(self):
        # Test the division operator
        result = self.calculator.calculate('DivOperator', 20, 2, 5)
        self.assertEqual(result, 2, "Expected result of 20 / 2 / 5 to be 2")

    def test_div_by_zero(self):
        # Test division by zero error
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calculate('DivOperator', 20, 0)

    def test_operator_not_found(self):
        # Test for a non-existent operator
        with self.assertRaises(ValueError):
            self.calculator.calculate('NonExistentOperator', 1, 2)
            