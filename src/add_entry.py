# src/add_entry.py
import streamlit as st
import pandas as pd
from datetime import date
import os

DATA_PATH = os.path.join("data", "spices_entries.csv")

# Ensure data folder exists
if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists(DATA_PATH):
    pd.DataFrame(columns=["Date", "Category", "Reflection"]).to_csv(DATA_PATH, index=False)

def show_add_entry_form():
    st.subheader("✍️ Add a New SPICES Entry")
    st.write("Reflect on your personal growth across UTSA's SPICES dimensions.")

    # Input fields
    category = st.selectbox(
        "Select a SPICES Category",
        [
            "Service",
            "Professional Development",
            "Intellectual Achievement",
            "Cultural Exploration",
            "Engaged Living",
            "Skill Development",
        ],
    )

    entry_date = st.date_input("Date", date.today())
    reflection = st.text_area("Reflection", placeholder="What did you do? What did you learn?")

    # Save button
    if st.button("💾 Save Entry"):
        if reflection.strip() == "":
            st.warning("Please enter a reflection before saving.")
        else:
            new_entry = pd.DataFrame([[entry_date, category, reflection]],
                                     columns=["Date", "Category", "Reflection"])
            new_entry.to_csv(DATA_PATH, mode="a", header=False, index=False)
            st.success("✅ Entry saved successfully!")


