import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from agents.conversation_agent import ConversationAgent

st.set_page_config(page_title="Conversations", page_icon="💬")

def main():
    st.title("Conversation Management 💬")
    
    # Fake data for demonstration
    conversations = {
        "Active": [
            {"company": "TechCorp", "status": "Negotiating", "last_contact": "2 days ago"},
            {"company": "DataSoft", "status": "Following Up", "last_contact": "1 day ago"}
        ],
        "Completed": [
            {"company": "AITech", "status": "Closed Won", "last_contact": "1 week ago"},
            {"company": "CloudServ", "status": "Closed Lost", "last_contact": "3 days ago"}
        ]
    }
    
    tab1, tab2 = st.tabs(["Active Conversations", "Completed"])
    
    with tab1:
        st.write("### Active Conversations")
        for conv in conversations["Active"]:
            with st.container():
                col1, col2, col3 = st.columns([2,1,1])
                with col1:
                    st.write(f"**{conv['company']}**")
                with col2:
                    st.write(conv['status'])
                with col3:
                    st.write(conv['last_contact'])
    
    with tab2:
        st.write("### Completed Conversations")
        for conv in conversations["Completed"]:
            with st.container():
                col1, col2, col3 = st.columns([2,1,1])
                with col1:
                    st.write(f"**{conv['company']}**")
                with col2:
                    st.write(conv['status'])
                with col3:
                    st.write(conv['last_contact'])

if __name__ == "__main__":
    main()