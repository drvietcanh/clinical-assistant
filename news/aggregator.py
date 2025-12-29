"""
News Aggregator
Fetches and aggregates medical news from RSS feeds
"""

import feedparser
import streamlit as st
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from news.rss_feeds import RSS_FEEDS, get_feeds_by_category


@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_feed(feed_url: str) -> List[Dict]:
    """
    Fetch and parse a single RSS feed
    
    Args:
        feed_url: URL of the RSS feed
        
    Returns:
        List of news items
    """
    try:
        feed = feedparser.parse(feed_url)
        items = []
        
        for entry in feed.entries[:10]:  # Limit to 10 items per feed
            item = {
                "title": entry.get("title", "No title"),
                "link": entry.get("link", ""),
                "summary": entry.get("summary", entry.get("description", "")),
                "published": entry.get("published", ""),
                "published_parsed": entry.get("published_parsed"),
                "source": feed.feed.get("title", "Unknown"),
                "author": entry.get("author", ""),
            }
            items.append(item)
        
        return items
    except Exception as e:
        # Silently fail for individual feeds
        return []


def fetch_latest_news(limit: int = 20, category: Optional[str] = None) -> List[Dict]:
    """
    Fetch latest news from all RSS feeds
    
    Args:
        limit: Maximum number of news items to return
        category: Optional category filter
        
    Returns:
        List of news items sorted by date
    """
    feeds_to_fetch = get_feeds_by_category(category) if category else RSS_FEEDS
    
    all_news = []
    
    for feed in feeds_to_fetch:
        items = fetch_feed(feed.url)
        for item in items:
            item["category"] = feed.category
            all_news.append(item)
    
    # Sort by published date (newest first)
    all_news.sort(
        key=lambda x: x.get("published_parsed") or (2000, 1, 1),
        reverse=True
    )
    
    return all_news[:limit]


def get_news_by_category(category: str, limit: int = 20) -> List[Dict]:
    """
    Get news filtered by category
    
    Args:
        category: News category
        limit: Maximum number of items
        
    Returns:
        List of news items
    """
    return fetch_latest_news(limit=limit, category=category)


def get_cached_news() -> List[Dict]:
    """Get cached news (for display without refetching)"""
    # This will use Streamlit's cache
    return fetch_latest_news(limit=30)


def clear_cache():
    """Clear news cache"""
    fetch_feed.clear()
    get_cached_news.clear()

