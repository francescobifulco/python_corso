# Importiamo le librerie necessarie da tkinter
from tkinter import *
from tkinter import ttk

root = Tk() # Creiamo la finestra principale dell'applicazione (la radice del nostro programma)

root.title('il nostro programma') # Definiamo il titolo della finestra
root.geometry('600x400+500+500') # Impostiamo la dimensione e la posizione iniziale della finestra (larghezza x altezza + posizione x + posizione y)
#root.iconbitmap("internet.ico") # Imposto la mia icona
#root.resizable(False,True) # Disabilita o abilita la ridimensionabilità della finestra in larghezza e/o altezza

root.minsize(400,100) # Imposta la dimensione minima della finestra che l'utente può raggiungere
root.maxsize(1000,1000) # Imposta la dimensione massima della finestra che l'utente può raggiungere

#root.attributes('-alpha',0.5) # Imposta il livello di trasparenza della finestra (da 0.0 a 1.0)

#root.attributes('-topmost',1) # Fa sì che la finestra rimanga sempre sopra le altre
root.lift() # Sposta la finestra in primo piano, portandola sopra le altre finestre
#root.lower() # Sposta la finestra in secondo piano, dietro le altre finestre

# Definiamo una funzione che verrà eseguita quando il bottone viene cliccato
def saluta():
    print('ho cliccato il bottone')

#photo = PhotoImage(file='pixil-frame-0 (9).png')
# Creiamo un bottone con varie opzioni di personalizzazione
button = Button(
                text='ciao',  # Il testo visualizzato sul bottone
                background='red',  # Colore dello sfondo del bottone
                foreground='blue',  # Colore del testo del bottone
                width=20,  # Larghezza del bottone (in caratteri)
                borderwidth=3,  # Spessore del bordo del bottone
                command=saluta,  # Collega la funzione 'saluta' all'evento di click
                # image=photo,  # Aggiunge un'immagine al bottone (richiede una PhotoImage)
                # command=lambda: root.quit(),  # Utilizza una funzione lambda per chiudere l'applicazione
                compound='bottom'  # Posiziona l'immagine rispetto al testo
                )
#button['state'] = 'disabled' # Rende il bottone disabilitato, impedendone il click
button.pack(ipadx=50, ipady=50) # Posiziona il bottone nella finestra e aggiunge un riempimento interno

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)
