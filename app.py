from dotenv import load_dotenv
import streamlit as st
import os
import pathlib
import textwrap
import google.generativeai as genai
from PIL import Image
import io

load_dotenv()  

# Configure Google Generative AI with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to convert text into markdown format
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function to get a response from the Gemini AI model
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Placeholder function for crop detection from an image
# Replace this with actual image recognition/crop detection logic
def detect_crop_from_image(image):
    # Example placeholder response for disease detection
    detected_disease = "Powdery Mildew"  # Example disease detection
    prevention_tips = "Ensure good air circulation, avoid overhead watering, and apply fungicides as needed."
    return detected_disease, prevention_tips

# Streamlit page configuration
st.set_page_config(page_title="Plant Disease Doctor")
st.header("Plant Disease Doctor ~ FramMart")

# Introduction prompt
st.markdown("""
### Welcome to the Plant Disease Doctor!
I am an AI specialized in diagnosing plant diseases and providing prevention tips. 
You can ask me questions about plant health, or upload an image of your plant for analysis.
""")

# Input for text-based Q&A
input_text = st.text_input("Describe your plant's symptoms or ask a question:", key="input")

# Upload an image for crop/disease detection
uploaded_image = st.file_uploader("Upload an image of your plant for disease detection", type=["jpg", "jpeg", "png"])

# Submit buttons for both functionalities
submit_question = st.button("Ask the Question")
submit_image = st.button("Analyze Image")

# Handling the text-based Q&A
if submit_question and input_text:
    question = f"As a plant disease doctor, {input_text}"
    response = get_gemini_response(question)
    st.subheader("Diagnosis and Prevention Tips:")
    st.write(response)

# Handling the image-based crop/disease detection
if submit_image and uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Call the crop/disease detection function
    detected_disease, prevention_tips = detect_crop_from_image(image)
    
    st.subheader("Detected Disease:")
    st.write(detected_disease)
    
    st.subheader("Prevention Tips:")
    st.write(prevention_tips)
