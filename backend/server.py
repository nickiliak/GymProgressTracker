from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Weight(BaseModel):
    weight_kg: float
    logged_at: date

@app.get("/weights/", response_model=List[Weight])
def get_weights(start_date: date, end_date: date):
    weights = db_helper.fetch_weights_for_date(start_date, end_date)
    if weights is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve weights from the database.")

    return weights
