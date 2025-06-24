"""Esercizio 2: Input Utente e Conversione di Tipo
Obiettivo: Ottenere dati dall'utente e convertirli nel tipo appropriato per le operazioni.

Chiedi all'utente di inserire il suo nome e memorizzalo in una variabile nome_utente.
Chiedi all'utente di inserire la sua età e memorizzala in una variabile eta_utente. Assicurati che sia un numero intero.
Chiedi all'utente di inserire il suo reddito annuale e memorizzalo in una variabile reddito_utente. Assicurati che sia un numero decimale (float).
Stampa un messaggio che riepiloga le informazioni inserite, ad esempio: "Ciao [NomeUtente]! Hai [EtàUtente] anni e il tuo reddito annuale è di [RedditoUtente] euro."
Calcola e stampa il reddito mensile dell'utente (reddito annuale diviso 12)."""

nome_utente = str(input("insersci un nome: "))
eta_utente = int(input("inerisci eta: "))
reddito_utente = float(input("quale il tuo redito: "))

print(f"Ciao {nome_utente}! Hai {eta_utente} anni e il tuo reddito annuale è di {reddito_utente} euro.")

calcolo_redito = reddito_utente / 12
print(f"il tuo redito annuale e di {calcolo_redito}")