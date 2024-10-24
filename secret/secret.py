import os
import streamlit as st


def load_secrets(groq_api_key: str)-> None:
    if "GROQ_API_KEY" in st.secrets["GROQ_API_KEY"]:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    else:
        os.environ["GROQ_API_KEY"] = groq_api_key