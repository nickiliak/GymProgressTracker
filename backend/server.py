from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Exercise(BaseModel):
    exercise_name: str
    kg: float
    reps: int
    sets: int
    category: str

class DayProgram(BaseModel):
    exercises: list[Exercise]
    day_number: int
    
class Weight(BaseModel):
    weight_kg: float
    logged_at: date

@app.get("/weights_analytics/", response_model=List[Weight])
def get_weights(start_date: date, end_date: date):
    weights = db_helper.fetch_weights_for_date(start_date, end_date)
    if weights is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve weights from the database.")

    return weights

@app.post("/weights_insert/")
def insert_weight(weight: Weight):
    db_helper.insert_weight(weight.weight_kg, weight.logged_at)
    
@app.delete("/weights_delete/{date}")
def delete_weight(date: date):
    db_helper.delete_at_date(date)
    
@app.post("/add_day/")
def add_day(day_program: DayProgram):
    db_helper.insert_new_day(day_program.exercises, day_program.day_number)
    return {"message": "Day program inserted successfully"}

@app.get("/exercises/")
def get_exercises():
    exercises = db_helper.fetch_all_exercises()
    
    if exercises is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve exercises from the database.")
    
    return exercises