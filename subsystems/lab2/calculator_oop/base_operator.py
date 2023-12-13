"""Required ABC module"""
from abc import ABC, abstractmethod

class BaseOperator(ABC):
    """Base module for operator"""
    def __init__(self, sign) -> None:
        super().__init__()
        self.sign = sign

    @abstractmethod
    def calc(self, *args) -> float:
        """Calculation method that should be override"""