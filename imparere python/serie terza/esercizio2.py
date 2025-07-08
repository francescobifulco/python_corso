#Crea due variabili numeriche, num1 e num2. Calcola la loro somma, differenza, prodotto e quoziente intero. Stampa tutti i risultati.
num1 = int(input("inserisci il numero: "))
num2 = int(input("inserisci il numero: "))

somma = num1+num2
differenza = num1-num2
prodotto = num1*num2
quoziente_intero = num1//num2
print(f"la somma e {somma}, la differenza e {differenza}, il prodotto e {prodotto}, il quoziente per intero e {quoziente_intero}")

#Calcola l'area di un cerchio. Chiedi all'utente il raggio. Stampa il risultato arrotondato a due cifre decimali.
PI_GRECO = 3.14

raggio = float(input("inserisci il raggio: "))

area = raggio*PI_GRECO*raggio
print(f"area del cerchio e: {area}")