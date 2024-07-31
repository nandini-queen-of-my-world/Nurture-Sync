# utils.py

from config import Config
import os
import pandas as pd
import numpy as np

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def save_uploaded_file(file):
    filename = os.path.join(Config.UPLOAD_FOLDER, file.filename)
    file.save(filename)
    return filename

def load_data(file_path):
    # Load and preprocess data
    df = pd.read_csv(file_path)
    return df

def analyze_report(file_path):
    # Dummy function for report analysis
    # Integrate actual AI/ML logic here
    return "Report Analysis Complete"

def generate_recommendations(user_data):
    # Dummy function for generating recommendations
    # Replace with actual AI logic
    return "Personalized Recommendations Generated"
