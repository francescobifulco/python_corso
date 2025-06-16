# Stampa a video la stringa
print("ciao")
print("Hello World!")

# Dichiaro una variabile messaggio da input
# messaggio = input("Inserisci qualcosa:")
# Stampo il messaggio che l'utente ha inserito
# print(messaggio)

# Struttura dell'if
if 1 < 5:
    print("messaggio")

# Assegno alla variabile x il valore 5
x = 5
print(x)

# Assegno valori a più variabili contemporaneamente
x, y, z = 32, 100, 987
print(x)
print(y)
print(z)

# Una lista
citta = ["Roma", "Milano", "Napoli"]
a, b, c = citta
print(a)
print(b)
print(c)

# Somma
x = 32
y = 8
z = x + y
print(z)

x = 5
# type ci restituisce il tipo di dato della variabile
print(type(x))

# Float
x = 5.5
print(type(x))

# Stringa
x = "ciao"
print(type(x))

# Boolean
x = False
print(type(x))

# Concatena due stringhe
x = "Ciao sono "
y = "Luca"
print(x + y)

# str fa il casting in stringa
w = "Ciao sono "
r = str(5)
print(w + r)

# int fa il casting in intero
w = 5
r = int("5")
print(w + r)

# float fa il casting in float
w = 5.5
r = float(5)
print(w + r)

## Stringhe

x = "ciao"
y = "ciao"

print("hello")
print(x)

# Le """ """ ci permettono di scrivere una stringa su più righe
x = """ciao
sono una poesia"""
print(x)

# Prende il carattere alla posizione 0 della stringa
print(x[0])

# len ci dice la lunghezza della stringa
print(len(x))

# Stampa i caratteri della stringa x dalla posizione 0 alla 2 (3 escluso)
print(x[:3])
# Stampa i caratteri della stringa x dalla posizione 3 alla 16 (17 escluso)
print(x[3:17])
# Stampa il carattere alla posizione -4 della stringa (contando da destra)
print(x[-4])

# upper trasforma la stringa in maiuscolo
print(x.upper())

# lower trasforma la stringa in minuscolo
print(x.lower())

# strip elimina gli spazi all'inizio e alla fine della stringa
print(x.strip())

# replace sostituisce un carattere con un altro
print(x.replace("o", "w"))

# split divide la stringa in una lista di sottostringhe
print(x.split())

# format ci permette di concatenare stringhe e numeri
x = 23
prova = "Ciao sono Luca e sono nato il {}"
print(prova.format(x))

prova = "Ciao sono Luca e sono nato il {}, peso {}, altezza {}"
print(prova.format(15, 65, 1.70))

# Nel format possiamo anche utilizzare degli indici
prova = "Ciao sono Luca e sono nato il {2}, peso {0}, altezza {1}"
print(prova.format(15, 65, 1.70))

# \ ci permette di aggiungere le virgolette all'interno di una stringa
prova = "Ciao sono Luca e sono \"figo\""
print(prova)

## Boolean

x = True
y = False

# Verifica se 5 è minore di 10 (True)
print(5 < 10)

# Verifica se 11 è minore di 10 (False)
print(11 < 10)

# Struttura condizionale if-else
if 5 < 10:
    print("sono minore di 10")
else:
    print("sono maggiore di 10")

# bool(1) restituisce True
print(bool(1))

# bool(0) restituisce False
print(bool(0))

pane = 0

# Verifica se la variabile 'pane' è True (non zero)
if pane:
    print("non serve andare al supermercato")
else:
    print("uscire a prendere il pane")

listaCoseDaComprare = []

# Verifica se la lista 'listaCoseDaComprare' è non vuota
if listaCoseDaComprare:
    print("andare al supermercato")
else:
    print("non serve andare al supermercato")

listaCoseDaComprare = ["limone", "pane", "carote"]

# Verifica se la lista 'listaCoseDaComprare' è non vuota
if listaCoseDaComprare:
    print("andare al supermercato")
else:
    print("non serve andare al supermercato")

## Operazioni aritmetiche

x = 5
y = 9

# Somma +
print(x + y)

# Sottrazione -
print(x - y)

# Moltiplicazione *
print(x * y)

# Divisione /
print(x / y)

# Resto della divisione %
print(x % y)

# Potenza **
print(x ** y)

# Arrotonda per difetto della divisione //
print(x // y)

# Assegna il valore a destra dell'operatore alla variabile situata a sinistra =
numero = 10

print(x + y * 2)
print((x + y) * 2)

# Operatore assegnamento
x = 5
x += 2
y = 7
print(x)

# min ci dà il minimo
x = min(5, 10, 25)
print(x)

# max ci dà il massimo
x = max(5, 10, 25)
print(x)

# abs ci dà il valore assoluto
x = abs(-5)
print(x)

# pow ci calcola la potenza
x = pow(4, 2)
print(x)


## if

x = 5 

# Verifica se x è minore di 10
if x < 10:
    print("5 è minore di 10")
print("non sono nell'if")

c = 10

# Verifica se c è uguale a 10
if c == 10:
    print("condizione verificata")
 
v = 11

# Verifica se v è diverso da 10
if v != 10:
    print("condizione verificata") 

b = 9

# Verifica se b è minore o uguale a 10
if b <= 10:
    print("condizione verificata")  

n = 19

# Verifica se n è maggiore o uguale a 10
if n >= 10:
    print("condizione verificata")

n = 9

# Verifica se n è maggiore o uguale a 10, altrimenti esegue l'else
if n >= 10:
    print("condizione verificata")
else:
    print("condizione non verificata")

n = 10

# Verifica con elif (else if) se n è uguale a 10
if n < 10:
    print("condizione verificata")
elif n == 10:
    print("uguale a 10")
else:
    print("condizione non verificata")
    
x = 11
y = 5

# Verifica se x è compreso tra 10 e 20
if 10 <= x <= 20:
    print("compreso tra 10 e 20")
    
# Verifica se x è maggiore di 10 e y è maggiore di 10
if x > 10 and y > 10:
    print("condizione verificata")
else:
    print("condizione non verificata")

# Verifica se x è maggiore di 10 o y è maggiore di 10
if x > 10 or y > 10:
    print("condizione verificata")
else:
    print("condizione non verificata")

# Verifica la negazione di (x < 10)
if not (x < 10):
    print("condizione verificata")
else:
    print("condizione non verificata")

# Condizione in una sola riga
if x > 10: print("è maggiore di 10")

# Operatore ternario per stampa condizionale
print("è maggiore di 10") if x > 10 else print("è minore di 10")

# Verifica se x è pari e minore di 10, altrimenti è dispari if anidati 
if x % 2 == 0:
    if x < 10:
        print("numero pari e minore di 10")
else:
    print("numero dispari")