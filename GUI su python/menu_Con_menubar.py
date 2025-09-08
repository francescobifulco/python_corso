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

# --- Creazione della Barra dei Menu ---

# Creiamo l'oggetto principale della barra dei menu.
menubar = Menu(root)

# Colleghiamo la barra dei menu alla finestra principale.
root.config(menu=menubar)

# Creiamo un menu a tendina. 'tearoff=0' rimuove la linea tratteggiata in alto,
# che permette di "staccare" il menu dalla finestra.
file_menu = Menu(menubar, tearoff=0)

# Aggiungiamo comandi al menu 'File'. Ogni comando ha un'etichetta e una funzione da eseguire.
# In questo caso, 'root.quit' chiude l'applicazione.
file_menu.add_command(label='New', command=root.quit)
file_menu.add_command(label='Open', command=root.quit)

# Creiamo un sottomenu.
file_altro_submenu = Menu(file_menu, tearoff=0)

# Aggiungiamo delle voci al sottomenu.
file_altro_submenu.add_cascade(label='ciao')
file_altro_submenu.add_cascade(label='buongiorno')

# Colleghiamo il sottomenu al menu 'File' principale.
# Questo crea una voce di menu che, quando cliccata, mostra il sottomenu.
file_menu.add_cascade(label='Altro', menu=file_altro_submenu)

# Aggiungiamo un separatore orizzontale per organizzare visivamente il menu.
file_menu.add_separator()

# Aggiungiamo un altro comando che chiude l'applicazione.
file_menu.add_command(label='Exit', command=root.quit)

# Aggiungiamo il menu 'File' alla barra dei menu principale.
menubar.add_cascade(label='File', menu=file_menu)

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)