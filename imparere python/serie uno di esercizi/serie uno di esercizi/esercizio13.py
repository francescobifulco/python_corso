"""Esercizio 13: Incapsulamento (usando le proprietà)
Obiettivo: Usare le proprietà per controllare l'accesso agli attributi.

Modifica la classe Cane dagli esercizi precedenti.
Rendi gli attributi nome e razza "privati" per convenzione (prefiggili con _).
Aggiungi metodi getter (proprietà) per nome e razza usando il decoratore @property.
Aggiungi metodi setter per nome e razza se vuoi permettere che vengano modificati dopo l'inizializzazione, aggiungendo una validazione (es. il nome non può essere vuoto).
Prova ad accedere e modificare gli attributi usando le proprietà."""

class Cane:
    def __init__(self,nome,razza):
        self._nome = nome
        self._razza = razza
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def set_nome(self,nome_nuovo):
        if isinstance(nome_nuovo, str) and nome_nuovo.strip() != "":
             self._nome = nome_nuovo
             print("nome modificato")
        else:
           print("il nome non deve essere vuoto")
        
    @property
    def razza(self):
        return self._razza
    
    @razza.setter
    def set_razza(self,razza):
        self._razza  
        
    def abbaia(self):
        print("Woof!")
        
    def descrizione(self):
        return (f"{self._nome} è un {self._razza} ")
    
cane1 = Cane("fido","barboncino")
cane2 = Cane("pippo","labrador")
print(f"il cane 1 si chiama {cane1.nome} di razza {cane1.razza} invece il cane 2 si chiama {cane2.nome} di razza {cane2.razza}")

print(cane1.descrizione())
cane1.abbaia()
print(cane2.descrizione())
cane2.abbaia()

cane1.set_nome = "gianfranco"
print(cane1.nome)
cane2.set_nome = ""
print(cane2.nome)