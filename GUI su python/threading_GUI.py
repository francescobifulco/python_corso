# inporto le liberie di tkinter
import time
from tkinter import *
from tkinter import ttk
import threading

root = Tk() #mi crea la finestra ma chiude subito

root.title('il nostro programma') #definiama il titolo della finesta
root.geometry('600x400+500+500') #le dimensioni della finestra
#root.iconbitmap("./internet.ico") #imposto la mia icona
#root.resizable(False,True)

root.minsize(400,100) #dimensione minima della finestra 
root.maxsize(1000,1000) #dimensione massima della finestra

#root.attributes('-alpha',0.5) #trasparenza della finesta

#root.attributes('-topmost',1) #va sempre sopra
root.lift() #va aventi 
#root.lower() #va indietro

def dormi():
    time.sleep(5)
    print('stavo dormendo...')
def mangia():
    print('stavo mangiando...')

button1 = Button(
    root,
    text='dormi',
    command=lambda: threading.Thread(target=dormi).start()
)
button1.pack(expand=True, fill=X)

button2 = Button(
    root,
    text='mangia',
    command=mangia
)
button2.pack(expand=True, fill=X)

root.mainloop() #mi fa mantenere la finestra aperta 
