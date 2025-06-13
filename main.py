"""create un gestionale scolastico per studenti che utilizza un file di testo 
come database:gli utenti potranno aggiungere alunni e voti, modificare alunni e 
voti, eliminare alunni e voti, visualizzare gli alunni presenti"""

matrice = ["nome", "cognome" ,"voti"]
voti = []
while True:
    nome = input("inserisci un nome: ")
    cogn = input("inserisci un cognome: ")
    while True:
        voto_s = input("inserisci un voto oppure fine: ")
        if voto_s == "fine": 
            break
        voti.append(voto_s)
        print(voti)
    studente = [nome, cogn, voti]
    matrice.append(studente)
    print(matrice)

with open("studenti.txt" ,"w") as file:
    contenuto = file.write()