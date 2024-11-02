import os
import streamlit as st
from secret import load_secrets
from file import load_csv, split_csv
from vector_store import create_pinecone_index, load_vector_store, get_retriever, clear_index
from chatbot import chat_with_csv, stream_text
import pandas as pd
from io import StringIO


st.set_page_config(page_title="CSVBot")

#app side bar
with st.sidebar:    
    st.write("## Upload Credentials")
    try:
        if "GROQ_API_KEY" and "PINECONE_API_KEY" and "GOOGLE_PROJECT_ID" and "GOOGLE_API_KEY" in st.secrets:
            load_secrets()
        else:
            st.subheader("Upload the credentials.")
            
            groq_api_key = st.text_input("Groq API Key", None, type="password")
            
            pinecone_api_key= st.text_input("Pinecone API Key", None, type="password")
            
            google_api_key = st.text_input("Google API Key", None, type="password")
            
            google_project_id = st.text_input("Google Project ID", None, type="password")
            
            if groq_api_key and pinecone_api_key and google_api_key and google_project_id:
                if st.button("Save Credentials"):
                    load_secrets(groq_api_key=groq_api_key, pinecone_api_key=pinecone_api_key, google_api_key=google_api_key, google_project_id=google_project_id)
            else:
                st.warning("⚠️ Please enter valid credentials!")

    except Exception as e:
        st.error("🚨 Error while loading secrets: " + str(e.args))
        
    st.write("Clear Chat History")
    if st.button("Clear Chat History"):
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you? 👋"}]
        
    st.write("Clear Vector Store")
    if st.button("Clear Vector Store"):
        clear_index()

st.title("🦜 CSVBot : Your Conversational CSV Assistant")

if "credentials_saved" in st.session_state:
    if st.session_state['credentials_saved']:
        try:
            upload_files = st.file_uploader("Upload File", type=["CSV"], accept_multiple_files=True, help=""" Click the button or drag and drop your CSV file here to get started. Once uploaded, you can ask questions like "What’s the average sales figure?" or "Show me all rows where region is 'North'." """)
            
            if upload_files:
                for upload_file in upload_files:
                    st.write(upload_file.name)
                    df=pd.read_csv(upload_file, low_memory=False)
                    st.dataframe(df)

        except Exception as e:
            st.error("🚨 Error while uploading files: " + str(e.args))
            
        if upload_files:
            if st.button("Submit"):
                with st.status("Uploading files...", expanded=False):

                    documents=load_csv(upload_files=upload_files)

                    splitted_documents=split_csv(documents=documents)
                    
                    st.write("Creating index...")
                    index_name=create_pinecone_index()
                    
                    st.write("Loading vector store...")
                    vector_store=load_vector_store(documents=splitted_documents)
                    
                if "retriever" not in st.session_state:
                    st.session_state['retriever'] = get_retriever()
                        

        retriever=get_retriever()
        # Store LLM generated responses
        if "messages" not in st.session_state.keys():
            st.session_state.messages = [{"role": "assistant", "content": "How may I help you? 👋"}]

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # User-provided prompt
        if prompt := st.chat_input():
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.write(prompt)

        # Generate a new response if last message is not from assistant
        if st.session_state.messages[-1]["role"] != "assistant":
            try:
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = chat_with_csv(question=prompt, retriever=retriever)
                        st.write_stream(stream_text(response))
                message = {"role": "assistant", "content": response}
                st.session_state.messages.append(message)
            except Exception as e:
                st.warning(f"An unexpected error occurred: {str(e.args)}. Please try again.", icon="⚠️")
            
            
else:
    st.warning("⚠️ Please enter valid credentials!")
    




