from commons.logger_settings import set_logger_by_config
from engine.trading_controller import TradingController


class TradingPlatform:
    _trading_controller = None

    def __init__(self):
        self._trading_controller = TradingController().get_instance()

    def start_strategy(self, strategy_name: str):
        self._trading_controller.register_strategy(strategy_name)
        pass


if __name__ == '__main__':
    set_logger_by_config()
    trading_platform = TradingPlatform()
    name = input('input strategy name: ')
    trading_platform.start_strategy(name)

