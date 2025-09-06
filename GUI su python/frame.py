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


frame0 = LabelFrame(
    root,
    #background='red',
    text='sono label frame',
    padx=10,
    pady=50,
    height=100,
    width=200
)
frame0.pack(
    #fill=X,
    #expand=True
    )

frame1 = Frame(
    root,
    background='red',
    padx=10,
    pady=50,
    height=100,
    width=200
)
frame1.pack(
    #fill=X,
    #expand=True
    )

frame2 = Frame(
    root,
    background='yellow',
    padx=10,
    pady=50,
    height=100,
    width=200
)
frame2.pack(
    #fill=X,
    #expand=True
    )

frame3 = Frame(
    root,
    background='green',
    padx=10,
    pady=50,
    height=100,
    width=200
)
frame3.pack(
    #fill=X,
    #expand=True
    )


button1 = Button(
    frame1,
    text='ciao'
)
button1.pack()

button2 = Button(
    frame2,
    text='ciao'
)
button2.pack()

button3 = Button(
    frame3,
    text='ciao'
)
button3.pack()

root.mainloop() #mi fa mantenere la finestra aperta 