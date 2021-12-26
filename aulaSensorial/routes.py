from flask import render_template, url_for, flash, redirect
from aulaSensorial import app
from aulaSensorial.forms import RegistrarDocenteForm, RegistrarEstudianteForm, LoginForm
from aulaSensorial.models import Docente, Estudiante

@app.route('/')
def home():
    form = LoginForm()
       
    
    return render_template('login.html', form=form)

@app.route('/registrarDocente')
def registrarDocente():
    form = RegistrarDocenteForm()
    
    
    return render_template('registroDocente.html', form=form)

@app.route('/registrarEstudiante')
def registrarEstudiante():
    form = RegistrarEstudianteForm()
    
    
    return render_template('registroEstudiante.html', form=form)
