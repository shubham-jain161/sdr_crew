from agents.lead_generation_agent import LeadGenerationAgent
from agents.lead_research_agent import LeadResearchAgent
from agents.outreach_agent import OutreachAgent
from agents.conversation_agent import ConversationAgent
from tools.serp_api import SerpApiClient
import os
from typing import List, Dict

def process_generated_leads() -> List[Dict]:
    """Process leads generated through SERP API"""
    print("Starting SDR AI Crew System - Lead Generation...")
    
    try:
        # Initialize agents
        serp_client = SerpApiClient()
        lead_gen_agent = LeadGenerationAgent(serp_client)
        research_agent = LeadResearchAgent()
        outreach_agent = OutreachAgent()
        
        # Generate leads
        query = "B2B SaaS companies in USA"
        generated_leads = lead_gen_agent.generate_leads(query, num_results=5)
        
        if generated_leads:
            # Research generated leads
            print("\nResearching generated leads...")
            analyzed_leads = research_agent.analyze_leads(generated_leads)
            
            # Process outreach
            print("\nProcessing outreach for generated leads...")
            results = outreach_agent.process_leads(analyzed_leads)
            return results
    except Exception as e:
        print(f"Error in lead generation process: {e}")
    return []

def process_csv_leads() -> List[Dict]:
    """Process leads from external CSV file"""
    print("\nStarting SDR AI Crew System - CSV Processing...")
    
    try:
        # Initialize agents
        research_agent = LeadResearchAgent()
        outreach_agent = OutreachAgent()
        
        # Process leads from CSV
        csv_path = "sdr-ai-crew-system/data/leads.csv"
        
        if not os.path.exists(csv_path):
            print(f"CSV file not found: {csv_path}")
            return []
        
        # Research CSV leads
        print("Analyzing leads from CSV...")
        analyzed_leads = research_agent.process_csv_leads(csv_path)
        
        if analyzed_leads:
            # Process outreach
            print("\nProcessing outreach for CSV leads...")
            results = outreach_agent.process_leads(analyzed_leads)
            return results
    except Exception as e:
        print(f"Error in CSV processing: {e}")
    return []

def main():
    # Process both lead sources
    generated_results = process_generated_leads()
    csv_results = process_csv_leads()
    
    # Combined results
    all_results = generated_results + csv_results
    
    print("\nFinal Summary:")
    print(f"Total Leads Processed: {len(all_results)}")
    print(f"Successfully Contacted: {sum(1 for r in all_results if r.get('email_sent', False))}")
    print("-" * 50)

if __name__ == "__main__":
    main()