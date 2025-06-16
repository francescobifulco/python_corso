#Create un programma che richiede all’utente Nome,Cognome e Indirizzo Email e poi lo stampa nel terminale inmaniera formattata:Esempio’Il 
# tuo nome è Tommaso, il tuo cognome è Muraca, il tuoindirizzo Email è: corsi.online.muraca@gmail.com’

#nome = input("Inserisci il tuo nome: ")
#cognome = input("Inserisci il tuo cognome: ")
#Email = input("Inserisci la tua Email: ")

#print("Il tuo nome e: " +nome+ " il tuo cognome e: " +cognome+ " la tua email e: " +Email)

#Create un programma che richiede all’utente Nome, anno di nascita e giorno della settimana (a numero) e stampa in maniere formattata 
# oltre al nome, l’età e i giorni che mancano al prossimo weekend (sabato): Esempio ’Il tuo nome è Tommaso, hai 38 anni e mancano 4 giorni
# al weekend’

#nome = input("Inserisci il tuo nome: ")
#eta = input("Inserisci anno di nascita: ")
#settimana = input("Inserisci il giorno della settimana (1=Lunedì, 7=Domenica): ")

#eta_essa = int(eta)
#anno = 2025
#eta1 = anno - eta_essa

#giorno_reale = int(settimana)
#sabato = 6
#giorni_mancanti_weekend = (sabato - giorno_reale + 7) % 7

#print(f"Il tuo nome e: {nome}  i tuoi anni: {eta1}  e mancano a: {settimana} giorni al weekend.")

#create un programma che richiede all’utente l’età, se ha la patente e se ha bevuto e in base alle risposte ci dice se può guidare.

"""eta = input("Inserisci la tua eta: ")
eta_int = int(eta)
if eta_int >= 18:
    print("puoi guidare sei maggiorenne")
    
    patente = input("Inserisci se hai la patente (si/no)")
    if patente == "si":
        print("puoi guidare hai la patente")
        
        bevuto = input("Inserisci se hai bevuto (si/no)")
        if bevuto == "si": print("non puoi guidare perche hai bevuto")  
        else:print("puoi giudare non hai bevuto")
    else: print("non puoi giudare non hai la patente")
else: print("non puoi giudare sei minorenne")"""

#create un programma che richiede all’utente tre numeri e ci restituisce il numero più grande dei tre o se ci sono 2 numeri uguali.

"""num1 = input("Inserisci un numero 1: ")
num2 = input("Inserisci un numero 2: ")
num3 = input("Inserisci un numero 3: ")

num1_ = int(num1)
num2_ = int(num2)
num3_ = int(num3)

numero_piu_grande = None

if num1_ == num2_ and num2_ == num3_: print("tutti i numeri sono uguali")

elif num1_ == num3_: 
    print("ci sono due numeri uguali", num1_)
    print(f" il massimo e: max")
    if num1_ > num3_:
        numero_piu_grande = num1_
    else: # include il caso in cui numero3 > numero1 o numero3 == numero1
        numero_piu_grande = num3_
    print(f"Il numero più grande è: {numero_piu_grande}")
    
elif num1_ == num3_:
    print(f"Il primo e il terzo numero sono uguali: {num1_}.")
    if num1_ > num2_:
        numero_piu_grande = num1_
    else:
        numero_piu_grande = num2_
    print(f"Il numero più grande è: {numero_piu_grande}")

elif num2_ == num3_:
    print(f"Il secondo e il terzo numero sono uguali: {num2_}.")
    if num2_ > num1_:
        numero_piu_grande = num2_
    else:
        numero_piu_grande = num1_
    print(f"Il numero più grande è: {numero_piu_grande}")
else:
    print("Nessun numero è uguale.")
    numero_piu_grande = num1_ 
    if num2_ > numero_piu_grande:
        numero_piu_grande = num2_
    
    # Confrontiamo con il terzo numero
    if num3_ > numero_piu_grande:
        numero_piu_grande = num3_
        
    print(f"Il numero più grande è: {numero_piu_grande}")"""
    
#Il programma chiederà all’utente 2 numeri e quale operazione deve fare su quei numeri, restituirà quindi il risultato dell’operazione.

