import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def program_builder_tab():
    st.header("Build your program💪")
    
    if "day_counter" not in st.session_state: st.session_state.day_counter = None
    if st.session_state.day_counter == None: st.session_state.day_counter = 1
    
    st.session_state.day_counter
    categories = ["Shoulders", "Back", "Arms", "Chest", "Legs", "Core"]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        add = st.button("Add day")
        if add: st.session_state.day_counter += 1
    with col2:
        delete = st.button("Delete day")
        if st.session_state.day_counter > 1:
            if delete: st.session_state.day_counter -= 1
    with col3:
        download = st.button("Download program")
        if download: print("download")
    
    dc = st.session_state.day_counter
    for i in range(0, dc):
        st.subheader("Day " + str(i + 1))
        with st.form(key=f"form{i}"):
            for j in range(5):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.text_input(label="Exercise", key=f"category0_{j}{i})")
                with col2:
                    st.selectbox(label="Category", options=categories, key=f"category1_{j}{i}")
                with col3:
                    st.number_input(label="Kg", key=f"category2_{j}{i}")
                with col4:
                    st.number_input(label="Reps", key=f"category3_{j}{i}")
            
            submit_button = st.form_submit_button()        
            if submit_button:
                print("real")
        