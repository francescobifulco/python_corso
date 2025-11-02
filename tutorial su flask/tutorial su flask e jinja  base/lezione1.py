# --- Blocco 1: Importazioni e Configurazione Base ---
from flask import Flask, render_template, url_for, request # Importa le classi e funzioni necessarie da Flask
from flask_wtf import FlaskForm # Importa la classe base per i form da Flask-WTF
from wtforms import( # Importa i tipi di campo (widgets) da WTForms
    StringField, # Campo di input per stringhe di testo
    SubmitField, # Campo per il bottone di invio (submit)
    BooleanField,
    RadioField,
    SelectField,
    TextAreaField
)

# Crea un'istanza dell'applicazione 
# Flask. __name__ è il nome del modulo corrente.
app = Flask(__name__)

app.config['SECRET_KEY'] = 'chiavedisicurezza'

# --- Blocco 2: Routing Base ---

# Definisce la rotta per la homepage del sito ('/').
@app.route('/')
def index():
    # Ritorna il rendering del template 'index.html'.
    return render_template('index.html')

# Definisce una rotta di esempio per 
# mostrare il template engine Jinja2.
@app.route('/esempio/')
def jinja():
    # Ritorna il rendering del template 'esempio.html'.
    return render_template('esempio.html')

# Definisce una rotta semplice che ritorna una stringa.
@app.route('/info/')
def info():
    return f'Qui ci sono molti informazioni'

# --- Blocco 3: Routing con Variabili nell'URL ---

# L'URL accetta una stringa (chiamata name) dopo /info/. 
# La funzione usa questa variabile.
@app.route('/info/<name>') # 127.0.0.1:5000/info/franco
def my_name(name):
    # La variabile 'name' catturata 
    # dall'URL viene usata nella risposta.
    return f'Il mio nome e {name}'

""" @app.route('/info-errore/<name>')
def errore(name):
    return f'Generiamo un errore'.format(name[50]) """

# Definisce un endpoint che rende il template 
# percorsotuto.html e gli passa la variabile name 
# sotto il nome nome per l'uso con Jinja2.
@app.route('/tutorial/lista-tutorial/<name>')
def tutorial(name):
    # Crea una lista di elementi da passare al template.
    lista_tutorial = ['flask', 
                      'padan', 
                      'seabron', 
                      'numpy', 
                      'python base', 
                      'pygame']
    # Rende il template 'percorsotuto.html'.
    # Passa la variabile 'name' dall'URL come 'nome' per Jinja2.
    # Passa la lista come 'pagina_lista' per Jinja2.
    return render_template('percorsotuto.html', nome=name, 
                           pagina_lista=lista_tutorial)

# --- Blocco 4: Gestione Errori (Error Handler) ---

# Registra una funzione come gestore 
# per l'errore 404 (Pagina non trovata).
@app.errorhandler(404)
def errore(page_404):
    # Ritorna il rendering di 'errore.html' 
    # e il codice di stato HTTP 404.
    return render_template('errore.html'), 404

# --- Blocco 5: Routing con Query Parameters (GET) ---

# Definisce una rotta che accede ai 
# parametri della query string nell'URL.
# Esempio di URL: /tutorial/nuovo/?nome_tutorial=Flask&oggetto_tutorial=Web
@app.route('/tutorial/nuovo/')
def page_new():
    # Ottiene il valore del parametro 'nome_tutorial' 
    # dalla query string (es. ?nome_tutorial=Flask).
    nome_tutorial = request.args.get('nome_tutorial')
    # Ottiene il valore del parametro 'oggetto_tutorial'.
    soggetto_tutorial = request.args.get('oggetto_tutorial')
    # Rende il template passando i valori ottenuti.
    return render_template('newpage.html', nome_tutorial=nome_tutorial, 
                           soggetto_tutorial=soggetto_tutorial)

# Definisce una rotta che prepara dei 
# valori vuoti e rende un template per un form.
@app.route('/tutorial/form/')
def page_form():
    nome_tutorial = ''
    soggetto_tutorial = ''
    # Rende il template 'form_page.html' 
    # con variabili inizialmente vuote.
    return render_template('form_page.html', 
                           nome_tutorial=nome_tutorial, 
                           soggetto_tutorial=soggetto_tutorial)

# --- Blocco 6: Definizione della Classe Base e Form WTForms (Incompleto) ---
    
class FormBase(FlaskForm):
    nome = StringField('Nome del tutorial')
    pulsante = SubmitField('Submit')
    tutorial_act= BooleanField('Tutorial attivo')
    diffecolta = RadioField('Difficolta del tutorial{: ', 
                            choices=[{'facile', 'Facile'},
                                     {'medio', 'Medio'}, 
                                     {'avanzato', 'Avanzato'}])
    sito_tutorial = SelectField('Sito online del tutorial', 
                                choices=[{'github', }])
    soggetto = StringField('Soggetto del tutorial')

@app.route('/tutorial/nuovo/facile/', methods=['GET', 'POST'])
def form_avanzato():
    nome = False
    soggetto = False
    form = FormBase()
    if form.validate_on_submit():
        nome = form.nome.data
        soggetto = form.soggetto.data
        form.nome.data = ''
        form.soggetto.data = ''
    
    return render_template('tutorialsimpli.html', 
                           tutorial_form=form, 
                           tutorial_name=nome,
                           tutorial_soggetto=soggetto)

# --- Blocco 7: Avvio dell'Applicazione ---

# Avvia il server di sviluppo. debug=True 
# abilita il ricaricamento automatico.
app.run(debug=True)