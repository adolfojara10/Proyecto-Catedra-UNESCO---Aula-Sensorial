from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Aula.models import Docente, Estudiante


class RegistrarDocenteForm(FlaskForm):
    nombre = StringField('Nombre',
                           validators=[DataRequired(), Length(min=2, max=75)])
    apellido = StringField('Apellido',
                           validators=[DataRequired(), Length(min=2, max=75)])
    fechaNacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    especialidad = StringField('Especialidad')
    anioBasica = IntegerField("Año de Básica", validators=[DataRequired()])
    
    nombreUsuario = StringField('Nombre usuario',
                        validators=[DataRequired(), Length(min=2, max=75)])
    
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña',
                                     validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Crear Docente')
    
    def validate_username(self, username):
        user = Docente.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    

class RegistrarEstudianteForm(FlaskForm):
    nombre = StringField('Nombre',
                           validators=[DataRequired(), Length(min=2, max=75)])
    apellido = StringField('Apellido',
                           validators=[DataRequired(), Length(min=2, max=75)])
    genero = SelectField('Género',
                           validators=[DataRequired()], choices=[("Masculino", "Masculino"), ("Femenino", "Femenino")])
    fechaNacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    anioBasica = IntegerField("Año de Básica", validators=[DataRequired()])
    diagnostico = StringField('Diagnostico')
    residencia = StringField('Residencia',
                           validators=[DataRequired(), Length(min=2, max=150)])
    carnet = SelectField('Carnet', choices=[("Si", "SI"), ("No", "NO")])
    porcentajeDiscapacidad = IntegerField("Procentaje de Discapacidad", default=0)
    escolarizado = SelectField('Escolarizado',
                           validators=[DataRequired()], choices=[("Si", "SI"), ("No", "NO")])
    
    submit = SubmitField('Crear Estudiante')


class LoginForm(FlaskForm):
    nombreUsuario = StringField('Usuario',
                        validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    
    submit = SubmitField('Iniciar Sesion')
    

class RegistrarJuego(FlaskForm):
    
    nombre = StringField('Nombre del Juego',
                        validators=[DataRequired()])
    
    categorias = TextAreaField('Categorias. Ej: Dado,Luces(Separar con una coma y sin espacios)', description='En caso de que sean varias categorias, separarlar por una coma. Ej: Dado, Luces', default="-")
    
    submit = SubmitField('Crear Juego')
    