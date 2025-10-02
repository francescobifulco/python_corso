"""Statistiche e Funzioni Universali (ufunc):

Calcola statistiche di base come media (np.mean()), mediana, 
deviazione standard (np.std()), minimo (np.min()) e massimo (np.max()) 
su un array.

Applica funzioni universali (es. trigonometriche, esponenziali) agli 
array.

Usa funzioni di aggregazione lungo assi specifici (es. calcola la somma 
delle colonne di una matrice)."""

import numpy as np 

arr = np.arange(21)

arrmean = np.arange(21)
print(f'Media di un array a una dimensione:\n{arrmean.mean()}')

print('-'*50)

arrmedian = np.median(arr)
print(f'Mediana di un array a una dimensione:\n{arrmedian}')

print('-'*50)

arrstd = np.std(arr)
print(f'Deviazione standard di un array a una dimensione:\n{arrstd}')

print('-'*50)

print(f'Valore minimo in un array a una dimensione:\n{arr.min()}')

print('-'*50)

print(f'Valore massimo in un array a una dimensione:\n{arr.max()}')

print('-'*50)

potenza = np.power(arr,2)
print(f'Gli esponenziali in un array a una dimensione:\n{potenza}')

print('-'*50)

Sin = np.sin(arr)
print(f'Funzione seno applicata all\'array:\n{Sin}')

print('-'*50)

Cos = np.cos(arr)
print(f'Funzione coseno applicata all\'array:\n{Cos}')

print('-'*50)

Esponenziale = np.exp(arr)
print(f'Esponenziale (e^x) applicato all\'array:\n{Esponenziale}')

print('-'*50)

arr_2D = np.arange(9).reshape(3, 3)
print(f'Array a due dimensioni:\n{arr_2D}')

print('-'*50)

SommaColonne = np.sum(arr_2D, axis=0)
print(f'Somma delle colonne:\n{SommaColonne}')

print('-'*50)

SommaRighe = np.sum(arr_2D, axis=1)
print(f'Somma delle righe:\n{SommaRighe}')