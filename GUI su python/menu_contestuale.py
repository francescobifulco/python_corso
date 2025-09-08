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

# --- Creazione e Posizionamento del Frame ---

# Creiamo un Frame (un contenitore invisibile) che useremo come area su cui fare click destro.
frame = Frame(
    root,
    background='red'
)

# Posizioniamo il Frame usando .pack().
# 'expand=True' lo fa espandere per occupare lo spazio extra nella finestra.
# 'fill=BOTH' lo fa espandere sia in orizzontale che in verticale.
frame.pack(expand=True, fill=BOTH)

# --- Creazione del Menu Contestuale ---

# Creiamo l'oggetto del menu.
# 'tearoff=0' è essenziale per un menu contestuale, impedendo che venga "staccato" dalla finestra.
ctx_menu = Menu(root, tearoff=0)

# Aggiungiamo le voci al menu con `add_command()`.
ctx_menu.add_command(label='Taglia')
ctx_menu.add_command(label='Copia')
ctx_menu.add_command(label='Incolla')

# Aggiungiamo un separatore per migliorare l'organizzazione visiva.
ctx_menu.add_separator()
ctx_menu.add_command(label='Prova')

# --- Funzione per il Popup del Menu ---

def ctx_menu_popup(event):
    try:
        # Mostra il menu contestuale nella posizione del mouse.
        # 'event.x_root' e 'event.y_root' sono le coordinate assolute del cursore sullo schermo.
        ctx_menu.tk_popup(event.x_root, event.y_root)
    finally:
        # Rilascia la "cattura" del menu. Questo è importante per garantire che il menu si chiuda
        # quando l'utente fa clic altrove.
        ctx_menu.grab_release()

# --- Associazione dell'Evento ---

# Associamo l'evento di click destro (<Button-3>) sul 'frame' alla funzione 'ctx_menu_popup'.
# Quando l'utente fa clic destro (il bottone 3 del mouse) sull'area del frame,
# la funzione 'ctx_menu_popup' viene chiamata.
frame.bind('<Button-3>', ctx_menu_popup)

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)