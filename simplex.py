from operator import index

import numpy as np

a = np.matrix([
    [2,1],
    [3,3],
    [1.5,0]
])

i = np.matrix([
    [1,0,0],
    [0,1,0],
    [0,0,1]
])

b = np.array([1000,2400,600])

c = np.array([30,20,0,0,0])

c_b = np.array([0,0,0])

x_b = [2,3,4]

target = 'max'

# step 1. choose a variable for the base
# search for the fastest increasing variable in optimized f.
max_ind = np.where(c == max(c))
out_of_base_index = 1

quotient = np.int64(b[0]) / np.int64(a[max_ind, 0])
for i in range(len(c_b)):
    temp = np.int64(b[i]) / np.int64(a[max_ind, i])
    if quotient > temp:
        quotient = temp
        out_of_base_index = i
print(out_of_base_index)
criteria = False

