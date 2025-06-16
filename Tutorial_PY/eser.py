#Chiedi all'utente il suo nome.
"""nome = input("Inserisci il tuo nome: ")
print("il tuo nome e: ",nome)"""

#Stampa un messaggio di saluto personalizzato, ad esempio: "Ciao, [NomeUtente]! Benvenuto in Python."

"""nome = input("Inserisci il tuo nome: ")
print(f"Ciao, {nome}! Benvenuto in Python.")"""

#Chiedi all'utente due numeri interi.

"""num1 = input("Inserisci un numero: ")
num2 = input("Inserisci un numero: ")
print(f" Il primo numero e: {num1}, il secondo e: {num2}")"""

#Stampa la somma dei due numeri.

"""num1 = input("Inserisci un numero: ")
num2 = input("Inserisci un numero: ")

num1_ = int(num1)
num2_ = int(num2)

print(f"Il primo numero e: {num1_}, il secondo e: {num2_} la somma e : {num1_+num2_}")"""

#Chiedi all'utente la base e l'altezza di un rettangolo.

"""base = input("La base del rentongolo: ")
altezza = input("altezza del rentongolo: ")

base_ = float(base)
altezza_ = float(altezza)
print(f"La base e: {base_}, l'altezza e: {altezza_}")"""

# Calcola e stampa l'area del rettangolo.

"""base = input("La base del rentongolo: ")
altezza = input("altezza del rentongolo: ")

base_ = float(base)
altezza_ = float(altezza)

area = base_ * altezza_

print(f"La base e: {base_}, l'altezza e: {altezza_} area e: {area}")"""

#Assegna due valori a due variabili diverse (es. a = 5, b = 10). Scambia i valori delle due variabili senza usare una terza variabile ausiliaria.
#Stampa i nuovi valori di a e b.

"""a = 5
b = 10

a = a + b
b = a - b
a = a - b

print(f"Il primo numero e: {a}, il secondo e: {b}")"""

#Chiedi all'utente un numero intero. Stampa se il numero è pari o dispari.

"""num1 = input("Inserisci un numero: ")
num2 = input("Inserisci un numero: ")

num1_ = int(num1)
num2_ = int(num2) 

if num1_ % 2 == 0: print("pari")
else: print("dispari")

if num2_ % 2 == 0: print("pari")
else: print("dispari")"""

#Chiedi all'utente la sua età. Se l'età è maggiore o uguale a 18, stampa "Sei maggiorenne.". Altrimenti, stampa "Sei minorenne.".

"""eta = input("Inserisci eta: ")
eta_ = int(eta)

if eta_ > 18: print("maggiorenne")
else: print("minorenne")"""

#Chiedi all'utente di inserire un voto da 0 a 10. Stampa un giudizio in base al voto:
"""0-4: "Gravemente insufficiente"
5: "Insufficiente"
6: "Sufficiente"
7: "Buono"
8: "Distinto"
9-10: "Ottimo"""

"""voto = input("Inserisci un voto da 0 a 10: ")
voto_ = int(voto)

if voto_ >= 0 and voto_ <= 4: print("Gravemente insufficiente")
elif voto_ == 5: print("Insufficiente")
elif voto_ == 6: print("Sufficiente")
elif voto_ == 7: print("Buono")
elif voto_ == 8: print("Distinto")
elif voto_ >= 9 and voto_ <= 10: print("Ottimo")"""

#Chiedi all'utente due numeri. Stampa quale dei due è il maggiore, oppure se sono uguali.

"""num1 = input("Inserisci un numero: ")
num2 = input("Inserisci un numero: ")

num1_ = int(num1)
num2_ = int(num2) 

max_ = max(num1_,num2_)
print(f"Il massimo e: {max_}")"""

#Chiedi all’utente di inserire due numeri e stampa la loro somma.

"""num1 = input("Inserisci un numero: ")
num2 = input("Inserisci un numero: ")

num1_ = int(num1)
num2_ = int(num2)

print(f"La somme e: {num1_+num2_}")"""

#Trova il massimo tra tre numeri

"""num1 = input("Inserisci un numero: ")
num2 = input("Inserisci un numero: ")
num3 = input("Inserisci un numero: ")

num1_ = int(num1)
num2_ = int(num2)
num3_ = int(num3) 

max_ = max(num1_,num2_,num3_)
print(f"Il massimo e: {max_}")"""

#Stampa la tabellina di un numero da 1 a 10.

"""num = input("Inserisci un numero da 1 a 10: ")
num_ = int(num)

count = 0
while count <= 10:
    risul = num_ * count
    print(f"{num_} * {count} = {risul}")
    count += 1"""

#Calcola il fattoriale di un numero intero positivo.

"""n = int(input("Inserisci un numero intero positivo: "))
fattoriale = 1

for i in range(1, n + 1):
    fattoriale *= i

print("Il fattoriale è:", fattoriale)"""

#Dichiarare una variabile "nome" e assegnargli il tuo nome. Mandare a schermo.

"""nome = "francesco"
print(nome)

#Dichiarare una variabile "eta" e assegnargli la tua età. Mandare a schermo.

eta = 24
print(eta)

#Dichiarare una variabile "pi" e assegnargli il valore di pi greco (3,14159). Mandare a schermo.

pi = 3,14159
print(pi)

#Creare una variabile "lunghezza" e assegnargli un valore, quindi riassegnare la variabile a 15. Mandare a schermo.

lunghezza = 7
lunghezza = 6
print(lunghezza)

#Creare una variabile "nome_completo" e assegnargli una stringa contenente il tuo nome e cognome. Mandare a schermo.

nome_completo = "francesco bifulco"
print(nome_completo)

#Creare una variabile "eta_futura" e assegnargli il valore dell'età che avrai tra 10 anni (utilizzando la variabile età già esistente). Mandare a schermo.

eta_futura = eta + 10
print(eta_futura)

#Creare delle variabili "nome", "cognome" ed "anno_di_nascita" ed assegnarle il valore dei valori. Mandare a schermo in un unico print. Sovrascrivere tutte le variabili e rimandare a schermo una seconda volta.

nome = "francesco"
cognome = "bifulco"
anno_nascita = "03/03/2001"
print(f"{nome} {cognome} {anno_nascita}")

nome = "francisco"
cognome = "bifo"
anno_nascita = "03/03/2002"
print(f"{nome} {cognome} {anno_nascita}")

#Creare una variabile `eta_attuale` e assegnargli il valore dell'età che hai attualmente, calcolandola in base all'anno corrente. Mandare a schermo `eta_attuale`

eta_attuale = 2025 - 2001
print(eta_attuale)"""

