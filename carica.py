import json

def visualizza():
    try:
        with open('contatti.json', 'r') as file:
            data = json.load(file)
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except (FileNotFoundError, json.JSONDecodeError):
        print("Nessun contatto trovato o file non valido.")