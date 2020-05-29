# automatically generated by the FlatBuffers compiler, do not modify

# namespace: guppy_ipc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ClientStats(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsClientStats(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ClientStats()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def ClientStatsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x30\x30\x30\x32", size_prefixed=size_prefixed)

    # ClientStats
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ClientStats
    def InputReadCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # ClientStats
    def OutputReadCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def ClientStatsStart(builder): builder.StartObject(2)
def ClientStatsAddInputReadCount(builder, inputReadCount): builder.PrependUint32Slot(0, inputReadCount, 0)
def ClientStatsAddOutputReadCount(builder, outputReadCount): builder.PrependUint32Slot(1, outputReadCount, 0)
def ClientStatsEnd(builder): return builder.EndObject()
