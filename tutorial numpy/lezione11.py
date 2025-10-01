import numpy as np
from numpy import random

# --- 1. Generazione di Numeri Casuali Singoli ---

# random.randint(N): Genera un singolo intero casuale tra 0 (incluso) e N (escluso)
numero = random.randint(100)
print(f"Intero casuale < 100: {numero}")

# random.rand(d1, d2, ...): Genera un array con la forma specificata, riempito con float casuali tra 0.0 (incluso) e 1.0 (escluso)
arr = random.rand(3,5,2)
print(f"Array di float casuali (3x5x2):\n{arr}")

# --- 2. Generazione di Array di Interi Casuali ---

# random.randint(N, size=(...)): Genera un array di interi casuali tra 0 (incluso) e N (escluso) con la forma specificata
arrRandom = random.randint(100, size=(5))
print(f"Array di 5 interi casuali < 100: {arrRandom}")

# --- 3. Scelta Casuale da un Array Esistente ---

# random.choice(arr, size=(...)): Sceglie elementi casuali dall'array 'arr' con la dimensione specificata
arr = np.array([1,2,3,4,5,6])
arrChoice = random.choice(arr, size=(5))
print(f"Scelta casuale (5 elementi): {arrChoice}")

# --- 4. Scelta Casuale con Probabilità (Pesata) ---

valore = np.array([10,20,30,40,50,60])
probability = np.array([0.5, 0.1, 0.1, 0.1, 0.1, 0.1]) # Probabilità leggermente corretta per sommare a 1.0
# Normalizza le probabilità per sommare a 1 (garantisce che la somma sia 1.0)
probability = probability / probability.sum()
print(f"Probabilità usate: {probability}")

# 'p=probability' assegna la probabilità a ciascun elemento. '10' avrà il 50% di probabilità di essere scelto.
arrprobability = random.choice(valore, p=probability, size=(2, 3, 3))
print(f"Array con scelta pesata (2x3x3):\n{arrprobability}") # Il valore '10' apparirà più spesso

# --- 5. Rimescolamento degli Array ---

# np.shuffle(): Rimescola l'array IN-PLACE (modifica l'array originale)
arrShuffle = np.array([1,2,3,4,5,6])
random.shuffle(arrShuffle)
print(f"\nArray dopo shuffle (modificato): {arrShuffle}")

# np.permutation(): Ritorna un NUOVO array rimescolato (non modifica l'originale)
arrPermutation = random.permutation(arrShuffle)
print(f"Array da permutation (nuova copia rimescolata): {arrPermutation}")