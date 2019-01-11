from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_bcrypt import Bcrypt
from flask_argon2 import Argon2
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()
app.config.from_object(Config)
mail = Mail(app)
db = SQLAlchemy(app)
login = LoginManager(app)
#bcrypt = Bcrypt(app)
argon2 = Argon2(app)
migrate = Migrate(app, db)
moment = Moment(app)


from app import routes, models
from app import forms
