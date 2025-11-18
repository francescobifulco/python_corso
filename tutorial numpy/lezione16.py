import numpy as np

# Creazione della matrice 5×5 con valori da 0 a 24
v1 = np.arange(0, 25).reshape(5,5)
print("Matrice v1:\n", v1, "\n")

# Creazione del vettore riga di lunghezza 5
v2 = np.array([0, 1, 2, 3, 4])
print("Vettore riga v2:\n", v2, "\n")

# Sottrazione con broadcasting
risultato = v1 - v2
print("Risultato della sottrazione (broadcasting):\n", risultato)

# 1. Genera array 100×3 di valori casuali (tra 0 e 1)
v1 = np.random.rand(100, 3)
print("Array originale (100x3):\n", v1)

# 2. Normalizzazione tra 0 e 1 di ogni colonna
min_valo = v1.min(axis=0)
max_valo = v1.max(axis=0)

v_norm = (v1 - min_valo) / (max_valo - min_valo)
print("Array normalizzato tra 0 e 1:\n", v_norm, "\n")

# 3. Media e deviazione standard delle colonne normalizzate
media = v_norm.mean(axis=0)
std  = v_norm.std(axis=0)

print("Media delle colonne normalizzate:\n", media)
print("\nDeviazione standard delle colonne normalizzate:\n", std)

# 1. Matrice casuale 3x3
v1 = np.random.uniform(0, 11, (3, 3))
print("Matrice v1:\n", v1)

# 2. Autovalori e autovettori
autovalori, autovettori = np.linalg.eig(v1)
print("\nAutovalori:\n", autovalori)
print("\nAutovettori (colonne):\n", autovettori)

# 3. Verifica A v = λ v
print("\nVerifica v1 @ v = λ v:\n")
for i in range(len(autovalori)):
    λ = autovalori[i]
    v = autovettori[:, i]   # autovettore i-esimo

    left = v1 @ v           # A @ v
    right = λ * v           # λ v

    print(f"Autovalore λ{i+1} = {λ}")
    print("v1 @ v = ", left)
    print("λ * v = ", right)
    print("Differenza = ", left - right)  # dovrebbe essere ~0
    print("-" * 40)
