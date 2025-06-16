"""Verifica se due parole sono 
anagrammi."""

"""parola1 = input("inserisci una parola: \n")
parola2 = input("inserisci una parola: \n")
lista_parola2 = list(parola2)
for i in range(len(lista_parola2)):
    inversa = lista_parola2[::-1]
legibile = "".join(inversa)  

if sorted(parola1) == sorted(legibile):
    print("le parole sono anagrammi")
else: print("le parole non sono anagrammi")

Chiedi una frase e 
sostituisci tutte le vocali 
con *.

vocali = "aeiou"
lista_vocali = list(vocali)
frase = input("inserisci una frase: \n")
lista_frase = list(frase)
for i in range(len(lista_frase)):
    if lista_frase[i] in lista_vocali:
        lista_frase[i] = "*"
frase_com = "".join(lista_frase)
print(frase_com)

Scrivi un programma che 
rimuove tutti gli spazi da una 
stringa.

frase = input("inserisci una frase: \n")
spazzi = frase.replace(" ", "")
print(spazzi)

Chiedi una frase e stampa 
ogni parola su una riga 
diversa.

frase = input("inserisci una frase: \n")
lista = frase.split()
print(lista)
print("\n".join(lista))

Scrivi un programma che conta 
il numero di parole in una 
frase.

frase = str(input("inserisci una frase: \n"))
lista = frase.split()
print(lista)
print(len(lista))


Chiedi all’utente una 
parola e stampa il numero di 
vocali presenti.

conteggio = 0
parola = str(input("inserisci una parola: \n"))
lista = list(parola)
print(lista)
vocali = "aeiou"
lista1 = list(vocali)
for el in lista:
    if el in lista1:
        conteggio += 1
print(conteggio) 

Chiedi due numeri all’utente 
e stampa la loro somma, 
differenza, prodotto e 
divisione.

num1 = int(input("inserisci un numero: \n"))
num2 = int(input("inserisci un numero: \n"))
print(num1+num2)
print(num1*num2)
print(num1/num2)
print(num1-num2)

Scrivi un programma che 
chiede all’utente il suo nome e 
lo stampa in maiuscolo.

nome = input("inserisci il tuo nome: \n")
print(nome.upper())

Scrivi un programma che somma 
due matrici 3x3.

# Definizione delle due matrici 3x3
matrice1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrice2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Matrice somma vuota
somma_matrice = []

# Ciclo per sommare elemento per elemento
for i in range(3):
    riga = []
    for j in range(3):
        riga.append(matrice1[i][j] + matrice2[i][j])
    somma_matrice.append(riga)

# Stampa del risultato
for riga in somma_matrice:
    print(riga)
    
Stampa tutti gli elementi di 
una matrice riga per riga, 
usando un ciclo for.

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for riga in matrice:
    print(riga)

Scrivi un programma che 
stampa la diagonale principale 
di una matrice quadrata."""
"""Scrivi un programma che 
stampa la diagonale secondaria 
di una matrice 3x3.

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matrice)):
    diagonale_principale = [matrice[i][i]]
    print(diagonale_principale)  # Output: [1, 5, 9]

n = len(matrice)
diagonale_secondaria = [matrice[i][n - 1 - i] for i in range(n)]
print(diagonale_secondaria)  # Output: [3, 5, 7] controlla

Chiedi all’utente di inserire 
i valori per una matrice 2x2 e 
stampala.

matrice = []

for i in range(2):  # due righe
    riga = []
    for j in range(2):  # due colonne
        valore = input(f"Inserisci il valore per la posizione [{i}][{j}]: ")
        riga.append(valore)
    matrice.append(riga)

# Stampa della matrice
for riga in matrice:
    print(riga)
    
Crea una matrice 3x3 
contenente solo zeri e stampala 
in formato leggibile.

matrice = [[0,0,0],[0,0,0],[0,0,0]]
for riga in matrice:
    print(riga)"""
    
#Conta le consonanti
"""Scrivi un programma che chiede una parola all’utente e 
stampa quante consonanti contiene."""

