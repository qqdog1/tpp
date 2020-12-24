# 這個物件應該要細到以strategy為單位
# 目前就讓所有strategy共用一個
class TradingElements:
    _order_manager = None
    _price_cache = None
    _account_manager = None

    def __init__(self):
        pass

    def get_balance(self):
        pass

    def get_last_buy(self):
        pass

    def get_last_sell(self):
        pass

    def send_order(self):
        pass
