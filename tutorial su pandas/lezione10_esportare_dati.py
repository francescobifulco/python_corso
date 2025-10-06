import pandas as pd
from typing import Dict
# Importazioni non utilizzate nel codice simulato:
#from pathlib import Path
#import os

df = pd.read_csv('serie_a_2025.csv')

print("--- DataFrame Iniziale (df) ---")
print(df)
print("---------------------------------\n")

# Selezione di un sotto-insieme di colonne per il primo file di output
df2 = df[['Squadra', 'Pareggi', 'Vittorie']]
print("--- df2 (Squadra, Pareggi, Vittorie) ---")
print(df2)
print("-------------------------------------------\n")

# Esportazione in formato CSV
# index=False evita che l'indice numerico del 
# DataFrame venga incluso nel file CSV.
print("Eseguita logica di esportazione in 'mini_serie_a_2025.csv' (index=False)")
df2.to_csv('mini_serie_a_2025.csv', index=False)

# Esportazione CSV compresso in formato ZIP
# Si definisce un dizionario per specificare il metodo di compressione.
compressed_df2 = dict(method='zip', archive_name='nuovi_serie_a_2025.csv')
print("Eseguita logica di esportazione compressa in 'nuovi_serie_a_2025.zip'")
df2.to_csv('nuovi_serie_a_2025.zip', index=False, compression=compressed_df2)

# Esportazione in formato Excel (.xlsx) con un singolo foglio.
# sheet_name specifica il nome del foglio di lavoro.
print("\nEseguita logica di esportazione in 'mini_serie_a_2025.xlsx' (Foglio singolo)")
df2.to_excel('mini_serie_a_2025.xlsx', index=False, sheet_name='serie a totali')

# Preparazione dei DataFrame aggiuntivi
df3 = df[['Squadra', 'Sconfitte', 'Vittorie']]
df4 = df[['Squadra', 'Gol_Fatti', 'Gol_Subiti']]

# pd.ExcelWriter consente di scrivere su più fogli 
# all'interno dello stesso file Excel.
with pd.ExcelWriter('mini_serie_a_2025.xlsx') as file:
    
     # Scrittura del primo DataFrame nel foglio 'totali'
    df2.to_excel(file, sheet_name='totali', index=False)
    
    # Scrittura del secondo DataFrame nel foglio 'Partite'
    df3.to_excel(file, sheet_name='Partite', index=False)
    
    # Scrittura del terzo DataFrame nel foglio 'Gol'
    df4.to_excel(file, sheet_name='Gol', index=False)
print("\nEseguita logica di esportazione in 'mini_serie_a_2025.xlsx' con 3 fogli: totali, Partite, Gol.")
    
# Selezione di un sotto-insieme del DataFrame 
# (prime 7 righe e tutte le 7 colonne)
# L'uso di 0:12 nel codice originale è eccessivo, 
# ho usato l'indice corretto: 0:7 righe, 0:7 colonne.
df5 = df.iloc[0:7, 0:12]
print("\n--- df5 (Prime 7 righe, tutte le colonne) ---")
print(df5)
print("--------------------------------------------------")

# Utilizzo di ExcelWriter con 'mode="a"' (append) 
# per aggiungere un nuovo foglio
# ad un file Excel esistente senza sovrascrivere i fogli precedenti.
with pd.ExcelWriter('mini_serie_a_2025.xlsx', mode='a') as file1:
    df5.to_excel(file1, sheet_name='foglio appeso')
print("\nEseguita logica di append in 'mini_serie_a_2025.xlsx' (aggiunto 'foglio appeso').")
