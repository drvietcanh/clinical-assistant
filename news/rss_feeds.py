"""
RSS Feed Configuration
Medical news RSS feeds from various sources
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class RSSFeed:
    """RSS Feed information"""
    name: str
    url: str
    category: str  # Cardiology, Infectious, General, etc.
    language: str = "en"  # en, vi
    description: str = ""


# RSS Feeds Configuration
RSS_FEEDS: List[RSSFeed] = [
    # === GENERAL MEDICAL NEWS ===
    RSSFeed(
        name="Medscape Medical News",
        url="https://www.medscape.com/rss/allnews",
        category="General",
        language="en",
        description="Latest medical news from Medscape"
    ),
    RSSFeed(
        name="Healthline Medical News",
        url="https://www.healthline.com/rss/health-news",
        category="General",
        language="en",
        description="Health news from Healthline"
    ),
    RSSFeed(
        name="Medical News Today",
        url="https://www.medicalnewstoday.com/rss",
        category="General",
        language="en",
        description="Medical news from Medical News Today"
    ),
    
    # === CARDIOLOGY ===
    RSSFeed(
        name="Medscape Cardiology",
        url="https://www.medscape.com/rss/cardiology",
        category="Cardiology",
        language="en",
        description="Cardiology news from Medscape"
    ),
    
    # === INFECTIOUS DISEASES ===
    RSSFeed(
        name="Medscape Infectious Diseases",
        url="https://www.medscape.com/rss/infectious-diseases",
        category="Infectious",
        language="en",
        description="Infectious diseases news from Medscape"
    ),
    
    # === ONCOLOGY ===
    RSSFeed(
        name="Medscape Oncology",
        url="https://www.medscape.com/rss/oncology",
        category="Oncology",
        language="en",
        description="Oncology news from Medscape"
    ),
    
    # === NEUROLOGY ===
    RSSFeed(
        name="Medscape Neurology",
        url="https://www.medscape.com/rss/neurology",
        category="Neurology",
        language="en",
        description="Neurology news from Medscape"
    ),
    
    # === RESEARCH & PUBMED ===
    RSSFeed(
        name="PubMed Latest",
        url="https://pubmed.ncbi.nlm.nih.gov/rss/search/1?fc=Y&filters=DatesFilter:2024-01-01:2025-12-31",
        category="Research",
        language="en",
        description="Latest research articles from PubMed"
    ),
    
    # === GUIDELINES & UPDATES ===
    RSSFeed(
        name="NEJM This Week",
        url="https://www.nejm.org/action/showFeed?type=etoc&feed=rss&jc=nejm",
        category="Guidelines",
        language="en",
        description="New England Journal of Medicine updates"
    ),
]


def get_feeds_by_category(category: str) -> List[RSSFeed]:
    """Get RSS feeds filtered by category"""
    if category == "All" or not category:
        return RSS_FEEDS
    return [feed for feed in RSS_FEEDS if feed.category == category]


def get_all_categories() -> List[str]:
    """Get list of all available categories"""
    categories = set(feed.category for feed in RSS_FEEDS)
    return sorted(list(categories))

