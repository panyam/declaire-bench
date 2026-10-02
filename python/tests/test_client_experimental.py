import grpc.experimental

from inventory.v1 import inventory_pb2
from inventory_client.client import reserve_at


def test_reserve_at_calls_the_target(monkeypatch):
    calls = []

    def unary_unary(request, target, method, *args, **kwargs):
        calls.append((target, method, request.order_id))
        return inventory_pb2.ReserveItemResponse(reservation_id="order-3-1", remaining=0)

    monkeypatch.setattr(grpc.experimental, "unary_unary", unary_unary)
    assert reserve_at("inventory:50051", "order-3", "sku-1", 1) == "order-3-1"
    assert calls == [("inventory:50051", "/inventory.v1.InventoryService/ReserveItem", "order-3")]
