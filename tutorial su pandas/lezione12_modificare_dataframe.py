import pandas as pd


df = pd.read_csv('serie_a_2025.csv')

print("--- DataFrame Iniziale ---")
print(df)
print("----------------------------\n")

# Filtro iniziale: Seleziona e stampa la riga della 'Juventus'
print("--- 1. Riga 'Juventus' prima della modifica ---")
print(df.loc[df['Squadra'] == 'Juventus'])

# Modifica (Condizione, Colonna) = Nuovo Valore
# Cambia il nome della squadra da 'Juventus' a 'Juve'.
df.loc[df['Squadra'] == 'Juventus', 'Squadra'] = 'Juve'

print("\n--- 2. Modifica Singola Colonna (Juve) ---")
print(df[df['Squadra'] == 'Juve'])

# Modifica (Condizione, [Lista Colonne]) = Nuovo Valore Unico
# Imposta Gol_Fatti e Gol_Subiti a 45 per la squadra 'Lecce'.
df.loc[df['Squadra'] == 'Lecce', ['Gol_Fatti', 'Gol_Subiti']] = 45

print("\n--- 3. Modifica Colonne Multiple (Lecce) con Valore Unico ---")
# Stampa solo la riga appena modificata per verifica
print(df[df['Squadra'] == 'Lecce'])

# Modifica (Condizione, [Lista Colonne]) = [Lista di Nuovi Valori]
# Imposta Gol_Fatti a 32 e Gol_Subiti a 23 per la 'Fiorentina'.
# NOTA: L'ordine dei valori nella lista deve corrispondere 
# all'ordine delle colonne.
df.loc[df['Squadra'] == 'Fiorentina', ['Gol_Fatti', 'Gol_Subiti']] = [32, 23]

print("\n--- 4. Modifica Colonne Multiple (Fiorentina) con Lista di Valori ---")
# Stampa solo la riga appena modificata per verifica
print(df[df['Squadra'] == 'Fiorentina'])

# Modifica (Condizione Complessa, [Lista Colonne]) 
# = [Lista di Nuovi Valori]
# Condizione: 'Squadra' contiene 'er' (Inter) E
# 'Punti' è maggiore di 80 (85).
# La condizione è soddisfatta solo per l'Inter.
df.loc[(df['Squadra'].str.contains('er')) & (df['Punti'] > 80), ['Gol_Fatti', 'Gol_Subiti']] = [100, 10]

print("\n--- 5. Modifica con Filtro AND Combinato (Inter) ---")
# Stampa la riga dell'Inter per verifica (Gol_Fatti=100, Gol_Subiti=10)
print(df[df['Squadra'] == 'Inter'])
print("----------------------------------------------------------------")