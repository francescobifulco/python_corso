import pandas as pd

df = pd.read_csv('serie_a_2025.csv')

print("--- DataFrame Iniziale (non ordinato) ---")
print(df)
print("-------------------------------------------\n")

# L'indice numerico è già ordinato nel DataFrame di default, 
# quindi questo comando ha un effetto 
# visibile nullo qui, ma è cruciale 
# se l'indice fosse stato personalizzato o riorganizzato.
sidf = df.sort_index()
print("--- 1. Ordinamento per Indice (di default: ascendente) ---")
print(sidf.head(5))

# Ordina il DataFrame in base alla colonna 
# 'Squadra' (alfabetico, A-Z di default).
svdf = df.sort_values(by='Squadra')
print("\n--- 2. Ordinamento per 'Squadra' (Ascendente - A/Z) ---")
print(svdf.head(5))

# Ordina in base alla colonna 'Squadra' in ordine decrescente (Z-A).
svdf1 = df.sort_values(by='Squadra', ascending=False)
print("\n--- 3. Ordinamento per 'Squadra' (Discendente - Z/A) ---")
print(svdf1.head(5))

# Ordina prima per 'Squadra' (A-Z) e poi, 
# in caso di pareggio nel nome squadra, 
# per 'Vittorie' (numerico ascendente).
# Ho selezionato solo alcune colonne per la 
# stampa per renderla più chiara.
svdf2 = df.sort_values(by=['Squadra', 'Vittorie'])
print("\n--- 4. Ordinamento Multi-Colonna: [Squadra A-Z, Vittorie Ascendenti] ---")
print(svdf2[['Squadra', 'Punti', 'Pareggi']].head(7))

# Ordina prima per 'Squadra' (Z-A) e poi per 
# 'Vittorie' (numerico decrescente).
# NOTA: L'opzione 'ascending=False' si applica a ENTRAMBE le colonne.
svdf3 = df.sort_values(by=['Squadra', 'Vittorie'], ascending=False)
print("\n--- 5. Ordinamento Multi-Colonna: [Squadra Z-A, Vittorie Discendenti] ---")
print(svdf3[['Squadra', 'Punti', 'Pareggi']].head(7))

# Ordinamento con direzioni miste.
# ascending=[False, True] significa:
# 1. 'Squadra': False (Decrescente / Z-A)
# 2. 'Vittorie': True (Ascendente / 0-9)
svdf4 = df.sort_values(by=['Squadra', 'Vittorie'], ascending=[False, True])
print("\n--- 6. Ordinamento Misto: [Squadra Z-A, Vittorie Ascendenti] ---")
print(svdf4[['Squadra', 'Punti', 'Pareggi']].head(5))
print("-------------------------------------------------------------------")