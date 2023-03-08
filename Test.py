import snap7
import struct
import csv
import time
from datetime import datetime
from datetime import date
import snap7.client as c
from snap7.util import *
from snap7.types import *
import math
import matplotlib.pyplot as plt
import datetime

import os

from enum import EnumMeta


def contains(cls, member):
    return isinstance(member, cls) and member._name_ in cls._member_map_


EnumMeta.__contains__ = contains

client = c.Client()
client.connect('192.168.2.22', 0, 1)

# Variable initialization
# set_value = 0
size = 128
min_1 = 1190
in_table = []
a = 1190

"""
S7 1200 PlcSim IP 192.168.2.22
size analog value min = 1200 (0.41 mg/L)    max = 14000 (5.04 mg/L)
optimum = 6000 (2,15 mg/L)

MW14- to DB1.DBW2 Analog AQ2 oxygen1 KDN
MW16 - to DB1.DBW16 Analog Pressure Oxygen KDN
MW18 - DB1.DBW0 Analog Current Over Inverter


"""


def read_memory(plc, byte, bit, data_type):
    result = plc.read_area(Areas['MK'], 0, byte, data_type)
    if data_type == S7WLBit:
        return get_bool(result, 0, bit)
    elif data_type == S7WLByte or data_type == S7WLWord:
        return get_int(result, 0)
    elif data_type == S7WLReal:
        return get_real(result, 0)
    elif data_type == S7WLDWord:
        return get_dword(result, 0)
    else:
        return None


def write_memory(plc, byte, bit, data_type, value):
    result = plc.read_area(Areas['MK'], 0, byte, data_type)
    if data_type == S7WLBit:
        set_bool(result, 0, bit, value)
    elif data_type == S7WLByte or data_type == S7WLWord:
        set_int(result, 0, value)
    elif data_type == S7WLReal:
        set_real(result, 0, value)
    elif data_type == S7WLDWord:
        set_real(result, 0, value)
    plc.write_area(Areas['MK'], 0, byte, result)


def function_sim_sinus(in_table, size, min_1, a):
    b = 0
    x = 0
    d = 0
    k = 0
    while x < 256:
        x += 1
        for i in range(size):
            a += 100
            k += 1
            if a < 14000 and b == 0:
                in_table.append(a)
                print(b)
            elif a >= 2590 and b == 0:
                b = 1
                d = a
                print('my set a -c', a)
            else:
                a = 1190

        for j in range(size):
            if b != 0 and d > min_1:
                d -= 100
                k += 1
                in_table.append(d)
                print(b)
            elif d <= min_1 and b != 0:
                a = d
                b = 0
                print('my set c -a ', d)
            else:
                a = 1000
# ---------------------------------


function_sim_sinus(in_table, size, min_1, a)

Size_table = len(in_table)
print('Size table :', Size_table)
print('Table', in_table)

set_value = 0

for x_1 in range(256):
    print(x_1)
    time.sleep(2)
    set_value = in_table[x_1]
    write_memory(client, 5, 0, S7WLWord, value=set_value)
    print(read_memory(client, 13, 0, S7WLWord))

if __name__ == "__main__":
    plc = c.Client()
    plc.connect('192.168.2.22', 0, 1)
    # Writing
    write_memory(plc,5, 0, S7WLWord, value=set_value)
    # Reading
    print(read_memory(plc, 13, 0, S7WLWord))
    print(in_table)

