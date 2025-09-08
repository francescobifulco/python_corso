# Importiamo le librerie necessarie da tkinter
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

# La sezione commentata con le 'Label' mostra un esempio dell'uso del metodo .pack(), che posiziona i widget in blocchi.
# Questo metodo non è usato nel codice finale ma è utile per dimostrare un'alternativa a .grid().

"""
label1 = Label(
    root,
    text='Label 1',
    background='green',
    foreground='white'
)
label1.pack(
    ipadx=10,
    ipady=10,
    fill=X
    )

label2 = Label(
    root,
    text='Label 2',
    background='red',
    foreground='white'
)
label2.pack(
    ipadx=10,
    ipady=10,
    fill=X
    )

label3 = Label(
    root,
    text='Label 3',
    background='blue',
    foreground='white'
)
label3.pack(
    ipadx=10,
    ipady=10,
    fill=X
    )

label4 = Label(
    root,
    text='Label 4',
    background='purple',
    foreground='white'
)
label4.pack(
    ipadx=10,
    ipady=10,
    fill=X,
    expand=True,
    side=LEFT
    )

label5 = Label(
    root,
    text='Label 5',
    background='yellow',
    foreground='white'
)
label5.pack(
    ipadx=10,
    ipady=10,
    fill=X,
    expand=True,
    side=LEFT
    )

label6 = Label(
    root,
    text='Label 6',
    background='orange',
    foreground='white'
)
label6.pack(
    ipadx=10,
    ipady=10,
    fill=X,
    expand=True,
    side=LEFT
    )"""

# --- Impostazione della Griglia ---

# Configura il comportamento di ridimensionamento della colonna 0 della griglia.
# weight=1 significa che la colonna si espanderà per occupare lo spazio disponibile.
root.columnconfigure(
    0,
    weight=1
    )

# Configura il comportamento di ridimensionamento della colonna 1.
root.columnconfigure(
    1,
    weight=1
    )

# --- Creazione dei Frame ---
# Creiamo quattro Frame, ognuno con un colore e dimensioni specifiche, che useremo come "celle" della nostra griglia.

frame1 = Frame(
    root,
    background='red',
    height=200,
    width=200
)
frame2 = Frame(
    root,
    background='yellow',
    height=200,
    width=200
)
frame3 = Frame(
    root,
    background='blue',
    height=200,
    width=200
)
frame4 = Frame(
    root,
    background='orange',
    height=200,
    width=200
)

# --- Posizionamento dei Frame nella Griglia ---
# Utilizziamo il metodo .grid() per posizionare ogni Frame in una cella specifica della griglia.
# La griglia ha 2 righe (0 e 1) e 2 colonne (0 e 1).

# Posiziona il frame1 nella riga 0, colonna 0.
# columnspan=2 fa in modo che il frame si estenda su 2 colonne.
frame1.grid(
    column=0,
    row=0,
    #rowspan=2,# Opzione per estendere il frame su più righe
    columnspan=2
)
frame2.grid(
    column=1,
    row=0
)
frame3.grid(
    column=0,
    row=1
    
)
frame4.grid(
    column=1,
    row=1
)

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)