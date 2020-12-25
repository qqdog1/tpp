import abc


class PrivateConnectorInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_balance') and
                callable(subclass.get_balance) and
                hasattr(subclass, 'send_order') and
                callable(subclass.send_order))

    @abc.abstractmethod
    def get_balance(self):
        raise NotImplementedError

    @abc.abstractmethod
    def send_order(self):
        raise NotImplementedError

    @abc.abstractmethod
    def cancel_order(self):
        raise NotImplementedError
