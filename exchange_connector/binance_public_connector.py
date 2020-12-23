import abc
import json
import threading
import time

import websocket


def callback_test(symbol:str, bid_price: float, bid_qty: float, ask_price: float, ask_qty: float):
    print(symbol, ':', bid_price, '@', bid_qty, " : ", ask_price, '@', ask_qty)


class BinancePublicConnector(metaclass=abc.ABCMeta):
    def __init__(self):
        self.connect_status = False
        self.callback_dict = {}
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            # "wss://stream.binance.com:9443/stream?streams=" + topics,
            "wss://stream.binance.com:9443/ws",
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
        message = '{"method":"SUBSCRIBE","params":["' + symbol + '@depth5"],"id":1}'
        self.ws.send(message)

    def unsubscribe(self, market: str):
        symbol = market.replace('-', '').lower()
        if symbol in self.callback_dict.keys():
            self.callback_dict.pop(symbol)

    def on_open(self):
        print("onOpen")
        self.connect_status = True

    def on_message(self, message):
        json_node = json.loads(message)
        if 'lastUpdateId' in json_node:
            self.parse_book(json_node)

    def on_error(self):
        print("onerror")
        self.connect_status = False

    def on_close(self):
        print("onclose")
        self.connect_status = False

    def parse_book(self, json_node):
        print(json_node)
        print(json_node['bids'][0][0])


if __name__ == '__main__':
    connector = BinancePublicConnector()
    t1 = threading.Thread(target=connector.start)
    t1.start()

    while not connector.is_connect:
        time.sleep(0.1)

    connector.subscribe('BTC-USDT', callback_test)
    connector.subscribe('ETH-USDT', callback_test)

    connector.stop()
