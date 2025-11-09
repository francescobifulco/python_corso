from main import db, Tuto, app

with app.app_context():
    # CREATE
    pandas = Tuto('Pandas', 'manipolazione di dati', 18)
    db.session.add(pandas)
    db.session.commit()
    
    # READ
    tutorial =Tuto.query.all()
    print("\nTutti i tutorial:")
    print(tutorial)
    
    # SELECT
    selezioni = Tuto.query.get(3)
    print("\nTutorial con ID 3:")
    print(selezioni)
    
    # FILTRO
    selezione_nome = Tuto.query.filter_by(nome='Pandas')
    # Ritorna la query
    print("\nFiltro (query object):", selezione_nome)
    # Ritorna tutti i risultati trovati
    print("Tutti i risultati trovati:", selezione_nome.all()) 
    # Ritorna solamente il primo risultato
    print("Primo risultato trovato:", selezione_nome.first()) 
    
    # UPDATE
    flask = Tuto.query.get(1)
    if flask:
        flask.durata = 5
        db.session.add(flask)
        db.session.commit()
        print("\nTutorial aggiornato:", Tuto.query.get(1))
    else:
        print("\nNessun tutorial con ID 1 trovato per aggiornare.")
    
    print(Tuto.query.get(1))
    
    # DELETE
    rimuove = Tuto.query.filter_by(nome='Pandas').all()
    if rimuove:
        db.session.delete(rimuove[-1])
        db.session.commit()
        print("\nTutorial 'Pandas' rimosso.")
    else:
        print("\nNessun tutorial 'Pandas' trovato da rimuovere.")
