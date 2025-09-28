import numpy as np

arr = np.array([1,2,3,4,5,6])

for x in arr:
    print(x)
    
arr_2D = np.array([[1,2,3],
                   [4,5,6]])

for x in arr_2D:
    for y in x:
        print(y)
        
arr_3D = np.array([ [[1,2,3],[4,5,6]],
                   [[7,8,9],[10,11,12]] ])

for x in arr_3D:
    for y in x:
        for z in y:
            print(z)

for x in np.nditer(arr_3D):
    print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)
    
for x in np.nditer(arr_2D[:,::2]):
    print(x)
    
for indice,x in np.ndenumerate(arr_2D):
    print(indice,x)