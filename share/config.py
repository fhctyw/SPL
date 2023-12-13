"""Module for check if file exists"""
import os
import logging

from share.file_io.json_io import JSONFileIO

class KeyConfigNotFoundException(Exception):
    """Exception if key not found"""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Config:
    """
    Configuration class. Need to get configuration from config file.
    Example:
        # data/lab1/config.json:
        # {
        #     "default color": "red",
        #     "default font": 20
        # }

        config = Config("data/lab1/config.json")
        color = config.get("default color") # config["default color"]
        print(color) # output "red"
    """
    def __init__(self, config_file) -> "Config":
        self.config_data = {}
        self._load_config(config_file)
        logging.info("Config has been successfully created")

    def _load_config(self, config_file) -> None:
        logging.info("Try to load config from '%s'", config_file)
        if os.path.exists(config_file):
            json_file_io = JSONFileIO()
            self.config_data = json_file_io.read_file(config_file)
        else:
            logging.error("Config file '%s' not found", config_file)
            raise FileNotFoundError(f"Config file '{config_file}' not found.")
        logging.info("Config has been successfully loaded")

    def get(self, key, default=None):
        """Get config value by key"""
        result = self.config_data.get(key, default)
        if result is None:
            logging.warning("Key('%s') is missing in config. Result will be 'None'", key)
        return result

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            logging.exception("Key('%s') config not found", key)
            raise KeyConfigNotFoundException(f"Key config '{key}' not found.")
        return value
