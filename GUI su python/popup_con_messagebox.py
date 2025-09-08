# inporto le liberie di tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk() #mi crea la finestra ma chiude subito

root.title('il nostro programma') #definiama il titolo della finesta
root.geometry('600x400+500+500') #le dimensioni della finestra
#root.iconbitmap("internet.ico") #imposto la mia icona
#root.resizable(False,True)

root.minsize(400,100) #dimensione minima della finestra 
root.maxsize(1000,1000) #dimensione massima della finestra

#root.attributes('-alpha',0.5) #trasparenza della finesta

#root.attributes('-topmost',1) #va sempre sopra
root.lift() #va aventi 
#root.lower() #va indietro

def show_message_info():
    messagebox.showinfo(title='info', message='questo e un messaggio di informazione')
def show_message_warning():
    messagebox.showwarning(title='Attenzione', message='server in manutenzione')
def show_message_error():
    messagebox.showerror(title='ERRORE', message='questo e un errore')
def show_message_askyesno():
    risposta = messagebox.askyesno(title='prova', message='ti piace la piazza con l ananas?')

    if risposta:
        root.destroy()
        
def show_message_askokcancel():
    risposta = messagebox.askokcancel(title='prova', message='ti piace la piazza con l ananas?')

    if risposta:
        root.destroy()
        
def show_message_askretrycancel():
    risposta = messagebox.askretrycancel(title='prova', message='ti piace la piazza con l ananas?')

    if risposta:
        root.destroy()
        
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

root.mainloop() #mi fa mantenere la finestra aperta 