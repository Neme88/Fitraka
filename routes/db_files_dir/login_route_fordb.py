# login_route.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import check_password_hash
from app.models.profile_model import profile
from app.models.models import db, User
# Import your User model and other necessary modules

# Create a Blueprint for the login route
login_bp = Blueprint('login', __name__)

# Define the login route
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username_or_email = data['username_or_email']
        password = data['password']

        # Check if username/email and password are provided
        if not username_or_email or not password:
            flash("Sorry, you can't skip any field. Please try again.", 'error')
            return redirect(url_for('login.login'))

        # Find user by username or email
        user = User.query.filter_by(username=username_or_email).first() or \
               User.query.filter_by(email=username_or_email).first()

        if not user or not check_password_hash(user.password_hash, password):
            flash("Wrong login credentials. Please try again.", 'error')
        else:
            # Log in the user
            login_user(user)
            flash("Login successful!", 'success')
            return redirect(url_for('dashboard.dashboard'))

    return render_template('login.html')