#Definire una costante per il valore di pi greco e usarla per calcolare la circonferenza di un cerchio di raggio 5.

"""PI_GRECO = 3.14159
raggio = 5
circonferenza = 2 * PI_GRECO * raggio

print("La circonferenza del cerchio è:", circonferenza)

#Definire una costante per il valore della gravità terrestre e usarla per calcolare il peso di un oggetto di massa 10 kg.

GRAVITA = 9.81
oggetto = 10
peso = GRAVITA*oggetto

print(peso)

#Definire una costante per il tasso di cambio euro-dollaro e usarla per convertire 100 euro in dollari.

TASSO = 1.14
euro = 100
dorallo = euro*TASSO
print(dorallo)

#Definire una costante per la velocità della luce e usarla per calcolare quanto tempo impiega la luce a percorrere 1.000.000 km.

VELOCITA =  299792458
percorso = 1000000*1000
tempo = VELOCITA / percorso
print(tempo)

#Definire una costante per il numero di giorni in una settimana e usarla per calcolare quante settimane ci sono in 365 giorni.

SETTIMANA = 7
anno = 365
calcolo = SETTIMANA / anno
print(calcolo)

#Definire una costante per il numero di minuti in un'ora e usarla per calcolare quante ore ci sono in 720 minuti.

MINITI_ORA = 60 
ore = 720 
calcolo = MINITI_ORA / ore
print(calcolo)

#Definire una costante per il numero di giorni in un anno non bisestile e usarla per calcolare quanti giorni ci sono in 5 anni non 
#bisestili.

GIORNI_ANNO = 365
anni = 5
calcolo = anni*GIORNI_ANNO
print(calcolo)

#Definire una costante per il valore di Planck e usarla per calcolare l'energia di un fotone con una frequenza di 5e14 Hz.

PLANCK = 6.62607015e-34
fotone = 5e14
energia = PLANCK * fotone
print(energia)

#Definire una costante per il numero di secondi in un'ora e usarla per convertire 5 ore in secondi.

SECONTI_ORA = 3600
ore = 5 
calcolo = SECONTI_ORA * ore
print(calcolo)

#Definire una costante per il numero di centimetri in un metro e usarla per convertire 250 centimetri in metri.

CENTIMETRI = 100
converti = 250 
metri = converti / CENTIMETRI
print(metri)"""

#Dichiarare una variabile "numero_intero" e assegnargli un valore **intero**. Mandare a schermo il tipo della variabile per conferma.

"""nume = int(7)
print(type(nume))

#Dichiarare una variabile "numero_decimale" e assegnargli un valore **float**. Mandare a schermo il tipo della variabile per conferma.

nume = float(4.4)
print(type(nume))

#Creare una variabile "testo" e assegnargli una **stringa** contenente una frase. Mandare a schermo il tipo della variabile per conferma.

nume = "ciao"
print(type(nume))

#Creare una variabile "valore_booleano" e assegnargli un valore **booleano**. Mandare a schermo il tipo della variabile per conferma.

nume = True
print(type(nume))

#Creare una lista "numeri" contenente 5 numeri interi. Mandare a schermo il tipo della variabile per conferma.

lista = [1,2,3,4,5]
print(type(lista))

#Creare una lista "misti" contenente un numero intero, un numero float, una stringa e un valore booleano. Mandare a schermo il tipo 
# della variabile per conferma.

lista = [1,"e",True,3.4]
print(type(lista))"""

#Creare una lista vuota e assegnarla a una variabile.

"""lista = []
print(lista)

#Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile.

nume = [1,2,3,4,5]
print(nume)

#Accedere all'elemento con indice 2 della lista precedente.

indice = nume[2]
print(indice)

#Aggiungere un nuovo elemento "6" alla lista precedente.

nume.append(6)
print(nume)

#Rimuovere l'elemento con indice 3 dalla lista precedente.

del nume[3]
print(nume)

#Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.

primi = nume[:3]
print(primi)

#Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.

dispari = nume[1::2]
print(dispari)

#Ordinare la lista precedente in ordine decrescente.

nume.sort(reverse=True)
print(nume)

#Contare quante volte l'elemento "2" appare nella lista precedente.

indice = nume.count(2)
print(indice)"""

#Scrivi un programma che permetta all'utente di gestire una semplice lista della spesa.
"""Inizia con una lista vuota: lista_spesa = [].
Chiedi all'utente di aggiungere 3 articoli alla lista, uno alla volta, usando un ciclo. Ogni volta che aggiunge un articolo, 
stampa l'intera lista_spesa aggiornata.
Dopo aver aggiunto tutti gli articoli, chiedi all'utente se vuole rimuovere un articolo specifico. Se l'articolo è nella lista, 
rimuovilo e stampa la lista aggiornata. Se non è nella lista, stampa un messaggio di errore.
Infine, stampa un messaggio che indica quanti articoli sono rimasti nella lista della spesa."""

"""spesa = []
num_arti = int(input("quanti articoli vuoi aggiungere: "))

for lista in range(num_arti):
    elemento = input(f"Inserisci un articolo {lista + 1}: ")
    spesa.append(elemento)
print(f"La mia lista della spesa e: {spesa}")

remuv_spesa = str(input("vuoi rimuovere un articolo nella spesa (s/n): "))
for riv in spesa:
    arti = input("Quale articolo vuoi rimuovere: ")
    if arti in spesa:
        spesa.remove(arti)
        print("Articolo rimosso.")
    else: 
        print("articolo non ci sta")
        print(f"lista della spesa aggiurnata: {spesa}")
    if remuv_spesa == "n":
        print("hai deciso di non rimuovere viente")
    break
if len(spesa) == 0: print("la lista e vuota")"""

