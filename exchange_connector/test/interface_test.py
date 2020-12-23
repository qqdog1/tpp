import unittest

from exchange_connector import max_public_connector, public_connector_interface, binance_public_connector


class InterfaceTest(unittest.TestCase):
    def test_is_subclass(self):
        self.assertTrue(
            issubclass(max_public_connector.MaxPublicConnector, public_connector_interface.PublicConnectorInterface))
        self.assertTrue(
            issubclass(binance_public_connector.BinancePublicConnector, public_connector_interface.PublicConnectorInterface))


if __name__ == '__main__':
    unittest.main()
