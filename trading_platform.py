from commons import logger_settings
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
    logger_settings.import_default_logger_settings()
    trading_platform = TradingPlatform()
    print('input start plus strategy_name or stop plus strategy_name to operate your strategy')
    print('or exit to exit the program')

    while True:
        name = input('> ')
        action = name.split(' ')
        if action[0] == 'start':
            trading_platform.start_strategy(action[1])
        elif action[0] == 'stop':
            trading_platform.stop_strategy(action[1])
        elif action[0] == 'exit':
            exit()
