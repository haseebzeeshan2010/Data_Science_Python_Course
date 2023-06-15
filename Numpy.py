import numpy as np

a = np.array([0,12,345,6,8,9])

print(type(a)) # type of array

print(a.dtype) # type of elements

print(a.size) # size of array

a[3:5] = 100,200 # changing multiple values within a range
print(a)
