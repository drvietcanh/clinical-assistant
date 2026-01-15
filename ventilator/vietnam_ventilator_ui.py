"""
Vietnamese Ventilator UI Simulation
Giao diện mô phỏng các máy thở phổ biến tại Việt Nam
"""

import streamlit as st
from components.ui.results import render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert
from typing import Dict, Optional
import time


# Popular ventilators in Vietnam
VIETNAM_VENTILATORS = {
    "VFS-410 (Vingroup)": {
        "type": "Invasive",
        "technology": "Turbine",
        "modes": ["AC", "VC", "SIMV", "PSV"],
        "features": [
            "Turbine technology",
            "Auto-adjust synchronization",
            "Oxygen level monitoring",
            "PEEP monitoring",
            "Patient breathing measurement"
        ],
        "notes": "Made in Vietnam. Dựa trên thiết kế MIT. Không có CPAP mode.",
        "ui_layout": "simple"
    },
    "VFS-510 (Vingroup)": {
        "type": "Invasive/Non-invasive",
        "technology": "Medtronic PB560 based",
        "modes": ["AC", "VC", "SIMV", "PSV", "CPAP", "BiPAP"],
        "features": [
            "6 flexible breathing modes",
            "Adult và pediatric",
            "Invasive và non-invasive",
            "Compact, lightweight, portable"
        ],
        "notes": "Made in Vietnam. Dựa trên Medtronic PB560. Tương đương PB560.",
        "ui_layout": "standard"
    },
    "Mindray SV300": {
        "type": "ICU/Intermediate Care",
        "technology": "Turbine",
        "modes": ["AC", "VC", "SIMV", "PSV", "CPAP", "BiPAP", "APRV", "PRVC"],
        "features": [
            "Volumetric CO₂ measurement",
            "Weaning indicators",
            "O₂ Therapy",
            "Intelli Cycle",
            "Neonate, pediatric, adult"
        ],
        "notes": "Phổ biến tại các bệnh viện lớn. Giao diện đơn giản.",
        "ui_layout": "modern"
    },
    "Mindray SV800/SV600": {
        "type": "High-end ICU",
        "technology": "Advanced",
        "modes": ["AC", "VC", "SIMV", "PSV", "CPAP", "BiPAP", "APRV", "PRVC", "AMV", "CPRV"],
        "features": [
            "1080P HD wide screen",
            "PulmoSight™",
            "Adaptive Minute Ventilation (AMV)",
            "IntelliCycle Pro",
            "CPRV mode",
            "User configurable UI"
        ],
        "notes": "Máy thở cao cấp. Có nhiều tính năng thông minh.",
        "ui_layout": "advanced"
    },
    "Medtronic PB560": {
        "type": "ICU",
        "technology": "Standard",
        "modes": ["AC", "VC", "SIMV", "PSV", "CPAP"],
        "features": [
            "FDA approved",
            "Standard ICU modes",
            "Reliable performance"
        ],
        "notes": "Máy thở chuẩn. Đã quen thuộc với bác sĩ Việt Nam.",
        "ui_layout": "standard"
    }
}


def render_ventilator_ui_simulation(ventilator_model: str):
    """Render ventilator UI simulation"""
    if ventilator_model not in VIETNAM_VENTILATORS:
        st.error(f"Máy thở {ventilator_model} không có trong database")
        return
    
    vent_info = VIETNAM_VENTILATORS[ventilator_model]
    
    st.header(f"🫁 Mô phỏng máy thở: {ventilator_model}")
    st.caption(f"Giao diện mô phỏng {ventilator_model}")
    
    st.markdown("---")
    
    # Ventilator info
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"**Loại:** {vent_info['type']}")
    with col2:
        st.markdown(f"**Công nghệ:** {vent_info['technology']}")
    with col3:
        st.markdown(f"**Layout:** {vent_info['ui_layout']}")
    
    st.markdown("---")
    
    # Simulated ventilator display
    st.markdown("### 📺 Màn hình máy thở (Mô phỏng)")
    
    # Create simulated display based on layout
    if vent_info['ui_layout'] == 'simple':
        render_simple_ventilator_ui(ventilator_model)
    elif vent_info['ui_layout'] == 'standard':
        render_standard_ventilator_ui(ventilator_model)
    elif vent_info['ui_layout'] == 'modern':
        render_modern_ventilator_ui(ventilator_model)
    else:  # advanced
        render_advanced_ventilator_ui(ventilator_model)
    
    st.markdown("---")
    
    # Available modes
    st.markdown("### 🔧 Chế độ có sẵn")
    
    modes = vent_info['modes']
    cols = st.columns(len(modes))
    
    for idx, mode in enumerate(modes):
        with cols[idx]:
            st.markdown(f"**{mode}**")
    
    st.markdown("---")
    
    # Features
    st.markdown("### ⭐ Tính năng")
    
    for feature in vent_info['features']:
        st.markdown(f"- {feature}")
    
    st.markdown("---")
    
    # Notes
    render_info_alert(vent_info['notes'])


