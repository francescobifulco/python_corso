import numpy as np

arr_1D = np.array([1,2,3,4])
print(arr_1D[-3])

arr_2D = np.array([[1,2,3],
                   [4,5,6]])
print(arr_2D[-1,0])

arr_3D = np.array([ [[1,2,3],[4,5,6]],
                   [[7,8,9],[10,11,12]]])
print(arr_3D[0,1,-2])