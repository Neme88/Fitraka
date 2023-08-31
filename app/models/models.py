from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.models.profile_model import profile
from app.models.track_exercise_model import track_exercise
# Import SQLAlchemy instance and create it
db = SQLAlchemy()

# Import the necessary SQLAlchemy components for defining relationships
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Define the one-to-one relationship with the Profile model
    #profile = db.relationship('profile', backref='user', uselist=False)

    # Define the one-to-many relationship with the TrackExercise model
    #tracked_exercises = db.relationship('track_exercise', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