def render_simple_ventilator_ui(ventilator_model: str):
    """Render simple ventilator UI (VFS-410 style)"""
    st.markdown("""
    <div style="background: #1e1e1e; color: #00ff00; padding: 20px; border-radius: 8px; font-family: monospace;">
        <div style="text-align: center; font-size: 18px; margin-bottom: 15px;">
            <strong>{}</strong>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <div>Mode: <span style="color: #ffff00;">AC</span></div>
            <div>Vt: <span style="color: #ffff00;">420</span> mL</div>
            <div>RR: <span style="color: #ffff00;">20</span> /min</div>
            <div>PEEP: <span style="color: #ffff00;">10</span> cmH2O</div>
            <div>FiO2: <span style="color: #ffff00;">60</span>%</div>
            <div>Plateau: <span style="color: #00ff00;">25</span> cmH2O</div>
        </div>
    </div>
    """.format(ventilator_model), unsafe_allow_html=True)


def render_standard_ventilator_ui(ventilator_model: str):
    """Render standard ventilator UI (VFS-510, PB560 style)"""
    st.markdown("""
    <div style="background: #2d2d2d; color: #ffffff; padding: 20px; border-radius: 8px; font-family: Arial;">
        <div style="text-align: center; font-size: 20px; margin-bottom: 20px; border-bottom: 2px solid #4a9eff;">
            <strong>{}</strong>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 15px;">
            <div style="background: #3d3d3d; padding: 10px; border-radius: 5px;">
                <div style="font-size: 12px; color: #aaa;">MODE</div>
                <div style="font-size: 24px; color: #4a9eff;">AC</div>
            </div>
            <div style="background: #3d3d3d; padding: 10px; border-radius: 5px;">
                <div style="font-size: 12px; color: #aaa;">Vt</div>
                <div style="font-size: 24px; color: #4a9eff;">420 mL</div>
            </div>
            <div style="background: #3d3d3d; padding: 10px; border-radius: 5px;">
                <div style="font-size: 12px; color: #aaa;">RR</div>
                <div style="font-size: 24px; color: #4a9eff;">20 /min</div>
            </div>
            <div style="background: #3d3d3d; padding: 10px; border-radius: 5px;">
                <div style="font-size: 12px; color: #aaa;">PEEP</div>
                <div style="font-size: 24px; color: #4a9eff;">10 cmH2O</div>
            </div>
            <div style="background: #3d3d3d; padding: 10px; border-radius: 5px;">
                <div style="font-size: 12px; color: #aaa;">FiO2</div>
                <div style="font-size: 24px; color: #4a9eff;">60%</div>
            </div>
            <div style="background: #3d3d3d; padding: 10px; border-radius: 5px;">
                <div style="font-size: 12px; color: #aaa;">Plateau</div>
                <div style="font-size: 24px; color: #00ff00;">25 cmH2O</div>
            </div>
        </div>
    </div>
    """.format(ventilator_model), unsafe_allow_html=True)


def render_modern_ventilator_ui(ventilator_model: str):
    """Render modern ventilator UI (SV300 style)"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 25px; border-radius: 10px;">
        <div style="text-align: center; font-size: 22px; margin-bottom: 25px; font-weight: bold;">
            {}
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px;">
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; opacity: 0.8;">MODE</div>
                <div style="font-size: 28px; font-weight: bold;">AC</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; opacity: 0.8;">Vt</div>
                <div style="font-size: 28px; font-weight: bold;">420 mL</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; opacity: 0.8;">RR</div>
                <div style="font-size: 28px; font-weight: bold;">20</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; opacity: 0.8;">PEEP</div>
                <div style="font-size: 28px; font-weight: bold;">10</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; opacity: 0.8;">FiO2</div>
                <div style="font-size: 28px; font-weight: bold;">60%</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; opacity: 0.8;">Plateau</div>
                <div style="font-size: 28px; font-weight: bold; color: #90EE90;">25</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; opacity: 0.8;">Compliance</div>
                <div style="font-size: 28px; font-weight: bold;">30</div>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px; text-align: center;">
                <div style="font-size: 11px; opacity: 0.8;">CO2</div>
                <div style="font-size: 28px; font-weight: bold;">45</div>
            </div>
        </div>
    </div>
    """.format(ventilator_model), unsafe_allow_html=True)


