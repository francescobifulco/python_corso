# Importiamo le librerie necessarie da tkinter
from calendar import month_name
from tkinter import *
from tkinter import ttk

# Importiamo la libreria per la connessione a MySQL
import mysql.connector


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

# --- Connessione al Database MySQL ---

# Ci connettiamo al database MySQL usando le credenziali specificate
try:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='miodatabase'
    )
    # Creiamo un oggetto cursore per eseguire le query SQL
    cursore = db.cursor()
except mysql.connector.Error as err:
    # Gestione degli errori di connessione
    print(f"Errore durante la connessione al database: {err}")
    # Chiudiamo l'applicazione se la connessione fallisce
    root.destroy()
    exit()

# Creiamo un oggetto cursore per eseguire le query SQL
cursore = db.cursor()

# --- Creazione e Popolamento della Tabella (Treeview) ---

# Eseguiamo una query per recuperare tutti i dati dalla tabella 'prodotti'
cursore.execute('SELECT * from prodotti')
risultato = cursore.fetchall()

# Definiamo le colonne della nostra tabella
colonne = (
    'id',
    'email',
    'username',
    'password',
           )

# Creiamo il widget Treeview, che agisce come una tabella
tabella = ttk.Treeview(
    root,
    columns=colonne,
    show='headings' # Mostra solo le intestazioni delle colonne
)

# Impostiamo il testo per le intestazioni di ogni colonna
tabella.heading('id',text='ID')
tabella.heading('email',text='EMAIL')
tabella.heading('username',text='USERNAME')
tabella.heading('password',text='PASSWORD')

# Inseriamo i dati recuperati nella tabella (Treeview)
for riga in risultato:
    tabella.insert('',END, values=riga)

# Posizioniamo la tabella nella griglia principale della finestra
tabella.grid(row=0, column=0, sticky='nsew')
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# --- Funzioni per le Operazioni sul Database ---

def inserisci():
    try:
        inserisci_Sql = 'INSERT INTO prodotti(nome_prodotto) VALUES (%s)'
        inserisci_valori = ('pc da game',)
        cursore.execute(inserisci_Sql,inserisci_valori)
        db.commit() # Salviamo le modifiche al database
        print("Record inserito con successo.")
    except mysql.connector.Error as err:
        print(f"Errore durante l'inserimento: {err}")
        
def modifica():
    try:
        modifica_sql = 'UPDATE prodotto SET nome_prodotto = "tavolo"WHERE nome_prodotto = "pc da game"'
        cursore.execute(modifica_sql)
        db.commit() # Salviamo le modifiche al databas
        print("Record inserito con successo.")
    except mysql.connector.Error as err:
        print(f"Errore durante la modifica: {err}")
        
def elimina():
    try:
        elimina_sql = 'DELETE FROM prodotti WHERE nome_prodotto = "pc da game"'
        cursore.execute(elimina_sql)
        db.commit() # Salviamo le modifiche al database
        print("Record eliminato con successo.")
    except mysql.connector.Error as err:
        print(f"Errore durante l'eliminazione: {err}")
    
# --- Creazione dei Bottoni ---

# Creiamo i bottoni e li associamo alle funzioni di gestione del database
inserisci_btn = Button(root, text='inserisci', command=inserisci)
modifica_btn = Button(root, text='modifica', command=modifica)
elimina_btn = Button(root, text='elimina', command=elimina)

# Posizioniamo i bottoni nella griglia
inserisci_btn.grid(row=1, column=0)
modifica_btn.grid(row=2, column=0)
elimina_btn.grid(row=3, column=0)

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)