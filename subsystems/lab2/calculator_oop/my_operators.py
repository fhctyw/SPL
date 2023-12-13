"""Base class BaseOperator"""
from functools import reduce
from .base_operator import BaseOperator

class PlusOperator(BaseOperator):
    """Addition class"""
    def __init__(self) -> None:
        super().__init__('+')

    def calc(self, *args) -> float:
        return reduce(lambda x, y: x + y, args)

class MinusOperator(BaseOperator):
    """Subtraction class"""
    def __init__(self) -> None:
        super().__init__('-')

    def calc(self, *args) -> float:
        return reduce(lambda x, y: x - y, args)

class MultOperator(BaseOperator):
    """Multiplication class"""
    def __init__(self) -> None:
        super().__init__('*')

    def calc(self, *args) -> float:
        return reduce(lambda x, y: x * y, args)

class DivOperator(BaseOperator):
    """Division class"""
    def __init__(self) -> None:
        super().__init__('/')

    def calc(self, *args) -> float:
        return reduce(lambda x, y: x / y, args)
