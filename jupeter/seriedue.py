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

#Scrivi un blocco try-except che gestisca una 
#ZeroDivisionError.
try:
    num = 8
    num1 = 0
    divi = num / num1
    print(f'la divisione e {divi}')
except ZeroDivisionError:
    print('inpossibile fare la divisione per 0')
    
#Crea una funzione che richieda un input numerico e 
# gestisca una ValueError se l'input non è un numero.
def inserire_un_numero():
    try:
     numero = int(input('inserire un numero: '))
     print(f'il numero inserito e: {numero}')
    except ValueError:
        print('non e un numero')

#inserire_un_numero()

#Utilizza un blocco finally per stampare un messaggio 
#indipendentemente dal fatto che si verifichi 
#un'eccezione.
try:
    saluta = input('saluta: ').strip()
    if not saluta:
        raise ValueError("Il saluto non può essere vuoto")
    print(f'il tuo saluto: {saluta}')
except ValueError as e:
    print(f'Errore: {e}')
finally:
    print('sono nel blocco finally')
    