import numpy as np

# 3, Määriteltyjä AB, BC ja CB, lasketaan -->
# AB
array1 = np.array([[1, 2 ,3],
                   [1, 0, -2]])

array2 = np.array([[1],
                   [4],
                   [2]])
array_result = np.dot(array1, array2)
print(f"Array AB result: \n {array_result}")

# BC
array1 = np.array([[1],
                   [4],
                   [2]])

array2 = np.array([[1, 0, 2]])

array_result = np.dot(array1, array2)
print(f"Array BC result: \n {array_result}")

# CB
array1 = np.array([[1, 0, 2]])

array2 = np.array([[1],
                   [4],
                   [2]])

array_result = np.dot(array1, array2)
print(f"Array CB result: \n {array_result}")