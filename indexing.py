import numpy as np
'''indexing..'''
# arr = np.array([1,2,3,4,5])
# print(arr[2] + arr[4])

'''Access the third element of the second array of the first array'''
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[1, 1, 2])

'''Print the last element from the 2nd dim'''
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])