"""Esercizio 1: Variabili, Tipi di Dati e Operazioni Base
Obiettivo: Comprendere come dichiarare variabili, assegnare tipi di dati diversi ed eseguire operazioni aritmetiche fondamentali.

Crea una variabile numero_intero e assegna un valore numerico intero a tua scelta.
Crea una variabile numero_decimale e assegna un valore numerico decimale (float).
Crea una variabile testo e assegna una frase breve come stringa.
Crea una variabile booleano_vero e assegna il valore booleano True.
Stampa il tipo di dato di ciascuna di queste variabili usando type().
Esegui le seguenti operazioni usando numero_intero e numero_decimale e stampa il risultato di ciascuna:
Somma
Sottrazione
Moltiplicazione
Divisione (normale, con il risultato float)
Divisione intera (solo la parte intera del risultato)
Resto della divisione (modulo)
Elevamento a potenza (es. numero_intero elevato a 2)"""

numero_intero = 10
numero_decimale = 20.5
testo = "ciao a tutti come state"
booleano_vero = True

print(type(numero_intero))
print(type(numero_decimale))
print(type(testo))
print(type(booleano_vero))

somma = numero_intero + numero_decimale
sotrazione = numero_intero - numero_decimale
moltiplicazione = numero_intero * numero_decimale
divisione = numero_intero / numero_decimale
quoziente = numero_intero % numero_decimale
potenza = numero_intero**2
divisione_intero = numero_intero // numero_decimale

print(f"la somma e {somma}, la moltiplicazione e {moltiplicazione}, la sotrazione e {sotrazione}, la divisione e {divisione}, il resto e {quoziente} la divisione intera e {divisione_intero}")