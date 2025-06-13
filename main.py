"""create un gestionale scolastico per studenti che utilizza un file di testo 
come database:gli utenti potranno aggiungere alunni e voti, modificare alunni e 
voti, eliminare alunni e voti, visualizzare gli alunni presenti"""

alunni = {}
while True:
    nome = input("Nome alunno (o 'media' per finire): ")
    if nome == "media":
        break
    if nome not in alunni:
        alunni[nome] = []
    else:
        print("Nome già presente")
        continue
while True:
    voto = input(f"Inserisci un voto per {nome} ('fine' per cambiare alunno): ")
    if voto == "fine":
        break
    alunni[nome].append(float(voto))
    for nome in alunni:
        media = sum(alunni[nome]) / len(alunni[nome])
    print(f"Nome: {nome}, Media: {media}")
    
    with open("Studenti.txt", "w") as file:
        file.write("Studenti.txt")