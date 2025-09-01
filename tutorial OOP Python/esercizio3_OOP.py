'''
Esercizio 3: Classe Contatore

Crea una classe Contatore con:

attributo: valore inizializzato a 0

metodi:

incrementa()

decrementa()

stampa() → stampa il valore corrente
'''

class Contatore:
    def __init__(self, valore = 0):
        self.valore = valore
    
    def incrementa(self):
        self.valore += 1
        return self.valore
    
    def decrementa(self):
        self.valore -= 1
        return self.valore
    
    def spampa(self):
        print(f'il valore e: {self.valore}')
        
cont = Contatore()
cont.incrementa()
cont.incrementa()
cont.decrementa()
cont.spampa()