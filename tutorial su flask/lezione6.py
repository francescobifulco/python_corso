from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Configurazione del path del database
# L'uso di os.path.abspath(os.getcwd()) assicura che 
# il percorso sia assoluto
base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Configurazione per un database SQLite chiamato 'app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Per disabilitare un avviso

db = SQLAlchemy(app) # Inizializzazione dell'oggetto SQLAlchemy

# Definizione del Modello (Tabella)
class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titolo = db.Column(db.String(100), nullable=False)
    contenuto = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Nota {self.titolo}>'

# Creazione delle tabelle nel database (da eseguire una volta)
with app.app_context():
    db.create_all()

# Route per visualizzare le note
@app.route('/notes')
def list_notes():
    # Query per ottenere tutte le note
    note = Nota.query.all()
    return render_template('notes.html', notes=note)

# Route per aggiungere una nota
@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        titolo = request.form['titolo']
        contenuto = request.form['contenuto']
        
        nuova_nota = Nota(titolo=titolo, contenuto=contenuto)
        db.session.add(nuova_nota) # Aggiunge la nota alla sessione
        db.session.commit() # Salva le modifiche nel database
        
        return redirect(url_for('list_notes'))
        
    return render_template('add_note_form.html')

# Esecuzione dell'applicazione
if __name__ == '__main__':
    # app.run() avvia il server di sviluppo locale.
    # debug=True abilita la modalità debug (utile per lo sviluppo).
    app.run(debug=True)