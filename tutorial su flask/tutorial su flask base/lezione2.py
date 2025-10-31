from flask import Flask # Importa la classe Flask

# Crea un'istanza dell'applicazione Flask.
# __name__ è un nome speciale che 
# dice a Flask dove cercare i template e i file statici.
app = Flask(__name__)

# Il routing determina quale codice 
# Python viene eseguito per una data URL.
@app.route('/about')
def about():
    return "Questa è la pagina 'About'."

# Esecuzione dell'applicazione
if __name__ == '__main__':
    # app.run() avvia il server di sviluppo locale.
    # debug=True abilita la modalità debug (utile per lo sviluppo).
    app.run(debug=True)