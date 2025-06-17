"""creare una classe base MembroSquadra e diverse classi figlie che rappresentano ruoli specifici all'interno della squadra di calcio, come Giocatore, Allenatore, e Assistente. 
L'esercizio consente di esplorare come differenti membri della squadra possono ereditare attributi comuni dalla classe base, ma anche come possono differire nei loro comportamenti e responsabilità.
Classe MembroSquadra:
Attributi:
nome (stringa)
età (intero)
Metodi:
descrivi() (stampa una descrizione generale del membro della squadra)
Classi Derivate:
Giocatore:
Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
Metodi come gioca_partita() che possono includere azioni specifiche del giocatore
Allenatore:
Attributi aggiuntivi come anni_di_esperienza
Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti
Assistente:
Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team"""

class MembroSquadra:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
    def descrivi(self):
        return f"il menbro della e molto forte e bravo <3"
class Giocatore(MembroSquadra): 
    def __init__(self, nome, eta,attaccante,difensore,numero_maglia):
        super().__init__(nome, eta)
        self.attaccante = attaccante
        self.difensore = difensore
        self.numero_maglia = numero_maglia
    def gioca_partita(self):
        print(f"{self.nome} gioca la partita con la maglia numero {self.numero_maglia}.")
class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza

    def dirige_allenamento(): #che dettagliano come l'allenatore conduce gli allenamenti
        print("L'allenatore inizia l'allenamento con il riscaldamento.")
class Assistente(MembroSquadra):
    def __init__(self, nome, eta,fisioterapista, analista_gioco):
        super().__init__(nome, eta)
        self.fisioterapista = fisioterapista
        self.analista_gioco = analista_gioco
    def supporta_team():
        print("aiuta i giocattori a essere piu forti")