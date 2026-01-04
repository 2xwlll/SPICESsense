# app.py
import streamlit as st
import sys
from pathlib import Path
import os
import pandas as pd
from datetime import date

# Add src directory to Python path so imports work
sys.path.append(str(Path(__file__).resolve().parent / "src"))

# Import the Add Entry function
from add_entry import show_add_entry_form

# ------------------ Helper functions for other pages ------------------

def show_home():
    st.title("🌶️ SPICESsense Dashboard")
    st.markdown(
        """
        Welcome to **SPICESsense** — a UTSA-inspired tracker and reflection tool that helps you record growth in:
        - 🧠 **Intellectual Achievement**
        - 🤝 **Service**
        - 🌍 **Cultural Exploration**
        - 🧩 **Skill Development**
        - 🚀 **Professional Development**
        - 🏡 **Engaged Living**
        """
    )
    st.write("Use the sidebar to add entries or view your progress!")

def show_progress():
    st.title("📊 View Progress")

    DATA_PATH = os.path.join("data", "spices_entries.csv")
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        if df.empty:
            st.info("No entries yet. Add some SPICES experiences first!")
        else:
            st.subheader("All Entries")
            st.dataframe(df)

            st.subheader("Entries by Category")
            chart_data = df['Category'].value_counts()
            st.bar_chart(chart_data)

            st.subheader("Entries Over Time")
            df['Date'] = pd.to_datetime(df['Date'])
            timeline = df.groupby('Date').size()
            st.line_chart(timeline)
    else:
        st.info("No entries yet. Add some SPICES experiences first!")

def show_settings():
    st.title("⚙️ Settings")
    st.write("Adjust preferences and data options here.")

# ------------------ Streamlit App ------------------

st.set_page_config(page_title="SPICESsense", page_icon="🌶️", layout="wide")

# Sidebar navigation
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Add Entry", "View Progress", "Settings"]
)

# Render the selected page
if page == "Home":
    show_home()
elif page == "Add Entry":
    show_add_entry_form()
elif page == "View Progress":
    show_progress()
elif page == "Settings":
    show_settings()

