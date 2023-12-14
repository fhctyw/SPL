from abc import ABC, abstractmethod

class AbstractConsoleOutput(ABC):
    """
    Abstract base class for console output.

    This class defines a standard interface for output operations to the console.
    It serves as a template for concrete implementations that specify how messages
    are displayed to the user.
    """

    @abstractmethod
    def output(self, message):
        """
        Abstract method to output a message to the console.

        This method should be implemented by subclasses to define a specific 
        way of displaying messages to the console. The implementation might 
        include formatting the message or handling special output requirements.

        Args:
            message: The message to be outputted to the console. This could be 
                     a string or any other format that the subclass implementation 
                     chooses to support.
        """
        pass
