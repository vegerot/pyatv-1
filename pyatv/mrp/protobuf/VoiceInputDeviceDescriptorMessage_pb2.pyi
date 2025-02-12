# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.AudioFormatSettingsMessage_pb2 import (
    AudioFormatSettings as pyatv___mrp___protobuf___AudioFormatSettingsMessage_pb2___AudioFormatSettings,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class VoiceInputDeviceDescriptor(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def defaultFormat(self) -> pyatv___mrp___protobuf___AudioFormatSettingsMessage_pb2___AudioFormatSettings: ...

    @property
    def supportedFormats(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[pyatv___mrp___protobuf___AudioFormatSettingsMessage_pb2___AudioFormatSettings]: ...

    def __init__(self,
        *,
        defaultFormat : typing___Optional[pyatv___mrp___protobuf___AudioFormatSettingsMessage_pb2___AudioFormatSettings] = None,
        supportedFormats : typing___Optional[typing___Iterable[pyatv___mrp___protobuf___AudioFormatSettingsMessage_pb2___AudioFormatSettings]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> VoiceInputDeviceDescriptor: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"defaultFormat"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"defaultFormat",u"supportedFormats"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"defaultFormat",b"defaultFormat"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"defaultFormat",b"defaultFormat",u"supportedFormats",b"supportedFormats"]) -> None: ...
