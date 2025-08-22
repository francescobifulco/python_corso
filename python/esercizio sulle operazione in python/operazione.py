#Esercizio 1: Addizione Semplice
#Definisci due variabili intere, a = 15 e b = 7. Calcola la loro somma e stampala.

a = 15 
b = 7
somma = a + b

print(f'la somma tra {a} e {b}: {somma}')

#Esercizio 2: Sottrazione di Numeri Decimali
#Definisci due variabili decimali, prezzo_originale = 49.99 e sconto = 12.50. Calcola il prezzo finale dopo lo sconto e stampalo.

prezzo_originale = 49.99
sconto = 12.50
prezzo_scontato = sconto / 100
prezzo_finale = prezzo_originale - prezzo_scontato

print(f'ecco il prezzo finale di {prezzo_originale}: {prezzo_finale:.2f}')

#Esercizio 3: Moltiplicazione
#Definisci una variabile quantita = 8 e una variabile costo_unitario = 3.50. Calcola il costo totale e stampalo.

quantita = 8
costo_unitario = 3.50
costo_totale = quantita * costo_totale

print(f'il costo finale e: {costo_totale}')

#Esercizio 4: Divisione Intera (Floor Division)
#Definisci due variabili intere, totale_caramelle = 25 e bambini = 4. Calcola quante caramelle riceverà ogni bambino se le dividi equamente, senza pezzi (usa la divisione intera), e stampa il risultato.

totale_caramelle = 25
bambini = 4
caramelle_finali = totale_caramelle / bambini

print(f'ogni bambino riceverà tot caramelle: {caramelle_finali:.2f}')

#Esercizio 5: Resto della Divisione (Modulo)
#Usando le stesse variabili dell'Esercizio 4 (totale_caramelle = 25, bambini = 4), calcola quante caramelle rimarranno dopo averle divise e stampale.

totale_caramelle = 25
bambini = 4
caramelle_rimanenti = totale_caramelle % bambini

print(f'rimangono tot caramelle: {caramelle_rimanenti:.2}')

#Esercizio 6: Potenza
#Definisci una variabile base = 2 e una variabile esponente = 5. Calcola il risultato di base elevato all'esponente e stampalo.

base = 2
esponente = 5
risultato_elebato = base ** esponente

print(f'il risultato del {base} elevato a {esponente} e: {risultato_elebato}')

#Esercizio 7: Ordine delle Operazioni (PEMDAS/BODMAS)
#Definisci le variabili x = 10, y = 3, z = 2. Calcola il risultato dell'espressione x + y * z e stampalo.

x = 10 
y = 3
z = 2
espressione = x + y * z

print(f'il risultato dell espressione e: {espressione}')

#Esercizio 8: Parentesi nelle Operazioni
#Usando le stesse variabili dell'Esercizio 7, calcola il risultato dell'espressione (x + y) * z e stampalo. Confronta il risultato con l'esercizio precedente.

x = 10 
y = 3
z = 2
espressione = (x + y) * z

print(f'il risultato dell espressione e: {espressione}')

#Esercizio 9: Divisione Decimale Standard
#Definisci due variabili num1 = 17 e num2 = 4. Esegui una divisione che restituisca un risultato con la parte decimale e stampalo.

num1 = 17
num2 = 4
## devi finire

#Esercizio 10: Combinazione di Operazioni
#Definisci tre variabili valore1 = 20, valore2 = 5, valore3 = 3. Calcola il risultato di (valore1 / valore2) + (valore3 ** 2) e stampalo.

valore1 = 20 
valore2 = 5
valore3 = 3
risultato = (valore1 / valore2) + (valore3 ** 2)

print(f'il risultato del espresione e: {risultato:.2f}')

#Esercizio 11: Calcolo della Media Aritmetica
#Definisci tre variabili, num1 = 12, num2 = 18, num3 = 24. Calcola la loro media aritmetica e stampala.

num1 = 12
num2 = 18
num3 = 24
somma = num1 + num2 + num3
media = somma / 3

print(f'la media dei 3 numeri e: {media}')

#Esercizio 12: Elevamento a Potenza con Numeri Decimali
#Definisci una variabile base = 2.5 e una variabile esponente = 2. Calcola il quadrato della base e stampalo.

base = 2.5
esponente = 2
risultato_elebato = base ** esponente

print(f'il risultato del {base} elevato a {esponente} e: {risultato_elebato}')

#Esercizio 13: Operazioni Miste e Conversione di Tipo
#Definisci una variabile numero_str = "7". Convertila in un numero intero, aggiungi 3 e poi moltiplica il risultato per 2. Stampa il valore finale.

numero_str = "7"
numero_int = int(numero_str)
aggiungi = numero_int + 3
moltiplica = aggiungi * 2

print(f'il risultato finale del numero {numero_int} e: {moltiplica}')

#Esercizio 14: Calcolo del Perimetro del Quadrato
#Definisci una variabile lato = 9. Calcola il perimetro del quadrato e stampalo.

lato = 9
perimetro = lato * 4

print(f'il perimetro del quadrato e: {perimetro}')

#Esercizio 15: Operazioni con Numeri Negativi
#Definisci due variabili temp_max = 5 e temp_min = -3. Calcola la differenza tra la temperatura massima e quella minima e stampala.

