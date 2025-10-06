import pandas as pd

# Seleziona solo la prima riga del DataFrame
df = pd.read_csv('serie_a_2025.csv').head(1)

print("--- Iterazione 1: Per Colonne (df.items()) ---")

# 'key' sarà il nome della colonna (es. 'Squadra'), 
# 'value' sarà la colonna come una Pandas Series.
for key, value in df.items():
    print(f"Colonna (Key): {key}")
    print(f"Contenuto (Value, tipo Series):\n{value}")
    
    # Stampa combinata (il valore è la Series, 
    # quindi apparirà formattata su più righe)
    print(f"Stampa combinata: {key}\n{value}\n")
    
# Seleziona le prime 10 righe del DataFrame
df = pd.read_csv('serie_a_2025.csv').head(10)

print("--- Iterazione 2: Per Righe (df.iterrows()) ---")

# 'index' sarà l'indice numerico della riga, 
# 'row' sarà il contenuto della riga come una Pandas Series.
for index, row in df.iterrows():
    print(f"Riga {index} (Row, tipo Series):\n{row}")
    # Stampa combinata
    print(f"Stampa combinata (Indice, Riga):\n{index}\n{row}\n")

df = pd.read_csv('serie_a_2025.csv')

print("--- Iterazione 3: Tentativo di Modifica con .iterrows() ---")

# Si tenta di modificare il nome della 'Squadra' nella prima riga
for index, row in df.iterrows():
    if index == 0:
         # Questa assegnazione modifica 
         # solo la copia locale 'row', NON il DataFrame df originale.
        row['Squadra'] = 'Cagliari (Tentativo di modifica fallito)'
    print(f"Riga {index} stampata (può mostrare la modifica temporanea):\n{row}")
    
# Stampa la prima riga del DataFrame df ORIGINALE.
# Si vedrà che la modifica non ha avuto effetto (rimane 'Inter').
print("\n--- Verifica Modifica: Il DataFrame originale non è cambiato (df.head(1)) ---")
print(df.head(1)) 

# Seleziona le prime 2 righe del DataFrame
df = pd.read_csv('serie_a_2025.csv').head(2)

print("\n--- Iterazione 4: La più Veloce (df.itertuples()) ---")

# 'row' è una namedtuple. Gli attributi sono accessibili come 
# 'row.Squadra', 'row.Punti', ecc.
for row in df.itertuples():
    # La tupla include l'indice della riga 
    # come primo elemento (di default 'Index').
    print(f"Tupla (NamedTuple):\n{row}")