import datetime
import mysql.connector
import random
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="gym_logger"
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
        cursor.execute("SELECT * FROM WeightLogs WHERE logged_at BETWEEN %s AND %s", (start_date, end_date))
        weights = cursor.fetchall()
        return weights
    
def fetch_weight():
    logger.info(f"Fetch everything")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM WeightLogs")
        weights = cursor.fetchall()
        return weights
    
def insert_weight(weight, date):
    logger.info(f"insert_weight was called with weight:{weight}, date:{date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO WeightLogs (weight_kg, logged_at) VALUES (%s, %s)",
            (weight, date)
        )
        
def delete_at_date(date):
    logger.info(f"delete_at_date was called with date:{date,}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM WeightLogs WHERE logged_at=%s", (date,))
        
def delete_all():
    logger.info(f"Delete everything")
    with get_db_cursor() as cursor:
        cursor.execute("TRUNCATE TABLE WeightLogs")

# if __name__ == "__main__":
#     delete_all()
#     value = 70
#     for i in range(1, 30):
#         chance = 0.4
#         if random.random() < chance:  # random.random() returns float [0.0, 1.0)
#             increment = random.uniform(0.1, 0.5)  # small increment
#             value += increment
            
#         insert_weight(value, datetime.date(2025, 9, i))
