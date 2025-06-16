#Progetto 1: Gestore di Contatti Semplice
"""Obiettivo: Creare un'applicazione da console per 
gestire una lista di contatti (nome, telefono, email) 
salvandoli in un file JSON.
Funzionalità Richieste:

Aggiungi Contatto: Permettere all'utente di inserire nome, 
telefono ed email per un nuovo contatto.
Visualizza Contatti: Mostrare tutti i contatti salvati in 
un formato leggibile.
Salva Contatti: Salvare l'elenco dei contatti in un file 
JSON (contatti.json).
Carica Contatti: Caricare l'elenco dei contatti dal file 
JSON all'avvio del programma.
Menu Interattivo: Un menu che permetta all'utente di 
scegliere tra le opzioni (aggiungi, visualizza, esci).
Concetti Python Coinvolti:

Collezioni: Lista di dizionari (ogni dizionario 
rappresenta un contatto).
JSON: Modulo json per serializzare/deserializzare dati 
Python in/da JSON.
Funzioni: Per incapsulare le logiche di aggiunta, 
visualizzazione, caricamento e salvataggio.
Gestione File: open(), with open(...), read(), write(), 
json.dump(), json.load().
Strutture di Controllo: while per il menu, if/elif/else 
per la scelta delle opzioni.
Suggerimenti per l'Implementazione:

Definisci una lista vuota rubrica = [] all'inizio del tuo 
script.
Crea una funzione carica_contatti() che tenta di aprire 
contatti.json in modalità lettura ('r'). Usa un blocco 
try-except FileNotFoundError per gestire il caso in cui il 
file non esista ancora (in tal caso, restituisci una lista 
vuota). Usa json.load().
Crea una funzione salva_contatti(rubrica) che apra 
contatti.json in modalità scrittura ('w') e usi 
json.dump(rubrica, file, indent=4).
Crea una funzione aggiungi_contatto(rubrica) che chieda 
all'utente i dettagli e crei un dizionario, aggiungendolo 
poi alla rubrica.
Crea una funzione visualizza_contatti(rubrica) che itera 
sulla rubrica e stampa ogni contatto in modo formattato.
Nel tuo ciclo principale (menu), chiama carica_contatti() 
all'inizio e salva_contatti() quando l'utente sceglie di 
uscire."""

import json
import carica

rubrica = []
while True:
    aggiu_conta = input("aggiungi un nuovo contatto per aggiunre un conttat premi 'invio' per uscire premi 'esci': ")
    if aggiu_conta == "esci":
        break
    elif aggiu_conta == "invio":
        
    