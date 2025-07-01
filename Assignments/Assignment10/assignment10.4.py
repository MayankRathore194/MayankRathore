# Replace negative value with zero in NumPy array using replace

import numpy as np
array=np.array([1,2,3,4,-5])
print("Initial array:\n",array)
arr=np.where(array<0,0,array)
print("replace -ve array:\n",arr)

