#
#

import math
import numpy as np
import matplotlib.pyplot as plt
import datetime


def function_sim_sinus(in_table, size, min_1, a):
    a = 0
    b = 0
    x = 0
    d = 0
    k = 0
    while x < 256:
        x += 1
        for i in range(size):
            a += 2
            k += 1
            if a < 29 and b == 0:
                in_table.append(a)
                print(b)
            elif a >= 29 and b == 0:
                b = 1
                d = a
                print('my set a -c', a)
            else:
                a = 21

        for j in range(size):
            if b != 0 and d > min_1:
                d -= 2
                k += 1
                in_table.append(d)
                print(b)
            elif d <= min_1 and b != 0:
                a = d
                b = 0
                print('my set c -a ', d)
            else:
                a = 8


# my_size = 128
# min_my = 8
# my_table = []
# index_a = 0
#
# function_sim_sinus(my_table, my_size, min_my, index_a)
#
# """"
# for j in range(len(in_table)):
#     out_table.append(math.sin(in_table[j]))
#     j += 1
# """
#
# # red for numpy.sin()
# x_time = np.arange(0.0, len(my_table), 1)
#
#
# print(my_table)
# print(len(my_table))
#
# plt.plot(x_time, my_table,  color="red")
# plt.xlabel("Time")
# plt.ylabel("Value")
# plt.show()


