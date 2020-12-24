import logging
import threading
import time

from commons.callback import callback_test
from commons.logger_settings import set_logger_by_config
from exchange_connector.binance_public_connector import BinancePublicConnector
from exchange_connector.empty_public_connector import EmptyPublicConnector


class ConnectorFactory:
    BINANCE = 'binance'
    EMPTY = 'empty'

    _instance = None
    _connectors_dict = {}

    @staticmethod
    def get_instance():
        if ConnectorFactory._instance is None:
            ConnectorFactory()
        return ConnectorFactory._instance

    def __init__(self):
        if ConnectorFactory._instance is not None:
            raise Exception('can not have multiple instance')
        else:
            self._id = id(self)
            ConnectorFactory._instance = self

    def get_public_connector(self, name: str):
        if name in self._connectors_dict.keys():
            return self._connectors_dict[name]

        if name == self.BINANCE:
            self._connectors_dict[name] = BinancePublicConnector()
            return self._connectors_dict[name]
        elif name == self.EMPTY:
            self._connectors_dict[name] = EmptyPublicConnector()
            return self._connectors_dict[name]

        logging.error('Unknown exchange:' + name)

    def get_private_connector(self, name: str):
        pass


if __name__ == '__main__':
    set_logger_by_config()
    factory = ConnectorFactory.get_instance()
    connector = factory.get_public_connector(ConnectorFactory.BINANCE)
    # factory.get_public_connector('QQ')

    t1 = threading.Thread(target=connector.start)
    t1.start()

    while not connector.is_connect:
        time.sleep(0.1)

    connector.subscribe('BTC-USDT', callback_test)

    # 故意在new一個instance看看
    # cf = ConnectorFactory()

    # 在拿一次
    connector2 = factory.get_public_connector(ConnectorFactory.BINANCE)
    # unsubscribe如果成功表示singleton work
    connector2.unsubscribe('BTC-USDT')
