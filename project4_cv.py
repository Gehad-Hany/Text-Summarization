import streamlit as st
from transformers import pipeline

# Load text summarization model from Hugging Face
summarization_pipeline = pipeline("summarization")

# Streamlit app interface
st.title("AI-Powered Text Summarization 📜")
st.write("Enter any long text, and we will summarize it for you!")

# User text input
user_input = st.text_area("Enter text here:")

if st.button("Summarize Text"):
    if user_input:
        result = summarization_pipeline(user_input, max_length=100, min_length=30, do_sample=False)
        summary = result[0]['summary_text']
        
        # Display the summary
        st.write("**Summary:**")
        st.write(summary)
    else:
        st.warning("Please enter text to summarize!")
