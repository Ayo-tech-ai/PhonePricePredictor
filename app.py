# Import necessary libraries
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("PhonePrice_model.pkl", "rb") as file:
    model = pickle.load(file)

# Set the background image with an opacity effect
def set_background(image_url):
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-blend-mode: darken;
        background-color: rgba(255, 255, 255, 0.6); /* Adds a whitish overlay */
    }}
    h1 {{
        color: blue; /* Sets the title color to blue */
    }}
    label {{
        color: blue; /* Sets the input label color to blue */
        font-weight: bold; /* Makes the input label bold */
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set your background image
background_image_url = "https://github.com/Ayo-tech-ai/PhonePricePredictor/raw/main/backgrd.jpg"  # Update the URL to your new background image
set_background(background_image_url)

# Set up the app title
st.title("Phone Price Predictor")

# Input fields for the features
ppi = st.number_input("Enter Pixels Per Inch (PPI)", min_value=1, max_value=1000, step=1)
cpu_freq = st.number_input("Enter CPU Frequency (GHz)", min_value=0.1, max_value=10.0, step=0.1)
ram = st.number_input("Enter RAM Size (GB)", min_value=1, max_value=128, step=1)
battery = st.number_input("Enter Battery Capacity (mAh)", min_value=500, max_value=10000, step=100)

# Predict button
if st.button("Predict"):
    # Prepare input features for the model
    input_features = np.array([[ppi, cpu_freq, ram, battery]])
    predicted_price = model.predict(input_features)[0]
    
    # Display the result with styled output
    st.markdown(
        f"""
        <h3 style="text-align: center;">
        Predicted Phone Price: 
        <span style="color: green; font-weight: bold;">${predicted_price:.2f}</span>
        </h3>
        """, 
        unsafe_allow_html=True
)
