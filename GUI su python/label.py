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

# --- Creazione e Configurazione del Widget Label ---

# La riga seguente serve per caricare un'immagine da un file. È commentata e non usata,
# ma è un esempio di come si prepara un'immagine per un widget.
#photo = PhotoImage(file='pixil-frame-0 (9).png')

# Creiamo un widget Label, un elemento grafico che mostra del testo o un'immagine.
label = Label(
              text='Ciao \n sono francesco.', # Il testo da visualizzare. '\n' crea una nuova riga.
              background='#33e4e2', # Colore di sfondo usando un codice esadecimale.
              padx=50, # Spaziatura interna orizzontale (padding) in pixel.
              pady=50, # Spaziatura interna verticale (padding) in pixel.
              foreground='white', # Colore del testo.
              font=('Helvetica', 30), # Tipo e dimensione del font.
              cursor='circle', # Cambia l'aspetto del cursore quando si passa sopra il label.
              justify='right', # Allinea il testo all'interno del label a destra (se il testo ha più righe).
              #image=photo, # Associa un'immagine al label (la variabile 'photo' deve essere definita).
              compound='bottom' # Se si usa un'immagine, la posiziona sotto il testo.
              )

# Posizioniamo il label nella finestra. Il metodo .pack() lo impacchetta e lo rende visibile.
# Di default, .pack() posiziona il widget al centro e lo estende per occupare lo spazio necessario.
label.pack()

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)