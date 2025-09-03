import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"

def program_analytics():
    """
    Fetches all exercise data from the API, counts the occurrences of each
    category, and displays the results in a pie chart.
    """
    # Fetch all exercise data from the backend API
    response = requests.get(f"{API_URL}/exercises/")
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Check if there is data to display
        if not data:
            st.info("No exercise data found to analyze. Please add some exercises first.")
            return

        # Convert the JSON data into a pandas DataFrame
        df = pd.DataFrame(data)
        
        # Group by the 'category' column and count the occurrences of each
        # The .value_counts() method is a convenient way to do this
        category_counts = df['category'].value_counts().reset_index()
        category_counts.columns = ['Category', 'Count']
        
        st.write("### Category Occurrences")
        st.dataframe(category_counts, hide_index=True)

        # Create the pie chart using plotly.express
        fig = px.pie(
            category_counts, 
            values='Count', 
            names='Category', 
            title='Distribution of Exercises by Category',
            labels={'Count': 'Number of Exercises', 'Category': 'Exercise Category'}
        )
        
        # Display the chart in the Streamlit app
        st.plotly_chart(fig)
        
    else:
        st.error(f"Failed to fetch data from the API. Status code: {response.status_code}")