"""frase = str(input("inserisci una frase: "))
consonanti = "bcdfghlmnpqrstvz"
conteggio = 0
vocali ="aeiou"
conteggio1 = 0
for i in frase:
    if i in consonanti:
        conteggio = frase.count(i)
    if i in vocali:
        conteggio1 = frase.count(i)

print(f"numero di consonanti sono: {conteggio}")
print(f"numero di vocali sono: {conteggio1}")"""

#Inverti una stringa
"""Scrivi un programma che prende una frase e stampa la 
stessa frase al contrario (carattere per carattere)."""

"""frase = str(input("inserisci una frase: "))
inversa = frase[::-1]
print(inversa)"""

#Conta le parole più lunghe di 4 caratteri
"""Chiedi all’utente di inserire una frase e conta quante parole hanno più di 4 lettere."""

"""frase = str(input("inserisci una frase: "))
lista_lun = frase.split()
print(lista_lun)
conteggio = 0
for i in range(len(lista_lun)):
    if len(lista_lun[i]) > 4: 
        print("parola e lunga")
        conteggio += 1
    else: print("parola corta")

print(conteggio)"""

#Rimuovi i caratteri duplicati
"""Scrivi un programma che rimuove i caratteri duplicati consecutivi da una stringa 
inserita dall’utente.
Esempio: "aabbccdde" → "abcde"."""

# Rimuove i caratteri duplicati consecutivi da una stringa inserita dall’utente

"""frase = input("Inserisci una frase: ")
risultato = ""

for i in range(len(frase)):
    if i == 0 or frase[i] != frase[i - 1]:
        risultato += frase[i]

print(risultato)"""

#Controlla se una stringa è palindroma
"""Chiedi all’utente una parola e verifica se è palindroma 
(cioè si legge uguale da sinistra a destra e da destra 
a sinistra)"""

"""parola = input("inserisci una parola: ")

if parola == parola[::-1]:
    print("la parola e palindroma")
else: print("non e palindroma")"""

#Sostituisci tutte le consonanti con #
"""Scrivi un programma che sostituisce tutte le consonanti di 
una frase con il simbolo #."""

"""consonanti = "bcdfghlmnpqrstvz"
lista_consonanti = list(consonanti)
frase = input("inserisci una frase: ")
lista_frase = list(frase)
for i in range(len(lista_frase)):
    if lista_frase[i] in lista_consonanti:
        lista_frase[i] = "#"
frase_com = "".join(lista_frase)
print(frase_com)"""

#Estrai le parole che iniziano con una vocale
"""Chiedi una frase e stampa solo le parole che inizano con una 
vocale."""

"""frase = input("Inserisci una frase: ")
consonanti = ("b", "c", "d", "f", "g", "h", "l", "m", "n", "p", "q", "r", "s", "t", "v", "z")
vocali = ("a", "e", "i", "o", "u")

parole = frase.split()

for parola in parole:
    if parola.lower().startswith(vocali):
        print(f"La parola '{parola}' inizia con una vocale.")
    elif parola.lower().startswith(consonanti):
        print(f"La parola '{parola}' inizia con una consonante.")

# Crea una nuova lista solo con le parole che NON iniziano con una consonante
parole_senza_consonanti = [p for p in parole if not p.lower().startswith(consonanti)]
print(parole_senza_consonanti)"""

#Conta quante volte compare una lettera
"""Chiedi all’utente una frase e una lettera, e stampa quante 
volte quella lettera compare nella frase."""

"""frase = input("inserisci una frase: ")
lista_frase = list(frase)
conteggio = 0

for lettera in set(lista_frase):
    if lettera in lista_frase:
        conteggio = lista_frase.count(lettera)
        print(f"La lettera '{lettera}' compare volte: {conteggio}")"""

#Elimina tutte le vocali da una frase
"""Scrivi un programma che rimuove tutte le vocali da una frase 
inserita dall’utente."""

"""frase = input ("inserisci una frase: ")
vocali ="aeiou"
frase_senza_vocali = ""
for carattere in frase:
    if carattere.lower() not in vocali:
        frase_senza_vocali += carattere
print(frase_senza_vocali)"""

"""Chiedi un numero all’utente e stampa se è pari o dispari."""

