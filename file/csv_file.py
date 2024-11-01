import os
from tempfile import NamedTemporaryFile
import streamlit as st
from langchain_community.document_loaders import CSVLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_csv(upload_files):
    try:
        documents=[]
        for upload_file in upload_files:
            
            with NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(upload_file.getvalue())
                tmp_file_path=tmp_file.name
                    
            loader=CSVLoader(file_path=tmp_file_path, encoding="utf-8", csv_args={
                'delimiter': ','})
            
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

