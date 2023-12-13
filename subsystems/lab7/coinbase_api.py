import logging
import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError
from consolemenu import *
from consolemenu.items import *
from tabulate import tabulate

from share.menu import Menu, menu_item
from share.config import Config

config = Config("data/lab7/config.json")

URL = config["url"]

class CoinbaseAPI(Menu):
    def __init__(self):
        super().__init__("Coinbase Api")

    @menu_item("Get server time")
    def get_time(self):
        try:
            headers = {'Accept': 'application/json'}
            correct_url = f"{URL}/time"
            logging.info("Getting request to %s", correct_url)
            response = requests.get(correct_url, headers=headers)
            response.raise_for_status()

            json_data = response.json()['data']
            print(f"iso: {json_data['iso']}")
            print(f"epoch: {json_data['epoch']}")
        except ConnectionError as ce:
            logging.error("Connection error occurred while getting server time: %s", ce)
        except Timeout as te:
            logging.error("Request timed out while getting server time: %s", te)
        except HTTPError as http_err:
            logging.error("HTTP error occurred while getting server time: %s", http_err)
        except Exception as e:
            logging.error("Unexpected error occurred while getting server time: %s", e)
        finally:
            input()

    @menu_item("Exchange")
    def exchange(self):
        try:
            currency = input("Enter currency: ")
            amount = float(input(f"Enter amount of {currency.upper()}: "))

            headers = {'Accept': 'application/json'}
            correct_url = f"{URL}/exchange-rates?currency={currency}"
            logging.info("Getting request to %s", correct_url)
            response = requests.get(correct_url, headers=headers)

            json_data = response.json()['data']

            rates = json_data['rates']

            exchange_rate_data = [[key, float(rate) * amount] for key, rate in rates.items()]

            table = tabulate(exchange_rate_data, headers=['Currency', f'Amount in {currency.upper()}'], tablefmt='grid')
            print(table)
        except ConnectionError as ce:
            logging.error("Connection error occurred while exchange, %s", ce)
        except Timeout as te:
            logging.error("Request timed out while exchange, %s", te)
        except HTTPError as http_err:
            logging.error("HTTP error occurred while exchange: %s", http_err)
        except Exception as e:
            logging.error("Unexpected error occurred while exchange: %s", e)
        input()

    @menu_item("Get crypto currencies")
    def get_crypto_currencies(self):
        try:
            headers = {'Accept': 'application/json'}
            correct_url = f"{URL}/currencies/crypto"
            logging.info("Getting request to %s", correct_url)
            response = requests.get(correct_url, headers=headers)
            response.raise_for_status()

            json_data = response.json()['data']
            sorted_json_data = sorted(json_data, key=lambda x: x['sort_index'])

            crypto_data = [[crypto['code'], crypto['name'], crypto['sort_index']] for crypto in sorted_json_data]
            crypto_table = tabulate(crypto_data, headers=['Code', 'Name', 'Sort Index'], tablefmt='grid')
            print(crypto_table)
        except ConnectionError as ce:
            logging.error("Connection error occurred while fetching crypto currencies: %s", ce)
        except Timeout as te:
            logging.error("Request timed out while fetching crypto currencies: %s", te)
        except HTTPError as http_err:
            logging.error("HTTP error occurred while fetching crypto currencies: %s", http_err)
        except Exception as e:
            logging.error("Unexpected error occurred while fetching crypto currencies: %s", e)
        finally:
            input()

    @menu_item("Get currencies")
    def get_all_currencies(self):
        try:
            headers = {'Accept': 'application/json'}
            correct_url = f"{URL}/currencies"
            logging.info("Getting request to %s", correct_url)
            response = requests.get(correct_url, headers=headers)
            response.raise_for_status()

            json_data = response.json()
            data = [[currency['id'], currency['name'], currency['min_size']] for currency in json_data['data']]
            table = tabulate(data, headers=['ID', 'Name', 'Minimum Size'], tablefmt='grid')
            print(table)
        except ConnectionError as ce:
            logging.error("Connection error occurred while fetching all currencies: %s", ce)
        except Timeout as te:
            logging.error("Request timed out while fetching all currencies: %s", te)
        except HTTPError as http_err:
            logging.error("HTTP error occurred while fetching all currencies: %s", http_err)
        except Exception as e:
            logging.error("Unexpected error occurred while fetching all currencies: %s", e)
        finally:
            input()

    def run(self) -> None:
        self.show()