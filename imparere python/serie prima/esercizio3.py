"""Esercizio 3: Istruzioni Condizionali (if/elif/else)
Obiettivo: Usare la logica condizionale per prendere decisioni.

Chiedi all'utente di inserire un numero.
Verifica se il numero è positivo, negativo o zero.
Stampa un messaggio appropriato."""

numero = int(input("inserire un numero: "))

if numero > 0:
    print("positivo")
elif numero == 0:
    print("il numero e 0")
else: 
    print("negativo")
