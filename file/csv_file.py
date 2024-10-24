import os
import streamlit as st
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


def save_csv(files:list, temp_dir:str):
    try:
        saved_files=[]
        for file in files:
            file_name = file.name
            
            save_dir = os.path.join(temp_dir, file_name)
            
            with open(save_dir, 'wb') as f:
                file.write(file.read())
                saved_files.append(save_dir)
                
        return saved_files
    except Exception as e:
        st.error("🚨 Error while saving files: " + str(e.args))
        
        

def load_csv(file_paths):
    try:
        documents=[]
        for file_path in file_paths:
            loader = CSVLoader(file_path=file_path)
            file_data = loader.load()
            
            for data in file_data:
                documents.append(Document(page_content=data.page_content))

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

def create_dir(dir="temp"):
    if not os.path.exists(dir):
        os.makedirs(dir)
        
    return dir

def remove_files(temp_dir):
    try:
        list_dir=os.listdir(temp_dir)
        for file in list_dir:
            os.remove(os.path.join(temp_dir, file))
    except Exception as e:
        st.error("🚨 Error while removing files: " + str(e.args))
        
        
        