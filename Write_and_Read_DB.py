#  Test program for communication of Snap7 python with S7 1200
# Reading data from one variable in a data block
# by Radosław Tecmer
# radek69tecmer@gmail.com
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


def ReadMemory(plc,byte,bit,datatype):
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        return get_bool(result,0,bit)
    elif datatype==S7WLByte or datatype==S7WLWord:
        return get_int(result,0)
    elif datatype==S7WLReal:
        return get_real(result,0)
    elif datatype==S7WLDWord:
        return get_dword(result,0)
    else:
        return None

def WriteMemory(plc,byte,bit,datatype,value):
    result = plc.read_area(areas['DB'],0,byte,datatype)
    if datatype==S7WLBit:
        set_bool(result,0,bit,value)
    elif datatype==S7WLByte or datatype==S7WLWord:
        set_int(result,0,value)
    elif datatype==S7WLReal:
        set_real(result,0,value)
    elif datatype==S7WLDWord:
        plc.write_area(areas["DB"],0,byte,result)


if __name__=="__main__":
    plc = c.Client()
    plc.connect('192.168.1.121',0,1)
    print( ReadMemory(plc,1,0,S7WLReal))
    print(WriteMemory(plc,14,38,S7AreaDB,3.141592))
