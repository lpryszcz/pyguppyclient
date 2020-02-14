# automatically generated by the FlatBuffers compiler, do not modify

# namespace: guppy_ipc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MessageData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMessageData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MessageData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def MessageDataBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x30\x30\x30\x31", size_prefixed=size_prefixed)

    # MessageData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MessageData
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from pyguppyclient.guppy_ipc.ProtocolVersion import ProtocolVersion
            obj = ProtocolVersion()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MessageData
    def SenderId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MessageData
    def ContentType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # MessageData
    def Content(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def MessageDataStart(builder): builder.StartObject(4)
def MessageDataAddVersion(builder, version): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(version), 0)
def MessageDataAddSenderId(builder, senderId): builder.PrependUint32Slot(1, senderId, 0)
def MessageDataAddContentType(builder, contentType): builder.PrependUint8Slot(2, contentType, 0)
def MessageDataAddContent(builder, content): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(content), 0)
def MessageDataEnd(builder): return builder.EndObject()
