import abc
import websocket


class MaxPublicConnector(metaclass=abc.ABCMeta):
    def __init__(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(
            "wss://max-stream.maicoin.com/ws",
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        ws.on_open = self.on_open
        ws.run_forever()

    def start(self):
        pass

    def stop(self):
        pass

    def subscribe(self):
        pass

    def unsubscribe(self):
        pass

    def on_open(self):
        print("onOpen")

    def on_message(self, message):
        print(message)

    def on_error(self):
        print("onerror")

    def on_close(self):
        print("onclose")


if __name__ == '__main__':
    connector = MaxPublicConnector()
