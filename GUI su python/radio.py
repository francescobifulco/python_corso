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

genere = StringVar()
r1 = Radiobutton(text='maschio',
                 value='m',
                 variable=genere)
r2 = Radiobutton(text='femmina',
                 value='f',
                 variable=genere)
button = Button(text='prova',
                command=lambda:print(genere.get())
                )

r1.pack()
r2.pack()
button.pack()


taglia_selezionata = StringVar()
taglie = (
    ('Smail','S'),
    ('Medium','M'),
    ('Large','L'),
    ('Extra Large','XL')
)

for taglia in taglie:
    r = ttk.Radiobutton(root,
                        text=taglia[0],
                        value=taglia[1],
                        variable=taglia_selezionata)
    r.pack(padx=5,
           pady=5)

button = Button(text='prova',
                command=lambda:print(taglia_selezionata.get())
                )
button.pack()

root.mainloop() #mi fa mantenere la finestra aperta 