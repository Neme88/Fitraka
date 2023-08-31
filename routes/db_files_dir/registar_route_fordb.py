from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from passlib.hash import sha256_crypt
from app.models.profile_model import profile
from app.models.models import db, User
registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        username = data['username']
        email = data['email']
        password = data['password']

        # Validate input
        if not username or not email or not password:
            flash('All fields are required', 'error')
            return redirect(url_for('registration.register'))

        # Check if username already exists
        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            flash('Username already exists', 'error')
            return redirect(url_for('registration.register'))

        # Check if email already exists
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already exists', 'error')
            return redirect(url_for('registration.register'))

        # Hash the password using Passlib's sha256_crypt
        hashed_password = sha256_crypt.hash(password)

        # Create user in the database
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Your registration was successful', 'success')
        return redirect(url_for('auth.login'))

    # Retrieve flashed messages here
    messages = get_flashed_messages()  # Add this line
    return render_template('register.html', messages=messages)  # Pass messages to the template

