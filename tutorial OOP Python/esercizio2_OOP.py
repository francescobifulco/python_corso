'''
Esercizio 2: Classe Rettangolo

Crea una classe Rettangolo con:

attributi: base, altezza

metodi:

area() → restituisce l’area

perimetro() → restituisce il perimetro
'''

class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
    
    def area(self):
        area = self.base * self.altezza
        print(f'area del rettangolo e: {area}')
    
    def perimetro(self):
        perimetro = 2 * (self.base + self.altezza)
        print(f'il perimetro del rettangolo e: {perimetro}')

rett = Rettangolo(45, 23)
rett.area()
rett.perimetro()