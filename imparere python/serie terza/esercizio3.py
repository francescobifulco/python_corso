#Chiedi all'utente due numeri come stringhe. Convertili in interi e calcola la loro somma. Stampa il risultato.

num1 = input("inseriri un numero: ")
num2 = input("inseriri un numero: ")

num1_ = int(num1)
num2_ = int(num2)

somma = num1_+num2_
print(f"la somma e: {somma}")

#Crea una variabile intera e una variabile stringa. Tenta di concatenarle direttamente (ti darà un errore). Converti l'intero in una stringa e poi concatenale. Stampa il risultato.
num_int = '5'
num_str = '6'
somma = num_int+num_str
print(somma)