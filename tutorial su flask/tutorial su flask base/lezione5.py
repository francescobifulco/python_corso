from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Se la richiesta è POST, l'utente ha inviato il form.
        username = request.form.get('username') # Ottiene il valore del campo 'username'
        password = request.form.get('password') # Ottiene il valore del campo 'password'
        
        # Logica di autenticazione (ad es. verifica nel DB)
        if username == 'admin' and password == '1234':
            # Reindirizza l'utente a un'altra pagina dopo il login
            # url_for('index') genera l'URL per la 
            # funzione con quel nome
            return redirect(url_for('index')) 
        else:
            return "Credenziali non valide!"

    # Se la richiesta è GET, mostra il form di login.
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)