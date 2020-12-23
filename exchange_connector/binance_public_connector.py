import abc
import websocket


class BinancePublicConnector(metaclass=abc.ABCMeta):
    def __init__(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(
            # "wss://stream.binance.com:9443/ws/btcusdt@depth",
            "wss://stream.binance.com:9443/ws",
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        ws.on_open = self.on_open
        ws.run_forever()

    @property
    def ws(self):
        return self.ws

    @property
    def is_connect(self):
        return self.is_connect

    def subscribe(self, market: str, callback):
        pass

    def unsubscribe(self):
        pass

    def on_open(self):
        print("onOpen")
        is_connect = True

    def on_message(self, message):
        print(message)

    def on_error(self):
        print("onerror")

    def on_close(self):
        print("onclose")


if __name__ == '__main__':
    connector = BinancePublicConnector()
    print(connector.is_connect)
