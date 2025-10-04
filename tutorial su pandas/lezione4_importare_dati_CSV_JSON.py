import pandas as pd

# Uso di pd.read_csv per creare il DataFrame dalla stringa CSV.
# index_col=0 imposta la prima colonna ('Squadra') 
# come indice delle righe.
df = pd.read_csv('serie_a_2025.csv', index_col=0)

# Stampa del DataFrame completo per contesto
print("--- DataFrame Simulato Serie A (df) ---")
print(df)
print("------------------------------------------")

# Uso di .loc['Inter'] per selezionare e stampare l'intera riga 
# corrispondente all'indice (squadra) 'Inter'.
print("\n--- Selezione Righe: Dati dell'Inter (.loc) ---")
print(df.loc['Inter'])
print("--------------------------------------------------")

# Uso di pd.read_json per creare il DataFrame dalla stringa JSON.
df1 = pd.read_json('csvjson.json')

# Stampa del DataFrame creato dal JSON.
print("\n--- DataFrame Simulato da JSON (df1) ---")
print(df1)
print("-------------------------------------------")
