import pandas as pd

df = pd.read_csv('serie_a_2025.csv')

print("--- DataFrame Iniziale ---")
print(df)
print("----------------------------\n")

# Aggiunta di una singola colonna con un valore fisso. 
# Questo è il modo più semplice e veloce.
df['Supercoppa Italiana'] = 4
print("--- 1. Colonna Singola Aggiunta (df['Nuova Colonna'] = valore) ---")

# Stampa le colonne selezionate per verificare l'aggiunta.
print(df[['Squadra', 'Gol_Subiti', 'Supercoppa Italiana']])

# Aggiunta/Modifica di più colonne contemporaneamente 
# con una lista di valori scalari.
# La lista [3, 2, 4] viene assegnata a ogni 
# riga delle tre nuove colonne.
df[['Supercoppa Italiana', 'Scudeti', 'Coppa Italia']] = [3,2,4]
print("\n--- 2. Colonne Multiple Aggiunte/Modificate ---")
print(df[['Squadra', 'Supercoppa Italiana', 'Scudeti', 'Coppa Italia']])

# Aggiunta di una colonna in una posizione specifica 
# (indice 2, dopo 'Punti').
# 'Stelle' sarà la terza colonna (indice 2).
df.insert(2, 'Stelle', 3)
print("\n--- 3. Colonna Aggiunta con df.insert(Posizione, Nome, Valore) ---")
print(df.head())

# Aggiunta di una colonna tramite .loc. 
# Simile al metodo df['colonna'], ma 
# usa la sintassi .loc per garantire l'allineamento.
df.loc[:, 'Coppa Italia Serie C'] = 4
print("\n--- 4. Colonna Aggiunta con df.loc[:, 'Nuova Colonna'] ---")
print(df.head())

# Aggiunta di una colonna tramite il metodo 
# .assign (utile per il chaining).
df = df.assign(Champions_League = 3)
print("\n--- 5. Colonna Aggiunta con df.assign() ---")
print(df.head())

# Eliminazione con df.drop(). axis=1 indica che 
# stiamo eliminando una colonna.
# inplace=True modifica il DataFrame df direttamente 
# (non necessario riassegnare df = df.drop(...)).
df.drop('Supercoppa Italiana', inplace=True, axis=1)
print("\n--- 6. Eliminazione Colonna con df.drop(..., axis=1, inplace=True) ---")
print(df.head())

# Eliminazione con l'istruzione del. Metodo Python standard e veloce.
del df['Coppa Italia Serie C']
print("\n--- 7. Eliminazione Colonna con del df['Nome Colonna'] ---")
print(df.head())

# Eliminazione con df.pop(). 
# Questo metodo elimina la colonna e la restituisce come Serie.
colPop = df.pop('Squadra')
print("\n--- 8. Eliminazione Colonna con df.pop('Nome Colonna') ---")
print("DataFrame senza 'Squadra':")
print(df.head(2))
print("\nSerie restituita dalla pop (le prime 2 righe):")
print(colPop.head(2))

# Selezione basata sulle etichette delle colonne (nomi).
print("\n--- 9. Selezione Colonne (Etichette) con df.loc[:, lista] ---")
print(df.loc[:, ['Vittorie', 'Punti', 'Scudeti']])

# Selezione basata sull'indice numerico delle colonne (iloc). 
# Riordina le colonne in base alla loro posizione.
# Le colonne sono ora: [Punti, Pareggi, Vittorie, 
# Sconfitte, Gol_Subiti, Stelle, Scudeti, 
# Coppa Italia, Champions_League]
# Il comando stampa: Punti (1), Sconfitte (3), 
# Pareggi (2), Gol_Subiti (4), ...
print("\n--- 10. Selezione/Riordinamento Colonne (Posizione) con df.iloc[:, lista] ---")
print(df.iloc[:, [1,3,2,4,5,0]])

# Riordinamento usando il reverse della lista dei nomi delle colonne.
# Ottieni la lista dei nomi delle colonne, 
# la inverti e usi la lista per selezionare (riordinare) il DataFrame.
columns = list(df.columns)
columns.reverse()
print("\n--- 11. Riordinamento Colonna (Inversione lista nomi) ---")
print(df[columns].head())

# Ripetizione dell'esempio 11 con un altro modo per 
# ottenere la lista delle colonne.
columns1 = df.columns.tolist()
columns1.reverse()
print("\n--- 12. Riordinamento Colonna (Inversione tolist()) ---")
print(df[columns1].head())

# Assegnazione del DataFrame riordinato (permanente).
columns2 = df.columns.tolist() # Ricarico la lista dei nomi delle colonne, prima di invertirla
columns2.reverse()
df = df[columns2]
print("\n--- 13. Assegnazione Permanente del Riordinamento ---")
print(df.head())
print("---------------------------------------------------------")