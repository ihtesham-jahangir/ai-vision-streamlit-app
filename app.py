import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Fetch the GOOGLE_API_KEY from the environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the genai library with the fetched API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')

# Streamlit app
st.title("Ai Vision")

# User input
user_input = st.text_input("Enter a prompt...")

# Image upload
uploaded_image = st.file_uploader("Upload an image[jpg,jpeg,png]", type=["jpg", "jpeg", "png"])

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
