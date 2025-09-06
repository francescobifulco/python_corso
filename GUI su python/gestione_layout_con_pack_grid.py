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

'''label1 = Label(
    root,
    text='Label 1',
    background='green',
    foreground='white'
)
label1.pack(
    ipadx=10,
    ipady=10,
    fill=X
    )

label2 = Label(
    root,
    text='Label 2',
    background='red',
    foreground='white'
)
label2.pack(
    ipadx=10,
    ipady=10,
    fill=X
    )

label3 = Label(
    root,
    text='Label 3',
    background='blue',
    foreground='white'
)
label3.pack(
    ipadx=10,
    ipady=10,
    fill=X
    )

label4 = Label(
    root,
    text='Label 4',
    background='purple',
    foreground='white'
)
label4.pack(
    ipadx=10,
    ipady=10,
    fill=X,
    expand=True,
    side=LEFT
    )

label5 = Label(
    root,
    text='Label 5',
    background='yellow',
    foreground='white'
)
label5.pack(
    ipadx=10,
    ipady=10,
    fill=X,
    expand=True,
    side=LEFT
    )

label6 = Label(
    root,
    text='Label 6',
    background='orange',
    foreground='white'
)
label6.pack(
    ipadx=10,
    ipady=10,
    fill=X,
    expand=True,
    side=LEFT
    )
    '''
    
root.columnconfigure(
    0,
    weight=1
    )

root.columnconfigure(
    1,
    weight=1
    )

frame1 = Frame(
    root,
    background='red',
    height=200,
    width=200
)
frame2 = Frame(
    root,
    background='yellow',
    height=200,
    width=200
)
frame3 = Frame(
    root,
    background='blue',
    height=200,
    width=200
)
frame4 = Frame(
    root,
    background='orange',
    height=200,
    width=200
)

frame1.grid(
    column=0,
    row=0,
    #rowspan=2,
    columnspan=2
)
frame2.grid(
    column=1,
    row=0
)
frame3.grid(
    column=0,
    row=1
    
)
frame4.grid(
    column=1,
    row=1
)

root.mainloop() #mi fa mantenere la finestra aperta 