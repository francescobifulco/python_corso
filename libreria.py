""" Gestore di Libreria Base (Basic Library Manager)
Questo progetto ti permette di tenere traccia di un catalogo di libri.

Concetti Utilizzati:
Classi: Crea una classe Libro con attributi come titolo, autore, anno_pubblicazione, disponibile (booleano).
Collezioni: Una lista di oggetti Libro per rappresentare la libreria.
Funzioni: Metodi all'interno della classe Libro (es. mostra_dettagli()) e funzioni esterne per gestire la lista di libri 
(aggiungi, cerca, presta, restituisci).
Gestione File: Salvare e caricare i dati dei libri (potresti usare json o un semplice formato testuale).
Moduli: Potresti usare json per una serializzazione/deserializzazione più semplice degli oggetti.
Funzionalità:
Aggiungi Libro: Crea un nuovo oggetto Libro e aggiungilo alla lista.
Visualizza Tutti i Libri: Mostra i dettagli di tutti i libri.
Cerca Libro: Cerca un libro per titolo o autore.
Presta/Restituisci Libro: Modifica lo stato disponibile di un libro.
Salva/Carica Libreria: Persisti lo stato della libreria su un file.
Consigli per lo Sviluppo:
Inizia Semplice: Non cercare di implementare tutte le funzionalità contemporaneamente. Inizia con la logica base e poi aggiungi 
complessità.
Struttura il Codice: Utilizza funzioni per organizzare il tuo codice e renderlo più leggibile e modulare.
Commenta: Aggiungi commenti per spiegare parti complesse o scelte di design.
Gestione degli Errori: Pensa a cosa succede se l'utente inserisce un input non valido (es. testo invece di un numero) e usa blocchi 
try-except.
Interfaccia Utente Semplice: Inizia con un'interfaccia a riga di comando (CLI).
Testa il Tuo Codice: Esegui il tuo programma frequentemente per assicurarti che funzioni come previsto."""

class Libro:
    libreria = []
    titolo = ""
    autore = ""
    anno_pubblicazione =""
    disonibile = True
    """def __init__(self,titolo, autore, anno_pubblicazione, disponibile):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione
        self.disonibile = disponibile"""
    def aggiungi(self):
         while True:
            self.titolo = input("Aggiungi del libro (per uscire premi 'esci'): ").lower()
            if self.titolo == "esci":
                break
            self.autore = input("Inserisci autore del libro: ")
            self.anno_pubblicazione = input("Inserisci anno di pubblicazione del libro: ")
            self.disonibile = input("Inserisci se il libro e disponibile (s: il libro e disponibile/n: il libro non e disponibile): ")
            if self.disonibile == "s":
                self.disonibile = True
            elif self.disonibile == "n":
                self.disonibile = False
            libri = {
                "titolo": self.titolo,
                "autore": self.autore,
                "anno pubblicazione": self.anno_pubblicazione,
                "disponibilita": self.disonibile
            }
            self.libreria.append(libri)
            print(self.libreria)
    def cerca(self):
        titolo = input("trova libro: ").lower()
        trova = False
        for book in self.libreria:
            if book["titolo"] == titolo:
                trova = True
                print(self.libreria)
        if not trova: print(f"Articolo '{titolo}' non trovato.")
    def prestato(self):
        titolo = input("trova libro da prendere: ").lower()
        trova = False
        for book in self.libreria:
            if book["titolo"] == titolo:
                trova = True
                print(self.libreria)
                if self.disonibile == True:
                    print("il libro e disponibile puo essere prestato")
                    book["disponibilita"] = False
                else:
                    print("il libro non e disponibile non puo essere prestato")
        if not trova: print(f"Articolo '{titolo}' non trovato.")
    def restituisci(self):
        titolo = input("trova il libro da restituire: ").lower()
        trova = False
        for book in self.libreria:
            if book["titolo"] == titolo:
                trova = True
                print(self.libreria)
                if self.disonibile == False:
                    print("il libro che e stato prestato viene restituisce")
                    book["disponibilita"] = True
                else:
                    print("il libro non e stato prestato")
        if not trova: print(f"Articolo '{titolo}' non trovato.")
    def mostra_dettagli(self):
        mostra = input("inserisci il titolo del libro per mostrare le info: ").lower()
        trova = False
        for book in self.libreria:
            if book["titolo"] == mostra:
                trova = True
                print(f"ecco tutte le info del libro: {self.libreria}")
        if not trova: print(f"Articolo '{mostra}' non trovato.")
    def salvare(self):
        with open("bibloteca.txt", "a", encoding="utf-8") as file:
            for libro in self.libreria:
                file.write(f"{libro}\n")
        
bibloteca = Libro()
while True:
    scelta = input("premi 'invio' per effettuare le opperazioni di CRUD per uscire premi 'esci': ").lower()
    if scelta == "esci": break
    elif scelta == "invio":
        while True:
            scelta1 = input("[a]ggiungi, [c]erca, [p]restato, [r]estituisce, [m]ostra info, [s]alvare, [e]sci: ").lower()
            if scelta1 == "a": bibloteca.aggiungi()
            elif scelta1 == "c": bibloteca.cerca()
            elif scelta1 == "p": bibloteca.prestato()
            elif scelta1 == "r": bibloteca.restituisci()
            elif scelta1 == "m": bibloteca.mostra_dettagli()
            elif scelta1 == "s": bibloteca.salvare()
            elif scelta1 == "e": break