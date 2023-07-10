#  Test program for communication of Snap7 python with S7 1200
# Reading dnd writing variable MK
# by Radosław Tecmer
# radek69tecmer@gmail.com
# 2023 -02-28 ( ok)
# ------------------------

import snap7
import snap7.client as c
from snap7.util import *
from snap7.snap7types import *
import struct
import csv
import time
from datetime import datetime
from datetime import date
import fnmatch
import os
import locale

"""
Home Co
DB4.X6.0 - furnace valve
DB4.X6.1 - Living room valve
DB4.X6.2 - Hall room valve
DB4.X6.3 - Bedroom 1 valve
DB4.X6.4 - Bedroom 2 valve
DB4.X6.5 - TV room valve
DB4.X6.6 - Bathroom valve 
DB4.X6.7 - WC valve

"""

client = snap7.client.Client()
client.connect('192.168.1.121', 0, 1)
client.get_connected()


def read_memory(client, byte, bit, data_type):
    result = client.read_area(Areas['MK'], 0, byte, data_type)
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


def write_memory(client, byte, bit, data_type, value):
    result = client.read_area(Areas['MK'], 0, byte, data_type)
    if data_type == S7WLBit:
        set_bool(result, 0, bit, value)
    elif data_type == S7WLByte or data_type == S7WLWord:
        set_int(result, 0, value)
    elif data_type == S7WLReal:
        set_real(result, 0, value)
    elif data_type == S7WLDWord:
        set_real(result, 0, value)
    client.write_area(Areas["MK"], 0, byte, result)


if __name__ == "__main__":
    print(read_memory(client, 102, 0, S7WLWord))
    print(write_memory(client,100,0,S7WLWord,3))
