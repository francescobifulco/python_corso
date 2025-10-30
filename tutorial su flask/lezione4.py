from flask import Flask, render_template # Importa render_template

app = Flask(__name__)

@app.route('/saluta/<nome>')
def saluta_utente(nome):
    # Definisci una lista per l'esempio del ciclo 'for'
    lista_cose = ["Python", "Flask", "Jinja2"]
    
    # render_template cerca 'saluto.html' nella cartella 'templates'
    # e gli passa le variabili come argomenti keyword.
    return render_template('saluto.html', nome=nome, elementi=lista_cose)

# Esecuzione dell'applicazione
if __name__ == '__main__':
    # app.run() avvia il server di sviluppo locale.
    # debug=True abilita la modalità debug (utile per lo sviluppo).
    app.run(debug=True)