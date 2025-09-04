# test_app.py
import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    """Test the home page."""
    res = client.get('/')
    assert res.status_code == 200
    assert b"Welcome to the ACEest Fitness and Gym API!" in res.data

def test_get_workouts_initially_empty(client):
    """Test that workouts are initially empty."""
    res = client.get('/workouts')
    assert res.status_code == 200
    assert res.json == []

def test_add_workout(client):
    """Test adding a new workout."""
    # First, clear the list for a clean test
    from app import workouts
    workouts.clear()

    res = client.post('/workouts', json={"workout": "Running", "duration": 30})
    assert res.status_code == 201
    assert res.json['workout'] == "Running"
    assert res.json['duration'] == 30

    # Verify it was added
    res_get = client.get('/workouts')
    assert len(res_get.json) == 1
    assert res_get.json[0]['workout'] == "Running"

def test_add_workout_bad_request(client):
    """Test adding a workout with missing data."""
    res = client.post('/workouts', json={"workout": "Pushups"})
    assert res.status_code == 400
    assert b"Missing workout name or duration" in res.data