#Analisi di Voti Scolastici

"""Hai una lista di voti di uno studente: voti = [7, 8, 5, 9, 6, 7, 10, 8].
Calcola e stampa il voto medio (la somma di tutti i voti divisa per il numero di voti).
Trova e stampa il voto più alto ottenuto.
Trova e stampa il voto più basso ottenuto.
Conta e stampa quante volte è stato preso il voto 7."""

"""voti = [7, 8, 5, 9, 6, 7, 10, 8]
print(voti)

somma = sum(voti)
media = somma / len(voti)
print(f"La somma dei voti e: {somma} invece la media dei voti e: {media}")

massimo = max(voti)
minimo = min(voti)
print(f"Il voto piu grande e: {massimo} il voti piu baso e: {minimo}")

conteggio = voti.count(7)
print(f"Il voto 7 e stato preso {conteggio} volte.")"""

#Gestione Inventario Semplice
"""Immagina di avere un piccolo inventario di prodotti.

Crea una lista di prodotti: inventario = ["monitor", "tastiera", "mouse", "webcam", "microfono"].
Chiedi all'utente di inserire il nome di un prodotto che vuole cercare nell'inventario.
Se il prodotto è presente, stampa un messaggio come: "Il prodotto 'X' è disponibile nel nostro inventario!".
Se il prodotto non è presente, stampa un messaggio come: "Il prodotto 'Y' non è disponibile. Vuoi aggiungerlo all'inventario? (sì/no)".
Se l'utente risponde "sì", aggiungi il prodotto alla lista inventario e stampa la lista aggiornata.
Se l'utente risponde "no" (o qualsiasi altra cosa), non fare nulla e ringrazialo."""

"""prodotti = ["ciao","monitor", "tastiera", "mouse", "webcam", "microfono"]
print(prodotti)

for i in range(len(prodotti)):
    cercare = input("inserisci il nome di un prodotto da cercare: ")
    print(f"Il prodotto da cercare e: {cercare}")
    prodotti_trovare = cercare in prodotti
    if prodotti_trovare == True:print(f"Il prodotto ci sta ")
    else: 
        print("Il prodotto non ci sta")
        aggiungi = str(input("vuoi aggiungere (s/n): "))
        if aggiungi == "s": 
            prodotti.append(cercare)
            print(f"Il prodotto {cercare} e stato aggiunto")
            print(f"La tua lista e: {prodotti}")
        else: 
            print("Nessun prodotto aggiunto.")
            break"""

#Trova l'Elemento Massimo/Minimo:
"""Crea una lista di numeri interi (es. numeri = [5, 12, 3, 9, 15, 1]).
Trova e stampa il numero più grande e il più piccolo nella lista. Non usare le funzioni max() o min() incorporate!"""

"""numeri = [5, 12, 3, 9, 15, 1]
numeri[0]
minimo = numeri[0]
massimo =numeri[0]

for n in numeri:
    if n > massimo:
        massimo = n
    if n < minimo:
        minimo = n

print(f"Il massimo è: {massimo}")
print(f"Il minimo è: {minimo}")"""

#Lista di Nomi:
"""Chiedi all'utente 5 nomi.
Memorizza questi nomi in una lista.
Stampa tutti i nomi della lista, uno per riga."""

"""nomi =[]
for i in range(5):
    aggiungi_nomi = str(input("aggiungi 5 nomi: "))
    nomi.append(aggiungi_nomi)
print(f"I nomi sono {nomi}")"""

#Somma degli Elementi di una Lista
"""Crea una lista di numeri interi (es. numeri = [10, 20, 30, 40]).
Calcola e stampa la somma di tutti gli elementi della lista. Non usare la funzione sum() incorporata!"""

"""numeri = [10, 20, 30, 40]
somma = 0
for n in numeri:
    somma += n
print(f"La somma degli elementi è: {somma}")"""

#Conta Occorrenze
"""Crea una lista di elementi (es. frutti = ["mela", "banana", "mela", "arancia", "mela"]).
Chiedi all'utente un elemento da cercare.
Conta e stampa quante volte quell'elemento appare nella lista."""

"""frutti = ["mela", "banana", "mela", "arancia", "mela"]
print(f"La lista e: {frutti}")

cercare = str(input("inserisci un elemento da cercare: "))
print(f"Il elementa da cercare: {cercare}")

elementi_cerca = cercare in frutti
if elementi_cerca == True: print("elemento da cercare ci sta")
else: print("elemento da cercare non ci sta")

conteggio = frutti.count(cercare)
print(f"elemento da cercare si ripete in: {conteggio}")"""

#Rimuovi Duplicati
"""Crea una lista con elementi duplicati (es. colori = ["rosso", "blu", "verde", "rosso", "giallo", "blu"]).
Crea una nuova lista che contenga solo gli elementi unici della lista originale, senza duplicati.
Stampa la nuova lista."""

"""colori = ["rosso", "blu", "verde", "rosso", "giallo", "blu"]
print("Lista originale:", colori)

colori_unici = []
for colore in colori:
    if colore not in colori_unici:
        colori_unici.append(colore)
print("Lista senza duplicati:", colori_unici)"""

#Stampa numeri pari: Scrivi un programma che stampi tutti i numeri pari da 1 a 20 usando un ciclo 

"""for i in range(20):
    if i % 2 == 0: print(i)"""

#Somma di numeri: Scrivi un programma che chieda all'utente di inserire 5 numeri interi e ne calcoli la somma usando un ciclo

"""som = 0
count = 0
while count < 5:
    numeri = int(input("inserisci 5 numeri:"))
    som = som + numeri
    count +=1
print(f"La somma e: {som}")"""

#Conto alla rovescia: Scrivi un programma che stampi un conto alla rovescia da 10 a 0, e poi stampi "Buon Anno!" alla fine.

"""count = 10
while count >= 0:
    print(count)
    count -=1
print("Buon anno!")"""

#Tabellina: Chiedi all'utente un numero e stampa la tabellina di quel numero da 1 a 10 usando un ciclo 

"""numeri = int(input("inserisci un numero da 1 a 10: "))
for i in range(11):
    print(f"{numeri} * {i} = {numeri*i}")"""
    
