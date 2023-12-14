"""Module for parsing and handling configuration files.

This module provides functionality to load and retrieve configuration settings
from JSON files. It includes a custom exception for handling missing keys in
the configuration data.
"""

import os
import logging
from share.file_io.json_io import JSONFileIO

class KeyConfigNotFoundException(Exception):
    """
    Custom exception raised when a specified key is not found in the configuration.

    Attributes:
        args: Arguments passed to the Exception constructor.
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Config:
    """
    Class for handling configuration data from JSON files.

    This class reads configuration data from a specified JSON file and provides
    methods to access the configuration values.

    Attributes:
        config_data (dict): A dictionary containing the configuration data.

    Example:
        # Assuming data/lab1/config.json contains:
        # {
        #     "default color": "red",
        #     "default font": 20
        # }

        config = Config("data/lab1/config.json")
        color = config.get("default color")  # Or: config["default color"]
        print(color)  # Outputs: red
    """

    def __init__(self, config_file) -> "Config":
        """
        Initialize the Config object by loading data from the specified JSON file.

        Args:
            config_file (str): Path to the JSON configuration file.

        Raises:
            FileNotFoundError: If the specified configuration file does not exist.
        """
        self.config_data = {}
        self._load_config(config_file)
        logging.info("Config has been successfully created")

    def _load_config(self, config_file) -> None:
        """
        Internal method to load configuration data from a JSON file.

        Args:
            config_file (str): Path to the JSON configuration file.

        Raises:
            FileNotFoundError: If the specified configuration file does not exist.
        """
        logging.info("Trying to load config from '%s'", config_file)
        if os.path.exists(config_file):
            json_file_io = JSONFileIO()
            self.config_data = json_file_io.read_file(config_file)
        else:
            logging.error("Config file '%s' not found", config_file)
            raise FileNotFoundError(f"Config file '{config_file}' not found.")
        logging.info("Config has been successfully loaded")

    def get(self, key, default=None):
        """
        Retrieve the configuration value for the given key.

        Args:
            key (str): The key for which to retrieve the value.
            default (optional): The default value to return if the key is not found.

        Returns:
            The value associated with the key, or the default value if the key is not found.
        """
        result = self.config_data.get(key, default)
        if result is None:
            logging.warning("Key('%s') is missing in config. Result will be 'None'", key)
        return result

    def __getitem__(self, key):
        """
        Retrieve the configuration value using dictionary-like indexing.

        Args:
            key (str): The key for which to retrieve the value.

        Returns:
            The value associated with the key.

        Raises:
            KeyConfigNotFoundException: If the key is not found in the configuration data.
        """
        value = self.get(key)
        if value is None:
            logging.exception("Key('%s') config not found", key)
            raise KeyConfigNotFoundException(f"Key config '{key}' not found.")
        return value
