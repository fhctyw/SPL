"""Module for console input handling.

This module provides a concrete implementation of console input operations
based on the AbstractConsoleInput class.
"""

from .abc_console_input import AbstractConsoleInput

class ConsoleInput(AbstractConsoleInput):
    """
    Concrete class for standard console input.

    This class implements the input method defined in the AbstractConsoleInput class.
    It provides a basic mechanism to capture input from the console.
    """

    def __init__(self) -> None:
        """
        Initialize the ConsoleInput instance.

        Calls the constructor of the AbstractConsoleInput to ensure proper
        initialization of the abstract base class.
        """
        super().__init__()

    def input(self):
        """
        Capture and return input from the console.

        This method provides a standard way to capture input from the console.
        It does not include exception handling, so it's recommended to handle
        potential exceptions where this method is used.

        Returns:
            The string input by the user.
        """
        return input()
