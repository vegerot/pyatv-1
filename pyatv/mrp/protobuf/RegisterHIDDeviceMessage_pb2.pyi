# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.VirtualTouchDeviceDescriptorMessage_pb2 import (
    VirtualTouchDeviceDescriptor as pyatv___mrp___protobuf___VirtualTouchDeviceDescriptorMessage_pb2___VirtualTouchDeviceDescriptor,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class RegisterHIDDeviceMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def deviceDescriptor(self) -> pyatv___mrp___protobuf___VirtualTouchDeviceDescriptorMessage_pb2___VirtualTouchDeviceDescriptor: ...

    def __init__(self,
        *,
        deviceDescriptor : typing___Optional[pyatv___mrp___protobuf___VirtualTouchDeviceDescriptorMessage_pb2___VirtualTouchDeviceDescriptor] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RegisterHIDDeviceMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"deviceDescriptor"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"deviceDescriptor"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"deviceDescriptor",b"deviceDescriptor"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"deviceDescriptor",b"deviceDescriptor"]) -> None: ...

registerHIDDeviceMessage = ... # type: google___protobuf___descriptor___FieldDescriptor
