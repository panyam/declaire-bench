from inventory_client.client import reserve_for_order
from tests.fakes import FakeChannel


def reserve(channel: FakeChannel) -> str:
    return reserve_for_order(channel, "order-1", "sku-1", 3)


def test_returns_the_reservation_id():
    assert reserve(FakeChannel("order-1-1")) == "order-1-1"


class TestReserveForOrder:
    def test_sends_the_order(self):
        channel = FakeChannel("order-1-1")
        reserve(channel)
        assert [(r.order_id, r.sku, r.quantity) for r in channel.requests] == [("order-1", "sku-1", 3)]