"""num1 = input("Inserisci un numero 1: ")
num2 = input("Inserisci un numero 2: ")

num1_ = int(num1)
num2_ = int(num2) 

operazione = input("Inserisci una operazione (1 a 4): ")
#operazione_int = int(operazione)

if operazione == "1":print(num1_+num2_)
elif operazione == "2":print(num1_-num2_)
elif operazione == "3": print(num1_*num2_)
elif operazione == "4": 
    if num2_ == 0: print("divisione impossibile")
    else: print(num1_/num2_)"""
    
#Scrivete un programma che chiede all'utente di inserire un numero e poi stampi la tabellina di quel numero da 1 a 10

"""num1 = input("Inserisci un numero da 1 a 10: ")
num1_ = int(num1)

count = 0
while count <= 10:
    resul = num1_*count
    print(f"{num1_} * {count} = {resul}" )
    count +=1"""
    
#Scrivete un gioco in cui il giocatore 1 inserisce un numero da 1 a 100 e il giocatore2 ha 5 tentativi per 
# indovinare il numero. Il programma fornisce suggerimenti (troppo alto, troppo basso) termina quando l'utente 
# indovina correttamente, quando i tentativi finiscono o se scrive «mi arrendo».

"""gio1 = int(input("Inserisci un numero da 1 a 100: "))
gio2 = 5

print(f"Ho pensato a un numero tra 1 e 100. Hai {gio2} tentativi per indovinare!")
print("Puoi digitare 'mi arrendo' in qualsiasi momento per terminare il gioco.")

while gio2 > 0:
    indovina = int(input("indovina il numero: "))
    haiperso = input("vuoi arrendere ('mi arrendo') se non vuoi arrandere premi invio: ")
    if haiperso == "mi arrendo": 
        print("ti sei arreso")
        break
    if indovina > gio1: print("troppo grande")
    elif indovina < gio1: print("numero troppo baso")
    else: 
        print("hai indovinato")
        break
    gio2 -= 1
    if gio2 > 0:
        print(f"Hai ancora {gio2} tentativi.")
    else:
        print("non hai piu vita")"""
        
#Trasformate la calcolatrice che avete creato in precedenza in un programma reale che esegue operazioni sui numeri finche l’utente non 
# richiede il risultato e si chiude solo se l’utente inserisce «Esci»

"""valore = ""
num1 = int(input("Inserisci un numero 1: "))
while True:
    
    num2 = int(input("Inserisci un numero 2: "))
    operazione = input("Inserisci una operazione (som,sott,molt,divi): ")
    esegui = input("se vuoi il risultato del operazione premi '=' se vuoi inserire un altro numero inserrisci 'altro': ")
    
    if valore == "esci":
            print("Programma terminato.")
            break
        
    if esegui == "=" or esegui == "altro":
        if operazione == "som":
            print(f"Risultato: {num1 + num2}")
        elif operazione == "sott":
            print(f"Risultato: {num1 - num2}")
        elif operazione == "molt":
            print(f"Risultato: {num1 * num2}")
        elif operazione == "divi":
            if num2 == 0:
                print("Errore: divisione per zero non consentita.")
            else:
                print(f"Risultato: {num1 / num2}")
        else:
            print("Operazione non riconosciuta.")
    else:
        print("Hai scelto di non eseguire l'operazione.")"""
        
#Scrivete un programma che chiede all'utente una lista di parole e restituisce la lunghezza di ogni parola.

"""lista = []
nume_parole = int(input("quanti parole vuoi aggiungere: "))

for parole in range(nume_parole):
    elemento = input(f"Inserisci una parola {parole + 1}: ")
    lista.append(elemento)
print(f"La mia lista di parole e: {lista}")

for parola in lista:
    print(f"'{parola}' ha lunghezza: {len(parola)}")"""
    
#Scrivete un programma che chiede all'utente una parola e restituisce solo le vocali e l’indice della vocale all’interno della parola.

"""parole = input("Inserire una parola: ")
print(f"La tua parola e: {parole}")

vocale = str(input("inserisci una vocale: "))
if len(vocale) == 1 and vocale in "aeiou":
    conteggio = parole.count(vocale)
    print(f"La vocale {vocale} si ripete in {conteggio} volte nella parola {parole}")
posizioni_trovate = []
for indice in range(len(parole)):
    if parole[indice] == vocale:
        posizioni_trovate.append(indice)
if posizioni_trovate: print(f"La vocale '{vocale}' si trova alle posizioni: {posizioni_trovate}")
else: print(f"La vocale '{vocale}' non è stata trovata nella parola.")"""

