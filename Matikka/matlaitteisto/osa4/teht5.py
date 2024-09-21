import numpy as np

# Tehtävä 5
# AB

array1 = np.array([[1, 0.5],
                   [2, 1]])

array2 = np.array([[-1, -2],
                   [2, 4]])
array_result = np.dot(array1, array2)
print(f"Array AB result: \n {array_result}")

# BA
array1 = np.array([[-1, -2],
                   [2, 4]])


array2 = np.array([[1, 0.5],
                   [2, 1]])
array_result = np.dot(array1, array2)
print(f"Array BA result: \n {array_result}")