#Indovina il numero: Genera un numero casuale tra 1 e 10. Chiedi all'utente di indovinare il numero. Continua a chiedere finché 
# l'utente non indovina, fornendo suggerimenti ("troppo alto", "troppo basso")

#Creazione e stampa: Crea una lista di 5 colori a tua scelta e stampala.

"""colori = ["rosso","blu","verde","arancione","marine"]
print(colori)"""

#Accesso elementi: Data la lista frutta = ["mela", "banana", "ciliegia", "dattero"], stampa il primo elemento, l'ultimo elemento e 
# l'elemento in posizione 2.

"""frutta = ["mela", "banana", "ciliegia", "dattero"]
print(f"Il primo elemento: {frutta[0]} ultimo elemento: {frutta[-1]} il secondo elemento: {frutta[1]}")"""

#Aggiunta elementi: Crea una lista vuota. Chiedi all'utente di inserire 3 nomi di animali e aggiungili alla lista. Stampa la 
# lista risultante.

"""lista_anim = []
for i in range(3):
    animali = str(input("inserisci 3 niomi di animali: "))
    lista_anim.append(animali)
print(lista_anim)"""

#Modifica elemento: Data la lista numeri = [1, 2, 3, 4, 5], modifica il terzo elemento in 10 e poi stampa la lista modificata.

"""numeri = [1, 2, 3, 4, 5]
numeri.insert(3,10)
print(numeri)"""

#Iterazione e calcolo: Data la lista prezzi = [12.50, 8.99, 5.00, 20.00], calcola e stampa la somma di tutti i prezzi usando un ciclo

"""prezzi = [12.50, 8.99, 5.00, 20.00]
tot = 0
for i in prezzi:
    tot = sum(prezzi)
print(f"La somma totale dei prezzi è: {tot}")"""

#Lista di liste: Crea una lista che contenga altre due liste: una con nomi di città italiane e una con nomi di città straniere. 
# Stampa il primo elemento della seconda sottolista.

"""citta_ita = ["roma", "napoli", "venezia"]
citta_stra = ["parigi", "tokyo", "barcellona"]

lista_mista = [citta_ita, citta_stra]
print(lista_mista)

# Stampa il primo elemento della seconda sottolista (città straniere)
print(lista_mista[1][0])"""

#Rimozione elementi: Data la lista lista_spesa = ["pane", "latte", "uova", "formaggio", "pane"], rimuovi la prima occorrenza di 
# "pane" e stampa la lista.

"""lista_spesa = ["pane", "latte", "uova", "formaggio", "pane"]
lista_spesa.remove("pane")
print(lista_spesa)"""

#Lunghezza stringa: Chiedi all'utente di inserire il suo nome e stampa la lunghezza del nome.

"""nome = str(input("inserisci un nome: "))
print(f"Il nome e: {nome} la lunghezza e: {len(nome)}")"""

#Concatenazione: Crea due stringhe, stringa1 = "Hello" e stringa2 = "World". Concatena le due stringhe e stampa il risultato.

"""stringa1 = "Hello"
stringa2 = "World"
print(stringa1 +" "+ stringa2)"""

#Sottostringhe (Slicing): Data la stringa messaggio = "Programmazione Python", estrai e stampa le seguenti sottostringhe:
"""I primi 5 caratteri.
Gli ultimi 6 caratteri.
I caratteri dal sesto al dodicesimo."""

"""messaggio = "Programmazione Python"
primi = messaggio[:5]
print(primi)
ultimi = messaggio[-6:]
print(ultimi)
inmezzo = messaggio[5:12]
print(inmezzo)"""

#Maiuscolo/Minuscolo: Chiedi all'utente di inserire una frase. Stampa la frase in maiuscolo e poi in minuscolo.

"""frase = str(input("inserisci una frase: "))
print(f"La frase da inserito e: ")
print(frase.upper())
print(frase.lower())"""

#Sostituzione: Data la stringa testo = "Ciao a tutti, sono un robot", sostituisci la parola "robot" con "programma" e stampa il nuovo testo.

"""testo = "Ciao a tutti, sono un robot"
print(testo.replace('robot','programmatore'))"""

#Divisione (Split): Data la stringa date = "2023-04-15", dividila in base al trattino (-) e stampa i singoli elementi.

"""date = "2023-04-15"
data_finale = date.split('-')
print(data_finale)"""

#Controllo presenza: Chiedi all'utente di inserire una frase e una parola. Controlla se la parola è presente nella frase e stampa un messaggio appropriato.

"""frase = str(input(f"inserisci una frase: "))
parola = str(input("inserisci una parola da controllare: "))
print(f"La frase e : {frase} e la parola da cercare e: {parola}")
if parola in frase: print("la parola ci sta")
else: print("la parola non ci sta")"""

#Inversione stringa: Chiedi all'utente una parola e stampala al contrario.

"""frase = str(input(f"inserisci una frase: "))

parola = str(input("inserisci una parola da controllare: "))
print(f"La frase e : {frase} e la parola da cercare e: {parola}")

if parola in frase: print("la parola ci sta")
else: print("la parola non ci sta")

inversa = parola[::-1]
print(f"La parola inversa è: {inversa}")"""

#Creazione e stampa:
"""Crea un set chiamato frutti con i seguenti elementi: 
    "mela", "banana", "ciliegia", "mela". Stampa il 
    set e osserva cosa succede con l'elemento duplicato.
Crea un set vuoto e aggiungi gli elementi "rosso", "verde", 
"blu" uno alla volta. Stampa il set."""

"""set1 = {"mela", "banana", "ciliegia", "mela"}
print(set1)

set2 = set()
set2.add("rosso")
set2.add("verde")
set2.add("blu")
print(set2)"""

#Operazioni di base:
"""Dati i set A = {1, 2, 3, 4} e B = {3, 4, 5, 6}:
Calcola e stampa l'unione di A e B.
Calcola e stampa l'intersezione di A e B.
Calcola e stampa la differenza tra A e B (elementi in A ma non in B).
Calcola e stampa la differenza simmetrica tra A e B (elementi in A o in B ma non in entrambi)."""

