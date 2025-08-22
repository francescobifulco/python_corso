#Esercizio 1: Ottenere e Stampare un nome
#Scrivi un programma che chieda all'utente di inserire il proprio nome e poi stampi un messaggio di benvenuto utilizzando il nome inserito

nome = input('inserire il tuo nome: ')

print(f'ti do il benvenuto {nome}')

#esercizio 2: Ottenere e Sommare Due Numeri
#Chiedi all'utente di iserire due numeri interi. Coneverti gli input in numeri e stampare la loro somma.

num1 = int(input('inserire un numero: '))
num2 = int(input('inserire un numero: '))
somma = num1 + num2

print(f'somma tra {num1} e {num2}: {somma}')

#Esercizio 3: Ottenere una Frase e Contare i Caratteri
#Richiedi all'utente di digitare una frase. Stampare la frase inserita e il numero totale di caratteri che contiene

frase = str(input('inserire una frase: '))

print(f'la frase inserita e: {frase} e contiene {len(frase)} di caratteri}')

#Esercizio 4: input Booleano Semplice
#Chiedi all'utente "Sei maggiorenne? (si/no)". Se la risposta è "si", stampare "Benvenuto!", altrimenti stampa "Accesso negato".

scelta = str(input('Sei maggiorenne? (si/no)')).lower()

if scelta == 'si':
print('Benvenuto!')
else:
print('Accesso negato')

#Esercizio 5: Clacola dell'Area del Rettangolo
#Chiedi all'utente la lunghezza e la larghezza di un rettangolo. Calcola e stampa l'area.

lunghezza = float(input('inserire la lunghezza del rettangolo: '))
larghezza = float(input('inserire la larghezza del rettangolo: '))
area = larghezza * lunghezza

print(f'area del rettangolo e: {area:.2f}')

#Esercizio 6: Conevertire un input in virgola Mobile
#Richiedi all'utente di inserire un prezzo (es. 19.99). Converti l'input in un numero decimale e stampalo formattatto con due cifre decimali.

numero = input('inserire un numero: ')

print(f'il numero {numero} in formato decimale: {numero:.2f}')

#Esercizio 8: Validazione Semplice dell'input
#Chiedi all'utente di inserire una password. Se la password è "segreta123", stampa "Accesso consentito", altrimenti stampa "Password errata". 

password = input('inserire la password: ').lower()

if password == 'segreta123'
print('Accesso consentito')
else: 
print('Password errata')

#Esercizio 9: Ottenere più Informazioni Personali
#Chiedi all'utente il suo nome, cognome ed eta. Stampa tutte le informazioni su una signola riga. 

nome = str(input('inserire il suo nome: '))
cognome = str(input('inserire il suo cognome: '))
eta = int(input('inserire la tua eta: '))

print(f'benvenuto {nome} {cognome} e hai {eta} anni')

#Esercizio 10: Input con Numeri Negativi
#Chiedi all'utente di inserire una temperatura. Stampa un messaggio che indicho se la temperatura è sopra o sotto zero.

temperatura = input('inserire la temperatura: ')

if temperatura < 0:
print(f'la temperatura {temperatura} si trova sotto lo 0')
else:
print(f'la temperatura si trova sopra la 0')

#Esercizio 11: Calcolo Semplice dell'Età
#Chiedi all'utente il suo anno di nascita e l'anno corrente. Calcola e stampa la sua età approssimativa.

anno_nascita = int(input('inserisci il tuo anno di nascita: '))
anno_corrente = int(input('inserisci anno corrente: '))
eta_utente = anno_corrente - anno_nascita

print(f'la tua eta: {eta_utente}')

#Esercizio 12: Input con Spazi
#Chiedi all'utente di inserire una frase che contenga degli spazi. Stampa la frase e poi stampa la stessa frase senza gli spazi.

frase = input('inserisci una frase: ')
frase_senza_spazi = frase.lstrip()

print(f'la frase originale: {frase}')
print(f'la frase senza spazi: {frase_senza_spazi}')

#Esercizio 13: Verifica di un Numero Pari/Dispari
#Richiedi all'utente di inserire un numero intero. Stampa un messaggio che indichi se il numero è pari o dispari.

numero = int(input('inserisci un numero: '))

if numero % 2 == 0:
print(f'il numero {numero} e pari')
else:
print(f'il numero {numero} e dispari')

#Esercizio 14: Input di un Colore Preferito
#Chiedi all'utente qual è il suo colore preferito. Stampa una frase che incorpori il colore scelto, ad esempio: "Il tuo colore preferito è [colore]."

colore = str(input('inserire il tuo colore preferito: '))

print(f'Il tuo colore preferito è {colore}')

#Esercizio 15: Input di Conferma
#Poni all'utente una domanda che richiede una risposta "sì" o "no" (o "S" o "N"). Stampa un messaggio diverso a seconda della risposta.

domanda = str(input('hai mangiato (s/n)').lower())

if domanda == 's':
print('buon apetito')
else:
print('mangia qualcosa')

#Esercizio 16: Input per un Messaggio Personalizzato
#Chiedi all'utente di inserire un messaggio. Stampa il messaggio racchiuso tra due righe di asterischi (es. ********** \n * Messaggio * \n **********).

messaggio = str(input('inserire un messaggio: '))
print(f'********** \n * {messaggio} * \n **********')

#Esercizio 17: Calcolo del Quadrato di un Numero
#Chiedi all'utente di inserire un numero. Stampa il quadrato di quel numero.

