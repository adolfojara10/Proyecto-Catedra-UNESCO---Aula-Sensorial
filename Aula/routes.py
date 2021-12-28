from flask import render_template, url_for, flash, redirect, request
from flask.json import jsonify
from Aula import app, db, bcrypt, id_estudiante
from Aula.forms import LoginForm, RegistrarEstudianteForm, RegistrarDocenteForm
from Aula.models import Estudiante, Docente, Encoder
from flask_login import login_user, current_user, logout_user, login_required
from datetime import date
import json
from flask_cors import cross_origin


@app.route("/", methods=['GET', 'POST'])
def home():
    
    if current_user.is_authenticated:
        return redirect(url_for('escogerEstudiante'))
    form = LoginForm()
    if form.is_submitted():
        doc = Docente.query.filter_by(nombreUsuario=form.nombreUsuario.data).first()
        if doc and bcrypt.check_password_hash(doc.contrasenia, form.password.data):
            login_user(doc)
            flash('Login successful!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('home.html', title='Login', form=form)


@app.route("/escogerEstudiante", methods=['GET', 'POST', 'OPTIONS'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'], supports_credentials=True)
def escogerEstudiante():
    
    estudiantes = Estudiante.query.all()
    estudiantesJSON = (Encoder().encode(est) for est in estudiantes)
    
    """
    if ( request.args.get('value') != None):
        name=request.args.get('value')
        print('name',name)
        return jsonify({'reply':'success'})
    """
    #estudiantesJSON = json.dumps(estudiantes)
    
    #print(estudiantes[0].id)
    
    """
    if request.method == 'post':
        js_variable = request.form
        print(js_variable)
"""
    
    return render_template('escogerEstudiante.html', title='Estudiante', estudiantes=estudiantes, estudiantesJSON=estudiantesJSON)


#@cross_origin(origin='localhost',headers=['Content- Type','Authorization'], supports_credentials=True)
@app.route("/procesando", methods=['GET','POST'])
def procesando():
    
    if request.method == "POST":
        qtc_data =  request.get_json()
        print(type(qtc_data))
        idEst = int(qtc_data)
        print(type(idEst))
        estu = Estudiante.query.filter_by(id=idEst).first()
        
        print(estu)
        return qtc_data
    
    #information = request.data
    
    
    
    #name = request.form.get('name')
    
    """
    jsdata = request.form['javascript_data']
    print(jsdata)
    
    
    name=request.args.get('value')
    print('name',name)
    return jsonify({'reply':'success'})
    """
    
@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/registrarDocente", methods=['GET', 'POST'])
def registrarDocente():
    
    if current_user.is_authenticated:
            return redirect(url_for('escogerEstudiante'))
    form = RegistrarDocenteForm()
    
    if form.is_submitted():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        doc = Docente(nombre=form.nombre.data, apellido=form.apellido.data, fechaNacimiento=date.today(),
                      especialidad=form.especialidad.data, anioBasica=form.anioBasica.data, nombreUsuario=form.nombreUsuario.data,
                      contrasenia=hashed_password)
        db.session.add(doc)
        db.session.commit()
        flash('Docente creado con exito', 'success')
        return redirect(url_for('home'))
    
    return render_template('registrarDocente.html', title='Register', form=form)

@app.route("/registrarEstudiante", methods=['GET', 'POST'])
def registrarEstudiante():
    form = RegistrarEstudianteForm()
    
    if form.is_submitted():
        
        estu = Estudiante(nombre=form.nombre.data, apellido=form.apellido.data, genero=form.genero.data, fechaNacimiento=date.today(),
                      diagnostico=form.diagnostico.data, residencia=form.residencia.data, carnet=form.carnet.data,
                      porcentajeDiscapacidad=form.porcentajeDiscapacidad.data, escolarizado=form.escolarizado.data)
        db.session.add(estu)
        db.session.commit()
        flash('Estudiante creado con exito', 'success')
        return redirect(url_for('home'))
    return render_template('registrarEstudiante.html', title='Register', form=form)


@app.route("/juegos")
def juegos():
    return render_template('juegos.html', title='Juegos')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))