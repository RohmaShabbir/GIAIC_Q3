import streamlit as st
import json
import os
from datetime import datetime
import uuid
import pandas as pd
from PIL import Image

# Logo and branding
logo = Image.open("skillbridge_logo.png")  # You'll need to create this

def projects_page():
    user = st.session_state["user"]
    st.title("Project Management")
    
    # Add new project
    with st.expander("Add New Project"):
        clients = db.get_clients(user["user_id"])
        if not clients:
            st.warning("Please add clients first before creating projects")
        else:
            with st.form("new_project_form"):
                title = st.text_input("Project Title")
                client = st.selectbox("Client", [c["name"] for c in clients])
                deadline = st.date_input("Deadline")
                budget = st.number_input("Budget (Rs.)", min_value=0.0, step=1000.0)
                status = st.selectbox("Status", ["Ongoing", "Completed", "On Hold"])
                submit = st.form_submit_button("Add Project")
                
                if submit:
                    client_id = next(c["client_id"] for c in clients if c["name"] == client)
                    new_project = Project(
                        title=title,
                        client_id=client_id,
                        deadline=deadline.strftime("%Y-%m-%d"),
                        budget=budget,
                        status=status,
                        user_id=user["user_id"]
                    )
                    db.add_project(new_project)
                    st.success("Project added successfully!")
                    st.rerun()
    
    # View projects
    projects = db.get_projects(user["user_id"])
    
    if projects:
        st.subheader("Your Projects")
        
        # Filter options
        col1, col2 = st.columns(2)
        with col1:
            status_filter = st.selectbox("Filter by status", ["All", "Ongoing", "Completed", "On Hold"])
        with col2:
            sort_by = st.selectbox("Sort by", ["Deadline (Ascending)", "Deadline (Descending)", "Budget (High-Low)", "Budget (Low-High)"])
        
        filtered_projects = projects
        if status_filter != "All":
            filtered_projects = [p for p in filtered_projects if p["status"] == status_filter]
        
        if sort_by == "Deadline (Ascending)":
            filtered_projects.sort(key=lambda x: x["deadline"])
        elif sort_by == "Deadline (Descending)":
            filtered_projects.sort(key=lambda x: x["deadline"], reverse=True)
        elif sort_by == "Budget (High-Low)":
            filtered_projects.sort(key=lambda x: float(x["budget"]), reverse=True)
        elif sort_by == "Budget (Low-High)":
            filtered_projects.sort(key=lambda x: float(x["budget"]))
        
        df = pd.DataFrame(filtered_projects)
        
        # Get client names for display
        clients = {c["client_id"]: c["name"] for c in db.get_clients(user["user_id"])}
        df["client"] = df["client_id"].map(clients)
        
        st.dataframe(df[["title", "client", "deadline", "budget", "status"]], hide_index=True)
        
        # Project details
        if filtered_projects:
            selected_project = st.selectbox("Select project to view details", [p["title"] for p in filtered_projects])
            project = next(p for p in filtered_projects if p["title"] == selected_project)
            
            st.subheader(f"Project: {project['title']}")
            st.write(f"**Client:** {clients[project['client_id']]}")
            st.write(f"**Deadline:** {project['deadline']}")
            st.write(f"**Budget:** Rs. {float(project['budget']):,.2f}")
            st.write(f"**Status:** {project['status']}")
            
            # Project actions
            tab1, tab2 = st.tabs(["Invoices", "Update Status"])
            
            with tab1:
                invoices = db.get_invoices(project_id=project["project_id"])
                
                if invoices:
                    st.write("Project Invoices")
                    invoice_df = pd.DataFrame(invoices)
                    invoice_df["is_paid"] = invoice_df["is_paid"].map({True: "Paid", False: "Unpaid"})
                    st.dataframe(invoice_df[["amount", "due_date", "description", "is_paid"]], hide_index=True)
                else:
                    st.info("No invoices for this project yet")
                
                with st.expander("Create New Invoice"):
                    with st.form("new_invoice_form"):
                        amount = st.number_input("Amount (Rs.)", min_value=0.0, step=1000.0)
                        due_date = st.date_input("Due Date")
                        description = st.text_area("Description")
                        submit = st.form_submit_button("Create Invoice")
                        
                        if submit:
                            new_invoice = Invoice(
                                project_id=project["project_id"],
                                amount=amount,
                                due_date=due_date.strftime("%Y-%m-%d"),
                                description=description
                            )
                            db.add_invoice(new_invoice)
                            st.success("Invoice created successfully!")
                            st.rerun()
            
            with tab2:
                with st.form("update_status_form"):
                    new_status = st.selectbox("Update Status", ["Ongoing", "Completed", "On Hold"])
                    update = st.form_submit_button("Update Status")
                    
                    if update:
                        # Update project status in database
                        data = db.load_data()
                        for p in data["projects"]:
                            if p["project_id"] == project["project_id"]:
                                p["status"] = new_status
                                break
                        db.save_data(data)
                        st.success("Project status updated!")
                        st.rerun()
    else:
        st.info("No projects added yet. Add your first project to get started!")