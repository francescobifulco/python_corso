import numpy as np

# --- 1. Introduzione alle Universal Functions (ufunc) ---

# Stampa il tipo di np.add, che è una Universal Function (ufunc)
print(f"Tipo di np.add: {type(np.add)}")

# --- 2. Creazione di una ufunc Personalizzata con np.frompyfunc ---

arr = np.array([1,2,3,4,5,6,7])

# Definisce una funzione Python che aggiunge 5
def addCinque(x):
    return x + 5

# np.frompyfunc() converte la funzione Python in una ufunc di NumPy.
# 1, 1: indicano che la funzione accetta 1 input e produce 1 output.
addCinque_ufunc = np.frompyfunc(addCinque, 1, 1)
# Applica la ufunc all'array intero, velocemente elemento per elemento
print(f"Ufunc personalizzata (aggiungi 5): {addCinque_ufunc(arr)}")

# --- 3. Ufunc Aritmetiche Base (Elemento per Elemento) ---

arr1 = np.array([10,20,30,40,50])
arr2 = np.array([5,10,15,20,25])

arrAdd = np.add(arr1, arr2)       # Somma elemento per elemento
print(f"np.add: {arrAdd}")  

arrSubtract = np.subtract(arr1, arr2) # Sottrazione elemento per elemento
print(f"np.subtract: {arrSubtract}")

arrMultiply = np.multiply(arr1, arr2) # Moltiplicazione elemento per elemento
print(f"np.multiply: {arrMultiply}") 

arrDivide = np.divide(arr1, arr2) # Divisione elemento per elemento
print(f"np.divide: {arrDivide}")

arrPower = np.power(arr1, arr2)  # Potenza elemento per elemento (arr1 elevato a arr2)
# Nota: i risultati possono essere molto grandi
print(f"np.power: {arrPower}")

# Modulo (Resto della divisione)
arrMod = np.mod(arr1, arr2)
print(f"np.mod: {arrMod}")

# remainder è un alias di np.mod, fa esattamente la stessa cosa
arrRemainder = np.remainder(arr1, arr2)
print(f"np.remainder (alias di mod): {arrRemainder}")

# --- 4. Ufunc di Arrotondamento (Rounding) ---

# np.trunc(): Tronca i decimali verso lo zero (rimuove la parte frazionaria)
arrTrunc = np.trunc([3.4,23.5])
print(f"\nnp.trunc (troncamento): {arrTrunc}")

# np.fix(): Funziona esattamente come np.trunc
arrFix = np.fix([3.4,23.5])
print(f"np.fix (stesso di trunc): {arrFix}")

# np.around(): Arrotonda al numero intero più vicino (standard)
arrAround = np.around([3.4,23.5])
print(f"np.around (standard): {arrAround}")

# np.ceil(): Arrotonda per eccesso (al valore intero immediatamente superiore)
# Correzione: accetta un solo input. Usiamo arrFloat.
arrCeil = np.ceil(arr1, arr2)
print(f"np.ceil (eccesso): {arrCeil}")

# np.floor(): Arrotonda per difetto (al valore intero immediatamente inferiore)
# Correzione: accetta un solo input. Usiamo arrFloat.
arrFloor = np.floor(arr1, arr2)
print(f"np.floor (difetto): {arrFloor}")