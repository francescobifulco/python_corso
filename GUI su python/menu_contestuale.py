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

frame = Frame(
    root,
    background='red'
)
frame.pack(expand=True, fill=BOTH)

ctx_menu = Menu(root, tearoff=0)
ctx_menu.add_command(label='Taglia')
ctx_menu.add_command(label='Copia')
ctx_menu.add_command(label='Incolla')
ctx_menu.add_separator()
ctx_menu.add_command(label='Prova')

def ctx_menu_popup(event):
    try:
        ctx_menu.tk_popup(event.x_root, event.y_root)
    finally:
        ctx_menu.grab_release()

frame.bind('<Button-3>', ctx_menu_popup)

root.mainloop() #mi fa mantenere la finestra aperta 