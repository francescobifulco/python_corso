"""Esercizio 9: Gestione degli Errori (try/except)
Obiettivo: Gestire potenziali errori in modo elegante.

Chiedi all'utente di inserire due numeri.
Tenta di dividere il primo numero per il secondo.
Usa un blocco try-except per catturare un ZeroDivisionError se il secondo numero è zero e stampa un messaggio di errore appropriato.
Inoltre, gestisci ValueError se l'utente inserisce un input non numerico."""

try:
    numero1 = int(input("inserisci un numero: "))
    numero2 = int(input("inserisci un numero: "))
    dividi = numero1 / numero2
    print(f"la divisione tra {numero1} e {numero2}: {dividi}")
except ZeroDivisionError:
    print("impossibile dividere per 0")
except ValueError:
    print("inseriri un numero")