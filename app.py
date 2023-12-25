from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables
import streamlit as st
import google.generativeai as genai
import os


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini-pro model and get responses

# initialize model
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

## initialize or setup your streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

## when submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)
