import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"


def weight_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2025, 9, 2))

    with col2:
        end_date = st.date_input("End Date", datetime(2025, 9, 3))
    
    if st.button("Get Weight Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.get(f"{API_URL}/weights/", params=payload)
        response = response.json()
    
        print(response)
        
        df = pd.DataFrame(response)
        df = df.sort_values("logged_at")
        st.write("Logged weights")
        st.dataframe(df)

        # # Plot line chart
        st.line_chart(df.set_index("logged_at")["weight_kg"])
