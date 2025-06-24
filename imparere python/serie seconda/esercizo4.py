"""Esercizio 4: Liste e Tuple (Collezioni)
Obiettivo: Comprendere e manipolare le liste e le tuple, le due collezioni base di Python.

Crea una lista chiamata numeri_interi contenente almeno 5 numeri interi.
Aggiungi un nuovo numero alla fine della lista.
Rimuovi il terzo elemento dalla lista.
Inserisci il numero 0 all'inizio della lista.
Stampa la lista modificata.
Trova e stampa l'indice del numero 5 (o un numero a tua scelta presente nella lista).
Crea una tupla chiamata colori contenente almeno 3 colori.
Prova ad aggiungere un nuovo colore alla tupla (osserva cosa succede, le tuple sono immutabili!). Scrivi un commento nel codice spiegando il risultato.
Accedi e stampa il secondo elemento della tupla."""

numeri_interi = [1,2,3,4,5]
print(numeri_interi)

numeri_interi.append(6)
print(numeri_interi)

numeri_interi.remove(4)
print(numeri_interi)

numeri_interi.insert(0,0)
print(numeri_interi)

indice = numeri_interi.index(5)
print(indice)

colori = ("blu","verde","rosso")
print(colori[1])