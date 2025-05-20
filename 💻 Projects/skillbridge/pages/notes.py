import streamlit as st
import json
import os
from datetime import datetime
import uuid
import pandas as pd
from PIL import Image

# Logo and branding
logo = Image.open("skillbridge_logo.png")  # You'll need to create this

def notes_page():
    user = st.session_state["user"]
    st.title("Notes")
    
    # Add new note
    with st.expander("Add New Note"):
        with st.form("new_note_form"):
            title = st.text_input("Note Title")
            content = st.text_area("Content")
            submit = st.form_submit_button("Save Note")
            
            if submit:
                new_note = {
                    "note_id": str(uuid.uuid4()),
                    "user_id": user["user_id"],
                    "title": title,
                    "content": content,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                db.add_note(new_note)
                st.success("Note saved successfully!")
                st.rerun()
    
    # View notes
    notes = db.get_notes(user["user_id"])
    
    if notes:
        st.subheader("Your Notes")
        
        # Search notes
        search_term = st.text_input("Search notes")
        
        filtered_notes = notes
        if search_term:
            filtered_notes = [
                n for n in notes 
                if search_term.lower() in n["title"].lower() or search_term.lower() in n["content"].lower()
            ]
        
        if filtered_notes:
            for note in filtered_notes:
                with st.expander(note["title"]):
                    st.write(note["content"])
                    st.caption(f"Created: {note['created_at']}")
                    
                    if st.button(f"Delete {note['title']}", key=f"delete_{note['note_id']}"):
                        # Delete note from database
                        data = db.load_data()
                        data["notes"] = [n for n in data["notes"] if n["note_id"] != note["note_id"]]
                        db.save_data(data)
                        st.success("Note deleted!")
                        st.rerun()
        else:
            st.info("No notes match your search")
    else:
        st.info("No notes added yet. Add your first note to get started!")