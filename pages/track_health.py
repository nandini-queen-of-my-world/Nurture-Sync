# pages/track_health.py

import streamlit as st

def page():
    st.header("Track Your Health")
    st.write("Log your daily activities and food intake.")
    with st.form(key='tracking_form'):
        food_log = st.text_input("Food Intake")
        activity_log = st.text_input("Physical Activity")
        submit_button = st.form_submit_button("Log Activity")
        if submit_button:
            st.write(f"Logged: Food - {food_log}, Activity - {activity_log}")
