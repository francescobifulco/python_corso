import numpy as np

# --- Sezione 1: array.copy() ---

arr = np.array([1,2,3])
arrCopy = arr.copy() # Crea una COPIA: una nuova, indipendente area di memoria con gli stessi dati.

arr[0] = 10  # Modifica il primo elemento dell'array ORIGINALE 'arr

print(f"Array ORIGINALE (dopo la modifica): {arr}")     # Stampa [10 2 3]
print(f"Array COPIA (non modificato): {arrCopy}")       # Stampa [1 2 3] - Rimane invariato

# arr.base verifica se l'array è una vista. Se è None, è l'array originale o una copia.
print(f"Base di arr (originale): {arr.base}")           # Stampa 'None'
# arrCopy.base verifica se la copia è una vista. Se è None, è una copia completa.
print(f"Base di arrCopy (copia): {arrCopy.base}")       # Stampa 'None'

print('#', '-'*20)

# --- Sezione 2: array.view() ---

arr = np.array([1,2,3])
arrView = arr.view()  # Crea una VISTA: una nuova variabile che punta alla STESSA area di memoria.
arr[0] = 10               # Modifica il primo elemento dell'array ORIGINALE 'arr'

print(f"Array ORIGINALE (dopo la modifica): {arr}")     # Stampa [10 2 3]
print(f"Array VISTA (modificato): {arrView}")           # Stampa [10 2 3] - Riflette la modifica

# Stampa l'array base della vista per confermare il collegamento
print(f"Base di arrView (vista): {arrView.base}")       # Stampa l'array [10 2 3] (ovvero 'arr' stesso)
print(arr.base)
print(arrCopy.base)