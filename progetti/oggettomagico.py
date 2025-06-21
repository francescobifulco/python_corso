"""Esercizio – La Bottega delle Meraviglie
Lo scopo di questo esercizio è costruire un piccolo sistema di gestione per una bottega che vende oggetti magici. L'obiettivo è consolidare l'uso delle classi, delle liste, dei dizionari e della gestione dello stato degli oggetti, senza utilizzare l'ereditarietà.
Struttura richiesta
1. Classe OggettoMagico
Crea una classe OggettoMagico con i seguenti attributi:
nome: nome dell’oggetto (es. "Pozione di guarigione")
potere: descrizione dell’effetto dell’oggetto
prezzo: prezzo di vendita
quantita: quantità disponibile in bottega
La classe deve includere un metodo:
descrizione(): stampa tutte le informazioni dell’oggetto in modo leggibile.
2. Classi Pozione, Artefatto e Pergamena
Crea tre classi separate (senza ereditarietà) chiamate Pozione, Artefatto e Pergamena. Ognuna di queste deve avere un attributo:
oggetto: che contiene un’istanza della classe OggettoMagico.
3. Classe BottegaMagica
Crea una classe BottegaMagica che gestisce l'inventario della bottega.
Attributi:
oro: quantità iniziale di monete d’oro disponibili
inventario: dizionario con chiavi "Pozioni", "Artefatti" e "Pergamene", ognuna contenente una lista di oggetti magici
Metodi richiesti:
aggiungi(categoria, oggetto): aggiunge un oggetto magico all'inventario nella categoria corretta
mostra_inventario(): stampa tutte le categorie e gli oggetti disponibili
vendi(nome_oggetto, categoria, quantita): da completare – cerca un oggetto, riduce la quantità, aggiorna l’oro e rimuove l’oggetto se esaurito
reso(nome_oggetto, categoria, quantita): da completare – aumenta la quantità di un oggetto restituito
cerca_oggetto(nome_oggetto, categoria): da completare – restituisce l’oggetto corrispondente se esiste
Obiettivo finale
Implementare tutte le classi e i metodi richiesti. Alcuni metodi saranno da completare con logica personalizzata. Il sistema deve essere in grado di:
Aggiungere oggetti al magazzino
Mostrare l’inventario completo
Eseguire una vendita e aggiornare l’oro
Gestire i resi di oggetti
Trovare oggetti nel dizionario"""

class OggettoMagico:
    def __init__(self, nome_ogg,potere_ogg,prezzo,quantita):
        self.nome_ogg = nome_ogg
        self.potere_ogg = potere_ogg
        self.prezzo = prezzo
        self.quantita = quantita
    
    def descrizione(self):
        return f"L'{self.nome_ogg}' ha il potere di {self.potere_ogg}, il suo prezzo è di {self.prezzo} monete imperiali, e può essere usato {self.quantita} volte in battaglia."

class Pozione:
    def __init__(self, oggetto):
        self.oggetto = oggetto
class Artefatto:
    def __init__(self, oggetto):
        self.oggetto = oggetto
class Pergamena:
    def __init__(self, oggetto):
        self.oggetto = oggetto

class BottegaMagica:
    def __init__(self,oro):
        self.oro = oro
        self.inventario = {
            "Pozioni": [],
            "Artefatti": [],
            "Pergamene": []
        }
    def aggiungi(self,categoria, oggetto):
        if categoria in self.inventario:
             self.inventario[categoria].append(oggetto)
             print(f"{oggetto.oggetto.nome_ogg} aggiunto nella categoria {categoria}.")
        else:
            print("Categoria non valida.")
    def mostra_inventario(self):
        print("Inventario della bottega:")
        for categoria, lista in self.inventario.items():
           print(f"\nCategoria: {categoria}")
           if not lista:
               print("  Nessun oggetto in questa categoria.")
           else: 
               for oggetto in lista:
                print("  -", oggetto.oggetto.descrizione())
    def vendi(self, nome_oggetto, categoria, quantita):
        trova = False
        if categoria in self.inventario:
            for oggetto_wrapper in self.inventario[categoria]:
                oggetto = oggetto_wrapper.oggetto
                if oggetto.nome_ogg.lower() == nome_oggetto.lower():
                    trova = True
                    if int(oggetto.quantita) >= quantita:
                        oggetto.quantita = int(oggetto.quantita) - quantita
                        self.oro += int(oggetto.prezzo) * quantita
                        print(f"Hai venduto {quantita} {oggetto.nome_ogg}. Oro attuale: {self.oro}")
                        if oggetto.quantita == 0:
                            self.inventario[categoria].remove(oggetto_wrapper)
                            print(f"{oggetto.nome_ogg} esaurito e rimosso dall'inventario.")
                        else:
                            print(f"Quantità insufficiente di {oggetto.nome_ogg} per la vendita.")
                            break
                        if not trova:
                            print(f"Articolo '{nome_oggetto}' non trovato nella categoria '{categoria}'.")
    def reso(self, nome_oggetto, categoria, quantita):
        if categoria in self.inventario:
            for oggetto_vendi in self.inventario[categoria]:
                oggetto = oggetto_vendi.oggetto
                if oggetto.nome_ogg.lower() == nome_oggetto.lower():
                    oggetto.quantita = int(oggetto.quantita) + quantita
                    self.oro -= int(oggetto.prezzo) * quantita
                    print(f"Hai restituito {quantita} {oggetto.nome_ogg}. Oro attuale: {self.oro}")
                    return
            print(f"Articolo '{nome_oggetto}' non trovato nella categoria '{categoria}'.")
        else:
            print("Categoria non valida.")
    def cerca_oggetto(self, nome_oggetto, categoria):
        if categoria in self.inventario:
            for oggetto_cerca in self.inventario[categoria]:
                oggetto = oggetto_cerca.oggetto
                if oggetto.nome_ogg.lower() == nome_oggetto.lower():
                    return oggetto_cerca
            print(f"Articolo '{nome_oggetto}' non trovato nella categoria '{categoria}'.")
            return None
        else:
            print("Categoria non valida.")
            return None

nome = input("inserisci il nome del oggetto: ")
potere = input("inserisci il potere del oggetto: ")
prezzo_ogg = input("inserisci il prezzo del oggetto: ")
quantita_uso = input("inserisci quante volte viene usato in battaglia: ")

bataglia = OggettoMagico(nome, potere, prezzo_ogg, quantita_uso)
print(bataglia.descrizione())    

magia = OggettoMagico(nome, potere, prezzo_ogg, quantita_uso)
pozione = Pozione(magia)
artefatto = Artefatto(magia)
pergamena = Pergamena(magia)

print(pozione.oggetto.descrizione())

bottega = BottegaMagica(100)
pozione_guarigione = Pozione(OggettoMagico("Pozione di guarigione", "cura", 10, 3))
bottega.aggiungi("Pozioni", pozione_guarigione)

bottega.mostra_inventario()
bottega.vendi(nome, "Artefatti", 1)         
bottega.cerca_oggetto(nome, "Pozioni")      
bottega.reso(nome, "Pergamene", 1)         