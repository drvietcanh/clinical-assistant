"""
Real-time Ventilator Monitoring and Auto-adjustment
Theo dõi và điều chỉnh tự động theo các chỉ số thời gian thực
"""

import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import time
from components.ui.results import render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert
from typing import Dict, List, Optional
import numpy as np


# Alert thresholds
ALERT_THRESHOLDS = {
    "plateau_pressure": {
        "critical": 35,
        "warning": 30,
        "normal": 30
    },
    "driving_pressure": {
        "critical": 18,
        "warning": 15,
        "normal": 15
    },
    "pf_ratio": {
        "critical": 100,
        "warning": 200,
        "normal": 300
    },
    "ph": {
        "critical_low": 7.20,
        "warning_low": 7.30,
        "warning_high": 7.50,
        "critical_high": 7.60
    },
    "paco2": {
        "critical_high": 60,
        "warning_high": 50,
        "warning_low": 30,
        "critical_low": 25
    },
    "compliance": {
        "critical_low": 20,
        "warning_low": 30,
        "normal": 50
    }
}


def check_parameter_alerts(parameter: str, value: float) -> Dict:
    """Check if parameter value triggers alerts"""
    if parameter not in ALERT_THRESHOLDS:
        return {"level": None, "message": None}
    
    thresholds = ALERT_THRESHOLDS[parameter]
    
    if parameter == "plateau_pressure":
        if value > thresholds["critical"]:
            return {"level": "critical", "message": f"Plateau pressure rất cao ({value:.1f} cmH2O) - Nguy cơ barotrauma"}
        elif value > thresholds["warning"]:
            return {"level": "warning", "message": f"Plateau pressure cao ({value:.1f} cmH2O) - Cần theo dõi"}
        else:
            return {"level": "normal", "message": None}
    
    elif parameter == "driving_pressure":
        if value > thresholds["critical"]:
            return {"level": "critical", "message": f"Driving pressure rất cao ({value:.1f} cmH2O) - Cần giảm Vt"}
        elif value > thresholds["warning"]:
            return {"level": "warning", "message": f"Driving pressure cao ({value:.1f} cmH2O)"}
        else:
            return {"level": "normal", "message": None}
    
    elif parameter == "pf_ratio":
        if value < thresholds["critical"]:
            return {"level": "critical", "message": f"P/F ratio rất thấp ({value:.0f}) - ARDS nặng"}
        elif value < thresholds["warning"]:
            return {"level": "warning", "message": f"P/F ratio thấp ({value:.0f}) - ARDS trung bình"}
        else:
            return {"level": "normal", "message": None}
    
    elif parameter == "ph":
        if value < thresholds["critical_low"]:
            return {"level": "critical", "message": f"pH rất thấp ({value:.2f}) - Nhiễm toan nặng"}
        elif value < thresholds["warning_low"]:
            return {"level": "warning", "message": f"pH thấp ({value:.2f}) - Nhiễm toan"}
        elif value > thresholds["critical_high"]:
            return {"level": "critical", "message": f"pH rất cao ({value:.2f}) - Nhiễm kiềm nặng"}
        elif value > thresholds["warning_high"]:
            return {"level": "warning", "message": f"pH cao ({value:.2f}) - Nhiễm kiềm"}
        else:
            return {"level": "normal", "message": None}
    
    elif parameter == "paco2":
        if value > thresholds["critical_high"]:
            return {"level": "critical", "message": f"PaCO2 rất cao ({value:.0f} mmHg) - Tăng CO2 nặng"}
        elif value > thresholds["warning_high"]:
            return {"level": "warning", "message": f"PaCO2 cao ({value:.0f} mmHg)"}
        elif value < thresholds["critical_low"]:
            return {"level": "critical", "message": f"PaCO2 rất thấp ({value:.0f} mmHg) - Giảm CO2 nặng"}
        elif value < thresholds["warning_low"]:
            return {"level": "warning", "message": f"PaCO2 thấp ({value:.0f} mmHg)"}
        else:
            return {"level": "normal", "message": None}
    
    elif parameter == "compliance":
        if value < thresholds["critical_low"]:
            return {"level": "critical", "message": f"Compliance rất thấp ({value:.1f} mL/cmH2O) - Phổi cứng"}
        elif value < thresholds["warning_low"]:
            return {"level": "warning", "message": f"Compliance thấp ({value:.1f} mL/cmH2O)"}
        else:
            return {"level": "normal", "message": None}
    
    return {"level": None, "message": None}


