"""
Ventilator History Management - PHIÊN 5
Lưu trữ và quản lý lịch sử thông số máy thở
"""

import streamlit as st
from datetime import datetime
from typing import Dict, List, Optional, Any
import pandas as pd


def init_history_state():
    """Khởi tạo session state cho lịch sử"""
    if 'ventilator_history' not in st.session_state:
        st.session_state.ventilator_history = []


def save_ventilator_entry(
    vent_settings: Dict[str, Any],
    abg_data: Dict[str, Any],
    calculations: Dict[str, Any],
    patient_info: Optional[Dict[str, Any]] = None,
    notes: Optional[str] = None
) -> Dict[str, Any]:
    """
    Lưu một entry vào lịch sử
    
    Args:
        vent_settings: Thông số máy thở (mode, vt, rr, peep, fio2, plateau, peak)
        abg_data: Dữ liệu ABG (ph, po2, pco2, hco3, be, fio2)
        calculations: Kết quả tính toán (pf_ratio, driving_pressure, compliance, etc.)
        patient_info: Thông tin bệnh nhân (sex, height, pbw)
        notes: Ghi chú thêm
    
    Returns:
        Entry đã lưu
    """
    init_history_state()
    
    entry = {
        'timestamp': datetime.now(),
        'vent_settings': vent_settings.copy() if vent_settings else {},
        'abg_data': abg_data.copy() if abg_data else {},
        'calculations': calculations.copy() if calculations else {},
        'patient_info': patient_info.copy() if patient_info else {},
        'notes': notes or ''
    }
    
    st.session_state.ventilator_history.append(entry)
    
    # Giới hạn tối đa 100 entries để tránh quá tải
    if len(st.session_state.ventilator_history) > 100:
        st.session_state.ventilator_history = st.session_state.ventilator_history[-100:]
    
    return entry


def get_history() -> List[Dict[str, Any]]:
    """Lấy toàn bộ lịch sử"""
    init_history_state()
    return st.session_state.ventilator_history.copy()


def get_history_count() -> int:
    """Lấy số lượng entries trong lịch sử"""
    init_history_state()
    return len(st.session_state.ventilator_history)


def clear_history():
    """Xóa toàn bộ lịch sử"""
    init_history_state()
    st.session_state.ventilator_history = []


def delete_history_entry(index: int):
    """Xóa một entry cụ thể"""
    init_history_state()
    if 0 <= index < len(st.session_state.ventilator_history):
        st.session_state.ventilator_history.pop(index)


def get_history_dataframe() -> pd.DataFrame:
    """Chuyển lịch sử thành DataFrame để hiển thị"""
    history = get_history()
    
    if not history:
        return pd.DataFrame()
    
    rows = []
    for entry in history:
        row = {
            'Thời gian': entry['timestamp'].strftime('%H:%M:%S'),
            'Ngày': entry['timestamp'].strftime('%d/%m/%Y'),
            'Mode': entry['vent_settings'].get('mode', 'N/A'),
            'Vt (mL)': entry['vent_settings'].get('vt', 0),
            'RR': entry['vent_settings'].get('rr', 0),
            'PEEP': entry['vent_settings'].get('peep', 0),
            'FiO₂ (%)': entry['vent_settings'].get('fio2', 0),
            'Plateau': entry['vent_settings'].get('plateau', 0),
            'P/F Ratio': entry['calculations'].get('pf_ratio', None),
            'Driving P': entry['calculations'].get('driving_pressure', None),
            'Compliance': entry['calculations'].get('compliance', None),
            'Vt/kg': entry['calculations'].get('vt_per_kg', None),
            'PaO₂': entry['abg_data'].get('po2', None),
            'PaCO₂': entry['abg_data'].get('pco2', None),
            'pH': entry['abg_data'].get('ph', None),
        }
        rows.append(row)
    
    df = pd.DataFrame(rows)
    return df


