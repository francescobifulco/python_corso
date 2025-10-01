import numpy as np

arr = np.array([1,2,3,4,5,6])

print("\n--- Iterazione Standard (1D) ---")
for x in arr: # Cicla su ogni elemento dell'array 1D
    print(x)  # Stampa l'elemento corrente (1, 2, 3, ...)

print('#', '-'*25)

arr_2D = np.array([[1,2,3],
                   [4,5,6]])

print("\n--- Iterazione Nidificata Standard (2D) ---")
# Il primo ciclo itera sulle RIGHE (gli array 1D interni)
for x in arr_2D:
    # Il secondo ciclo itera sugli ELEMENTI all'interno della riga corrente
    for y in x:
        print(y) # Stampa ogni elemento individuale (1, 2, 3, 4, 5, 6)

print('#', '-'*25)

arr_3D = np.array([ [[1,2,3],[4,5,6]],
                   [[7,8,9],[10,11,12]] ])

print("\n--- Iterazione Nidificata Standard (3D) ---")
# Primo livello: Blocchi (2 blocchi)
for x in arr_3D:
    # Secondo livello: Matrici (2 matrici 1D per blocco)
    for y in x:
        # Terzo livello: Elementi (3 elementi per matrice 1D)
        for z in y:
            print(z) # Stampa ogni elemento individuale da 1 a 12
            
print('#', '-'*25)

# --- Iterazione con nditer (più efficiente, semplificata) ---

print("\n--- Iterazione con np.nditer (Flattened) ---")
for x in np.nditer(arr_3D): # nditer cicla su TUTTI gli elementi come se fosse un array 1D
    print(x)                # Stampa ogni elemento individuale da 1 a 12

# --- nditer con flag e dtypes ---

print("\n--- nditer con Flags e astype al volo ---")
# 'buffered': permette di convertire il tipo di dato al volo
# 'op_dtypes': specifica il tipo di output desiderato ('S' per stringa a byte)
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x) # Stampa [1, 2, 3, ...] come stringhe di byte (es. b'1', b'2')

# --- nditer con slicing ---

print("\n--- nditer su Slicing ---")
# arr_2D[:,::2] seleziona tutte le righe e solo le colonne con passo 2 (0 e 2)
# Risultato dello slicing: [[1 3] [4 6]]
for x in np.nditer(arr_2D[:,::2]):
    print(x) # Stampa gli elementi selezionati (1, 3, 4, 6)

print('#', '-'*25)

# --- Iterazione con ndenumerate (indice + valore) ---

print("\n--- Iterazione con np.ndenumerate (Indice e Valore) ---")
# ndenumerate fornisce una tupla (indice) e il valore in ogni iterazione
for indice, x in np.ndenumerate(arr_2D):
    # L'indice è una tupla che corrisponde alla posizione (riga, colonna)
    print(f"Indice: {indice}, Valore: {x}") # Stampa (0, 0) 1, (0, 1) 2, ..., (1, 2) 6
