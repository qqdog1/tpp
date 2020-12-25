class PriceCache:
    _last_buy = {}
    _last_sell = {}

    def get_last_buy(self, exchange_name: str, market: str) -> [float]:
        if exchange_name in self._last_buy.keys():
            if market in self._last_buy[exchange_name].keys():
                return self._last_buy[exchange_name][market]
        return [0, 0]

    def get_last_sell(self, exchange_name: str, market: str) -> [float]:
        if exchange_name in self._last_sell.keys():
            if market in self._last_sell[exchange_name].keys():
                return self._last_sell[exchange_name][market]
        return [0, 0]

    def set_last_buy(self, exchange_name: str, market: str, price: float, qty: float):
        if exchange_name not in self._last_buy.keys():
            self._last_buy[exchange_name] = {}
        self._last_buy[exchange_name][market] = [price, qty]

    def set_last_sell(self, exchange_name: str, market: str, price: float, qty: float):
        if exchange_name not in self._last_sell.keys():
            self._last_sell[exchange_name] = {}
        self._last_sell[exchange_name][market] = [price, qty]


if __name__ == '__main__':
    cache = PriceCache()
    print(cache.get_last_sell('QQ', 'kk'))
    cache.set_last_buy('QQ', 'kk', 9.1, 8.765)
    print(cache.get_last_buy('QQ', 'kk'))
    print(type(cache.get_last_buy('QQ', 'kk')[0]))
