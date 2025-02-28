import streamlit as st
import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from agents.lead_research_agent import LeadResearchAgent

st.set_page_config(page_title="Lead Research", page_icon="🔍")

def main():
    st.title("Lead Research 🔍")
    
    # Check Azure OpenAI configuration
    if not all([
        os.getenv("AZURE_OPENAI_API_KEY"),
        os.getenv("AZURE_OPENAI_ENDPOINT"),
        os.getenv("AZURE_OPENAI_API_VERSION")
    ]):
        st.error("❌ Azure OpenAI not configured!")
        st.info("Please check your .env file for Azure OpenAI credentials")
        return
    
    # File upload for CSV with leads
    uploaded_file = st.file_uploader("Upload your leads CSV", type=['csv'])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        
        if st.button("Research Selected Leads"):
            with st.spinner("Researching leads..."):
                try:
                    research_agent = LeadResearchAgent()
                    
                    progress_bar = st.progress(0)
                    for idx, lead in df.iterrows():
                        research_results = research_agent.research_lead(lead)
                        
                        with st.expander(f"🎯 {lead['company_name']}"):
                            st.write("### Research Results")
                            st.write(f"Industry: {research_results['industry']}")
                            st.write(f"Company Size: {research_results['company_size']}")
                            st.write(f"Key Decision Makers: {research_results['decision_makers']}")
                            st.write(f"Pain Points: {research_results['pain_points']}")
                        
                        progress_bar.progress((idx + 1)/len(df))
                        
                except Exception as e:
                    st.error(f"Error during research: {str(e)}")

if __name__ == "__main__":
    main()