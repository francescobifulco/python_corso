"""Esercizio 11: Metodi di Classe
Obiettivo: Aggiungere metodi a una classe per definire comportamenti.

Aggiungi un metodo chiamato abbaia alla classe Cane (dall'Esercizio 10) che stampa "Woof!".
Aggiungi un altro metodo chiamato descrizione che restituisce una stringa come: "[Nome del Cane] è un [Razza del Cane]."
Chiama i metodi abbaia e descrizione per i tuoi oggetti Cane."""

class Cane:
    def __init__(self,nome,razza):
        self.nome = nome
        self.razza = razza
        
    def abbaia(self):
        print("Woof!")
        
    def descrizione(self):
        return (f"{self.nome} è un {self.razza} ")
    
cane1 = Cane("fido","barboncino")
cane2 = Cane("pippo","labrador")
print(f"il cane 1 si chiama {cane1.nome} di razza {cane1.razza} invece il cane 2 si chiama {cane2.nome} di razza {cane2.razza}")

print(cane1.descrizione())
cane1.abbaia()
print(cane2.descrizione())
cane2.abbaia()