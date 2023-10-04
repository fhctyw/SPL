from abc import ABC, abstractmethod

class BaseOperator(ABC):
    def __init__(self, sign) -> None:
        super().__init__()
        self.sign = sign

    @abstractmethod
    def calc(self, number1: float, number2: float) -> float:
        pass