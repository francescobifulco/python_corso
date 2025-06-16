import json

def salva_contatti(rubrica):
    with open("contatti.json", "w") as file:
        json.dump(rubrica, file, indent=4)