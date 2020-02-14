# automatically generated by the FlatBuffers compiler, do not modify

# namespace: guppy_ipc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BarcodeArrangementResults(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBarcodeArrangementResults(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BarcodeArrangementResults()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def BarcodeArrangementResultsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x30\x30\x30\x31", size_prefixed=size_prefixed)

    # BarcodeArrangementResults
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BarcodeArrangementResults
    def BarcodeTrimFront(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # BarcodeArrangementResults
    def BarcodeTrimRear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # BarcodeArrangementResults
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BarcodeArrangementResults
    def NormalisedId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BarcodeArrangementResults
    def Kit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BarcodeArrangementResults
    def Variant(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BarcodeArrangementResults
    def Score(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # BarcodeArrangementResults
    def Front(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from pyguppyclient.guppy_ipc.BarcodeResults import BarcodeResults
            obj = BarcodeResults()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BarcodeArrangementResults
    def Back(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from pyguppyclient.guppy_ipc.BarcodeResults import BarcodeResults
            obj = BarcodeResults()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BarcodeArrangementResults
    def MidFront(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from pyguppyclient.guppy_ipc.BarcodeMidDetectResults import BarcodeMidDetectResults
            obj = BarcodeMidDetectResults()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BarcodeArrangementResults
    def MidRear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from pyguppyclient.guppy_ipc.BarcodeMidDetectResults import BarcodeMidDetectResults
            obj = BarcodeMidDetectResults()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BarcodeArrangementResults
    def FrontIdInner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BarcodeArrangementResults
    def FrontScoreInner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # BarcodeArrangementResults
    def RearIdInner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BarcodeArrangementResults
    def RearScoreInner(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def BarcodeArrangementResultsStart(builder): builder.StartObject(15)
def BarcodeArrangementResultsAddBarcodeTrimFront(builder, barcodeTrimFront): builder.PrependInt32Slot(0, barcodeTrimFront, 0)
def BarcodeArrangementResultsAddBarcodeTrimRear(builder, barcodeTrimRear): builder.PrependInt32Slot(1, barcodeTrimRear, 0)
def BarcodeArrangementResultsAddId(builder, id): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)
def BarcodeArrangementResultsAddNormalisedId(builder, normalisedId): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(normalisedId), 0)
def BarcodeArrangementResultsAddKit(builder, kit): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(kit), 0)
def BarcodeArrangementResultsAddVariant(builder, variant): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(variant), 0)
def BarcodeArrangementResultsAddScore(builder, score): builder.PrependFloat32Slot(6, score, 0.0)
def BarcodeArrangementResultsAddFront(builder, front): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(front), 0)
def BarcodeArrangementResultsAddBack(builder, back): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(back), 0)
def BarcodeArrangementResultsAddMidFront(builder, midFront): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(midFront), 0)
def BarcodeArrangementResultsAddMidRear(builder, midRear): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(midRear), 0)
def BarcodeArrangementResultsAddFrontIdInner(builder, frontIdInner): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(frontIdInner), 0)
def BarcodeArrangementResultsAddFrontScoreInner(builder, frontScoreInner): builder.PrependFloat32Slot(12, frontScoreInner, 0.0)
def BarcodeArrangementResultsAddRearIdInner(builder, rearIdInner): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(rearIdInner), 0)
def BarcodeArrangementResultsAddRearScoreInner(builder, rearScoreInner): builder.PrependFloat32Slot(14, rearScoreInner, 0.0)
def BarcodeArrangementResultsEnd(builder): return builder.EndObject()
