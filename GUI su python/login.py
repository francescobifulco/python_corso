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

# --- Funzione di Login ---

def login():
    print(email_entry.get()) # Otteniamo e stampiamo il testo del campo Email.
    print(password_entry.get()) # Otteniamo e stampiamo il testo del campo Password.
    
# --- Creazione dei Widget ---

# Creiamo una Label (etichetta) per il campo Email.
label_email = Label(
    root,
    text="Email"
)
# Posizioniamo la Label nella finestra con un po' di spaziatura esterna.
label_email.pack(
   padx=5,  # Spazio orizzontale
   pady=5   # Spazio verticale
)

# Creiamo una variabile di controllo per l'input dell'email.
# Questo ci permette di accedere facilmente al contenuto del campo.
email = StringVar()

# Creiamo il widget Entry (campo di testo) per l'email, associandolo alla variabile 'email'.
email_entry = ttk.Entry(
    root,
    textvariable=email
)

# Posizioniamo il campo Entry nella finestra.
email_entry.pack()

# Impostiamo il focus del cursore sul campo email, in modo che l'utente possa iniziare a digitare subito.
email_entry.focus()

# Creiamo una variabile di controllo per l'input della password.
password = StringVar()

# Creiamo il widget Entry per la password.
password_entry = ttk.Entry(
    root,
    textvariable=password,
    show='*' # Il parametro 'show' sostituisce i caratteri digitati con un asterisco per nasconderli.
)

# Creiamo una Label per il campo Password.
label_password = Label(
    root,
    text="Password"
)

# Posizioniamo la Label per la password con un po' di spaziatura.
label_password.pack(
    padx=5,
    pady=5
)

# Posizioniamo la Label per la password con un po' di spaziatura.
password_entry.pack()

# Posizioniamo il campo Entry per la password.
button = ttk.Button(
    root,
    text='Login',
    command=login  # Colleghiamo il bottone alla funzione 'login' che verrà eseguita al click.
)

# Posizioniamo il bottone nella finestra.
button.pack()

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)