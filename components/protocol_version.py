"""
Protocol Version History Component
Display version information and update history
"""

import streamlit as st
import html
from typing import Dict, Optional
from datetime import datetime


# Protocol version information
PROTOCOL_VERSIONS = {
    "Sepsis 1-Hour Bundle": {
        "version": "2.0",
        "last_updated": "2024-01-15",
        "guideline": "Surviving Sepsis Campaign 2021",
        "guideline_year": 2021,
        "changelog": [
            "Updated: 1-hour bundle from 3-hour bundle",
            "Added: Lactate monitoring requirements",
            "Updated: Antibiotic selection guidelines"
        ]
    },
    "Sepsis 3-Hour Bundle": {
        "version": "1.5",
        "last_updated": "2024-01-10",
        "guideline": "Surviving Sepsis Campaign 2021",
        "guideline_year": 2021,
        "changelog": [
            "Maintained: 3-hour bundle for reference",
            "Note: 1-hour bundle is now standard"
        ]
    },
    "Stroke Management": {
        "version": "3.2",
        "last_updated": "2024-02-01",
        "guideline": "AHA/ASA Guidelines 2023",
        "guideline_year": 2023,
        "changelog": [
            "Updated: Door-to-needle time targets",
            "Added: Extended window for thrombectomy",
            "Updated: Imaging recommendations"
        ]
    },
    "DKA Protocol": {
        "version": "2.1",
        "last_updated": "2024-01-20",
        "guideline": "ADA Clinical Practice Recommendations 2024",
        "guideline_year": 2024,
        "changelog": [
            "Updated: Insulin dosing protocol",
            "Added: Bicarbonate use criteria",
            "Updated: Monitoring frequency"
        ]
    },
    "ACS": {
        "version": "4.0",
        "last_updated": "2024-01-25",
        "guideline": "ACC/AHA Guidelines 2023",
        "guideline_year": 2023,
        "changelog": [
            "Major update: New risk stratification",
            "Updated: Antiplatelet recommendations",
            "Added: New anticoagulation options"
        ]
    },
    "ARDS Management": {
        "version": "3.1",
        "last_updated": "2024-01-18",
        "guideline": "ARDS Definition Task Force 2023",
        "guideline_year": 2023,
        "changelog": [
            "Updated: Ventilator settings",
            "Added: Prone positioning criteria",
            "Updated: ECMO indications"
        ]
    }
}


def get_protocol_version(protocol_name: str) -> Optional[Dict]:
    """
    Get version information for a protocol.
    
    Args:
        protocol_name: Name of the protocol
        
    Returns:
        Version dict or None if not found
    """
    # Try exact match
    if protocol_name in PROTOCOL_VERSIONS:
        return PROTOCOL_VERSIONS[protocol_name]
    
    # Try partial match
    clean_name = protocol_name.split(' ', 1)[-1] if ' ' in protocol_name else protocol_name
    
    for key, version_info in PROTOCOL_VERSIONS.items():
        if key.lower() in clean_name.lower() or clean_name.lower() in key.lower():
            return version_info
    
    # Default version info
    return {
        "version": "1.0",
        "last_updated": "2024-01-01",
        "guideline": "Standard Protocol",
        "guideline_year": 2024,
        "changelog": []
    }


def render_version_badge(protocol_name: str):
    """
    Render version badge at top of protocol.
    
    Args:
        protocol_name: Name of the protocol
    """
    version_info = get_protocol_version(protocol_name)
    
    if not version_info:
        return
    
    version = version_info.get("version", "1.0")
    last_updated = version_info.get("last_updated", "")
    guideline = version_info.get("guideline", "")
    guideline_year = version_info.get("guideline_year", "")
    
    # Format date
    try:
        date_obj = datetime.strptime(last_updated, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%d/%m/%Y")
    except:
        formatted_date = last_updated
    
    html = f"""
    <div style="
        background: linear-gradient(135deg, #E7F3FF 0%, #ffffff 100%);
        border-left: 4px solid #0066CC;
        padding: 0.75rem 1rem;
        border-radius: 4px;
        margin-bottom: 1rem;
    ">
        <div style="display: flex; align-items: center; gap: 1rem; flex-wrap: wrap;">
            <span style="
                background: #0066CC;
                color: white;
                padding: 0.25rem 0.75rem;
                border-radius: 12px;
                font-size: 0.875rem;
                font-weight: 600;
            ">v{html.escape(str(version))}</span>
            <span style="color: #6C757D; font-size: 0.875rem;">
                📅 Cập nhật: <strong>{html.escape(formatted_date)}</strong>
            </span>
            <span style="color: #6C757D; font-size: 0.875rem;">
                📚 {html.escape(guideline)} {html.escape(str(guideline_year))}
            </span>
        </div>
    </div>
    """
    
    st.markdown(html, unsafe_allow_html=True)


def render_version_history(protocol_name: str):
    """
    Render version history section.
    
    Args:
        protocol_name: Name of the protocol
    """
    version_info = get_protocol_version(protocol_name)
    
    if not version_info:
        return
    
    with st.expander("📋 Lịch Sử Phiên Bản", expanded=False):
        version = version_info.get("version", "1.0")
        last_updated = version_info.get("last_updated", "")
        guideline = version_info.get("guideline", "")
        guideline_year = version_info.get("guideline_year", "")
        changelog = version_info.get("changelog", [])
        
        # Current version info
        st.markdown(f"**Phiên bản hiện tại:** v{version}")
        
        try:
            date_obj = datetime.strptime(last_updated, "%Y-%m-%d")
            formatted_date = date_obj.strftime("%d/%m/%Y")
        except:
            formatted_date = last_updated
        
        st.markdown(f"**Cập nhật lần cuối:** {formatted_date}")
        st.markdown(f"**Căn cứ:** {guideline} {guideline_year}")
        
        if changelog:
            st.markdown("---")
            st.markdown("**Thay đổi:**")
            for change in changelog:
                st.markdown(f"- {change}")
        else:
            st.info("💡 Chưa có thông tin thay đổi chi tiết.")
        
        # Update notification
        st.markdown("---")
        st.caption("💡 Protocol được cập nhật định kỳ theo guidelines mới nhất. Vui lòng kiểm tra thường xuyên.")


def render_evidence_level(level: str, source: str, year: int):
    """
    Render evidence level indicator.
    
    Args:
        level: Evidence level (A, B, C)
        source: Source organization
        year: Publication year
    """
    level_colors = {
        "A": ("#28A745", "Mạnh"),
        "B": ("#FFC107", "Trung bình"),
        "C": ("#DC3545", "Yếu")
    }
    
    color, label = level_colors.get(level, ("#6C757D", "Không xác định"))
    
    html = f"""
    <div style="
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: {color}20;
        border: 1px solid {color};
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.5rem 0;
    ">
        <span style="
            background: {color};
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 50%;
            font-weight: 700;
            font-size: 0.875rem;
        ">{level}</span>
        <span style="font-size: 0.875rem; color: {color};">
            <strong>Mức độ bằng chứng {label}</strong> - {source} {year}
        </span>
    </div>
    """
    
    st.markdown(html, unsafe_allow_html=True)