#Scrivete una programma che richiede una lista di numeri all’utente e fornisce in output un istogramma basato su questi numeri, usando asterischi per disegnarlo. Data ad esempio la lista [3, 7, 9, 5], il programma dovrà produrre questa
#sequenza:
"""
***
*******
*********
*****
"""

"""lista = []
quanti = int(input("Quanti numeri vuoi aggiungere: "))

for i in range(quanti):
    numero = int(input(f"Inserisci il numero {i + 1}: "))
    lista.append(numero)

print(f"La mia lista di numeri è: {lista}")

print("Istogramma:")
for numero in lista:
    print("*" * numero)"""
    
#Scrivete un programma che chiede una stringa all’utente e restituisce un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.
"""Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}
"""

"""frase = str(input("inserisci una frase: "))
print(f"La frase inserita e: {frase}")

frequnza = {}

for carattere in frase:
     if carattere in frequnza:frequnza[carattere] += 1
     else:frequnza[carattere] = 1
print(f"La frequenza dei caratteri è: {frequnza}")"""

#Scrivete un programma che chiede un numero all’utente e restituisce un dizionario con il quadrato del numero, se è pari o dispari e quante cifre contiene.
"""
Esempio:
Numero 12
Risultato
{‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }
"""

"""numero = int(input("inserisci un numero: "))
print(f"Il numero inserito e: {numero}")

infor = {}

quar = numero * numero
infor['quadrato'] = quar"""

#pari = "pari"
#disp = "dispari"
#if numero % 2 == 0: infor['pari o dispari'] = pari
#else: infor['pari o dispari'] = disp

"""if numero % 2 == 0: pari="pari"
else: pari="dispari"
infor['pari o dispari'] = pari

numero_ = str(numero)
infor['n. cifre'] = len(numero_)

print(infor)"""

#Scrivete un programma che prenda i nomi degli alunni di una classe e i loro voti, quando l’utente scrive media il programma andrà a 
#stampare i nomi di tutti gli alunni e per ogni alunno la media dei voti.
"""Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10"""

"""alunni = {}

while True:
    nome = input("Nome alunno (o 'media' per finire): ")

    if nome == "media":
        break

    if nome not in alunni:
        alunni[nome] = []

    while True:
        voto = input(f"Inserisci un voto per {nome} ('fine' per cambiare alunno): ")
        if voto == "fine":
            break
        alunni[nome].append(float(voto))

for nome in alunni:
    media = sum(alunni[nome]) / len(alunni[nome])
    print(f"Nome: {nome}, Media: {media}")
alunni = {}

while True:
    nome = input("Nome alunno (o 'media' per finire): ")

    if nome == "media":
        break

    while True:
        voto = input(f"Inserisci un voto per {nome} ('fine' per cambiare alunno): ")
        if voto == "fine":
            break
        alunni[nome].append(float(voto))

for nome in alunni:
    media = sum(alunni[nome]) / len(alunni[nome])
    print(f"Nome: {nome}, Media: {media}")"""

"""1.Età del conducente:
⚬ Meno di 18 anni → "Non sei idoneo per l'assicurazione"
⚬ 18 - 25 anni → Applica una maggiorazione del 20% sul prezzo base
⚬ 26 - 50 anni → Nessuna maggiorazione
⚬ Più di 50 anni → Sconto del 10%
2.Anni di esperienza alla guida:
⚬ Meno di 2 anni → Applica una maggiorazione del 30% sul prezzo base
⚬ 2 o più anni → Nessuna maggiorazione
3.Numero di incidenti negli ultimi 5 anni:
⚬ 0 incidenti → Nessun aumento
⚬ 1 incidente → Aumento del 15%
⚬ 2 o più incidenti → Aumento del 30%
⚬ Più di 4 incidenti → "Non sei idoneo per l'assicurazione"
4.Scelta del pacchetto assicurativo:
⚬ Base: Prezzo standard
⚬ Intermedio: +20%
⚬ Premium: +50%
Prezzo base dell'assicurazione: 500€"""

