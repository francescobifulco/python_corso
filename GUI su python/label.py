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

#photo = PhotoImage(file='pixil-frame-0 (9).png')

label = Label(text='Ciao \n sono francesco.', 
              background='#33e4e2', 
              padx=50, 
              pady=50, 
              foreground='white', 
              font=('Helevetica', 
              30),
              cursor='circle',
              justify='right',
              #image=photo
              compound='bottom'
              )
label.pack() #manda a schermo la scritta del label

root.mainloop() #mi fa mantenere la finestra aperta 