def recommend_adjustments(current_params: Dict, alerts: List[Dict]) -> List[Dict]:
    """Recommend ventilator adjustments based on alerts"""
    recommendations = []
    
    for alert in alerts:
        param = alert.get("parameter")
        level = alert.get("level")
        
        if level in ["critical", "warning"]:
            if param == "plateau_pressure":
                recommendations.append({
                    "parameter": "Tidal Volume",
                    "action": "Giảm",
                    "current": current_params.get("vt_ml", "N/A"),
                    "recommended": f"{current_params.get('vt_ml', 420) * 0.9:.0f} mL",
                    "reason": "Giảm Vt để giảm plateau pressure"
                })
                recommendations.append({
                    "parameter": "PEEP",
                    "action": "Cân nhắc giảm",
                    "current": current_params.get("peep", "N/A"),
                    "recommended": f"{max(current_params.get('peep', 10) - 2, 5):.0f} cmH2O",
                    "reason": "Giảm PEEP nếu có thể"
                })
            
            elif param == "driving_pressure":
                recommendations.append({
                    "parameter": "Tidal Volume",
                    "action": "Giảm",
                    "current": current_params.get("vt_ml", "N/A"),
                    "recommended": f"{current_params.get('vt_ml', 420) * 0.85:.0f} mL",
                    "reason": "Giảm Vt để giảm driving pressure"
                })
                recommendations.append({
                    "parameter": "PEEP",
                    "action": "Cân nhắc tăng",
                    "current": current_params.get("peep", "N/A"),
                    "recommended": f"{min(current_params.get('peep', 10) + 2, 20):.0f} cmH2O",
                    "reason": "Tăng PEEP có thể giúp giảm driving pressure"
                })
            
            elif param == "pf_ratio":
                recommendations.append({
                    "parameter": "PEEP",
                    "action": "Tăng",
                    "current": current_params.get("peep", "N/A"),
                    "recommended": f"{min(current_params.get('peep', 10) + 2, 20):.0f} cmH2O",
                    "reason": "Tăng PEEP để cải thiện oxygenation"
                })
                recommendations.append({
                    "parameter": "FiO2",
                    "action": "Tăng",
                    "current": current_params.get("fio2", "N/A"),
                    "recommended": f"{min(current_params.get('fio2', 0.6) + 0.1, 1.0):.1f}",
                    "reason": "Tăng FiO2 để cải thiện PaO2"
                })
            
            elif param == "ph" and alert.get("value", 7.4) < 7.30:
                recommendations.append({
                    "parameter": "Respiratory Rate",
                    "action": "Tăng",
                    "current": current_params.get("rr", "N/A"),
                    "recommended": f"{current_params.get('rr', 20) + 2:.0f} /min",
                    "reason": "Tăng RR để giảm PaCO2 và cải thiện pH"
                })
            
            elif param == "paco2" and alert.get("value", 40) > 50:
                recommendations.append({
                    "parameter": "Respiratory Rate",
                    "action": "Tăng",
                    "current": current_params.get("rr", "N/A"),
                    "recommended": f"{min(current_params.get('rr', 20) + 2, 30):.0f} /min",
                    "reason": "Tăng RR để giảm PaCO2"
                })
                recommendations.append({
                    "parameter": "Tidal Volume",
                    "action": "Cân nhắc tăng",
                    "current": current_params.get("vt_ml", "N/A"),
                    "recommended": f"{min(current_params.get('vt_ml', 420) * 1.1, 600):.0f} mL",
                    "reason": "Tăng Vt nếu plateau pressure cho phép"
                })
    
    return recommendations


def init_realtime_state():
    """Initialize real-time monitoring state"""
    if 'realtime_ventilator_data' not in st.session_state:
        st.session_state['realtime_ventilator_data'] = []
    
    if 'realtime_monitoring_active' not in st.session_state:
        st.session_state['realtime_monitoring_active'] = False
    
    if 'realtime_last_update' not in st.session_state:
        st.session_state['realtime_last_update'] = None


