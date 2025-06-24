"""Esercizio 5: Dizionari (Collezioni)
Obiettivo: Lavorare con i dizionari, una collezione di coppie chiave-valore.

Crea un dizionario chiamato studente con le seguenti informazioni:
nome: Il tuo nome
età: La tua età
corso: "Informatica"
media: 8.5
Accedi e stampa il corso dello studente.
Aggiorna l'età dello studente a un nuovo valore (es. +1 anno).
Aggiungi una nuova coppia chiave-valore al dizionario: città con il nome della tua città.
Rimuovi la chiave media dal dizionario.
Stampa tutte le chiavi del dizionario.
Stampa tutti i valori del dizionario.
Itera sul dizionario e stampa ogni coppia chiave-valore in un formato leggibile (es. "Chiave: [chiave], Valore: [valore]")."""

studente = {"nome":"franco", "eta":24, "corso":"Informatica", "media":8.5}

print(f"il corso dello studente e: {studente['corso']}")
studente["eta"] = 25
studente["citta"] = "napoli"
studente.pop("media")

print("\n----CHIAVI----")
for chiave in studente.keys():
    print(f"le chiave: {chiave}")

print("\n----VALORI----")  
for valore in studente.values():
    print(f"i valori: {valore}")

print("\n----TUTTI----")
for chiave,valore in studente.items():
    print(f"Chiave: {chiave}, Valore: {valore}")