"""A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

set1 = set()
set2 = set()
set3 = set()
set4 = set()

unione = set1.union(A | B)
print(unione)
intersezione = A.intersection(B)
print(intersezione)
differenza = A.difference(B)
print(differenza)
differenza_simm = A.symmetric_difference(B)
print(differenza_simm)"""

#Rimozione elementi:
"""Dato il set numeri_pari = {2, 4, 6, 8, 10}, rimuovi 
l'elemento 6. Stampa il set risultante.
Prova a rimuovere un elemento che non esiste nel set 
(es. 3). Cosa succede? (Gestisci l'errore se necessario)."""

"""numeri_pari = {2, 4, 6, 8, 10}
numeri_pari.discard(6)
print(numeri_pari)
numeri_pari.discard(3)
print(numeri_pari)"""

#Controllo appartenenza:
"""Chiedi all'utente di inserire un frutto. Controlla se 
il frutto è presente nel set frutti creato all'esercizio 1 
e stampa un messaggio appropriato."""

"""set1 = {"mela", "banana", "ciliegia", "pera"}
print(set1)

cerca = str(input("inserisci un frutto: "))
if cerca in set1: print(f"Il frutto {cerca} ci sta")
else: print(f"Il frutto {cerca} non ci sta")"""

#Conversione da lista:
"""Data la lista numeri_duplicati = [1, 2, 2, 3, 4, 4, 5], 
convertila in un set per rimuovere i duplicati. Stampa il 
set."""

"""numeri_duplicati = [1, 2, 2, 3, 4, 4, 5]
insieme = set(numeri_duplicati)
print(insieme)"""

#Creazione e stampa:
"""Crea un dizionario chiamato persona con le seguenti 
coppie chiave-valore: nome: "Alice", eta: 30, citta: 
"Roma". Stampa l'intero dizionario.
Crea un dizionario vuoto chiamato libri_preferiti. 
Aggiungi tre voci: autore: "Titolo del Libro". 
Stampa il dizionario."""

"""persona = {"nome": "Alice", "eta": 30, "citta": "Roma"}
print(persona)

libri_preferiti = {}
libri_preferiti["autore"] = "Titolo del Libro"
libri_preferiti["titolo"] = "Titolo del Libro"
libri_preferiti["anno"] = "Titolo del Libro"
print(libri_preferiti)"""

#Accesso elementi:
"""Dal dizionario persona creato nell'esercizio 1, stampa 
il nome e l'età.
Prova ad accedere a una chiave che non esiste nel 
dizionario. Cosa succede? (Gestisci l'errore se necessario)."""

"""persona = {"nome": "Alice", "eta": 30, "citta": "Roma"}
print(persona)

print(f"Il nome e: {persona['nome']} eta e: {persona['eta']}")
# Gestione eccezione per chiave non esistente
cognome = persona.get('cognome')
if cognome is None:
    print("La chiave 'cognome' non esiste nel dizionario.")
else:
    print(cognome)"""
    
#Modifica e aggiunta elementi:
"""Modifica l'età di Alice a 31 nel dizionario persona.
Aggiungi una nuova coppia chiave-valore al dizionario 
persona: occupazione: "Ingegnere". Stampa il dizionario 
aggiornato."""

"""persona = {"nome": "Alice", "eta": 30, "citta": "Roma"}
print(persona)

persona["eta"] = 31
print(persona["eta"])

persona["occupazione"] = "Ingegnere"
print(persona)"""

#Iterazione su dizionari:
"""Itera sul dizionario persona e stampa solo le chiavi.
Itera sul dizionario persona e stampa solo i valori.
Itera sul dizionario persona e stampa sia le chiavi che 
i valori in questo formato: "Chiave: [chiave], Valore: 
[valore]"."""

"""persona = {"nome": "Alice", "eta": 30, "citta": "Roma"}
print(persona)

chiave = persona.keys()
print(chiave)

valori = persona.values()
print(valori)
for chiave, valore in persona.items():
    print(f"Chiave: [{chiave}], Valore: [{valore}]")"""

#Rimozione elementi:
"""Rimuovi la chiave citta dal dizionario persona. 
Stampa il dizionario risultante.
Usa il metodo pop() per rimuovere una chiave e ottenere il 
suo valore."""

"""persona = {"nome": "Alice", "eta": 30, "citta": "Roma"}
print(persona)

#del persona["citta"]
#print(persona)
rimoso = persona.pop("citta")
print(rimoso)"""

#Dizionario annidato:
"""Crea un dizionario studenti dove le chiavi sono i nomi 
degli studenti e i valori sono altri dizionari che 
contengono eta e voto_medio.
Esempio: studenti = 
{"Marco": {"eta": 20, "voto_medio": 8.5}, 
"Laura": {"eta": 22, "voto_medio": 9.2}}
Stampa il voto medio di "Marco"."""

"""studenti = {"Marco": {"eta": 20, "voto_medio": 8.5}, "Laura": {"eta": 22, "voto_medio": 9.2}}
print(studenti)
for chiave,valore in studenti.items():
    if chiave == "Marco": 
        media = studenti["Marco"]["voto_medio"]
        print(f"La media di marco e: {media}")"""

#Conteggio parole:
"""Data la stringa testo = "il cane e il gatto sono amici, 
il cane e il gatto giocano".
Trasforma la stringa in una lista di parole.
Usa un dizionario per contare le occorrenze di ciascuna 
parola (ignora la punteggiatura e le maiuscole/minuscole)."""

testo = "il cane e il gatto sono amici, il cane e il gatto giocano"

#testo1 = testo.split()
#print(testo1)
"""print(f"il testo e tutto in minuscolo: {testo.lower()}")
for i in testo:
    if i == ",": 
        testo1 = testo.lower().replace(",", "")
        print(f"testo senza punteggiatura: {testo1}")
print(f"il testo e diviso: {testo1.split()}")"""

"""dizionario = {}
lista=testo.split()
for parola in lista:
    if parola in dizionario:
         dizionario[parola] += 1
    else:dizionario[parola] = 1
print(dizionario)"""