quadrato = int(input('inserire un numero: '))

print(f'il numero {numero} il suo quadrato {quadrato}')

#Esercizio 18: Input di una Data Semplice
#Chiedi all'utente di inserire il giorno, il mese e l'anno come numeri separati. Stampa la data nel formato "DD/MM/AAAA".

while True:
giorno = int(input('inserisci un numero tra 1 a 31'))
mese = int(input('inserisci un numero tra 1 a 12'))
anno = int(input('inserisci un numero tra 1900 a 2025'))

if giorno >= 1 and giorno <= 31:
print('inserimeto corretto')
else:
print('numero non valido')

if mese >= 1 and mese <= 12:
print('inserimeto corretto')
else:
print('numero non valido')

if anno >= 1900 and anno <= 2025:
print('inserimeto corretto')
else:
print('numero non valido')

print(f'la data e: {giorno}/{mese}/{anno}')

#Esercizio 19: Concatenazione di Nome e Cognome
#Chiedi all'utente il suo nome e poi il suo cognome. Stampa il nome completo.

nome = str(input('inserisci il tuo nome: '))
cognome = str(input('inserisci il tuo cognome: '))

print(f'il tuo nome completo e: {nome} {cognome}')

#Esercizio 20: Input e Conversione a Virgola Mobile (Gestione Errori Semplice)
#Chiedi all'utente di inserire un numero decimale. Tenta di convertirlo in float. Se l'utente inserisce qualcosa che non è un numero decimale valido, stampa un messaggio di errore anziché un crash.

try:
numero_decimale = float(input('inserisci un numero: '))
print(f'il numero che hai inserito e: {numero_decimale}')
except ValueError:
print('il numero non e decimale')


#Esercizio 21: Confronto di Stringhe
#Chiedi all'utente di inserire due parole. Stampa un messaggio che indichi se le due parole sono uguali o diverse.

parola1 = str(input('inserisci una parola: '))
parola2 = str(input('inserisci una parola: '))

if parola1 == parola2:
print('sono uguali')
else:
print('non sono uguali')

#Esercizio 22: Input con Conversione a Maiuscolo/Minuscolo
#Chiedi all'utente di inserire una città. Stampa la città inserita in tutto maiuscolo e poi in tutto minuscolo.

citta = str(input('inserisci una citta: '))

print(f'la citta tutto maiuscolo: {citta.lower()}')
print(f'la citta tutto minuscolo: {citta.upper()}')

#Esercizio 23: Calcolo dell'Indice di Massa Corporea (BMI) Semplificato
#Chiedi all'utente il suo peso (in kg) e la sua altezza (in metri). Calcola un BMI semplificato (peso / altezza). Non è richiesta la radice quadrata.

peso = float(input('inserisci il tuo peso: '))
altezza = float(input('inserisci la tua altezza: '))

BMI_semplificato = peso / altezza
BMI_complesso peso / (altezza * altezza)

print(f'BMI semplificato senza la radice quadrata: {BMI_semplificato}')
print(f'BMI complesso con la radice quadrata: {BMI_complesso}')

#Esercizio 24: Input Multiplo con Separatore
#Chiedi all'utente di inserire una serie di numeri separati da una virgola (es. "10,20,30"). Stampa i singoli numeri che hai estratto.

numeri_serie = input('inserisci una serie di numeri separati con la virgola: ')
print(f'la serie di numeri e: {numeri_serie}')

#Esercizio 25: Domanda Sì/No con Risposta Specificata
#Poni una domanda all'utente che abbia come risposte valide solo 'S' o 'N'. Se l'utente inserisce altro, stampa un messaggio di errore e richiedi l'input corretto (senza implementare un loop, solo la stampa dell'errore).

try:

domanda = str(input('hai mangiato (s/n)').lower())

if domanda == 's':
print('buon apetito')
else:
print('mangia qualcosa')
except  :
print('inserimento non valito')

#Esercizio 26: Input Numerico per un Intervallo
#Chiedi all'utente di inserire un numero intero. Stampa un messaggio che indichi se il numero è compreso tra 10 e 20 (inclusi).

numero = int(input('inserisci un numero: '))

if numero >= 10 and numero <= 20:
print('il numero comprende tra 10 e 20')

#Esercizio 27: Stampa di Pattern con Input
#Chiedi all'utente di inserire un carattere e un numero intero. Stampa quel carattere ripetuto il numero di volte indicato dall'utente.

numero = int(input('inserisci un numero: '))
carratere = input('inserisci un carratere: ')

for indice in numero:
print(f' il numero di volete ripetuto {indice} il carratere {carattere}')

#Esercizio 28: Input e Lunghezza della Parola
#Chiedi all'utente di inserire una parola. Stampa la parola e la sua lunghezza.

parola = str(input('inserisci una parola: '))

print(f'la lunghezza della parola {parola} e {len(parola)}')

#Esercizio 29: Domanda Personalizzata
#Chiedi all'utente il suo animale domestico preferito e il suo nome. Stampa una frase che usi entrambe le informazioni (es. "Il tuo [animale] si chiama [nome].").

animale = str(input('inserisci il tuo animale: '))
nome_del_animale = str(input('inserisci il nome del tuo animale: '))

print(f'Il tuo {animale} si chiama {nome}.')

#Esercizio 30: Input Numerico per Calcolo Semplice
#Chiedi all'utente un numero di giorni. Converti questo numero in settimane e giorni rimanenti, stampando il risultato. (es. 10 giorni sono 1 settimana e 3 giorni).

 