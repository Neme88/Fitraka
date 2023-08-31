# Create a new file for your landing page blueprint, e.g., landing_route.py

from flask import Blueprint, render_template

# Create the landing page blueprint
landing_bp = Blueprint('landing', __name__)

# Define the route for the landing page
@landing_bp.route('/')
def landing():
    return render_template('index.html')

