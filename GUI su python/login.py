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

def login():
    print(email_entry.get())
    print(password_entry.get())
    
label_email = Label(
    root,
    text="Email"
)
label_email.pack(
    padx=5,
    pady=5
)

email = StringVar()
email_entry = ttk.Entry(
    root,
    textvariable=email
)
email_entry.pack()
email_entry.focus()

password = StringVar()
password_entry = ttk.Entry(
    root,
    textvariable=password,
    show='*'
)

label_password = Label(
    root,
    text="Password"
)
label_password.pack(
    padx=5,
    pady=5
)
password_entry.pack()

button = ttk.Button(
    root,
    text='Login',
    command=login
)

button.pack()

root.mainloop() #mi fa mantenere la finestra aperta 