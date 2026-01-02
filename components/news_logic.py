"""
Medical News Logic
Fetches and parses RSS feeds from medical sources.
Uses standard libraries (requests, xml) to avoid extra dependencies.
"""

import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import streamlit as st
from typing import List, Dict, Optional
import json
import os

# Paths
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
LOCAL_NEWS_PATH = os.path.join(DATA_DIR, "local_news.json")
RSS_SOURCES_PATH = os.path.join(DATA_DIR, "rss_sources.json")

def load_json_data(filepath: str) -> List[Dict]:
    """Load list of dicts from JSON file safely"""
    try:
        if not os.path.exists(filepath):
            return []
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return []

def parse_rss_item(item, source_name: str) -> Dict:
    """Helper to parse XML item element"""
    # Namespaces are annoying in XML, try simple find first
    title = item.findtext("title")
    link = item.findtext("link")
    description = item.findtext("description")
    pubDate = item.findtext("pubDate")

    # Clean description (remove HTML tags if simple)
    # For now, just truncating if too long might be enough, but let's keep it raw
    
    return {
        "title": title,
        "link": link,
        "summary": description, # Mapping description to summary for consistency
        "date": pubDate, # TODO: Format date nicely
        "source": source_name
    }

@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_news_feed(url: str, source_name: str) -> List[Dict]:
    """
    Fetch and parse RSS feed.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        # Determine encoding if possible, else utf-8
        response.encoding = 'utf-8' 
        
        root = ET.fromstring(response.content)
        items = []
        
        # Parse standard RSS 2.0
        # Usually items are under channel/item
        channel = root.find("channel")
        if channel is not None:
            xml_items = channel.findall("item")
        else:
            # Fallback for some feeds (Atom/RSS1.0 might be different structure)
             xml_items = root.findall(".//item") # Recursive search

        for item in xml_items[:5]: # Limit to 5 items per source
            news_item = parse_rss_item(item, source_name)
            items.append(news_item)
            
        return items
    except Exception as e:
        # Return error item so UI knows, or just empty list to hide failure
        return [{"title": f"Không thể tải tin từ {source_name}", "summary": str(e), "error": True}]

def get_medical_news() -> Dict[str, List[Dict]]:
    """
    Get all news (Local JSON + International Live RSS)
    """
    # 1. Local/Curated News (from JSON)
    local_news = load_json_data(LOCAL_NEWS_PATH)
    
    # 2. International News (Live from RSS)
    rss_sources = load_json_data(RSS_SOURCES_PATH)
    intl_news = []
    
    # Simple strategy: Fetch first 2 sources to avoid waiting too long
    # Or fetch all. Let's try fetching first 2 for performance in this demo
    for source in rss_sources[:3]:
        feed_items = fetch_news_feed(source['url'], source['name'])
        intl_news.extend(feed_items)
    
    # Fallback if no internet or empty
    if not intl_news:
         intl_news = [
            {
                "title": "International News Unavailable",
                "link": "#",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "source": "System",
                "summary": "Could not fetch live RSS feeds. Please check internet connection."
            }
         ]
    
    return {
        "local": local_news,
        "international": intl_news
    }
