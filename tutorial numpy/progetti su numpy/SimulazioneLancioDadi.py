"""Simulazione del Lancio di Dadi:

Crea un array di grandi dimensioni che simuli N lanci di due dadi, 
usando la funzione np.random.randint().

Calcola la distribuzione di frequenza delle somme e visualizzala."""

import numpy as np
import random

# Numero di lanci
N = 10000

# Simula N lanci di due dadi
dadi = np.random.randint(1, 7, size=(N, 2))  # 2 colonne: dado1 e dado2

# Calcola la somma per ogni lancio
somme = np.sum(dadi, axis=1)

# Calcola la frequenza delle somme
valori, conteggi = np.unique(somme, return_counts=True)

# Mostra la distribuzione come istogramma testuale
print(f"Distribuzione delle somme in {N} lanci:\n")
for val, cnt in zip(valori, conteggi):
    barra = '#' * (cnt // (N // 100))  # scala per renderlo leggibile
    print(f"Somma {val:2d}: {cnt:5d} | {barra}")