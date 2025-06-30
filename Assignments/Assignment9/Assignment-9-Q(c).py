import numpy as np
a = np.array([[1,2,3,4],[2,3,2,1],[12,13,14,11]])
print("original array \n",a)
r = a.flatten()[::-1].reshape(a.shape)
print("\nreversed array\n",r)
