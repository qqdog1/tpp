import abc
import threading
import time

from commons.callback import callback_test
from commons.logger_settings import set_logger_by_config


class EmptyPublicConnector(metaclass=abc.ABCMeta):
    _connect_status = False
    _callback_dict = {}

    @property
    def is_connect(self):
        return self._connect_status

    def start(self):
        self._connect_status = True
        while self._connect_status:
            for market in self._callback_dict.keys():
                self._callback_dict[market](market, 1, 2, 3, 4)
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
    set_logger_by_config()
    connector = EmptyPublicConnector()
    print(connector.is_connect)
    t1 = threading.Thread(target=connector.start)
    t1.start()
    print(connector.is_connect)
    connector.subscribe('BTC-USDT', callback_test)
    connector.subscribe('QQaa', callback_test)
    connector.unsubscribe('QQaa')

    # connector.stop()
