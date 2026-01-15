"""
Disease-Specific Ventilator Mode Settings
Cài đặt máy thở cụ thể cho từng loại bệnh
"""

import streamlit as st
from components.ui.results import render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert
from typing import Dict, Optional


# Disease-specific ventilator settings
DISEASE_SETTINGS = {
    "ARDS": {
        "mode": "AC hoặc VC",
        "vt": "6 mL/kg IBW",
        "rr": "12-20 /min",
        "peep": "8-12 cmH2O (theo PEEP/FiO2 table)",
        "fio2": "100% → giảm dần",
        "ie_ratio": "1:2",
        "targets": {
            "plateau": "≤30 cmH2O",
            "driving_pressure": "≤15 cmH2O",
            "pf_ratio": ">200",
            "ph": "7.30-7.45"
        },
        "notes": "Lung-protective ventilation. Tuân thủ ARDSNet protocol.",
        "priority": "critical"
    },
    "COPD": {
        "mode": "AC hoặc PSV",
        "vt": "6-8 mL/kg IBW",
        "rr": "10-14 /min",
        "peep": "5-8 cmH2O (cẩn thận auto-PEEP)",
        "fio2": "Đủ để SpO2 >88%",
        "ie_ratio": "1:3 hoặc 1:4",
        "targets": {
            "plateau": "≤30 cmH2O",
            "paco2": "Cho phép tăng (permissive hypercapnia)",
            "ph": "≥7.20",
            "auto_peep": "Tránh"
        },
        "notes": "Cho phép hypercapnia nhẹ. Tránh auto-PEEP. I:E ratio dài hơn.",
        "priority": "high"
    },
    "Asthma": {
        "mode": "AC",
        "vt": "6-8 mL/kg IBW",
        "rr": "10-14 /min",
        "peep": "5 cmH2O (tránh auto-PEEP)",
        "fio2": "Đủ để SpO2 >90%",
        "ie_ratio": "1:3 hoặc 1:4",
        "targets": {
            "plateau": "≤30 cmH2O",
            "paco2": "Cho phép tăng (permissive hypercapnia)",
            "ph": "≥7.15",
            "auto_peep": "Tránh tuyệt đối"
        },
        "notes": "Tránh hyperinflation. Cho phép hypercapnia. I:E ratio dài.",
        "priority": "high"
    },
    "Post-operative": {
        "mode": "AC hoặc SIMV",
        "vt": "8-10 mL/kg IBW",
        "rr": "12-16 /min",
        "peep": "5-8 cmH2O",
        "fio2": "40-60%",
        "ie_ratio": "1:2",
        "targets": {
            "plateau": "≤30 cmH2O",
            "spO2": ">95%",
            "ph": "7.35-7.45"
        },
        "notes": "Cai máy thở sớm nếu có thể. Thường ngắn hạn.",
        "priority": "medium"
    },
    "Sepsis/Shock": {
        "mode": "AC",
        "vt": "6-8 mL/kg IBW",
        "rr": "16-20 /min",
        "peep": "8-10 cmH2O",
        "fio2": "Đủ để SpO2 >94%",
        "ie_ratio": "1:2",
        "targets": {
            "plateau": "≤30 cmH2O",
            "spO2": ">94%",
            "ph": "≥7.30",
            "map": "≥65 mmHg"
        },
        "notes": "Hỗ trợ huyết động. Tránh barotrauma. Theo dõi lactate.",
        "priority": "critical"
    },
    "Trauma": {
        "mode": "AC",
        "vt": "6-8 mL/kg IBW",
        "rr": "14-18 /min",
        "peep": "8-10 cmH2O",
        "fio2": "Đủ để SpO2 >94%",
        "ie_ratio": "1:2",
        "targets": {
            "plateau": "≤30 cmH2O",
            "spO2": ">94%",
            "ph": "≥7.30",
            "icp": "Nếu có chấn thương sọ não"
        },
        "notes": "Cân nhắc chấn thương sọ não (ICP). Tránh tăng ICP.",
        "priority": "high"
    },
    "Neuromuscular": {
        "mode": "AC hoặc SIMV",
        "vt": "8-10 mL/kg IBW",
        "rr": "12-16 /min",
        "peep": "5-8 cmH2O",
        "fio2": "21-40%",
        "ie_ratio": "1:2",
        "targets": {
            "plateau": "≤30 cmH2O",
            "spO2": ">95%",
            "ph": "7.35-7.45"
        },
        "notes": "Phổi thường bình thường. Hỗ trợ thông khí đơn giản.",
        "priority": "medium"
    },
    "Cardiac Failure": {
        "mode": "AC hoặc PSV",
        "vt": "6-8 mL/kg IBW",
        "rr": "12-16 /min",
        "peep": "5-8 cmH2O (cẩn thận với suy tim)",
        "fio2": "Đủ để SpO2 >94%",
        "ie_ratio": "1:2",
        "targets": {
            "plateau": "≤30 cmH2O",
            "spO2": ">94%",
            "ph": "≥7.30",
            "cvp": "Theo dõi"
        },
        "notes": "PEEP có thể ảnh hưởng tiền tải. Theo dõi huyết động sát.",
        "priority": "high"
    },
    "Pneumonia": {
        "mode": "AC",
        "vt": "6-8 mL/kg IBW",
        "rr": "14-18 /min",
        "peep": "8-10 cmH2O",
        "fio2": "Đủ để SpO2 >94%",
        "ie_ratio": "1:2",
        "targets": {
            "plateau": "≤30 cmH2O",
            "pf_ratio": ">200",
            "spO2": ">94%",
            "ph": "≥7.30"
        },
        "notes": "Có thể tiến triển thành ARDS. Theo dõi sát.",
        "priority": "high"
    },
    "Acute Heart Failure": {
        "mode": "AC hoặc PSV",
        "vt": "6-8 mL/kg IBW",
        "rr": "14-18 /min",
        "peep": "5-8 cmH2O",
        "fio2": "Đủ để SpO2 >94%",
        "ie_ratio": "1:2",
        "targets": {
            "plateau": "≤30 cmH2O",
            "spO2": ">94%",
            "ph": "≥7.30",
            "cvp": "Theo dõi"
        },
        "notes": "PEEP thấp hơn. Hỗ trợ huyết động.",
        "priority": "high"
    }
}


