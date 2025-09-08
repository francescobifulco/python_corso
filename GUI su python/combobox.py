# Importiamo le librerie necessarie da tkinter
from calendar import month_name # Importiamo la liberia calendario
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

# Creiamo una variabile di controllo di tipo StringVar per memorizzare il valore selezionato dalla combobox
mese_selezionato = StringVar()

# Creiamo il widget Combobox, associandolo alla finestra principale e alla variabile
comobobox = ttk.Combobox(
    root,
    textvariable=mese_selezionato
)

# Impostiamo la lista dei valori (i mesi dell'anno) per la combobox
comobobox['values'] = [month_name[m] for m in range(1,13)]

# Impostiamo lo stato della combobox su "readonly" per impedire all'utente di digitare valori non presenti
comobobox['state'] = 'readonly'

# Posizioniamo la combobox nella finestra
comobobox.pack()

# Definiamo una funzione che gestisce l'evento di selezione di un elemento dalla combobox
def evento_mese(event):
     # Stampiamo il valore del mese selezionato
    print(mese_selezionato.get())

# Associamo l'evento di selezione del Combobox alla funzione "evento_mese"
comobobox.bind('<<ComboboxSelected>>',
               evento_mese
               ) # La stringa '<<ComboboxSelected>>' è l'evento che si verifica quando un elemento è scelto

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)