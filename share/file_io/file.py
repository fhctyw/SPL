"""Abstract class that should be implemented"""
from .abc_file_io import AbstractFileIO

class FileIO(AbstractFileIO):
    """Class for writing/reading any data in/from file"""
    def __init__(self, encoding='utf-8') -> None:
        super().__init__()
        self.encoding = encoding

    def read_file(self, file_path):
        """Read file from `file_path`"""
        with open(file_path, 'r', encoding=self.encoding) as file:
            return file.read()

    def write_file(self, file_path, content):
        """Write `content` in `file_path`"""
        with open(file_path, 'w', encoding=self.encoding) as file:
            file.write(content)
