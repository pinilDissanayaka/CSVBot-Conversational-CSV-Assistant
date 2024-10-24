import os
import streamlit as st


def load_secrets(groq_api_key=None, pinecone_api_key=None)-> None:
    try:
        if "GROQ_API_KEY" and "PINECONE_API_KEY" in st.secrets:
            os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
            os.environ["PINECONE_API_KEY"]=st.secrets["PINECONE_API_KEY"]
        elif groq_api_key and pinecone_api_key:
            os.environ["GROQ_API_KEY"] = groq_api_key
            os.environ["PINECONE_API_KEY"]=pinecone_api_key
    except Exception as e:
        st.error("🚨 Error while loading secrets: " + str(e.args))
    