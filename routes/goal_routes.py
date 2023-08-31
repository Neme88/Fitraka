from flask import Blueprint, render_template, request

goal_routes_bp = Blueprint('goal_routes', __name__)

# Define fitness goals and their corresponding exercise suggestions
fitness_goals = {
    "lose_weight": "Take up cardio exercises like jogging or cycling.",
    "keep_fit": "Run or walk for at least 20 minutes a day.",
    "build_muscle": "Incorporate weightlifting exercises into your routine."
}

@goal_routes_bp.route('/set_goal_route', methods=['GET', 'POST'])
def set_goal_route():
    if request.method == 'POST':
        selected_goal = request.form.get('goal')

        if selected_goal in fitness_goals:
            suggestion = fitness_goals[selected_goal]
            return render_template('suggestion.html', suggestion=suggestion)

    return render_template('set_goal.html', goals=fitness_goals.keys())

