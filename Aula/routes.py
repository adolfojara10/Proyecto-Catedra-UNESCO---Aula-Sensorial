from flask import render_template, url_for, flash, redirect, request
from flask.json import jsonify
from Aula import app, db, bcrypt, idEstudiante, idCategoria
from Aula.forms import LoginForm, RegistrarEstudianteForm, RegistrarDocenteForm, RegistrarJuego
from Aula.models import Estudiante, Docente, Juego, Categoria, Reporte
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
    #estudiantesJSON = (Encoder().encode(est) for est in estudiantes)
    
    
    if request.method == "POST":
        qtc_data =  request.get_json()
        #print(type(qtc_data))
        idEst = int(qtc_data)
        #print(type(idEst))
        global estu 
        estu = Estudiante.query.filter_by(id=idEst).first()
        global idEstudiante
        idEstudiante = estu
        #print(id_estudiante)
        #return redirect(url_for('juegos'))
        #return qtc_data
    
    
        
    return render_template('escogerEstudiante.html', title='Estudiante', estudiantes=estudiantes)



@app.route("/escogerJuego", methods=['GET', 'POST', 'OPTIONS'])
def escogerJuego():
    
    if idEstudiante:
        flash(f'Estudiante {idEstudiante.nombre} {idEstudiante.apellido}!', 'success')
        
        juegos = Juego.query.all()
        
        print(juegos)
        
        '''
        print(juegos)
        if request.method == "POST":
            qtc_data =  request.get_json()
            print(type(qtc_data))
            
            global idCategoria
            
            if len(qtc_data) > 2:
                
                global cat 
                cat = Categoria.query.filter_by(nombre=qtc_data).first()

                idCategoria = cat
                
                print(idCategoria)
                
                return redirect(url_for('juegos'))
            
            else:
                
                idJuego = int(qtc_data)
                
                global juego 
                juego = Juego.query.filter_by(id=idJuego).first()
                                
                idCategoria = juego
                
                print(idCategoria)
                
                return redirect(url_for('juegos'))
                '''
                    
        return render_template('escogerJuego.html', title='Juego', juegos=juegos)
    
    else:     
            
        flash(f'Por favor escoga un estudiante para continuar', 'danger')
        return redirect(url_for('escogerEstudiante'))



@app.route("/procesarJuego", methods=['GET', 'POST', 'OPTIONS'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'], supports_credentials=True)
def procesarJuego():
           
    if request.method == "POST":
       
        qtc_data = request.get_json()
        #print(qtc_data) 
        
        
        cat = Categoria.query.filter_by(nombre=qtc_data)
        print(cat)
        global idCategoria
        idCategoria = cat
                
        
        
        
        '''
        if len(qtc_data) > 2:
            
            print(qtc_data)
            global cat 
            cat = Categoria.query.filter_by(nombre=qtc_data).first()
            idCategoria = cat
                
            print(type(idCategoria), cat)
                
            return redirect(url_for('juegos'))
            
        else:
                
            print(qtc_data)
            idJuego = int(qtc_data)
                
            global juego 
            juego = Juego.query.filter_by(id=idJuego).first()
                                
            idCategoria = juego
                
            print(idCategoria)
                
            return redirect(url_for('juegos'))
               '''     
    

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
                      diagnostico=form.diagnostico.data,  anioBasica=form.anioBasica.data, residencia=form.residencia.data, carnet=form.carnet.data,
                      porcentajeDiscapacidad=form.porcentajeDiscapacidad.data, escolarizado=form.escolarizado.data)
        db.session.add(estu)
        db.session.commit()
        flash('Estudiante creado con exito', 'success')
        return redirect(url_for('home'))
    return render_template('registrarEstudiante.html', title='Register', form=form)



@app.route("/juegos",  methods=['GET', 'POST'])
def juegos():
    
    form = RegistrarJuego()
    
    if form.validate_on_submit():
        
        categorias = form.categorias.data
        
        if categorias != "-":
            
            categorias = categorias.split(',')
            
            juego = Juego(nombre=form.nombre.data)
            
            db.session.add(juego)
            db.session.commit()
            juego = Juego.query.filter_by(nombre=juego.nombre).first()
            
            for cat in categorias:
                
                catego = Categoria(nombre=cat, juego_id=juego.id)
                
                db.session.add(catego)
                
            db.session.commit()
            
            flash(f'Juego: {juego.nombre} creado con exito con sus categorias!', 'success')
            
            print(juego)
            
            return redirect(url_for('escogerJuego'))
            
        else:
            
            juego = Juego(nombre=form.nombre.data)
            
            db.session.add(juego)
            db.session.commit()
            
            flash(f'Juego: {juego.nombre} creado con exito!', 'success')
            
            print(juego)
            
            return redirect(url_for('escogerJuego'))
            
    
    return render_template('RegistrarJuego.html', title='Registrar Juegos', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/about")
def about():
    return render_template('about.html', title='About')
