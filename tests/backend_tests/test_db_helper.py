from backend import db_helper
from datetime import date
import pandas as pd

def test_fetch_weights_for_date():
    start_date = date(2025, 9, 1)
    end_date = date(2025, 9, 10)
    
    weights = db_helper.fetch_weights_for_date(start_date, end_date)
    df = pd.DataFrame(weights)
    
    if(len(weights)> 0):
        assert df["logged_at"].min() >= start_date
        assert df["logged_at"].max() <= end_date