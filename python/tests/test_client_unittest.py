import unittest

from inventory_client.client import reserve_for_order
from tests.fakes import FakeChannel


class ChannelCase(unittest.TestCase):
    def setUp(self):
        self.channel = FakeChannel("order-2-1")


class ReserveForOrderCase(ChannelCase):
    def test_sends_one_request(self):
        reserve_for_order(self.channel, "order-2", "sku-1", 1)
        self.assertEqual(len(self.channel.requests), 1)
