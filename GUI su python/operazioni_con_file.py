# Importiamo le librerie necessarie: tkinter per l'interfaccia, ttk per i widget moderni
from tkinter import *
from tkinter import ttk
from tkinter import filedialog # filedialog per le finestre di dialogo dei file.

# Creiamo la finestra principale dell'applicazione (la radice del nostro programma)
root = Tk() 

# Definiamo il titolo della finestra
root.title('il nostro programma') 

# Impostiamo la dimensione e la posizione iniziale della finestra (larghezza x altezza + posizione x + posizione y)
root.geometry('600x400+500+500') 

# Disabilita o abilita la ridimensionabilità della finestra in larghezza e/o altezza
# root.resizable(False, True) 

# Imposta la dimensione minima della finestra che l'utente può raggiungere
root.minsize(400, 100) 

# Imposta la dimensione massima della finestra che l'utente può raggiungere
root.maxsize(1000, 1000) 

#root.iconbitmap("internet.ico") # Imposto la mia icona

# Imposta il livello di trasparenza della finestra (da 0.0 a 1.0)
# root.attributes('-alpha', 0.5) 

# Fa sì che la finestra rimanga sempre sopra le altre
# root.attributes('-topmost', 1) 

# Sposta la finestra in primo piano, portandola sopra le altre finestre
root.lift() 

# Sposta la finestra in secondo piano, dietro le altre finestre
# root.lower()

# --- Funzioni per la Gestione dei File ---

def apri_file():
    # Definiamo i tipi di file che possono essere mostrati nella finestra di dialogo.
    # Ogni tupla contiene il nome della descrizione e il pattern del file.
    filetypes = (
        ('file di testo', '*.txt'),
        ('tutti i file', '*.*')
    )
    
    # Apriamo la finestra di dialogo 'Apri file'.
    # I parametri 'title', 'initialdir' e 'filetypes' personalizzano la finestra.
    filename = filedialog.askopenfilename(title='Apri un file', 
                                          initialdir='/', # Directory iniziale (in questo caso la radice del file system)
                                          filetypes=filetypes)
   
    # Se l'utente ha selezionato un file (filename non è vuoto)
    if filename:
        try:
            # Apriamo il file in modalità di lettura ('r').
            f = open(filename, 'r')
            # Leggiamo tutto il contenuto del file.
            data = f.read()
            # Stampiamo il contenuto nella console.
            print(data)
            # Chiudiamo il file.
            f.close()
        except FileNotFoundError:
            print("Il file non è stato trovato.")
        except Exception as e:
            print(f"Si è verificato un errore: {e}")
    
def apri_file1():
    # Apriamo la finestra di dialogo 'Salva come'.
    # 'mode='w'' imposta la modalità di scrittura.
    # 'defaultextension='.txt'' aggiunge '.txt' se non specificato.
    f = filedialog.asksaveasfile(
        mode='w', 
        title='salva file', 
        defaultextension='.txt'
        )
    
    # Se l'utente non ha annullato la finestra di dialogo (f non è None)
    if f:
        # Scriviamo del testo nel file.
        data = 'prima riga del file'
        f.write(data)
        # Chiudiamo il file per salvare i cambiamenti.
        f.close()
        print(f"File salvato con successo: {f.name}")
    
# Creiamo il primo bottone che, quando cliccato, chiama la funzione apri_file()
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

root.mainloop() # Avvia il "loop" principale di Tkinter.
# Questo mantiene la finestra aperta e in ascolto degli eventi (click, ridimensionamento, ecc.)