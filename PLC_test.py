

import snap7
import snap7.client as c
from snap7.util import *
from snap7.types import *

client = snap7.client.Client()
client.connect('192.168.2.22', 0, 1)
client.get_connected()

# data = client.db_read(1, 0, 4)
data = client.upload(snap7.util.DB(1, 0, 17+2, 1,  ))


print(data)



