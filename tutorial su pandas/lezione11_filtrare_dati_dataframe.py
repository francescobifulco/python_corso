import pandas as pd

df = pd.read_csv('serie_a_2025.csv')

print("--- DataFrame Iniziale ---")
print(df)
print("----------------------------\n")

# Stampa la colonna 'Squadra' (risultato: una Pandas Series)
print("--- 1. Selezione Singola Colonna 'Squadra' ---")
print(df['Squadra'])

# Filtro: Seleziona le righe dove la colonna 
# 'Squadra' è esattamente 'Roma'.
print("\n--- 2. Filtro per Uguaglianza (Squadra == 'Roma') ---")
print(df[df['Squadra'] == 'Roma'])

# Filtro: Seleziona le righe dove la colonna 
# 'Squadra' NON è 'Roma' (operatore !=).
print("\n--- 3. Filtro per Disuguaglianza (Squadra != 'Roma') ---")
print(df[df['Squadra'] != 'Roma'])

# Filtro basato su stringa: .str.contains() 
# cerca un frammento ('na') all'interno del nome della squadra.
print("\n--- 4. Filtro Stringa (Squadra contiene 'na') ---")
print(df[df['Squadra'].str.contains('na')])

# Filtro: Seleziona le righe dove la colonna 
# 'Squadra' è contenuta nella lista 'filtro' (operatore .isin()).
filtro = ['Inter', 'Fiorentina', 'Juventus']
print("\n--- 5. Filtro per Lista (Squadra .isin(filtro)) ---")
print(df[df['Squadra'].isin(filtro)])

# Filtro: Seleziona le righe dove 'Punti' è maggiore di 35.
print("\n--- 6. Filtro Numerico (Punti > 35) ---")
print(df[df['Punti'] > 35])

# Filtro: Seleziona le righe dove 'Punti' è minore di 50.
print("\n--- 7. Filtro Numerico (Punti < 50) ---")
print(df[df['Punti'] < 50])

# Filtro: NOT (Punti < 50) -> Equivale a Punti >= 50.
# L'operatore tilde (~)
# inverte il risultato booleano della condizione.
print("\n--- 8. Filtro NOT (Punti >= 50) ---")
print(df[~df['Punti'] < 50])

# Filtro combinato AND: Punti > 35 E Gol_Fatti > 12.
# Le parentesi attorno a ciascuna condizione 
# sono MANDATORIE quando si usano & o |.
print("\n--- 9. Filtro Combinato AND (&) ---")
print(df[(df['Punti'] > 35) & (df['Gol_Fatti'] > 12)])

# Filtro combinato OR: Punti > 50 OPPURE Gol_Fatti > 23.
print("\n--- 10. Filtro Combinato OR (|) ---")
print(df[(df['Punti'] > 50) | (df['Gol_Fatti'] > 23)])

# Filtro e Selezione con .loc: 
# 1. Filtra: df['Squadra'] == 'Napoli'
# 2. Seleziona Colonne: 
# ['Squadra', 'Punti', 'Gol_Fatti', 'Gol_Subiti']
print("\n--- 11. Filtro + Selezione Colonne con .loc ---")
print(df.loc[(df['Squadra'] == 'Napoli'), ['Squadra', 'Punti', 'Gol_Fatti', 'Gol_Subiti']])

# Filtro e Selezione con .loc e .str.contains:
print("\n--- 12. Filtro Stringa + Selezione Colonne con .loc ---")
print(df.loc[(df['Squadra'].str.contains('na')), ['Squadra', 'Punti', 'Gol_Fatti', 'Gol_Subiti']])

# Filtro con df.query(): Usa una sintassi basata 
# su stringhe, più leggibile.
# Utile soprattutto per condizioni complesse.
print("\n--- 13. Filtro con df.query('Squadra == \"Lecce\"') ---")
print(df.query('Squadra == "Lecce"'))

# Filtro con df.query() combinato (AND).
# L'esempio originale non produceva risultati, 
# l'ho adattato per mostrare la sintassi query.
# Seleziona le righe con Punti > 50 E Sconfitte < 10.
print("\n--- 14. Filtro con df.query('Punti > 50 and Sconfitte < 10') ---")
print(df.query('Punti > 78 and Sconfitte > 10'))
print("-------------------------------------------------------------------")
