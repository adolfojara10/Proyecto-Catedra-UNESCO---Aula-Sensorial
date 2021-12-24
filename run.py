from datetime import datetime 
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from forms import RegistrarDocente, RegistrarEstudiante, LoginForm
#from AulaSensorial import db, login_manager
#from flask import current_app
from flask_login import UserMixin
#from itsdangerous import TimedJSONWebSignatureSerializer as serializer

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SECRET_KEY'] = '917dd64aa8e7d27e920a93e9f298f6be715aa320'

#the connection with bbdd: /// -> are a relative path to the current file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Docente(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(75), nullable=False)
    apellido = db.Column(db.String(75), nullable=False)
    fechaNacimiento = db.Column(db.Date, nullable=False)
    especialidad = db.Column(db.String(75), nullable=False)
    anioBasica = db.Column(db.Integer, nullable=False)
    nombreUsuario = db.Column(db.String(75), unique=True, nullable=False)
    contrasenia = db.Column(db.String(60), nullable=False)
    
    reportes = db.relationship('Reporte', backref='tutor', lazy=True)
    
    def __repr__(self) -> str:
        return f"Docente('{self.nombre}', '{self.apellido}', '{self.nombreUsuario}')"
    

class Estudiante(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(75), nullable=False)
    apellido = db.Column(db.String(75), nullable=False)
    genero = db.Column(db.String(15), nullable=False)
    fechaNacimiento = db.Column(db.Date, nullable=False)
    diagnostico = db.Column(db.String(125), nullable=True)
    residencia = db.Column(db.String(150), nullable=False)
    carnet = db.Column(db.String(2), nullable=False)
    porcentajeDiscapacidad = db.Column(db.Integer, nullable=True)
    escolarizado = db.Column(db.String(2), nullable=False)
    
    def __repr__(self) -> str:
        return f"Docente('{self.nombre}', '{self.apellido}', '{self.fechaNacimiento}', '{self.residencia}', '{self.diagnostico}')"

        

@app.route('/')
def home():
    form = LoginForm()
       
    
    return render_template('login.html', form=form)

@app.route('/registrarDocente')
def registrarDocente():
    form = RegistrarDocente()
    
    
    return render_template('registroDocente.html', form=form)

@app.route('/registrarEstudiante')
def registrarEstudiante():
    form = RegistrarEstudiante()
    
    
    return render_template('registroEstudiante.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)