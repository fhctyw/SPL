"""Module for Abstract Base Classes (ABCs).

This module defines abstract base classes for standardizing
console input operations across different implementations.
"""

from abc import ABC, abstractmethod

class AbstractConsoleInput(ABC):
    """
    An abstract base class that defines a standard interface for console input.

    This class serves as a template for all console input operations. It ensures
    that all subclasses implement the required input methods.
    """

    def __init__(self) -> None:
        """
        Initialize the AbstractConsoleInput instance.

        As an abstract class, it's not intended to be instantiated directly.
        """
        super().__init__()

    @abstractmethod
    def input(self):
        """
        Abstract method for standard input.

        This method should be overridden in concrete subclasses to
        provide specific input functionality from the console.
        """
        pass
