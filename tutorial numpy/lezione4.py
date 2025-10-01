import numpy as np

# --- 1. Determinazione del Tipo di Dati (Dtype) ---

arrInt = np.array([1,2,3,4]) # Crea un array di numeri interi
print(arrInt.dtype)   # Stampa il tipo di dato (generalmente 'int64' o 'int32' a seconda dell'architettura)

arrStr = np.array(['a','b','c']) # Crea un array di stringhe
print(arrStr.dtype) # Stampa il tipo di dato (generalmente '<U1', che è una stringa Unicode di lunghezza 1)

arrFloat = np.array([1.2,2.1,3.4,4.55]) # Crea un array di numeri con virgola (float)
print(arrFloat.dtype)  # Stampa il tipo di dato (generalmente 'float64')

arrBoolean = np.array([True,False,True])  # Crea un array di valori booleani (True/False)
print(arrBoolean.dtype) # Stampa il tipo di dato ('bool')

# --- 2. Specificazione Esplicita del Dtype ---

arrS = np.array([1,2,3,4], dtype='S')  # Crea un array specificando il tipo come Stringa a Byte ('S')
print(arrS.dtype) # Stampa il tipo di dato (ad esempio '|S1')

# --- 3. Conversione del Tipo di Dati (astype) ---

arrFloat_example = np.array([1.9, 2.1, 3.5])
arrInt_converted = arrFloat_example.astype(int) # Converte in intero (tronca i decimali)
print(arrInt_converted)                         # Stampa [1 2 3]
print(arrInt_converted.dtype)                   # Stampa il nuovo tipo di dato ('int64' o simile)
