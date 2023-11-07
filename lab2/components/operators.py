from ..tools.base_operator import BaseOperator

class PlusOperator(BaseOperator):
    def __init__(self) -> None:
        super().__init__('+')

    def calc(self, number1: float, number2: float) -> float:
        return number1 + number2

class MinusOperator(BaseOperator):
    def __init__(self) -> None:
        super().__init__('-')

    def calc(self, number1: float, number2: float) -> float:
        return number1 - number2

class MultOperator(BaseOperator):
    def __init__(self) -> None:
        super().__init__('*')

    def calc(self, number1: float, number2: float) -> float:
        return number1 * number2

class DivOperator(BaseOperator):
    def __init__(self) -> None:
        super().__init__('/')

    def calc(self, number1: float, number2: float) -> float:
        return number1 / number2
