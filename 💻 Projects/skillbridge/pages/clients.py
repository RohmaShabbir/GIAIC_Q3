import streamlit as st
import json
import os
from datetime import datetime
import uuid
import pandas as pd
from PIL import Image

# Logo and branding
logo = Image.open("skillbridge_logo.png")  # You'll need to create this

def clients_page():
    user = st.session_state["user"]
    st.title("Client Management")
    
    # Add new client
    with st.expander("Add New Client"):
        with st.form("new_client_form"):
            name = st.text_input("Client Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            submit = st.form_submit_button("Add Client")
            
            if submit:
                new_client = Client(
                    name=name,
                    email=email,
                    phone=phone,
                    user_id=user["user_id"]
                )
                db.add_client(new_client)
                st.success("Client added successfully!")
                st.rerun()
    
    # View clients
    clients = db.get_clients(user["user_id"])
    
    if clients:
        st.subheader("Your Clients")
        df = pd.DataFrame(clients)
        st.dataframe(df[["name", "email", "phone"]], hide_index=True)
        
        # Client details
        selected_client = st.selectbox("Select client to view details", [c["name"] for c in clients])
        client = next(c for c in clients if c["name"] == selected_client)
        
        st.subheader(f"Details for {client['name']}")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Email:** {client['email']}")
            st.write(f"**Phone:** {client['phone']}")
        
        with col2:
            client_projects = [p for p in db.get_projects(user["user_id"]) if p["client_id"] == client["client_id"]]
            st.write(f"**Total Projects:** {len(client_projects)}")
            paid_invoices = [i for i in db.get_invoices() if i["project_id"] in [p["project_id"] for p in client_projects] and i["is_paid"]]
            total_paid = sum(float(i["amount"]) for i in paid_invoices)
            st.write(f"**Total Paid:** Rs. {total_paid:,.2f}")
        
        # Projects with this client
        if client_projects:
            st.subheader("Projects with this client")
            st.dataframe(pd.DataFrame(client_projects)[["title", "deadline", "status", "budget"]], hide_index=True)
    else:
        st.info("No clients added yet. Add your first client to get started!")