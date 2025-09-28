import numpy as np

arr_0D = np.array(42)
print(f'arrery di zero dimensione: {arr_0D}')

arr_1D = np.array([1,2,3,4,5])
print(f'arrery di una dimensione: {arr_1D}')

arr_2D = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
print(f'arrery di due dimensione: {arr_2D}')

arr_3D = np.array([[[1,2,3],[4,5,6]], 
                   [[7,8,9],[10,11,12]]])
print(f'arrery di tre dimensione: {arr_3D}')

print(arr_0D.ndim)
print(arr_1D.ndim)
print(arr_2D.ndim)
print(arr_3D.ndim)

arr_5D = np.array([1,2,3,4], ndmin=5)
print(arr_5D.ndim)
print(f'arrery di tre dimensione: {arr_5D}')

arrArange = np.arange(5,50, 5)
print(arrArange)

arrZeros = np.zeros((3,2))
print(arrZeros)

arrOnes = np.ones((3,2))
print(arrOnes)