#Gestione inventario:
"""Crea un dizionario inventario che mappi nomi di prodotti (stringhe) alla loro quantità (interi).
Permetti all'utente di aggiungere nuovi prodotti e quantità.
Permetti all'utente di aggiornare la quantità di un prodotto esistente.
Permetti all'utente di visualizzare l'intero inventario.
Permetti all'utente di rimuovere un prodotto dall'inventario."""

"""inventario = {"pane": 10,
    "latte": 5,
    "uova": 12
    }
while True:
    scelta = input("inserisci la scelta 1 di aggiungere un prodotto e 2 aggiornare la quantita del prodotto per rimuovere un prodotto metti 3 per 'uscire': ")
    if scelta == "uscire": break
    if scelta == "1": 
        prodotti = str(input("inserisci un prodotto: "))
        quantitta = int(input("inserisci la quantita: "))
        inventario[prodotti] = quantitta
        print(inventario)
    elif scelta == "2":
        aggiorna = str(input("inserisci il prodotto da aggiornare: "))
        aggio_quant = int(input(f"il prodoto {aggiorna} inscerisci la quantitta da modificare: "))
        inventario[aggiorna] = aggio_quant
        print(inventario)
    elif scelta == "3":
        rimuovi = str(input("inserisci il prodotto da rimuovi: "))
        inventario.pop(rimuovi)
        print(inventario)"""

#Filtrare numeri duplicati:
"""Chiedi all'utente di inserire una serie di numeri separati da spazi.
Converti la stringa in una lista di interi.
Usa un set per trovare e stampare solo i numeri unici.
Stampa anche i numeri duplicati (se presenti) usando un approccio che combini liste e set."""

"""serie_num = input("inserisci una serie di numere separati da spazio: ")
print(serie_num)

lista = serie_num.split()
print(lista)

set1 = set(lista)
print(set1)

duplicati = [x for x in lista if lista.count(x) > 1]
duplicati_unici = set(duplicati)
print("Duplicati:", duplicati_unici)"""

#Sistema di gestione contatti:
"""Crea un dizionario dove le chiavi sono i nomi dei contatti e i valori sono altri dizionari contenenti telefono e email.
Implementa funzionalità per:
Aggiungere un nuovo contatto.
Cercare un contatto per nome e visualizzarne i dettagli.
Aggiornare il telefono o l'email di un contatto esistente.
Eliminare un contatto.
Visualizzare tutti i contatti."""

"""telefono = {
    "fra": {"numero": 454544354, "Email": "dgdgdgd@sfdsf.df"},
    "marco": {"numero": 7645897, "Email": "dgdf@ddf.cxd"}
}

aggiugi = input("aggiungi un nuovo contatto: ")
num_tel = int(input("inserisci un numeri di telefono: "))
email = input("inserisci email: ")
telefono[aggiugi] = {"numero": num_tel, "Email": email}
print(telefono)

cerca = input("inserisci un nome da cercare: ")
print(telefono.get(cerca, "contato non trovato"))

aggiorna = input("inserisci un nome da aggiornare: ")
num = int(input("inserisci un nuovo numero: "))
email_new = input("inserisci un nuovo email: ")
telefono[aggiorna] = {"numero": num, "Email": email_new}
print(telefono)

rimuovi = input("inserisci un nome da cancella: ")
telefono.pop(rimuovi)
print(telefono)"""

#Analisi di testo con set e dizionari:
"""Data una frase, usa un set per trovare tutte le parole uniche.
Usa un dizionario per contare la frequenza di ogni parola.
Stampa le parole uniche e la frequenza di ogni parola."""

"""frase = "Il sole splende e il vento soffia, il sole scalda la terra."
lista = frase.lower().split()
set1 = set(lista)
print(set1)

frequnza = {}
for parola in lista:
    if parola in frequnza:
        frequnza[parola] += 1
    else:frequnza[parola] = 1
print(frequnza)"""

#Funzione di saluto:
"""Scrivi una funzione chiamata saluta che prende un nome come argomento e stampa un messaggio di saluto come "Ciao, [nome]!".
Chiama la funzione con il tuo nome."""

"""def saluto(nome):
    print(f"ciao {nome}!")

saluto("francesco")"""

#Somma di due numeri:
"""Scrivi una funzione chiamata somma_due_numeri che prende due numeri come argomenti, li somma e restituisce il risultato.
Chiama la funzione con due numeri a tua scelta e stampa il risultato."""

"""def somma_due_numeri(num1, num2):
    print(num1+num2)
    
somma_due_numeri(5,7)"""

#Controllo pari o dispari:
"""Scrivi una funzione chiamata is_pari che prende un numero intero come argomento.
La funzione deve restituire True se il numero è pari, altrimenti False.
Prova la funzione con numeri pari e dispari."""

"""def is_pari(num):
    vero = True
    falso = False
    if num % 2 == 0: print(vero)
    else: print(falso)
    
is_pari(5)"""

#Area del rettangolo:
"""Scrivi una funzione chiamata calcola_area_rettangolo che prende la larghezza e l'altezza di un rettangolo come argomenti.
La funzione deve calcolare e restituire l'area.
Usa la funzione per calcolare l'area di un rettangolo con larghezza 5 e altezza 10."""

"""def calcola_area_rettangolo(larghezza, altezza):
    area = larghezza * altezza
    print(area)
calcola_area_rettangolo(5,10)"""
  
#Trova il massimo:
"""Scrivi una funzione chiamata trova_massimo che prende una lista di numeri come argomento.
La funzione deve trovare e restituire il numero più grande nella lista.
Testa la funzione con una lista di numeri interi."""

"""def trova_massimo(lista):
    for i in lista:
        massimo = max(lista)
    print(f"Il massiono e: {massimo}")

conseri = []
for el in range(5):
    nume = int(input(f"inserisci un numero {el}: "))
    conseri.append(nume)
trova_massimo(conseri)"""
    
#Conteggio vocali:
"""Scrivi una funzione chiamata conta_vocali che prende una stringa come argomento.
La funzione deve contare e restituire il numero di vocali (a, e, i, o, u, sia maiuscole che minuscole) presenti nella stringa.
Prova la funzione con diverse parole o frasi."""

