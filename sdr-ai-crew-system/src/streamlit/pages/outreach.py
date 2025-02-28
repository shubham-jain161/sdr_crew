import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from agents.outreach_agent import OutreachAgent

st.set_page_config(page_title="Email Outreach", page_icon="📧")

def main():
    st.title("Email Outreach 📧")
    
    # Check environment variables first
    if not os.getenv("AZURE_COMMUNICATION_CONNECTION_STRING"):
        st.error("❌ Azure Communication Services not configured!")
        st.info("Please add AZURE_COMMUNICATION_CONNECTION_STRING to your .env file")
        return
        
    if not os.getenv("AZURE_COMMUNICATION_SENDER_EMAIL"):
        st.error("❌ Sender email not configured!")
        st.info("Please add AZURE_COMMUNICATION_SENDER_EMAIL to your .env file")
        return
    
    # Add email configuration section
    with st.expander("Email Configuration"):
        sender_email = st.text_input("Sender Email", value=os.getenv("AZURE_COMMUNICATION_SENDER_EMAIL", ""))
        if not sender_email:
            st.warning("Please configure sender email in .env file")
    
    with st.form("outreach_form"):
        st.write("### Lead Information")
        company_name = st.text_input("Company Name")
        contact_name = st.text_input("Contact Name")
        contact_email = st.text_input("Contact Email")  # Added email input
        contact_role = st.text_input("Contact Role")
        
        st.write("### Customization")
        tone = st.select_slider(
            "Email Tone",
            options=["Formal", "Professional", "Casual", "Friendly"]
        )
        
        value_prop = st.text_area("Value Proposition")
        
        submitted = st.form_submit_button("Generate Email")
        
        if submitted:
            if not contact_email:
                st.error("Contact email is required")
                return
                
            with st.spinner("Generating personalized email..."):
                try:
                    outreach_agent = OutreachAgent()
                    email_content = outreach_agent.generate_email({
                        'company_name': company_name,
                        'contact_name': contact_name,
                        'contact_email': contact_email,
                        'contact_role': contact_role,
                    })
                    
                    st.success("Email Generated!")
                    with st.expander("Preview Email"):
                        st.write("**Subject:**", email_content['subject'])
                        st.write("**Content:**")
                        st.code(email_content['content'], language="text")
                    
                    if st.button("Send Email"):
                        success = outreach_agent.send_email(
                            recipient=contact_email,
                            subject=email_content['subject'],
                            content=email_content['content']
                        )
                        if success:
                            st.success(f"Email sent successfully to {contact_email}!")
                        else:
                            st.error("Failed to send email. Please check your configuration.")
                        
                except Exception as e:
                    st.error(f"Error generating email: {str(e)}")
                    st.info("Please check your .env file for AZURE_COMMUNICATION_CONNECTION_STRING")

if __name__ == "__main__":
    main()