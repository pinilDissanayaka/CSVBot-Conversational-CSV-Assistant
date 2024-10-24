from pinecone import Pinecone, ServerlessSpec
import streamlit as st
from langchain_pinecone import PineconeVectorStore


def create_index(index_name:str, dimension:int, metric="cosine"):
    try:
        pinecone=Pinecone()
        
        if index_name not in pinecone.list_indexes().names():
            pinecone.create_index(name=index_name, 
                                dimension=dimension, 
                                metric=metric, 
                                spec=ServerlessSpec(
                                    cloud='aws', 
                                    region='us-east-1'
                                    )
                                )
            st.write("✅ Index created successfully!")
            return index_name
        else:
            st.write("⚠️ Index already exists!")
            return index_name
        
    except Exception as e:
        st.error("🚨 Error while creating index: " + str(e.args))

def load_vector_store(index_name:str, documents, embeddings):
    try:
        vector_store=PineconeVectorStore(index_name=index_name)
        
        vector_store.add_documents(documents=documents, embeddings=embeddings)
        
        retriever=vector_store.as_retriever()
        
        return retriever
    except Exception as e:
        st.error("🚨 Error while loading vector store: " + str(e.args))