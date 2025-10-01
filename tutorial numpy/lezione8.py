import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# --- 1. Concatenazione di Array 1D ---

# np.concatenate() unisce gli array lungo l'asse 0 (asse predefinito per gli array 1D)
arr3 = np.concatenate((arr1,arr2))
print(f"Concatenate 1D: {arr3}")

print('#', '-'*25)

arr1_2D = np.array([[1,2,3],
                    [4,5,6]])
arr2_2D = np.array([[7,8,9],
                    [10,11,12]])

# --- 2. Concatenazione di Array 2D lungo un Asse Specifico ---

# np.concatenate(..., axis=1) unisce gli array lungo l'asse 1 (colonne)
arr3_2D = np.concatenate((arr1_2D,arr2_2D), axis=1)
print(f"Concatenate 2D (axis=1):\n{arr3_2D}")

print('#', '-'*25)

# --- 3. Confronto tra Concatenazione e Stacking (Impilamento) ---

# np.concatenate(): unisce array ESISTENTI lungo un asse
arrConc = np.concatenate((arr1,arr2))
print(f"\nnp.concatenate: {arrConc}")

# np.stack(): unisce array come NUOVE dimensioni
# Trasforma due array (3,) in un array (2, 3)
arrStack = np.stack((arr1, arr2))
print(f"np.stack: \n{arrStack}")

# np.hstack(): Stacking Orizzontale (equivalente a concatenate lungo axis=1, dopo aver aumentato le dimensioni)
# Per array 1D, è uguale a concatenate()
arrHstack = np.hstack((arr1, arr2))
print(f"np.hstack: {arrHstack}")

# np.vstack(): Stacking Verticale (equivalente a concatenate lungo axis=0, dopo aver aumentato le dimensioni)
# Trasforma due array (3,) in un array (2, 3)
arrVstack = np.vstack((arr1, arr2))
print(f"np.vstack: \n{arrVstack}")

# np.dstack(): Stacking Profondo (Depth Stack, lungo l'asse 2)
# Trasforma due array (3,) in un array (1, 3, 2)
arrDstack = np.dstack((arr1, arr2))
# Risultato: l'array 1D viene "impilato" in profondità
print(f"np.dstack: \n{arrDstack}")
