"""
Medical News Logic
Fetches and parses RSS feeds from medical sources.
Uses standard libraries (requests, xml) to avoid extra dependencies.
Enhanced with storage integration, deduplication, and smart caching.
"""

import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import streamlit as st
from typing import List, Dict, Optional
import json
import os
import time
import logging

# Import news storage module
try:
    from components.news_storage import (
        save_news_item,
        get_news_history,
        get_existing_hashes,
        cleanup_old_news,
        get_feed_stats
    )
    STORAGE_AVAILABLE = True
except ImportError:
    STORAGE_AVAILABLE = False
    logging.warning("news_storage module not available, running without history storage")

# Paths
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
LOCAL_NEWS_PATH = os.path.join(DATA_DIR, "local_news.json")
RSS_SOURCES_PATH = os.path.join(DATA_DIR, "rss_sources.json")
NEWS_CONFIG_PATH = os.path.join(DATA_DIR, "news_config.json")

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_json_data(filepath: str, default=None):
    """Load JSON data from file safely"""
    try:
        if not os.path.exists(filepath):
            return default if default is not None else []
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading {filepath}: {e}")
        return default if default is not None else []


def load_news_config() -> Dict:
    """Load news configuration"""
    default_config = {
        "update_on_page_load": True,
        "cache_ttl_minutes": 5,
        "max_items_per_feed": 10,
        "max_total_items": 50,
        "keep_history_days": 30,
        "auto_cleanup": True,
        "feeds": {
            "enabled": True,
            "timeout_seconds": 10,
            "retry_attempts": 2
        }
    }
    return load_json_data(NEWS_CONFIG_PATH, default=default_config)

def parse_rss_item(item, source_name: str) -> Dict:
    """Helper to parse XML item element"""
    # Namespaces are annoying in XML, try simple find first
    title = item.findtext("title") or ""
    link = item.findtext("link") or ""
    description = item.findtext("description") or ""
    pubDate = item.findtext("pubDate") or ""
    
    # Try to find pubDate in different formats
    if not pubDate:
        pubDate = item.findtext("published") or item.findtext("dc:date") or ""
    
    # Clean description (remove HTML tags if simple)
    # For now, just truncating if too long might be enough, but let's keep it raw
    
    return {
        "title": title.strip(),
        "link": link.strip(),
        "summary": description.strip(),  # Mapping description to summary for consistency
        "date": pubDate.strip(),
        "pub_date": pubDate.strip(),  # Add pub_date for consistency
        "source": source_name
    }

def fetch_news_feed_with_retry(url: str, source_name: str, timeout: int = 10, retry_attempts: int = 2) -> List[Dict]:
    """
    Fetch and parse RSS feed with retry logic.
    
    Args:
        url: RSS feed URL
        source_name: Name of the source
        timeout: Request timeout in seconds
        retry_attempts: Number of retry attempts
    
    Returns:
        List of news items
    """
    last_error = None
    
    for attempt in range(retry_attempts + 1):
        try:
            response = requests.get(url, timeout=timeout)
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
                xml_items = root.findall(".//item")  # Recursive search
            
            for item in xml_items:
                news_item = parse_rss_item(item, source_name)
                if news_item.get("title") and news_item.get("link"):  # Only add valid items
                    items.append(news_item)
            
            logger.info(f"Successfully fetched {len(items)} items from {source_name}")
            return items
            
        except requests.exceptions.Timeout:
            last_error = f"Timeout after {timeout}s"
            logger.warning(f"Timeout fetching {source_name} (attempt {attempt + 1}/{retry_attempts + 1})")
            if attempt < retry_attempts:
                time.sleep(1 * (attempt + 1))  # Exponential backoff
        except requests.exceptions.RequestException as e:
            last_error = str(e)
            logger.warning(f"Error fetching {source_name} (attempt {attempt + 1}/{retry_attempts + 1}): {e}")
            if attempt < retry_attempts:
                time.sleep(1 * (attempt + 1))  # Exponential backoff
        except ET.ParseError as e:
            last_error = f"Invalid XML: {str(e)}"
            logger.error(f"XML parse error for {source_name}: {e}")
            break  # Don't retry on parse errors
        except Exception as e:
            last_error = str(e)
            logger.error(f"Unexpected error fetching {source_name}: {e}")
            break  # Don't retry on unexpected errors
    
    # Return error item if all attempts failed
    logger.error(f"Failed to fetch {source_name} after {retry_attempts + 1} attempts: {last_error}")
    return [{"title": f"Không thể tải tin từ {source_name}", "summary": last_error or "Unknown error", "error": True}]


