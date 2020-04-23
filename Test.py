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


def write_data_area(db_number, start, data):
    data = bytearray(data)
    client.write_area(areas['DB'], db_number, start, data)


def write_db(db_number, start, value):
    data_my = [value]
    client.as_db_write(db_number, start, data_my)


def test_db_write_byte_array(db_number, start, size):
    data = bytearray(size)
    client.as_db_write(db_number, start, data)


def test_db_write_byte(db_number, start, size):
    data = bytes(size)
    client.as_db_write(db_number, start, data)


def data_block_read_Int(db_number, inst_number, data):
    db_val = client.db_read(db_number, inst_number, data)
    value_struct = struct.iter_unpack("!h", db_val[:2])
    for value_pack in value_struct:
        value_unpack = value_pack
    # Convert tuple to float
    # using join() + float() + str() + generator expression
    result = int('.'.join(str(ele) for ele in value_unpack))
    my_str_value = '%-.2i' % result
    return my_str_value


def data_block_read_float(db_number, inst_number, data):
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
#client.connect('192.168.4.3', 0, 1)

write_data_area(1, 18, (0,250))

write_data_area(1, 19, (0,100))

#  DB14 DBW 36, DB14 DBD 38, DB18 DBB19
# Job PLC DB1 DBW18 - oxygen
# DB1 DBW20 - oxygen 2
# DB1 DBW22 - Pressure
# DB1 DBW24 - Current


#my_read = client.db_read(14, 36, 2)

my_read1 = data_block_read_Int(14, 36, 2)
my_read2 = data_block_read_float(14, 38, 4)

print(my_read1)
print(my_read2)

client.disconnect()

