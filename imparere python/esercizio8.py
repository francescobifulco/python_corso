"""Esercizio 8: Manipolazione delle Stringhe
Obiettivo: Esercitarsi nelle operazioni comuni sulle stringhe.

Chiedi all'utente di inserire una frase.
Conta il numero di parole nella frase.
Converti la frase in maiuscolo.
Sostituisci una parola specifica nella frase con un'altra parola (es. sostituisci "ciao" con "salve").
Stampa la frase modificata."""

frase = input("inserire una frase: ")

lisa_frase = frase.split()

tot_parole = len(lisa_frase)
print(tot_parole)

print(frase.upper())

if "ciao" in frase:
    print(frase.replace("ciao","salve"))
else: print("non ce modo di modifficare")