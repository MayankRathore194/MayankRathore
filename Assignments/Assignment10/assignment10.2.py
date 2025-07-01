# Move axes of 3D array to new positions
import numpy as np

array=np.array([[[1,2,3,4],[10,20,30,40]],[[11,22,33,44],[100,200,300,400]]])
print("Initial array:\n",array)

arr=np.moveaxis(array,0 ,-1)
print("Moved axis\n",arr)

