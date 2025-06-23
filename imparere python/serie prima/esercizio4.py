"""Esercizio 4: Cicli (for e while)
Obiettivo: Usare i cicli per ripetere azioni.

Ciclo For: Stampa tutti i numeri pari da 0 a 20 (inclusi).
Ciclo While: Chiedi all'utente di inserire numeri ripetutamente finché non digita 'q' per uscire. Somma tutti i numeri inseriti prima di uscire."""

for i in range(0,21):
    if i % 2 == 0:
        print(i)

lista = []
somma_tot = 0
while True:
    numero = input("inserisci un numero 'q' per uscire: ")
    if numero == "q":
        break
    numero_ = int(numero)
    somma_tot += numero_
print(f"la somma e: {somma_tot}")
    