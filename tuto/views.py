from .app import app
from flask import render_template
from .models import get_sample,get_author

@app.route("/")
def home():
    return render_template(
        "home.html",
        title="My Books !",
        books=get_sample())

@app.route("/detail/<id>")
def detail(id):
    books = get_sample()
    book = books[int(id)-1]
    print(book)
    return render_template(
    "detail.html",book=book)

from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField
from wtforms.validators import DataRequired

class AuthorForm ( FlaskForm ):
    id = HiddenField('id')
    name = StringField('Nom', validators =[DataRequired()])
@app.route("/edit/author/<int:id>")
def edit_author(id):
    a = get_author(id)
    f = AuthorForm(id=a.id , name=a.name)
    return render_template("edit-author.html",author =a, form=f)

from flask import url_for , redirect
from .app import db
from .models import Author

@app.route("/save/author/", methods =("POST",))
def save_author ():
    a = None
    f = AuthorForm ()
    if f.validate_on_submit():
        id = int(f.id.data)
        a = get_author(id)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('one_author', id=a.id))
    a = get_author(int(f.id.data))
    return render_template("edit-author.html",author =a, form=f)