"""def conta_vocali(stringa): 
   counti = 0
   for el in stringa:
       if el in "aeiouAEIOU":counti += 1
   print(f"Le vocali nella frase sono: {counti}")
    
conta_vocali(stringa=str(input("inserisci una frase: ")))"""

#Palindromo:
"""Scrivi una funzione chiamata is_palindromo che prende una stringa come argomento.
La funzione deve restituire True se la stringa è un palindromo (si legge nello stesso modo al contrario), altrimenti False. Ignora spazi e maiuscole/minuscole.
Esempi: "anna", "radar", "A nut for a jar of tuna"."""

"""def palindromo(stringa):
    vero = True
    falso = False
    inversa = stringa[::-1] 
    if inversa==stringa:
        return print(vero)
    else:
        return print(falso)

def rimuoviSpazi(stringa):
    spazio=" "
    if stringa.isalpha():
        return stringa
    else:
        for i in range(len(spazio)):
            stringa =  stringa.lower().replace(spazio[i], "")
            
        return stringa

frase = input("inserisci una parola: ")
rimuoviSpazi(frase)
palindromo(frase)"""

#Generazione di numeri casuali (con default):
"""Scrivi una funzione chiamata genera_numeri_casuali che prende due argomenti: quantita (quanti numeri generare) e limite_superiore (il valore massimo che un numero può assumere).
Imposta un valore di default per limite_superiore a 100 se non viene fornito.
La funzione deve generare e restituire una lista di numeri interi casuali.
Importa il modulo random per usare random.randint().
Testa la funzione sia fornendo entrambi gli argomenti che omettendo limite_superiore."""

"""import random

def genera_numeri_casuali(quantita,limite_superiore):
    if limite_superiore == 0:
        print("limite non inserito")
        limite_superiore = 100
    else: print("limite inserito")
    for el in range(quantita):
        print(random.randint(0,limite_superiore))

quantita1 = int(input("inserisci qunati numeri da generare: "))
limite_superiore1 = int(input("inerisci il limete se non vuoi inserire in valore  permi '0': "))
genera_numeri_casuali(quantita1,limite_superiore1)"""
    
#Funzione ricorsiva per il fattoriale:
"""Scrivi una funzione ricorsiva chiamata fattoriale che calcola il fattoriale di un numero intero positivo n.
Ricorda: il fattoriale di 0 è 1, e il fattoriale di n è n * fattoriale(n-1).
Testa la funzione con alcuni numeri, come 5! (dovrebbe essere 120)."""


"""def palindromo(numero):
    vero = True
    falso = False
    numero_str = str(numero)
    inversa = numero_str[::-1] 
    if inversa==numero_str:
        return print(vero)
    else:
        return print(falso)

numero = int(input("inserisci una numero: "))
palindromo(numero)"""

#Creazione e importazione di un modulo semplice:
"""Passo 1: Crea il modulo. In una nuova cartella, crea un file chiamato operazioni_matematiche.py. All'interno di questo file, scrivi due funzioni:
addizione(a, b): che restituisce la somma di a e b.
sottrazione(a, b): che restituisce la differenza tra a e b.
Passo 2: Importa e usa il modulo. Nello stesso ambiente (stessa cartella), crea un altro file chiamato main.py. In main.py:
Importa il modulo operazioni_matematiche.
Usa le funzioni addizione e sottrazione per eseguire delle operazioni e stampa i risultati."""

"""import operazioni_matematiche 

print(operazioni_matematiche.addizione(5,4))
print(operazioni_matematiche.sottrazione(5,5))"""

#Importazione specifica e alias:
"""Passo 1: Modifica il modulo. Nel file operazioni_matematiche.py che hai creato, aggiungi una terza funzione:
moltiplicazione(a, b): che restituisce il prodotto di a e b.
Passo 2: Importazione selettiva e alias. In un nuovo file calcoli.py:
Importa solo la funzione moltiplicazione usando from operazioni_matematiche import moltiplicazione.
Importa la funzione addizione dandole un alias, ad esempio somma, usando from operazioni_matematiche import addizione as somma.
Usa entrambe le funzioni importate (moltiplicazione e somma) e stampa i risultati."""

#Utilizzo di moduli built-in: math:
"""Importa il modulo math.
Usa la funzione math.sqrt() per calcolare la radice quadrata di un numero (es. 25).
Usa math.pi per calcolare l'area di un cerchio con raggio 5. Stampa entrambi i risultati."""

"""import math

print(math.sqrt(25))
print(math.pi*5)"""

#Utilizzo di moduli built-in: random:
"""Importa il modulo random.
Genera un numero intero casuale tra 1 e 100 (inclusi) usando random.randint().
Seleziona un elemento casuale da una lista di colori ["rosso", "verde", "blu", "giallo"] usando random.choice().
Mescola (shuffla) una lista di numeri [1, 2, 3, 4, 5] usando random.shuffle(). Stampa tutti i risultati."""

"""import random

print(random.randint(1,100))

lista = ["rosso", "verde", "blu", "giallo"]
print(random.choice(lista))

numero = [1, 2, 3, 4, 5]
random.shuffle(numero)
print(numero)"""

#Organizzazione del codice in un pacchetto:
"""Passo 1: Crea la struttura del pacchetto. In una nuova cartella, crea una sottocartella chiamata strumenti (questo sarà il tuo pacchetto).
Dentro la cartella strumenti, crea due file:
__init__.py (può essere vuoto, ma è necessario per indicare che strumenti è un pacchetto).
conversione.py: All'interno di questo file, scrivi una funzione celsius_a_fahrenheit(celsius) che converte una temperatura da Celsius a Fahrenheit e la restituisce.
formattazione.py: All'interno di questo file, scrivi una funzione formatta_nome(nome, cognome) che restituisce il nome completo in formato "Cognome, Nome".
Passo 2: Importa dal pacchetto. Nel file main_pacchetto.py (fuori dalla cartella strumenti ma nella stessa cartella genitore):
Importa le funzioni dal pacchetto usando from strumenti.conversione import celsius_a_fahrenheit e from strumenti.formattazione import formatta_nome.
Usa queste funzioni per eseguire una conversione di temperatura e formattare un nome, stampando i risultati."""

