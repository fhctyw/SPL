"""Module for ABC"""
from abc import ABC, abstractmethod

class AbstractConsoleInput(ABC):
    """Abstract class for console input"""
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def input(self):
        """Standard input"""