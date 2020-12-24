import abc

from engine.order_manager import OrderManager
from engine.price_cache import PriceCache
from exchange_connector.connector_factory import ConnectorFactory


class SimpleStrategy(metaclass=abc.ABCMeta):
    _trading_market_dist = {}
    _running_status = False
    _price_cache = None
    _order_manager = None

    def __init__(self, price_cache: PriceCache, order_manager: OrderManager):
        self._price_cache = price_cache
        self._order_manager = order_manager
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
