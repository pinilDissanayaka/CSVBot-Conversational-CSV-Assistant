import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq.chat_models import ChatGroq
import yaml

def get_congig():
    try:
        config_file_path = "config.yml"
        
        with open(config_file_path, 'r') as stream:
            config = yaml.safe_load(stream)
        
        return config   
    except Exception as e:
        st.error("🚨 Error while loading config: " + str(e.args))

def get_embeddings():
    try:
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}
        
        return HuggingFaceEmbeddings(
            model_name=get_congig()["embeddings"]["name"], 
            model_kwargs=model_kwargs, 
            encode_kwargs=encode_kwargs
            )
    except Exception as e:
        st.error("🚨 Error while loading embeddings: " + str(e.args))

def get_llm():
    try:
        llm = ChatGroq(model=get_congig()["llm"]["name"], temperature=get_congig()["llm"]["temperature"])
        return llm
    except Exception as e:
        st.error("🚨 Error while loading llm: " + str(e.args))