"""Module for console output handling.

This module provides a concrete implementation of console output operations
based on the AbstractConsoleOutput class.
"""

from .abc_console_output import AbstractConsoleOutput

class ConsoleOutput(AbstractConsoleOutput):
    """
    Concrete class for console output.

    This class implements the output method defined in the AbstractConsoleOutput class.
    It provides a basic mechanism to display messages to the console.
    """

    def output(self, message):
        """
        Display a message to the console.

        This method provides a straightforward way to output a message to the console.
        It utilizes the built-in print function for displaying the message.

        Args:
            message: The message to be displayed. This could be a string or any other 
                     object that can be converted to a string (the object's __str__ method 
                     will be called).
        """
        print(message)
