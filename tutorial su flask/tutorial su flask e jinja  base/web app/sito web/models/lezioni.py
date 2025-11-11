from lezione2 import db

class Lezioni(db.Model):
    __tablename__ = 'lezioni'
    __table_args__ = (db.UniqueConstraint('id', 
                                          'data', 
                                          name='constraint_lezioni'),)
    
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descrizione = db.Column(db.String(255), nullable=False)
    # usare Date qui perché il codice passa oggetti datetime.date
    data = db.Column(db.Date())
    tutorial_id = db.Column(db.Integer(), db.ForeignKey('tutorial.id'))
    
    def __init__(self, nome, descrizione, data):
        self.nome = nome
        self.descrizione = descrizione
        self.data = data
    
    def __repr__(self):
        return f'''Lezioni: {self.nome},
                 descrizioni: {self.descrizione} 
                 in data: {self.data}'''