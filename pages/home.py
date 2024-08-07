import streamlit as st
import pandas as pd
import numpy as np

def page():
    # Remove this line from home.py
    # st.set_page_config(layout='wide', initial_sidebar_state='expanded')

    # Sidebar for navigation
    st.sidebar.header('NurtureSync Navigation')
    menu = st.sidebar.radio("Go to", ['Home', 'Profile', 'Track', 'Reports'])

    # Custom CSS for enhanced appearance
    custom_css = """
        <style>
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 8px;
            }
            .stButton>button:hover {
                background-color: #45a049;
            }
            .stTextInput>div>div>input {
                border: 1px solid #4CAF50;
                border-radius: 8px;
                padding: 10px;
                width: 100%;
            }
            .stTextInput>div>div>input:focus {
                border: 2px solid #45a049;
            }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Home Section
    if menu == 'Home':
        st.title('Home')
        st.write('Overview of your health metrics.')

        # Example data for weight tracking
        weight_data = pd.DataFrame({
            'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
            'Weight': np.random.normal(70, 1, 30)
        })

        # Example data for thyroid levels
        thyroid_data = pd.DataFrame({
            'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
            'Thyroid Level': np.random.normal(1.5, 0.1, 30)
        })

        # Example data for food calorie intake
        calorie_data = pd.DataFrame({
            'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
            'Calories': np.random.normal(2000, 100, 30)
        })

        # Display plots for the metrics
        st.markdown('### Weight Tracking')
        st.line_chart(weight_data.set_index('Date'))

        st.markdown('### Thyroid Levels')
        st.line_chart(thyroid_data.set_index('Date'))

        st.markdown('### Food Calorie Intake')
        st.line_chart(calorie_data.set_index('Date'))

    # Profile Section
    elif menu == 'Profile':
        st.title('Profile')
        st.write('Manage your personal information and preferences.')

        # Input fields for profile details
        st.text_input('Name')
        st.text_input('Age')
        st.text_input('Location')
        st.text_input('Health Conditions')
        st.text_input('Current Doctor')

        st.markdown('### Past Month Tracking')
        st.markdown('#### Food')
        st.markdown('#### Exercise')
        st.markdown('#### Medicine')
        st.markdown('#### Previous Reports')

    # Track Section
    elif menu == 'Track':
        st.title('Track')
        st.write('Track your food intake, exercise, medication, and lab results.')

        # Subsections for tracking
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header('Food')
            st.button('Add', key='food_add')
            st.text_input('Description', key='food_description')
        with col2:
            st.header('Exercise')
            st.button('Add', key='exercise_add')
            st.text_input('Description', key='exercise_description')
        with col3:
            st.header('Medicine')
            st.button('Add', key='medicine_add')
            st.text_input('Description', key='medicine_description')
        with col4:
            st.header('Lab')
            st.button('Add', key='lab_add')
            st.text_input('Description', key='lab_description')

        # Choices table (as a placeholder, you can replace it with real data and logic)
        st.markdown('### Choices Table')
        st.write(pd.DataFrame({
            'Food': ['Breakfast', 'Lunch', 'Dinner'],
            'Exercise': ['Running', 'Yoga', 'Cycling'],
            'Medicine': ['Pill 1', 'Pill 2', 'Pill 3'],
            'Lab': ['Blood Test', 'Thyroid Test', 'Sugar Test']
        }))

    # Reports Section
    elif menu == 'Reports':
        st.title('Reports')
        st.write('Analyze and upload your medical reports.')

        col1, col2 = st.columns(2)
        with col1:
            st.header('Upload New')
            uploaded_file = st.file_uploader("Choose a file")
            if uploaded_file is not None:
                st.write('File uploaded successfully.')

        with col2:
            st.header('View Previous')
            # Placeholder for previous reports
            st.write('No previous reports uploaded.')

        st.markdown('### Analysis')
        # Placeholder for analysis charts
        st.write("Analysis charts will be displayed here when reports are uploaded.")
