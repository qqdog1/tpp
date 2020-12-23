import abc


class PublicConnectorInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'subscribe') and
                callable(subclass.subscribe) and
                hasattr(subclass, 'unsubscribe') and
                callable(subclass.unsubscribe))

    @abc.abstractmethod
    def subscribe(self, market: str):
        raise NotImplementedError

    @abc.abstractmethod
    def unsubscribe(self, market: str):
        raise NotImplementedError
