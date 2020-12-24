import threading
import time

from commons.callback import callback_test
from commons.logger_settings import set_logger_by_config
from exchange_connector.binance_public_connector import BinancePublicConnector
from exchange_connector.max_public_connector import MaxPublicConnector


class ConnectorFactory:
    BINANCE = 'binance'
    MAX = 'max'

    _instance = None

    @staticmethod
    def get_instance():
        if ConnectorFactory._instance is None:
            ConnectorFactory()
        return ConnectorFactory._instance

    def __init__(self):
        if ConnectorFactory._instance is not None:
            raise Exception('can not have multiple factory')
        else:
            self._id = id(self)
            ConnectorFactory._instance = self
        self.connectors_dist = {}

    def get_public_connector(self, name: str):
        if name in self.connectors_dist.keys():
            return self.connectors_dist[name]

        if name == self.BINANCE:
            connector = BinancePublicConnector()
            self.connectors_dist[name] = connector
            return connector
        elif name == self.MAX:
            connector = MaxPublicConnector()
            self.connectors_dist[name] = connector
            return connector


if __name__ == '__main__':
    set_logger_by_config()
    factory = ConnectorFactory.get_instance()
    connector = factory.get_public_connector(ConnectorFactory.BINANCE)

    t1 = threading.Thread(target=connector.start)
    t1.start()

    while not connector.is_connect:
        time.sleep(0.1)

    connector.subscribe('BTC-USDT', callback_test)
