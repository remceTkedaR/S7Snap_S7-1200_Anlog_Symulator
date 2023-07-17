#  Test program for communication of Snap7 python with S7 1200
# Reading data from one variable in a data block
# by Radosław Tecmer
# radek69tecmer@gmail.com
# ------------------------

"""
S7 300PlcSim IP 192.168.3.203
size analog value min = 1200 (0.41 bar)    max = 27648 (10.0 bar)


MW5- to DB1.DBW2 Analog pressure (przetłaczanie)
MW7 - to DB1.DBW16 Analog pressure (dosilanie)
MW13 - DB1.DBW0 Flower (przepływomierz pompownia)


"""

import snap7
import snap7.exceptions
import struct
import csv
import time
from datetime import datetime
from datetime import date
import snap7.client as c
from snap7.util import *
from snap7.types import *
import os
import locale
import functionSin

# Initialization client plc S7-1200
plc = snap7.client.Client()


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
    plc.write_area(Areas["MK"], 0, byte, result)


# Function write data from instance db, %MW,
def write_db(db_number, start, value):
    data = value
    plc.as_db_write(db_number, start, data)

# Function read data from instance db


def data_block_read(db_number, inst_number, data):
    global value_unpack
    db_val = plc.db_read(db_number, inst_number, data)
    value_struct = struct.iter_unpack("!f", db_val[:4])
    for value_pack in value_struct:
        value_unpack = value_pack
    # Convert tuple to float
    # using join() + float() + str() + generator expression
    result = float('.'.join(str(ele) for ele in value_unpack))
    my_str_value = '%-.4f' % result
    return my_str_value


# function reading coils (byte_out - PLC) (byte-size - PLC coils size) (out_bit - PLC coil)


def read_coils_s7(byte_out, byte_size, out_bit):
    byte_bit = plc.ab_read(byte_out, byte_size)
    byte_bit_array = (byte_bit[0])
    byte_coils = bin(byte_bit_array).replace("0b", "")
    result = (byte_coils[out_bit])
    return result

# my variables
my_size = 128
min_my = 8
my_table = []
index_a = 0
set_value = 0

# time start to  delay
last_time_ms = int(round(time.time() * 10000))

functionSin.function_sim_sinus()

while True:
    # index measurement loop
    f = 0
    e = 0
    d = 0
    c = len(in_table)
    print(c)
    print(in_table)

    # measurement loop
    while d < c:
        d += 1
        e += 1
        # execution condition delay time
        diff_time_ms = int(round(time.time() * 10000)) - last_time_ms
        # This is delay 80000ms = 8s
        if diff_time_ms >= 30000:
            last_time_ms = int(round(time.time() * 10000))

            #  connect to S7 1200
            try:
                plc.connect('192.168.3.203', 0, 1)
            except snap7.snap7exceptions.Snap7Exception:
                time.sleep(0.2)
                plc.connect('192.168.2.203', 0, 1)

                # Writing
                set_value = in_table[e]
                write_memory(plc, 5, 0, S7WLWord, set_value)

                # Reading
                print(read_memory(plc, 5, 0, S7WLWord))

print("koniec")

 #def __init__(self):
 #   lib_location='/usr/local/lib/libs nap7.so'
