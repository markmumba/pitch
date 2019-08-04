from flask import Flask
from forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import User,Post



app = Flask(__name__)
app.config['SECRET_KEY'] = 'markian'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