def add_realtime_entry(timestamp: datetime, params: Dict):
    """Add real-time monitoring entry"""
    init_realtime_state()
    
    entry = {
        'timestamp': timestamp,
        **params
    }
    
    st.session_state['realtime_ventilator_data'].append(entry)
    
    # Keep only last 100 entries
    if len(st.session_state['realtime_ventilator_data']) > 100:
        st.session_state['realtime_ventilator_data'] = st.session_state['realtime_ventilator_data'][-100:]
    
    st.session_state['realtime_last_update'] = timestamp


def get_realtime_dataframe() -> pd.DataFrame:
    """Get real-time data as DataFrame"""
    init_realtime_state()
    
    if not st.session_state['realtime_ventilator_data']:
        return pd.DataFrame()
    
    return pd.DataFrame(st.session_state['realtime_ventilator_data'])


def render_realtime_monitoring():
    """Render real-time monitoring interface"""
    st.header("📊 Theo dõi thời gian thực")
    st.caption("Theo dõi và điều chỉnh tự động các thông số máy thở")
    
    init_realtime_state()
    
    st.markdown("---")
    
    # Control panel
    st.markdown("### 🎛️ Bảng điều khiển")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        monitoring_active = st.checkbox(
            "Bật theo dõi real-time",
            value=st.session_state['realtime_monitoring_active'],
            key="realtime_active"
        )
        st.session_state['realtime_monitoring_active'] = monitoring_active
    
    with col2:
        auto_adjust = st.checkbox(
            "Tự động đề xuất điều chỉnh",
            value=True,
            key="auto_adjust"
        )
    
    with col3:
        update_interval = st.selectbox(
            "Tần suất cập nhật:",
            ["Mỗi 5 giây", "Mỗi 10 giây", "Mỗi 30 giây", "Mỗi 1 phút"],
            key="update_interval"
        )
    
    st.markdown("---")
    
    # Current parameters input
    st.markdown("### 📝 Nhập thông số hiện tại")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        vt_ml = st.number_input("Vt (mL):", min_value=0.0, value=420.0, key="realtime_vt")
        rr = st.number_input("RR (/min):", min_value=0.0, value=20.0, key="realtime_rr")
    
    with col2:
        peep = st.number_input("PEEP (cmH2O):", min_value=0.0, value=10.0, key="realtime_peep")
        fio2 = st.slider("FiO2:", 0.21, 1.0, 0.6, 0.01, key="realtime_fio2")
    
    with col3:
        plateau = st.number_input("Plateau (cmH2O):", min_value=0.0, value=25.0, key="realtime_plateau")
        compliance = st.number_input("Compliance (mL/cmH2O):", min_value=0.0, value=30.0, key="realtime_compliance")
    
    with col4:
        pao2 = st.number_input("PaO2 (mmHg):", min_value=0.0, value=60.0, key="realtime_pao2")
        paco2 = st.number_input("PaCO2 (mmHg):", min_value=0.0, value=45.0, key="realtime_paco2")
        ph = st.number_input("pH:", min_value=6.5, max_value=7.8, value=7.35, step=0.01, key="realtime_ph")
    
    # Calculate derived parameters
    driving_pressure = plateau - peep if plateau and peep else None
    pf_ratio = pao2 / fio2 if pao2 and fio2 > 0 else None
    
    # Save current parameters
    current_params = {
        "vt_ml": vt_ml,
        "rr": rr,
        "peep": peep,
        "fio2": fio2,
        "plateau": plateau,
        "compliance": compliance,
        "pao2": pao2,
        "paco2": paco2,
        "ph": ph,
        "driving_pressure": driving_pressure,
        "pf_ratio": pf_ratio
    }
    
    # Check alerts
    alerts = []
    
    if plateau:
        alert = check_parameter_alerts("plateau_pressure", plateau)
        if alert["level"]:
            alerts.append({"parameter": "plateau_pressure", "level": alert["level"], "message": alert["message"], "value": plateau})
    
    if driving_pressure:
        alert = check_parameter_alerts("driving_pressure", driving_pressure)
        if alert["level"]:
            alerts.append({"parameter": "driving_pressure", "level": alert["level"], "message": alert["message"], "value": driving_pressure})
    
    if pf_ratio:
        alert = check_parameter_alerts("pf_ratio", pf_ratio)
        if alert["level"]:
            alerts.append({"parameter": "pf_ratio", "level": alert["level"], "message": alert["message"], "value": pf_ratio})
    
    if ph:
        alert = check_parameter_alerts("ph", ph)
        if alert["level"]:
            alerts.append({"parameter": "ph", "level": alert["level"], "message": alert["message"], "value": ph})
    
    if paco2:
        alert = check_parameter_alerts("paco2", paco2)
        if alert["level"]:
            alerts.append({"parameter": "paco2", "level": alert["level"], "message": alert["message"], "value": paco2})
    
    if compliance:
        alert = check_parameter_alerts("compliance", compliance)
        if alert["level"]:
            alerts.append({"parameter": "compliance", "level": alert["level"], "message": alert["message"], "value": compliance})
    
    # Display current status
    st.markdown("---")
    st.markdown("### 📊 Trạng thái hiện tại")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if plateau:
            plat_color = 'error' if plateau > 30 else ('warning' if plateau > 28 else 'success')
            render_result_card(
                title="Plateau",
                value=f"{plateau:.1f}",
                unit="cmH2O",
                color=plat_color,
                subtitle="Target: ≤30"
            )
    
    with col2:
        if driving_pressure:
            dp_color = 'error' if driving_pressure > 15 else ('warning' if driving_pressure > 12 else 'success')
            render_result_card(
                title="Driving P",
                value=f"{driving_pressure:.1f}",
                unit="cmH2O",
                color=dp_color,
                subtitle="Target: ≤15"
            )
    
    with col3:
        if pf_ratio:
            pf_color = 'error' if pf_ratio < 100 else ('warning' if pf_ratio < 200 else 'success')
            render_result_card(
                title="P/F Ratio",
                value=f"{pf_ratio:.0f}",
                unit="",
                color=pf_color,
                subtitle="Target: >200"
            )
    
    with col4:
        if compliance:
            comp_color = 'error' if compliance < 20 else ('warning' if compliance < 30 else 'success')
            render_result_card(
                title="Compliance",
                value=f"{compliance:.1f}",
                unit="mL/cmH2O",
                color=comp_color,
                subtitle="Target: >30"
            )
    
    # Display alerts
    if alerts:
        st.markdown("---")
        st.markdown("### 🚨 Cảnh báo")
        
        critical_alerts = [a for a in alerts if a["level"] == "critical"]
        warning_alerts = [a for a in alerts if a["level"] == "warning"]
        
        if critical_alerts:
            for alert in critical_alerts:
                render_error_alert(alert["message"], "")
        
        if warning_alerts:
            for alert in warning_alerts:
                render_warning_alert(alert["message"], "")
        
        # Recommendations
        if auto_adjust:
            recommendations = recommend_adjustments(current_params, alerts)
            
            if recommendations:
                st.markdown("---")
                st.markdown("### 💡 Đề xuất điều chỉnh")
                
                import pandas as pd
                rec_df = pd.DataFrame(recommendations)
                st.dataframe(rec_df, use_container_width=True, hide_index=True)
    else:
        st.success("✅ Tất cả thông số trong giới hạn an toàn")
    
    # Save entry button
    st.markdown("---")
    if st.button("💾 Lưu thông số hiện tại", use_container_width=True):
        add_realtime_entry(datetime.now(), current_params)
        st.success("✅ Đã lưu!")
        st.rerun()
    
    # Display trends
    df = get_realtime_dataframe()
    
    if not df.empty and len(df) > 1:
        st.markdown("---")
        st.markdown("### 📈 Xu hướng")
        
        # Select parameters to plot
        plot_params = st.multiselect(
            "Chọn thông số để vẽ biểu đồ:",
            ["plateau", "driving_pressure", "pf_ratio", "compliance", "ph", "paco2"],
            default=["plateau", "driving_pressure", "pf_ratio"],
            key="plot_params"
        )
        
        if plot_params:
            plot_df = df[['timestamp'] + plot_params].copy()
            plot_df = plot_df.set_index('timestamp')
            st.line_chart(plot_df)
        
        # Recent entries table
        st.markdown("### 📋 Lịch sử gần đây")
        display_df = df[['timestamp'] + [p for p in plot_params if p in df.columns]].copy()
        display_df = display_df.sort_values('timestamp', ascending=False).head(10)
        display_df['timestamp'] = display_df['timestamp'].dt.strftime('%H:%M:%S')
        st.dataframe(display_df, use_container_width=True, hide_index=True)
