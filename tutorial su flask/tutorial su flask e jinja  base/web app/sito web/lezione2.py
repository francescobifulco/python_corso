import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
#from flask_migrate import Migrate

app = Flask(__name__)

Bootstrap(app)

app.config['SECRET_KEY'] = 'imieisegreti'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Avviare il server solo quando il file viene eseguito direttamente.
    app.run(debug=True)