class PriceCache:
    _last_buy = {}
    _last_sell = {}

    def get_last_buy(self, market: str):
        if market in self._last_buy.keys():
            return self._last_buy[market]
        return [0, 0]

    def get_last_sell(self, market: str):
        if market in self._last_sell.keys():
            return self._last_sell[market]
        return [0, 0]

    def set_last_buy(self, market: str, price: float, qty: float):
        self._last_buy[market] = [price, qty]

    def set_last_sell(self, market: str, price: float, qty: float):
        self._last_sell[market] = [price, qty]


if __name__ == '__main__':
    cache = PriceCache()
    print(cache.get_last_sell('QQ'))
    cache.set_last_buy('QQ', 9.1, 8.765)
    print(cache.get_last_buy('QQ'))
