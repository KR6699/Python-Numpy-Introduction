import numpy as np

'''1-d'''
# arr = np.array([1, 2, 3])
# for x in arr:
#   print(x)

'''2-d'''
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#   print(x)

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#   for y in x:
#     print(y)

'''3-d'''
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#   print(x)

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr:
#   for y in x:
#     for z in y:
#       print(z,end=',')

'''using nditer()'''
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)