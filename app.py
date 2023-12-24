import streamlit as st #import streamlit with alies st
import os #import os for environment variable 
import google.generativeai as genai #import generativeai model gemini pro vision from google
from PIL import Image
from dotenv import load_dotenv #import dotenv for environment variable
# Fetch the GOOGLE_API_KEY from the environment variable
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the genai library with the fetched API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')

# Streamlit app
st.title("Ai Vision")

# User input
user_input = st.text_input("Enter a prompt...")

# Image upload
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Generate button
if st.button("Generate"):
    if user_input:
        if uploaded_image:
            # Read the uploaded image
            img = Image.open(uploaded_image)

            # Prompt the model with the user's input
            response = model.generate_content(img)

            # Display the generated description
            st.write("Ai Response:")
            st.write(response.text)
        else:
            st.write("Please upload an image.")
    else:
        st.write("Please enter a  Prompt before generating.")

st.write("Powered by 2023@AlphaNetworks ")
