import numpy as np
from numpy.ma.core import concatenate

a=np.ones(10)
print("\n 1D array\n",a)
b=a.reshape(1,10)
a1=np.zeros([2,10])
print("\n 2D array\n",a1)
k=np.concatenate([b,a1])
print("\narray after concatenation\n",k)