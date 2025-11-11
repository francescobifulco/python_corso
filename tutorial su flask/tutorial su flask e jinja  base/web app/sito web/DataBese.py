from lezione2 import db, app
# usare import locali (la cartella si chiama 'sito web' e non esiste il pacchetto sitoweb)
from models.tutorial import Tutorial, Tag
from models.lezioni import Lezioni

import datetime

with app.app_context():
    # Creazione tabelle
    db.create_all()

    # Creazione Tag
    tag1 = Tag('Flask')
    tag2 = Tag('Pygame')
    tag3 = Tag('Sviluppo web')
    tag4 = Tag('Videogame')
    tag5 = Tag('Divertente')

    db.session.add_all([tag1, tag2, tag3, tag4, tag5])
    db.session.commit()

    # Creazione Tutorial
    tutorial_flask = Tutorial(
        'Flask', 'sito web', 
        'un tutorial su come creare un sito', 12, 'base'
    )

    tutorial_pygame = Tutorial(
        'Pygame', 'giochi', 'sviluppare dei giochi', 4, 'base'
    )

    # Associazione tag
    tutorial_flask.tag = [tag1, tag3]
    tutorial_pygame.tag = [tag2, tag4, tag5]

    db.session.add_all([tutorial_flask, tutorial_pygame])
    db.session.commit()

    # Creazione Lezioni
    lezioni1 = Lezioni('Flask Lezione 1', 
                       'Introduzione a Flask',
                       datetime.date(2025, 11, 12))
    lezioni2 = Lezioni('Flask Lezione 2', 
                       'Form con Jinja', 
                       datetime.date(2025, 10, 19))
    lezioni3 = Lezioni('Pygame Lezione 1', 
                       'Introduzione', 
                       datetime.date(2025, 12, 25))

    # Collegamento Lezioni → Tutorial
    flask = Tutorial.query.filter_by(nome='Flask').first()
    pygame = Tutorial.query.filter_by(nome='Pygame').first()

    lezioni1.tutorial_id = flask.id
    lezioni2.tutorial_id = flask.id
    lezioni3.tutorial_id = pygame.id

    db.session.add_all([lezioni1, lezioni2, lezioni3])
    db.session.commit()
    
    # CHECK - Stampa leggibile
    tutorials = Tutorial.query.all()

    print("\n📘 Lista dei Tutorial:\n")
    for t in tutorials:
        print(f"👉 {t.nome} ({t.livello}) — {t.soggetto}")
        print(f"🏷️ Tag: {[tag.nome for tag in t.tag]}")
        
        # Lezioni ordinate per data per OGNI tutorial
        lezioni = Lezioni.query.filter_by(tutorial_id=t.id).order_by(Lezioni.data.asc()).all()
        if lezioni:
            for l in lezioni:
                print(f" 📅 {l.data}: {l.nome} — {l.descrizione}")
        else:
            print(" ⚠️ Nessuna lezione trovata.")
    print()
