from .abc_file_io import AbstractFileIO

class FileIO(AbstractFileIO):
    """
    Concrete class for file I/O operations.

    This class implements the abstract methods defined in AbstractFileIO for reading
    from and writing to files. It supports specifying the file encoding.
    """

    def __init__(self, encoding='utf-8') -> None:
        """
        Initialize a FileIO instance with the specified encoding.

        Args:
            encoding (str): The encoding to use for file operations. Defaults to 'utf-8'.
        """
        super().__init__()
        self.encoding = encoding

    def read_file(self, file_path):
        """
        Read and return the content from the specified file.

        This method opens the file in read mode and returns its contents as a string.

        Args:
            file_path (str): The path of the file to be read.

        Returns:
            str: The content read from the file.
        """
        with open(file_path, 'r', encoding=self.encoding) as file:
            return file.read()

    def write_file(self, file_path, content):
        """
        Write the given content to the specified file.

        This method opens the file in write mode and writes the content to it. 
        If the file already exists, its content will be overwritten.

        Args:
            file_path (str): The path of the file where the content will be written.
            content: The content to be written to the file. This should be a string or 
                     any object that can be converted to a string.
        """
        with open(file_path, 'w', encoding=self.encoding) as file:
            file.write(content)
