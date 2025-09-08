# inporto le liberie di tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import mysql.connector

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

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='miodatabase'
)

cursore = db.cursor()
cursore.execute('SELECT * from prodotti')
risultato = cursore.fetchall()

colonne = (
    'id',
    'email',
    'username',
    'password',
           )
tabella = ttk.Treeview(
    root,
    columns=colonne,
    show='headings'
)
tabella.heading('id',text='ID')
tabella.heading('email',text='EMAIL')
tabella.heading('username',text='USERNAME')
tabella.heading('password',text='PASSWORD')

for riga in risultato:
    tabella.insert('',END, values=riga)

tabella.grid(row=0, column=0, sticky='nsew')

def inserisci():
    inserisci_Sql = 'INSERT INTO prodotti(nome_prodotto) VALUES (%s)'
    inserisci_valori = ('pc da game',)
    
    cursore.execute(inserisci_Sql,inserisci_valori)
    db.commit()
def modifica():
    modifica_sql = 'UPDATE prodotto SET nome_prodotto = "tavolo"'
    cursore.execute(modifica_sql)
    db.commit()
    
def elimina():
    elimina_sql = 'DELETE FROM prodotti WHERE nome_prodotto = "pc da game"'
    cursore.execute(elimina_sql)
    db.commit()
    
inserisci_btn = Button(root, text='inserisci', command=inserisci)
modifica_btn = Button(root, text='modifica', command=modifica)
elimina_btn = Button(root, text='elimina', command=elimina)


inserisci_btn.grid(row=1, column=0)
modifica_btn.grid(row=2, column=0)
elimina_btn.grid(row=3, column=0)

root.mainloop() #mi fa mantenere la finestra aperta 