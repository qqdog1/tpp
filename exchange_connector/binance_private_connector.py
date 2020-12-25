import abc
import requests


class BinancePrivateConnector(metaclass=abc.ABCMeta):
    def get_balance(self):
        pass

    def send_order(self):
        pass

    def cancel_order(self):
        pass

    def rest_sample(self):
        uri = 'https://api.binance.com/api/v3/time'
        response = requests.get(uri)
        node = response.json()
        print(node['serverTime'])


if __name__ == '__main__':
    connector = BinancePrivateConnector()
    connector.rest_sample()
