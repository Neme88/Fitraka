from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class track_exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(100), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    date_tracked = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    calories_burned = db.Column(db.Float, nullable=True)  # Add calories_burned column
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    def __init__(self, exercise_name, duration_minutes, user_id, calories_burned=None):
        self.exercise_name = exercise_name
        self.duration_minutes = duration_minutes
        self.user_id = user_id
        self.calories_burned = calories_burned


