

#Esercizio 9: Stampa Multilinea
#Stampa un piccolo paragrafo di almeno tre righe utilizzando un'unica istruzione print().

print('fare generare un praragrafo di tre righe')

#Esercizio 10: Stampa di Output di una Funzione
#Definisci una semplice funzione che restituisce una stringa, ad esempio"Programmazione in Python". Chiama questa funzione e stampa il valore che restituisce.

def stampa_funzione():
return 'Programmazione in Python'

stampa_funzione()

#Esercizio 11: Stampa di Numeri con Allineamento
#Stampa i numeri da 1 a 3, ciascuno su una nuova riga, allineandoli a destra su un campo di 5 caratteri (es. "    1").

for numeri in range(1,4):
print(f'     {numeri}')

#Esercizio 12: Stampa con Separatore e Fine Riga Vuoti
#Stampa le parole "uno", "due", "tre" sulla stessa riga, separate da uno spazio, ma assicurati che non ci sia un carattere di nuova riga alla fine dell'output.

print('uno due tre')

#Esercizio 13: Stampa del Contenuto di una Lista
#Data una lista di colori colori = ["rosso", "verde", "blu"], stampa ogni colore su una riga separata.

colori = ["rosso", "verde", "blu"]
for indice in colori:
print(f'il colore che si trova nella lista: {indice}')

#Esercizio 14: Stampa di una Stringa Invertita
#Definisci una stringa testo = "Python". Stampa la stringa invertita.

testo = "Python"
print(f'il testo invertito: {testo[::-1]}')

#Esercizio 15: Stampa con Ripetizione di Caratteri
#Stampa una riga di 20 asterischi (*).

print('*********************')

#Esercizio 16: Stampa di una Tabella Semplice
#Stampa una piccola tabella con due colonne (Nome, Età) e due righe di dati, allineando il testo per creare un aspetto ordinato.
#Esempio di output desiderato:
#Nome    Età
#Alice   30
#Bob     25

dizionario = {'Nome': ['Alice','Bob'],
              'Età': [30,25]}
print(f'{dizionario['Nome']}    {dizionario['Età']}')
for valori in dizionario.values()
print(f'{valore}    {valore}')

#Esercizio 17: Stampa con Precisione Decimale
#Definisci una variabile pi = 3.14159265. Stampa il valore di pi con una precisione di due cifre decimali (es. 3.14).

pi = 3.14159265
print(f'il valore PI greco: {pi:.2}')

#Esercizio 18: Stampa Condizionale
#Definisci una variabile punteggio = 75. Se il punteggio è maggiore o uguale a 60, stampa "Promosso!", altrimenti stampa "Riprovato.".

punteggio = 75
if punteggio >= 60:
print('Promosso')
else:
print('Riprovato')

#Esercizio 19: Stampa di Caratteri Unicode
#Stampa il simbolo del copyright: ©.

print('copyright ©')

#Esercizio 20: Stampa di Messaggi di Errore
#Simula un messaggio di errore stampando una stringa che inizi con "ERRORE:" seguita da una descrizione del problema (es. "ERRORE: File non trovato.").

print('ERRORE: File non trovato.')

#Esercizio 21: Stampa di Variabili Booleane
#Definisci una variabile is_attivo = True e una variabile is_completo = False. Stampa il valore di entrambe le variabili.

is_attivo = True
is_completo = False
print(f'il valore di is_attivo e: {is_attivo}, il valore di is_completo e: {is_completo}')

#Esercizio 22: Stampa con Concatenazione di Stringhe
#Definisci tre stringhe: parte1 = "Benvenuto", parte2 = "nel", parte3 = "mondo Python". Stampa una singola frase unendo queste tre stringhe.

parte1 = "Benvenuto"
parte2 = "nel"
parte3 = "mondo Python"
print(f'la frase e composto e: {parte1} {parte2} {parte3}')

#Esercizio 23: Stampa del Tipo di una Variabile
#Definisci una variabile valore = 123. Stampa il tipo di questa variabile.

valore = 123
print(f'il tipo della variabile {valore} e: {type(valore)}')

#Esercizio 24: Stampa di una Linea di Separazione
#Stampa una linea di 30 trattini (-) per separare visivamente diverse sezioni dell'output.

print('------------------------------')
print('separatore delle sezioni dell output')
print('------------------------------')
print('ciao momdo')
print('------------------------------')

#Esercizio 25: Stampa di una Stringa con Indice
#Data la stringa parola = "programmazione", stampa solo i primi 5 caratteri.

parola = "programmazione"
print(f'i primi 5 caratteri della parola {parola} e: {parola[:4]}')

#Esercizio 26: Stampa di Percentuali Formattate
#Definisci una variabile percentuale_completamento = 0.85. Stampa questo valore come una percentuale formattata, ad esempio "Completato al 85.00%".

percentuale_completamento = 0.85
print(f'la percentuale e: {percentuale_completamento:.2f}')

#Esercizio 27: Stampa con Spazi Iniziali/Finali
#Data la stringa frase_spazi = "   Testo con spazi   ", stampa la stringa senza spazi iniziali e finali.

frase_spazi = "   Testo con spazi   "
print(f'la frase senza spazi: {frase_spazi.lstrip()}')

#Esercizio 28: Stampa di Elementi di un Dizionario
#Definisci un dizionario dettagli = {"nome": "Luca", "citta": "Roma"}. Stampa una frase che includa sia il nome che la città, ad esempio: "Luca vive a Roma."

dettagli = {"nome": "Luca", 
            "citta": "Roma"}
print(f"{dettagli['Luca']} vive a {dettagli['Roma']}.")

#Esercizio 29: Stampa di un Risultato di Calcolo Scientifico
#Stampa il risultato di 10 ** 3 (dieci elevato alla terza) in una frase descrittiva.

print(f'il risultato di 10 elevato alla terza e: {10 ** 3}')

#Esercizio 30: Stampa di una "Cornice" Semplice
#Stampa una "cornice" di asterischi intorno alla parola "BENVENUTO".
'''Esempio di output desiderato:
*********
*BENVENUTO*
*********
'''

print('*********')
print('*BENVENUTO*')
print('*********')