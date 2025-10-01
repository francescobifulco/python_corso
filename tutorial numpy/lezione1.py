import numpy as np

# Creazione di un array a 0 dimensioni (scalare)
arr_0D = np.array(42)
print(f'Array a zero dimensioni (scalare): {arr_0D}')

# Creazione di un array a 1 dimensione (vettore)
arr_1D = np.array([1,2,3,4,5])
print(f'Array a una dimensione (vettore): {arr_1D}')

# Creazione di un array a 2 dimensioni (matrice)
arr_2D = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
print(f'Array a due dimensioni (matrice): {arr_2D}')

# Creazione di un array a 3 dimensioni (tensore)
arr_3D = np.array([[[1,2,3],[4,5,6]], 
                   [[7,8,9],[10,11,12]]])
print(f'Array a tre dimensioni (tensore): {arr_3D}')

# Stampa del numero di dimensioni (ndim) per ciascun array
print(f"Dimensioni di arr_0D: {arr_0D.ndim}") # ndim per l'array a 0D (risultato: 0)
print(f"Dimensioni di arr_1D: {arr_1D.ndim}") # ndim per l'array a 1D (risultato: 1)
print(f"Dimensioni di arr_2D: {arr_2D.ndim}") # ndim per l'array a 2D (risultato: 2)
print(f"Dimensioni di arr_3D: {arr_3D.ndim}") # ndim per l'array a 3D (risultato: 3)

# Creazione di un array con un numero specificato di dimensioni (in questo caso 5)
arr_5D = np.array([1,2,3,4], ndmin=5)
print(f"Dimensioni di arr_5D: {arr_5D.ndim}") # Stampa il numero di dimensioni (risultato: 5)
print(f'Array a cinque dimensioni: {arr_5D}') # Stampa l'array (i dati sono racchiusi in 5 coppie di parentesi quadre)

# Utilizzo di np.arange() per creare un array di numeri
# Inizia da 5, arriva fino a (ma non include) 50, con passo 5
arrArange = np.arange(5,50, 5)
print(f"Array con arange: {arrArange}")

# Utilizzo di np.zeros() per creare un array riempito con zeri
# La tupla (3, 2) definisce la forma: 3 righe e 2 colonne
arrZeros = np.zeros((3,2))
print(f"Array di zeri (3x2):\n{arrZeros}")

# Utilizzo di np.ones() per creare un array riempito con uno
# La tupla (3, 2) definisce la forma: 3 righe e 2 colonne
arrOnes = np.ones((3,2))
print(f"Array di uno (3x2):\n{arrOnes}")