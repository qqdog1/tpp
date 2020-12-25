import abc
import logging
import time

from engine.trading_elements import TradingElements
from exchange_connector.supported_exchange import EMPTY, BINANCE


class SimpleStrategy(metaclass=abc.ABCMeta):
    _trading_market_dict = {}
    _running_status = False
    _trading_elements = None
    _last_buy_price = float(0)
    _last_sell_price = float(0)
    _last_balance_dict = {}

    def __init__(self, trading_elements: TradingElements):
        self._trading_elements = trading_elements
        trading_markets = ['BTC-USDT', 'ETH-USDT']
        self._trading_market_dict[BINANCE] = trading_markets
        # self._trading_market_dict[EMPTY] = trading_markets

    # 這個start 也是要等connector都準備好才能被叫起來
    def start(self):
        self._running_status = True
        # while loop 可以改成讓trading controller去控制
        self._last_balance_dict = self._trading_elements.get_balance(BINANCE)
        if self._last_balance_dict is not None:
            logging.info('strategy init balance: ')
            logging.info(self._last_balance_dict)
        while self._running_status:
            self._strategy_logic()
            time.sleep(1)

    def stop(self):
        self._running_status = False

    def get_trading_market(self):
        return self._trading_market_dict

    def _strategy_logic(self):
        # 不應該在這邊做 要在交易一個cycle後檢查
        # if not self._is_balance_growing():
        #     self._force_stop()

        buy = self._trading_elements.get_last_buy(BINANCE, 'BTC-USDT')
        sell = self._trading_elements.get_last_sell(BINANCE, 'BTC-USDT')

        # 還沒價格近來只做update
        if self._last_buy_price == 0 or self._last_sell_price == 0:
            self._update_price()
            return
        else:
            if buy[0] / self._last_buy_price > 1.1:
                self._trading_elements.send_order()
            elif sell[0] / self._last_sell_price < 0.9:
                self._trading_elements.send_order()
            self._update_price()

    def _is_balance_growing(self):
        if self._last_balance_dict is None:
            self._last_balance_dict = self._trading_elements.get_balance()
            return True
        else:
            new_balance_dict = self._trading_elements.get_balance()
            for currency in self._last_balance_dict.keys():
                if currency in new_balance_dict.keys():
                    if new_balance_dict[currency] < self._last_balance_dict[currency]:
                        return False
                else:
                    # 回傳的balance連currency都不見表示被歸零了
                    return False
        return True

    def _update_price(self):
        buy = self._trading_elements.get_last_buy(BINANCE, 'BTC-USDT')
        sell = self._trading_elements.get_last_sell(BINANCE, 'BTC-USDT')
        self._last_buy_price = buy[0]
        self._last_sell_price = sell[0]
        logging.debug('price update:' + str(self._last_buy_price) + ":" + str(self._last_sell_price))

    def _force_stop(self):
        logging.error('balance decrease, stop this strategy')
        self._running_status = False
