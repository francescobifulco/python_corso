#Chiedi all'utente il suo nome e la sua età. Stampa un messaggio di benvenuto che includa il nome e l'età dell'utente, ad esempio: "Benvenuto [Nome], hai [Età] anni!".
nome = str(input("inserisci il nome: "))
eta = int(input("inserisci eta: "))
print(f"Benvenuto {nome}, hai {eta} anni!")

#Stampa la data e l'ora attuali utilizzando un modulo appropriato
from datetime import datetime
ora_corrente = datetime.now()
print("Ora corrente:", ora_corrente)