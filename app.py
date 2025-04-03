# app.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Function to convert image to sketch
def image_to_sketch(image):
    # Convert uploaded image to grayscale
    image_gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

    return edges

# Inject CSS styles
st.markdown("""
    <style>
    /* General page styling */
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        max-width: 1200px;
        margin: auto;
    }

    /* Title styling */
    h1 {
        color: #2c3e50;
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-bottom: 10px;
    }

    /* Subtitle/description styling */
    .stMarkdown p {
        color: #7f8c8d;
        text-align: center;
        font-size: 16px;
        font-family: 'Arial', sans-serif;
    }

    /* File uploader styling */
    .stFileUploader {
        border: 2px dashed #3498db;
        border-radius: 8px;
        padding: 10px;
        background-color: #ffffff;
        margin: 20px 0;
    }

    /* Column container styling */
    .stColumn {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 10px;
    }

    /* Image caption styling */
    .stImage > div > div > div > p {
        color: #34495e;
        font-size: 14px;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }

    /* Error message styling */
    .stError {
        background-color: #ffe6e6;
        color: #c0392b;
        border-radius: 5px;
        padding: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app layout
st.title("Image to Sketch Converter")
st.write("Upload an image to convert it into a sketch!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Open the uploaded image
        original_image = Image.open(uploaded_file).convert("RGB")

        # Convert to sketch
        sketch = image_to_sketch(original_image)

        # Display original and sketch side by side
        col1, col2 = st.columns(2)

        with col1:
            st.image(original_image, caption="Original Image", use_container_width=True)

        with col2:
            st.image(sketch, caption="Generated Sketch", use_container_width=True, clamp=True, channels="GRAY")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")