"""num = int(input("inserisci un numero: "))
if num % 2 == 0: print("pari")
else: print("dispari")"""

"""Scrivi un programma che stampa i numeri da 1 a 100, ma per i 
multipli di 3 stampa "Fizz", per i multipli di 5 "Buzz", e per 
entrambi "FizzBuzz"."""

"""for i in range(1,101):
    divisione = 3
    divisione1 = 5
    if i % divisione == 0 and i % divisione1 == 0: print(f"{i} fizzbuzz")
    elif i % divisione == 0: print(f"{i} fizz")
    elif i % divisione1 == 0: print(f"{i} buzz")"""


"""Chiedi un numero all’utente e stampa tutti i suoi divisori."""

"""numero = int(input("inserisci un numero: "))

for divisi in range(1,numero+1):
    if numero % divisi == 0: print(f"il {numero} e divisibile per {divisi}")"""

"""Scrivi un programma che verifica se una parola è palindroma."""

"""parola = input("inserisci una parola: ")
if parola == parola[::-1]: print("pelindroma")
else: print("non e palindroma")"""

"""Calcola la somma di tutti i numeri dispari da 1 a 100."""

"""somma=0
for i in range(1,101):
    if i % 2 != 0: somma = i + somma
print(somma)"""

"""Chiedi all’utente di inserire 5 numeri e memorizzali in una 
lista. Stampa la lista in ordine crescente."""

"""lista = []

for i in range(5):
    numeri = input("inserisci un numero:")
    lista.append(numeri)
    lista.sort()
print(lista)"""

"""Esercizi sulle Collezioni e gli Indici Esercizio 1: Accesso agli
Elementi di una Lista Data la seguente lista di frutta: 
frutta = ["mela", "banana","ciliegia", "kiwi", "arancia"]
* Accedi e stampa il secondoelemento della lista.
* Accedi e stampa l'ultimo elemento della lista utilizzando
un indice negativo.
* Prova ad accedere a un indice che non esiste nella lista. Cosa
succede? (Non devi gestirel'errore, solo descrivere cosa accade)."""

"""frutta = ["mela", "banana", "ciliegia", "kiwi", "arancia"]
print(frutta[1])
print(frutta[-1])
print(frutta[7])"""

"""Esercizio 2:Manipolazione di Stringhe con Indici 
Data la seguente stringa: saluto = "Ciao Mondo!"
* Stampa il primo carattere della stringa.
* Stampa l'ultimo carattere della stringa.
* Utilizza lo "slicing" per stampare solo la parola "Mondo".
* Utilizza lo "slicing" per stampare la stringa al contrario."""

"""saluto = "Ciao Mondo!"
print(saluto[0])
print(saluto[-1])
print(saluto[5:10])
print(saluto[::-1])"""

"""Esercizio 3: Modifica di Elementi in una Lista Data la seguente lista di numeri:
numeri = [10, 20, 30, 40, 50]
* Modifica il terzo elemento della lista (l'elemento con valore 30) in 35.
* Aggiungi un nuovo elemento (ad esempio, 60) alla fine della 
lista senza usare append() ma assegnandolo direttamente a un 
indice. (Suggerimento: dovrai prima estendere la lista o sapere 
quale sarà la sua dimensione finale).
* Modifica i primi due elementi della lista in 5 e 15."""
 
"""numeri = [10, 20, 30, 40, 50]
numeri.remove(30)
print(numeri)
numeri.insert(2,35)
print(numeri)
numeri.insert(5,60)
print(numeri)
numeri[0] = 5
numeri[1] = 15
print(numeri)"""

"""Esercizio 4: Trovare l'Indice di un Elemento Data la seguente lista di colori:
colori = ["rosso", "verde", "blu", "giallo", "blu"]
Trova e stampa l'indice della prima occorrenza del colore "blu".
Prova a trovare l'indice di un colore che non è presente nella lista 
(es. "viola"). Cosa succede?"""

"""colori = ["rosso", "verde", "blu", "giallo", "blu"]
for i in colori:
    if i == "blu":
        indice = colori.index("blu")
        indice1 = colori.index("viola")
print(indice)
print(indice1)"""

