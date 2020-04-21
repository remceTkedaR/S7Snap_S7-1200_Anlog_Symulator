import snap7
import struct
import csv
import time
from datetime import datetime
from datetime import date
import snap7.client as c
from snap7.util import *
from snap7.snap7types import *
import os


# Function write data from instance db, %MW,


def write_data_area(db_number, byte, datatype):
    area = snap7.snap7types.S7AreaDB
    client.write_area(areas['DB'], db_number, byte, datatype)


def write_db(db_number, start, value):
    data_my = [value]
    client.as_db_write(db_number, start, data_my)


def test_db_write(db_number, start, size):
    data = bytearray(size)
    client.as_db_write(db_number, start, data)


def data_block_read(db_number, inst_number, data):
    db_val = client.db_read(db_number, inst_number, data)
    value_struct = struct.iter_unpack("!f", db_val[:4])
    for value_pack in value_struct:
        value_unpack = value_pack
    # Convert tuple to float
    # using join() + float() + str() + generator expression
    result = float('.'.join(str(ele) for ele in value_unpack))
    my_str_value = '%-.4f' % result
    return my_str_value


client = snap7.client.Client()
client.connect('192.168.1.121', 0, 1)


test_db_write(14, 38, 2)


my_db14_DB36 = data_block_read(14, 36, 4)

print(my_db14_DB36)

