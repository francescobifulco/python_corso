from flask import Flask # Importa la classe Flask

# Crea un'istanza dell'applicazione Flask.
# __name__ è un nome speciale che 
# dice a Flask dove cercare i template e i file statici.
app = Flask(__name__)

# Puoi catturare parti dell'URL come variabili:

@app.route('/utente/<username>')
def mostra_profilo_utente(username):
    # La variabile 'username' viene passata alla funzione.
    return f'Profilo di: {username}'

@app.route('/post/<int:post_id>')
def mostra_post(post_id):
    # Usando <int:post_id> si definisce il tipo
    # della variabile come intero.
    return f'Post numero: {post_id}'

# Esecuzione dell'applicazione
if __name__ == '__main__':
    # app.run() avvia il server di sviluppo locale.
    # debug=True abilita la modalità debug (utile per lo sviluppo).
    app.run(debug=True)