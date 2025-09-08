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


# --- Primo Gruppo di Radiobutton (Genere) ---

# Creiamo una StringVar per memorizzare il valore selezionato dal gruppo di radiobutton.
# Le StringVar sono variabili speciali di Tkinter per la gestione di stringhe.
genere = StringVar()

# Creiamo il primo Radiobutton.
r1 = Radiobutton(
    text='maschio',      # Testo visualizzato accanto al radiobutton.
    value='m',           # Il valore assegnato a questa opzione quando viene selezionata.
    variable=genere      # Collega questo radiobutton alla variabile 'genere'.
    )

r2 = Radiobutton(
    text='femmina',
    value='f',
    variable=genere
    )

# Creiamo un bottone che, quando premuto, stamperà il valore corrente della variabile 'genere'.
button = Button(
    text='prova',
    command=lambda:print(genere.get()) # Usiamo una lambda per chiamare print con il valore corrente della variabile.
                )

# Posizioniamo il radiobutton nella finestra usando il layout manager .pack()
r1.pack()
r2.pack()
button.pack()

# --- Secondo Gruppo di Radiobutton (Taglie) ---

# Creiamo un'altra StringVar per memorizzare la taglia selezionata.
taglia_selezionata = StringVar()

# Definiamo una tupla di tuple contenente le taglie. Ogni tupla ha il testo da mostrare
# e il valore associato (che verrà memorizzato nella StringVar).
taglie = (
    ('Smail','S'),
    ('Medium','M'),
    ('Large','L'),
    ('Extra Large','XL')
)

# Iteriamo sulla lista delle taglie per creare un Radiobutton per ciascuna.
for taglia in taglie:
    # Creiamo un Radiobutton di tipo ttk.Radiobutton per un aspetto più moderno.
    r = ttk.Radiobutton(
        root,                  # Il widget padre (la finestra principale).
        text=taglia[0],        # Il testo visibile (es. 'Smail').
        value=taglia[1],       # Il valore associato (es. 'S').
        variable=taglia_selezionata # Collega questo radiobutton alla variabile 'taglia_selezionata'.
    )
    # Posizioniamo il radiobutton nella finestra con un po' di spaziatura.
    r.pack(padx=5, pady=5)

# Creiamo un secondo bottone che stamperà la taglia selezionata quando premuto.
button = Button(
    text='prova',
    command=lambda:print(taglia_selezionata.get())
                )
button.pack()

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)