# 這個物件應該要細到以strategy為單位
# 目前就讓所有strategy共用一個
from engine.order_manager import OrderManager
from engine.price_cache import PriceCache


class TradingElements:
    _order_manager = None
    _price_cache = None

    def __init__(self):
        self._order_manager = OrderManager()
        self._price_cache = PriceCache()

    def get_balance(self, exchange_name: str):
        return self._order_manager.get_balance(exchange_name)

    def get_last_buy(self, exchange_name: str, market: str) -> [float]:
        return self._price_cache.get_last_buy(exchange_name, market)

    def get_last_sell(self, exchange_name: str, market: str) -> [float]:
        return self._price_cache.get_last_sell(exchange_name, market)

    def set_last_buy(self, exchange_name: str, market: str, price: float, qty: float):
        self._price_cache.set_last_buy(exchange_name, market, price, qty)

    def set_last_sell(self, exchange_name: str, market: str, price: float, qty: float):
        self._price_cache.set_last_sell(exchange_name, market, price, qty)

    def send_order(self):
        return self._order_manager.send_order()

    def cancel_order(self):
        return self._order_manager.cancel_order()
