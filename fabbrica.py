"""Lo scopo di questo esercizio è creare un sistema di gestione per una fabbrica che produce e vende vari tipi di prodotti. Gli studenti dovranno creare una classe base chiamata Prodotto e diverse classi derivate che rappresentano diversi tipi di prodotti. Inoltre, dovranno creare una classe Fabbrica che gestisce l'inventario e le vendite dei prodotti.
Classe Prodotto:
Attributi:
nome (stringa che descrive il nome del prodotto)
costo_produzione (costo per produrre il prodotto)
prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
Metodi:
calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione. // 
Classe di riferimento su cui basare le altre
Classi Derivate:
Creare almeno due classi derivate da Prodotto, per esempio Elettronica e Abbigliamento.
Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
Classe Fabbrica:
Attributi:
inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
Metodi:
aggiungi_prodotto: aggiunge prodotti all'inventario.
vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.
"""

class Prodotto:
    nome = ""
    costo_produzione = 0
    prezzo_vendita = 0  
    def inserimento(self):
        self.nome = input("inserisci un nome al prodotto: ").lower()
        self.costo_produzione = float(input("inserisci il costo di produzione: "))
        self.prezzo_vendita = float(input("inserisci il prezzo di vendita del prodotto: "))
    def calcola_profitto(self):
        margine = self.prezzo_vendita - self.costo_produzione
        print(f"il costo e {self.costo_produzione} il prezzo di vendita e {self.prezzo_vendita} il margine e {margine}")
        return margine

class Fabbrica:
    inventario = []
    def aggiungi_prodotto(self):
        while True:
            aggi = input("aggiungi un prodotto per uscire premi 'esci': ").lower()
            if aggi == "esci": break
            prodo = {"nome": aggi}
            self.inventario.append(prodo)
            print(self.inventario)
    
produzione = Prodotto()
produzione.inserimento()
produzione.calcola_profitto()

prodo = Fabbrica()
prodo.aggiungi_prodotto()