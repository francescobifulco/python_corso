import numpy as np

# --- 1. Array a 1 Dimensione (Vettore) ---

arr1D = np.array([1,2,3,4,5])

# Stampa l'elemento all'indice 4 (l'ultimo elemento, ovvero il '5')
print(f"Elemento 1D [4]: {arr1D[4]}") 

# --- 2. Array a 2 Dimensioni (Matrice) ---

arr2D = np.array([[1,2,3],
                  [4,5,6]])

# Stampa l'elemento specificato dagli indici [riga, colonna]: 
# Riga 1 (la seconda), Colonna 2 (la terza, ovvero il '6')
print(f"Elemento 2D [1, 2]: {arr2D[1, 2]}")

# --- 3. Array a 3 Dimensioni (Tensore) ---

arr3D = np.array([[[1, 2, 3], [4, 5, 6]], 
                  [[7, 8, 9], [10, 11, 12]]])

print(f"Elemento 3D [-1, 0, 2]: {arr3D[-1, 0, 2]}")