"""A channel that answers ReserveItem without a server."""

from inventory.v1 import inventory_pb2


class FakeChannel:
    """Records each ReserveItem request and answers with a fixed reservation id."""

    def __init__(self, reservation_id: str):
        self.reservation_id = reservation_id
        self.requests = []

    def unary_unary(self, method, request_serializer=None, response_deserializer=None, _registered_method=None):
        def call(request, **kwargs):
            self.requests.append(request)
            return inventory_pb2.ReserveItemResponse(reservation_id=self.reservation_id, remaining=0)

        return call
