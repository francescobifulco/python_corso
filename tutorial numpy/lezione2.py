import numpy as np

# Array a 1 dimensione (Vettore)
arr_1D = np.array([1,2,3,4]) # Crea un array [1 2 3 4]
print(arr_1D[-3])

# Array a 2 dimensioni (Matrice)
arr_2D = np.array([[1,2,3],
                   [4,5,6]]) # Crea una matrice 2x3
print(arr_2D[-1,0])

# Array a 3 dimensioni (Tensore)
arr_3D = np.array([ [[1,2,3],[4,5,6]],
                   [[7,8,9],[10,11,12]]]) # Crea un tensore 2x2x3
print(arr_3D[0,1,-2])

# Array a 5 dimensioni (ndmin)
arr_5D = np.array([1,2,3], ndmin=5) # Crea un array con i dati [1, 2, 3] ma forzato a 5 dimensioni
print(arr_5D)

# Funzione arange
arrArange = np.arange(5,50,5) # Crea un array che parte da 5, arriva fino a 50 (escluso), con passo 5
print(arrArange)

# Funzione zeros
arrZeros = np.zeros((3,2)) # Crea una matrice 3x2 riempita con zeri (tipo float)
print(arrZeros)

# Funzione ones
arrOnes = np.ones((3,2)) # Crea una matrice 3x2 riempita con uno (tipo float)
print(arrOnes)