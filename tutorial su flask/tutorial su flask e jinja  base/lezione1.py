from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/esempio/')
def jinja():
    return render_template('esempio.html')

@app.route('/info/')
def info():
    return f'Qui ci sono molti informazioni'

# L'URL accetta una stringa (chiamata name) dopo /info/. 
# La funzione usa questa variabile.
@app.route('/info/<name>') # 127.0.0.1:5000/info/franco
def my_name(name):
    return f'Il mio nome e {name}'

""" @app.route('/info-errore/<name>')
def errore(name):
    return f'Generiamo un errore'.format(name[50]) """

# Definisce un endpoint che rende il template 
# percorsotuto.html e gli passa la variabile name 
# sotto il nome nome per l'uso con Jinja2.
@app.route('/tutorial/flask/<name>')
def tutorial(name):
    return render_template('percorsotuto.html', nome=name)

# Avvia il server di sviluppo. debug=True 
# abilita il ricaricamento automatico.
app.run(debug=True)