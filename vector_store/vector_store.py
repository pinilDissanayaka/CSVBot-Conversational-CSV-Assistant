from pinecone import Pinecone, ServerlessSpec
import streamlit as st
from langchain_pinecone import PineconeVectorStore
from config import get_config, get_embeddings


def create_pinecone_index()->None:
        pinecone=Pinecone()
        
        index_name=str(get_config["vector_store"]["index_name"])
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


def load_vector_store(documents):
    try:
        index_name=str(get_config["vector_store"]["index_name"])

        vector_store=PineconeVectorStore(index_name=index_name)
        
        embeddings=get_embeddings()
        
        vector_store.add_documents(documents=documents, embeddings=embeddings)
        
        retriever=vector_store.as_retriever()
        
        return retriever
    except Exception as e:
        st.error("🚨 Error while loading vector store: " + str(e.args))