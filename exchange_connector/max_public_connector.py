import abc
from websocket import WebSocketApp


class MessageFunc(object):
    pass


class ErrorFunc(object):
    pass


class CloseFunc(object):
    pass


class OpenFunc(object):
    print(object)


class MaxPublicConnector(metaclass=abc.ABCMeta):
    def __init__(self):
        ws = WebSocketApp(
            'wss://max-stream.maicoin.com/ws',
            on_message=MessageFunc,
            on_error=ErrorFunc,
            on_close=CloseFunc
        )
        ws.on_open = OpenFunc
        ws.run_forever()

    def subscribe(self):
        pass

    def unsubscribe(self):
        pass


if __name__ == '__main__':
    connector = MaxPublicConnector()
