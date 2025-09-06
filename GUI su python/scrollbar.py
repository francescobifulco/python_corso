# inporto le liberie di tkinter
from tkinter import *
from tkinter import ttk
from calendar import month_name 
from tkinter import scrolledtext
from tkinter.messagebox import showinfo

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

'''linguaggi = (
    'Javascript',
    'Java',
    'C',
    'C++',
    'Python',
    'PHP',
    'Ruby',
    'Go',
    'Javascript',
    'Java',
    'C',
    'C++',
    'Python',
    'PHP',
    'Ruby',
    'Go',
    'Javascript',
    'Java',
    'C',
    'C++',
    'Python',
    'PHP',
    'Ruby',
    'Go',
    'Javascript',
    'Java',
    'C',
    'C++',
    'Python',
    'PHP',
    'Ruby',
    'Go'
    )

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

linguaggio_selezionato = StringVar(value=linguaggi)
listbox = Listbox(
    root,
    listvariable=linguaggio_selezionato,
    height=6,
    selectmode='extended'
)
listbox.grid(
    column=0,
    row=0,
    sticky='nwes'
)

scrollbar = ttk.Scrollbar(
    root,
    orient='vertical',
    command=listbox.yview
)
scrollbar.grid(
    row=0,
    column=1,
    sticky='ns'
    )

listbox['yscrollcommand'] = scrollbar.set
'''

scrolledtxt = scrolledtext.ScrolledText(
    root,
    width=50,
    height=10
)
scrolledtxt.pack(
    fill=BOTH, 
    side=LEFT, 
    expand=True
    )

root.mainloop() #mi fa mantenere la finestra aperta 