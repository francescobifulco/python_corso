import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.dialects.sqlite

BASEDIR = os.path.abspath(os.path.dirname(__name__))
print(f'Base Directory: {BASEDIR}')

app = Flask(__name__)

# Configurare il path del DB e alcune informazioni

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + os.path.join(BASEDIR, 'db.sqlite')