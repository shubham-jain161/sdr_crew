import streamlit as st
import sys
import os

# Add parent directory to path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from agents.lead_generation_agent import LeadGenerationAgent
from tools.serp_api import SerpApiClient

st.set_page_config(page_title="Lead Generation", page_icon="🎯")

def main():
    st.title("Lead Generation 🎯")
    
    # Search query input
    query = st.text_input("Enter your search query:", 
                         placeholder="e.g., B2B SaaS companies in USA")
    
    num_results = st.slider("Number of results:", 5, 50, 10)
    
    if st.button("Generate Leads"):
        with st.spinner("Generating leads..."):
            try:
                # Initialize agents
                serp_client = SerpApiClient()
                lead_gen_agent = LeadGenerationAgent(serp_client)
                
                # Generate leads
                leads = lead_gen_agent.generate_leads(query, num_results)
                
                # Display results
                if leads:
                    st.success(f"Found {len(leads)} leads!")
                    for lead in leads:
                        with st.expander(f"📊 {lead['company_name']}"):
                            st.write(f"Website: {lead['website']}")
                            st.write(f"Description: {lead['description']}")
                else:
                    st.warning("No leads found. Try adjusting your search query.")
                    
            except Exception as e:
                st.error(f"Error generating leads: {str(e)}")

if __name__ == "__main__":
    main()