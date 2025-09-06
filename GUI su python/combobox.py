# inporto le liberie di tkinter
from tkinter import *
from tkinter import ttk
from calendar import month_name 

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

mese_selezionato = StringVar()
comobobox = ttk.Combobox(
    root,
    textvariable=mese_selezionato
)
comobobox['values'] = [month_name[m] for m in range(1,13)]
comobobox['state'] = 'readonly'

comobobox.pack()

def evento_mese(event):
    print(mese_selezionato.get())

comobobox.bind('<<ComboboxSelected>>',
               evento_mese
               ) # creazione eventi

root.mainloop() #mi fa mantenere la finestra aperta 