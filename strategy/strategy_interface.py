import abc


class StrategyInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'start') and
                callable(subclass.start) and
                hasattr(subclass, 'stop') and
                callable(subclass.stop) and
                hasattr(subclass, 'get_trading_market') and
                callable(subclass.get_trading_market))

    @abc.abstractmethod
    def start(self):
        raise NotImplementedError

    @abc.abstractmethod
    def stop(self):
        raise NotImplementedError

    # 回傳這個strategy要交易的商品
    # 架構會是python dict
    # exchange name : [market array]
    @abc.abstractmethod
    def get_trading_market(self):
        raise NotImplementedError
