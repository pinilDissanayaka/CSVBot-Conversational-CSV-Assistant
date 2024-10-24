import os
import streamlit as st
from langchain_community.document_loaders import CSVLoader, DirectoryLoader


def save_csv(files:list, temp_dir):
    try:
        for file in files:
            file_name = file.name
            
            save_dir = os.path.join(temp_dir, file_name)
            
            with open(save_dir, 'wb') as f:
                file.write(file.read())
    except Exception as e:
        st.error("🚨 Error while saving files: " + str(e.args))
        
        

def load_csv(temp_dir):
    try:
        loader = DirectoryLoader(path=temp_dir, glob="**/*.csv", loader_cls=CSVLoader, use_multithreading=True)
        documents = loader.load()
        return documents
    except Exception as e:
        st.error("🚨 Error while loading files: " + str(e.args))
        
        
        