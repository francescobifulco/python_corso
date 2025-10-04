import pandas as pd

# Dizionario contenente i dati sui mesi, giorni, 
# stagione e alcune festività.
# Le chiavi del dizionario ('Mesi', 'Giorni', 
# 'Stagione', 'Festivita') diventeranno 
# i nomi delle colonne nel DataFrame.
ds = {
    'Mesi': ['gennaio', 'febbraio', 'marzo', 'aprile', 
             'maggio', 'giugno', 'luglio', 'agosto', 
             'settembre', 'ottobre', 'novembre', 'dicembre'],
    'Giorni': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    'Stagione': ['inverno', 'inverno', 'primavera', 'primavera',
                 'primavera', 'estate', 'estate', 'estate',
                 'autunno', 'autunno', 'autunno', 'inverno'],
    'Festivita': ['capodanno', 'carnevale', 'festa delle donne', 
                  'pasqua', 'Festa dei lavoratori', 
                  'Festa della Repubblica', 'Ferragosto', 
                  'Assunzione di Maria', 'Inizio scuola', 
                  'Ognissanti', 'Giorno dei morti', 'Natale']
}

# Creazione di un DataFrame di pandas a partire dal dizionario.
df = pd.DataFrame(ds, index=['gen', 'feb', 'mar', 'apr', 'mag', 'giu', 
                             'lug', 'ago', 'set', 'ott', 'nov', 'dic'])

print("--- DataFrame Completo: Mesi, Giorni, Stagioni e Festività ---")
print(df)
print("---------------------------------")

# --- Selezione e stampa di righe specifiche tramite l'indice (metodo .loc) ---

# Si utilizza .loc per selezionare 
# le righe basandosi sulle etichette dell'indice 
# fornite nella lista ['gen', 'ott'].
# Questo restituisce i dati completi per i mesi di Gennaio e Ottobre.
print("\n--- Selezione Righe: Gennaio e Ottobre (usando .loc) ---")
print(df.loc[['gen', 'ott']])
print("------------------------------------------------------------")