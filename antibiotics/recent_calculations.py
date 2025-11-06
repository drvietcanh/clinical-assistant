"""
Recent Calculations Manager - Phase 4
Lưu và quản lý recent dosing calculations
"""

import streamlit as st
from datetime import datetime
from typing import Dict, List, Optional


def save_calculation(calculation_data: Dict):
    """
    Lưu calculation vào recent calculations list
    
    Args:
        calculation_data: Dict chứa thông tin calculation
            - antibiotic_name: str
            - patient_info: dict (weight, height, age, sex, crcl, egfr)
            - indication: str
            - result: dict (từ calculate_adjusted_dose)
            - timestamp: datetime (optional, sẽ tự tạo nếu không có)
            - calculation_type: str ("quick" hoặc "scenario")
    """
    if 'recent_calculations' not in st.session_state:
        st.session_state.recent_calculations = []
    
    # Add timestamp if not present
    if 'timestamp' not in calculation_data:
        calculation_data['timestamp'] = datetime.now()
    
    # Add unique ID
    calculation_data['id'] = f"calc_{len(st.session_state.recent_calculations)}_{datetime.now().timestamp()}"
    
    # Add to beginning
    st.session_state.recent_calculations.insert(0, calculation_data)
    
    # Keep only last 10
    st.session_state.recent_calculations = st.session_state.recent_calculations[:10]


def get_recent_calculations(limit: int = 10) -> List[Dict]:
    """Lấy danh sách recent calculations"""
    if 'recent_calculations' not in st.session_state:
        st.session_state.recent_calculations = []
    
    return st.session_state.recent_calculations[:limit]


def clear_recent_calculations():
    """Xóa tất cả recent calculations"""
    st.session_state.recent_calculations = []


def remove_calculation(calc_id: str):
    """Xóa một calculation cụ thể"""
    if 'recent_calculations' not in st.session_state:
        return
    
    st.session_state.recent_calculations = [
        calc for calc in st.session_state.recent_calculations
        if calc.get('id') != calc_id
    ]


def format_calculation_summary(calc: Dict) -> str:
    """
    Format calculation thành string ngắn gọn để hiển thị
    
    Returns:
        String summary như: "Ceftriaxone - 70kg, CrCl 60 - Chuẩn"
    """
    ab_name = calc.get('antibiotic_name', 'Unknown')
    patient = calc.get('patient_info', {})
    indication = calc.get('indication', 'standard')
    
    # Map indication
    indication_map = {
        "standard": "Chuẩn",
        "severe": "Nhiễm khuẩn nặng",
        "meningitis": "Viêm màng não"
    }
    indication_vn = indication_map.get(indication, indication)
    
    weight = patient.get('weight', '?')
    crcl = patient.get('crcl', '?')
    
    # Format CrCl
    if isinstance(crcl, (int, float)):
        crcl_str = f"{crcl:.0f}"
    else:
        crcl_str = str(crcl)
    
    return f"{ab_name} - {weight}kg, CrCl {crcl_str} - {indication_vn}"


def render_recent_calculations_sidebar():
    """
    Render recent calculations trong sidebar
    """
    recent = get_recent_calculations(limit=10)
    
    if not recent:
        st.sidebar.info("💡 Chưa có calculations nào. Tính liều để lưu vào đây!")
        return
    
    st.sidebar.markdown("### 🕐 Tính Liều Gần Đây")
    
    for i, calc in enumerate(recent):
        summary = format_calculation_summary(calc)
        timestamp = calc.get('timestamp', datetime.now())
        
        # Format timestamp
        if isinstance(timestamp, datetime):
            time_str = timestamp.strftime("%H:%M")
        else:
            time_str = "N/A"
        
        # Create button to load calculation
        if st.sidebar.button(
            f"📋 {summary[:40]}...",
            key=f"load_calc_{calc.get('id', i)}",
            use_container_width=True
        ):
            # Load calculation data
            st.session_state['load_calculation'] = calc
            st.rerun()
        
        st.sidebar.caption(f"⏰ {time_str}")
        
        if i < len(recent) - 1:
            st.sidebar.markdown("---")
    
    # Clear all button
    if st.sidebar.button("🗑️ Xóa tất cả", key="clear_all_calculations"):
        clear_recent_calculations()
        st.rerun()

