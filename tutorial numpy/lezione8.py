import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr3 = np.concatenate((arr1,arr2))
print(arr3)

arr1_2D = np.array([[1,2,3],
                    [4,5,6]])
arr2_2D = np.array([[7,8,9],
                    [10,11,12]])

arr3_2D = np.concatenate((arr1_2D,arr2_2D), axis=1)
print(arr3_2D)

arrConc = np.concatenate((arr1,arr2))
arrStack = np.stack((arr1,arr2))
arrHstack = np.hstack((arr1,arr2))
arrVstack = np.vstack((arr1,arr2))
arrDstack = np.dstack((arr1,arr2))

print(arrConc)
print(arrStack)
print(arrHstack)
print(arrVstack)
print(arrDstack)