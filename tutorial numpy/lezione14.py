import numpy as np

# Genera due array 3x3
v1 = np.random.randint(0, 11, (3, 3))
v2 = np.random.randint(0, 11, (3, 3))

print("v1:\n", v1)
print("v2:\n", v2)

# Concatenazione orizzontale (cioè affiancati) → axis=1
orizzontale = np.concatenate((v1, v2), axis=1)
print("\nConcatenazione orizzontale:\n", orizzontale)

# Concatenazione verticale (sopra/sotto) → axis=0
verticale = np.concatenate((v1, v2), axis=0)
print("\nConcatenazione verticale:\n", verticale)

# Somma righe (axis=1) e colonne (axis=0) della matrice risultante
somma_righe = np.sum(orizzontale, axis=1)
somma_colonne = np.sum(orizzontale, axis=0)

print("\nSomma di ciascuna riga:", somma_righe)
print("Somma di ciascuna colonna:", somma_colonne)

# Imposta il seed
np.random.seed(50)

# Genera un array 4×5 tra -1 e 1
v1 = np.random.uniform(-1, 1, (4, 5))
print("Array v1:\n", v1)

# Calcola i valori assoluti
valore_asso = np.abs(v1)
print("\nValori assoluti:\n", valore_asso)

# Trova il massimo valore assoluto
max_assoluto = np.max(valore_asso)
print("\nMassimo valore assoluto:", max_assoluto)

# Trova la posizione del massimo valore assoluto
posizione = np.unravel_index(np.argmax(valore_asso), valore_asso.shape)
print("Posizione del massimo valore assoluto:", posizione)

# Imposta il seed
np.random.seed(50)

# Genera un array 4×5 tra -1 e 1
v1 = np.random.uniform(-1, 1, (4, 5))
print("Array v1:\n", v1)

# Calcola i valori assoluti
valore_asso = np.abs(v1)
print("\nValori assoluti:\n", valore_asso)

# Trova il massimo valore assoluto
max_assoluto = np.max(valore_asso)
print("\nMassimo valore assoluto:", max_assoluto)

# Trova la posizione del massimo valore assoluto
posizione = np.unravel_index(np.argmax(valore_asso), valore_asso.shape)
print("Posizione del massimo valore assoluto:", posizione)

# 1. Crea un array casuale di 20 float
v1 = np.random.random(size=20)
print("Array originale:\n", v1)

# 2. Ordina in ordine decrescente
ordinato_decrescente = np.sort(v1)[::-1]
print("\nOrdinato in ordine decrescente:\n", ordinato_decrescente)

# 3. Trova il 3° valore più grande
terzo_valore = ordinato_decrescente[2]
print("\n3° valore più grande:", terzo_valore)

# Trova la posizione del 3° valore più grande nell'array originale
posizione = np.where(v1 == terzo_valore)[0][0]
print("Posizione nell'array originale:", posizione)

# 4. Sostituisci con la media dei valori
media = np.mean(v1)
v1[posizione] = media

print("\nArray finale con sostituzione:\n", v1)