from pinecone import Pinecone, ServerlessSpec
import streamlit as st
from langchain_pinecone import PineconeVectorStore
from config import get_config, get_embeddings


def create_pinecone_index()->None:
    try:
        pinecone=Pinecone()
        
        index_name=str(get_config()["vector_store"]["index_name"])
        dimension=int(get_config()["vector_store"]["dimension"])
        metric=str(get_config()["vector_store"]["metric"])
        
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


def load_vector_store(index_name, documents):
    try:        
        embeddings=get_embeddings()
        
        vector_store=PineconeVectorStore(index_name=index_name, embedding=embeddings)
                
        vector_store.from_documents(documents=documents, embeddings=embeddings)
        
        retriever=vector_store.as_retriever()
        
        return retriever
    except Exception as e:
        st.error("🚨 Error while loading to the vector store: " + str(e.args))