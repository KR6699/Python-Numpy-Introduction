'''copy'''
import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 62

# print(arr)
# print(x)

'''view'''
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 62

# print(arr)
# print(x)

'''Check if Array Owns it's Data-------'''
arr = np.array([1, 2, 3])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)