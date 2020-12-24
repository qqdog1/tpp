import logging
import threading

from engine.trading_elements import TradingElements
from strategy.strategy_factory import StrategyFactory
from strategy.strategy_interface import StrategyInterface


class TradingController:
    _instance = None
    _strategy_factory = None
    _trading_elements = None
    _strategy_dict = {}

    @staticmethod
    def get_instance():
        if TradingController._instance is None:
            TradingController()
        return TradingController._instance

    def __init__(self):
        if TradingController._instance is not None:
            raise Exception('can not have multiple instance')
        else:
            self._id = id(self)
            TradingController._instance = self
        self._strategy_factory = StrategyFactory()
        self._trading_elements = TradingElements()

    def register_strategy(self, strategy_name: str):
        if strategy_name not in self._strategy_dict.keys():
            strategy = self._strategy_factory.get_strategy(strategy_name, self._trading_elements)
            self._strategy_dict[strategy_name] = strategy
            self._run_strategy(strategy)
        else:
            logging.warning(strategy_name + 'strategy is already running.')

    def _run_strategy(self, strategy: StrategyInterface):
        t = threading.Thread(target=strategy.start())
        t.start()

    def stop_strategy(self, strategy_name: str):
        if strategy_name in self._strategy_dict.keys():
            self._strategy_dict.pop(strategy_name).stop()
        else:
            logging.error('can stop strategy, ' + strategy_name + 'strategy not exist.')
