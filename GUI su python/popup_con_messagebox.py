# Importiamo le librerie necessarie: tkinter per l'interfaccia, ttk per i widget moderni
from tkinter import *
from tkinter import ttk
from tkinter import messagebox # Messagebox per le finestre di dialogo a messaggio.

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

# --- Funzioni per le Finestre di Dialogo ---

def show_message_info():
    messagebox.showinfo(
        #Mostra una finestra di dialogo di tipo 'informazione'. Ha un'icona 'i' e un bottone 'OK'.
        #Non restituisce un valore, serve solo per informare l'utente.
        title='info', 
        message='questo e un messaggio di informazione')
    
def show_message_warning():
    #Mostra una finestra di dialogo di tipo 'avviso'. Ha un'icona di allerta e un bottone 'OK'.
    #Utile per avvisare di situazioni non critiche ma importanti.
    messagebox.showwarning(
        title='Attenzione', 
        message='server in manutenzione')
    
def show_message_error():
    #Mostra una finestra di dialogo di tipo 'errore'. Ha un'icona di errore e un bottone 'OK'.
    #Usata per notificare all'utente che si è verificato un errore critico.
    messagebox.showerror(
        title='ERRORE', 
        message='questo e un errore')
    
def show_message_askyesno():
    #Mostra una finestra di dialogo di tipo 'sì/no'. Ha un'icona a punto interrogativo.
    #Restituisce True se l'utente clicca 'Sì' e False se clicca 'No'.
    risposta = messagebox.askyesno(
        title='prova', 
        message='ti piace la piazza con l ananas?')
    
    # Se l'utente ha risposto 'Sì', il programma si chiude.
    if risposta:
        root.destroy()
        
def show_message_askokcancel():
    #Mostra una finestra di dialogo di tipo 'OK/Annulla'. Ha un'icona a punto interrogativo.
    #Restituisce True se l'utente clicca 'OK' e False se clicca 'Annulla'.
    risposta = messagebox.askokcancel(
        title='prova', 
        message='ti piace la piazza con l ananas?')
    
    # Se l'utente ha risposto 'OK', il programma si chiude.
    if risposta:
        root.destroy()
        
def show_message_askretrycancel():
    #Mostra una finestra di dialogo di tipo 'Riprova/Annulla'. Ha un'icona a punto interrogativo.
    #Restituisce True se l'utente clicca 'Riprova' e False se clicca 'Annulla'.
    risposta = messagebox.askretrycancel(
        title='prova', 
        message='ti piace la piazza con l ananas?')
    
    # Se l'utente ha risposto 'Riprova', il programma si chiude.
    if risposta:
        root.destroy()
        
# --- Creazione dei Bottoni ---

# Ogni bottone è associato a una delle funzioni per le finestre di dialogo.
button1 = ttk.Button(
    root,
    text='mostra messaggio',
    command=show_message_info
).pack(fill=BOTH, padx=10, pady=10)

button2 = ttk.Button(
    root,
    text='mostra messaggio',
    command=show_message_warning
).pack(fill=BOTH, padx=10, pady=10)

button3 = ttk.Button(
    root,
    text='mostra messaggio',
    command=show_message_error
).pack(fill=BOTH, padx=10, pady=10)

button4 = ttk.Button(
    root,
    text='mostra messaggio',
    command=show_message_askyesno
).pack(fill=BOTH, padx=10, pady=10)

button5 = ttk.Button(
    root,
    text='mostra messaggio',
    command=show_message_askokcancel
).pack(fill=BOTH, padx=10, pady=10)

button6 = ttk.Button(
    root,
    text='mostra messaggio',
    command=show_message_askretrycancel
).pack(fill=BOTH, padx=10, pady=10)

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)