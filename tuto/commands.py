import click
from .app import app , db


@app.cli.command()
@click.argument('filename')

def loaddb ( filename ):
    '''Creates the tables and populates them with data.'''

    # création de toutes les tables
    db.create_all()

    # chargement de notre jeu de données
    import yaml
    books = yaml.load(open(filename))

    # import des modèles
    from .models import Author , Book

    # première passe: création de tous les auteurs
    authors = {}
    for b in books:
        a = b["author"]
        if a not in authors :
            o = Author(name=a)
            db.session.add(o)
            authors [a] = o
    db.session.commit()
    # deuxième passe: création de tous les livres
    for b in books:
        a = authors [b["author"]]
        o = Book(price = b["price"],
            title = b["title"],
            url = b["url"],
            img = b["img"],
            author_id = a.idb) 
        db.session.add(o)
    db.session.commit()