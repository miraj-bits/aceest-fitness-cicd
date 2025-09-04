# ACEest Fitness and Gym - DevOps CI/CD Project by Miraj Kumar (2025ht66045@wilp.bits-pilani.ac.in)


This repository contains the source code and DevOps configuration for the ACEest Fitness and Gym application, developed for the Introduction to DevOps course.

## Overview

This project includes a simple Flask web API for tracking workouts. It is containerized using Docker and features a complete CI/CD pipeline using GitHub Actions that automatically builds and tests the application on every push to the `main` branch.

---

### How to Set Up and Run Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/miraj-bits/aceest-fitness-cicd.git
    cd aceest-fitness-cicd
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Mac/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```bash
    flask run
    ```
    The application will be running at `http://127.0.0.1:5000`.

---

### How to Execute Tests

To run the unit tests locally, ensure you have installed the dependencies (including `pytest`) and then run the following command from the root directory:

```bash
pytest