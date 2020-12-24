import abc
import logging
import time

from engine.trading_elements import TradingElements
from exchange_connector.supported_exchange import EMPTY


class SimpleStrategy(metaclass=abc.ABCMeta):
    _trading_market_dict = {}
    _running_status = False
    _trading_elements = None

    def __init__(self, trading_elements: TradingElements):
        self._trading_elements = trading_elements
        trading_markets = ['BTC-USD', 'ETH-USD']
        # self._trading_market_dict[BINANCE] = trading_markets
        self._trading_market_dict[EMPTY] = trading_markets

    def start(self):
        self._running_status = True
        while self._running_status:
            buy = self._trading_elements.get_last_buy('BTC-USDT')
            sell = self._trading_elements.get_last_sell('BTC-USDT')
            logging.info(buy[0] + buy[1] + sell[0] + sell[1])
            time.sleep(1)

    def stop(self):
        self._running_status = False

    def get_trading_market(self):
        return self._trading_market_dict
