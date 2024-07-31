# pages/profile.py

import streamlit as st

def page():
    st.header("Your Profile")
    st.write("Manage your profile details and health information.")
    user_profile = {
        "Name": "John Doe",
        "Age": 30,
        "Condition": "Thyroid",
        "Contact": "john.doe@example.com"
    }
    st.write(user_profile)
