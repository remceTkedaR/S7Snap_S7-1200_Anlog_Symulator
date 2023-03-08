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

"""
S7 1200 PlcSim IP 192.168.2.22
size analog value min = 1200 (0.41 mg/L)    max = 14000 (5.04 mg/L)
optimum = 6000 (2,15 mg/L)

MW14- to DB1.DBW2 Analog AQ2 oxygen1 KDN
MW16 - to DB1.DBW16 Analog Pressure Oxygen KDN
MW18 - DB1.DBW0 Analog Current Over Inverter


"""


def read_memory(plc, byte, bit, data_type):
    result = plc.read_area(areas['MK'], 0, byte, data_type)
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
    result = plc.read_area(areas['MK'], 0, byte, data_type)
    if data_type == S7WLBit:
        set_bool(result, 0, bit, value)
    elif data_type == S7WLByte or data_type == S7WLWord:
        set_int(result, 0, value)
    elif data_type == S7WLReal:
        set_real(result, 0, value)
    elif data_type == S7WLDWord:
        set_real(result, 0, value)
    plc.write_area(areas["MK"], 0, byte, result)


# Variable initialization
#set_value = 0
size = 750
min = 9
in_table = []
a = 6


def function_sim_sinus(in_table, size, min, a):
    b = 0
    x = 0
    d = 0
    k = 0
    while x < 256:
        x += 1
        for i in range(size):
            a += 1
            k += 1
            if a < 27 and b == 0:
                in_table.append(a)
                print(b)
            elif a >= 27 and b == 0:
                b = 1
                d = a
                print('my set a -c', a)
            else:
                a = 21

        for j in range(size):
            if b != 0 and d > min:
                d -= 2
                k += 1
                in_table.append(d)
                print(b)
            elif d <= min and b != 0:
                a = d
                b = 0
                print('my set c -a ', d)
            else:
                a = 8
# ---------------------------------


plc = c.Client()
plc.connect('192.168.2.22', 0, 1)

function_sim_sinus(in_table, size, min, a)
Size_table = len(in_table)
print(Size_table)
print(in_table)

set_value_real = 2.5

# integer in size 0 - 27648 (respectively 0-10.0 to PLC)
set_value = 456

# integer in size 0-100 (respectively  0 -10 to PLC )
set_value_Int = 24

while True:

    for x_1 in range(256):
        print(x_1)
        print(read_memory(plc, 12, 0, S7WLWord))
        print(time.time())
        set_value_Int = in_table[x_1]
        if set_value_Int <= 23:
            time.sleep(15)
            write_memory(plc, 12, 0, S7WLWord, value=set_value_Int)
        elif time.sleep(12):
            write_memory(plc, 12, 0, S7WLWord, value=set_value_Int)
# print(read_memory(plc, 60, 0, S7WLWord))


    if __name__ == "__main__":
        plc = c.Client()
        plc.connect('192.168.2.22', 0, 1)
        # Writing
        #write_memory(plc, 21, 0, S7WLWord, value=set_value_Int)
        write_memory(plc, 12, 0, S7WLWord, value=set_value)
         # Reading
        print(read_memory(plc, 12, 0, S7WLWord))
        print(time.time())