@st.cache_data(ttl=300)  # Cache for 5 minutes (configurable via config)
def fetch_news_feed(url: str, source_name: str, use_storage: bool = True) -> List[Dict]:
    """
    Fetch and parse RSS feed with storage integration and deduplication.
    
    Args:
        url: RSS feed URL
        source_name: Name of the source
        use_storage: Whether to use storage for deduplication and history
    
    Returns:
        List of news items (new items first, then from history)
    """
    config = load_news_config()
    timeout = config.get("feeds", {}).get("timeout_seconds", 10)
    retry_attempts = config.get("feeds", {}).get("retry_attempts", 2)
    max_items = config.get("max_items_per_feed", 10)
    
    # Fetch new items from RSS
    new_items = fetch_news_feed_with_retry(url, source_name, timeout, retry_attempts)
    
    # Filter out error items
    valid_new_items = [item for item in new_items if not item.get("error")]
    
    # Save new items to storage and get only truly new ones
    if STORAGE_AVAILABLE and use_storage:
        existing_hashes = get_existing_hashes(url)
        truly_new_items = []
        
        for item in valid_new_items:
            # Check if item is new by trying to save it
            is_new = save_news_item(url, item)
            if is_new:
                truly_new_items.append(item)
        
        # Get historical items if we don't have enough new ones
        historical_items = []
        if len(truly_new_items) < max_items:
            historical_items = get_news_history(feed_url=url, limit=max_items - len(truly_new_items))
            # Convert historical items to display format
            historical_items = [
                {
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "summary": item.get("summary", item.get("description", "")),
                    "date": item.get("date", item.get("pub_date", "")),
                    "pub_date": item.get("pub_date", item.get("date", "")),
                    "source": item.get("source", source_name)
                }
                for item in historical_items
            ]
        
        # Combine new and historical items
        all_items = truly_new_items + historical_items
        # Remove duplicates (in case historical items overlap with new)
        seen_links = set()
        unique_items = []
        for item in all_items:
            link = item.get("link", "")
            if link and link not in seen_links:
                seen_links.add(link)
                unique_items.append(item)
        
        return unique_items[:max_items]
    else:
        # Without storage, just return new items
        return valid_new_items[:max_items]

def check_for_new_news(feed_url: str) -> int:
    """
    Check how many new news items are available for a feed.
    
    Args:
        feed_url: RSS feed URL to check
    
    Returns:
        Number of new items (estimated)
    """
    if not STORAGE_AVAILABLE:
        return 0
    
    try:
        # Get existing hashes
        existing_hashes = get_existing_hashes(feed_url)
        
        # Fetch current feed
        config = load_news_config()
        timeout = config.get("feeds", {}).get("timeout_seconds", 10)
        rss_sources = load_json_data(RSS_SOURCES_PATH)
        
        # Find source name
        source_name = "Unknown"
        for source in rss_sources:
            if source.get("url") == feed_url:
                source_name = source.get("name", "Unknown")
                break
        
        # Fetch feed
        new_items = fetch_news_feed_with_retry(feed_url, source_name, timeout, 1)
        valid_items = [item for item in new_items if not item.get("error")]
        
        # Count new items
        from components.news_storage import generate_item_hash
        new_count = 0
        for item in valid_items:
            item_hash = generate_item_hash(item)
            if item_hash not in existing_hashes:
                new_count += 1
        
        return new_count
    except Exception as e:
        logger.error(f"Error checking for new news: {e}")
        return 0


