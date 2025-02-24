from typing import List, Dict, Optional
from tools.serp_api import SerpApiClient

class LeadGenerationAgent:
    """Agent responsible for generating leads using SERP API"""
    def __init__(self, serp_api_client: Optional[SerpApiClient] = None):
        self.serp_api_client = serp_api_client or SerpApiClient()

    def generate_leads(self, query: str, num_results: int = 5) -> List[Dict]:
        """Generate leads using SERP API search"""
        print(f"Searching for leads with query: {query}")
        
        search_results = self.serp_api_client.search(query, num_results)
        if not search_results:
            print("No search results found")
            return []
            
        leads = self.process_results(search_results)
        print(f"Found {len(leads)} potential leads")
        return leads

    def process_results(self, search_results: Dict) -> List[Dict]:
        """Process search results into lead format"""
        leads = []
        for result in search_results.get("organic_results", []):
            lead = {
                "company_name": result.get("title"),
                "website": result.get("link"),
                "description": result.get("snippet"),
                "source": "SERP API",
                "contact_email": None,
                "contact_name": None,
                "industry": None
            }
            leads.append(lead)
        return leads