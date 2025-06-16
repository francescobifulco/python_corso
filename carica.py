import json

def carica_contatti():
    try:
        with open("contatti.json", "r") as file:
            dati = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        dati = {"id": 0, "contatti": []}
    return dati