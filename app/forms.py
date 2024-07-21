from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    birth_date = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired()])
    phone_number = StringField('Phone Number')
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')])
    submit = SubmitField('Register')