def compare_entries(index1: int, index2: int) -> Dict[str, Any]:
    """
    So sánh 2 entries trong lịch sử
    
    Returns:
        Dict với các thay đổi giữa 2 entries
    """
    history = get_history()
    
    if not (0 <= index1 < len(history) and 0 <= index2 < len(history)):
        return {}
    
    entry1 = history[index1]
    entry2 = history[index2]
    
    comparison = {
        'time_diff': (entry2['timestamp'] - entry1['timestamp']).total_seconds() / 60,  # phút
        'vent_changes': {},
        'abg_changes': {},
        'calculation_changes': {}
    }
    
    # So sánh vent settings
    for key in entry1['vent_settings']:
        val1 = entry1['vent_settings'].get(key)
        val2 = entry2['vent_settings'].get(key)
        if val1 != val2:
            comparison['vent_changes'][key] = {
                'before': val1,
                'after': val2,
                'delta': val2 - val1 if isinstance(val1, (int, float)) and isinstance(val2, (int, float)) else None
            }
    
    # So sánh ABG
    for key in entry1['abg_data']:
        val1 = entry1['abg_data'].get(key)
        val2 = entry2['abg_data'].get(key)
        if val1 != val2:
            comparison['abg_changes'][key] = {
                'before': val1,
                'after': val2,
                'delta': val2 - val1 if isinstance(val1, (int, float)) and isinstance(val2, (int, float)) else None
            }
    
    # So sánh calculations
    for key in entry1['calculations']:
        val1 = entry1['calculations'].get(key)
        val2 = entry2['calculations'].get(key)
        if val1 != val2 and val1 is not None and val2 is not None:
            comparison['calculation_changes'][key] = {
                'before': val1,
                'after': val2,
                'delta': val2 - val1 if isinstance(val1, (int, float)) and isinstance(val2, (int, float)) else None
            }
    
    return comparison


def render_history_panel():
    """Hiển thị panel quản lý lịch sử"""
    init_history_state()
    
    st.markdown("### 📜 Lịch Sử Thông số")
    
    history = get_history()
    
    if not history:
        st.info("📝 Chưa có lịch sử. Tính toán và lưu để xem lịch sử.")
        return
    
    # Hiển thị số lượng entries
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.caption(f"Tổng cộng: **{len(history)}** entries")
    with col2:
        if st.button("🗑️ Xóa Tất Cả", use_container_width=True):
            clear_history()
            st.rerun()
    with col3:
        if st.button("🔄 Làm Mới", use_container_width=True):
            st.rerun()
    
    st.markdown("---")
    
    # Hiển thị bảng lịch sử
    df = get_history_dataframe()
    
    if not df.empty:
        # Format số liệu
        numeric_cols = ['Vt (mL)', 'RR', 'PEEP', 'FiO₂ (%)', 'Plateau', 
                       'P/F Ratio', 'Driving P', 'Compliance', 'Vt/kg',
                       'PaO₂', 'PaCO₂', 'pH']
        
        for col in numeric_cols:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: f"{x:.1f}" if isinstance(x, (int, float)) and pd.notna(x) else "N/A")
        
        # Hiển thị bảng với selection
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            height=400
        )
        
        # So sánh entries
        st.markdown("---")
        st.markdown("#### 🔄 So sánh Entries")
        
        col1, col2 = st.columns(2)
        with col1:
            entry1_idx = st.selectbox(
                "Entry 1 (Trước):",
                range(len(history)),
                format_func=lambda x: f"Entry {x+1} - {history[x]['timestamp'].strftime('%H:%M:%S %d/%m/%Y')}",
                key="compare_entry1"
            )
        with col2:
            default_idx = len(history) - 1 if len(history) > 0 else 0
            entry2_idx = st.selectbox(
                "Entry 2 (Sau):",
                range(len(history)),
                format_func=lambda x: f"Entry {x+1} - {history[x]['timestamp'].strftime('%H:%M:%S %d/%m/%Y')}",
                index=default_idx,
                key="compare_entry2"
            )
        
        if entry1_idx != entry2_idx:
            comparison = compare_entries(entry1_idx, entry2_idx)
            
            if comparison:
                st.markdown(f"**⏱️ Khoảng thời gian:** {comparison['time_diff']:.1f} phút")
                
                # Hiển thị thay đổi
                if comparison['vent_changes']:
                    st.markdown("**⚙️ Thay Đổi Thông số Máy Thở:**")
                    for key, change in comparison['vent_changes'].items():
                        delta = change.get('delta')
                        delta_str = f" ({delta:+.1f})" if delta is not None else ""
                        st.write(f"- **{key}:** {change['before']} → {change['after']}{delta_str}")
                
                if comparison['abg_changes']:
                    st.markdown("**💨 Thay Đổi ABG:**")
                    for key, change in comparison['abg_changes'].items():
                        delta = change.get('delta')
                        delta_str = f" ({delta:+.1f})" if delta is not None else ""
                        st.write(f"- **{key}:** {change['before']} → {change['after']}{delta_str}")
                
                if comparison['calculation_changes']:
                    st.markdown("**📊 Thay Đổi Tính toán:**")
                    for key, change in comparison['calculation_changes'].items():
                        delta = change.get('delta')
                        delta_str = f" ({delta:+.1f})" if delta is not None else ""
                        st.write(f"- **{key}:** {change['before']:.1f} → {change['after']:.1f}{delta_str}")
    else:
        st.info("Không có dữ liệu để hiển thị")

