import numpy as np

# 1a)

array1 = np.array([[-1, 2],
                   [3, 1]])

array2 = np.array([[0, 1, 3],
                   [2, -3, 5]])
array_result = np.dot(array1, array2)
print(f"Array result: \n {array_result}")

# b)
array1 = np.array([[1, 3, 5],
                   [0, -2, 1],
                [2, -1, 4]])

array2 = np.array([[1],
                   [-3],
                   [-1]])
array_result = np.dot(array1, array2)
print(f"Array result: \n {array_result}")

# c)
array1 = np.array([[2, 0, 1],
                   [1, -3, 4],
                [0, 1, 5]])

array2 = np.array([[3],
                   [-5],
                   [7]])
array_result = np.dot(array1, array2)
print(f"Array result: \n {array_result}")

# d)
array1 = np.array([[1, -4, 2],
                   [3, 0, -2],
                [2, 1, 0]])

array2 = np.array([[5, 1, -1],
                   [-2, 1, 3],
                [0, 3, 4]])
array_result = np.dot(array1, array2)
print(f"Array result: \n {array_result}")