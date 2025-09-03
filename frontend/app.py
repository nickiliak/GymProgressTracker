import streamlit as st
from weight_tab import weight_tab
from weight_update_tab import weight_update_tab

st.title("Gym Progress Tracker")

tab1, tab2, tab3, tab4 = st.tabs(["Weight Analytics", "Weight Update", "Program Analytics", "Program Builder"])

with tab1:
    weight_tab()
    
with tab2:
    weight_update_tab()
