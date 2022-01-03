from datetime import date
from sqlalchemy.orm import backref
from Aula import db, login_manager
from flask_login import UserMixin 


@login_manager.user_loader
def load_user(docente_id):
    return Docente.query.get(int(docente_id))

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
    anioBasica = db.Column(db.Integer, nullable=False)
    residencia = db.Column(db.String(150), nullable=False)
    carnet = db.Column(db.String(2), nullable=False)
    porcentajeDiscapacidad = db.Column(db.Integer, nullable=True)
    escolarizado = db.Column(db.String(2), nullable=False)
    
    reportes = db.relationship('Reporte', backref='estudiante', lazy=True)
    
    def __repr__(self) -> str:
        return f"Estudiante('{self.nombre}', '{self.apellido}', '{self.fechaNacimiento}', '{self.residencia}', '{self.diagnostico}')"


class Juego(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(75), nullable=False, unique=True)
    
    categorias = db.relationship('Categoria', backref='juego', lazy=True)
    reportes = db.relationship('Reporte', backref='juego', lazy=True)
    
    
    def __repr__(self) -> str:
        return f"Juego('{self.nombre}')"


class Categoria(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(75), nullable=False)
    
    juego_id = db.Column(db.Integer, db.ForeignKey('juego.id'), nullable=False)
    reportes = db.relationship('Reporte', backref='categoria', lazy=True)
    
    
    def __repr__(self) -> str:
    
        return f"Categoria('{self.nombre}','{self.juego_id}')"
    
    
    
class Reporte(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.String(2), nullable=False)
    fecha = db.Column(db.Date, nullable=False, default=date.today())
    
    docente_id = db.Column(db.Integer, db.ForeignKey('docente.id'), nullable=False)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.id'), nullable=False)
    
    juego_id = db.Column(db.Integer, db.ForeignKey('juego.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=True)
    
    def __repr__(self) -> str:
        return f"Reporte('{self.docente_id}', '{self.estudiante_id}', '{self.juego_id}', '{self.calificacion}')"
