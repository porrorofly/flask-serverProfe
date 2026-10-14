from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email

class LoginForm(FlaskForm):
    #Campos de texto obligatorio para el email de usuario,con validacion formato de 
    email=StringField("Correo electrónico",validators=[DataRequired(),Email()])

    #Campos de texto obligatorio para la contraseña de usuario,con longtitud minima de 6 caracteres
    password=PasswordField("Contraseña",validators=[DataRequired(),Length(min=6)])

    #Botón de envío del formulario
    submit=SubmitField("Iniciar sesión")