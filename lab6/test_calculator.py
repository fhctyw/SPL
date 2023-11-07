import unittest
import unittest.mock
from lab1.main import *

class TestCalculator(unittest.TestCase):
    def test_init(self):
        plus = PlusOperator()
        minus = MinusOperator()
        mult = MultOperator()
        div = DivOperator()
        
        calculator = Calculator([plus, minus, mult, div])
        
        self.assertEqual(len(calculator.operations), 4)
        self.assertIn(plus, calculator.operations)
        self.assertIn(minus, calculator.operations)
        self.assertIn(mult, calculator.operations)
        self.assertIn(div, calculator.operations)
        
        self.assertEqual(calculator.users, [])
        
        self.assertIsNone(calculator.current_user)
        self.assertIsNone(calculator.current_operation)
        self.assertIsNone(calculator.number1)
        self.assertIsNone(calculator.number2)
        self.assertIsNone(calculator.result)

    def test_user_auth_new_user(self):
        with unittest.mock.patch('builtins.input', side_effect=['TestUser', '4']):
            calculator = Calculator()
            calculator.user_auth()
            self.assertEqual(len(calculator.users), 1)
            self.assertEqual(calculator.current_user.name, 'TestUser')
            self.assertEqual(calculator.current_user.float_precision, 4)
    
    def test_user_auth_existing_user(self):
        user = User('ExistingUser', 2)
        calculator = Calculator(users=[user])
        
        with unittest.mock.patch('builtins.input', return_value='ExistingUser'):
            calculator.user_auth()
            self.assertEqual(len(calculator.users), 1)
            self.assertEqual(calculator.current_user, user)

    def test_simple_addition(self):
        """Test simple addition operation."""
        user = User('UserForAddition', 2)
        calculator = Calculator([PlusOperator()], [user])
        calculator.current_user = user
        result = calculator.operations[0].calc(2.123, 4.567)
        self.assertEqual(round(result, user.float_precision), 6.69)