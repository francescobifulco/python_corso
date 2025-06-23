"""Esercizio 2: Input/Output di Base e Conversione di Tipo
Obiettivo: Ottenere input dall'utente, eseguire conversioni di tipo e stampare output formattato.

Chiedi all'utente il suo nome e memorizzalo in una variabile.
Chiedi all'utente il suo anno di nascita.
Calcola la sua età attuale (supponendo che l'anno corrente sia il 2025).
Stampa un messaggio come: "Ciao [Nome]! Hai [Età] anni."""

nome = str(input("inserisci il tuo nome: "))
eta = int(input("inserisci anno di nascita: "))

anno_attuale = 2025
anno = anno_attuale - eta 

print(f"Ciao {nome}! Hai {anno} anni.")