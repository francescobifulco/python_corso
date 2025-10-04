import pandas as pd

# Dizionario contenente i dati sui mesi e il numero di giorni
ds = {
    'Mesi': ['gennaio', 'febbraio', 'marzo', 'aprile', 
             'maggio', 'giugno', 'luglio', 'agosto', 
             'settembre', 'ottobre', 'novembre', 'dicembre'],
    'Giorni': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
}

# Creazione di un DataFrame di pandas a partire dal dizionario
df = pd.DataFrame(ds)

# Stampa del DataFrame per visualizzare la tabella creata
print("--- DataFrame 'Mesi e Giorni' ---")
print(df)
print("---------------------------------") 