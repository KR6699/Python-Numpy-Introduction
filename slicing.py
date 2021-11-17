import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[:4])
# print(arr[4:])

'''negetive slicing'''
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[-3:-1])

'''step'''
# arr = np.array([1, 2, 3, 4, 5, 6, 7,8,9,10])
# print(arr[1:5:2])
# print(arr[::2])

'''------Slicing 2-D Arrays--------'''
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[1, 1:4])
'''From both elements, return index 2'''
# print(arr[0:2, 2])
print(arr[0:2, 1:4])