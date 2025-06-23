"""Esercizio 10: Classe e Oggetto Base
Obiettivo: Definire una semplice classe e creare oggetti da essa.

Definisci una classe chiamata Cane.
La classe Cane dovrebbe avere un metodo __init__ che accetta nome e razza come argomenti e li inizializza come attributi.
Crea due oggetti Cane con nomi e razze diverse.
Stampa il nome e la razza di ciascun oggetto cane."""

class Cane:
    def __init__(self,nome,razza):
        self.nome = nome
        self.razza = razza
    
cane1 = Cane("fido","barboncino")
cane2 = Cane("pippo","labrador")
print(f"il cane 1 si chiama {cane1.nome} di razza {cane1.razza} invece il cane 2 si chiama {cane2.nome} di razza {cane2.razza}")