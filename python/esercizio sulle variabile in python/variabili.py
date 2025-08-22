#Esercizio 1: Dichiarazione e Assegnazione di una Variabile Stringa
#Dichiara una variabile chiamata nome_utente e assegnale il valore "Mario Rossi". Poi stampa il valore di questa variabile.

nome_utente = "Mario Rossi"

print(f'il valore della variabile e: {nome_utente}')

#Esercizio 2: Dichiarazione e Assegnazione di una Variabile Numerica Intera
#Dichiara una variabile chiamata eta_utente e assegnale il valore 25. Stampa il valore della variabile.

eta_utente = 25

print(f'ecco il valore del della variabile e: {eta_utente}')

#Esercizio 3: Dichiarazione e Assegnazione di una Variabile Numerica Decimale
#Dichiara una variabile chiamata prezzo_articolo e assegnale il valore 19.99. Stampa il valore della variabile.

prezzo_articolo = 19.99

print(f'ecco il prezzo del articolo: {prezzo_articolo}')

#Esercizio 4: Assegnazione di una Variabile Booleana
#Dichiara una variabile chiamata is_studente e assegnale il valore True. Stampa il valore della variabile.

is_studente = True

print(f'ecco il valore della varibile e: {is_studente}')

#Esercizio 5: Ri-assegnazione di una Variabile
#Dichiara una variabile punti e assegnale il valore 100. Successivamente, cambia il valore di punti a 150. Stampa il valore di punti dopo la ri-assegnazione.

punti = 100
print(f'il valore originale della variabile')

punti = 150
print(f'il valore della variabile ri-assegnazione')

#Esercizio 6: Copia di Valore tra Variabili
#Dichiara una variabile saldo_conto = 500. Dichiara una seconda variabile saldo_backup e assegnale il valore di saldo_conto. Successivamente, cambia il valore di saldo_conto a 400. Stampa sia saldo_conto che saldo_backup per vedere i loro valori finali.

saldo_conto = 500
saldo_backup = saldo_conto
saldo_conto = 400

print(f'il valore finale di saldo backup e: {saldo_backup}')
print(f'il valore finale di saldo conto e: {saldo_conto}')

#Esercizio 7: Utilizzo di Variabili in un'Operazione
#Dichiara due variabili: lato1 = 7 e lato2 = 5. Calcola il perimetro di un rettangolo con questi lati e assegna il risultato a una nuova variabile chiamata perimetro. Stampa il valore di perimetro.

lato1 = 7
lato2 = 5
perimetro = (lato1 + lato2) * 2

print(f'il valore del perimetro del rettangolo e: {perimetro}')

#Esercizio 8: Combinazione di Stringhe tramite Variabili
#Dichiara una variabile saluto = "Ciao," e una variabile destinatario = "Mondo!". Concatena queste due variabili (aggiungendo uno spazio nel mezzo) e assegna il risultato a una nuova variabile messaggio_completo. Stampa messaggio_completo.

saluto = "Ciao,"
destinatario = "Mondo!"

print(f'ecco il messaggio completo: {saluto} {destinatario}')

#Esercizio 9: Scambiare i Valori di Due Variabili
#Dichiara variabile_a = 10 e variabile_b = 20. Scambia i loro valori in modo che variabile_a diventi 20 e variabile_b diventi 10 (senza usare una variabile temporanea aggiuntiva se possibile, pensando al 'tuple unpacking' di Python). Stampa i valori di variabile_a e variabile_b dopo lo scambio.

variabile_a = 10
variabile_b = 20

variabile_a = variabile_b
variabile_b = variabile_a

#Esercizio 10: Dichiarazione di Variabili Multiple sulla Stessa Riga
#Dichiara tre variabili, x, y, z, e assegna loro rispettivamente i valori 1, 2, 3, tutto sulla stessa riga. Stampa il valore di ciascuna variabile.

x = 1, y = 2, z = 3

print(f'i valore delle variabili sono z: {z}, x: {x}, y: {y}') 

