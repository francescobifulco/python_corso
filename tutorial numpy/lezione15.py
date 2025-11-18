import numpy as np 

# Crea le matrici
A = np.random.randint(0, 11, (3, 4))
B = np.random.randint(11, 21, (4, 3))

# Moltiplicazione matriciale
C = A @ B
print("Matrice C:\n", C)

# Diagonale
diagonale = np.diag(C)
print("\nDiagonale:", diagonale)

# Traccia
traccia = np.trace(C)
print("Traccia:", traccia)

# Somma degli elementi sulla diagonale
somma_diagonale = np.sum(diagonale)
print("Somma degli elementi della diagonale:", somma_diagonale)

# 1. Matrice 4×4 casuale
A = np.random.randint(0, 11, (4,4))
print("Matrice A:\n", A)

# 2. Determinante
det = np.linalg.det(A)
print("\nDeterminante:", det)

# 3. Verifica invertibilità
if det != 0:
    print("\nLa matrice è invertibile.\n")

    # 4. Matrice inversa
    A_inv = np.linalg.inv(A)
    print("Inversa di A:\n", A_inv)

    # 5. Verifica A @ A_inv ≈ I
    controllo = A @ A_inv
    print("\nProdotto A @ A_inv:\n", controllo)

    print("\nVerifica numerica (≈ I):", np.allclose(controllo, np.eye(4)))

else:
    print("\nLa matrice NON è invertibile.")

# 1. Matrice 5×5 casuale
C = np.random.randint(0, 11, (5,5))
print("Matrice C:\n", C)

# 2. Trasposta
C_T = C.T
print("\nTrasposta C.T:\n", C_T)

# 3. Verifica simmetria
simmetrica = np.allclose(C, C_T)
print("\nÈ simmetrica?", simmetrica)

# 4. Rendi la matrice simmetrica forzatamente:
#    (C + C^T)/2 è un metodo standard per simmetrizzare
C_sym = (C + C_T) / 2
print("\nMatrice simmetrizzata:\n", C_sym)

# 5. Calcola la media dei valori sopra la diagonale
sopra_diag = C_sym[np.triu_indices(5, k=1)]   # elementi con i < j
media = np.mean(sopra_diag)
print("\nMedia dei valori sopra la diagonale:", media)

v1 = np.random.randint(0, 11, (5,5))
print("Matrice v1:\n", v1)

v_T = v1.T
print("\nTrasposta v_T:\n", v_T)

verifica = np.allclose(v1, v_T)
print("\nLa matrice è simmetrica?", verifica)

v_sym = (v1 + v_T) / 2
print("\nMatrice simmetrizzata v_sym:\n", v_sym)

media_dia = v_sym[np.triu_indices(5, k=1)]
print("\nElementi sopra la diagonale:\n", media_dia)

media = np.mean(media_dia)
print("\nMedia degli elementi sopra la diagonale:", media)

# 1. Crea matrice 10x10 di zeri
v1 = np.zeros((10,10))
print("Matrice iniziale di zeri:\n", v1)

# 2. Genera 10 valori casuali da inserire
valori_casuali = np.random.randint(1, 101, size=10)
print("\nValori casuali da inserire:", valori_casuali)

# 3. Scegli 10 posizioni casuali nella matrice
righe = np.random.randint(0, 10, size=10)
colonne = np.random.randint(0, 10, size=10)
print("\nPosizioni casuali (righe):", righe)
print("Posizioni casuali (colonne):", colonne)

# 4. Inserisci i valori nelle posizioni scelte
for i in range(10):
    v1[righe[i], colonne[i]] = valori_casuali[i]

print("\nMatrice con valori casuali inseriti:\n", v1)

# 5. Conta i valori non nulli
non_zeri = np.count_nonzero(v1)
print("\nNumero di valori non nulli:", non_zeri)

# 6. Sostituisci i valori non nulli con la loro radice quadrata
v1[v1 != 0] = np.sqrt(v1[v1 != 0])
print("\nMatrice dopo aver calcolato la radice quadrata dei valori non nulli:\n", v1)
