'''
Esercizio 4: Classe Banca e ContoBancario

Crea due classi:

ContoBancario con:

attributi: intestatario, saldo

metodi:

deposita(importo)

preleva(importo)

mostra_saldo()

Banca con:

attributo: lista_conti (lista di oggetti ContoBancario)

metodo:

aggiungi_conto(conto)

stampa_conti()
'''

class ContoBancario:
    def __init__(self, intestatario, saldo):
        self.intestatario = intestatario
        self.saldo = saldo
    
    def deposita(self, importo):
        self.saldo += importo
        #print(f'importo del saldo e: {self.saldo}')
    
    def preleva(self, importo):
        self.saldo -= importo
        #print(f'hai prevelato dal tuo conto: {self.saldo}')
    
    def mostra_saldo(self):
        print(f'dal conto {self.intestatario} hai un saldo di: {self.saldo}')
        
class Banca(ContoBancario):
    def __init__(self, lista_conti):
        
        
conto = ContoBancario('ciro', 10)
conto.mostra_saldo()

conto.deposita(20)
conto.mostra_saldo()

conto.preleva(10)
conto.mostra_saldo()