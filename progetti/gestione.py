""" Gestore di Inventario Semplice
Questo progetto ti permette di tenere traccia di un piccolo inventario di prodotti, inclusi nome, quantità e 
prezzo.
Concetti Utilizzati:
Classi: Una classe Prodotto per rappresentare ogni articolo con i suoi attributi.
Collezioni: Una lista di oggetti Prodotto per gestire l'intero inventario.
Funzioni: Per aggiungere, rimuovere, aggiornare e visualizzare i prodotti, oltre a calcolare il valore totale 
dell'inventario.
Gestione File: Salvare e caricare l'inventario da un file JSON per la persistenza dei dati. Questo ti introdurrà 
al 
modulo json, molto utile per la serializzazione.
Moduli: json per la gestione strutturata dei dati, os per la verifica dell'esistenza del file.
Stringhe: Input e output per i dettagli dei prodotti.
Numeri: Gestione di quantità e prezzi.
Funzionalità:
Aggiungi Prodotto: Richiedi nome, quantità e prezzo, poi crea un oggetto Prodotto e aggiungilo all'inventario.
Visualizza Inventario: Mostra tutti i prodotti con i loro dettagli.
Aggiorna Quantità: Permetti di modificare la quantità di un prodotto esistente.
Rimuovi Prodotto: Elimina un prodotto dall'inventario.
Calcola Valore Totale: Calcola il valore complessivo dell'inventario (somma di (quantità * prezzo) per ogni 
prodotto).
Salva/Carica Inventario: Implementa la lettura e scrittura dei dati su un file JSON."""

class Prodotto:
    def __init__(self, nome, quantita, prezzo):
        self.nome = nome
        self.quantita = quantita
        self.prezzo = prezzo

    def __str__(self):
        return f"Nome: {self.nome}, Quantità: {self.quantita}, Prezzo: {self.prezzo}"

class GestioneInventario:
    def __init__(self):
        self.prodotti = []
        
    def aggiungi(self):
         while True:
            nome = input("Aggiungi un nuovo prodotto (per uscire premi 'esci'): ").lower()
            if nome == "esci":
                break
            quantita = input("Inserisci la quantita del prodotto: ")
            prezzo = input("Inserisci il prezzo del prodotto: ")
            prodotto = Prodotto(nome, quantita, prezzo)
            self.prodotti.append(prodotto)
            print("Prodotto aggiunto!")
    def mostra_prodotti(self):
        if not self.prodotti:
            print("Nessun prodotto in inventario.")
        for mostra in self.prodotti:
            print(f"ecco tutti i prodotti che ci sono: {mostra}")
    def quantita_aggio(self):
        nome = input("inserisci il nome del prodotto: ")
        trova = False
        for prodot in self.prodotti:
            if prodot.nome == nome:
                trova = True
                quantita = int(input("inserisci la quantita da togliere: "))
                if quantita > int(prodot.quantita):
                    print("Non hai abbastanza prodotti in magazzino!")
                    return
                prodot.quantita = int(prodot.quantita) - quantita
                print(f"la quantita del prodotto {nome} e {quantita}")
                print(f"la quantita del prodotto {nome} e rimasto: {prodot.quantita}")
        if not trova: print(f"Il prodotto '{nome}' non trovato.")
    def rimuovi_prod(self):
        nome = input("inserisci il nome del prodotto: ")
        trova = False
        for prodot in self.prodotti:
            if prodot.nome == nome:
                trova = True
                rimuovi = input("vuoi rimuovere il prodotto s/n: ")
                if rimuovi == "s":
                    self.prodotti.remove(prodot)
                    print("prodotto rimoso!")
                elif rimuovi == "n": break
        if not trova: print(f"Il prodotto '{nome}' non trovato.")  
    def Calcola_Valore_Totale(self):
         #somma di (quantità * prezzo)
         for prodot in self.prodotti:
             somma = somma + (int(prodot.quantita) * int(prodot.prezzo))
             print(f"la somma di tutti i prodotti: {somma}")         

gestione = GestioneInventario()
gestione.aggiungi()
gestione.mostra_prodotti()
gestione.quantita_aggio()
gestione.rimuovi_prod()
gestione.Calcola_Valore_Totale()