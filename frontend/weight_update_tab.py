import streamlit as st
from datetime import datetime
import requests
from util import API_URL

def weight_update_tab():
    st.header("Insert weight")
    
    with st.form(key="data_form_insert"):
        col1_insert, col2_insert = st.columns(2)
        with col1_insert:  
            weight = st.number_input("Weight (kg)", min_value=0.0)
            submit_button_insert = st.form_submit_button(label="Add Data")
        with col2_insert:
            date_insert = st.date_input("Date", datetime.today())
            
        
    if submit_button_insert:
        with col2_insert:
            payload = {
            "weight_kg": weight,
            "logged_at": date_insert.strftime("%Y-%m-%d")
            }
            requests.post(f"{API_URL}/weights_insert/", json=payload)
            
            st.write("Added Weight")
    
    st.header("Delete weight")
    with st.form(key="data_form_delete"):
        col1_delete, = st.columns(1)
        with col1_delete:  
            date_delete = st.date_input("Date", datetime.today())
            submit_button_delete = st.form_submit_button(label="Delete Weights for Date")            
        

    if submit_button_delete:
        with col1_delete:
            
            strdate = date_delete.strftime("%Y-%m-%d")
            payload = {
                "date": strdate
            }

            requests.delete(f"{API_URL}/weights_delete/{strdate}", params=payload)
            
            st.write("Deleted weight")