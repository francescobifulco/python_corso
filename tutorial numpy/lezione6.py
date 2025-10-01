import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# --- Informazioni Base e Reshape ---

print(f"Forma originale (shape): {arr.shape}")        # Stampa la forma dell'array 1D (risultato: (12,))print(arr.reshape(-1).base)
print(f"Base di reshape(-1): {arr.reshape(-1).base}")  # Stampa l'array originale (arr) come base, confermando che reshape crea una vista

# --- Reshape a 2 Dimensioni ---

# Cambia la forma in una matrice 4 righe x 3 colonne (4x3)
print(f"Reshape (4,3):\n{arr.reshape(4, 3)}")          # Stampa l'array come 4 righe e 3 colonne

# --- Reshape a 3 Dimensioni ---

# Cambia la forma in un tensore 2 blocchi x 3 righe x 2 colonne (2x3x2)
print(f"Reshape (2,3,2):\n{arr.reshape(2, 3, 2)}")     # Stampa l'array come un tensore 3D

# --- Reshape con Dimensione Ignota (-1) ---

# Usa -1 per indicare a NumPy di calcolare automaticamente la dimensione mancante.
# 12 elementi / (2 * 3) = 2. Quindi, la forma diventa 2x3x2.
print(f"Reshape (2,3,-1):\n{arr.reshape(2, 3, -1)}")   # Stampa l'array come un tensore 2x3x2 (il -1 è risolto in 2)

# --- Flattening (appiattimento) ---

# arr.flatten() crea una COPIA indipendente dell'array e lo appiattisce a 1D (se non lo è già).
print(f"Flatten (copia 1D):\n{arr.flatten()}")         # Stampa l'array come 1D [1 2 3 ... 12]
