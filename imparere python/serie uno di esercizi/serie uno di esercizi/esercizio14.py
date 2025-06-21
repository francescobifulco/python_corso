"""Esercizio 14: Polimorfismo
Obiettivo: Comprendere come oggetti diversi possono rispondere alla stessa chiamata di metodo in modi propri.

Crea una funzione suono_animale che accetta un oggetto Animale come argomento e chiama il suo metodo parla.
Crea una classe Cane e una classe Gatto (entrambe ereditando da Animale e avendo i propri metodi parla).
Crea istanze di Cane e Gatto.
Chiama suono_animale sia con gli oggetti Cane che Gatto per osservare il polimorfismo."""

class Animale:
    def __init__(self,nome):
        self.nome = nome
    
    def parla(self):
        print("L'animale emette un suono.")

class Gatto(Animale):
    def __init__(self, nome):
        super().__init__(nome)
    
    def parla(self):
        print("Miao!")

class Cane(Animale):
    def __init__(self, nome):
        super().__init__(nome)
    
    def parla(self):
        print("Woof!")

def suono_animale(animale):
        print(f"animale con nome {animale.nome} fa", end=" ")
        animale.parla()   

anoma = Animale("topolino")
gatto = Gatto("geltrude")
cane = Cane("davire")

cane.parla()
anoma.parla()
gatto.parla()

suono_animale(anoma)
suono_animale(gatto)
suono_animale(cane)