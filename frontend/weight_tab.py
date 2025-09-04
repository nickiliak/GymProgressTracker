import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px
from dateutil.relativedelta import relativedelta

API_URL = "http://localhost:8000"


def weight_tab():

    if "data" not in st.session_state:
        st.session_state.data = None
    if "last_start_date" not in st.session_state:
        st.session_state.last_start_date = None
    if "last_end_date" not in st.session_state:
        st.session_state.last_end_date = None
    
    col1, col2 = st.columns(2)
    today = datetime.today()
    with col1:
        current_start_date  = st.date_input("Start Date", today - relativedelta(months=1))

    with col2:
        current_end_date = st.date_input("End Date", today)

    # Check if dates have changed since the last run
    dates_changed = (
        current_start_date != st.session_state.last_start_date
        or current_end_date != st.session_state.last_end_date
    )
    
    if dates_changed or st.session_state.data is None:
        
        st.session_state.last_start_date = current_start_date
        st.session_state.last_end_date = current_end_date
   
        payload = {
            "start_date": current_start_date.strftime("%Y-%m-%d"),
            "end_date": current_end_date.strftime("%Y-%m-%d")
        }

        response = requests.get(f"{API_URL}/weights_analytics/", params=payload)
        response = response.json()

        df = pd.DataFrame(response)
        if df == []:
            st.write(f"No weight found for the dates {today} - {today - relativedelta(months=1)}")
        else: 
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