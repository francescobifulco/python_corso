"""Esercizio 6: Liste
Obiettivo: Lavorare con le liste, inclusi l'aggiunta, la rimozione e l'iterazione.

Crea una lista dei tuoi frutti preferiti.
Aggiungi un nuovo frutto alla lista.
Rimuovi un frutto dalla lista.
Stampa ogni frutto nella lista usando un ciclo for.
Verifica se un frutto specifico è nella lista e stampa un messaggio di conseguenza."""

lista_frutta = ["mela","banana","pera"]
lista_frutta.append("anguria")
lista_frutta.remove("mela")

for frutto in lista_frutta:
    print(frutto)

if "pera" in lista_frutta:
    print("ci sta")
    

