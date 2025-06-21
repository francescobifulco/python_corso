"""create un gestionale scolastico per studenti che utilizza un file di testo 
come database:gli utenti potranno aggiungere alunni e voti, modificare alunni e 
voti, eliminare alunni e voti, visualizzare gli alunni presenti"""

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

def modifica(matrice):
    # Mostra tutti gli studenti con il loro indice
    print("Elenco studenti:")
    for i in range(1, len(matrice[0])):  # Salta l'intestazione
        print(f"{i}: {matrice[0][i]} {matrice[1][i]}, voti: {matrice[2][i]}")
    
    # Chiedi quale studente modificare
    indice = int(input("Inserisci il numero dello studente da modificare: "))
    if 1 <= indice < len(matrice[0]):
        nuovo_nome = input("Nuovo nome: ")
        nuovo_cognome = input("Nuovo cognome: ")
        quanti = int(input("Quanti voti vuoi inserire? "))
        nuovi_voti = []
        for _ in range(quanti):
            voto = int(input("Inserisci un voto: "))
            nuovi_voti.append(voto)
        matrice[0][indice] = nuovo_nome
        matrice[1][indice] = nuovo_cognome
        matrice[2][indice] = nuovi_voti
        print("Studente modificato con successo!")
    else:
        print("Indice non valido.")

    # Mostra la matrice aggiornata
    for riga in matrice:
        print(riga)

def rimuovi(matrice):
    # Mostra tutti gli studenti con il loro indice
    print("Elenco studenti:")
    for i in range(1, len(matrice[0])):  # Salta l'intestazione
        print(f"{i}: {matrice[0][i]} {matrice[1][i]}, voti: {matrice[2][i]}")
    
    indice = int(input("Inserisci il numero dello studente da rimuovere: "))
    if 1 <= indice < len(matrice[0]):
         matrice[0].pop(indice)
         matrice[1].pop(indice)
         matrice[2].pop(indice)
         print("Studente rimosso con successo.")
    else:
        print("Indice non valido.")


matrice = [["nome"],["cognome"],["voto"]]
while True:
    scelta = input("per inserire il nome e cognome e il voto dello studente premi 'invio' e per uscire premi 'esci': ")
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
        matrice[0].append(nome)
        matrice[1].append(cognome)
        matrice[2].append(voti)
        for riga in matrice:
            print(riga)
        while True:
            scelta1 = input("per eseguire le opperazioni crud (1'aggiungere',2'modifica',3'rimuovi') per uscire 'esci': ")
            if scelta1 == "esci":
                break
            elif scelta1 == "1":
                aggiungi(matrice)
            elif scelta1 == "2":
                modifica(matrice)
            elif scelta1 == "3":
                rimuovi(matrice)

with open("studenti.txt" ,"w") as file:
     for riga in matrice:
        file.write(str(riga) + "\n")