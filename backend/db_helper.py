import os
import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

# Read database credentials from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_NAME = os.getenv("DB_NAME", "gym_logger")


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()


def fetch_weights_for_date(start_date, end_date):
    logger.info(f"Fetching weights based on a start_date:{start_date} and end_date:{end_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM weightlogs WHERE logged_at BETWEEN %s AND %s", (start_date, end_date))
        weights = cursor.fetchall()
        return weights
    
def fetch_weight():
    logger.info(f"Fetch everything")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM weightlogs")
        weights = cursor.fetchall()
        return weights
    
def insert_weight(weight, date):
    logger.info(f"insert_weight was called with weight:{weight}, date:{date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO weightlogs (weight_kg, logged_at) VALUES (%s, %s)",
            (weight, date)
        )
        
def delete_at_date(date):
    logger.info(f"delete_at_date was called with date:{date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM weightlogs WHERE logged_at=%s", (date,))
        
def delete_all():
    logger.info(f"Delete everything")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("TRUNCATE TABLE weightlogs")

def delete_day(day_number):
    logger.info(f"Deleting all exercises for day: {day_number}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM exerciselogs WHERE day_number=%s", (day_number,))

def insert_new_exercise(exercise_name, kg, reps, sets, category, day_number):
    logger.info(f"Inserting new exercise: {exercise_name}, {kg}kg, {reps} reps, {sets} sets, category: {category}, day_number: {day_number}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO exerciselogs (exercise_name, kg, reps, sets, category, day_number) VALUES (%s, %s, %s, %s, %s, %s)",
            (exercise_name, kg, reps, sets, category, day_number)
        )
        
def insert_new_day(exercises, day_number):
    logger.info(f"Inserting a new day's worth of exercises ({len(exercises)} total) for day: {day_number}")
    
    # First, delete any existing exercises for this day to reset it
    delete_day(day_number)
    
    with get_db_cursor(commit=True) as cursor:
        # Prepare the list of tuples for executemany, including the day_number
        data_to_insert = [
            (e.exercise_name, e.kg, e.reps, e.sets, e.category, day_number) for e in exercises
        ]
        
        sql = "INSERT INTO exerciselogs (exercise_name, kg, reps, sets, category, day_number) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.executemany(sql, data_to_insert)
    logger.info(f"Batch insertion for day {day_number} successful.")

def fetch_all_exercises():
    logger.info(f"Fetching all exercises")
    
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM exerciselogs")
        exercises = cursor.fetchall()
        
    return exercises