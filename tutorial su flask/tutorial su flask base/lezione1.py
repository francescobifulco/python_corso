from flask import Flask # Importa la classe Flask

# Crea un'istanza dell'applicazione Flask.
# __name__ è un nome speciale che 
# dice a Flask dove cercare i template e i file statici.
app = Flask(__name__)

# Definizione della Route (Percorso)
# Il decoratore @app.route('/') 
# associa la URL radice ('/') alla funzione 'index'.
@app.route('/')
def index():
    # Questa funzione restituisce la risposta 
    # HTTP che viene visualizzata nel browser.
    return "<h1>Ciao, Mondo da Flask!</h1>"

# Esecuzione dell'applicazione
if __name__ == '__main__':
    # app.run() avvia il server di sviluppo locale.
    # debug=True abilita la modalità debug (utile per lo sviluppo).
    app.run(debug=True)