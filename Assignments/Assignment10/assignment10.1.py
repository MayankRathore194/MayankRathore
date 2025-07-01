# Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array
# [[6, -8, 73, -110], [np.nan, -8, 0, 94]]

import  numpy as np
arr=np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
print("Initial array is :\n",arr)
res=np.nan_to_num(arr,copy=True,nan=0)
print("Array after removal of nan:\n",res)
s=arr.transpose()
print("Array after swap row column:\n",s)