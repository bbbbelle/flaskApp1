from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from app import db
from .contact import Contact

class BlockEntry(db.Model, UserMixin):
    __tablename__ = "auth_users"
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    message = db.Column(db.String(280))
    email = db.Column(db.String(50))
    # avatar_url = db.Column(db.String(100))


    def __init__(self, name, message, email):
        self.name = name
        self.message = message
        self.email = email
        # self.avatar_url = avatar_url



    
    