def render_advanced_ventilator_ui(ventilator_model: str):
    """Render advanced ventilator UI (SV800/SV600 style)"""
    st.markdown("""
    <div style="background: #0a0a0a; color: #e0e0e0; padding: 30px; border-radius: 12px; border: 2px solid #4a9eff;">
        <div style="text-align: center; font-size: 24px; margin-bottom: 30px; color: #4a9eff; font-weight: bold;">
            {} - HD Display
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
            <div style="background: #1a1a1a; padding: 20px; border-radius: 8px; border-left: 4px solid #4a9eff;">
                <div style="font-size: 10px; color: #888; text-transform: uppercase;">Mode</div>
                <div style="font-size: 32px; color: #4a9eff; font-weight: bold; margin: 10px 0;">AC</div>
                <div style="font-size: 12px; color: #666;">Volume Control</div>
            </div>
            <div style="background: #1a1a1a; padding: 20px; border-radius: 8px; border-left: 4px solid #00ff88;">
                <div style="font-size: 10px; color: #888; text-transform: uppercase;">Tidal Volume</div>
                <div style="font-size: 32px; color: #00ff88; font-weight: bold; margin: 10px 0;">420</div>
                <div style="font-size: 12px; color: #666;">mL</div>
            </div>
            <div style="background: #1a1a1a; padding: 20px; border-radius: 8px; border-left: 4px solid #ffaa00;">
                <div style="font-size: 10px; color: #888; text-transform: uppercase;">Respiratory Rate</div>
                <div style="font-size: 32px; color: #ffaa00; font-weight: bold; margin: 10px 0;">20</div>
                <div style="font-size: 12px; color: #666;">/min</div>
            </div>
            <div style="background: #1a1a1a; padding: 20px; border-radius: 8px; border-left: 4px solid #ff6b6b;">
                <div style="font-size: 10px; color: #888; text-transform: uppercase;">PEEP</div>
                <div style="font-size: 32px; color: #ff6b6b; font-weight: bold; margin: 10px 0;">10</div>
                <div style="font-size: 12px; color: #666;">cmH2O</div>
            </div>
            <div style="background: #1a1a1a; padding: 20px; border-radius: 8px; border-left: 4px solid #9b59b6;">
                <div style="font-size: 10px; color: #888; text-transform: uppercase;">FiO2</div>
                <div style="font-size: 32px; color: #9b59b6; font-weight: bold; margin: 10px 0;">60</div>
                <div style="font-size: 12px; color: #666;">%</div>
            </div>
            <div style="background: #1a1a1a; padding: 20px; border-radius: 8px; border-left: 4px solid #00ff88;">
                <div style="font-size: 10px; color: #888; text-transform: uppercase;">Plateau Pressure</div>
                <div style="font-size: 32px; color: #00ff88; font-weight: bold; margin: 10px 0;">25</div>
                <div style="font-size: 12px; color: #666;">cmH2O</div>
            </div>
            <div style="background: #1a1a1a; padding: 20px; border-radius: 8px; border-left: 4px solid #3498db;">
                <div style="font-size: 10px; color: #888; text-transform: uppercase;">Compliance</div>
                <div style="font-size: 32px; color: #3498db; font-weight: bold; margin: 10px 0;">30</div>
                <div style="font-size: 12px; color: #666;">mL/cmH2O</div>
            </div>
            <div style="background: #1a1a1a; padding: 20px; border-radius: 8px; border-left: 4px solid #e74c3c;">
                <div style="font-size: 10px; color: #888; text-transform: uppercase;">Driving Pressure</div>
                <div style="font-size: 32px; color: #e74c3c; font-weight: bold; margin: 10px 0;">15</div>
                <div style="font-size: 12px; color: #666;">cmH2O</div>
            </div>
        </div>
        <div style="margin-top: 20px; padding: 15px; background: #1a1a1a; border-radius: 8px;">
            <div style="font-size: 12px; color: #888;">PulmoSight™ Active | AMV: ON | IntelliCycle: ON</div>
        </div>
    </div>
    """.format(ventilator_model), unsafe_allow_html=True)


def render_vietnam_ventilator_selector():
    """Render ventilator selector and UI simulation"""
    st.header("🫁 Máy thở phổ biến tại Việt Nam")
    st.caption("Giao diện mô phỏng và thông tin các máy thở phổ biến")
    
    st.markdown("---")
    
    # Ventilator selection
    ventilator_models = list(VIETNAM_VENTILATORS.keys())
    selected_vent = st.selectbox(
        "Chọn máy thở:",
        ventilator_models,
        key="vent_selector",
        help="Chọn máy thở để xem giao diện mô phỏng"
    )
    
    if selected_vent:
        render_ventilator_ui_simulation(selected_vent)
        
        # Comparison
        st.markdown("---")
        st.markdown("### 📊 So sánh với các máy thở khác")
        
        compare_vents = st.multiselect(
            "Chọn máy thở để so sánh:",
            [v for v in ventilator_models if v != selected_vent],
            key="compare_vents"
        )
        
        if compare_vents:
            import pandas as pd
            
            comparison_data = []
            selected_info = VIETNAM_VENTILATORS[selected_vent]
            comparison_data.append({
                "Máy thở": selected_vent,
                "Loại": selected_info['type'],
                "Công nghệ": selected_info['technology'],
                "Số chế độ": len(selected_info['modes']),
                "Layout": selected_info['ui_layout']
            })
            
            for comp_vent in compare_vents:
                comp_info = VIETNAM_VENTILATORS[comp_vent]
                comparison_data.append({
                    "Máy thở": comp_vent,
                    "Loại": comp_info['type'],
                    "Công nghệ": comp_info['technology'],
                    "Số chế độ": len(comp_info['modes']),
                    "Layout": comp_info['ui_layout']
                })
            
            df = pd.DataFrame(comparison_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