def get_disease_settings(disease: str, ibw_kg: float, height_cm: float = None) -> Optional[Dict]:
    """Get ventilator settings for specific disease"""
    if disease not in DISEASE_SETTINGS:
        return None
    
    settings = DISEASE_SETTINGS[disease].copy()
    
    # Calculate actual values if IBW provided
    if ibw_kg > 0:
        # Parse VT range
        vt_str = settings["vt"]
        if "6-8" in vt_str:
            vt_ml = ibw_kg * 7  # Average
        elif "6" in vt_str:
            vt_ml = ibw_kg * 6
        elif "8-10" in vt_str:
            vt_ml = ibw_kg * 9  # Average
        else:
            vt_ml = ibw_kg * 7  # Default
        
        settings["vt_ml"] = round(vt_ml, 1)
        settings["vt_liters"] = round(vt_ml / 1000, 3)
    
    return settings


def render_disease_specific_ventilator():
    """Render disease-specific ventilator settings calculator"""
    st.header("🫁 Cài đặt máy thở theo bệnh")
    st.caption("Hướng dẫn cài đặt máy thở cụ thể cho từng loại bệnh")
    
    st.markdown("---")
    
    # Patient information
    st.markdown("### 📋 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sex = st.radio("Giới tính:", ["Nam", "Nữ"], key="disease_sex", horizontal=True)
        height = st.number_input("Chiều cao (cm):", min_value=0.0, value=170.0, key="disease_height")
    
    with col2:
        weight = st.number_input("Cân nặng (kg):", min_value=0.0, value=70.0, key="disease_weight")
        age = st.number_input("Tuổi:", min_value=0, max_value=150, value=50, key="disease_age")
    
    # Calculate IBW
    from critical_care.ventilator import calculate_ibw
    ibw = calculate_ibw(sex, height)
    
    if ibw > 0:
        st.info(f"**IBW:** {ibw:.1f} kg")
    
    st.markdown("---")
    
    # Disease selection
    st.markdown("### 🦠 Chọn bệnh")
    
    diseases = list(DISEASE_SETTINGS.keys())
    disease = st.selectbox(
        "Bệnh:",
        diseases,
        key="disease_select",
        help="Chọn bệnh để xem cài đặt máy thở phù hợp"
    )
    
    if disease:
        settings = get_disease_settings(disease, ibw)
        
        if settings:
            st.markdown("---")
            st.markdown(f"### 📊 Cài đặt máy thở cho {disease}")
            
            # Priority indicator
            priority_colors = {
                "critical": "error",
                "high": "warning",
                "medium": "info"
            }
            
            priority_icons = {
                "critical": "🚨",
                "high": "⚠️",
                "medium": "ℹ️"
            }
            
            st.markdown(f"{priority_icons.get(settings['priority'], 'ℹ️')} **Mức độ ưu tiên:** {settings['priority'].upper()}")
            
            # Settings display
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### ⚙️ Thông số cài đặt")
                st.markdown(f"**Mode:** {settings['mode']}")
                st.markdown(f"**Tidal Volume:** {settings['vt']}")
                if 'vt_ml' in settings:
                    st.caption(f"→ {settings['vt_ml']:.1f} mL ({settings['vt_liters']:.3f} L)")
                st.markdown(f"**Respiratory Rate:** {settings['rr']}")
                st.markdown(f"**PEEP:** {settings['peep']}")
                st.markdown(f"**FiO2:** {settings['fio2']}")
                st.markdown(f"**I:E Ratio:** {settings['ie_ratio']}")
            
            with col2:
                st.markdown("#### 🎯 Mục tiêu")
                for target, value in settings['targets'].items():
                    st.markdown(f"**{target.replace('_', ' ').title()}:** {value}")
            
            # Notes
            st.markdown("---")
            st.markdown("### 💡 Ghi chú")
            render_info_alert(settings['notes'])
            
            # Quick actions
            st.markdown("---")
            st.markdown("### ⚡ Hành động nhanh")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("🫁 Mở Ventilator Calculator", use_container_width=True):
                    st.session_state['critical_care_tool_selection'] = "🫁 Ventilator Management"
                    st.rerun()
            
            with col2:
                if st.button("📊 Mở ARDS Protocol", use_container_width=True):
                    st.session_state['critical_care_tool_selection'] = "🫁 ARDS Protocols"
                    st.rerun()
            
            with col3:
                if st.button("🔄 Tính toán chi tiết", use_container_width=True):
                    st.session_state['ventilator_tool_to_open'] = 'initial'
                    st.session_state['critical_care_tool_selection'] = "🫁 Ventilator Management"
                    st.rerun()
            
            # Comparison table
            st.markdown("---")
            st.markdown("### 📋 So sánh với các bệnh khác")
            
            compare_diseases = st.multiselect(
                "Chọn bệnh để so sánh:",
                [d for d in diseases if d != disease],
                key="compare_diseases"
            )
            
            if compare_diseases:
                import pandas as pd
                
                comparison_data = []
                comparison_data.append({
                    "Bệnh": disease,
                    "Mode": settings['mode'],
                    "Vt": settings['vt'],
                    "RR": settings['rr'],
                    "PEEP": settings['peep'],
                    "FiO2": settings['fio2']
                })
                
                for comp_disease in compare_diseases:
                    comp_settings = DISEASE_SETTINGS[comp_disease]
                    comparison_data.append({
                        "Bệnh": comp_disease,
                        "Mode": comp_settings['mode'],
                        "Vt": comp_settings['vt'],
                        "RR": comp_settings['rr'],
                        "PEEP": comp_settings['peep'],
                        "FiO2": comp_settings['fio2']
                    })
                
                df = pd.DataFrame(comparison_data)
                st.dataframe(df, use_container_width=True, hide_index=True)


def get_all_disease_settings() -> Dict:
    """Get all disease settings"""
    return DISEASE_SETTINGS
