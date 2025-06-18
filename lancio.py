""" Simulatore di Dadi Semplice
Un programma interattivo che simula il lancio di uno o più 
dadi e visualizza il risultato.
Concetti Utilizzati:
Funzioni: Una funzione per simulare il lancio di un singolo 
dado, un'altra per gestire il lancio di più dadi.
Moduli: Il modulo random è fondamentale, in particolare 
random.randint() per simulare il lancio del dado.
Input Utente: Chiedere all'utente quanti dadi lanciare e 
quante facce hanno i dadi (es. D6, D20).
Cicli for: Per lanciare più dadi.
Stringhe: Messaggi di output per i risultati.
Condizioni if/else: Per gestire input utente non validi.
Funzionalità:
Lancia un Dado: Chiedi all'utente il numero di facce del 
dado (es. 6, 20) e simula un lancio, mostrando il risultato.
Lancia Più Dadi: Chiedi all'utente quanti dadi lanciare e il 
numero di facce per ogni dado. Mostra il risultato di ogni 
singolo dado e il totale.
Modalità Ripetuta: Permetti all'utente di continuare a 
lanciare i dadi finché non decide di uscire.
Statistiche Semplici: (Opzionale) Mantieni un conteggio 
delle occorrenze di ogni risultato su più lanci."""

import random

class Lancio:
    def numero_faccie(self):
        facce = input("inserisci il numero di facce: ")
        print(f"il numero di facce e: {facce}")
        return facce
    def singolo(self,facce):
        causuale = random.randint(1, int(facce))
        print(causuale)

dado1 = Lancio()
numero = dado1.numero_faccie()
dado1.singolo(numero)
