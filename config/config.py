import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_groq.chat_models import ChatGroq
import yaml

def get_config():
    try:
        config_file_path = "config/config.yml"
        
        with open(config_file_path, 'r') as stream:
            config = yaml.safe_load(stream)
        
        return config   
    except Exception as e:
        st.error("🚨 Error while loading config: " + str(e.args))

def get_embeddings():
    try:
        embedding_model_name=get_config()["embeddings"]["name"]
        
        embedding_model=GoogleGenerativeAIEmbeddings(model=embedding_model_name)
        
        return embedding_model
    except Exception as e:
        st.error("🚨 Error while loading embeddings: " + str(e.args))

def get_llm():
    try:
        llm = ChatGroq(model=get_config()["llm"]["name"], temperature=get_config()["llm"]["temperature"])
        return llm
    except Exception as e:
        st.error("🚨 Error while loading llm: " + str(e.args))