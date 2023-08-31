from flask import Blueprint, render_template, flash, redirect, url_for, request

# Define a Blueprint for the exercise_result route
exercise_result_bp = Blueprint('exercise_result', __name__)

# Define MET values for different exercises
met_values = {
    'Hiking': 4.5,
    'Walking': 3.9,
    'Running': 9.8,
    'Cycling': 7.0,
}

@exercise_result_bp.route('/exercise_result/<exercise>/<duration>', methods=['GET'])
def exercise_result(exercise, duration):
    try:
        # Ensure duration is a valid float
        duration = float(duration)

        # Calculate calories burned using MET value and duration
        if exercise in met_values:
            met = met_values[exercise]
            calories_burned = met * duration / 60.0  # Assuming duration is in minutes
        else:
            # Handle the case where the exercise is not in the MET values dictionary
            flash("Exercise not found in MET values.", 'error')
            return redirect(url_for('choose_exercise.choose_exercises'))

        # Pass the calories_burned value to the track_exercise route
        return redirect(url_for('track_exercise.track_exercise', exercise=exercise, duration=duration, calories_burned=calories_burned))

    except ValueError:
        # Handle the case where duration is not a valid float
        flash("Invalid duration value. Please enter a valid number.", 'error')
        return redirect(url_for('choose_exercise.choose_exercises'))

    except Exception as e:
        # Handle other exceptions if needed
        flash(f"An error occurred: {str(e)}", 'error')
        return redirect(url_for('choose_exercise.choose_exercises'))


