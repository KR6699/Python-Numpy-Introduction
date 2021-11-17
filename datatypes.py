'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
import numpy as np

# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)

'''Creating Arrays With a Defined Data Type'''
# arr = np.array([1, 2, 3, 4, 5, 6], dtype='S')
# print(arr)
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4, 5, 6], dtype='i4')
# print(arr)
# print(arr.dtype)

'''Converting Data Type on Existing Arrays---------------------'''

'''float to int'''
# arr = np.array([1.1, 2.1, 3.1])

# print(arr)
# print(arr.dtype)

# # newarr = arr.astype('i8')
# newarr = arr.astype('int')
# print(newarr)
# print(newarr.dtype)

'''int to bool'''
arr = np.array([1,0,3,4,5])
print(arr)
print(arr.dtype)
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)