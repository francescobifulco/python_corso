class Libro:
    editore = "Rizzoli"
    def __init__(self, titolo, autore, num_pag):
        self.titolo = titolo
        self.autore = autore
        self.num_pag = num_pag
    def desc(self):
        print(f"il libro si chiama {self.titolo}, scritto da {self.autore} il numero di pagine sono {self.num_pag}")
        
libro = Libro ("ciao", "enrico",500)
libro.desc()