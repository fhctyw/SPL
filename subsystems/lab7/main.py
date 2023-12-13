from coinbase_api import CoinbaseAPI

def main():
    api = CoinbaseAPI()
    api.run()

if '__main__' == __name__:
    main()