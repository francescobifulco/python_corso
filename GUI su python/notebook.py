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

# --- Creazione del Notebook (Interfaccia a Schede) ---

# Creiamo il widget Notebook, che serve da contenitore per le schede.
notebook = ttk.Notebook(root)

# Posizioniamo il notebook nella finestra principale.
# pady aggiunge un po' di spaziatura esterna.
# fill=BOTH e expand=True fanno in modo che il notebook si espanda
# e riempia tutto lo spazio disponibile quando la finestra viene ridimensionata.
notebook.pack(
    pady=10,
    fill=BOTH,
    expand=True
)

# --- Creazione delle Schede (Frame) ---

# Le schede non sono widget diretti, ma sono contenitori (Frame) che vengono
# aggiunti al notebook. Creiamo tre Frame per le nostre tre schede.
frame1 = ttk.Frame(
    notebook, # Questo Frame è un "figlio" del notebook
    width=400,
    height=280
    )
frame2 = ttk.Frame(
    notebook,
    width=400,
    height=280
    )
frame3 = ttk.Frame(
    notebook,
    width=400,
    height=280
    )

# Posizioniamo i frame all'interno del notebook.
# Anche se i Frame sono figli del notebook, devono comunque essere "impacchettati"
# per essere gestiti dal layout.
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)

# --- Aggiunta dei Frame al Notebook come Schede ---

# Il metodo .add() del notebook aggiunge un Frame come una nuova scheda.
# Il parametro 'text' definisce l'etichetta visibile sulla scheda.
notebook.add(frame1, text='tab1')
notebook.add(frame2, text='tab2')
notebook.add(frame3, text='tab3')
# --- Contenuto delle Schede ---

# Ogni scheda (Frame) può contenere i propri widget.
# In questo caso, aggiungiamo una semplice Label a ogni Frame.
label1 = Label(frame1, text='ciao').pack() # La Label è un "figlio" di frame1
label2 = Label(frame2, text='buongiorno').pack() # La Label è un "figlio" di frame2
label3 = Label(frame3, text='arrivederci').pack() # La Label è un "figlio" di frame3

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)