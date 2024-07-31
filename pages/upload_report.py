# pages/upload_report.py

import streamlit as st
from utils import save_uploaded_file, analyze_report

def page():
    st.header("Upload Your Medical Report")
    file = st.file_uploader("Choose a PDF file", type="pdf")

    if file is not None:
        file_path = save_uploaded_file(file)
        st.success(f"File {file.name} uploaded successfully!")
        analysis_result = analyze_report(file_path)
        st.write(f"Report Analysis: {analysis_result}")
