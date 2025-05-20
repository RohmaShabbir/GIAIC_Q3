import streamlit as st
import json
import os
from datetime import datetime
import uuid
import pandas as pd
from PIL import Image

# Logo and branding
logo = Image.open("skillbridge_logo.png")  # You'll need to create this

def settings_page():
    user = st.session_state["user"]
    st.title("Settings")
    
    st.subheader("Account Information")
    st.write(f"**Username:** {user['username']}")
    st.write(f"**Name:** {user['name']}")
    st.write(f"**Email:** {user['email']}")
    st.write(f"**Account Type:** {'Pro' if user['is_pro'] else 'Free'}")
    
    st.subheader("Update Profile")
    with st.form("update_profile"):
        new_name = st.text_input("Name", value=user["name"])
        new_email = st.text_input("Email", value=user["email"])
        
        if st.form_submit_button("Update Profile"):
            # Update user in database
            data = db.load_data()
            for u in data["users"]:
                if u["user_id"] == user["user_id"]:
                    u["name"] = new_name
                    u["email"] = new_email
                    break
            db.save_data(data)
            
            # Update session
            st.session_state["user"]["name"] = new_name
            st.session_state["user"]["email"] = new_email
            st.success("Profile updated successfully!")
            st.rerun()
    
    st.subheader("Change Password")
    with st.form("change_password"):
        current_password = st.text_input("Current Password", type="password")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm New Password", type="password")
        
        if st.form_submit_button("Change Password"):
            if current_password != user["password"]:
                st.error("Current password is incorrect")
            elif new_password != confirm_password:
                st.error("New passwords don't match")
            else:
                # Update password in database
                data = db.load_data()
                for u in data["users"]:
                    if u["user_id"] == user["user_id"]:
                        u["password"] = new_password
                        break
                db.save_data(data)
                
                # Update session
                st.session_state["user"]["password"] = new_password
                st.success("Password changed successfully!")
                st.rerun()
    
    st.subheader("Danger Zone")
    if st.button("Delete Account"):
        st.error("This will permanently delete your account and all data")
        confirm = st.text_input("Type 'DELETE' to confirm")
        if st.button("Permanently Delete") and confirm == "DELETE":
            # Delete user and all associated data
            data = db.load_data()
            data["users"] = [u for u in data["users"] if u["user_id"] != user["user_id"]]
            data["clients"] = [c for c in data["clients"] if c["user_id"] != user["user_id"]]
            data["projects"] = [p for p in data["projects"] if p["user_id"] != user["user_id"]]
            db.save_data(data)
            
            st.success("Account deleted successfully")
            logout()