import os
import streamlit as st
from tempfile import TemporaryDirectory


st.set_page_config(page_title="GraphMind")

#app side bar
with st.sidebar:    
    st.write("## Upload Credentials")
    if "GROQ_API_KEY" in st.secrets:
        st.success("✅ Credentials saved!")
        st.session_state['credentials_saved'] = True
    else:
        st.subheader("Upload the credentials.")
        
        groq_api_key = st.text_input("Groq API Key", "", type="password")
        
        
        
        if st.button("Save Credentials"):
            st.success("✅ Credentials saved!")
            st.session_state['credentials_saved'] = True
        else:
            st.warning("⚠️ Please enter valid credentials!")
            st.session_state['credentials_saved'] = False
            
            

if "credentials_saved" in st.session_state:
    if st.session_state['credentials_saved']:
        upload_files = st.file_uploader("Upload File", type="pdf", accept_multiple_files=True)
        
        if upload_files:
            for upload_file in upload_files:
                st.write("File name: ", upload_file.name)
                
