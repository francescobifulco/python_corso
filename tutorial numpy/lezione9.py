import numpy as np

arr = np.array([1,2,3,4,5,6])

# --- 1. array_split() (Generale e Flessibile) ---

# Divide l'array in 2 parti uguali (6 elementi / 2 = 3 elementi per parte)
arr2 = np.array_split(arr, 2)

print(f"Risultato array_split (lista di array):\n{arr2}") 
print(f"Primo elemento (indice 0): {arr2[0]}")

print('#', '-'*25)

arr_2D = np.array([[1,2],[3,4],[5,6],
                   [7,8],[9,10],[11,12]])

# np.array_split() con Asse Specifico
# Divide l'array in 3 parti lungo l'asse 1 (colonne)
# La matrice ha 2 colonne, 2 / 3 non è divisibile. array_split gestisce questo in modo non uniforme.
arr3 = np.array_split(arr_2D, 3, axis=1)
print(f"\narray_split (axis=1):\n{arr3}")

print('#', '-'*25)

arr_2D_B = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,12],
                   [13,14,15],
                   [16,17,18]])

# --- 2. Funzioni di Split Dedicate (Devono essere Divisibili) ---

# np.vsplit(): Split Verticale (lungo l'asse 0/Righe)
# Divide l'array 6x3 in 3 array più piccoli 2x3. (6 righe / 3 = 2 righe per pezzo)
arrVsplit = np.vsplit(arr_2D_B, 3)
print(f"\nVertical Split (vsplit):\n{arrVsplit}")

# np.hsplit(): Split Orizzontale (lungo l'asse 1/Colonne)
# Divide l'array 6x3 in 3 array più piccoli 6x1. (3 colonne / 3 = 1 colonna per pezzo)
arrHsplit = np.hsplit(arr_2D_B, 3)
print(f"\nHorizontal Split (hsplit):\n{arrHsplit}")

print('#', '-'*25)

arr_3D = np.array([[[1,2,3],[4,5,6]],
                   [[7,8,9],[10,11,12]],
                   [[13,14,15],[16,17,18]]])

# np.dsplit(): Split Profondo (lungo l'asse 2/Profondità)
# Tenta di dividere lungo il terzo asse (colonne interne).
# L'array ha 3 elementi sul terzo asse, divisi per 3 danno 1 elemento per pezzo.
arrDsplit = np.dsplit(arr_3D, 3)
print(f"\nDepth Split (dsplit):\n{arrDsplit}")