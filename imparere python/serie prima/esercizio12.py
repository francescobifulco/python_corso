"""Esercizio 12: Ereditarietà
Obiettivo: Comprendere come le classi possono ereditare proprietà e comportamenti da altre classi.

Crea una classe genitore chiamata Animale con un metodo __init__ che accetta nome e un metodo parla che stampa "L'animale emette un suono."
Crea una classe figlia chiamata Gatto che eredita da Animale.
Sovrascrivi il metodo parla nella classe Gatto per stampare "Miao!".
Crea un oggetto Animale e un oggetto Gatto.
Chiama il metodo parla per entrambi gli oggetti."""

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

anoma = Animale("topolino")
gatto = Gatto("geltrude")

anoma.parla()
gatto.parla()