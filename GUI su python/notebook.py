# inporto le liberie di tkinter
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

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

notebook = ttk.Notebook(root)
notebook.pack(
    pady=10,
    fill=BOTH,
    expand=True
)

frame1 = ttk.Frame(
    notebook,
    width=400,
    height=280
    )
frame2 = ttk.Frame(
    notebook,
    width=400,
    height=280
    )
frame3 = ttk.Frame(
    notebook,
    width=400,
    height=280
    )

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)

notebook.add(frame1, text='tab1')
notebook.add(frame2, text='tab2')
notebook.add(frame3, text='tab3')

label1 = Label(frame1, text='ciao').pack()
label2 = Label(frame2, text='buongiorno').pack()
label3 = Label(frame3, text='arrivederci').pack()

root.mainloop() #mi fa mantenere la finestra aperta 