"""Esercizio 5: Inserimento di Elementi in una Posizione Specifica
Data la seguente lista di animali:animali = ["cane", "gatto", 
"leone"] Inserisci "elefante" tra "gatto" e "leone" utilizzando 
l'indice corretto.Inserisci "tigre" all'inizio della lista."""

"""animali = ["cane", "gatto", "leone"]
animali.insert(2,"elefante")
print(animali)"""

"""Esercizio 6: Conteggio di Occorrenze e Indice
Data la seguente stringa di testo: testo = "Python è un 
linguaggio di programmazione molto popolare. Python è versatile. 
Conta quante volte la parola "Python" appare nella stringa (nota: 
la ricerca deve essere case-sensitive, quindi "python" non conta). 
Non usare il metodo count() della stringa. Suggerimento: potresti 
aver bisogno di iterare sulla stringa e usare slicing o trovare 
l'indice delle occorrenze.
Trova l'indice di tutte le occorrenze della lettera 'o' 
(minuscola) nella stringa. Stampa una lista di questi indici." """

"""testo = "Python è un linguaggio di programmazione molto popolare. Python è versatile."
coteggio = 0
lista = testo.split()
for el in lista:
    if el == "Python":
        coteggio += 1
print(f"la parola 'Python' conpare volte: {coteggio}")

indici = []
lista_ = list(testo)
for e in range(len(lista_)):
    if lista_[e] == "o":
        indici.append(e)
print(indici)"""

"""Esercizio 7: Inversione di Liste e Stringhe
Inverti la seguente lista di numeri senza usare il metodo 
reverse() o lo slicing [::-1]. Devi manipolare gli elementi 
usando gli indici.
numeri_da_invertire = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Inverti la seguente stringa, carattere per carattere, senza usare 
lo slicing [::-1].
stringa_da_invertire = "programmazione" """

#Lettura di un file di testo:
"""Crea un file di testo chiamato saluto.txt e scrivi al suo 
interno la riga: "Ciao, mondo!".
Scrivi un programma Python che apra saluto.txt in modalità lettura 
('r'), legga l'intero contenuto e lo stampi a schermo.
Assicurati di chiudere il file dopo averlo letto."""

"""with open("saluto.txt" ,"w") as file:
    file.write("Ciao, mondo!")

with open("saluto.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)"""
    
#Scrittura su un file di testo (Sovrascrittura):
"""Scrivi un programma Python che apra un file chiamato 
mio_file.txt in modalità scrittura ('w').
Scrivi la riga "Questa è la prima riga." e poi "Questa è la 
seconda riga." su righe separate nel file.
Chiudi il file.
Verifica il contenuto di mio_file.txt per assicurarti che le 
righe siano state scritte correttamente."""

"""with open("mio_file.txt" ,"w") as file:
    file.write("Questa è la prima riga\nQuesta è la seconda riga.")

with open("mio_file.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)"""
    
#Aggiunta a un file di testo (Append):
"""Scrivi un programma Python che apra mio_file.txt 
(creato nell'esercizio precedente) in modalità aggiunta ('a').
Aggiungi una nuova riga: "Questa riga è stata aggiunta 
successivamente."
Chiudi il file.
Verifica il contenuto di mio_file.txt per assicurarti che la 
nuova riga sia stata aggiunta senza sovrascrivere quelle 
esistenti."""

"""with open("mio_file.txt" ,"a") as file:
    file.write("Questa riga è stata aggiunta successivamente.\n")

with open("mio_file.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)"""
    
#Lettura riga per riga:
"""Crea un file di testo chiamato lista_frutta.txt con alcuni 
nomi di frutta, uno per riga (es. "mela", "banana", 
"ciliegia").
Scrivi un programma Python che legga il file lista_frutta.txt 
riga per riga e stampi ogni riga, rimuovendo il carattere di 
nuova riga (\n) alla fine."""

"""stringa = "mela \nbanana \nciliegia"
with open("lista_frutta.txt" ,"w") as file:
    file.write(stringa)
    
    

with open("lista_frutta.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)

stringa.replace("\n"," ")"""

