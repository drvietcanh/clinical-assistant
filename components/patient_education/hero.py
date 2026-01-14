"""
Hero Section Component
Featured topics and hero banner
"""

import streamlit as st
from typing import List, Optional
from patient_education.models import PatientEducationTopic
from patient_education.data import get_all_topics


def get_featured_topics(
    all_topics: List[PatientEducationTopic],
    count: int = 3
) -> List[PatientEducationTopic]:
    """
    Get featured topics (can be based on popularity, recency, etc.)
    
    For now, returns first topics from common categories
    """
    # Get topics from common categories
    categories = ["Disease", "Cardiovascular", "Diabetes", "Respiratory"]
    featured = []
    
    for category in categories:
        category_topics = [t for t in all_topics if t.category == category]
        if category_topics:
            featured.append(category_topics[0])
        if len(featured) >= count:
            break
    
    # Fill remaining with any topics
    if len(featured) < count:
        remaining = [t for t in all_topics if t not in featured]
        featured.extend(remaining[:count - len(featured)])
    
    return featured[:count]


def render_hero_section(
    topics: Optional[List[PatientEducationTopic]] = None,
    show_featured: bool = True
):
    """
    Render hero section with title and featured topics
    
    Args:
        topics: List of topics (if None, will fetch)
        show_featured: Show featured topics carousel
    """
    if topics is None:
        topics = get_all_topics()
    
    # Hero banner
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 40px 20px;
        border-radius: 16px;
        margin-bottom: 30px;
        color: white;
        text-align: center;
    ">
        <h1 style="color: white; margin: 0 0 16px 0; font-size: 2.5rem;">
            👥 Giáo dục Bệnh nhân
        </h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin: 0;">
            Tài liệu giáo dục với ngôn ngữ đơn giản, dễ hiểu. 
            Giúp bệnh nhân hiểu rõ về bệnh tật, thuốc men và cách chăm sóc sức khỏe.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured topics
    if show_featured:
        featured = get_featured_topics(topics, count=3)
        
        if featured:
            st.markdown("### ⭐ Tài liệu nổi bật")
            st.caption("Các tài liệu được xem nhiều nhất")
            
            from .cards import render_topic_grid
            render_topic_grid(featured, columns=3, show_preview=True)
            
            st.markdown("---")
