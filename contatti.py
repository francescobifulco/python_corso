class Contatto:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"Nome: {self.nome}, Numero: {self.numero}"

class Rubrica:
    def __init__(self):
        self.contatti = []

    def aggiungi(self):
        nome = input("Nome: ")
        numero = input("Numero: ")
        nuovo_contatto = Contatto(nome, numero)
        self.contatti.append(nuovo_contatto)
        print("Contatto aggiunto.")

    def stampa(self):
        print("Contatti in rubrica:")
        for contatto in self.contatti:
            print(contatto)
    
    def cerca(self,nome):
        trovato = False
        for contatto in self.contatti:
            if contatto.nome == nome:
                print(f"Il contatto {nome} è presente: {contatto.numero}")
                trovato = True
            if not trovato:
                print(f"Il contatto {nome} non è presente.")
    
    def elimina(self,nome):
        trovato = False
        for contatto in self.contatti:
            if contatto.nome == nome:
                self.contatti.remove(contatto)
                print(f"il contatto e stato eliminato: {nome}")
                trovato = True
            if not trovato:
                print(f"Il contatto {nome} non è presente.")
    
    def salva(self):
        with open("rubrica.txt", "w") as file:
            for contatto in self.contatti:
                file.write(f"{contatto.nome},{contatto.numero}\n")
            print("Rubrica salvata su file.")


rubrica = Rubrica()

while True:
    agg_con = input("Per effettuare le operazioni CRUD premi 'invio', per uscire 'esci': ").lower()
    if agg_con == "esci":
        break
    elif agg_con == "invio":
        cont = input("[a]ggiungi, [v]isualizza, [c]erca, [e]limina [s]alva: ").lower()
        if cont == "a":
            rubrica.aggiungi()
        elif cont == "v":
            rubrica.stampa()
        elif cont == "c":
            nome1 = input("inserire il nome del conttato: ")
            rubrica.cerca(nome1)
        elif cont == "e":
            nome1 = input("inserire il nome del conttato: ")
            rubrica.elimina(nome1)
        elif cont == "s":
            salvare = input("vuoi salvere il contatto s/n: ").lower()
            if salvare == "s":
                rubrica.salva()
            elif salvare == "n":
                break
        else:
            print("Scelta non valida.")