"""
Critical Care Quick Dashboard
Quick access to all critical care tools
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card


def render_critical_care_dashboard():
    """Render quick access dashboard for critical care tools"""
    
    st.markdown("## 🏠 Critical Care Dashboard")
    st.markdown("""
    Trang tổng quan - Truy cập nhanh tất cả công cụ hồi sức
    """)
    
    st.markdown("---")
    
    # Quick access cards
    st.markdown("### ⚡ Truy Cập Nhanh")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">💧</div>
            <div style="font-weight: bold; font-size: 1.1rem;">Fluid Therapy</div>
            <div style="font-size: 0.9rem; margin-top: 5px;">Dịch truyền & Điện giải</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 10px; color: white;">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">💉</div>
            <div style="font-weight: bold; font-size: 1.1rem;">Vasopressors</div>
            <div style="font-size: 0.9rem; margin-top: 5px;">Hướng dẫn liều</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); border-radius: 10px; color: white;">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">🩸</div>
            <div style="font-weight: bold; font-size: 1.1rem;">Transfusion</div>
            <div style="font-size: 0.9rem; margin-top: 5px;">Truyền máu</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); border-radius: 10px; color: white;">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">💤</div>
            <div style="font-weight: bold; font-size: 1.1rem;">Sedation</div>
            <div style="font-size: 0.9rem; margin-top: 5px;">An thần & Giảm đau</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Scoring systems
    st.markdown("### 📊 Scoring Systems")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="padding: 15px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #667eea;">
            <strong>📊 Đánh giá độ nặng:</strong><br>
            • APACHE II<br>
            • SOFA<br>
            • SAPS II
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="padding: 15px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #f5576c;">
            <strong>🧠 Đánh giá thần kinh:</strong><br>
            • GCS<br>
            • RASS<br>
            • CAM-ICU
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="padding: 15px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #4facfe;">
            <strong>🧪 Đánh giá thận:</strong><br>
            • AKI Staging (KDIGO)<br>
            • RIFLE
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Clinical scenarios quick links
    st.markdown("### 🎯 Tình Huống Lâm Sàng")
    
    scenarios = [
        {
            "title": "Sepsis",
            "icon": "🦠",
            "description": "Quản lý nhiễm trùng huyết",
            "tools": ["SOFA", "Fluid Therapy", "Vasopressors"]
        },
        {
            "title": "ARDS",
            "icon": "🫁",
            "description": "Hội chứng suy hô hấp cấp",
            "tools": ["Ventilator", "PEEP", "Sedation"]
        },
        {
            "title": "Shock",
            "icon": "💉",
            "description": "Sốc - Huyết động không ổn định",
            "tools": ["Fluid Therapy", "Vasopressors", "Transfusion"]
        },
        {
            "title": "Delirium",
            "icon": "🧠",
            "description": "Mê sảng ở ICU",
            "tools": ["CAM-ICU", "RASS", "Sedation"]
        }
    ]
    
    cols = st.columns(4)
    for idx, scenario in enumerate(scenarios):
        with cols[idx]:
            st.markdown(f"""
            <div style="padding: 15px; background: white; border-radius: 8px; border: 2px solid #e5e7eb; text-align: center;">
                <div style="font-size: 2rem; margin-bottom: 5px;">{scenario['icon']}</div>
                <div style="font-weight: bold; margin-bottom: 5px;">{scenario['title']}</div>
                <div style="font-size: 0.85rem; color: #6b7280;">{scenario['description']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recent calculations (placeholder)
    st.markdown("### 🕐 Tính toán gần đây")
    st.info("""
    **Tính năng đang phát triển:**
    - Lưu lịch sử tính toán
    - Truy cập nhanh các tính toán trước đó
    - Export kết quả
    """)
    
    st.markdown("---")
    
    # Quick tips
    st.markdown("### 💡 Mẹo sử dụng")
    
    tips = [
        "💧 **Fluid Therapy:** Sử dụng Holliday-Segar cho maintenance, tính deficit cho hypernatremia",
        "💉 **Vasopressors:** Bắt đầu với Norepinephrine, theo dõi MAP và lactate",
        "🩸 **Transfusion:** Tuân thủ MTP protocol, theo dõi hemoglobin và coagulation",
        "💤 **Sedation:** Mục tiêu RASS -1 to -2 cho hầu hết bệnh nhân, đánh giá hàng ngày",
        "📊 **Scoring:** SOFA hàng ngày cho sepsis, APACHE II cho tiên lượng ICU"
    ]
    
    for tip in tips:
        st.markdown(f"- {tip}")

