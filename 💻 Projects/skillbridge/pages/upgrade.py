import streamlit as st
import json
import os
from datetime import datetime
import uuid
import pandas as pd
from PIL import Image

# Logo and branding
logo = Image.open("skillbridge_logo.png")  # You'll need to create this

def upgrade_page():
    user = st.session_state["user"]
    st.title("Upgrade to SkillBridge Pro")
    
    st.image(logo, width=150)
    
    if user["is_pro"]:
        st.success("You're already a Pro member! Thank you for your support.")
        if st.button("Back to Dashboard"):
            st.session_state["page"] = "dashboard"
            st.rerun()
        return
    
    st.markdown("""
    ## Unlock Premium Features
    
    Upgrade to **SkillBridge Pro** for just **Rs. 500/month** and get:
    
    - ✔️ **Advanced Analytics** - Detailed earnings reports and client insights
    - ✔️ **Unlimited Projects** - No restrictions on the number of projects
    - ✔️ **Priority Support** - Get your questions answered quickly
    - ✔️ **Invoice Templates** - Professional invoice templates
    - ✔️ **Export Data** - Export your projects and invoices to Excel
    - ✔️ **Reminder System** - Automatic client follow-up reminders
    """)
    
    st.warning("Free version is limited to 5 projects and basic features")
    
    # Simulated payment
    with st.form("pro_payment"):
        st.write("### Payment Information")
        col1, col2 = st.columns(2)
        with col1:
            card_number = st.text_input("Card Number", "4242 4242 4242 4242")
            expiry = st.text_input("Expiry Date", "12/25")
        with col2:
            cvc = st.text_input("CVC", "123")
            name = st.text_input("Cardholder Name", user["name"])
        
        agree = st.checkbox("I agree to the terms and conditions")
        
        if st.form_submit_button("Subscribe to Pro (Rs. 500/month)"):
            if not agree:
                st.error("Please agree to the terms and conditions")
            else:
                # Update user to Pro in database
                data = db.load_data()
                for u in data["users"]:
                    if u["user_id"] == user["user_id"]:
                        u["is_pro"] = True
                        break
                db.save_data(data)
                
                # Update session
                st.session_state["user"]["is_pro"] = True
                st.success("🎉 Welcome to SkillBridge Pro! Your subscription is active.")
                st.balloons()
                st.session_state["page"] = "dashboard"
                st.rerun()
    
    if st.button("Back to Dashboard"):
        st.session_state["page"] = "dashboard"
        st.rerun()