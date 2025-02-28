import streamlit as st
import sys
import os
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables before anything else
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))

# Verify environment variables are loaded
if not all([
    os.getenv("AZURE_OPENAI_API_KEY"),
    os.getenv("AZURE_OPENAI_ENDPOINT"),
    os.getenv("AZURE_COMMUNICATION_CONNECTION_STRING")
]):
    st.error("Environment variables not loaded correctly")
    st.info("Current values:")
    st.write(f"AZURE_OPENAI_API_KEY: {'✅' if os.getenv('AZURE_OPENAI_API_KEY') else '❌'}")
    st.write(f"AZURE_OPENAI_ENDPOINT: {'✅' if os.getenv('AZURE_OPENAI_ENDPOINT') else '❌'}")
    st.write(f"AZURE_COMMUNICATION_CONNECTION_STRING: {'✅' if os.getenv('AZURE_COMMUNICATION_CONNECTION_STRING') else '❌'}")

# Add parent directory to path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

st.set_page_config(
    page_title="Gama AI",  # Changed title
    page_icon="🤖",
    layout="wide"
)

def get_mock_metrics():
    return {
        "leads": {"value": 127, "delta": 15},
        "emails": {"value": 89, "delta": 12},
        "responses": {"value": 34, "delta": 5},
        "meetings": {"value": 8, "delta": 2}
    }

def display_metrics():
    metrics = get_mock_metrics()
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Leads Generated", 
                 value=metrics["leads"]["value"], 
                 delta=metrics["leads"]["delta"])
    with col2:
        st.metric(label="Emails Sent", 
                 value=metrics["emails"]["value"], 
                 delta=metrics["emails"]["delta"])
    with col3:
        st.metric(label="Responses", 
                 value=metrics["responses"]["value"], 
                 delta=metrics["responses"]["delta"])
    with col4:
        st.metric(label="Meetings Scheduled", 
                 value=metrics["meetings"]["value"], 
                 delta=metrics["meetings"]["delta"])

def display_recent_activity():
    st.subheader("Recent Activity")
    
    activities = [
        {"time": "10 mins ago", "action": "New lead generated: TechCorp"},
        {"time": "1 hour ago", "action": "Email sent to DataSoft"},
        {"time": "2 hours ago", "action": "Response received from AITech"},
        {"time": "1 day ago", "action": "Meeting scheduled with CloudServ"}
    ]
    
    for activity in activities:
        st.write(f"**{activity['time']}:** {activity['action']}")

def main():
    # Sidebar
    st.sidebar.title("Gama AI")  # Changed sidebar title
    st.sidebar.success("Select a feature above.")
    
    # Main content
    st.title("Welcome to Gama AI SDR System 🚀")
    
    # Welcome message
    st.markdown("""
    ### Your AI-Powered Sales Development Platform
    
    Streamline your sales process with our intelligent SDR system:
    
    - 🎯 **Smart Lead Generation**: Find qualified prospects automatically
    - 🔍 **Deep Lead Research**: Get detailed company insights
    - 📧 **Automated Outreach**: Personalized email campaigns
    - 💬 **Intelligent Conversations**: AI-powered response handling
    """)
    
    # Display metrics
    st.markdown("---")
    st.subheader("Dashboard Overview")
    display_metrics()
    
    # Two-column layout for activity and quick actions
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("---")
        display_recent_activity()
    
    with col2:
        st.markdown("---")
        st.subheader("Quick Actions")
        st.button("✨ Generate New Leads")
        st.button("📊 Export Reports")
        st.button("📧 Send Bulk Emails")

if __name__ == "__main__":
    main()