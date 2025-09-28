import numpy as np

arr = np.array([1,2,3])
arrCopy = arr.copy()

arr[0] = 10

print(arr)
print(arrCopy)

arr = np.array([1,2,3])
arrView = arr.view()

arr[0] = 10

print(arr)
print(arrView)

print(arr.base)
print(arrCopy.base)