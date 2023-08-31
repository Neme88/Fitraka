from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.profile_model import profile # Import the User model

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        data = request.form
        current_user.username = data['username']
        current_user.email = data['email']
        current_user.age = data['age']
        current_user.gender = data['gender']

        # Update the profile, bio, and profile picture columns for the current user
        current_user.profile = data['profile']
        current_user.bio = data['bio']
        current_user.profile_picture = data['profile_picture']

        db.session.commit()
        flash("Profile updated successfully!", 'success')
        return redirect(url_for('profile.profile'))

    return render_template('profile.html')

