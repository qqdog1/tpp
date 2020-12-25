import abc
import random
import threading
import time
from commons.callback import callback_test
from commons.logger_settings import console_logger_settings
from exchange_connector.supported_exchange import EMPTY


class EmptyPublicConnector(metaclass=abc.ABCMeta):
    _connect_status = False
    _callback_dict = {}

    def is_connect(self):
        return self._connect_status

    def start(self):
        self._connect_status = True
        while self._connect_status:
            price = random.uniform(8000, 10000)
            qty = random.uniform(0.5, 3)
            for market in self._callback_dict.keys():
                self._callback_dict[market](EMPTY, market, price, qty, price + 100, qty + 1)
            time.sleep(1)

    def stop(self):
        self._connect_status = False

    def subscribe(self, market: str, callback):
        if self._connect_status:
            self._callback_dict[market] = callback

    def unsubscribe(self, market: str):
        if self._connect_status:
            if market in self._callback_dict.keys():
                self._callback_dict.pop(market)


if __name__ == '__main__':
    console_logger_settings()
    connector = EmptyPublicConnector()
    print(connector.is_connect)
    t1 = threading.Thread(target=connector.start)
    t1.start()
    print(connector.is_connect)
    connector.subscribe('BTC-USDT', callback_test)
    connector.subscribe('QQaa', callback_test)
    connector.unsubscribe('QQaa')

    # connector.stop()
