"""estendere una classe base UnitaMilitare per creare diverse unità specializzate, ciascuna con compiti e metodi specifici. 
Inoltre, implementaew una classe ControlloMilitare che eredita da tutte le altre classi per gestire e tenere traccia delle diverse unità.

Classe UnitaMilitare:
Attributi:
nome (stringa): nome dell'unità.
numero_soldati (intero): numero di soldati nell'unità.
Metodi:
muovi(): stampa un messaggio sul movimento dell'unità.
attacca(): stampa un messaggio sull'attacco.
ritira(): gestisce il ritiro strategico.
Classi Derivate:
Fanteria:
costruisci_trincea(): costruisce difese temporanee.
Artiglieria:
calibra_artiglieria(): calibra i pezzi di artiglieria per la precisione.
Cavalleria:
esplora_terreno(): esplora l'area per raccogliere informazioni sul nemico.
SupportoLogistico:
rifornisci_unita(): gestisce il rifornimento e la manutenzione.
Ricognizione:
conduci_ricognizione(): conduce missioni di sorveglianza.
Classe ControlloMilitare:
Eredita da tutte le classi precedenti.
Attributi aggiuntivi:
unita_registrate: dizionario/due liste per tenere traccia delle unità create.
Metodi:
registra_unita(unita): aggiunge un'unità al registro.
mostra_unita(): elenca tutte le unità registrate.
dettagli_unita(nome): mostra dettagli specifici di un'unità.
"""

class UnitaMilitare:
    def __init__(self,nome,numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati
    def muovi(self):
        print("si muovono in 3 gruppi")
    def attacca(self):
        print("attaccano con AK-24")
    def ritira(self):
        print("bandiera bianca")
class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    def costruisci_trincea(self): 
        print("costruisce difese temporanee")
class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    def calibra_artiglieria(self): 
        print("calibra i pezzi di artiglieria per la precisione.")
class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    def esplora_terreno(self): 
        print("esplora l'area per raccogliere informazioni sul nemico.")
class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    def rifornisci_unita(self): 
        print("gestisce il rifornimento e la manutenzione.")
class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
    def conduci_ricognizione(self): 
        print("conduce missioni di sorveglianza.")
class ControlloMilitare(Fanteria,Artiglieria,Cavalleria,SupportoLogistico,Ricognizione):
    def __init__(self, nome, numero_soldati,unita_registrate):
        UnitaMilitare.super().__init__(nome, numero_soldati)
        self.unita_registrate = unita_registrate
    def registra_unita(self,unita): 
        self.unita_registrate.append(unita)
    def mostra_unita(self):
        if not self.unita_registrate:
            print("Nessuna unità registrata.")
        else:
            print("Unità registrate:")
            for unita in self.unita_registrate:
                print(f"- {unita.nome} ({unita.__class__.__name__}), Soldati: {unita.numero_soldati}")

    def dettagli_unita(self, nome):
        trova = False
        for unita in self.unita_registrate:
            if unita.nome == nome:
                trova = True
                print(f"Dettagli unità '{nome}':")
                print(f"Tipo: {unita.__class__.__name__}")
                print(f"Numero soldati: {unita.numero_soldati}")
        if not trova:
            print(f"Unità '{nome}' non trovata.")
            
militari = UnitaMilitare("bravo", 150000)
militari.attacca()
militari.muovi()
militari.ritira()

print("fanteria")
fanta = Fanteria("alfa", 3000)
fanta.ritira()
fanta.attacca()
fanta.muovi()
fanta.costruisci_trincea

print("Artiglieria")
arti = Artiglieria("omega", 10000)
arti.attacca()
arti.calibra_artiglieria()
arti.muovi()
arti.ritira()

print("Cavalleria")
cava = Cavalleria("i piu forti", 20000)
cava.esplora_terreno()