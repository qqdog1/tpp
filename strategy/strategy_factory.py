import logging

from engine.trading_elements import TradingElements
from strategy.simple_strategy import SimpleStrategy


class StrategyFactory:
    SIMPLE = 'simple'

    _instance = None
    _strategies_dist = {}
    _trading_elements = None

    @staticmethod
    def get_instance(trading_elements: TradingElements):
        if StrategyFactory._instance is None:
            StrategyFactory(trading_elements)
        return StrategyFactory._instance

    def __init__(self, trading_elements: TradingElements):
        if StrategyFactory._instance is not None:
            raise Exception('can not have multiple instance')
        else:
            self._id = id(self)
            StrategyFactory._instance = self
            self._trading_elements = trading_elements

    def get_strategy(self, name: str):
        if name in self._strategies_dist.keys():
            return self._strategies_dist[name]

        if name == self.SIMPLE:
            self._strategies_dist[name] = SimpleStrategy(self._trading_elements)
            return self._strategies_dist[name]

        logging.error('Unknown strategy:' + name)
