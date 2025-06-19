"""Esercizio Complesso - “Gestione del Regno”
 Obiettivo
Creare un sistema gestionale per un regno medievale composto da villaggi, risorse e abitanti. Il giocatore veste i panni di un sovrano che gestisce il proprio regno e prende decisioni strategiche.

Struttura OOP
Classe Astratta: Abitante
Attributi protetti: nome, età, energia

Metodo astratto: lavora(villaggio)

Metodo: riposa()

Metodo: str() personalizzato per ogni sottoclasse (polimorfismo)

Sottoclassi:
Contadino: aumenta il cibo del villaggio

Minatore: aumenta le risorse (pietra e metallo)

Guerriero: non produce, ma difende dagli attacchi

Classe: Villaggio
Attributi privati:

nome, cibo, pietra, metallo, abitanti (lista di oggetti Abitante)

Metodi:

aggiungi_abitante(abitante)

passa_giornata(): ogni abitante lavora e consuma energia

report(): mostra stato delle risorse e salute del villaggio

Classe: Regno
Contiene lista di villaggi

Metodo gestisci_regno() che esegue un ciclo di gestione con scelta da terminale:

markdown
Copy
Edit
Visualizza stato villaggi
Assegna abitanti
Passa giornata
Costruisci nuovo villaggio
Esci
Requisiti tecnici
Uso di ABC e @abstractmethod su Abitante

Polimorfismo: ogni tipo di abitante implementa lavora in modo diverso

Incapsulamento e uso corretto di _attributi e proprietà (@property)

Composizione: un Villaggio contiene una lista di Abitante

Il Regno contiene una lista di Villaggi (2 livelli di oggetti annidati)

Interazione da terminale, con menu e input

 Estensioni opzionali
Aggiunta di eventi casuali (es. carestia, attacco nemico, bonus stagionali)

Introduzione della classe EventoCasuale con metodo applica(villaggio)

Salvataggio dello stato in un file JSON tra le giornate"""

from abc import ABC,abstractmethod

class Abitante(ABC):
    def __init__(self,nome,eta,energia):
        super().__init__()
        self.__nome = nome
        self.__eta = eta
        self.__energia = energia
    
    @property
    def get_nome(self):
        return self.__nome
    
    @nome.setter
    def set_nome(self, valore):
        self.__nome = valore
    
    @property    
    def get_eta(self):
        return self.__eta
    
    @eta.setter
    def set_eta(self, valore):
        self.__eta = valore
    
    @property    
    def get_energia(self):
        return self.__energia
    
    @energia.setter
    def set_energia(self, valore):
        self.__energia = valore
    
    @abstractmethod
    def lavora(villaggio):
        pass
    
    def riposa(self):
        pass
    
    def __str__(self):
        super().__str__()
        pass
    
class Contadino(Abitante):
    def __init__(self, nome, eta, energia,produce_cibo):
        super().__init__(nome, eta, energia)
        self.__produce_cibo = produce_cibo
    
    @property
    def get_produce_cibo(self):
        return self.__produce_cibo
    
    @roduce_cibo.setter
    def set_produce_cibo(self, valore):
        self.__cibo = valore

    def __str__(self):
        super().__str__()
        return (f"il contadeno produre cibo")
    
class Minatore(Abitante):
    def __init__(self, nome, eta, energia,produce_pietra,produce_metallo):
        super().__init__(nome, eta, energia)
        self.__produce_pietra = produce_pietra
        self.__produce_metallo = produce_metallo
    
    @property    
    def get_produce_pietra(self):
        return self.__produce_pietra
    
    @produce_pietra.setter
    def set_produce_pietra(self, valore):
        self.__produce_pietra = valore
    
    @property    
    def get_produce_metallo(self):
        return self.__produce_metallo
    
    @produce_metallo.setter
    def set_produce_metallo(self, valore):
        self.__produce_metallo = valore

    def __str__(self):
        super().__str__()
        return (f"il minatore produre pietra e metallo")
    
class Guerriero(Abitante):
    def __init__(self, nome, eta, energia,difende_villaggio):
        super().__init__(nome, eta, energia)
        self.__difende_villaggi = difende_villaggio
    
    @property    
    def get_difende_villaggio(self):
        return self.__defende_villaggio
     
    @difende_villaggio.setter
    def set_difende_villaggio(self, valore):
        self.__difende_villaggio = valore
    
    def __str__(self):
        super().__str__()
        return (f"il guerriero difende il villaggio")
    
class Villaggio:
    def __init__(self,nome_villaggio,pietra,metallo):
        self.__nome_villaggio = nome_villaggio
        self.__pietra = pietra
        self.__metallo = metallo
        self.__abitanti = []
    
    @property
    def get_nome_villaggio(self):
        return self.__nome_villaggio
    
    @nome_villaggio.setter
    def set_nome_villagio(self, valore):
        self.__nome_villaggio = valore
    
    @property    
    def get_pietra(self):
        return self.__pietra
    
    @pietra.setter
    def set_produce_pietra(self, valore):
        self.__pietra = valore
    
    @property    
    def get_metallo(self):
        return self.__produce_metallo
    
    @metallo.setter
    def set_metallo(self, valore):
        self.__metallo = valore
    
    def aggiungi_abitante(abitante):
        pass