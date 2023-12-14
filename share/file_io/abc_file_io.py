from abc import ABC, abstractmethod

class AbstractFileIO(ABC):
    """
    Abstract class for file input/output operations.

    This class serves as a template for implementing file reading and writing operations.
    It defines abstract methods for reading from and writing to files, which must be 
    implemented by any concrete subclasses.
    """

    @abstractmethod
    def read_file(self, file_path):
        """
        Abstract method to read content from a file.

        This method should be implemented in subclasses to define how to read and 
        return content from the specified file.

        Args:
            file_path (str): The path to the file to be read.

        Returns:
            The method implementation should return the content read from the file.
        """
        pass

    @abstractmethod
    def write_file(self, file_path, content):
        """
        Abstract method to write content to a file.

        This method should be implemented in subclasses to define how to write the given 
        content to the specified file. The implementation can handle various types of 
        content (like strings, bytes, or other serializable objects) and file handling 
        modes (e.g., overwrite, append).

        Args:
            file_path (str): The path to the file where the content will be written.
            content: The content to be written to the file. The type of content can vary 
                     and should be handled by the implementation.
        """
        pass
