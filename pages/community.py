# pages/community.py

import streamlit as st

def page():
    st.header("Join Our Community")
    st.write("Connect with others, share experiences, and get support from peers and healthcare professionals.")
    st.text_input("Share your story or ask a question...", key="community_input")
