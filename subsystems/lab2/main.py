"""Required classes from module"""
from calculator_oop.calculator import Calculator
from calculator_oop.my_operators import PlusOperator, DivOperator, MultOperator

if '__main__' == __name__:
    calc = Calculator([PlusOperator(), DivOperator(), MultOperator()])

    result = calc.calculate("PlusOperator", 3, 17, 313, 55, 2, 4)

    print(result)
