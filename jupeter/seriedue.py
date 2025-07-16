#Crea un file di testo chiamato mio_file.txt e scrivi al suo 
#interno "Ciao, questo è un test."

with open("mio_file.txt", "w") as file:
    file.write("Ciao, questo è un test.")

#Leggi il contenuto di mio_file.txt e stampalo sulla 
#console.
with open("mio_file.txt", "r") as file:
    contenuto = file.read()
print(contenuto)

#Aggiungi una nuova riga al file senza sovrascrivere il 
#contenuto esistente.
with open("mio_file.txt", "a") as file:
    file.write("\nquesta e la seconda riga")
    
"""
 Le modalità più comuni sono:

"r": Lettura (predefinita).
"w": Scrittura (sovrascrive il file se esiste).
"a": Aggiunta (scrive alla fine del file senza sovrascrivere).
"x": Creazione (fallisce se il file esiste già).
"""

#Gestisci l'eccezione nel caso in cui il file non esista 
#durante la lettura.
try:
    with open('file_non_esistente.txt', 'r') as file:
        contenuto = file.read()
        print(contenuto)
except FileNotFoundError:
    print("Il file non esiste")

