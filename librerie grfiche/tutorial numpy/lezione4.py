import numpy as np

arrInt = np.array([1,2,3,4])
print(arrInt.dtype)

arrStr = np.array(['a','b','c'])
print(arrStr.dtype)

arrFloat = np.array([1.2,2.1,3.4,4.55])
print(arrFloat.dtype)

arrBoolean = np.array([True,False,True])
print(arrBoolean.dtype)

arrS = np.array([1,2,3,4], dtype='S')
print(arrS.dtype)

arrInt1 = arrStr.astype(int)
print(arrInt1)