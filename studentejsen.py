import json

def aggiungi(matrice):
    while True:
        scelta = input("per aggiungere un nuovo studente 'invio' e per uscire premi 'esci': ")
        if scelta.lower() == "esci":
            break
        elif scelta.lower() == "invio":
            nome = input("inserisci il tuo nome: ")
            cognome = input("inserisci il tuo cognome: ")
            quanti = int(input("inserisci quanti voti vuoi metere: "))
            voti = []
            for el in range(quanti):
                voto = int(input("inserisci un voto: "))
                voti.append(voto)
            matrice[0].insert(1,nome)
            matrice[1].insert(1,cognome)
            matrice[2].insert(1,voti)
            for riga in matrice:
                print(riga)

def leggi():
    with open ("data.json", "r") as file:
        studenti = json.load(file)
    print(studenti)
    return studenti

def scrivi(studenti):
    with open ("data.json", "w") as file:
        json.dump(studenti)

while True:
    scelta = input("")
    