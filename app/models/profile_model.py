from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    bio = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), unique=True, nullable=False)
    profile_picture = db.Column(db.String(255))  # Add this line for the profile picture

    def __init__(self, full_name, date_of_birth, gender, bio, user_id, profile_picture):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.bio = bio
        self.user_id = user_id
        self.profile_picture = profile_picture