#Esercizio 11: Conversione di Tipo Implicita e Esplicita
#Dichiara una variabile numero_testo = "123". Convertila in un intero e assegna il risultato a numero_intero. Poi, dichiara una variabile valore_float = 45.67. Convertila in un intero e assegna il risultato a valore_intero_da_float. Stampa entrambi i nuovi valori.

numero_testo = "123"
numero_intero = int(numero_intero)
valore_float = 45.67
valore_intero = int(valore_float)

#Esercizio 12: Variabili in Nomi di File
#Dichiara una variabile nome_file = "report" e una variabile estensione = ".txt". Combina queste due variabili per creare il nome completo del file e assegnarlo a file_completo. Stampa file_completo.

nome_file = "report"
estensione = ".txt"
file_completo = nome_file + estensione

print(f'il file completo e: {file_completo}')

#Esercizio 13: Aggiornamento di Variabili con Operatori Compositi
#Dichiara una variabile conto = 100. Aggiungi 50 a conto usando un operatore di assegnazione composto (+=). Poi, sottrai 20 da conto usando un operatore di assegnazione composto (-=). Stampa il valore finale di conto.

conto = 100
conto += 50
conto -= 20

print(f'il conto finale e: {conto}')

#Esercizio 14: Variabili per Contatori
#Dichiara una variabile contatore_articoli = 0. Incrementa il contatore di 1 per tre volte successive. Stampa il valore finale del contatore.

contatore_articoli = 0

while contatore_articoli >= 3:
contatore_articoli += 1
print(f'il valore finale del contatore del articolo e: {contatore_articoli}')

#Esercizio 15: Assegnazione di Stringhe Vuote
#Dichiara una variabile risposta_utente e assegnale una stringa vuota (""). Stampa il valore della variabile e la sua lunghezza.

risposta_utente = ''

print(f'la risposta del utente e: {risposta_utente} la lunghezza della risposta e: {len(risposta_utente)}')

#Esercizio 16: Variabili e Booleani in Operazioni Logiche
#Dichiara due variabili booleane: condizione1 = True e condizione2 = False. Assegna il risultato di condizione1 AND condizione2 a una variabile risultato_and e il risultato di condizione1 OR condizione2 a risultato_or. Stampa entrambi i risultati.

condizione1 = True
condizione2 = False
risultato_and = condizione1 AND condizione2
risultato_or = condizione1 OR condizione2

print(f'ecco il risultato del AND: {risultato_and}')
print(f'ecco il risultato del OR: {risultato_or}')


#Esercizio 18: Variabili e Assegnazione di Risultati di Funzioni
#Dichiara una variabile lunghezza_parola = len("Python"). Stampa il valore di lunghezza_parola.

lunghezza_parola = len("Python")

print(f'ecco il risultato della lunghezza della parola: {lunghezza_parola}')

#Esercizio 19: Ridefinizione del Tipo di una Variabile
#Dichiara una variabile test = 10 (un intero). Successivamente, ri-assegna alla stessa variabile test il valore "Hello" (una stringa). Stampa il valore e il tipo di test dopo ogni assegnazione.

test = 10
print(f'ecco il tipo originale della variabile (test) e: {type(test)}')

test = 'Hello'
print(f'ecco il tipo della variabile (test) ri-assegnata e: {type(test)}')

#Esercizio 20: Variabili con Nomi Lunghi e Descrittivi
#Dichiara una variabile chiamata numero_di_tentativi_rimanenti e assegnale il valore 3. Diminuisci questo valore di 1. Stampa il valore finale.

numero_di_tentativi_rimanenti = 3 
numero_di_tentativi_rimanenti -= 1

print(f'ecco il valore finale della variabile e: {numero_di_tentativi_rimanenti}')

#Esercizio 21: Variabili e Stampa Formattata
#Dichiara una variabile prodotto = "Laptop" e una variabile prezzo = 1200.50. Stampa una frase utilizzando queste variabili e le f-string, ad esempio: "Il [prodotto] costa $[prezzo]."

prodotto = "Laptop"
prezzo = 1200.50

print(f'Il {prodotto} costa {prezzo} €.')

