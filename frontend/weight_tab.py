import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"


def weight_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2025, 9, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2025, 9, 30))
    
    if st.button("Get Weight Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.get(f"{API_URL}/weights/", params=payload)
        response = response.json()

        df = pd.DataFrame(response)
        df.rename(columns={"weight_kg": "weight", "logged_at": "date"}, inplace=True)
        df = df.dropna(subset=["weight"]) 
        df = df.sort_values("date")
        
        start_date = df["date"].min()
        final_date = df["date"].max()
        
        least_weight = df["weight"].min()
        max_weight = df["weight"].max()
        
        start_weight = df.loc[df["date"] == start_date, "weight"].iloc[0]
        final_weight = df.loc[df["date"] == final_date, "weight"].iloc[0]
        weight_diff = final_weight - start_weight
        
        fig = px.line(df, x="date", y="weight", title=f"Weight gain over time,  {weight_diff:.2f} kg", markers=True)
        
        fig.update_yaxes(range=[least_weight, max_weight], fixedrange=True)
        fig.update_xaxes(range=[start_date, final_date], fixedrange=True)
        
        fig.update_traces(hovertemplate='Date: %{x}<br>Weight: %{y} kg')
        st.plotly_chart(fig)
