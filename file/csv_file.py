import os
import shutil
import streamlit as st
import pandas as pd
from langchain_community.document_loaders import DataFrameLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_csv(loaded_data_frames):
    try:
        documents=[]
        for loaded_data_frame in loaded_data_frames:
            
            df=pd.read_csv(loaded_data_frame)
            
            loader=DataFrameLoader(data_frame=df)

            file_data = loader.load()
            
            for data in file_data:
                documents.append(Document(page_content=data.page_content))

        return documents
    except Exception as e:
        st.error("🚨 Error while loading files: " + str(e.args))
        
        
def split_csv(documents):
    try:
        splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function=len)
        splitted_document=splitter.split_documents(documents=documents)
        return splitted_document
    except Exception as e:
        st.error("🚨 Error while splitting files: " + str(e.args))

