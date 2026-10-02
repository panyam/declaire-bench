"""Calls into the inventory service."""

import grpc

from inventory.v1 import inventory_pb2, inventory_pb2_grpc


def reserve_for_order(channel: grpc.Channel, order_id: str, sku: str, quantity: int) -> str:
    """Reserves quantity of sku for order_id and returns the reservation id."""
    stub = inventory_pb2_grpc.InventoryServiceStub(channel)
    response = stub.ReserveItem(_request(order_id, sku, quantity))
    return response.reservation_id


def _request(order_id: str, sku: str, quantity: int) -> inventory_pb2.ReserveItemRequest:
    return inventory_pb2.ReserveItemRequest(order_id=order_id, sku=sku, quantity=quantity)


def reserve_at(target: str, order_id: str, sku: str, quantity: int) -> str:
    """Reserves quantity of sku for order_id at target, through grpc's experimental per-call API."""
    response = inventory_pb2_grpc.InventoryService.ReserveItem(_request(order_id, sku, quantity), target, insecure=True)
    return response.reservation_id
