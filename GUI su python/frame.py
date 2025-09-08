# Importiamo le librerie necessarie da tkinter
from calendar import month_name
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

# --- Creazione dei Contenitori (Frame e LabelFrame) ---

# Creiamo un contenitore di tipo LabelFrame.
# A differenza di un normale Frame, il LabelFrame ha un bordo e può avere un titolo.
frame0 = LabelFrame(
    root,
    text='sono label frame',  # Testo che appare sul bordo del contenitore
    padx=10,  # Spaziatura orizzontale interna al frame
    pady=50,  # Spaziatura verticale interna al frame
    height=100, # Altezza del frame (specificata ma spesso ignorata dai gestori di geometria come pack)
    width=200 # Larghezza del frame (specificata ma spesso ignorata da pack)
)
# Posizioniamo il LabelFrame nella finestra principale
frame0.pack(
    # fill=X,  # Estende il contenitore in larghezza
    # expand=True # Espande il contenitore per riempire lo spazio disponibile
)

# Creiamo un contenitore di tipo Frame.
# I Frame sono usati per raggruppare i widget e organizzarli.
frame1 = Frame(
    root,
    background='red',# Imposta il colore di sfondo del frame
    padx=10,
    pady=50,
    height=100,
    width=200
)
frame1.pack(
    #fill=X,
    #expand=True
    )

frame2 = Frame(
    root,
    background='yellow',
    padx=10,
    pady=50,
    height=100,
    width=200
)
frame2.pack(
    #fill=X,
    #expand=True
    )

frame3 = Frame(
    root,
    background='green',
    padx=10,
    pady=50,
    height=100,
    width=200
)
frame3.pack(
    #fill=X,
    #expand=True
    )

# --- Creazione dei Widget Figli (Bottoni) ---
# I bottoni che seguono non sono posizionati direttamente in "root",
# ma all'interno dei Frame che abbiamo appena creato.

button1 = Button(
    frame1,
    text='ciao'
)
button1.pack()

button2 = Button(
    frame2,
    text='ciao'
)
button2.pack()

button3 = Button(
    frame3,
    text='ciao'
)
button3.pack()

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)