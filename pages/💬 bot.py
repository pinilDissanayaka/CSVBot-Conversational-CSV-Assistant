import os
import streamlit as st
from secret import load_secrets
from tempfile import TemporaryDirectory



st.set_page_config(page_title="CSVBot")

#app side bar
with st.sidebar:    
    st.write("## Upload Credentials")
    try:
        if "GROQ_API_KEY" in st.secrets:
            st.success("✅ Credentials saved!")
            load_secrets()
            st.session_state['credentials_saved'] = True
        else:
            st.subheader("Upload the credentials.")
            
            groq_api_key = st.text_input("Groq API Key", "", type="password")
            
            
            if st.button("Save Credentials", on_click=load_secrets(groq_api_key=groq_api_key)):
                st.success("✅ Credentials saved!")
                st.session_state['credentials_saved'] = True
            else:
                st.warning("⚠️ Please enter valid credentials!")
                st.session_state['credentials_saved'] = False
                
    except Exception as e:
        st.error("🚨 Error while loading secrets: " + str(e.args))

st.title("🦜 CSVBot : Your Conversational CSV Assistant")

if "credentials_saved" in st.session_state:
    if st.session_state['credentials_saved']:
        try:
            upload_files = st.file_uploader("Upload File", type=["CSV", "XLS", "XLSX", "XLSM", "XLSB"], accept_multiple_files=True, help=""" Click the button or drag and drop your CSV file here to get started. Once uploaded, you can ask questions like "What’s the average sales figure?" or "Show me all rows where region is 'North'." """)
            
            if upload_files:
                for upload_file in upload_files:
                    st.write("File name: ", upload_file.name)

        except Exception as e:
            st.error("🚨 Error while uploading files: " + str(e.args))
            




