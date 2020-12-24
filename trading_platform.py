from commons.logger_settings import set_logger_by_config
from engine.trading_controller import TradingController


class TradingPlatform:
    _trading_controller = None

    def __init__(self):
        self._trading_controller = TradingController().get_instance()

    def start_strategy(self, strategy_name: str):
        self._trading_controller.register_strategy(strategy_name)

    def stop_strategy(self, strategy_name: str):
        self._trading_controller.stop_strategy(strategy_name)


if __name__ == '__main__':
    set_logger_by_config()
    trading_platform = TradingPlatform()

    while True:
        name = input('input start or stop plus strategy name: ')
        action = name.split(' ')
        if action[0] == 'start':
            trading_platform.start_strategy(action[1])
        elif action[0] == 'stop':
            trading_platform.stop_strategy(action[1])


