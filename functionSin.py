#
#

import math
import matplotlib.pyplot as plt
import datetime


size = 5000
in_table = []
a = 800
b = 0
x = 0

k = 0
while x < 1000:
    x += 1
    for i in range(size):
        a += 5
        k += 1
        if a < 100 and b == 0:
            in_table.append(a)
    else:
         b = 1

    for k in range(size):
     if b > 0:
        a -= 5
        k += 1
        in_table.append(a)



#for j in range(len(in_table)):
   # out_table.append(math.sin(in_table[j]))
    #j += 1


# red for numpy.sin()

plt.plot(in_table, len(in_table),  color="red")
plt.xlabel("X")
plt.ylabel(datetime)
plt.show()


