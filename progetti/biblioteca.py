#Crea una classe biblioteca che permetta di creare un libro e stamparlo
#Extra: permetti di creare quanti libri vuole l’utente

class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}"

class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, titolo, autore):
        libro = Libro(titolo, autore)
        self.libri.append(libro)

    def stampa_libri(self):
        for libro in self.libri:
            print(libro)
biblioteca = Biblioteca()
biblioteca.aggiungi_libro("Il nome della rosa", "Umberto Eco")
biblioteca.aggiungi_libro("1984", "George Orwell")
biblioteca.stampa_libri()