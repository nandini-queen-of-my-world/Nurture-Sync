import streamlit as st
from pages import home, upload_report, recommendations, track_health, community, profile
from chatbot.app import setup_chatbot  # Import the function from chatbot

def main():
    st.set_page_config(page_title="NurtureSync", page_icon=":heart:", layout="wide")

    st.title("NurtureSync: Your Health Companion")

    menu = ["Home", "Upload Report", "Recommendations", "Track Health", "Community", "Profile", "Chatbot"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        home.page()
    elif choice == "Upload Report":
        upload_report.page()
    elif choice == "Recommendations":
        recommendations.page()
    elif choice == "Track Health":
        track_health.page()
    elif choice == "Community":
        community.page()
    elif choice == "Profile":
        profile.page()
    elif choice == "Chatbot":
        setup_chatbot()  # Call the chatbot setup function

if __name__ == "__main__":
    main()