temp_max = 5
temp_min = -3
differenza = temp_max - temp_min

print(f'la differenza tra {temp_max} e {temp_min}: {differenza}')

#Esercizio 16: Resto con Numeri Più Grandi
#Definisci due variabili big_num = 150 e small_num = 13. Calcola il resto della divisione di big_num per small_num e stampalo.

big_num = 150
small_num = 13
resto_divisione = big_num % small_num

print(f'il resto della divisione e: {resto_divisione:.2f}')

#Esercizio 17: Calcolo Semplice dell'Interesse
#Definisci capitale = 1000, tasso = 0.05 e anni = 1. Calcola l'interesse semplice (capitale * tasso * anni) e stampalo.

capitale = 1000
tasso = 0.05
anni = 1
interesse = capitale * tasso * anni

print(f'interesse del capitale {capitale} e: {interesse:.2f}')

#Esercizio 18: Divisione per Zero (Esempio di Errore)
#Crea un'espressione che tenti di dividere un numero per zero. Osserva cosa succede (non devi gestire l'errore, solo provocarlo).

divisione_errore = 0 / 2
print(f'questa divisione crea un eccezione: {divisione_errore}')

#Esercizio 19: Operazioni con Ordine Inverso
#Definisci a = 20, b = 4, c = 2. Calcola il risultato di a / b - c e stampalo.

a = 20
b = 4
c = 2
operazione = a / b - c

print(f'il risultato di questo operazione: {operazione}')

#Esercizio 20: Combinazione di Divisione Intera e Modulo
#Definisci minuti_totali = 130. Calcola quante ore intere sono e quanti minuti rimangono. Stampa entrambi i risultati.

minuti_totali = 130
ore_totali =  

#Esercizio 21: Conversione Secondi in Ore, Minuti, Secondi
#Definisci una variabile secondi_totali = 3665. Calcola quante ore, minuti e secondi rimangono da questo totale. Stampa tutti e tre i risultati.

secondi_totali = 3665


#Esercizio 22: Calcolo della Percentuale
#Definisci parte = 30 e totale = 200. Calcola che percentuale parte rappresenta rispetto a totale. Stampa il risultato come valore decimale.

parte = 30
totale = 200

#Esercizio 23: Media Ponderata Semplice
#Definisci voto1 = 8, peso1 = 2, voto2 = 7, peso2 = 3. Calcola la media ponderata ((voto1 * peso1) + (voto2 * peso2)) / (peso1 + peso2) e stampala.

voto1 = 8
peso1 = 2
voto2 = 7
peso2 = 3
media_ponderata = ((voto1 * peso1) + (voto2 * peso2)) / (peso1 + peso2)

print(f'ecco il risultato della media ponderata: {media_ponderata:.2f}')

#Esercizio 24: Operazioni con Numeri Grandi
#Definisci due numeri interi molto grandi, big_int1 = 123456789 e big_int2 = 987654321. Calcola la loro somma e stampala.

big_int1 = 123456789 
big_int2 = 987654321
big_totate = big_int1 + big_int2

print(f'il totate di due numeri grandi: {big_totate}') 

#Esercizio 25: Arrotondamento Semplice 
#Definisci una variabile numero_decimale = 7.893. Arrotonda questo numero all'intero più vicino e stampalo (senza usare funzioni specifiche di arrotondamento, solo operazioni matematiche se possibile o l'approccio intuitivo della conversione).

numero_decimale = 7.893

print(f'il numero decimale in intero: {numero_decimale}')

#Esercizio 26: Calcolo del Volume di un Cubo
#Definisci la lunghezza del lato di un cubo, lato_cubo = 4. Calcola il volume del cubo (lato * lato * lato o lato ** 3) e stampalo.

lato_cubo = 4
volume_cubo = lato ** 3

print(f'il risultato del volume del cubo e: {volume_cubo}')

#Esercizio 27: Incremento/Decremento Semplice
#Definisci una variabile contatore = 10. Incrementa il suo valore di 1 e poi decrementalo di 2. Stampa il valore finale del contatore.

contatore = 10
incremento = contatore + 1
decremento = incremento - 2

print(f'il risultato del operazione: {decremento}')

#Esercizio 28: Divisione Intera con Numeri Negativi
#Definisci dividendo = -17 e divisore = 5. Esegui una divisione intera (//) e stampa il risultato. Osserva come si comporta Python con i numeri negativi.

dividendo = -17
divisore = 5
operazione = dividendo // dividere

print(operazione)

#Esercizio 29: Calcolo dell'Espressione Complessa
#Definisci a = 5, b = 2, c = 3. Calcola il risultato di (a + b) * c - (a / b) e stampalo.

a = 5 
b = 2
c = 3
risultato = (a + b) * c - (a / b)

print(f'il risultato del operazione: {risultato}')

#Esercizio 30: Verifica di Multipli
#Definisci un numero num = 27. Verifica (tramite l operatore modulo) se questo numero è un multiplo di 3 e stampa un messaggio appropriato (senza usare if/else). Pensa a come l output dell operatore modulo può indicare la divisibilità.

num = 27
risultato = num % 3
