"""
News Storage Management
Handles persistent storage of news items with deduplication and history tracking.
"""

import json
import os
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from pathlib import Path

# Paths
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
NEWS_HISTORY_PATH = os.path.join(DATA_DIR, "news_history.json")


def ensure_data_dir():
    """Ensure data directory exists"""
    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)


def generate_item_hash(item: Dict) -> str:
    """
    Generate a unique hash for a news item based on title, link, and pub_date.
    This is used for deduplication.
    """
    # Use title, link, and pub_date to create unique identifier
    title = str(item.get("title", "")).strip().lower()
    link = str(item.get("link", "")).strip()
    pub_date = str(item.get("pub_date") or item.get("date", "")).strip()
    
    # Create hash string
    hash_string = f"{title}|{link}|{pub_date}"
    return hashlib.md5(hash_string.encode('utf-8')).hexdigest()


def load_news_history() -> Dict:
    """Load news history from JSON file"""
    ensure_data_dir()
    
    if not os.path.exists(NEWS_HISTORY_PATH):
        return {
            "feeds": {},
            "metadata": {
                "total_items": 0,
                "oldest_item": None,
                "newest_item": None,
                "created_at": datetime.now().isoformat()
            }
        }
    
    try:
        with open(NEWS_HISTORY_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Error loading news history: {e}")
        return {
            "feeds": {},
            "metadata": {
                "total_items": 0,
                "oldest_item": None,
                "newest_item": None,
                "created_at": datetime.now().isoformat()
            }
        }


def save_news_history(data: Dict):
    """Save news history to JSON file"""
    ensure_data_dir()
    
    try:
        # Update metadata
        all_items = []
        for feed_data in data.get("feeds", {}).values():
            all_items.extend(feed_data.get("items", []))
        
        if all_items:
            dates = [item.get("pub_date") or item.get("date", "") for item in all_items if item.get("pub_date") or item.get("date")]
            if dates:
                data["metadata"]["oldest_item"] = min(dates)
                data["metadata"]["newest_item"] = max(dates)
        else:
            data["metadata"]["oldest_item"] = None
            data["metadata"]["newest_item"] = None
        
        data["metadata"]["total_items"] = len(all_items)
        data["metadata"]["last_updated"] = datetime.now().isoformat()
        
        with open(NEWS_HISTORY_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving news history: {e}")


def save_news_item(feed_url: str, item: Dict) -> bool:
    """
    Save a news item to history if it doesn't already exist.
    Returns True if item was saved (new), False if it was a duplicate.
    """
    history = load_news_history()
    
    # Initialize feed entry if it doesn't exist
    if feed_url not in history["feeds"]:
        history["feeds"][feed_url] = {
            "last_updated": None,
            "items": []
        }
    
    # Generate hash for deduplication
    item_hash = generate_item_hash(item)
    
    # Check if item already exists
    existing_hashes = {existing_item.get("hash") for existing_item in history["feeds"][feed_url]["items"]}
    if item_hash in existing_hashes:
        return False  # Duplicate
    
    # Add hash and fetched_at timestamp to item
    item_with_meta = {
        **item,
        "hash": item_hash,
        "fetched_at": datetime.now().isoformat()
    }
    
    # Add to feed's items
    history["feeds"][feed_url]["items"].append(item_with_meta)
    
    # Update feed's last_updated
    history["feeds"][feed_url]["last_updated"] = datetime.now().isoformat()
    
    # Save to file
    save_news_history(history)
    
    return True  # New item saved


def get_news_history(feed_url: Optional[str] = None, limit: int = 50) -> List[Dict]:
    """
    Get news history for a specific feed or all feeds.
    
    Args:
        feed_url: Specific feed URL to get history for, or None for all feeds
        limit: Maximum number of items to return
    
    Returns:
        List of news items, sorted by date (newest first)
    """
    history = load_news_history()
    
    all_items = []
    
    if feed_url:
        # Get items for specific feed
        if feed_url in history["feeds"]:
            all_items = history["feeds"][feed_url]["items"]
    else:
        # Get items from all feeds
        for feed_data in history["feeds"].values():
            all_items.extend(feed_data.get("items", []))
    
    # Sort by date (newest first)
    def get_sort_key(item):
        date_str = item.get("pub_date") or item.get("date", "")
        if date_str:
            try:
                # Try to parse various date formats
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
                # Fallback to fetched_at if available
                fetched = item.get("fetched_at")
                if fetched:
                    try:
                        return datetime.fromisoformat(fetched)
                    except:
                        pass
        return datetime.min
    
    all_items.sort(key=get_sort_key, reverse=True)
    
    return all_items[:limit]


def get_existing_hashes(feed_url: Optional[str] = None) -> set:
    """
    Get set of existing item hashes for deduplication.
    
    Args:
        feed_url: Specific feed URL, or None for all feeds
    
    Returns:
        Set of hash strings
    """
    history = load_news_history()
    
    hashes = set()
    
    if feed_url:
        if feed_url in history["feeds"]:
            for item in history["feeds"][feed_url]["items"]:
                if "hash" in item:
                    hashes.add(item["hash"])
    else:
        for feed_data in history["feeds"].values():
            for item in feed_data.get("items", []):
                if "hash" in item:
                    hashes.add(item["hash"])
    
    return hashes


def cleanup_old_news(days_to_keep: int = 30) -> int:
    """
    Remove news items older than specified days.
    
    Args:
        days_to_keep: Number of days to keep
    
    Returns:
        Number of items removed
    """
    history = load_news_history()
    cutoff_date = datetime.now() - timedelta(days=days_to_keep)
    removed_count = 0
    
    for feed_url, feed_data in history["feeds"].items():
        original_count = len(feed_data["items"])
        
        # Filter items by date
        kept_items = []
        for item in feed_data["items"]:
            item_date = None
            date_str = item.get("pub_date") or item.get("date", "")
            
            if date_str:
                try:
                    try:
                        from dateutil import parser
                        item_date = parser.parse(date_str)
                    except ImportError:
                        # Fallback to simple datetime parsing
                        try:
                            item_date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                        except:
                            pass
                except:
                    # If can't parse, use fetched_at
                    fetched = item.get("fetched_at")
                    if fetched:
                        try:
                            item_date = datetime.fromisoformat(fetched)
                        except:
                            pass
            
            # Keep if date is after cutoff or if date couldn't be parsed (keep recent items)
            if item_date is None or item_date >= cutoff_date:
                kept_items.append(item)
            else:
                removed_count += 1
        
        feed_data["items"] = kept_items
    
    if removed_count > 0:
        save_news_history(history)
    
    return removed_count


def deduplicate_by_hash() -> int:
    """
    Remove duplicate items based on hash.
    Keeps the oldest version of each duplicate.
    
    Returns:
        Number of duplicates removed
    """
    history = load_news_history()
    removed_count = 0
    
    for feed_url, feed_data in history["feeds"].items():
        seen_hashes = {}
        unique_items = []
        
        for item in feed_data["items"]:
            item_hash = item.get("hash")
            if not item_hash:
                # Generate hash if missing
                item_hash = generate_item_hash(item)
                item["hash"] = item_hash
            
            if item_hash not in seen_hashes:
                seen_hashes[item_hash] = item
                unique_items.append(item)
            else:
                removed_count += 1
        
        feed_data["items"] = unique_items
    
    if removed_count > 0:
        save_news_history(history)
    
    return removed_count


def get_feed_stats(feed_url: Optional[str] = None) -> Dict:
    """
    Get statistics about news storage.
    
    Args:
        feed_url: Specific feed URL, or None for all feeds
    
    Returns:
        Dictionary with statistics
    """
    history = load_news_history()
    
    if feed_url:
        if feed_url not in history["feeds"]:
            return {
                "total_items": 0,
                "last_updated": None,
                "feed_url": feed_url
            }
        
        feed_data = history["feeds"][feed_url]
        return {
            "total_items": len(feed_data.get("items", [])),
            "last_updated": feed_data.get("last_updated"),
            "feed_url": feed_url
        }
    else:
        return {
            "total_items": history["metadata"].get("total_items", 0),
            "oldest_item": history["metadata"].get("oldest_item"),
            "newest_item": history["metadata"].get("newest_item"),
            "total_feeds": len(history["feeds"]),
            "last_updated": history["metadata"].get("last_updated")
        }
