from exchange_connector.connector_factory import ConnectorFactory


class OrderManager:

    def send_order(self, exchange_name: str):
        pass

    def cancel_order(self):
        pass

    def get_balance(self, exchange_name: str):
        return ConnectorFactory.get_instance().get_private_connector(exchange_name).get_balance()
