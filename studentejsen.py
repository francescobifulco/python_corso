import json

def aggiungi_studente(dati):
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    voti = []

    while True:
        voto = input("Inserisci voto (oppure 'fine'): ")
        if voto.lower() == "fine":
            break
        try:
            voti.append(int(voto))
        except ValueError:
            print("Inserisci un numero valido")

    media = round(sum(voti)/len(voti), 2) if voti else 0
    nuovo_id = dati["last_id"] + 1

    nuovo_studente = {
        "id": nuovo_id,
        "nome": nome,
        "cognome": cognome,
        "voti": voti,
        "media": media
    }

    dati["students"].append(nuovo_studente)
    dati["last_id"] = nuovo_id
    print("Studente aggiunto.")

def leggi():
    try:
        with open("data.json", "r") as file:
            dati = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        dati = {"id": 0, "students": []}
    return dati

def scrivi(dati):
    with open("data.json", "w") as file:
        json.dump(dati, file, indent=4)

def modifica(dati):
    print("Elenco studenti:")
    for studente in dati["students"]:
        print(f"{studente['id']}: {studente['nome']} {studente['cognome']}, voti: {studente['voti']}")
        # Chiedi quale studente modificare
    indice = int(input("Inserisci il numero dello studente da modificare: "))
    if 1 <= indice < len(dati[0]):
        nuovo_nome = input("Nuovo nome: ")
        nuovo_cognome = input("Nuovo cognome: ")
        quanti = int(input("Quanti voti vuoi inserire? "))
        nuovi_voti = []
        for _ in range(quanti):
            voto = int(input("Inserisci un voto: "))
            nuovi_voti.append(voto)
        dati[0][indice] = nuovo_nome
        dati[1][indice] = nuovo_cognome
        dati[2][indice] = nuovi_voti
        print("Studente modificato con successo!")
    else:
        print("Indice non valido.")

    # Mostra la matrice aggiornata
    for riga in dati:
        print(riga)

registro = leggi()

while True:
    scelta = input("Scegli: [a]ggiungi studente, [v]isualizza registro, [e]sci, [m]odifica: ").lower()
    if scelta == "a":
        aggiungi_studente(registro)
        scrivi(registro)
    elif scelta == "v":
        for studente in registro["students"]:
            print(studente)
    elif scelta == "e":
        scrivi(registro)
        print("Arrivederci!")
        break
    elif scelta == "m":
        modifica(registro)
    else:
        print("Scelta non valida.")