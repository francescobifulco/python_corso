import pandas as pd

df = pd.read_csv('serie_a_2025.csv')

print("--- 1. DataFrame Completo (df) ---")
print(df)

# Slicing implicito: Seleziona le righe 
# da 0 (incluso) a 15 (escluso).
print("\n--- 2. Slicing Righe: prime 15 (df[0:15]) ---")
print(df[0:15])

# Slicing implicito: Seleziona le righe 
# da 2 (incluso) a 14 (escluso).
print("\n--- 3. Slicing Righe: dalla 3a alla 14a (df[2:14]) ---")
print(df[2:14])

# Metodo head: Visualizza le prime 
# N righe (predefinito 5, qui 10).
print("\n--- 4. Le prime 10 righe (df.head(10)) ---")
print(df.head(10))

# Metodo tail: Visualizza le ultime N righe (predefinito 5, qui 10).
print("\n--- 5. Le ultime 10 righe (df.tail(10)) ---")
print(df.tail(10))

# Selezione di una singola colonna: 
# restituisce una Serie Pandas.
print("\n--- 6. Selezione Colonna 'Squadra' (Serie) ---")
print(df['Squadra'])

# Slicing applicato alla Serie 'Squadra': 
# seleziona i primi 10 elementi.
print("\n--- 7. Slicing Serie 'Squadra': i primi 10 nomi ---")
print(df['Squadra'][0:10])

# Selezione di multiple colonne (lista di nomi) 
# e visualizzazione delle prime 7 righe.
# Il risultato è un DataFrame più piccolo.
print("\n--- 8. Selezione Colonne + head(7) ---")
print(df[['Squadra', 'Punti', 'Vittorie', 'Pareggi']].head(7))

# Selezione di multiple colonne seguita da slicing delle righe 
# (dalla riga 13 inclusa alla 19 esclusa).
print("\n--- 9. Selezione Colonne + Slicing Righe (13:19) ---")
print(df[['Squadra', 'Punti', 'Vittorie', 'Pareggi']][13:19])


# Selezione di un valore specifico tramite etichetta 
# (indice di riga 0, nome colonna 'Squadra').
# .loc usa l'etichetta dell'indice (0) e l'etichetta 
# della colonna ('Squadra').
print("\n--- 10. Valore Singolo con .loc[0, 'Squadra'] ---")

# Selezione di un valore specifico tramite posizione 
# numerica (indice di riga 0, indice di colonna 1).
# .iloc usa la posizione numerica (indice 0 per la riga, 
# indice 1 per la colonna 'Punti').
print("\n--- 11. Valore Singolo con .iloc[0, 1] ---")
print(f"Punti della squadra in posizione 0: {df.iloc[0, 1]}")
print("------------------------------------------------------------")