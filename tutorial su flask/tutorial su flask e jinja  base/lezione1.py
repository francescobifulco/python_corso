# --- Blocco 1: Importazioni e Configurazione Base ---
from flask import ( # Importa le classi e funzioni necessarie da Flask
    Flask, 
    render_template, 
    url_for, 
    request, 
    session, # Necessario per usare le sessioni utente
    redirect) # Necessario per reindirizzare l'utente
# Importa la classe base per i form da Flask-WTF
from flask_wtf import FlaskForm 
from wtforms import( # Importa i tipi di campo (widgets) da WTForms
    StringField, # Campo di input per stringhe di testo
    SubmitField, # Campo per il bottone di invio (submit)
    BooleanField, # Casella di controllo (checkbox)
    RadioField, # Gruppo di pulsanti radio
    SelectField, # Menu a tendina (dropdown)
    TextAreaField # Area di testo multilinea
)
# Validatore che richiede un dato
from wtforms.validators import DataRequired

# Crea un'istanza dell'applicazione 
# Flask. __name__ è il nome del modulo corrente.
app = Flask(__name__)

# Configura una chiave segreta necessaria per la 
# sicurezza delle sessioni (cookie firmati).
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
# Esempio di URL: /tutorial/nuovo/?
# nome_tutorial=Flask&oggetto_tutorial=Web
@app.route('/tutorial/nuovo/')
def page_new():
    # Ottiene il valore del parametro 'nome_tutorial' 
    # dalla query string (es. ?nome_tutorial=Flask).
    nome_tutorial = request.args.get('nome_tutorial')
    # Ottiene il valore del parametro 'oggetto_tutorial'.
    soggetto_tutorial = request.args.get('oggetto_tutorial')
    # Rende il template passando i valori ottenuti.
    return render_template('newpage.html', 
                           nome_tutorial=nome_tutorial, 
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
    """ Classe per la creazione di un form avanzato usando WTForms. """
    nome = StringField('Nome del tutorial', 
                       validators=[DataRequired()])
    pulsante = SubmitField('Invia Dati')
    tutorial_act = BooleanField('Tutorial attivo?')
    difficolta = RadioField('Difficolta del tutorial: ', 
                            choices=[('facile', 'Facile'),
                                     ('medio', 'Medio'), 
                                     ('avanzato', 'Avanzato')])
    sito_tutorial = SelectField('Sito online del tutorial', 
                                choices=[('github','Github'),
                                         ('linkedin', 'Linkedin'),
                                         ('x', 'X'),
                                          ('instagram', 'Instagram'),
                                          ('youtube', 'Youtube')])
    feedback = TextAreaField('Feedback aggiuntivo')
    soggetto = StringField('Soggetto del tutorial')

@app.route('/tutorial/nuovo/base/', methods=['GET', 'POST'])
def form_avanzato():
    # Inizializza le variabili per 
    # il template (saranno usate solo in GET)
    nome = None
    soggetto = None
    tutorial_act = None
    difficolta = None
    sito_tutorial = None
    feedback = None
    # Inizializza il form dalla classe FormBase
    form = FormBase()
    
    # Costruire la logica del form
    if form.validate_on_submit():
        # Quando il form viene inviato e validato:
        # 1. Salva i dati del form nella sessione utente
        session['nome'] = form.nome.data
        session['soggetto'] = form.soggetto.data
        session['tutorial_act'] = form.tutorial_act.data
        session['difficolta'] = form.difficolta.data
        session['sito_tutorial'] = form.sito_tutorial.data
        session['feedback'] = form.feedback.data
        
        # 2. Reindirizza l'utente alla pagina 
        # dei risultati (Pattern Post/Redirect/Get - PRG)
        return redirect(url_for('ressultato'))
    
    # LOGICA ALTERNATIVA: Mostra il form (GET o POST non validato)
    return render_template('tutorialsimpli.html', 
                           # Passa l'oggetto form per il
                           # rendering in Jinja
                           # Passa le variabili 
                           # inizializzate 
                           # (saranno vuote/None 
                           # per la prima visualizzazione)
                           tutorial_form=form, 
                           tutorial_nome=nome,
                           tutorial_soggetto=soggetto,
                           tutorial_attiva=tutorial_act,
                           tutorial_diffi=difficolta,
                           tutorial_sito=sito_tutorial,
                           tutorial_feedback=feedback)

@app.route('/tutorial/ressultato')
def ressultato(): # Recupera i dati salvati nella sessione
    nome = session.get('nome')
    soggetto = session.get('soggetto')
    tutorial_act = session.get('tutorial_act')
    difficolta = session.get('difficolta')
    sito_tutorial = session.get('sito_tutorial')
    feedback = session.get('feedback')
    
    # Rimuove i dati dalla sessione dopo 
    # l'uso (opzionale, ma buona pratica)
    session.pop('nome', None)
    session.pop('soggetto', None)
    session.pop('tutorial_act', None)
    session.pop('difficolta', None)
    session.pop('sito_tutorial', None)
    session.pop('feedback', None)

    # Rende il template di risultato passando i dati recuperati
    return render_template('ressultato.html', 
                           nome=nome, 
                           soggetto=soggetto,
                           tutorial_act=tutorial_act,
                           difficolta=difficolta,
                           sito_tutorial=sito_tutorial,
                           feedback=feedback)

# --- Blocco 7: Avvio dell'Applicazione ---

# Avvia il server di sviluppo. debug=True 
# abilita il ricaricamento automatico.
app.run(debug=True)