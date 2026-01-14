"""
Related Content Components
Show related topics, diseases, and medications
"""

import streamlit as st
from typing import List, Optional
from patient_education.models import PatientEducationTopic
from patient_education.data import get_all_topics


def find_related_topics(
    current_topic: PatientEducationTopic,
    all_topics: List[PatientEducationTopic],
    max_results: int = 3
) -> List[PatientEducationTopic]:
    """
    Find related topics based on category and content similarity
    
    Args:
        current_topic: Current topic
        all_topics: All available topics
        max_results: Maximum number of results
        
    Returns:
        List of related topics
    """
    related = []
    
    # Same category
    same_category = [
        t for t in all_topics
        if t.category == current_topic.category
        and t.id != current_topic.id
    ]
    
    # Related disease
    if current_topic.related_disease:
        related_by_disease = [
            t for t in all_topics
            if (t.related_disease == current_topic.related_disease
                or (current_topic.related_disease in t.content.lower()
                    and t.id != current_topic.id))
        ]
        related.extend(related_by_disease)
    
    # Related drugs
    if current_topic.related_drugs:
        for drug in current_topic.related_drugs:
            related_by_drug = [
                t for t in all_topics
                if drug in t.related_drugs
                and t.id != current_topic.id
                and t not in related
            ]
            related.extend(related_by_drug)
    
    # Add same category if not enough
    if len(related) < max_results:
        for topic in same_category:
            if topic not in related:
                related.append(topic)
            if len(related) >= max_results:
                break
    
    return related[:max_results]


def render_related_topics(
    current_topic: PatientEducationTopic,
    all_topics: Optional[List[PatientEducationTopic]] = None,
    max_results: int = 3
):
    """
    Render related topics section
    
    Args:
        current_topic: Current topic
        all_topics: All topics (if None, will fetch)
        max_results: Maximum related topics to show
    """
    if all_topics is None:
        all_topics = get_all_topics()
    
    related = find_related_topics(current_topic, all_topics, max_results)
    
    if not related:
        return
    
    st.markdown("---")
    st.markdown("### 🔗 Tài liệu liên quan")
    st.caption("Bạn có thể quan tâm đến các tài liệu sau:")
    
    # Render as compact cards
    from components.patient_education.cards import render_topic_card
    
    cols = st.columns(min(len(related), 3))
    for i, topic in enumerate(related):
        with cols[i % len(cols)]:
            render_topic_card(
                topic,
                show_preview=True,
                compact=True
            )


def render_related_resources(topic: PatientEducationTopic):
    """
    Render related diseases and medications links
    
    Args:
        topic: PatientEducationTopic object
    """
    has_related = False
    
    if topic.related_disease:
        has_related = True
        st.markdown(f"""
        **🫀 Bệnh lý liên quan:** {topic.related_disease}
        
        💡 Xem thêm trong [Bách khoa Bệnh lý](?page=16_📖_Disease_Encyclopedia)
        """)
    
    if topic.related_drugs:
        has_related = True
        drugs_list = ', '.join(topic.related_drugs)
        st.markdown(f"""
        **💊 Thuốc liên quan:** {drugs_list}
        
        💡 Xem thêm trong [Cơ sở dữ liệu thuốc](?page=07_💊_Drug_Database)
        """)
    
    if has_related:
        st.markdown("---")
