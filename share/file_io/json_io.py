"""Standard module for handling JSON files.

This module provides a class for reading from and writing to JSON files,
extending the functionality of the AbstractFileIO class.
"""

import json
import logging
from .abc_file_io import AbstractFileIO

class JSONFileIO(AbstractFileIO):
    """
    Class for handling JSON file input and output operations.

    This class provides methods for reading data from and writing data to JSON files.
    It uses the standard json library for JSON operations.
    """

    def __init__(self, encoding='utf-8'):
        """
        Initialize a JSONFileIO instance with the specified encoding.

        Args:
            encoding (str): The encoding to use for reading and writing JSON files.
                            Defaults to 'utf-8'.
        """
        super().__init__()
        self.encoding = encoding
        logging.info("JSONFileIO object has been successfully created")

    def read_file(self, file_path):
        """
        Read and return the content from a JSON file.

        This method opens the specified JSON file, parses the JSON content, and 
        returns the resulting data.

        Args:
            file_path (str): The path of the JSON file to be read.

        Returns:
            The data parsed from the JSON file.
        """
        logging.info("Trying to read JSON file '%s'", file_path)
        with open(file_path, 'r', encoding=self.encoding) as jsonfile:
            data = json.load(jsonfile)
            logging.info("Data has been successfully read from '%s'", file_path)
            return data

    def write_file(self, file_path, content):
        """
        Write the given content to a JSON file.

        This method serializes the provided content as JSON and writes it to the specified file.
        The content is written in a human-readable format with an indentation of 4 spaces.

        Args:
            file_path (str): The path of the file where the JSON content will be written.
            content: The data to be serialized to JSON and written to the file.
        """
        logging.info("Trying to write to JSON file '%s'", file_path)
        with open(file_path, 'w', encoding=self.encoding) as jsonfile:
            json.dump(content, jsonfile, indent=4)
            logging.info("Content has been successfully written to '%s'", file_path)
