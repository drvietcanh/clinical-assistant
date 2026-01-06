# Main Menu Redesign - Design Document

**Ngày tạo:** 2026-01-XX  
**Phiên bản:** 1.0  
**Trạng thái:** Planning Phase

---

## 📋 TỔNG QUAN

### Mục tiêu
Tạo Main Menu mới với các tính năng:
- Global search across all calculators
- Favorites system (star/bookmark calculators)
- Recently used tracking (last 10 used)
- Quick access cards for most popular tools
- Stats dashboard (total calculations, most used module)

---

## 🎨 THIẾT KẾ UI/UX

### Layout Structure

```
┌─────────────────────────────────────────────────────────┐
│  🏥 Clinical Assistant                    [Theme Toggle] │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  🔍 Search all calculators...                    │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ ⭐ Favorites │  │ 🕐 Recent    │  │ 📊 Stats     │  │
│  │   (5)        │  │   (10)       │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                          │
│  📊 Quick Access - Most Popular Tools                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│  │ ASCVD    │ │ CHA2DS2  │ │ SOFA     │ │ GCS      │    │
│  │ Risk     │ │ -VASc    │ │ Score    │ │ Score    │    │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘    │
│                                                          │
│  📚 Browse by Category                                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│  │ ❤️ Tim  │ │ 🚨 Cấp   │ │ 🧠 Thần  │ │ 💊 Thuốc │    │
│  │  Mạch   │ │  Cứu     │ │  Kinh    │ │          │    │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Components Structure

```
components/
├── main_menu/
│   ├── __init__.py
│   ├── search_bar.py          # Global search component
│   ├── favorites.py            # Favorites system
│   ├── recently_used.py        # Recently used tracking
│   ├── quick_access.py         # Quick access cards
│   ├── stats_dashboard.py      # Stats dashboard
│   └── category_browser.py     # Category browser
```

---

## 🔍 1. SEARCH BAR

### Features
- Global search across all calculators
- Autocomplete với suggestions
- Real-time search results
- Filter by category
- Keyboard shortcuts (Ctrl+K / Cmd+K)

### Implementation
- Component: `components/main_menu/search_bar.py`
- Storage: Session state cho search history
- Search algorithm: Fuzzy matching với priority scoring

### Data Structure
```python
{
    "query": str,
    "results": [
        {
            "id": str,
            "name": str,
            "category": str,
            "icon": str,
            "page": str,
            "relevance_score": float
        }
    ],
    "history": [str]  # Last 10 searches
}
```

---

## ⭐ 2. FAVORITES SYSTEM

### Features
- Star/bookmark calculators
- Favorites view với quick access
- Add/remove from favorites
- Sync across sessions (localStorage)

### Implementation
- Component: `components/main_menu/favorites.py`
- Storage: `localStorage` (browser) hoặc `session_state` (Streamlit)
- UI: Star icon toggle, favorites list

### Data Structure
```python
{
    "favorites": [
        {
            "id": str,
            "name": str,
            "category": str,
            "icon": str,
            "page": str,
            "added_date": datetime
        }
    ]
}
```

---

## 🕐 3. RECENTLY USED

### Features
- Auto-track last 10 used calculators
- Quick access từ main menu
- Clear history option
- Timestamp tracking

### Implementation
- Component: `components/main_menu/recently_used.py`
- Storage: `session_state` + `localStorage` (persistent)
- Tracking: Hook vào calculator navigation

### Data Structure
```python
{
    "recently_used": [
        {
            "id": str,
            "name": str,
            "category": str,
            "icon": str,
            "page": str,
            "last_used": datetime,
            "use_count": int
        }
    ]
}
```

---

## 📊 4. QUICK ACCESS CARDS

### Features
- Most popular tools (top 8-12)
- Based on usage statistics
- Visual cards với icons
- One-click access

### Implementation
- Component: `components/main_menu/quick_access.py`
- Data source: Usage statistics từ `localStorage` hoặc analytics
- Fallback: Default popular calculators nếu chưa có stats

### Data Structure
```python
{
    "quick_access": [
        {
            "id": str,
            "name": str,
            "category": str,
            "icon": str,
            "page": str,
            "usage_count": int,
            "last_used": datetime
        }
    ]
}
```

---

## 📈 5. STATS DASHBOARD

### Features
- Total calculations done
- Most used module/category
- Most used calculator
- Usage trends (optional)

### Implementation
- Component: `components/main_menu/stats_dashboard.py`
- Data source: Usage tracking từ `localStorage`
- Display: Cards với metrics

### Data Structure
```python
{
    "stats": {
        "total_calculations": int,
        "most_used_category": str,
        "most_used_calculator": {
            "id": str,
            "name": str,
            "count": int
        },
        "calculations_by_category": {
            "category": int
        },
        "calculations_by_date": [
            {
                "date": str,
                "count": int
            }
        ]
    }
}
```

---

## 📚 6. CATEGORY BROWSER

### Features
- Browse calculators by category
- Visual category cards
- Category icons
- Quick navigation

### Implementation
- Component: `components/main_menu/category_browser.py`
- Data source: `config/calculators.py` - categories
- Display: Grid layout với category cards

### Categories
- ❤️ Tim Mạch (Cardiology)
- 🚨 Cấp cứu (Emergency)
- 🧠 Thần Kinh (Neurology)
- 💊 Thuốc (Drugs)
- 🔬 Labs (Laboratory)
- 📋 Protocols
- Và các categories khác...

---

## 💾 DATA STORAGE

### Storage Strategy

1. **Session State (Streamlit)**
   - Search history (current session)
   - Recently used (current session)
   - Temporary UI state

2. **LocalStorage (Browser)**
   - Favorites (persistent)
   - Recently used (persistent)
   - Usage statistics
   - Quick access preferences

### Storage Keys
```python
STORAGE_KEYS = {
    "favorites": "medical_app_favorites",
    "recently_used": "medical_app_recently_used",
    "usage_stats": "medical_app_usage_stats",
    "quick_access": "medical_app_quick_access",
    "search_history": "medical_app_search_history"
}
```

---

## 🔄 USAGE TRACKING

### Tracking Points
1. Calculator opened → Track in recently_used
2. Calculator used → Increment usage_count
3. Category accessed → Track category usage
4. Search performed → Track search query

### Implementation
- Hook vào navigation functions
- Update localStorage on each action
- Aggregate statistics periodically

---

## 📱 RESPONSIVE DESIGN

### Mobile
- Stacked layout
- Collapsible sections
- Touch-friendly buttons
- Swipe gestures (optional)

### Desktop
- Multi-column layout
- Hover effects
- Keyboard shortcuts
- Larger cards

---

## 🎯 IMPLEMENTATION PHASES

### Phase 2.1: Planning ✅ (Current)
- Design document
- Component structure
- Data structures

### Phase 2.2: Search Bar
- Implement search component
- Autocomplete functionality
- Search algorithm

### Phase 2.3: Favorites System
- Favorites storage
- Star/bookmark UI
- Favorites view

### Phase 2.4: Recently Used & Quick Access
- Recently used tracking
- Quick access cards
- Stats dashboard
- Category browser

---

## 📝 NOTES

- Sử dụng Streamlit session_state cho temporary data
- Sử dụng JavaScript + localStorage cho persistent data
- Cần tạo utility functions cho storage operations
- Cần integrate với existing navigation system

---

**Cập nhật lần cuối:** 2026-01-XX  
**Phiên bản:** 1.0  
**Trạng thái:** Planning Complete - Ready for Implementation
