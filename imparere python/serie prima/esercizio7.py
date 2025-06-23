"""Esercizio 7: Dizionari
Obiettivo: Lavorare con coppie chiave-valore usando i dizionari.

Crea un dizionario che rappresenta una persona con chiavi come nome, eta e citta.
Accedi e stampa l'età della persona.
Aggiungi una nuova coppia chiave-valore, ad esempio occupazione.
Aggiorna il valore di una chiave esistente, ad esempio cambia la citta.
Itera e stampa tutte le coppie chiave-valore nel dizionario."""

dizionario = {"nome":"franco", "citta":"napoli", "eta": 24}
print(f"eta della persona e: {dizionario['eta']}")

dizionario["occupazione"] = "Programmatore"
dizionario["citta"] = "torino"

for chiave,valore in dizionario.items():
    print(chiave, valore)