"""utenti = {}
prezzo_base = 500
id_utente = 1

while True:
    opzione = input("Vuoi inserire un utente? Digita 'esci' per uscire oppure 'si' per continuare: ").lower()
    if opzione == "esci":
        break

    eta = int(input("Inserisci l'età: "))
    if eta < 18:
        continue
    anniExp = int(input("Inserisci gli anni di esperienza: "))
    if anniExp > eta - 18:
        print("Non mentire!")
        continue

    incidentiFatti = int(input("Inserisci numero incidenti fatti negli ultimi 5 anni: "))
    if incidentiFatti > 4:
        print("Non sei idoneo per l'assicurazione")
        continue

    tipoPacchetto = input("Inserisci scelta: BASE - INTERMEDIO - PREMIUM: ").upper()

    prezzo = prezzo_base

    if eta < 18:
        print("Non sei idoneo per l'assicurazione")
        continue
    elif eta <= 25:
        prezzo += prezzo_base * 0.2
    elif eta > 50:
        prezzo -= prezzo_base * 0.1

    if anniExp < 2:
        prezzo += prezzo_base * 0.3

    if incidentiFatti == 1:
        prezzo += prezzo_base * 0.15
    elif incidentiFatti >= 2:
        prezzo += prezzo_base * 0.3

    if tipoPacchetto == "BASE":
        prezzo = prezzo
    elif tipoPacchetto == "INTERMEDIO":
        prezzo = prezzo * 1.2
    elif tipoPacchetto == "PREMIUM":
        prezzo = prezzo * 1.5

    utente = {
        "età": eta,
        "anni di esperienza": anniExp,
        "incidenti": incidentiFatti,
        "pacchetto": tipoPacchetto,
        "prezzo finale": round(prezzo, 2)
    }

    utenti[id_utente] = utente
    id_utente += 1

    print("Prezzo finale assicurazione:", prezzo, "€")"""
  
#Scrivete un programma che utilizza una funzione che accetta come parametro una stringa passata dall’utente e restituisce in risposta se è palindroma o no.
"""Esempio:
‘I topi non avevano nipoti’ è palindroma
‘Ciao’ non è palindroma"""
 
"""def palindromo(stringa):

    inversa = stringa[::-1] 
    if inversa==stringa:
        return "frase palidroma"
    else:
        return "frase non palidroma"

def rimuoviSpazi(stringa):
    caratteriSpeciali=",.:; -_!?= @+"
    if stringa.isalpha():
        return stringa
    else:
        for i in range(len(caratteriSpeciali)):
            stringa =  stringa.lower().replace(caratteriSpeciali[i], "")
            
        return stringa

while True:
    parola = input("inserisci parola: ")
    parola = rimuoviSpazi(parola)
    print(palindromo(parola))"""
    
#Secondo Esercizio Scrivete un programma che riceve in input una stringa lunga e verifica se ci sono duplicati, quanti sono, quali sono e quanto sono lunghi i duplicati.
"""Esempio:
‘La casa è grande, una cucina una camera e un giardino. La cucina è piccola e la camera è spaziosa. Il giardino è verde
e fiorito.’
#outpout
"La" appare 2 volte, lunghezza 2.
"è" appare 3 volte, lunghezza 1.
"una" appare 2 volte, lunghezza 2.
"cucina" appare 2 volte, lunghezza 6.
"camera" appare 2 volte, lunghezza 6.
"e" appare 2 volte, lunghezza 1.
"un" appare 2 volte, lunghezza 2.
"giardino" appare 2 volte, lunghezza 8."""

"""stringa = "La casa è grande, una cucina una camera e un giardino. La cucina è piccola e la camera è spaziosa. Il giardino è verde e fiorito."

def rimuoviSpazi(stringa):
    stringa2 = ""
    for i in stringa:
        if i.isalnum() or i.isspace():
            stringa2 += i
    return stringa2

def duplicati(stringa,sep): #funzione che crea una lista con tutte le parole della lista
    lista=stringa.split(sep)
    frequnza = {}
    for parola in lista:
     if parola in frequnza:
         frequnza[parola] += 1
     else:frequnza[parola] = 1
    return frequnza



while True:
    parola = input("inserisci parola: ")
    parola = rimuoviSpazi(parola)
    frequenza = duplicati(parola, " ")
    controllo = False
    for parola in frequenza:
        if frequenza[parola] > 1:
            controllo = True
            print(f"La parola e: {parola} appare num {frequenza[parola]} e lunga: {len(parola)}")
    if not controllo:
        print("non ci sono dupplicati")"""

"""Scrivete un programma che utilizza il cifrario di Cesare per criptare una
parola o decriptarla.
Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
di posti corrispondente alla chiave."""

