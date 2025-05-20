import streamlit as st
import json
import os
from datetime import datetime
import uuid
import pandas as pd
from PIL import Image

# Logo and branding
logo = Image.open("skillbridge_logo.png")  # You'll need to create this

def dashboard():
    user = st.session_state["user"]
    
    st.title(f"Welcome, {user['name']}!")
    st.image(logo, width=150)
    
    if not user["is_pro"]:
        st.warning("You're using the free version of SkillBridge. Upgrade to Pro for advanced features!")
        if st.button("Upgrade to Pro (Rs. 500/month)"):
            st.session_state["page"] = "upgrade"
            st.rerun()
    
    # Stats overview
    projects = db.get_projects(user["user_id"])
    clients = db.get_clients(user["user_id"])
    invoices = db.get_invoices(user_id=user["user_id"])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Active Projects", len([p for p in projects if p["status"] == "Ongoing"]))
    with col2:
        st.metric("Total Clients", len(clients))
    with col3:
        total_earnings = sum(float(inv["amount"]) for inv in invoices if inv["is_paid"])
        st.metric("Total Earnings", f"Rs. {total_earnings:,.2f}")
    
    # Navigation
    st.sidebar.title("Navigation")
    pages = {
        "Dashboard": "dashboard",
        "Clients": "clients",
        "Projects": "projects",
        "Invoices": "invoices",
        "Notes": "notes",
        "Settings": "settings"
    }
    
    for page_name, page_id in pages.items():
        if st.sidebar.button(page_name):
            st.session_state["page"] = page_id
            st.rerun()
    
    st.sidebar.button("Logout", on_click=logout)
    
    # Recent activity
    st.subheader("Recent Activity")
    
    recent_projects = sorted(projects, key=lambda x: x["created_at"], reverse=True)[:5]
    if recent_projects:
        st.write(pd.DataFrame(recent_projects)[["title", "deadline", "status"]])
    else:
        st.info("No projects yet. Add your first project to get started!")
    
    # Upcoming deadlines
    upcoming = [p for p in projects if p["status"] == "Ongoing"]
    upcoming = sorted(upcoming, key=lambda x: x["deadline"])[:3]
    
    if upcoming:
        st.subheader("Upcoming Deadlines")
        for project in upcoming:
            deadline = datetime.strptime(project["deadline"], "%Y-%m-%d")
            days_left = (deadline - datetime.now()).days
            st.write(f"- {project['title']}: {project['deadline']} ({days_left} days left)")