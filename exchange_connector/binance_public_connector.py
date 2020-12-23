import abc
import threading
import time

import websocket


class BinancePublicConnector(metaclass=abc.ABCMeta):
    def __init__(self):
        self.connect = False
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            # "wss://stream.binance.com:9443/ws/btcusdt@depth",
            "wss://stream.binance.com:9443/ws",
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.on_open = self.on_open

    @property
    def is_connect(self):
        return self.connect

    def start(self):
        self.ws.run_forever()

    def subscribe(self, market: str, callback):
        pass

    def unsubscribe(self):
        pass

    def on_open(self):
        print("onOpen")
        self.connect = True

    def on_message(self, message):
        print(message)

    def on_error(self):
        print("onerror")

    def on_close(self):
        print("onclose")


if __name__ == '__main__':
    connector = BinancePublicConnector()
    t1 = threading.Thread(target=connector.start)
    t1.start()

    while True:
        print("is connect :", connector.is_connect)
        time.sleep(1)
