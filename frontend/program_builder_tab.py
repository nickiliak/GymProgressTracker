import streamlit as st
import requests

API_URL = "http://localhost:8000"

def program_builder_tab():
    st.header("Build your program💪")
    
    # Initialize session state variables
    if "day_counter" not in st.session_state:
        st.session_state.day_counter = 1
    if "submit_all_pressed" not in st.session_state:
        st.session_state.submit_all_pressed = False
        
    categories = ["Shoulders", "Back", "Arms", "Chest", "Legs", "Core"]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        add = st.button("Add day")
        if add:
            st.session_state.day_counter += 1
    with col2:
        delete = st.button("Delete day")
        if st.session_state.day_counter > 1 and delete:
            st.session_state.day_counter -= 1
    with col3:
        submit_all = st.button("Submit all")
        if submit_all:
            st.session_state.submit_all_pressed = True
    
    # --- Loop to create the forms for each day ---
    dc = st.session_state.day_counter
    
    for i in range(dc):
        day_number = i + 1
        st.subheader(f"Day {day_number}")
        with st.form(key=f"form_{i}"):
            
            # This loop creates the input widgets for each exercise
            for j in range(5):
                col1, col2, col3, col4, col5 = st.columns(5)
                
                with col1:
                    st.text_input(label="Exercise", key=f"exercise_{j}_{i}", label_visibility="collapsed")
                with col2:
                    st.selectbox(label="Category", options=categories, key=f"category_{j}_{i}", label_visibility="collapsed")
                with col3:
                    st.number_input(label="Kg", key=f"kg_{j}_{i}", min_value=0.0, label_visibility="collapsed")
                with col4:
                    st.number_input(label="Sets", key=f"sets_{j}_{i}", step=1, format="%d", min_value=1, label_visibility="collapsed")
                with col5:
                    st.number_input(label="Reps", key=f"reps_{j}_{i}", step=1, format="%d", min_value=1, label_visibility="collapsed")
            
            submit_button = st.form_submit_button(label=f"Submit Day {day_number}")
            
            # This block of code executes ONLY when a form is submitted or the "Submit all" button is pressed
            if submit_button or st.session_state.submit_all_pressed:
                # Correctly collect the data from session state
                exercises_to_submit = []
                for j in range(5):
                    exercise_name = st.session_state[f"exercise_{j}_{i}"]
                    if exercise_name: # Only add if the exercise name is not empty
                        exercises_to_submit.append({
                            "exercise_name": exercise_name,
                            "kg": st.session_state[f"kg_{j}_{i}"],
                            "reps": st.session_state[f"reps_{j}_{i}"],
                            "sets": st.session_state[f"sets_{j}_{i}"],
                            "category": st.session_state[f"category_{j}_{i}"]
                        })

                if exercises_to_submit:
                    submit_to_api(exercises_to_submit, day_number)
    
    # Reset submit_all_pressed after all forms are processed
    if st.session_state.submit_all_pressed:
        st.session_state.submit_all_pressed = False

# Function to handle API submission
def submit_to_api(exercises_list, day_number):
    try:
        payload = {
            "exercises": exercises_list,
            "day_number": day_number
        }
        response = requests.post(f"{API_URL}/add_day/", json=payload)
        response.raise_for_status()
        st.success(f"Exercises for Day {day_number} submitted successfully! 🎉")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to submit data for Day {day_number}: {e}")
