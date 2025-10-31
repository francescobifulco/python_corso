from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Ciao mondo!'

@app.route('/contatti')
def contatti():
    return 'Contattaci!'

app.run(debug=True)