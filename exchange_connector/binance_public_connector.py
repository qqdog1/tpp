import abc
import json
import logging
import threading
import time
import websocket
from commons.callback import callback_test
from commons.logger_settings import console_logger_settings
from exchange_connector.supported_exchange import BINANCE


class BinancePublicConnector(metaclass=abc.ABCMeta):
    _connect_status = False
    _callback_dict = {}
    _symbol_market_dict = {}
    _ws = None

    def __init__(self):
        websocket.enableTrace(True)
        self._ws = websocket.WebSocketApp(
            'wss://stream.binance.com/stream',
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self._ws.on_open = self.on_open

    def is_connect(self):
        return self._connect_status

    def start(self):
        self._ws.run_forever()

    def stop(self):
        self._ws.keep_running = False

    def subscribe(self, market: str, callback):
        # 要有queue 如果is connect = false, 變true要幫subscribe queue
        symbol = market.replace('-', '').lower()
        self._callback_dict[symbol] = callback
        self._symbol_market_dict[symbol] = market
        message = '{"method":"SUBSCRIBE","params":["' + symbol + '@depth5"],"id":1}'
        self._ws.send(message)

    def unsubscribe(self, market: str):
        symbol = market.replace('-', '').lower()
        if symbol in self._callback_dict.keys():
            self._callback_dict.pop(symbol)
            message = '{"method":"UNSUBSCRIBE","params":["' + symbol + '@depth5"],"id":1}'
            self._ws.send(message)

    def on_open(self):
        logging.info('websocket connected.')
        self._connect_status = True

    def on_message(self, message):
        json_node = json.loads(message)
        if 'stream' in json_node:
            topic = str(json_node['stream'])
            if 'depth' in topic:
                self.parse_book(json_node)

    def on_error(self):
        logging.info('websocket on error.')
        self._connect_status = False
        self.reconnect()

    def on_close(self):
        logging.info('websocket closed.')
        self._connect_status = False
        self.reconnect()

    def reconnect(self):
        pass

    def parse_book(self, json_node):
        topic = str(json_node['stream'])
        symbol = topic.split('@')[0]
        market = self._symbol_market_dict[symbol]
        self._callback_dict[symbol](BINANCE, market,
                                    float(json_node['data']['bids'][0][0]),
                                    float(json_node['data']['bids'][0][1]),
                                    float(json_node['data']['asks'][0][0]),
                                    float(json_node['data']['asks'][0][1]))


if __name__ == '__main__':
    console_logger_settings()

    connector = BinancePublicConnector()
    t1 = threading.Thread(target=connector.start)
    t1.start()

    while not connector.is_connect:
        time.sleep(0.1)

    connector.subscribe('BTC-USDT', callback_test)
    # connector.subscribe('ETH-USDT', callback_test)

    # connector.unsubscribe('ETH-USDT')

    # connector.stop()
