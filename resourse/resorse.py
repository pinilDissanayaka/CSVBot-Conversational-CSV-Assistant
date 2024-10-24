import os
import streamlit as st
from langchain_community.document_loaders import CSVLoader


def save_csv(files:list):
    try:
        for file in files:
            file_name = file.name
            
            with open(file_name, 'wb') as f:
                file.write(file.read())
    except Exception as e:
        st.error("🚨 Error while saving files: " + str(e.args))
            
            
            