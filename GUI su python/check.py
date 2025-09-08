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

# --- Gestione del Checkbutton ---

# Definiamo una funzione che verrà chiamata ogni volta che lo stato del Checkbutton cambia
def premo_check():
    # Creiamo una nuova etichetta (Label) e impostiamo il suo testo
    # prendendo il valore corrente dalla variabile 'nome' associata al Checkbutton
    label = Label(text=nome.get())
     # Posizioniamo la nuova etichetta nella finestra
    label.pack()
    
# Creiamo una variabile speciale di Tkinter (StringVar) per memorizzare il valore del Checkbutton.
# Questo è necessario perché il Checkbutton deve collegarsi a una variabile per sapere il suo stato.
nome = StringVar()

# Creiamo un widget Checkbutton (una casella di spunta)
check = Checkbutton(
                    text='ciao',  # Il testo visualizzato accanto alla casella di spunta
                    font=('helvetica', 30),  # Imposta il font e la dimensione del testo
                    command=premo_check,  # Specifica la funzione da chiamare quando il Checkbutton viene cliccato
                    variable=nome,  # Collega questo Checkbutton alla variabile 'nome' (StringVar)
                    onvalue='luca',  # Il valore che la variabile 'nome' assumerà quando il Checkbutton è selezionato
                    offvalue='marco'  # Il valore che la variabile 'nome' assumerà quando il Checkbutton NON è selezionato
                    )
# Posizioniamo il Checkbutton nella finestra usando il gestore di geometria pack()
# pack() è uno dei modi per disporre i widget nella finestra (altri sono grid() e place())
check.pack()

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)