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
            nome = input("Aggiungi un prodotto (per uscire premi 'esci'): ").lower()
            if nome == "esci":
                break
            quantita = int(input("Inserisci la quantità: "))
            costo = float(input("Inserisci il costo di produzione: "))
            prezzo = float(input("Inserisci il prezzo di vendita: "))
            prodotto = {
                "nome": nome,
                "quantita": quantita,
                "costo_produzione": costo,
                "prezzo_vendita": prezzo
            }
            self.inventario.append(prodotto)
            print(self.inventario)
    
    def vendi_prodotto(self):
        nome = input("trova prodotto: ").lower()
        trova = False
        for prodot in self.inventario:
            if prodot["nome"] == nome:
                trova = True
                vendi = int(input(f"inserisci il numero di vendite del prodotto {nome}: "))
                if vendi > prodot["quantita"]:
                    print("Non hai abbastanza prodotti in magazzino!")
                    return
                prodot["quantita"] -= vendi 
                profitto = prodot["prezzo_vendita"] - prodot["costo_produzione"]
                profitto_tot = profitto * vendi
                print(f"il profitto del prodotto e stato: {profitto_tot} €")
        if not trova: print(f"Articolo '{nome}' non trovato.")
    def resi_prodotto(self):
        nome = input("trova prodotto: ").lower()
        trova = False
        for prodot in self.inventario:
            if prodot["nome"] == nome:
                trova = True
                reso = int(input(f"inserisci il numero di vendite del prodotto {nome}: "))
                prodot["quantita"] += reso
                print(f"la quantita del prodotto {nome} e ritoranto di {prodot}")
        if not trova: print(f"Articolo '{nome}' non trovato.")
        
class Eletronica:
    def __init__(self, nome, prezzo):
       self.nome = nome
       self.prezzo = prezzo
    def __str__(self):
        return f"{self.nome},{self.prezzo}"
    
class Abbigliamento: 
    def __init__(self, nome, prezzo):
       self.nome = nome
       self.prezzo = prezzo
    def __str__(self):
        return f"{self.nome},{self.prezzo}"
      
        
    
produzione = Prodotto()
produzione.inserimento()
produzione.calcola_profitto()

prodo = Fabbrica()
prodo.aggiungi_prodotto()
prodo.vendi_prodotto()
prodo.resi_prodotto()

e = Eletronica("Smartphone", 299.99)
a = Abbigliamento("Maglietta", 19.99)

print(e)
print(a)