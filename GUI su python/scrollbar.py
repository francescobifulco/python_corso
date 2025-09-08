# Importiamo le librerie necessarie: tkinter per l'interfaccia, ttk per i widget moderni
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext # Scrolledtext per il widget di testo con scorrimento automatico.

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

# La sezione commentata qui sotto mostra l'uso di un widget Listbox con una Scrollbar
# implementata manualmente. Il codice successivo utilizza un widget più semplice,
# ScrolledText, che integra già la funzionalità di scorrimento.

'''linguaggi = (
    'Javascript',
    'Java',
    'C',
    'C++',
    'Python',
    'PHP',
    'Ruby',
    'Go',
    'Javascript',
    'Java',
    'C',
    'C++',
    'Python',
    'PHP',
    'Ruby',
    'Go',
    'Javascript',
    'Java',
    'C',
    'C++',
    'Python',
    'PHP',
    'Ruby',
    'Go',
    'Javascript',
    'Java',
    'C',
    'C++',
    'Python',
    'PHP',
    'Ruby',
    'Go'
    )

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

linguaggio_selezionato = StringVar(value=linguaggi)
listbox = Listbox(
    root,
    listvariable=linguaggio_selezionato,
    height=6,
    selectmode='extended'
)
listbox.grid(
    column=0,
    row=0,
    sticky='nwes'
)

scrollbar = ttk.Scrollbar(
    root,
    orient='vertical',
    command=listbox.yview
)
scrollbar.grid(
    row=0,
    column=1,
    sticky='ns'
    )

listbox['yscrollcommand'] = scrollbar.set
'''

# --- Creazione del Widget ScrolledText ---

# Creiamo un widget ScrolledText.
# Questo widget è una combinazione di un widget Text e di una Scrollbar,
# il che lo rende ideale per campi di testo multi-linea con contenuti lunghi.
scrolledtxt = scrolledtext.ScrolledText(
    root,
    width=50,  # Imposta la larghezza del widget in caratteri.
    height=10  # Imposta l'altezza del widget in righe.
)

# Posizioniamo il widget ScrolledText nella finestra.
# 'fill=BOTH' estende il widget per riempire lo spazio sia in orizzontale che in verticale.
# 'side=LEFT' lo allinea a sinistra all'interno dello spazio del suo contenitore.
# 'expand=True' permette al widget di espandersi per riempire lo spazio extra se la finestra viene ridimensionata.
scrolledtxt.pack(
    fill=BOTH, 
    side=LEFT, 
    expand=True
    )

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)