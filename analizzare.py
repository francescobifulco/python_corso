"""Analizzatore di Testo Semplice (Simple Text Analyzer)
Un programma che prende un testo in input e fornisce alcune statistiche.
Concetti Utilizzati:
Stringhe: Manipolazione di stringhe (metodi lower(), split(), count()).
Collezioni: Un dizionario per contare le occorrenze delle parole. Liste per parole uniche.
Funzioni: Per ogni analisi specifica (es. contare parole, contare vocali, trovare la parola più lunga).
Gestione File: Leggere il testo da un file di input (es. testo.txt).
Moduli: Potresti usare re (espressioni regolari) per una pulizia più avanzata del testo (opzionale, per sfidarti).
Funzionalità:
Conta Parole: Conta il numero totale di parole nel testo.
Conta Caratteri: Conta il numero totale di caratteri (esclusi spazi).
Conta Vocali/Consonanti: Conta il numero di vocali e consonanti.
Frequenza Parole: Mostra la frequenza di ogni parola nel testo.
Parola Più Lunga/Corta: Trova la parola più lunga e la più corta."""

class Analizzatore:
    testo = """Buchi Neri: Un Viaggio nel Mistero dello Spazio
Ibuchi neri sono tra i fenomeni più affascinanti e misteriosi 
dell'universo. Immagina di comprimere una quantità enorme di 
materia in uno spazio estremamente piccolo. Questo è, in 
sostanza, un buco nero. Si tratta di una regione dello spazio 
in cui la gravità è così forte che nulla, nemmeno la luce, 
può sfuggire dalla sua presa. Questo accade quando una stella 
massiccia esaurisce il suo combustibile e collassa sotto il 
suo stesso peso. Una volta formato, il buco nero diventa 
invisibile, ma la sua presenza può essere rilevata grazie agli 
effetti che ha sull'ambiente circostante, influenzando il 
movimento delle stelle vicine o emettendo raggi X quando 
ingloba materia. Studiare i buchi neri ci aiuta a comprendere 
meglio le leggi della fisica e la natura stessa dell'universo."""
    def conta_parola(self):
        lista_testo = Analizzatore.testo.split()
        print(len(lista_testo))
    def conta_carattere(self):
        lista_caratere = list(Analizzatore.testo)
        print(lista_caratere.count(len(lista_caratere)))

analizzi = Analizzatore()
analizzi.conta_parola()
analizzi.conta_carattere()