import numpy as np
import random

# 1.
random_array = np.random.randint(1,100, size=20)
sorted_array = np.sort(random_array)
twoD_array = random_array.reshape(4,5)

print(f"\n Original array: {random_array}")

print(f" Sorted array in ascending order: {sorted_array}")

print(f"\n Two dimensional array: \n {twoD_array}")

# 2. ja 3.

# a) u = 2i + 3j, v =4i - 7j
u = [2,3]
print("\n- Vektori u", u)

v = [4, -7]
print("- Vektori v", v)

u_norm = np.linalg.norm(u)
print(f"Vektorin u normi = {u_norm}")

v_norm = np.linalg.norm(v)
print(f"Vektorin v normi = {v_norm}\n")

# b) uu= i + j + k, vv 3i -3j + 2k.
uu = [1,1,1]
print("- Vektori uu", uu)
uu_norm = np.linalg.norm(uu)
print(f"Vektorin uu normi = {uu_norm} \n")

vv = [3,-3,2]
print("- Vektori vv", vv)
vv_norm = np.linalg.norm(vv)
print(f"Vektorin u normi = {vv_norm} ")