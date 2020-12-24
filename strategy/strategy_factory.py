import logging

from engine.trading_elements import TradingElements
from strategy.simple_strategy import SimpleStrategy


class StrategyFactory:
    SIMPLE = 'simple'

    _instance = None
    _strategies_dict = {}

    @staticmethod
    def get_instance(trading_elements: TradingElements):
        if StrategyFactory._instance is None:
            StrategyFactory(trading_elements)
        return StrategyFactory._instance

    def __init__(self):
        if StrategyFactory._instance is not None:
            raise Exception('can not have multiple instance')
        else:
            self._id = id(self)
            StrategyFactory._instance = self

    def get_strategy(self, name: str, trading_elements: TradingElements):
        if name in self._strategies_dict.keys():
            return self._strategies_dict[name]

        if name == self.SIMPLE:
            self._strategies_dict[name] = SimpleStrategy(trading_elements)
            return self._strategies_dict[name]

        logging.error('Unknown strategy:' + name)
