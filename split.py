import numpy as np

'''1-d'''
arr = np.array([1, 2, 3, 4, 5, 6, 7])

newarr = np.array_split(arr, 3)

print(newarr)

'''2-d'''
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# newarr = np.array_split(arr, 3)

# print(newarr)

'''hsplit()'''
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)