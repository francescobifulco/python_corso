from flask import Flask, render_template

app = Flask(__name__)  # Crea l'app Flask

@app.route('/')        # Definisce una route per la homepage
def hello():
    return render_template('index.html')