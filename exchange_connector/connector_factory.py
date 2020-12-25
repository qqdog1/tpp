import logging
import threading
import time
from commons.callback import callback_test
from commons.logger_settings import console_logger_settings
from exchange_connector.binance_private_connector import BinancePrivateConnector
from exchange_connector.binance_public_connector import BinancePublicConnector
from exchange_connector.empty_private_connector import EmptyPrivateConnector
from exchange_connector.empty_public_connector import EmptyPublicConnector
from exchange_connector.supported_exchange import BINANCE, EMPTY


class ConnectorFactory:
    _instance = None
    _public_connector_dict = {}
    _private_connector_dict = {}

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

    def get_public_connector(self, exchange_name: str):
        if exchange_name in self._public_connector_dict.keys():
            return self._public_connector_dict[exchange_name]

        if exchange_name == BINANCE:
            self._public_connector_dict[exchange_name] = BinancePublicConnector()
            return self._public_connector_dict[exchange_name]
        elif exchange_name == EMPTY:
            self._public_connector_dict[exchange_name] = EmptyPublicConnector()
            return self._public_connector_dict[exchange_name]

        logging.error('can not get public connector, unknown exchange:' + exchange_name)

    def get_private_connector(self, exchange_name: str):
        if exchange_name in self._private_connector_dict.keys():
            return self._private_connector_dict[exchange_name]

        if exchange_name == BINANCE:
            self._private_connector_dict[exchange_name] = BinancePrivateConnector()
            return self._private_connector_dict[exchange_name]
        elif exchange_name == EMPTY:
            self._private_connector_dict[exchange_name] = EmptyPrivateConnector()
            return self._private_connector_dict[exchange_name]

        logging.error('can not get private connector, unknown exchange:' + exchange_name)


if __name__ == '__main__':
    console_logger_settings()
    factory = ConnectorFactory.get_instance()
    connector = factory.get_public_connector(BINANCE)
    # factory.get_public_connector('QQ')

    t1 = threading.Thread(target=connector.start)
    t1.start()

    while not connector.is_connect:
        time.sleep(0.1)

    connector.subscribe('BTC-USDT', callback_test)

    # 故意在new一個instance看看
    # cf = ConnectorFactory()

    # 在拿一次
    connector2 = factory.get_public_connector(BINANCE)
    # unsubscribe如果成功表示singleton work
    connector2.unsubscribe('BTC-USDT')
