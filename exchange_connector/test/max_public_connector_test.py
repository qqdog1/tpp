import unittest

from exchange_connector.max_public_connector import MaxPublicConnector


class MaxPublicConnectorTest(unittest.TestCase):
    def test_is_connect(self):
        connector = MaxPublicConnector();
