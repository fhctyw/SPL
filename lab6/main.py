import unittest
from .test_calculator import TestCalculator

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)

    runner = unittest.TextTestRunner()

    runner.run(suite)
    input()

if '__main__' == __name__:
    main()