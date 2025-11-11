from lezione2 import db
from sqlalchemy import asc

# Tabella di associazione molti-a-molti
tags = db.Table(
    'tutorial_tags',
    db.Column('tutorial_id', 
              db.Integer, 
              db.ForeignKey('tutorial.id'), 
              primary_key=True),
    db.Column('tag_id',
              db.Integer,
              db.ForeignKey('tag.id'),
              primary_key=True)
)

class Tutorial(db.Model):
    __tablename__ = 'tutorial'
    
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    soggetto = db.Column(db.String(100))
    descrizione = db.Column(db.String(255))
    num_lezioni = db.Column(db.Integer())
    livello = db.Column(db.String(100))
    
    # relationship pluralizzata per coerenza con l'uso di self.lezioni in __init__
    lezioni = db.relationship('Lezioni', 
                              order_by='Lezioni.data', 
                              backref='tutorial', 
                              lazy='subquery')
    
    tag = db.relationship('Tag',
                          backref='tutorials',
                          lazy=True,
                          secondary=tags)
    
    def __init__(self, nome, soggetto, descrizione, lezioni, livello):
        self.nome = nome
        self.soggetto = soggetto
        self.descrizione = descrizione
        self.livello = livello
        # il costruttore accetta il numero di lezioni o una lista a seconda
        # dell'utilizzo; qui manteniamo l'attributo coerente con la relationship
        self.lezioni = lezioni
    
    def __repr__(self):
        return (f"""Tutorial: {self.nome}, 
                    soggetto: {self.soggetto}, 
                    livello: {self.livello}""")

class Tag(db.Model):
    __tablename__ = 'tag'
    
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(255), unique=True, nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
        
    def __repr__(self):
        return f'Tag: {self.nome}, id: {self.id}'