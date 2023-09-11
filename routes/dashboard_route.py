# dashboard.py

from flask import Blueprint, render_template
from flask_login import login_required


dashboard_bp = Blueprint('dashboard', __name__)

# Define the routes dictionary as you provided
routes = [
    {'name': 'Choose Exercise', 'url': '/choose-exercise'},
    {'name': 'Exercise Result', 'url': '/exercise_result/<exercise>/<duration>'},
    {'name': 'Set Goals', 'url': '/set_goal_route'},
    {'name': 'Logout', 'url': '/logout'},
    {'name': 'Profile', 'url': '/profile'},
    {'name': 'Track Exercise', 'url': '/track_exercise/<exercise>'},
]

@dashboard_bp.route('/dashboard')
# @login_required
def dashboard():
    return render_template('dashboard.html', routes=routes)



