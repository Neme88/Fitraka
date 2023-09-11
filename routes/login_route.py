import json
from flask import Blueprint, render_template, request, redirect, url_for, flash

# Create a Blueprint for the login route
login_bp = Blueprint('login', __name__)

# Define the login route
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        username_or_email = data['username_or_email']
        password = data['password']

        # Check if validation is required (you can change this based on your presentation needs)
        validation_required = True  # Change to False to bypass validation

        if validation_required:
            # Validation is required, you can implement proper validation here if needed
            # For demonstration purposes, let's assume any login is successful
            flash("Login successful!", 'succeed')
        else:
            # Validation is bypassed, log in the user without checking credentials
            flash("Login successful without validation!", 'succeed')

        return redirect(url_for('dashboard.dashboard'))

    return render_template('login.html')

