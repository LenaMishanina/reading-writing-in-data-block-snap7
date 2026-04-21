import snap7
from snap7.util import get_int, set_int, set_bool, get_bool

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

def ReadBool(db, byte_index, bit_index):
    data = plc.db_read(db, byte_index, 1)   # читаем 1 байт
    return get_bool(data, 0, bit_index)

# INT
# WriteInt(1, 2, 5)
# print(ReadInt(1, 2))

# BOOL
# WriteBool(1, 8, 2, False)   # SilverCap = False
# WriteBool(1, 0, 0, False)   # StartButton = True
# WriteBool(1, 0, 1, False)   # ResetButton = True


# что касается лотков
# ---------- READ ----------
def ReadInputs():
    data = plc.db_read(DB_NUMBER, 0, 1)  # читаем 1 байт
    wpc1 = get_bool(data, 0, 0)  # Input
    wpc2 = get_bool(data, 0, 1)
    return wpc1, wpc2


# ---------- WRITE ----------
def WriteControls(wpc1_ctrl, wpc2_ctrl):
    data = plc.db_read(DB_NUMBER, 0, 1)  # читаем байт

    set_bool(data, 0, 2, wpc1_ctrl)  # Control
    set_bool(data, 0, 3, wpc2_ctrl)

    plc.db_write(DB_NUMBER, 0, data)


DB_NUMBER = 32

# Чтение входов
wpc1, wpc2 = ReadInputs()
print("Input WpcSlide1:", wpc1)
print("Input WpcSlide2:", wpc2)

# Запись управления
WriteControls(False, True)

# Проверка
data = plc.db_read(DB_NUMBER, 0, 1)
print("Control WpcSlide1:", get_bool(data, 0, 2))
print("Control WpcSlide2:", get_bool(data, 0, 3))