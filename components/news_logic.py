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

# Constants
RSS_SOURCES = {
    "WHO Outbreak News": "https://www.who.int/feeds/entity/emergencies/disease-outbreak-news/en/rss.xml",
    # "PubMed - Clinical": "https://pubmed.ncbi.nlm.nih.gov/rss/search/1/K3... (Dynamic)" # Add later if needed
}

MOCK_VN_NEWS = [
    {
        "title": "Bộ Y tế ban hành Hướng dẫn Chẩn đoán và Điều trị Sốt xuất huyết Dengue (2024)",
        "link": "#",
        "date": "2024-08-15",
        "source": "Bộ Y Tế",
        "summary": "Cập nhật tiêu chuẩn chẩn đoán, phân độ lâm sàng và phác đồ điều trị dịch truyền..."
    },
    {
        "title": "Cảnh báo gia tăng ca mắc Sởi tại một số địa phương",
        "link": "#",
        "date": "2024-09-01",
        "source": "Cục YTDP",
        "summary": "Nhiều ca biến chứng nặng do không tiêm chủng đầy đủ..."
    },
    {
        "title": "Hướng dẫn mới về quản lý Tăng huyết áp tại tuyến cơ sở",
        "link": "#",
        "date": "2024-07-20",
        "source": "Bộ Y Tế",
        "summary": "Nhấn mạnh vai trò của phối hợp thuốc sớm và theo dõi huyết áp tại nhà..."
    }
]

def parse_rss_item(item) -> Dict:
    """Helper to parse XML item element"""
    return {
        "title": item.findtext("title"),
        "link": item.findtext("link"),
        "description": item.findtext("description"),
        "pubDate": item.findtext("pubDate"),
        "source": "International"
    }

@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_news_feed(url: str, source_name: str) -> List[Dict]:
    """
    Fetch and parse RSS feed.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        items = []
        
        # Parse standard RSS 2.0
        for item in root.findall(".//item")[:10]: # Limit to 10 items
            news_item = parse_rss_item(item)
            news_item["source"] = source_name
            items.append(news_item)
            
        return items
    except Exception as e:
        # Return error item so UI knows
        return [{"title": f"Không thể tải tin từ {source_name}", "summary": str(e), "error": True}]

def get_medical_news() -> Dict[str, List[Dict]]:
    """
    Get all news (Local Mock + International Live)
    """
    # 1. Local News (Mock)
    local_news = MOCK_VN_NEWS
    
    # 2. International News (Live)
    # Note: WHO RSS might be unstable depending on region, wrap safe
    intl_news = []
    # Uncomment to enable live fetch when internet is guaranteed
    # intl_news = fetch_news_feed(RSS_SOURCES["WHO Outbreak News"], "WHO")
    
    # Fallback/Demo content for International if fetch fails or disabled
    if not intl_news or intl_news[0].get("error"):
         intl_news = [
            {
                "title": "WHO: Global Strategy for Influenza 2024-2030",
                "link": "https://www.who.int",
                "date": "2024-09-10",
                "source": "WHO",
                "summary": "Strengthening country capacities for influenza surveillance and response..."
            },
            {
                "title": "New Clinical Guidelines for Sepsis Management",
                "link": "https://www.who.int",
                "date": "2024-09-05",
                "source": "WHO/Intl",
                "summary": "Updated surviving sepsis campaign bundles..."
            }
         ]
    
    return {
        "local": local_news,
        "international": intl_news
    }
