import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.dialects.sqlite

BASEDIR = os.path.abspath(os.path.dirname(__name__))
print(f'Base Directory: {BASEDIR}')

app = Flask(__name__)

# Configurare il path del DB e alcune informazioni

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# Aggiungiamo sqlalchemy all' applicazione

db = SQLAlchemy(app)


# Definizione tutorial

class Tuto(db.Model):
    # Nome della tabella
    __tablename__ = 'nome'
    
    # Definizione della struttura della tabella
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    soggetto = db.Column(db.Text)
    lezioni = db.Column(db.Integer)
    
    # Definire il costruttore
    def __init__(self, nome, soggetto, lezioni):
        self.nome = nome
        self.soggetto = soggetto
        self.lezioni = lezioni
    
    # Definiamo il print dell'oggetto
    def __repr__(self):
        messaggio = f'Il tutorial: {self.nome}\n il soggetto del tutorial e: {self.soggetto}\n e le lezioni durano {self.lezioni}\n con il id {self.id}'
        return messaggio
    