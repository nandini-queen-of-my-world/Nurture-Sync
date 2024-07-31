# pages/recommendations.py

import streamlit as st
from utils import generate_recommendations

def page():
    st.header("Personalized Recommendations")
    user_data = {"age": 30, "weight": 70, "height": 170, "condition": "Thyroid"}  # Example user data
    recommendations = generate_recommendations(user_data)
    st.write(f"Recommendations: {recommendations}")
