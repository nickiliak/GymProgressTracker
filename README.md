# Gym Progress Tracker

A simple web app to log and track your workouts. It consists of three main parts working together to store your data and visualize your progress.

---

## Technology Stack

- **Frontend:** Streamlit – interactive UI for entering and viewing data.  
- **Backend:** FastAPI – handles data requests and serves API endpoints.  
- **Database:** MySQL – stores all your exercise and weight data.  

---

## Quality and Automation

- **Logging:** Uses Python's `logging` module to track important events like data insertions and deletions, aiding debugging and monitoring.  
- **Testing:** Uses Pytest for unit and integration tests to ensure core functions work as expected.  
- **Continuous Integration (CI):** GitHub Actions automatically runs tests on every code change, keeping the codebase stable.  

---

## Docker Support

This project can be run entirely with Docker, eliminating the need to manually install Python, dependencies, or MySQL. With Docker Compose, you can start all services with a single command:

```bash
docker-compose up --build
```

This will:

1. Launch a MySQL database container with your schema.
2. Start the FastAPI backend container.
3. Start the Streamlit frontend container.
4. Automatically handle inter-service communication.

To stop all services:

```bash
docker-compose down
```

> You can still run the project manually without Docker if preferred.  

---

## How It Works

The app communicates between three layers:

1. **Frontend:** Streamlit UI where you input your workouts or view analytics.  
2. **Backend:** FastAPI handles incoming requests, queries the database, and returns results.  
3. **Database:** MySQL stores all your logged exercises and weight updates.  

When you submit data, the frontend sends requests to the backend. The backend saves or retrieves data from the database and sends it back for visualization.

---

## Key Features

### Program Builder
Log your workouts by adding or deleting workout days and exercises (name, weight, sets, reps, category). Submit the whole day's workout at once.

### Program Analytics
Visualize your workouts with pie charts showing exercise distribution by category.

### Weight Update
Log or update your weight entries.

### Weight Analytics
View weight progress over time with automatic chart generation.

---

## Running Without Docker

### Prerequisites
- Python 3.7+
- A running MySQL server
- Command-line interface

### Step 1: Check the database.
Make sure to use the database in tests/schema.sql

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Backend

```bash
uvicorn backend.server:app --reload
```

### Step 4: Run the Frontend

```bash
streamlit run frontend/app.py
```

The application will open in your web browser and you’ll be ready to log workouts.