#Copia di file:
"""Scrivi un programma Python che legga il contenuto di un 
file sorgente (es. saluto.txt) e lo scriva in un nuovo file 
destinazione (es. copia_saluto.txt).
Gestisci l'errore FileNotFoundError se il file sorgente non 
esiste."""

"""try:
    with open("saluto.txt" ,"w") as file:
        file.write("Ciao, mondo!")
    
    with open("saluto.txt", "r") as file_origi:
        contenuto = file_origi.read()
    with open("copia_saluto.txt", "w") as file_destinazione:
        file_destinazione.write(contenuto)
    with open("copia_saluto.txt", "r") as file:
        contenuto1 = file.read()
    print(contenuto1)
except FileNotFoundError:
    print("file non esiste")"""

#Conteggio parole in un file:
"""Crea un file di testo chiamato testo.txt con un paragrafo 
di testo a tua scelta (puoi usare un testo lungo qualche riga).
Scrivi un programma Python che legga il contenuto di testo.txt.
Conta il numero totale di parole nel file. 
(Suggerimento: potresti aver bisogno di trasformare il testo 
in minuscolo e rimuovere la punteggiatura).
Stampa il conteggio delle parole."""

"""testo = "Buchi Neri: Un Viaggio nel Mistero dello Spazio
I buchi neri sono tra i fenomeni più affascinanti e misteriosi 
dell'universo. Immagina di comprimere una quantità enorme di 
materia in uno spazio estremamente piccolo. Questo è, in 
sostanza, un buco nero. Si tratta di una regione dello spazio 
in cui la gravità è così forte che nulla, nemmeno la luce, 
può sfuggire dalla sua presa. Questo accade quando una stella 
massiccia esaurisce il suo combustibile e collassa sotto il 
suo stesso peso. Una volta formato, il buco nero diventa 
invisibile, ma la sua presenza può essere rilevata grazie agli 
effetti che ha sull'ambiente circostante, influenzando il 
movimento delle stelle vicine o emettendo raggi X quando 
ingloba materia. Studiare i buchi neri ci aiuta a comprendere 
meglio le leggi della fisica e la natura stessa dell'universo."

with open("testo.txt" ,"w") as file:
        file.write(testo)
with open("testo.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)

lista_testo = testo.split()
print(len(lista_testo))"""

#Conteggio righe in un file:
"""Usando lo stesso file testo.txt dell'esercizio precedente, 
scrivi un programma che conti il numero di righe presenti nel 
file.
Stampa il numero di righe."""

"""testo = "Buchi Neri: Un Viaggio nel Mistero dello Spazio
I buchi neri sono tra i fenomeni più affascinanti e misteriosi 
dell'universo. Immagina di comprimere una quantità enorme di 
materia in uno spazio estremamente piccolo. Questo è, in 
sostanza, un buco nero. Si tratta di una regione dello spazio 
in cui la gravità è così forte che nulla, nemmeno la luce, 
può sfuggire dalla sua presa. Questo accade quando una stella 
massiccia esaurisce il suo combustibile e collassa sotto il 
suo stesso peso. Una volta formato, il buco nero diventa 
invisibile, ma la sua presenza può essere rilevata grazie agli 
effetti che ha sull'ambiente circostante, influenzando il 
movimento delle stelle vicine o emettendo raggi X quando 
ingloba materia. Studiare i buchi neri ci aiuta a comprendere 
meglio le leggi della fisica e la natura stessa dell'universo."

with open("testo.txt" ,"w") as file:
        file.write(testo)
with open("testo.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)

lista_testo = testo.split()
print(len(lista_testo))

righe = contenuto.split("\n")
print(f"numero di righe: {len(righe)}")"""

#Scrittura di una lista su un file:
"""Hai una lista di nomi: nomi = 
["Alice", "Bob", "Charlie", "David"].
Scrivi un programma che salvi ogni nome di questa lista su una 
riga separata in un file chiamato nomi.txt."""

"""nomi = ["Alice", "Bob", "Charlie", "David"]

with open("nomi.txt" ,"w") as file:
    for nome in nomi:
        file.write(nome + "\n")
with open("nomi.txt", "r") as file:
    contenuto = file.read()
    print(contenuto)"""

#