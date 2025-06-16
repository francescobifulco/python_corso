"""Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base . 
Requisiti:
Definizione della Classe:
Creare una classe chiamata Ristorante.
La classe dovrebbe avere un costruttore init che accetta due parametri: nome (nome del ristorante) e tipo_cucina (tipo di cucina offerta).
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere impostato su False di default (cioè, il ristorante è chiuso).
Un dizionario menu dove dentro ci sono i piatti e prezzi che ha il ristorante
Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
togli_dal_menu(): Un metodo per togliere piatti al menu
stampa_menu(): Un metodo per stampare il menu
Testare la Classe:
Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
Testare tutti i metodi creati per assicurarsi che funzionino come previsto.
"""

class Ristorante:
    aperto = False
    menu = {
    "Margherita": 7.50,
    "Marinara": 6.00,
    "Quattro Formaggi": 9.00,
    "Diavola": 8.50,
    "Capricciosa": 9.50,
    "Patatine Fritte": 4.00,
    "Coca Cola 33cl": 3.00,
    "Acqua Naturale 0.5L": 2.00,
    "Tiramisù": 5.50,
    "Panna Cotta": 4.50
}
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
    def descrivi_ristorante(self):
        print(f"il ristoranti di lusso {self.nome} prepare una tipologia di piatti {self.tipo_cucina} di ottima qualita")
    def stato_apertura(self):
        if Ristorante.aperto:
            print("Il ristorante è aperto.")
        else:
            print("Il ristorante è chiuso.")
    def apri_ristorante(self):
        Ristorante.aperto = True
        print(f"il ristorante e aperto potete venire a spendere e vostri soldi")
    def chiudi_ristorante(self):
        Ristorante.aperto = False
        print(f"il ristorante e chiuso apriamo quando abbiomo voglio")
    def aggiungi_al_menu(self):
        aggiu = input("aggiungi al menu un piatto per fare spendere piu i clienti: ")
        prezzo = float(input("il prezzo deve essere alto perche dobbiamo diventare ricchi: "))
        Ristorante.menu[aggiu] = prezzo
    def togli_dal_menu(self):
        while True:
            scelta = input("togliere un piatto s/n: ").lower()
            if scelta == "s":
                cerca = input("togliere un piatto nel menu s/n: ")
                if cerca in Ristorante.menu:
                    Ristorante.menu.pop(cerca)
                    print(f"il piatto {cerca} e stato tolto")
            elif scelta == "n": break
    def stampa_menu(self):
        print(Ristorante.menu)
        

risto = Ristorante ("pippo il fusso", "pizze e dolci")
risto.descrivi_ristorante()
risto.stato_apertura()
risto.apri_ristorante()
risto.chiudi_ristorante()
risto.aggiungi_al_menu()
risto.togli_dal_menu()
risto.stampa_menu()
    
        