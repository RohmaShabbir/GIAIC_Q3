import streamlit as st
import json
import os
from datetime import datetime
import uuid
import pandas as pd
from PIL import Image

# Logo and branding
logo = Image.open("skillbridge_logo.png") 

def main():
    initialize_session()
    
    if st.session_state["page"] == "login":
        login_page()
    elif "user" not in st.session_state:
        st.session_state["page"] = "login"
        st.rerun()
    elif st.session_state["page"] == "dashboard":
        dashboard()
    elif st.session_state["page"] == "clients":
        clients_page()
    elif st.session_state["page"] == "projects":
        projects_page()
    elif st.session_state["page"] == "invoices":
        invoices_page()
    elif st.session_state["page"] == "notes":
        notes_page()
    elif st.session_state["page"] == "upgrade":
        upgrade_page()
    elif st.session_state["page"] == "settings":
        settings_page()

if __name__ == "__main__":
    main()