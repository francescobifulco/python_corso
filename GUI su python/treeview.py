# Importiamo le librerie necessarie: tkinter per l'interfaccia, ttk per i widget moderni
from tkinter import *
from tkinter import ttk

# Creiamo la finestra principale dell'applicazione (la radice del nostro programma)
root = Tk() 

# Definiamo il titolo della finestra
root.title('il nostro programma') 

# Impostiamo la dimensione e la posizione iniziale della finestra (larghezza x altezza + posizione x + posizione y)
root.geometry('600x400+500+500') 

# Disabilita o abilita la ridimensionabilità della finestra in larghezza e/o altezza
# root.resizable(False, True) 

# Imposta la dimensione minima della finestra che l'utente può raggiungere
root.minsize(400, 100) 

# Imposta la dimensione massima della finestra che l'utente può raggiungere
root.maxsize(1000, 1000) 

#root.iconbitmap("internet.ico") # Imposto la mia icona

# Imposta il livello di trasparenza della finestra (da 0.0 a 1.0)
# root.attributes('-alpha', 0.5) 

# Fa sì che la finestra rimanga sempre sopra le altre
# root.attributes('-topmost', 1) 

# Sposta la finestra in primo piano, portandola sopra le altre finestre
root.lift() 

# Sposta la finestra in secondo piano, dietro le altre finestre
# root.lower()

# --- Configurazione della Griglia e Creazione della Treeview ---

# Definiamo le colonne che la nostra tabella (Treeview) avrà.
# Queste sono etichette interne che useremo per riferirci alle colonne.
colonne = (
    'nome',
    'cognome',
    'email'
)

# Creiamo il widget Treeview.
# 'root' è il contenitore padre.
# 'columns=colonne' specifica le colonne da visualizzare.
# 'show='headings'' indica di mostrare solo le intestazioni delle colonne definite, nascondendo la colonna predefinita (spesso usata per icone).
tabella = ttk.Treeview(
    root,
    columns=colonne,
    show='headings'
)

# Configurazione delle intestazioni visibili delle colonne.
# 'tabella.heading('nome_colonna', text='Testo Intestazione')' imposta il testo per ogni colonna.
tabella.heading('nome', text='Nome')
tabella.heading('cognome', text='Cognome')
tabella.heading('email', text='Email')

# --- Generazione e Inserimento dei Dati Fittizi ---

# Creiamo una lista vuota che conterrà le righe di dati.
righe = []
# Generiamo 50 righe di dati fittizi.
for n in range(1,50):
    # Ogni riga è una tupla che corrisponde ai valori delle colonne definite.
    righe.append((f'nome {n}', 
                  f'cognome {n}',
                  f'email {n}'
                  ))

# Inseriamo ogni riga di dati nella Treeview.
# '' indica che la riga è una riga di primo livello (non nidificata).
# 'END' indica che la riga deve essere aggiunta alla fine.
# 'values=riga' imposta i valori della riga corrente.
for riga in righe:
    tabella.insert('', END, values=riga)

# Posizioniamo la Treeview nella finestra usando il geometry manager 'grid'.
# 'row=0' e 'column=0' la posizionano nella cella in alto a sinistra.
# 'sticky='nsew'' fa sì che la tabella si espanda per riempire tutta la cella
# (Nord, Sud, Est, Ovest) quando la finestra viene ridimensionata.
tabella.grid(
    row=0,
    column=0,
    sticky='nsew'
)

# --- Configurazione della Barra di Scorrimento (Scrollbar) ---

# Creiamo una barra di scorrimento verticale.
# 'root' è il contenitore.
# 'orient=VERTICAL' specifica che è una barra verticale.
# 'command=tabella.yview' collega la barra di scorrimento alla vista verticale della tabella.
# Quando la barra viene mossa, chiama la funzione 'yview' della tabella per aggiornare la visualizzazione.
scrollbar = ttk.Scrollbar(
    root,
    orient=VERTICAL,
    command=tabella.yview
)

# Posizioniamo la barra di scorrimento nella griglia.
# 'row=0' e 'column=1' la mettono alla destra della tabella.
# 'sticky='ns'' la fa espandere verticalmente per allinearsi con la tabella.
scrollbar.grid(
    row=0,
    column=1,
    sticky='ns'
)

# Colleghiamo la tabella alla barra di scorrimento.
# 'tabella.configure(yscrollcommand=scrollbar.set)' dice alla tabella di informare
# la barra di scorrimento (tramite scrollbar.set) ogni volta che la vista della tabella cambia,
# in modo che la barra di scorrimento possa aggiornare la sua posizione.
tabella.configure(yscrollcommand=scrollbar.set)

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)