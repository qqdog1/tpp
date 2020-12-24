import abc
from engine.trading_elements import TradingElements
from exchange_connector.connector_factory import ConnectorFactory


class SimpleStrategy(metaclass=abc.ABCMeta):
    _trading_market_dist = {}
    _running_status = False
    _trading_elements = None

    def __init__(self, trading_elements: TradingElements):
        self._trading_elements = trading_elements
        trading_markets = ['BTC-USD', 'ETH-USD']
        self._trading_market_dist[ConnectorFactory.BINANCE] = trading_markets
        self._trading_market_dist[ConnectorFactory.EMPTY] = trading_markets

    def start(self):
        self._running_status = True
        while self._running_status:
            pass

    def stop(self):
        self._running_status = False

    def get_trading_market(self):
        return self._trading_market_dist
