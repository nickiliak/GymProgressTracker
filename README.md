# Project Description: Gym Progress Tracker
This project is a simple web app that helps you log and track your workouts. It's built with three main parts that work together to store your data and show you your progress.

## Technology
This project uses:

Streamlit for the frontend, which is the part you see and interact with.

FastAPI for the backend, which is the server that handles data requests.

MySQL for the database, which is where all your exercise data is stored.

## Quality and Automation
To ensure the project is reliable and maintainable, a few key practices were implemented:

Logging: The application uses Python's logging module to track important events, such as data insertions and deletions. This is crucial for debugging and monitoring.

Testing with Pytest: Pytest is used for basic unit and integration testing to ensure core functions work as expected.

Continuous Integration (CI): The project is set up with GitHub Actions for CI. This automatically runs the tests on every code change, ensuring the code remains stable and functional.

## How It Works
The app works by sending information between the parts. When you enter data and click a button on the Streamlit frontend, it sends a request to the FastAPI backend. The backend then saves that information to the MySQL database. When you want to see your progress, the backend retrieves the data from the database and sends it back to the frontend to display it.

## Key Features
### Program Builder
This is where you log your workouts. You can easily add or delete workout days and enter details for each exercise, like the name, weight, sets, and reps. When you're done, you can submit the whole day's workout at once.
 <img width="1367" height="1364" alt="program_builder" src="https://github.com/user-attachments/assets/1296767d-14a6-443f-9289-340db62b24e4" />
 
### Program Analytics
This feature helps you visualize your workout data. It pulls all your logged exercises from the database and creates a pie chart to show you the distribution of your exercises by category, so you can see which muscle groups you focus on most.
<img width="1355" height="1150" alt="program_analytics" src="https://github.com/user-attachments/assets/0be7fbfe-7536-4f7c-94cd-9c575c8f797a" />

### Weight Update
This is where you can log or edit your weight.
  <img width="1030" height="1001" alt="update_weight" src="https://github.com/user-attachments/assets/17b3231b-41ad-4a25-bc16-68ff9d1def12" />

### Weight Analytics
Visualization of your weight over time period.
<img width="1216" height="1104" alt="weight_analytics" src="https://github.com/user-attachments/assets/016c6cdd-768d-481f-97b0-07ce0ef37b76" />

## How to Run the Project
Prerequisites
Python 3.7+

A running MySQL server

A command-line interface

### Step 1: Set up the Database
Connect to your MySQL server and run this code to create the database and table:

CREATE DATABASE gym_logger;

USE gym_logger;

CREATE TABLE `exerciselogs` (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    exercise_name VARCHAR(255) NOT NULL,
    kg FLOAT,
    reps INT,
    sets INT,
    category VARCHAR(255) NOT NULL,
    day_number INT NOT NULL
);



### Step 2: Install Dependencies
Open your terminal, go to the project folder, and install the required libraries using the requirements.txt file:

pip install -r requirements.txt



### Step 3: Run the Backend
In one terminal, start the backend server:

uvicorn backend.server:app --reload



### Step 4: Run the Frontend
In a new terminal, run the Streamlit app:

streamlit run frontend/app.py



The application will open in your web browser, and you'll be ready to start logging your workouts.
