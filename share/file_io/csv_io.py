"""Standard module for handling csv files"""
import csv
from .abc_file_io import AbstractFileIO

class CSVFileIO(AbstractFileIO):
    """Class for writing/reading in/from csv file"""
    def __init__(self, encoding="utf-8") -> None:
        super().__init__()
        self.encoding = encoding

    def read_file(self, file_path):
        """Read file from `file_path`"""
        with open(file_path, mode='r', newline='', encoding=self.encoding) as csvfile:
            reader = csv.reader(csvfile)
            return list(row for row in reader)

    def write_file(self, file_path, content):
        """Write `content` in `file_path`"""
        if not isinstance(content, list):
            raise ValueError("Content must be a list of rows.")
        with open(file_path, mode='w', newline='', encoding=self.encoding) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(content)
