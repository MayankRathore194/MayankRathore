# Replace NaN values with average of columns
import  numpy as np
array=np.array([[6, 8, 73, 110], [np.nan, 8, 0, 94]])
mean=np.nanmean(array)
arr=np.nan_to_num(array,copy=True,nan=mean)
print("nan replaced by average:\n",arr)



