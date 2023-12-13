import logging
from .base_operator import BaseOperator

class Calculator():
    """OOP Calculator class"""
    def __init__(self, operators: list[BaseOperator]) -> None:
        self.operators = {type(op).__name__: op for op in operators}
        logging.info("Calculator initialized with operators: %s", ', '.join(type(op).__name__ for op in operators))

    def calculate(self, operator_name: str, *args):
        """Main method for calculation"""
        logging.info("Calculation requested using operator %s with arguments: %s", operator_name, args)
        
        operator = self.operators.get(operator_name)
        if not operator:
            logging.error("Operator %s not found", operator_name)
            raise ValueError(f"Operator {operator_name} not found")
        
        result = operator.calc(*args)
        logging.info("Result of the calculation: %s", result)
        return result
