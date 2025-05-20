import streamlit as st
import json
import os
from datetime import datetime
import uuid
import pandas as pd
from PIL import Image

# Logo and branding
logo = Image.open("skillbridge_logo.png")  # You'll need to create this

def login_page():
    st.title("SkillBridge - Freelancer's Companion")
    st.image(logo, width=200)
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")
            
            if login_button:
                user = db.get_user(username)
                if user and user["password"] == password:
                    st.session_state["user"] = user
                    st.session_state["page"] = "dashboard"
                    st.rerun()
                else:
                    st.error("Invalid username or password")
    
    with tab2:
        with st.form("signup_form"):
            new_username = st.text_input("Choose a username")
            new_password = st.text_input("Choose a password", type="password")
            confirm_password = st.text_input("Confirm password", type="password")
            name = st.text_input("Full name")
            email = st.text_input("Email")
            signup_button = st.form_submit_button("Create Account")
            
            if signup_button:
                if new_password != confirm_password:
                    st.error("Passwords don't match!")
                elif db.get_user(new_username):
                    st.error("Username already exists!")
                else:
                    new_user = User(
                        username=new_username,
                        password=new_password,
                        name=name,
                        email=email
                    )
                    db.add_user(new_user)
                    st.success("Account created successfully! Please login.")