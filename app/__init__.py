from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = 'markian'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

# auth = Blueprint('auth',__name__)

from app import routes
