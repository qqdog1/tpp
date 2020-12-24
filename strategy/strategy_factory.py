import logging

from engine.trading_elements import TradingElements
from strategy.simple_strategy import SimpleStrategy
from strategy.supported_strategy import SIMPLE


class StrategyFactory:
    _instance = None
    _strategies_dict = {}

    @staticmethod
    def get_instance():
        if StrategyFactory._instance is None:
            StrategyFactory()
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

        if name == SIMPLE:
            self._strategies_dict[name] = SimpleStrategy(trading_elements)
            return self._strategies_dict[name]

        logging.error('Unknown strategy:' + name)
