"""Module providing base class for abstraction and decorator for methods that will be overriding"""
from abc import ABC, abstractmethod

class AbstractFileIO(ABC):
    """Abstract class that presents file input and output"""
    @abstractmethod
    def read_file(self, file_path):
        """Methods for reading from file"""

    @abstractmethod
    def write_file(self, file_path, content):
        """Methods for writing in file"""
