from serpapi import GoogleSearch
import os
from typing import List, Dict, Optional
from dotenv import load_dotenv

class SerpApiClient:
    """SERP API client for lead generation"""
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("SERPAPI_API_KEY")
        if not self.api_key:
            raise ValueError("SERPAPI_API_KEY not found in environment variables")

    def search(self, query: str, num_results: int = 10) -> Optional[List[Dict]]:
        """Execute search using SERP API"""
        try:
            search = GoogleSearch({
                "q": query,
                "num": num_results,
                "api_key": self.api_key,
                "engine": "google"
            })
            
            return search.get_dict()
        except Exception as e:
            print(f"Error in SERP API search: {e}")
            return None