import datetime
import mysql.connector
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

def fetch_weight_date_range(start_date, end_date):
    logger.info(f"Fetching weight based on a start_date and end_date")
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
        
def delete_all():
    logger.info(f"Delete everything")
    with get_db_cursor() as cursor:
        cursor.execute("TRUNCATE TABLE WeightLogs")

if __name__ == "__main__":
    delete_all()
    insert_weight(72.5, datetime.date(2025, 9, 2))
    insert_weight(72.5, datetime.date(2025, 9, 3))
    insert_weight(72.5, datetime.date(2025, 9, 4))
    insert_weight(72.5, datetime.date(2025, 9, 5))
    insert_weight(72.5, datetime.date(2025, 9, 6))

    weights = fetch_weight_date_range(datetime.date(2025, 9, 2), datetime.date(2025, 9, 4))
    for weight in weights:
        print(weight)
    
