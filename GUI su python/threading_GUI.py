# Importiamo le librerie necessarie: tkinter per l'interfaccia, ttk per i widget moderni
import time # Il modulo time per la funzione di pausa
from tkinter import *
from tkinter import ttk
import threading # Threading per la gestione dei thread.

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

# --- Funzioni per le Operazioni ---

def dormi():
    #Questa funzione simula un'operazione che richiede molto tempo (5 secondi).
    #Senza un thread, bloccherebbe l'intera interfaccia grafica.
    time.sleep(5)
    print('stavo dormendo...')
    
def mangia():
    print('stavo mangiando...') #Questa funzione esegue un'operazione istantanea.

# --- Creazione e Configurazione dei Bottoni ---

# Creiamo un bottone per l'operazione "dormi".
button1 = Button(
    root,
    text='dormi',
    # Colleghiamo il bottone a una funzione lambda che avvia un nuovo thread.
    # Il thread viene creato e la funzione 'dormi' viene eseguita al suo interno.
    # Questo permette all'interfaccia di rimanere reattiva.
    command=lambda: threading.Thread(target=dormi).start()
)
button1.pack(expand=True, fill=X)

# Creiamo un bottone per l'operazione "mangia".
button2 = Button(
    root,
    text='mangia',
    # Questo bottone esegue la funzione 'mangia' direttamente nel thread principale di Tkinter.
    # Poiché l'operazione è istantanea, non c'è rischio di blocco.
    command=mangia
)
button2.pack(expand=True, fill=X)

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)