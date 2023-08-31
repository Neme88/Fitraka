from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user
#from app.models.track_exercise_model import track_exercise # Import your TrackExercise model


# Define a Blueprint for the track_exercise route
track_exercise_bp = Blueprint('track_exercise', __name__)

@track_exercise_bp.route('/track_exercise/<exercise>', methods=['GET', 'POST'])
def track_exercise(exercise):
    if request.method == 'POST':
        try:
            # Handle exercise tracking logic here
            duration = float(request.form.get('duration'))

            # Receive the calories_burned value passed from the exercise_result route
            calories_burned = float(request.form.get('calories_burned'))

            # Create a new TrackExercise record with calories_burned
            new_track_exercise = TrackExercise(
                exercise_name=exercise,
                duration_minutes=duration,
                user_id=current_user.id,  # Assuming you're using Flask-Login
                calories_burned=calories_burned  # Set the calories_burned value
            )

            # Add and commit the new record to the database
            db.session.add(new_track_exercise)
            db.session.commit()

            return render_template('exercise_result.html', exercise=exercise, duration=duration, calories_burned=calories_burned)

        except ValueError:
            # Handle the case where duration or calories_burned is not a valid float
            flash("Invalid input value. Please enter valid numbers.", 'error')
            return redirect(url_for('choose_exercise.choose_exercises'))

        except Exception as e:
            # Handle other exceptions if needed
            flash(f"An error occurred: {str(e)}", 'error')
            return redirect(url_for('choose_exercise.choose_exercises'))

    return render_template('track_exercise.html', exercise=exercise)


