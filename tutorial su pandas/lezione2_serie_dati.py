import pandas as pd

# Dizionario 'ds': Mappa delle etichette (chiavi) ai valori numerici.
# Questo sarà la fonte dei dati per la nostra Series.
ds = {
    'preUno': 5,
    'preDue': 10,
    'preTre': 15,
    'preQuattro': 20,
    'preCinque': 25
    }

# --- Creazione della prima Serie (Selezione Parziale) ---

# Si crea una Serie usando l'intero dizionario ds,
# ma si usa l'argomento 'index' 
# per selezionare solo le chiavi (indici) 
# specificate ('preDue' e 'preTre').
# Tutte le altre chiavi del dizionario vengono ignorate.
pandasSerie = pd.Series(ds, index=['preDue', 'preTre'])

print("--- Prima Serie (Selezione Parziale) ---")
print(pandasSerie)

# Accesso a un singolo elemento della Serie usando 
# il suo indice (etichetta)
print("\nValore dell'elemento con indice 'preTre':")
print(pandasSerie['preTre'])

# --- Creazione della seconda Serie (Completa) ---

# Si crea una Serie usando l'intero dizionario 
# ds senza specificare 'index'.
# La Serie includerà automaticamente tutte le 
# coppie chiave-valore del dizionario.
pandasSerie1 =  pd.Series(ds)

print("\n--- Seconda Serie (Completa) ---")
print(pandasSerie1)
print("-----------------------------------")