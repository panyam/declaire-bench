from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Item(_message.Message):
    __slots__ = ("sku", "name", "on_hand")
    SKU_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ON_HAND_FIELD_NUMBER: _ClassVar[int]
    sku: str
    name: str
    on_hand: int
    def __init__(self, sku: _Optional[str] = ..., name: _Optional[str] = ..., on_hand: _Optional[int] = ...) -> None: ...

class GetItemRequest(_message.Message):
    __slots__ = ("sku",)
    SKU_FIELD_NUMBER: _ClassVar[int]
    sku: str
    def __init__(self, sku: _Optional[str] = ...) -> None: ...

class GetItemResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: Item
    def __init__(self, item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class ReserveItemRequest(_message.Message):
    __slots__ = ("order_id", "sku", "quantity")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    sku: str
    quantity: int
    def __init__(self, order_id: _Optional[str] = ..., sku: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...

class ReserveItemResponse(_message.Message):
    __slots__ = ("reservation_id", "remaining")
    RESERVATION_ID_FIELD_NUMBER: _ClassVar[int]
    REMAINING_FIELD_NUMBER: _ClassVar[int]
    reservation_id: str
    remaining: int
    def __init__(self, reservation_id: _Optional[str] = ..., remaining: _Optional[int] = ...) -> None: ...
