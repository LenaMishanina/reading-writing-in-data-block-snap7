import snap7
from snap7.util import get_int, set_int, set_bool

plc = snap7.client.Client()
plc.connect('192.168.0.1', 0, 1)

def WriteInt(db, offset, value):
    data = bytearray(2)
    set_int(data, 0, value)
    plc.db_write(db, offset, data)

def ReadInt(db, offset):
    data = plc.db_read(db, offset, 2)
    return get_int(data, 0)

def WriteBool(db, byte_index, bit_index, value):
    data = plc.db_read(db, byte_index, 1)
    set_bool(data, 0, bit_index, value)
    plc.db_write(db, byte_index, data)

# INT
# WriteInt(1, 2, 5)
# print(ReadInt(1, 2))

# BOOL
# WriteBool(1, 8, 2, False)   # SilverCap = False
WriteBool(1, 0, 0, False)   # StartButton = True
# WriteBool(1, 0, 1, False)   # ResetButton = True