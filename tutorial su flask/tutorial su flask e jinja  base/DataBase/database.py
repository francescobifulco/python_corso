from main import db, Tuto, app

# Tutto ciò che usa il db deve stare dentro il contesto dell'app
with app.app_context():
    # Creazione delle tabelle
    db.create_all()

    # Costruiamo degli oggetti
    flask = Tuto('Flask', 'creazione di siti web', 10)
    gui = Tuto('GUI', 'creazione della GUI di Python', 15)

    # Aggiungiamo alla sessione
    db.session.add(flask)
    db.session.add(gui)

    # Confermiamo le modifiche
    db.session.commit()

    # Visualizziamo gli ID dopo il commit
    print('Id tutorial Flask:', flask.id)
    print('Id tutorial GUI:', gui.id)