"""Crea array 1D, 2D e 3D usando np.array(), np.zeros(), np.ones(), 
np.arange(), e np.linspace().

Esegui operazioni aritmetiche di base (addizione, moltiplicazione) 
tra array e tra array e scalari.

Usa l'indicizzazione e lo slicing per accedere e modificare elementi.

Cambia la forma (reshape) degli array."""

import numpy as np 

arr_1D = np.array([1, 2, 3, 4, 5])
print(f'Arrye a una dimensione:\n{arr_1D}')

print('-'*50)

arr_2D = np.zeros((3,3))
print(f'Arrye a due dimensioni con tutti zeri:\n{arr_2D}')

print('-'*50)

arr_3D = np.ones((3,3,3))
print(f'Arrye a tre dimensioni con tutti uno:\n{arr_3D}')

print('-'*50)

arr_1D_Arange = np.arange(20)
print(f'Arrye a una dimensione creato con arange:\n{arr_1D_Arange}')

print('-'*50)

arr_1D_Linspace = np.linspace(5, 20, 5)
print(f'Arrye a una dimensione creato con linspace:\n{arr_1D_Linspace}')

print('-'*50)

arrAdd = np.arange(10)
print(f'Array prima della somma con scalare:\n{arrAdd}')
print(f'Array dopo la somma con 50:\n{arrAdd + 50}')

print('-'*50)

arrMultiply = np.arange(10)
print(f'Array prima della moltiplicazione con scalare:\n{arrMultiply}')
print(f'Array dopo la moltiplicazione per 10:\n{arrMultiply * 10}')

print('-'*50)

arr1 = np.arange(10)
print(f'Arrey a una dimensio:\n{arr1}')
print(f'Elemento all\'indice 4: {arr1[4]}')

print('-'*50)

arr2 = np.arange(10)
print(f'Arrey a una dimensio:\n{arr2}')
print(f'Slicing dall\'indice 1 al 5 (escluso 6): {arr2[1:6]}')

print('-'*50)

arr2 = np.arange(12)
print(f'Arrey prima del reshape:\n{arr2}')
arrReshape = arr2.reshape(3,4)
print(f'Array dopo il reshape a (3, 4):\n{arrReshape}')