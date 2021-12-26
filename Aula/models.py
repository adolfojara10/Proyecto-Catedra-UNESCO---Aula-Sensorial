from datetime import date
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
    
    #reportes = db.relationship('Reporte', backref='tutor', lazy=True)
    
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
        return f"Estudiante('{self.nombre}', '{self.apellido}', '{self.fechaNacimiento}', '{self.residencia}', '{self.diagnostico}')"