"""Scrivete un programma che genera 5 numeri
casuali e li salva su un file, l’utente dovrà
cercare di indovinarne almeno 2 oppure
avrà perso."""

"""import random

lista = []
for i in range(5):
    randomo = random.randint(0,100)
    lista.append(randomo)

with open("gioco.txt", "w") as filee:
    filee.write(" ".join(str(x) for x in lista))

count = 0
while True:
    indoviva = input("indoviva due numeri 'esci' per uscire: ")
    if indoviva == "esci": 
        break
    indoviva_ = int(indoviva)
    if indoviva_ in lista:
        print("hai indovinato")
        count += 1
        if count == 2:
            print("hai indovinato 2 numeri")
            break
    else: print("non hai indovinato")"""
    
testo = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus mattis fermentum facilisis. Nulla et commodo est. Donec molestie pharetra orci, in condimentum lorem semper eget. Aenean nec sapien porta, gravida ante pretium, posuere ipsum. Quisque rutrum ante at eleifend sagittis. Fusce tellus enim, lacinia suscipit sollicitudin semper, volutpat sit amet ligula. Donec massa lectus, luctus quis ligula vel, posuere scelerisque dui.
Ut iaculis velit ac mi faucibus dictum. Nunc vulputate tellus aliquet sagittis pellentesque. Nulla consequat dolor at dictum pharetra. Aliquam sit amet nibh et ante sodales mollis non a massa. Proin sollicitudin, lorem et rutrum luctus, lacus ex molestie neque, at dictum metus metus sit amet est. Morbi non nibh cursus, faucibus nulla id, ornare augue. Ut varius rutrum sem id mattis.
Integer rhoncus risus vel ante tincidunt posuere. Morbi vel turpis eu tortor mollis malesuada. Ut id maximus lacus. Fusce et mi nec est posuere ullamcorper eget ac ipsum. Donec varius sagittis turpis scelerisque feugiat. Nunc mauris arcu, dictum ut lorem quis, volutpat tempor lectus. Mauris nec fringilla ligula. Suspendisse potenti. Quisque sollicitudin nisi mi. Etiam ac fermentum felis. Suspendisse scelerisque at erat id porta. Pellentesque vel nibh auctor, accumsan nibh vel, iaculis turpis. Aliquam at erat dictum massa porta tempus laoreet sed arcu. Fusce tempus semper tincidunt. Mauris arcu est, pretium id egestas iaculis, luctus a magna. Donec in nunc lobortis, pellentesque est sit amet, imperdiet ex.
Fusce aliquet interdum feugiat. Suspendisse venenatis odio nec felis consectetur, et ornare magna vehicula. Nullam tempor justo non tortor efficitur, eget molestie augue tempus. Mauris ut leo nec enim venenatis porta. Aenean malesuada tellus eu nisi imperdiet, ac rutrum risus consequat. Nunc porta viverra sodales. Quisque vehicula mauris vitae vestibulum congue. Nulla elit lorem, mollis non ipsum vitae, pretium congue purus. Duis ut dolor orci. Mauris sit amet libero nibh. Curabitur commodo a est non dignissim. Aenean at posuere ex, vitae convallis dui. Aliquam hendrerit mattis aliquam. In hac habitasse platea dictumst.
In efficitur mauris eget egestas viverra. Aenean sodales ex ac risus volutpat congue. Pellentesque cursus, ante nec eleifend pulvinar, lorem ante euismod massa, sagittis blandit ante felis at mauris. Aliquam in fringilla urna, aliquam faucibus velit. Nullam non nulla in orci ultricies volutpat. Nullam et auctor diam. Vestibulum rutrum eleifend ipsum et varius. Cras pretium purus risus, posuere imperdiet tortor placerat ut. Maecenas id ornare enim. Quisque sollicitudin, lectus sed cursus venenatis, augue tortor sodales dui, ac ornare risus tortor ac justo."""

with open("testo.txt", "w") as filee:
    filee.write(testo)

with open("testo.txt", "r") as filee:
    contenuto = filee.read()
#print(contenuto)
caratteri = contenuto.replace("\n","")
print(f"numero di carratteri: {len(caratteri)}")
parole = contenuto.split()
print(f"numeri di parole: {len(parole)}")
righe = contenuto.split("\n")
print(f"numero di righe: {len(righe)}")