from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SECRET_KEY'] = '917dd64aa8e7d27e920a93e9f298f6be715aa320'

#the connection with bbdd: /// -> are a relative path to the current file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from aulaSensorial import routes