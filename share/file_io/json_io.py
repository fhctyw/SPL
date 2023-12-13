"""Standard module for handling json files"""
import json
import logging
from .abc_file_io import AbstractFileIO

class JSONFileIO(AbstractFileIO):
    """Class for handling JSON file input and output operations."""

    def __init__(self, encoding='utf-8'):
        """Constructor for JSONFileIO."""
        self.encoding = encoding
        logging.info("JSONFileIO object has been successfully created")

    def read_file(self, file_path):
        """Reads content from a JSON file"""
        logging.info("Try to read json file '%s'", file_path)
        with open(file_path, 'r', encoding=self.encoding) as jsonfile:
            data = json.load(jsonfile)
            logging.info("Data has been successfully read")
            return data

    def write_file(self, file_path, content):
        """Writes content to a JSON file"""
        logging.info("Try to write json file '%s'", file_path)
        with open(file_path, 'w', encoding=self.encoding) as jsonfile:
            json.dump(content, jsonfile, indent=4)
            logging.info("Content has been successfully read")
            