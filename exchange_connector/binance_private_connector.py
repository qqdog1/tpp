import abc
import hashlib
import hmac
import json
import time

import requests


class BinancePrivateConnector(metaclass=abc.ABCMeta):
    _key = ''
    _secret = ''

    def __init__(self):
        # python 都用main class的位置做相對
        # 應該有什麼聰明解法
        with open('./config/binance.config') as f:
            node = json.load(f)
        self._key = node['key']
        self._secret = node['secret']

    def get_balance(self):
        uri = 'https://api.binance.com/api/v3/account?'
        millis = str(int(time.time() * 1000))
        header = {'X-MBX-APIKEY': self._key}
        query_string = 'timestamp=' + millis
        signature = hmac.new(bytes(self._secret, 'UTF-8'), bytes(query_string, 'UTF-8'), digestmod=hashlib.sha256)\
            .hexdigest().lower()
        query_string += '&signature=' + signature
        response = requests.get(uri + query_string, headers=header)

        node = response.json()
        balance_node = node['balances']
        balance_dict = {}
        for inner_node in balance_node:
            qty = float(inner_node['free']) + float(inner_node['locked'])
            if qty > 0:
                balance_dict[inner_node['asset']] = qty

        return balance_dict

    def send_order(self):
        pass

    def cancel_order(self):
        pass

    def rest_sample(self):
        print(self._key)
        print(self._secret)
        uri = 'https://api.binance.com/api/v3/time'
        response = requests.get(uri)
        node = response.json()
        print(node['serverTime'])


if __name__ == '__main__':
    connector = BinancePrivateConnector()
    connector.rest_sample()
    connector.get_balance()
