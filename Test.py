import snap7
import struct
import csv
import time
from datetime import datetime
from datetime import date
import snap7.client as c
from snap7.util import *
from snap7.snap7types import *
import math
import matplotlib.pyplot as plt
import datetime

import os

from enum import EnumMeta


def contains(cls, member):
    return isinstance(member, cls) and member._name_ in cls._member_map_


EnumMeta.__contains__ = contains

client = c.Client()
client.connect(PLC_IP, 0, 1)

# Variable initialization
# set_value = 0
size = 128
min_1 = 1190
in_table = []
a = 1190
PLC_IP = '192.168.1.121'

plc = snap7.client.Client()


"""
S7 1200 PlcSim IP 192.168.2.22


Lists verilable 
%MW  - 


"""



def read_memory(plc, byte, bit, data_type):
    result = plc.read_area(Areas['Mk'], 0, byte, data_type)
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
    write_memory(client, 100, 0, S7WLWord, value=set_value)
    print(read_memory(client, 102, 0, S7WLWord))

if __name__ == "__main__":
    # plc = c.Client()
    # plc.connect('192.168.2.22', 0, 1)
    #  connect to S7 1200
    connected = False

    while not connected:
        try:
            plc = snap7.client.Client()
            plc.connect(PLC_IP, 0, 1)
            error_connect = plc.get_connected()
            connected = True  # Set flag  na True, if connected
        except Exception:
            print("Not connected. sleep 15 sec...")
            time.sleep(15)
    # Writing
    write_memory(plc,100, 0, S7WLWord, value=set_value)
    # Reading
    print(read_memory(plc, 102, 0, S7WLWord))
    print(in_table)

