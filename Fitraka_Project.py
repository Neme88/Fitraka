import sys
import os
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager, UserMixin
from utils import hash_password, verify_password  # Import password handling functions
from config import Config  # Import your configuration class
# Import models and db
#from app.models.models import db, User
#from app.models.profile_model import profile
#from app.models.track_exercise_model import track_exercise

USER_CREDENTIALS_FILE_PATH = os.path.join(os.getcwd(), 'user_credentials.json')

# Initialize extensions without initializing them
#db = SQLAlchemy()
#migrate = Migrate()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    # Load a user from the database based on their ID
    return User.query.get(int(user_id))


def create_app():
    Fitraka_Project = Flask(__name__)
    Fitraka_Project.config.from_object(Config)

    # Initialize extensions with the app
    #db.init_app(app)
    #migrate.init_app(app, db)
    login_manager.init_app(Fitraka_Project)

    Fitraka_Project.config['USER_CREDENTIALS_FILE_PATH'] = USER_CREDENTIALS_FILE_PATH

    # Enable CORS (Cross-Origin Resource Sharing)
    CORS(Fitraka_Project)

    # Import and register route blueprints
    from routes.landing_route import landing_bp
    from routes.registar_route import register_bp
    from routes.login_route import login_bp
    from routes.logout_route import logout_bp
    from routes.dashboard_route import dashboard_bp
    from routes.profile_route import profile_bp
    from routes.choose_exercises_route import exercise_bp
    from routes.goal_routes import goal_routes_bp
    from routes.exercise_result_route import exercise_result_bp
    from routes.track_exercise_route import track_exercise_bp

    # Blueprint registeration
    Fitraka_Project.register_blueprint(landing_bp)
    Fitraka_Project.register_blueprint(register_bp)
    Fitraka_Project.register_blueprint(login_bp)
    Fitraka_Project.register_blueprint(logout_bp)
    Fitraka_Project.register_blueprint(dashboard_bp)
    Fitraka_Project.register_blueprint(profile_bp)
    Fitraka_Project.register_blueprint(exercise_bp)
    Fitraka_Project.register_blueprint(goal_routes_bp)
    Fitraka_Project.register_blueprint(exercise_result_bp)
    Fitraka_Project.register_blueprint(track_exercise_bp)


    return Fitraka_Project
"""
# Example password hashing
user_password = input ("Enter your password: ")
hashed_password = hash_password(user_password)

# Verify a password
if verify_password(user_password, hashed_password):
    print("Password is valid")
else:
    print("Password is invalid")
"""
# Initialize the app with your configuration class
Fitraka_Project = create_app()