#Gestione di ValueError con conversione input:
"""Chiedi all'utente di inserire un numero intero.
Usa un blocco try-except per gestire l'eccezione ValueError che si verifica se l'utente inserisce qualcosa che non è un numero intero (es. una stringa).
Se si verifica l'errore, stampa un messaggio amichevole come "Input non valido. Per favore, inserisci un numero intero."
Se l'input è valido, convertilo in un intero e stampalo."""

"""try:
    num = int(input("inserisci un numero :"))
except ValueError:
    print("Input non valido. Per favore, inserisci un numero intero.")"""
    
#Gestione di ZeroDivisionError:
"""Chiedi all'utente di inserire due numeri: un numeratore e un denominatore.
Prova a dividere il numeratore per il denominatore.
Usa un blocco try-except per catturare l'eccezione ZeroDivisionError se il denominatore è zero.
In caso di errore, stampa "Impossibile dividere per zero."
Altrimenti, stampa il risultato della divisione."""

"""try:
    num1 = int(input("inserire un numero: "))
    num2 = int(input("inserire un numero: "))
    divi = num1/num2
    print(divi)
except ZeroDivisionError:
    print("Impossibile dividere per zero.")"""
    
#Gestione di IndexError con liste:
"""Crea una lista numeri = [10, 20, 30].
Chiedi all'utente di inserire un indice.
Prova ad accedere all'elemento della lista usando l'indice fornito.
Usa un blocco try-except per catturare l'eccezione IndexError se l'indice è fuori dai limiti della lista.
In caso di errore, stampa "Indice non valido. La lista ha solo 3 elementi (da 0 a 2)."
Altrimenti, stampa l'elemento trovato."""

"""try:
    numeri = [10, 20, 30]
    cerca = int(input("inserisci un indice: "))
    for el in numeri:
        cerca in numeri
    print(numeri[cerca])
except IndexError:
    print("Indice non valido. La lista ha solo 3 elementi (da 0 a 2).")"""
    
#Gestione di FileNotFoundError:
"""Chiedi all'utente il nome di un file.
Prova ad aprire il file in modalità lettura ('r').
Usa un blocco try-except per catturare l'eccezione FileNotFoundError se il file non esiste.
In caso di errore, stampa "Errore: Il file specificato non è stato trovato."
Se il file esiste, leggi il suo contenuto e stampalo (assicurati di chiudere il file). Suggerimento: Puoi creare un file di testo temporaneo per testare questo esercizio."""

"""try:
    cerca = input("inserisci il nome del file: ")
    with open(cerca, "r") as file:
        conenuto = file.read()
        print(conenuto)
        file.close()
except FileNotFoundError:
    print("Errore: Il file specificato non è stato trovato.")"""
    
#Utilizzo di else e finally:
"""Riprendi l'esercizio 1 (Gestione di ValueError).
Aggiungi un blocco else che si esegua solo se non si verificano eccezioni nel blocco try. Nel blocco else, stampa "Input accettato e convertito correttamente."
Aggiungi un blocco finally che stampi "Operazione completata." Indipendentemente dal fatto che si sia verificato un errore o meno."""

"""try:
    num = int(input("inserisci un numero :"))
except ValueError:
    print("Input non valido. Per favore, inserisci un numero intero.")
else: print("Input accettato e convertito correttamente.")
finally: print("Operazione completata.")"""

#Gestione di eccezioni multiple:
"""Chiedi all'utente di inserire una lista di numeri separati da virgole (es. "1,2,tre,4").
Prova a:
Dividere la stringa in una lista di stringhe.
Convertire ogni stringa in un intero.
Calcolare la somma degli interi.
Usa un singolo blocco try-except con più clausole except per gestire:
ValueError (se una delle stringhe non può essere convertita in intero).
TypeError (se provi a sommare elementi di tipo diverso, anche se con la conversione corretta questo dovrebbe essere evitato).
Se si verifica una delle eccezioni, stampa un messaggio specifico per l'errore.
Se tutto va bene, stampa la somma."""

"""try: 
    nume = input("inserisci una serie di numeri separati con la ',': ")
    print(nume)
    dividi = nume.split(",")
    numero_ = [int(x) for x in dividi]
    print(numero_)
    print(sum(numero_))
except ValueError:
    print("Input non valido. Per favore, inserisci un numero intero.")
except TypeError:
    print("operazione non eseguita")"""
    
#Sollevamento di eccezioni (raise):
"""Scrivi una funzione verifica_eta(eta) che prenda un'età come argomento.
Se l'età è minore di 0 o maggiore di 120, la funzione dovrebbe sollevare un ValueError con un messaggio appropriato (es. "L'età deve essere tra 0 e 120.").
Altrimenti, stampa "Età valida."
Chiama la funzione con diversi valori (validi e non validi) e usa try-except per catturare l'eccezione sollevata."""

def verifica_eta(eta):
    if eta > 0 and eta < 120:
        print(f"{eta} eta valida")
    else

try:
    eta_ = int(input("inserisci un eta: "))
    verifica_eta(eta_)
except ValueError:
    print("L'età deve essere tra 0 e 120")


#Hai ricevuto un messaggio WhatsApp da un numero sconosciuto. Potrebbe essere di quella ragazza/ragazzo con accento straniero che hai incontrato ieri sera?
"""Scrivi una semplice funzione per verificare se la stringa contiene la parola hallo in diverse lingue.Ecco le lingue delle possibili persone che hai incontrato la sera prima:
hello - inglese
ciao - italiano
salut - francese
hallo - tedesco
hola - spagnolo
ahoj - republica cieca
czesc - polacco"""

"""def controllo(strnga):
    if strnga.lower() == "hello":
        print("e inglese")
    elif strnga.lower() == "ciao":
        print("e italiano")
    elif strnga.lower() == "salut":
        print("e francese")
    elif strnga.lower() == "hallo":
        print("e tedesco")
    elif strnga.lower() == "hola":
        print("e spagnolo")
    elif strnga.lower() == "ahoj":
        print("e republica cieca")
    elif strnga.lower() == "czesc":
        print("e polacco")
controllo(strnga=input("inserisci un saluto: "))"""