import abc
import json
import logging
import threading
import time
from logging.config import fileConfig

import websocket


def callback_test(symbol:str, bid_price: float, bid_qty: float, ask_price: float, ask_qty: float):
    print(symbol, ':', bid_price, '@', bid_qty, " : ", ask_price, '@', ask_qty)


class BinancePublicConnector(metaclass=abc.ABCMeta):
    def __init__(self):
        self.connect_status = False
        self.callback_dict = {}
        self.symbol_market_dict = {}
        # self.logger = logging.getLogger('BinancePublicConnector')
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            'wss://stream.binance.com/stream',
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.on_open = self.on_open

    @property
    def is_connect(self):
        return self.connect_status

    def start(self):
        self.ws.run_forever()

    def stop(self):
        self.ws.keep_running = False

    def subscribe(self, market: str, callback):
        symbol = market.replace('-', '').lower()
        self.callback_dict[symbol] = callback
        self.symbol_market_dict[symbol] = market
        message = '{"method":"SUBSCRIBE","params":["' + symbol + '@depth5"],"id":1}'
        self.ws.send(message)

    def unsubscribe(self, market: str):
        symbol = market.replace('-', '').lower()
        if symbol in self.callback_dict.keys():
            self.callback_dict.pop(symbol)
            message = '{"method":"UNSUBSCRIBE","params":["' + symbol + '@depth5"],"id":1}'
            self.ws.send(message)

    def on_open(self):
        # self.logger.info('websocket connected.')
        logging.info('websocket connected.')
        self.connect_status = True

    def on_message(self, message):
        json_node = json.loads(message)
        if 'stream' in json_node:
            topic = str(json_node['stream'])
            if 'depth' in topic:
                self.parse_book(json_node)

    def on_error(self):
        self.logger.info('websocket on error.')
        self.connect_status = False
        self.reconnect()

    def on_close(self):
        self.logger.info('websocket closed.')
        self.connect_status = False
        self.reconnect()

    def reconnect(self):
        pass

    def parse_book(self, json_node):
        print(json_node)
        topic = str(json_node['stream'])
        symbol = topic.split('@')[0]
        market = self.symbol_market_dict[symbol]
        self.callback_dict[symbol](market, json_node['data']['bids'][0][0], json_node['data']['bids'][0][1],
                                   json_node['data']['asks'][0][0], json_node['data']['asks'][0][1])


if __name__ == '__main__':
    fileConfig('../logging_config.txt')
    # logging.basicConfig(level=logging.INFO)
    logging.getLogger().info('asdfasdfsdf')

    connector = BinancePublicConnector()
    t1 = threading.Thread(target=connector.start)
    t1.start()

    while not connector.is_connect:
        time.sleep(0.1)

    connector.subscribe('BTC-USDT', callback_test)
    # connector.subscribe('ETH-USDT', callback_test)

    # connector.unsubscribe('ETH-USDT')

    # connector.stop()
