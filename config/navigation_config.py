"""
Navigation Configuration
Reorganized navigation structure with categories and sub-modules
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class NavigationItem:
    """Single navigation item (page/module)"""
    id: str
    title: str
    icon: str
    page_path: str
    is_sub_item: bool = False
    parent_id: Optional[str] = None


@dataclass
class NavigationCategory:
    """Navigation category with sub-modules"""
    id: str
    title: str
    icon: str
    description: str
    module_ids: List[str]
    color: str
    border: str
    default_expanded: bool = False


# Navigation structure with 6 main categories (optimized)
# Organized by clinical workflow for easier access
# Reduced from 23+ top-level pages to 7 main pages + 11 sub-items
NAVIGATION_CATEGORIES = {
    "home_search": NavigationCategory(
        id="home_search",
        title="🏠 Trang chủ & Tìm kiếm",
        icon="🏠",
        description="Main menu and global search",
        module_ids=["main_menu"],
        color="linear-gradient(135deg, #f5f5f5 0%, #e0e0e0 100%)",
        border="#757575",
        default_expanded=True
    ),
    "drugs_dosing": NavigationCategory(
        id="drugs_dosing",
        title="💊 Thuốc & Liều dùng",
        icon="💊",
        description="Drug database with sub-modules: antibiotics, pill identifier, TDM",
        module_ids=["drug_database", "antibiotics", "pill_identifier", "tdm"],
        color="linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",
        border="#4caf50",
        default_expanded=True
    ),
    "calculators_scores": NavigationCategory(
        id="calculators_scores",
        title="📊 Tính toán & Thang điểm",
        icon="📊",
        description="Clinical scores, calculators, and lab tools",
        module_ids=["scores", "labs"],
        color="linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)",
        border="#1976d2",
        default_expanded=True
    ),
    "critical_care_protocols": NavigationCategory(
        id="critical_care_protocols",
        title="🫁 Hồi sức & Phác đồ",
        icon="🫁",
        description="Critical care with sub-modules: ventilator, protocols, guidelines, medical news",
        module_ids=["critical_care", "ventilator", "protocols", "guidelines_tracker", "medical_news"],
        color="linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",
        border="#ff6f00",
        default_expanded=False
    ),
    "diagnosis_reference": NavigationCategory(
        id="diagnosis_reference",
        title="🩺 Chẩn đoán & Tham khảo",
        icon="🩺",
        description="Differential diagnosis with sub-modules: disease encyclopedia, ICD-10, articles, patient education",
        module_ids=["diagnosis", "disease_encyclopedia", "icd10_lookup", "in_depth_articles", "patient_education"],
        color="linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%)",
        border="#f44336",
        default_expanded=False
    ),
    "support_tools": NavigationCategory(
        id="support_tools",
        title="🧭 Hỗ trợ & Công cụ",
        icon="🧭",
        description="Decision support with sub-modules: AI assistant, vaccination, settings, analytics",
        module_ids=["phase2_features", "ai_assistant", "vaccination", "settings", "analytics"],
        color="linear-gradient(135deg, #e1f5fe 0%, #b3e5fc 100%)",
        border="#0288d1",
        default_expanded=False
    ),
}

# Sub-item mappings (which items are sub-items of main items)
# Format: {sub_item_id: parent_item_id}
# Organized to reduce top-level menu items from 23+ to 7 main pages
NAVIGATION_SUB_ITEMS = {
    # Drugs & Dosing: 3 sub-items under drug_database
    "antibiotics": "drug_database",
    "pill_identifier": "drug_database",
    "tdm": "drug_database",
    
    # Critical Care & Protocols: 4 sub-items under critical_care
    "ventilator": "critical_care",
    "protocols": "critical_care",
    "guidelines_tracker": "critical_care",
    "medical_news": "critical_care",
    
    # Diagnosis & Reference: 4 sub-items under diagnosis
    "disease_encyclopedia": "diagnosis",
    "icd10_lookup": "diagnosis",
    "in_depth_articles": "diagnosis",
    "patient_education": "diagnosis",
    
    # Support & Tools: 4 sub-items under phase2_features
    "ai_assistant": "phase2_features",
    "vaccination": "phase2_features",
    "settings": "phase2_features",
    "analytics": "phase2_features",
}


def get_category_by_module_id(module_id: str) -> Optional[NavigationCategory]:
    """Get navigation category for a module ID"""
    for category in NAVIGATION_CATEGORIES.values():
        if module_id in category.module_ids:
            return category
    return None


def get_all_categories() -> Dict[str, NavigationCategory]:
    """Get all navigation categories"""
    return NAVIGATION_CATEGORIES


def get_modules_by_category(category_id: str) -> List[str]:
    """Get module IDs for a category"""
    category = NAVIGATION_CATEGORIES.get(category_id)
    if category:
        return category.module_ids
    return []


def get_category_info(category_id: str) -> Optional[NavigationCategory]:
    """Get category information"""
    return NAVIGATION_CATEGORIES.get(category_id)


def get_navigation_items_for_category(category_id: str) -> List[NavigationItem]:
    """
    Get navigation items for a category, including sub-items structure
    
    Returns:
        List of NavigationItem objects with sub-item relationships
    """
    category = NAVIGATION_CATEGORIES.get(category_id)
    if not category:
        return []
    
    items = []
    main_items = []
    sub_items = {}
    
    # Separate main items and sub-items
    for module_id in category.module_ids:
        if module_id in NAVIGATION_SUB_ITEMS:
            parent_id = NAVIGATION_SUB_ITEMS[module_id]
            if parent_id not in sub_items:
                sub_items[parent_id] = []
            sub_items[parent_id].append(module_id)
        else:
            main_items.append(module_id)
    
    # Get module info from app_config
    try:
        from config.app_config import get_module_info
    except ImportError:
        return []
    
    # Create main items
    for module_id in main_items:
        module_info = get_module_info(module_id)
        if module_info:
            items.append(NavigationItem(
                id=module_id,
                title=module_info.title,
                icon=module_info.icon,
                page_path=module_info.page_path,
                is_sub_item=False
            ))
            
            # Add sub-items if any
            if module_id in sub_items:
                for sub_id in sub_items[module_id]:
                    sub_info = get_module_info(sub_id)
                    if sub_info:
                        items.append(NavigationItem(
                            id=sub_id,
                            title=sub_info.title,
                            icon=sub_info.icon,
                            page_path=sub_info.page_path,
                            is_sub_item=True,
                            parent_id=module_id
                        ))
    
    return items


# Export
__all__ = [
    'NavigationCategory',
    'NavigationItem',
    'NAVIGATION_CATEGORIES',
    'NAVIGATION_SUB_ITEMS',
    'get_category_by_module_id',
    'get_all_categories',
    'get_modules_by_category',
    'get_category_info',
    'get_navigation_items_for_category',
]

