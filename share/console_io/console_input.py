"""Abc module"""
from .abc_console_input import AbstractConsoleInput

class ConsoleInput(AbstractConsoleInput):
    """Class for console input"""
    def __init__(self) -> None:
        super().__init__()

    def input(self):
        """Standard input without exception handing"""
        return input()