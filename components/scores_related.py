"""
Scores Related Calculators Component
Shows related calculators based on specialty, category, or usage
"""

import streamlit as st
from typing import List, Dict, Optional
from scores.config import SCORES_BY_SPECIALTY


def get_related_calculators(
    current_specialty: str,
    current_score_id: str,
    limit: int = 5
) -> List[Dict]:
    """
    Get related calculators based on:
    1. Same specialty
    2. Similar keywords in name/description
    3. Daily use calculators
    
    Args:
        current_specialty: Current specialty
        current_score_id: Current score ID
        limit: Maximum related calculators to return
    
    Returns:
        List of related calculators
    """
    if current_specialty not in SCORES_BY_SPECIALTY:
        return []
    
    current_score_info = SCORES_BY_SPECIALTY[current_specialty].get(current_score_id)
    if not current_score_info:
        return []
    
    current_name = current_score_info.get("name", "").lower()
    current_desc = (current_score_info.get("desc", "") or "").lower()
    
    # Extract keywords from current calculator
    keywords = set()
    for word in current_name.split():
        if len(word) > 3:
            keywords.add(word)
    for word in current_desc.split():
        if len(word) > 3:
            keywords.add(word)
    
    related = []
    
    # 1. Same specialty (exclude current)
    for score_id, score_info in SCORES_BY_SPECIALTY[current_specialty].items():
        if score_id == current_score_id:
            continue
        
        relevance = 10  # Base relevance for same specialty
        
        # Check keyword matches
        name_lower = score_info.get("name", "").lower()
        desc_lower = (score_info.get("desc", "") or "").lower()
        
        for keyword in keywords:
            if keyword in name_lower:
                relevance += 5
            if keyword in desc_lower:
                relevance += 2
        
        # Daily use bonus
        if "DÙNG HÀNG NGÀY" in (score_info.get("desc", "") or ""):
            relevance += 3
        
        related.append({
            "specialty": current_specialty,
            "score_id": score_id,
            "score_info": score_info,
            "relevance": relevance,
            "reason": "Cùng chuyên khoa"
        })
    
    # 2. Other specialties with keyword matches
    for specialty, scores in SCORES_BY_SPECIALTY.items():
        if specialty == current_specialty:
            continue
        
        for score_id, score_info in scores.items():
            relevance = 0
            
            name_lower = score_info.get("name", "").lower()
            desc_lower = (score_info.get("desc", "") or "").lower()
            
            # Check keyword matches
            for keyword in keywords:
                if keyword in name_lower:
                    relevance += 3
                if keyword in desc_lower:
                    relevance += 1
            
            # Daily use bonus
            if "DÙNG HÀNG NGÀY" in (score_info.get("desc", "") or ""):
                relevance += 1
            
            if relevance > 0:
                related.append({
                    "specialty": specialty,
                    "score_id": score_id,
                    "score_info": score_info,
                    "relevance": relevance,
                    "reason": "Có từ khóa tương tự"
                })
    
    # Sort by relevance
    related.sort(key=lambda x: x["relevance"], reverse=True)
    
    return related[:limit]


def get_category_related(
    category_keywords: List[str],
    exclude_specialty: Optional[str] = None,
    exclude_score_id: Optional[str] = None,
    limit: int = 5
) -> List[Dict]:
    """
    Get calculators related by category/keywords.
    
    Args:
        category_keywords: List of keywords for category
        exclude_specialty: Specialty to exclude
        exclude_score_id: Score ID to exclude
        limit: Maximum results
    
    Returns:
        List of related calculators
    """
    related = []
    
    for specialty, scores in SCORES_BY_SPECIALTY.items():
        if specialty == exclude_specialty:
            continue
        
        for score_id, score_info in scores.items():
            if score_id == exclude_score_id:
                continue
            
            relevance = 0
            name_lower = score_info.get("name", "").lower()
            desc_lower = (score_info.get("desc", "") or "").lower()
            
            for keyword in category_keywords:
                keyword_lower = keyword.lower()
                if keyword_lower in name_lower:
                    relevance += 5
                if keyword_lower in desc_lower:
                    relevance += 2
            
            if relevance > 0:
                related.append({
                    "specialty": specialty,
                    "score_id": score_id,
                    "score_info": score_info,
                    "relevance": relevance,
                    "reason": f"Thuộc nhóm: {', '.join(category_keywords)}"
                })
    
    related.sort(key=lambda x: x["relevance"], reverse=True)
    return related[:limit]


def render_related_calculators(
    current_specialty: str,
    current_score_id: str,
    title: str = "📋 Calculators Liên Quan",
    max_display: int = 5
):
    """
    Render related calculators section.
    
    Args:
        current_specialty: Current specialty
        current_score_id: Current score ID
        title: Section title
        max_display: Maximum calculators to display
    """
    related = get_related_calculators(current_specialty, current_score_id, limit=max_display)
    
    if not related:
        return
    
    st.markdown("---")
    st.subheader(title)
    st.caption(f"Tìm thấy {len(related)} calculator liên quan")
    
    # Display as cards
    for idx, calc in enumerate(related):
        score_info = calc["score_info"]
        name = score_info.get("name", "")
        desc = score_info.get("desc", "") or ""
        status = score_info.get("status", "✅")
        is_daily_use = "DÙNG HÀNG NGÀY" in desc
        
        # Truncate description
        if len(desc) > 100:
            desc = desc[:97] + "..."
        
        col1, col2 = st.columns([4, 1])
        
        with col1:
            display_name = f"{status} {name}"
            if is_daily_use:
                display_name += " ⭐"
            st.markdown(f"**{display_name}**")
            st.caption(desc)
            st.caption(f"📍 {calc['specialty']} • {calc['reason']}")
        
        with col2:
            if st.button("📊 Mở", key=f"related_{calc['score_id']}_{idx}", use_container_width=True):
                st.session_state['navigate_to_specialty'] = calc['specialty']
                st.session_state['navigate_to_score'] = calc['score_id']
                st.rerun()
        
        if idx < len(related) - 1:
            st.markdown("---")


def render_category_suggestions(
    category_keywords: List[str],
    title: str = "📂 Calculators Nhóm Tương Tự",
    max_display: int = 5
):
    """
    Render calculators by category/keywords.
    
    Args:
        category_keywords: Keywords for category
        title: Section title
        max_display: Maximum calculators to display
    """
    related = get_category_related(category_keywords, limit=max_display)
    
    if not related:
        return
    
    st.markdown("---")
    st.subheader(title)
    
    for idx, calc in enumerate(related):
        score_info = calc["score_info"]
        name = score_info.get("name", "")
        desc = score_info.get("desc", "") or ""
        status = score_info.get("status", "✅")
        
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"**{status} {name}**")
            st.caption(f"📍 {calc['specialty']}")
        
        with col2:
            if st.button("📊 Mở", key=f"category_{calc['score_id']}_{idx}", use_container_width=True):
                st.session_state['navigate_to_specialty'] = calc['specialty']
                st.session_state['navigate_to_score'] = calc['score_id']
                st.rerun()
        
        if idx < len(related) - 1:
            st.markdown("---")

