import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(arr[0:2])
print(arr[2:])
print(arr[:4])
print(arr[:])

print(arr[2:-1])

print(arr[::2])

arr_2D = np.array([ [1,2,3],
                    [4,5,6]])

print(arr_2D[1,1:])

arr_3D = np.array([ [[0,1,2,3,4],[4,5,6,7,8]], 
                    [[7,8,9,10,11],[10,11,12,13,14]] ])
print(arr_3D[0,0,0::2])