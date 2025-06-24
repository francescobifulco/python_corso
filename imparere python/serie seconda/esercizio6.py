"""Esercizio 6: Cicli (for, while), range e Iterabili
Obiettivo: Utilizzare i cicli per ripetere operazioni e comprendere il concetto di iterabile.

Ciclo for con range: Stampa tutti i numeri da 1 a 10 (inclusi).
Ciclo for su una lista: Data la lista frutti = ["mela", "banana", "ciliegia", "dattero"], stampa ogni frutto.
Ciclo while: Chiedi all'utente di indovinare un numero segreto (es. 5). Continua a chiedere finché l'utente non indovina. Dopo ogni tentativo, dai un suggerimento ("Troppo alto" o "Troppo basso"). Quando indovina, stampa "Congratulazioni!".
Combinare for e if: Stampa solo i numeri pari da 0 a 20 (inclusi) usando un ciclo for e una condizione if.
Iterare su una stringa: Data la stringa parola = "programmazione", stampa ogni lettera della parola."""

for numeri in range(1,11):
    print(f"i numeri: {numeri}")

print()
frutti = ["mela", "banana", "ciliegia", "dattero"]
for lista in frutti:
    print(f"la lista di frutti: {lista}")

print()
numero_indovina = 10
count = 0
while count <= 5:
    numero = int(input("indovina il numero: "))
    if numero > numero_indovina:
        print(f"il numero {numero} e troppo grande")
    elif numero < numero_indovina:
        print(f"il numero {numero} e troppo piccolo")
    elif numero == numero_indovina:
        print(f"hai indovinato congratulazione")
        break
    count += 1

for pari in range(0,21):
    if pari % 2 == 0:
        print(f"il numero e pari: {pari}")

print()
parola = "programmazione"
lista_parola = list(parola)
for lista in lista_parola:
    print(f"la lettera e: {lista}")