import requests
from consolemenu import *
from consolemenu.items import *
from tabulate import tabulate

URL = "https://api.coinbase.com/v2"

class CoinbaseAPI:
    def __init__(self) -> None:
        self.menu = ConsoleMenu("Coinbase Api")
        self.menu.append_item(FunctionItem("Get currencies", self.get_all_currencies))
        self.menu.append_item(FunctionItem("Get crypto currencies", self.get_crypto_currencies))
        self.menu.append_item(FunctionItem("Exchange", self.exchange))
        self.menu.append_item(FunctionItem("Get server time", self.get_time))

    def get_time(self):
        headers = {'Accept': 'application/json'}
        response = requests.get(f"{URL}/time", headers=headers)

        json_data = response.json()['data']
        print(f"iso: {json_data['iso']}")
        print(f"epoch: {json_data['epoch']}")
        input()

    def exchange(self):
        currency = input("Enter currency: ")
        amount = float(input(f"Enter amount of {currency.upper()}: "))

        headers = {'Accept': 'application/json'}
        response = requests.get(f"{URL}/exchange-rates?currency={currency}", headers=headers)

        json_data = response.json()['data']

        rates = json_data['rates']

        exchange_rate_data = [[key, float(rate) * amount] for key, rate in rates.items()]

        table = tabulate(exchange_rate_data, headers=['Currency', f'Amount in {currency.upper()}'], tablefmt='grid')
        print(table)
        input()

    def get_crypto_currencies(self):
        headers = {'Accept': 'application/json'}
        response = requests.get(f"{URL}/currencies/crypto", headers=headers)

        json_data = response.json()['data']
        sorted_json_data = sorted(json_data, key=lambda x: x['sort_index'])

        crypto_data = [[crypto['code'], crypto['name'], crypto['sort_index']] for crypto in sorted_json_data]

        crypto_table = tabulate(crypto_data, headers=['Code', 'Name', 'Color', 'Sort Index', 'Exponent', 'Type', 'Address Regex', 'Asset ID'], tablefmt='grid')
        print(crypto_table)

        input()

    def get_all_currencies(self):
        headers = {'Accept': 'application/json'}
        response = requests.get(f"{URL}/currencies", headers=headers)

        json_data = response.json()
        data = [[currency['id'], currency['name'], currency['min_size']] for currency in json_data['data']]

        table = tabulate(data, headers=['ID', 'Name', 'Minimum Size'], tablefmt='grid')
        print(table)

        input()

    def run(self) -> None:
        self.menu.show()