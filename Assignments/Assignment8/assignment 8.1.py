import numpy as np

random_array = np.random.rand(4, 2)
print("Random 4x2 array:\n", random_array)

empty_array = np.empty((4, 2))
print("\nEmpty 4x2 array:\n", empty_array)

full_array = np.full((4, 2), fill_value=7)
print("\nFull 4x2 array filled with 7:\n", full_array)

zeros_array = np.zeros((3, 5))
print("\n3x5 array with all zeros:\n", zeros_array)

ones_array = np.ones((4, 3, 2))
print("\n4x3x2 array with all ones:\n", ones_array)