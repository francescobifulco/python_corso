import math

class Punto:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def stampaCoo(self):
        print(f"coodinate dei punti. x {self.x} y {self.y}")
    def muovi(self, dx,dy):
        self.x=dx
        self.y=dy
    def distan(self):
        x2 = self.x**2
        y2 = self.y**2
        dis =round(math.sqrt((x2+y2)))
        return dis

punto = Punto(10,2)
punto.stampaCoo()
print(punto.distan())