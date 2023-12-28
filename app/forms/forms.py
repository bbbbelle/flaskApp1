from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField,EmailField,PasswordField )
from wtforms import validators
from wtforms.validators import InputRequired, Length





class RegistrationForm(FlaskForm):
    Username = StringField('Username', validators=[InputRequired(),
                                             Length(min=2,max=20)])
    Email = EmailField('Email', validators=[InputRequired(),
                                             validators.Email(message='Invalid Email')])
    
    Password = PasswordField('Password', validators=[InputRequired(),
                                             Length(min=1),validators.Regexp(r'.*\d.*', message='Password must contain at least one number')])
    Confirm_Password = PasswordField('Confirm Password', validators=[InputRequired(),
                                             Length(min=1), validators.EqualTo('Password', message='Passwords must match')])


 