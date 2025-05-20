import streamlit as st
import json
import os
from datetime import datetime
import uuid
import pandas as pd
from PIL import Image

# Logo and branding
logo = Image.open("skillbridge_logo.png")  # You'll need to create this

def invoices_page():
    user = st.session_state["user"]
    st.title("Invoice Management")
    
    invoices = db.get_invoices(user_id=user["user_id"])
    projects = {p["project_id"]: p for p in db.get_projects(user["user_id"])}
    clients = {c["client_id"]: c for c in db.get_clients(user["user_id"])}
    
    if invoices:
        # Summary stats
        total_invoices = len(invoices)
        paid_invoices = len([i for i in invoices if i["is_paid"]])
        unpaid_amount = sum(float(i["amount"]) for i in invoices if not i["is_paid"])
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Invoices", total_invoices)
        col2.metric("Paid Invoices", paid_invoices)
        col3.metric("Pending Amount", f"Rs. {unpaid_amount:,.2f}")
        
        # Filter options
        st.subheader("Your Invoices")
        filter_status = st.selectbox("Filter by payment status", ["All", "Paid", "Unpaid"])
        
        filtered_invoices = invoices
        if filter_status == "Paid":
            filtered_invoices = [i for i in invoices if i["is_paid"]]
        elif filter_status == "Unpaid":
            filtered_invoices = [i for i in invoices if not i["is_paid"]]
        
        # Display invoices
        invoice_data = []
        for inv in filtered_invoices:
            project = projects.get(inv["project_id"], {})
            client = clients.get(project.get("client_id", ""), {})
            invoice_data.append({
                "Project": project.get("title", "N/A"),
                "Client": client.get("name", "N/A"),
                "Amount": f"Rs. {float(inv['amount']):,.2f}",
                "Due Date": inv["due_date"],
                "Status": "Paid" if inv["is_paid"] else "Unpaid",
                "invoice_id": inv["invoice_id"]
            })
        
        df = pd.DataFrame(invoice_data)
        st.dataframe(df[["Project", "Client", "Amount", "Due Date", "Status"]], hide_index=True)
        
        # Invoice actions
        if filtered_invoices:
            selected_invoice_id = st.selectbox("Select invoice to manage", [i["invoice_id"] for i in filtered_invoices])
            selected_invoice = next(i for i in filtered_invoices if i["invoice_id"] == selected_invoice_id)
            project = projects.get(selected_invoice["project_id"], {})
            client = clients.get(project.get("client_id", ""), {})
            
            st.subheader("Invoice Details")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Project:** {project.get('title', 'N/A')}")
                st.write(f"**Client:** {client.get('name', 'N/A')}")
                st.write(f"**Amount:** Rs. {float(selected_invoice['amount']):,.2f}")
            with col2:
                st.write(f"**Created:** {selected_invoice['created_at']}")
                st.write(f"**Due Date:** {selected_invoice['due_date']}")
                st.write(f"**Status:** {'Paid' if selected_invoice['is_paid'] else 'Unpaid'}")
            
            st.write(f"**Description:** {selected_invoice['description']}")
            
            # Payment action
            if not selected_invoice["is_paid"]:
                if st.button("Mark as Paid"):
                    db.update_invoice_status(selected_invoice_id, True)
                    st.success("Invoice marked as paid!")
                    st.rerun()
                
                # Simulate payment gateway
                with st.expander("Make Payment (Simulation)"):
                    st.write("This is a simulation of a payment gateway")
                    col1, col2 = st.columns(2)
                    with col1:
                        card_number = st.text_input("Card Number", "4242 4242 4242 4242")
                        expiry = st.text_input("Expiry Date", "12/25")
                    with col2:
                        cvc = st.text_input("CVC", "123")
                        name = st.text_input("Cardholder Name", user["name"])
                    
                    if st.button("Pay Now"):
                        db.update_invoice_status(selected_invoice_id, True)
                        st.success("Payment successful! Invoice marked as paid.")
                        st.rerun()
            
            # Download invoice (simulated)
            st.download_button(
                label="Download Invoice (PDF)",
                data=f"Invoice #{selected_invoice_id}\n\nProject: {project.get('title', 'N/A')}\nClient: {client.get('name', 'N/A')}\nAmount: Rs. {float(selected_invoice['amount']):,.2f}\nDue Date: {selected_invoice['due_date']}\nDescription: {selected_invoice['description']}",
                file_name=f"invoice_{selected_invoice_id[:8]}.txt",
                mime="text/plain"
            )
    else:
        st.info("No invoices created yet. Create your first invoice from a project.")