#Esercizio 22: Assegnazione Multipla e Indipendenza
#Dichiara due variabili valore_iniziale_a = 5 e valore_iniziale_b = 5. Cambia valore_iniziale_a a 10. Stampa entrambi i valori per dimostrare che sono indipendenti.

valore_iniziale_a = 5
valore_iniziale_b = 5
valore_iniziale_a = 10

print(f'il valore della variabile e: {valore_iniziale_a}')
print(f'il valore della variabile e: {valore_iniziale_b}')

#Esercizio 23: Variabili e Input Utente
#Chiedi all'utente di inserire il suo piatto preferito e assegna la risposta a una variabile piatto_preferito. Stampa la variabile.

piatto_preferito = str(input('inserisci il tuo piato preferito: '))

print(f'ecco il tuo piato preferito e: {piatto_preferito}')

#Esercizio 24: Variabili per Contenere Risultati Logici
#Dichiara eta_minima = 18 e mia_eta = 20. Assegna il risultato del confronto mia_eta >= eta_minima a una variabile booleana posso_votare. Stampa il valore di posso_votare.

eta_minima = 18
mia_eta = 20

if mia_eta >= eta_minima: 
posso_votare = True
print(f'posso votare: {posso_votare}')
else:
print(f'non posso votare')

#Esercizio 25: Variabili Temporanee per Scambio di Valori (Metodo Tradizionale)
#Dichiara num1 = 50 e num2 = 100. Scambia i loro valori utilizzando una variabile temporanea (ad esempio temp). Stampa i valori di num1 e num2 dopo lo scambio.

num1 = 50
num2 = 100
temp = num1
num1 = num2
num2 = temp

print(f'il valore della prima variabile e: {num1}')
print(f'il valore della prima variabile e: {num2}')

#Esercizio 26: Variabili e Operatori di Concatenazione
#Dichiara prefisso = "http://" e dominio = "esempio.com". Combina queste due stringhe per formare un URL completo e assegnalo a una variabile url_sito. Stampa url_sito.

prefisso = "http://"
dominio = "esempio.com"
url_sito = prefisso + dominio

print(f'ecco l URL completo del sito: {url_sito}')

#Esercizio 27: Variabili e Proprietà Immutabili delle Stringhe
#Dichiara una variabile stringa_originale = "programma". Tenta di modificare il primo carattere di stringa_originale a 'P' direttamente (es. stringa_originale[0] = 'P'). Osserva l'errore che si verifica. Poi, crea una nuova stringa con la modifica e assegnale a nuova_stringa. Stampa nuova_stringa.

stringa_originale = "programma"
stringa_originale[0] = 'P'
nuova_stringa = list(stringa_originale)
nuova_stringa[0] = 'P'

print(f'ecco la nuova stringa: {nuova_stringa}')

#Esercizio 28: Variabili e Utilizzo in Condizioni (Semplice)
#Dichiara una variabile soglia = 100. Dichiara valore_attuale = 120. Senza usare if, pensa a come un operatore di confronto (>) e l'assegnazione a una variabile booleana potrebbero indicare se valore_attuale supera la soglia. Stampa il risultato.

soglia = 100
valore_attuale = 120
supera = valore_attuale > soglia

print(f'il valore attuale supera la soglia: {supera}')


#Esercizio 29: Variabili Globali vs Locali (Concetto Base)
#Definisci una variabile global_var = "Sono globale". Poi, crea una funzione semplice che definisca al suo interno una variabile local_var = "Sono locale" e la stampi. Fuori dalla funzione, tenta di stampare global_var e local_var. Osserva quale viene stampata e quale no (per local_var si aspetta un errore).

global_var = "Sono globale"

def stampa():
local_var = "Sono locale"

print(stampa())

#Esercizio 30: Variabili con None
#Dichiara una variabile risultato_ricerca e assegnale il valore speciale None. Stampa il valore e il tipo di risultato_ricerca.

risultato_ricerca = None

print(f'il tipo della variabile: {type(risultato_ricerca)}')
print(f'il valore della variabile: {risultato_ricerca}')