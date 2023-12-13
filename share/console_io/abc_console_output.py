"""Required classes"""
from abc import ABC, abstractmethod

class AbstractConsoleOutput(ABC):
    """Abstract base class for console output"""    
    @abstractmethod
    def output(self, message):
        """Output the message to the console."""
        