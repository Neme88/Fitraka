import json
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import check_password_hash

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

        # Read user credentials from the file
        with open('user_credentials.json', 'r') as user_file:
            users = json.load(user_file)

        user = None

        # Find user by username or email
        for u in users:
            if isinstance(u, dict) and ('username' in u or 'email' in u):
                if u['username'] == username_or_email or u['email'] == username_or_email:

                    user = u
                    break

        if user and check_password_hash(user['password_hash'], password):
            # Log in the user
            flash("Login successful!", 'succeed')
            return redirect(url_for('dashboard.dashboard'))

        flash("Wrong login credentials. Please try again.", 'error')

    return render_template('login.html')

