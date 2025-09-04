# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store (for simplicity)
workouts = []
next_id = 1

@app.route('/')
def home():
    """Home endpoint providing basic API info."""
    return jsonify({
        "message": "Welcome to the ACEest Fitness and Gym API!",
        "version": "1.0"
    })

@app.route('/workouts', methods=['POST'])
def add_workout():
    """Adds a new workout to the list."""
    global next_id
    if not request.json or 'workout' not in request.json or 'duration' not in request.json:
        return jsonify({"error": "Missing workout name or duration in request"}), 400

    try:
        duration = int(request.json['duration'])
    except ValueError:
        return jsonify({"error": "Duration must be an integer"}), 400

    new_workout = {
        "id": next_id,
        "workout": request.json['workout'],
        "duration": duration
    }
    workouts.append(new_workout)
    next_id += 1
    return jsonify(new_workout), 201

@app.route('/workouts', methods=['GET'])
def get_workouts():
    """Retrieves the list of all workouts."""
    return jsonify(workouts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)