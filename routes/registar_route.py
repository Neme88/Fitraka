from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
import json

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get user data from the registration form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username, email, and password are provided
        if not username or not email or not password:
            flash("Please fill in all fields.", 'error')
            return redirect(url_for('register.register'))

        # Load existing user data from a JSON file or create an empty list if the file doesn't exist
        try:
            with open('user_credentials.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {'users': []}

        # Check if the username or email already exists
        if any(user['username'] == username or user['email'] == email for user in data['users']):
            flash("Username or email already exists. Please choose another.", 'error')
            return redirect(url_for('register.register'))

        else:
            # Hash the password
            password_hash = generate_password_hash(password, method='sha256')

            # Create a new user dictionary
            new_user = {
                'username': username,
                'email': email,
                'password_hash': password_hash
            }

            # Append the new user to the existing data
            data['users'].append(new_user)

            # Save the updated data back to the JSON file
            with open('user_credentials.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            flash("Registration successful! You can now log in.", 'success')
            return redirect(url_for('login.login'))


    #return redirect(url_for('login.login'))
    return render_template('register.html')

