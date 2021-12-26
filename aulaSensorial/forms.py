from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrarDocenteForm(FlaskForm):
    nombre = StringField('Nombre',
                           validators=[DataRequired(), Length(min=2, max=75)])
    apellido = StringField('Apellido',
                           validators=[DataRequired(), Length(min=2, max=75)])
    fechaNacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()], format="%d-%m-%y")
    especialidad = StringField('Especialidad',
                           validators=[DataRequired(), Length(min=2, max=75)])
    anioBasica = IntegerField("Año de Básica", validators=[DataRequired()])
    
    nombreUsuario = StringField('Nombre usuario',
                        validators=[DataRequired(), Length(min=2, max=75)])
    
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña',
                                     validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Crear Docente')
    

class RegistrarEstudianteForm(FlaskForm):
    nombre = StringField('Nombre',
                           validators=[DataRequired(), Length(min=2, max=75)])
    apellido = StringField('Apellido',
                           validators=[DataRequired(), Length(min=2, max=75)])
    genero = SelectField('Género',
                           validators=[DataRequired()], choices=[("Masculino", "Masculino"), ("Femenino", "Femenino")])
    fechaNacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()], format="%d-%m-%y")
    diagnostico = StringField('Diagnostico',
                           validators=[Length(min=2, max=125)])
    residencia = StringField('Residencia',
                           validators=[DataRequired(), Length(min=2, max=150)])
    carnet = SelectField('Carnet',
                           validators=[DataRequired()], choices=[("Si", "SI"), ("No", "NO")])
    porcentajeDiscapacidad = IntegerField("Procentaje de Discapacidad")
    escolarizado = SelectField('Escolarizado',
                           validators=[DataRequired()], choices=[("Si", "SI"), ("No", "NO")])
    
    submit = SubmitField('Crear Estudiante')


class LoginForm(FlaskForm):
    nombreUsuario = StringField('Usuario',
                        validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    
    submit = SubmitField('Iniciar Sesion')