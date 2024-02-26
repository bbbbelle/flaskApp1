from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField )
from app import db
from .contact import Contact
import datetime
from wtforms import validators
from wtforms.validators import DataRequired


class BlockEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    message = db.Column(db.String(280), unique=True)
    email = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    date_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, name,message,email,date_created,date_updated):
        self.name = name
        self.message= message
        self.email = email
        self.date_created = date_created
        self.date_updated =date_updated

    def update(self, name,message,email,date_created,date_updated):
        self.name = name
        self.message= message
        self.email = email
        self.date_created = date_created
        self.date_updated =date_updated

class PostForm(FlaskForm):
    message = StringField("Message",validators=[DataRequired()])
    submit = SubmitField("Submit",validators=[DataRequired()])
    