import logging
import threading
from engine.trading_elements import TradingElements
from exchange_connector.connector_factory import ConnectorFactory
from exchange_connector.public_connector_interface import PublicConnectorInterface
from strategy.strategy_factory import StrategyFactory
from strategy.strategy_interface import StrategyInterface


def _run_public_connector(exchange_connector: PublicConnectorInterface):
    t = threading.Thread(target=exchange_connector.start)
    t.start()


def _run_strategy(strategy: StrategyInterface):
    t = threading.Thread(target=strategy.start)
    t.start()


class TradingController:
    _instance = None
    _strategy_factory = None
    _connector_factory = None
    _trading_elements = None
    _strategy_dict = {}
    _connector_dict = {}

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
        self._strategy_factory = StrategyFactory().get_instance()
        self._connector_factory = ConnectorFactory().get_instance()
        self._trading_elements = TradingElements()

    def register_strategy(self, strategy_name: str):
        if strategy_name not in self._strategy_dict.keys():
            strategy = self._strategy_factory.get_strategy(strategy_name, self._trading_elements)
            if strategy is not None:
                self._strategy_dict[strategy_name] = strategy
                self._subscribe_market(strategy)
                _run_strategy(strategy)
            else:
                logging.warning(strategy_name + ' strategy not found.')
        else:
            logging.warning(strategy_name + 'strategy is already running.')

    def _subscribe_market(self, strategy: StrategyInterface):
        trading_market = strategy.get_trading_market()
        for exchange_name in trading_market.keys():
            if exchange_name not in self._connector_dict.keys():
                connector = self._connector_factory.get_public_connector(exchange_name)
                self._connector_dict[exchange_name] = connector
                _run_public_connector(connector)
            for market in trading_market[exchange_name]:
                self._connector_dict[exchange_name].subscribe(market, self.on_price_update)

    def stop_strategy(self, strategy_name: str):
        if strategy_name in self._strategy_dict.keys():
            self._strategy_dict.pop(strategy_name).stop()
        # 要對strategy所有market做整理 停掉的時候才有辦法unsubscribe
        else:
            logging.error('can stop strategy, ' + strategy_name + ' strategy not exist.')

    def on_price_update(self, exchange_name: str, market: str,
                        buy_price: float, buy_qty: float, sell_price: float, sell_qty: float):
        self._trading_elements.set
