from flask import Blueprint, render_template
from flask_login import login_required

exercise_bp = Blueprint('exercise', __name__)

@exercise_bp.route('/choose-exercise')
@login_required
def choose_exercise():
    # List of available exercises
    exercises = ['Hiking', 'Walking', 'Running', 'Cycling']

    return render_template('choose_exercise.html', exercises=exercises)
