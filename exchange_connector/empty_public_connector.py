import abc

from commons.logger_settings import set_logger_by_config


class EmptyPublicConnector(metaclass=abc.ABCMeta):
    _connect_status = False

    @property
    def is_connect(self):
        return self._connect_status

    def start(self):
        self._connect_status = True

    def stop(self):
        self._connect_status = False

    def subscribe(self, market: str, callback):
        pass

    def unsubscribe(self, market: str):
        pass


if __name__ == '__main__':
    set_logger_by_config()
    connector = EmptyPublicConnector()
    print(connector.is_connect)
    connector.start()
    print(connector.is_connect)