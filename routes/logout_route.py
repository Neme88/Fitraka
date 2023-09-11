# logout_route.py

from flask import Blueprint, render_template, flash, get_flashed_messages
from flask_login import logout_user, login_required

# Create a Blueprint for the logout route
logout_bp = Blueprint('logout', __name__)

# Define the logout route
@logout_bp.route('/logout')
# @login_required
def logout():
    logout_user()
    flash("Logout successful!", 'success')
    messages = get_flashed_messages()  # Retrieve flashed messages
    return render_template('logout.html', messages=messages)  # Pass messages to the template

