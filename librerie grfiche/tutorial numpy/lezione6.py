import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(arr.shape)
print(arr.reshape(-1).base)
print(arr.reshape(4,3))
print(arr.reshape(2,3,2))
print(arr.reshape(2,3,-1))

print(arr.flatten())