import numpy as np

# Array a 1 dimensione (Vettore)
arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(arr[0:2])    # Stampa gli elementi dall'indice 0 (incluso) all'indice 2 (escluso) -> [1 2]
print(arr[2:])     # Stampa gli elementi dall'indice 2 (incluso) fino alla fine dell'array -> [3 4 5 6 7 8 9 10]
print(arr[:4])     # Stampa gli elementi dall'inizio fino all'indice 4 (escluso) -> [1 2 3 4]
print(arr[:])      # Stampa tutti gli elementi dell'array (una copia completa) -> [1 2 3 4 5 6 7 8 9 10]


print(arr[2:-1]) # Stampa gli elementi dall'indice 2 (incluso) fino all'ultimo elemento (escluso) -> [3 4 5 6 7 8 9]

print(arr[::2])  # Stampa tutti gli elementi con un "passo" (step) di 2 (elementi a indice pari) -> [1 3 5 7 9]

print('#', '-'*25)

# Array a 2 dimensioni (Matrice)
arr_2D = np.array([ [1,2,3],
                    [4,5,6]])

# [Riga, Colonna]
print(arr_2D[1,1:]) # Stampa la seconda riga (indice 1) e, al suo interno, gli elementi dall'indice 1 fino alla fine -> [5 6]

print('#', '-'*25)

# Array a 3 dimensioni (Tensore)
arr_3D = np.array([ [[0,1,2,3,4],[4,5,6,7,8]], 
                    [[7,8,9,10,11],[10,11,12,13,14]] ])

# [Blocco, Riga, Colonna]
print(arr_3D[0,0,0::2]) # Stampa:
                          # 1. Il primo Blocco (indice 0)
                          # 2. La prima Riga di quel blocco (indice 0): [0, 1, 2, 3, 4]
                          # 3. All'interno di quella riga: tutti gli elementi (::) con passo 2 (0::2) -> [0 2 4]