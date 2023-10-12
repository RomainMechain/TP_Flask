from .app import db
class Author (db.Model ):
    id = db.Column(db.Integer , primary_key =True)
    name = db.Column (db.String (100))
class Book(db.Model ):
    id = db.Column(db.Integer , primary_key =True)
    price = db.Column(db.Float)
    title = db.Column(db.String(100))
    url = db.Column(db.String(200))
    img = db.Column(db.String(200))
    author_id = db.Column(db.Integer,db.ForeignKey("author.id"))
    author = db. relationship ("Author",
        backref =db.backref ("books",lazy="dynamic"))


def get_sample ():
    return Book.query.limit(10).all()