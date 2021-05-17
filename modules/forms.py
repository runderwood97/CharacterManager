  
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField
from wtforms.validators import InputRequired, Length
from modules.connections import connection

class Login_Form(FlaskForm):
    identifier = StringField("identifier", validators = [InputRequired(), Length(max = 50)], render_kw = {"placeholder" : "Username or Email"})
    email = StringField("email", validators = [InputRequired()], render_kw = {"placeholder" : "Email"})
    password = PasswordField("password", validators = [InputRequired()], render_kw = {"placeholder" : "Password"})

class Character_Form(FlaskForm):
    pass