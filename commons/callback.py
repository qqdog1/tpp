def callback_test(symbol:str, bid_price: float, bid_qty: float, ask_price: float, ask_qty: float):
    print(symbol, ':', bid_price, '@', bid_qty, " : ", ask_price, '@', ask_qty)