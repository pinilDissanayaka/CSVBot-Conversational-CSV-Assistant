import os
import streamlit as st
from langchain_community.document_loaders import CSVLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


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
        
        
def split_csv(documents):
    try:
        splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function=len)
        splitted_csv=splitter.split_documents(documents=documents)
        return splitted_csv
    except Exception as e:
        st.error("🚨 Error while splitting files: " + str(e.args))
        
        
        