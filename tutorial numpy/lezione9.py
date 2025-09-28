import numpy as np

arr = np.array([1,2,3,4,5,6])

arr2 = np.array_split(arr, 2)

print(arr2)
print(arr2[0])

arr_2D = np.array([[1,2],[3,4],[5,6],
                   [7,8],[9,10],[11,12]])

arr3 = np.array_split(arr_2D, 3, axis=1)

print(arr3)

arr_2D = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,12],
                   [13,14,15],
                   [16,17,18]])

arrVsplit = np.vsplit(arr_2D, 3)
arrHsplit = np.hsplit(arr_2D, 3)

arr_3D = np.array([[[1,2,3],[4,5,6]],
                   [[7,8,9],[10,11,12]],
                   [[13,14,15],[16,17,18]]])

arrDsplit = np.dsplit(arr_3D, 3)

print(arrVsplit)
print(arrHsplit)
print(arrDsplit)