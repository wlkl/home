from flask_wtf import Form
from wtforms.fields import StringField, TextField, PasswordField, SubmitField
from wtforms.validators import ValidationError, Email, InputRequired, Length, DataRequired

class LoginForm(Form):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
