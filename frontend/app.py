import streamlit as st
from weight_tab import weight_tab

st.title("Gym Progress Tracker")

tab1, = st.tabs(["Weight"])

with tab1:
    weight_tab()