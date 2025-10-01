import numpy as np

# --- 1. Ricerca con np.where() ---

arrCerca = np.array([1,2,3,4,5,4,4])

# np.where() restituisce una tupla contenente gli indici dove la condizione è True
arrIndici = np.where(arrCerca == 4)
print(f"Indici di '4' (np.where): {arrIndici}") 

print('#', '-'*25)

# -- 2. Ordinamento con np.sort() ---

arrSort = np.array([5,6,1,2,4,7,2,8,9,5,7])

# np.sort() restituisce una NUOVA copia dell'array ordinata (non modifica l'originale)
arrOrdinamento = np.sort(arrSort)
print(f"Array ordinato (1D): {arrOrdinamento}")

arrSort_2D = np.array([[5,6,1,2],
                       [4,7,2,8],
                       [9,5,10,7]])

# Senza specificare 'axis', np.sort() ordina INDIVIDUALMENTE ogni riga
arrOrdinamento_2D = np.sort(arrSort_2D)
print(f"Array ordinato (2D, per riga):\n{arrOrdinamento_2D}")

print('#', '-'*25)

# --- 3. Filtering Statico (Maschera Booleana Manuale) ---

arrFiltareStatico = np.array([1,2,3,4])

# Maschera booleana (deve avere la stessa lunghezza dell'array)
filtroPari = [False, True, False, True]
arrFiltro = arrFiltareStatico[filtroPari]
print(f"Filtro Statico: {arrFiltro}")

print('#', '-'*25)

# --- 4. Filtering Dinamico (Generazione della Maschera con Ciclo) ---

arrFiltareDinamico = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

filtroPari = [] # Inizializza la lista per la maschera

for numero in arrFiltareDinamico: # Cicla su ogni elemento (meno efficiente in NumPy)
    if numero % 2 == 0:
        filtroPari.append(True) # Aggiunge True se il numero è pari
    else:
        filtroPari.append(False) # Aggiunge False se il numero è dispari
        
arrFiltro1 = arrFiltareDinamico[filtroPari]
print(f"Filtro Dinamico (con ciclo): {arrFiltro1}")

print('#', '-'*25)

# --- 5. Filtering con Scorciatoia (Maschera Booleana Vettorizzata) ---

arrFiltareScociatoria = np.array([1, 2, 3, 4])

# Operazione VETTORIZZATA: la condizione crea istantaneamente la maschera booleana
filtroPari = arrFiltareScociatoria % 2 == 0 # Risultato: [False True False True]

# Applica la maschera all'array
arrFiltro = arrFiltareScociatoria[filtroPari]
print(f"Filtro Vettorizzato (migliore): {arrFiltro}")