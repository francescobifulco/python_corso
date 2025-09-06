# inporto le liberie di tkinter
from tkinter import *
from tkinter import ttk

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

colonne = (
    'nome',
    'cognome',
    'email'
)
tabella = ttk.Treeview(
    root,
    columns=colonne,
    show='headings'
)

tabella.heading('nome', text='Nome')
tabella.heading('cognome', text='Cognome')
tabella.heading('email', text='Email')

righe = []
for n in range(1,50):
    righe.append((f'nome {n}', 
                  f'cognome {n}',
                  f'email {n}'
                  ))

for riga in righe:
    tabella.insert('', END, values=riga)

tabella.grid(
    row=0,
    column=0,
    sticky='nsew'
)

scrollbar = ttk.Scrollbar(
    root,
    orient=VERTICAL,
    command=tabella.yview
)
scrollbar.grid(
    row=0,
    column=1,
    sticky='ns'
)
tabella.configure(yscrollcommand=scrollbar.set)

root.mainloop() #mi fa mantenere la finestra aperta 