# Calculate average mean median mode values of two NumPy 2d-arrays
import  numpy as np
arr1=np.array([[1,2,3,4],[10,20,30,40]])
arr2=np.array([[11,22,33,44],[100,200,300,400]])
print("arr1:\n",arr1,"arr2:\n",arr2)
combined = np.concatenate((arr1.flatten(), arr2.flatten()))

mean_val = np.mean(combined)

median_val = np.median(combined)

unique, counts = np.unique(combined, return_counts=True)
mode_val = unique[np.argmax(counts)]

print("\nMean value:", mean_val)
print("Median value:", median_val)
print("Mode value:", mode_val)
