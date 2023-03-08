# Test program
# Function SWAP
# by Radosław Tecmer
# radek69tecmer@gmail.com
# Work in progress
#---------------------------------

""""
Let’s say the two integers were in fact 1 and 770.
Because 770 = 256 * 3 + 2, the 4 bytes in memory would contain
respectively: 0, 1, 3, 2. The bytes I have loaded from the file would have these contents:

"""

import numpy as np

big_end_buffer = bytearray([0, 1, 3, 2]) # to jest liczba 770
bytearray(b'\\x00\\x01\\x03\\x02')

big_end_arr = np.ndarray(shape=(2,), dtype='>i2', buffer=big_end_buffer)


big_end_arr[1]

print(big_end_arr[1])