def get_medical_news(force_refresh: bool = False) -> Dict[str, List[Dict]]:
    """
    Get all news (Local JSON + International Live RSS with history).
    
    Args:
        force_refresh: Force refresh even if cache is valid
    
    Returns:
        Dictionary with 'local' and 'international' news lists, plus metadata
    """
    config = load_news_config()
    
    # 1. Local/Curated News (from JSON)
    local_news = load_json_data(LOCAL_NEWS_PATH, default=[])
    
    # 2. International News (Live from RSS + History)
    rss_sources = load_json_data(RSS_SOURCES_PATH, default=[])
    intl_news = []
    new_items_count = 0
    last_updated = None
    
    # Auto cleanup if enabled
    if STORAGE_AVAILABLE and config.get("auto_cleanup", True):
        try:
            days_to_keep = config.get("keep_history_days", 30)
            removed = cleanup_old_news(days_to_keep)
            if removed > 0:
                logger.info(f"Cleaned up {removed} old news items")
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
    
    # Fetch from RSS sources
    max_total = config.get("max_total_items", 50)
    feeds_enabled = config.get("feeds", {}).get("enabled", True)
    
    if feeds_enabled:
        for source in rss_sources:
            if len(intl_news) >= max_total:
                break
            
            try:
                feed_items = fetch_news_feed(
                    source['url'],
                    source['name'],
                    use_storage=STORAGE_AVAILABLE
                )
                
                # Count new items
                for item in feed_items:
                    if not item.get("error"):
                        # Check if this is a new item (has fetched_at timestamp)
                        if item.get("fetched_at"):
                            new_items_count += 1
                
                intl_news.extend(feed_items)
                
                # Get last updated time for this feed
                if STORAGE_AVAILABLE:
                    stats = get_feed_stats(source['url'])
                    feed_last_updated = stats.get("last_updated")
                    if feed_last_updated:
                        try:
                            feed_time = datetime.fromisoformat(feed_last_updated)
                            if last_updated is None or feed_time > last_updated:
                                last_updated = feed_time
                        except:
                            pass
            except Exception as e:
                logger.error(f"Error fetching feed {source.get('name', 'Unknown')}: {e}")
                # Add error item
                intl_news.append({
                    "title": f"Lỗi khi tải tin từ {source.get('name', 'Unknown')}",
                    "link": "#",
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "source": source.get('name', 'Unknown'),
                    "summary": str(e),
                    "error": True
                })
    
    # Fallback if no internet or empty
    if not intl_news:
        # Try to get from history if available
        if STORAGE_AVAILABLE:
            historical_items = get_news_history(limit=max_total)
            if historical_items:
                intl_news = [
                    {
                        "title": item.get("title", ""),
                        "link": item.get("link", ""),
                        "summary": item.get("summary", item.get("description", "")),
                        "date": item.get("date", item.get("pub_date", "")),
                        "source": item.get("source", "History"),
                        "from_history": True
                    }
                    for item in historical_items
                ]
        
        # If still empty, show error message
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
    
    # Sort international news by date (newest first)
    def get_sort_key(item):
        date_str = item.get("pub_date") or item.get("date", "")
        if date_str:
            try:
                try:
                    from dateutil import parser
                    return parser.parse(date_str)
                except ImportError:
                    # Fallback to simple datetime parsing
                    try:
                        return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                    except:
                        pass
            except:
                pass
        # Fallback to fetched_at if available
        fetched = item.get("fetched_at")
        if fetched:
            try:
                return datetime.fromisoformat(fetched)
            except:
                pass
        return datetime.min
    
    intl_news.sort(key=get_sort_key, reverse=True)
    
    # Limit total items
    intl_news = intl_news[:max_total]
    
    return {
        "local": local_news,
        "international": intl_news,
        "metadata": {
            "new_items_count": new_items_count,
            "last_updated": last_updated.isoformat() if last_updated else None,
            "total_international": len(intl_news),
            "storage_enabled": STORAGE_AVAILABLE
        }
    }
