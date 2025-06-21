"""Idea Progetto 1: Sistema di Gestione Animali da Compagnia
Immagina di voler creare un sistema per gestire diversi tipi di animali domestici in un rifugio o in una clinica veterinaria.

Classi Base e Concetti:

Classe Base (Padre): Pensa a una classe Animale. Quali attributi comuni hanno tutti gli animali (es. nome, età, specie, sesso)? E quali comportamenti generici (es. dormire, mangiare, fare un suono)? Ricorda di utilizzare l'incapsulamento per proteggere gli attributi.
Classi Derivate (Figlie): Crea classi come Cane, Gatto, Uccello che ereditano da Animale. Quali attributi o comportamenti sono specifici di un cane (es. razza, abbaiare) o di un gatto (es. colore del pelo, fare le fusa)? Come puoi specializzare i metodi generici (es. un cane abbaia, un gatto miagola)? Questo è un ottimo esempio di ereditarietà e polimorfismo.
Classe di Gestione: Potresti avere una classe Rifugio o ClinicaVeterinaria che contiene una collezione di oggetti Animale. Questa classe dovrebbe avere metodi per aggiungere nuovi animali, cercare animali per nome o specie, e magari elencare tutti gli animali presenti. Anche qui, pensa all'incapsulamento per la lista degli animali.
Suggerimenti per l'Implementazione:

Usa attributi privati (__) per i dati interni delle classi e fornisci metodi pubblici (getter e setter) per accedervi o modificarli in modo controllato (principio dell'incapsulamento).
Sfrutta super().__init__() nelle classi figlie per inizializzare gli attributi della classe padre.
Pensa a come gestire i "suoni" specifici di ogni animale. Potrebbe essere un metodo nella classe base che viene sovrascritto nelle classi derivate."""

class Animali:
    def __init__(self,nome,eta,specie,sesso):
         self._nome = nome
         self._eta = eta
         self._specie = specie
         self._sesso = sesso
    def dormire(self):
        print("dormono di notte e di giorno")
    def mangiare(self):
        print("carnivore e ervibori")
    def suono(self):
        print("che suono fanno?")
    def __str__(self):
        return (f"Nome: {self._nome.capitalize()}, Età: {self._eta} anni, "
                f"Specie: {self._specie.capitalize()}, Sesso: {self._sesso}")

class Cane(Animali):
    def __init__(self, nome, età, specie, sesso,razza):
        super().__init__(nome,età, specie, sesso)
        self._razza = razza
    def dormire(self):
        super().dormire()
        print("il cane dorme di notte")
    def suono(self):
        super().suono()
        print("il cae abbaiare")
    

print("-----Animali------")
nome_animale = "Pippo"
eta_animale = 34
specie_animale = "quella che si sente"
sesso_animale = "M"

animale_generico = Animali(nome_animale, eta_animale, specie_animale, sesso_animale)
print(animale_generico)
animale_generico.dormire()
animale_generico.mangiare()
animale_generico.suono()

print("----Cane---")
nome_animale = "minni"
eta_animale = 0
specie_animale = "Cane"
sesso_animale = "F"
razza_cane = "labador"
cane = Cane(nome_animale, eta_animale, specie_animale, sesso_animale,razza_cane)