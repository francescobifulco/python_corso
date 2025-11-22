# Importa la libreria che permette di copiare testo negli appunti
import pyperclip

 # Dizionario che contiene le password dei vari siti
psw = {# Password associata alle chiavi dei sito
    'facebook': 'Cenareinsieme2025?', 
    'instagram': 'mondopiuBello2000?',
    'youtube': 'Chefenehaifatto3035()'
}

# Stampa un messaggio che chiede all’utente quale password vuole
print('Quale password ti interessa?')

# Ciclo che scorre tutte le chiavi del dizionario (i siti)
for sito in psw:
    # Stampa ogni sito disponibile in elenco
    print(' -', sito)
    
try:
    # Legge dal terminale il nome del sito scelto dall’utente
    scelto = input()
    # Recupera la password corrispondente alla chiave inserita
    password = psw[scelto]
    # Copia la password negli appunti del sistema           
    pyperclip.copy(password)
    # Conferma che la password è stata copiata          
    print('Password trovata. Sei pronto ad incollarla.')  
    
    # Pausa per evitare la chiusura immediata del programma
    input()                           
# Viene eseguito se la
# chiave non è presente nel dizionario 
except KeyError: 
                         
    # Messaggio di errore se il sito digitato non è valido
    print('Il sito non esiste.')      

input()