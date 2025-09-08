# inporto le liberie di tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

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

def apri_file():
    filetypes = (
        ('file di testo', '*.txt'),
        ('tutti i file', '*.*')
    )
    
    filename = filedialog.askopenfilename(title='Apri un file', 
                                          initialdir='/', 
                                          filetypes=filetypes)
    f = open(filename, 'r')
    data = f.read()
    print(data)
    
def apri_file1():
    f = filedialog.asksaveasfile(mode='w', title='salva file', defaultextension='.txt')
    data = 'prima riga del file'
    f.write(data)
    f.close()
    
bottone = ttk.Button(
    root,
    text='apri file',
    command=apri_file
).pack(expand=True)

bottone1 = ttk.Button(
    root,
    text='apri file',
    command=apri_file1
).pack(expand=True)

root.mainloop() #mi fa mantenere la finestra aperta 