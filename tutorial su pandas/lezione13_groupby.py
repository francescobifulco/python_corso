import pandas as pd

df = pd.read_csv('serie_a_2025.csv')

print("--- DataFrame Iniziale ---")
print(df)
print("----------------------------\n")

# Raggruppa il DataFrame in base ai valori 
# unici della colonna 'Punti'.
# Il risultato è un oggetto GroupBy, non un DataFrame.
punti = df.groupby('Punti')

# Stampa i gruppi: mostra un dizionario dove 
# la chiave è il valore 'Punti' 
# e il valore è la lista degli indici di riga 
# che appartengono a quel gruppo.
print("--- 1. Gruppi in base a 'Punti' (.groups) ---")
print(punti.groups)

# Iterazione sull'oggetto GroupBy:
# 'name' è il valore di raggruppamento (es. 60, 50, 45).
# 'group' è il DataFrame contenente 
# solo le righe che hanno quel 'name'.
print("\n--- 2. Iterazione sui Gruppi di 'Punti' ---")
for name, group in punti:
    print(f"\nGruppo Punti: {name}")
    print(group)
    
# Raggruppa il DataFrame usando Criteri 
# Multipli (tupla di colonne).
# Le righe sono raggruppate solo se hanno la stessa 
# combinazione di Gol_Fatti E Gol_Subiti.
gol = df.groupby(['Gol_Fatti', 'Gol_Subiti'])

print("\n-- 3. Gruppi in base a ['Gol_Fatti', 'Gol_Subiti'] ---")
print(gol.groups)

# Iterazione sui gruppi multipli. 'name' è ora 
# una tupla (Gol_Fatti, Gol_Subiti).
print("\n--- 4. Iterazione sui Gruppi Multipli ---")
for name, group in gol:
    print(f"\nGruppo Gf/Gs: {name}")
    print(group)

# Calcola la media (mean) per ogni colonna 
# numerica all'interno di ciascun gruppo 'Punti'.
# numeric_only=True garantisce che vengano 
# considerate solo le colonne numeriche.
punti1 = df.groupby(['Punti']).mean(numeric_only=True)
print("\n--- 5. Media di Tutte le Colonne per 'Punti' ---")
print(punti1)

# Raggruppa per 'Punti', Seleziona Colonne e 
# calcola la Media.
# Selezionando esplicitamente le colonne, è possibile 
# omettere numeric_only=True.
punti2 = df.groupby(['Punti'])[['Vittorie','Pareggi', 'Sconfitte']].mean()
print("\n--- 6. Media di Colonne Selezionate per 'Punti' ---")
print(punti2)

# Calcola la media, poi ordina il risultato in base 
# alla colonna 'Gol_Fatti' (discendente).
punti3 = df.groupby(['Punti'])[['Vittorie','Pareggi', 'Sconfitte', 'Gol_Fatti']].mean()
print("\n--- 7. Media Ordinata per 'Gol_Fatti' (Discendente) ---")
print(punti3.sort_values(by='Gol_Fatti', ascending=False))

# Calcola la Somma (sum) dei valori per ogni gruppo 'Punti'.
punti4 = df.groupby(['Punti'])[['Vittorie','Pareggi', 'Sconfitte']].sum()
print("\n--- 8. Somma Totale per 'Punti' ---")
print(punti4)

# Calcola il Valore Minimo (min) dei valori per ogni gruppo 'Punti'.
punti5 = df.groupby(['Punti'])[['Vittorie','Pareggi', 'Sconfitte']].min()
print("\n--- 9. Valore Minimo per 'Punti' ---")
print(punti5)

# Calcola il Valore Massimo (max) dei valori per ogni gruppo 'Punti'.
punti6 = df.groupby(['Punti'])[['Vittorie','Pareggi', 'Sconfitte']].max()
print("\n--- 10. Valore Massimo per 'Punti' ---")
print(punti6)

# Calcola il Conteggio (count) delle righe in ogni gruppo.
# Il risultato conta le occorrenze non-NaN per tutte le 
# altre colonne in ciascun gruppo.
punti7 = df.groupby(['Punti']).count()
print("\n--- 11. Conteggio (count) di tutte le colonne per 'Punti' ---")
print(punti7)

# Metodo consigliato per contare il numero di 
# elementi (squadre) in ciascun gruppo:
# 1. Crea una colonna fittizia con un valore 
# fisso ('count' = 1).
df['count'] = 1

# 2. Raggruppa per 'Punti' e somma la 
# colonna 'Conteggio Squadre'.
# Il risultato è una Serie che mostra il 
# numero esatto di squadre per ogni punteggio.
punti8 = df.groupby(['Punti']).count()['count']
print("\n--- 12. Conteggio Esplicito delle Squadre per 'Punti' (Consigliato) ---")
print(punti8)
print("-------------------------------------------------------------------------")