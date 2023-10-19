from flask import Flask
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)
import os.path
def mkpath (p):
    return os.path. normpath (
os.path.join(
os.path. dirname ( __file__ ),p))
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "5a2c2f8a-427e-45ca-972d-7e7d976b6589"