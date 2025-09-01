'''
Esercizio 1: Classe Persona

Crea una classe Persona con i seguenti attributi:

nome

cognome

età

Aggiungi un metodo saluta() che stampi:

"Ciao, mi chiamo Nome Cognome e ho X anni."
'''
class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
    def stampa(self):
        print(f'Ciao, mi chiamo {self.nome} {self.cognome} e ho {self.eta} anni.')

per1 = Persona('antonio', 'brancaccio', '34')
per1.stampa()