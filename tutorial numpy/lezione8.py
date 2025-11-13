import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# --- 1. Concatenazione di Array 1D ---

# np.concatenate() unisce gli array lungo 
# l'asse 0 (asse predefinito per gli array 1D)
arr3 = np.concatenate((arr1, arr2))
print(f"Concatenate 1D: {arr3}")

print('#', '-'*25)

arr1_2D = np.array([[1,2,3],
                    [4,5,6]])
arr2_2D = np.array([[7,8,9],
                    [10,11,12]])

# --- 2. Concatenazione di Array 2D lungo un Asse Specifico ---

# np.concatenate(..., axis=1) unisce gli array lungo l'asse 1 (colonne)
arr3_2D = np.concatenate((arr1_2D, arr2_2D), axis=1)
print(f"Concatenate 2D (axis=1):\n{arr3_2D}")

print('#', '-'*25)

# --- 3. Confronto tra Concatenazione e Stacking (Impilamento) ---

# np.concatenate(): unisce array ESISTENTI lungo un asse
arrConc = np.concatenate((arr1, arr2))
print(f"\nnp.concatenate: {arrConc}")

# np.stack(): unisce array come NUOVE dimensioni
# Trasforma due array (3,) in un array (2, 3)
arrStack = np.stack((arr1, arr2))
print(f"np.stack: \n{arrStack}")

# np.hstack(): Stacking Orizzontale (equivalente a 
# concatenate lungo axis=1, dopo aver aumentato le dimensioni)
# Per array 1D, è uguale a concatenate()
arrHstack = np.hstack((arr1, arr2))
print(f"np.hstack: {arrHstack}")

# np.vstack(): Stacking Verticale (equivalente a 
# concatenate lungo axis=0, dopo aver aumentato le dimensioni)
# Trasforma due array (3,) in un array (2, 3)
arrVstack = np.vstack((arr1, arr2))
print(f"np.vstack: \n{arrVstack}")

# np.dstack(): Stacking Profondo (Depth Stack, lungo l'asse 2)
# Trasforma due array (3,) in un array (1, 3, 2)
# L'array 1D viene "impilato" in profondità (terza dimensione)
arrDstack = np.dstack((arr1, arr2))
print(f"np.dstack: \n{arrDstack}")

# --- 4. Matrice Identità ---

# np.eye(n) crea una matrice identità 
# n×n (diagonale principale con 1, resto 0)
arrDiagonale_prin = np.eye(6)
print(f"np.eye (diagonale principale): \n{arrDiagonale_prin}")

# np.fliplr(np.eye(n)) ribalta orizzontalmente la matrice identità,
# ottenendo la diagonale secondaria 
# (dall’alto a destra verso il basso a sinistra)
arrDiagonale_seco = np.fliplr(np.eye(6))
print(f"""np.fliplr(np.eye): (diagonale secondaria): 
      \n{arrDiagonale_seco}""")

# --- 5. Generazione e Reshape di Array ---

# np.linspace(start, stop, num) genera 
# 'num' valori equispaziati tra start e stop
arrLinspace = np.linspace(0, 11, 30)
print(f"np.linspace: {arrLinspace}")

# np.reshape() cambia la forma dell’array 
# mantenendo lo stesso numero di elementi
arrReshape = arrLinspace.reshape((5,6))
print(f"np.reshape: {arrReshape}")

# --- 6. Ricerca di Massimi e Minimi ---

# np.argmax() restituisce l'indice del valore massimo nell'array
arrArgmax = np.argmax(arr1)
print(f"""np.argmax: indice del valore 
      massimo in arr1 -> {arrArgmax} (valore = {arr1[arrArgmax]})""")

# np.argmin() restituisce l'indice del valore minimo nell'array
arrArgmin = np.argmin(arr1)
print(f"""np.argmin: indice del valore minimo 
      in arr1 -> {arrArgmin} (valore = {arr1[arrArgmin]})""")

# --- 7. Filtro di Array Casuale ---

# Genera un array casuale di 100 numeri interi tra 1 e 100
v1 = np.random.randint(1, 101, size=100)
print(f"\nArray casuale v1:\n{v1}")

# Filtra solo i numeri divisibili per 3 ma NON per 5
# (v1 % 3 == 0) seleziona multipli di 3
# ~(v1 % 5 == 0) esclude i multipli di 5
filtro = v1[(v1 % 3 == 0) & ~(v1 % 5 == 0)]
print(f"\nNumeri divisibili per 3 ma non per 5:\n{filtro}")

# Conta quanti numeri soddisfano questa condizione
conteggio = filtro.size
print(f"\nQuantità di numeri che soddisfano la condizione: {conteggio}")