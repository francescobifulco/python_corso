class Animali:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
    def fai_suono():
        print("il suo del animale: ")
class Leone(Animali):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
    def caccia():
        print("il leone caccio in modo silenzioso")
    def habitat():
        print("il leone abita nella savana")
        def fai_suono():
            print("il leone ruggisce: ROAR")
class Giraffa(Animali):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
    def alimentazione():
        print("le giraffe sono erbivori")
    def fai_suono():
        print("la giraffa silenziosi: schuuu")
class Pinguino(Animali):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
    def fisiche():
        print("sono nero sul dorso e bianco sul ventre")
    def fai_suono():
        print("i pinguini strillano: kraa-kraa")

#aggiusta
animale_generico = Animali()
leone = Leone()
