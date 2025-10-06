import pandas as pd

df = pd.read_csv('serie_a_2025.csv', index_col=0)

# Utilizzo di .loc per selezionare un valore specifico 
# usando le etichette (nome riga e nome colonna).
# Seleziona il numero di Vittorie della squadra 'Inter'.
print("\n--- 1. .loc[Riga Etichetta, Colonna Etichetta] ---")
print(f"Vittorie dell'Inter: {df.loc['Inter', 'Vittorie']}")

# Utilizzo di .iloc per selezionare un valore 
# specifico usando la posizione numerica (indice intero).
# La riga 9 è 'Bologna', la colonna 3 è 'Pareggi'.
print("\n--- 2. .iloc[Posizione Riga (9), Posizione Colonna (3)] ---")
print(f"Pareggi del Bologna (9a squadra, 3a colonna): {df.iloc[9, 3]}")

# Slicing di righe tramite posizione numerica (iloc). 
# Seleziona le prime 5 righe (da 0 a 5, 5 escluso).
print("\n--- 3. .iloc[Slicing Righe: 0:5] ---")
print(df.iloc[0:5])

# Slicing di righe tramite etichetta (loc). 
# Seleziona le righe da 'Napoli' A 'Verona' (INCLUSI).
# Nel slicing con .loc l'etichetta finale è inclusa, 
# a differenza del normale slicing Python.
print("\n--- 4. .loc[Slicing Righe: 'Napoli':'Verona'] ---")
print(df.loc['Napoli':'Verona'])

# .loc[:, [Nomi Colonne]]: Seleziona TUTTE le righe 
# (il primo :) e solo le colonne specificate.
print("\n--- 5. .loc[Tutte Righe, Colonne Etichette] ---")
print(df.loc[:, ['Vittorie', 'Pareggi', 'Sconfitte']])

# Selezione di un blocco di dati specifico: 
# Riga singola ('Inter') e colonne specificate.
# Il risultato è una Pandas Series.
print("\n--- 6. .loc[Riga 'Inter', Colonne Etichette] ---")
print(df.loc['Inter', ['Vittorie', 'Pareggi', 'Sconfitte']])

# .iloc[:, [Indici Colonne]]: Seleziona TUTTE le righe 
# (il primo :) e le colonne in base alla posizione numerica.
# [2, 3, 5] corrispondono a 'Vittorie', 
# 'Pareggi' e 'Sconfitte' 
# (sebbene la colonna 'Sconfitte' 
# sia in posizione 4 nel mio esempio).
# Ho corretto la lista di indici per puntare a 'Vittorie' 
# (indice 2), 'Pareggi' (indice 3) e 'Sconfitte' (indice 4).
print("\n--- 7. .iloc[Tutte Righe, Colonne Posizione ([2, 3, 4])] ---")
print(df.iloc[:, [2, 3, 4]]) 

# Selezione di valori da una riga singola 
# (posizione 0) e colonne specifiche tramite posizione numerica.
# Seleziona le statistiche di 'Vittorie', 
# 'Pareggi' e 'Sconfitte' per la prima squadra ('Inter').
print("\n--- 8. .iloc[Riga Posizione (0), Colonne Posizione ([2, 3, 4])] ---")
print(df.iloc[0, [2, 3, 4]])
print("-----------------------------------------------------------------------")
