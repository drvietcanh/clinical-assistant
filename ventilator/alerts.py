"""
Ventilator Alerts System
Hệ thống cảnh báo thông minh
"""

import streamlit as st


def check_ventilator_alerts(vent_settings, abg_data, calculations, pbw):
    """Kiểm tra và tạo cảnh báo dựa trên tất cả thông số"""
    alerts = []
    
    # Get values
    plateau = vent_settings.get("plateau", 0)
    driving_pressure = calculations.get("driving_pressure", None)
    pf_ratio = calculations.get("pf_ratio", None)
    compliance = calculations.get("compliance", None)
    vt = vent_settings.get("vt", 0)
    vt_per_kg = calculations.get("vt_per_kg", None)
    peep = vent_settings.get("peep", 0)
    pco2 = abg_data.get("pco2", 0)
    ph = abg_data.get("ph", 7.40)
    
    # Critical alerts (cần can thiệp ngay)
    
    # Plateau pressure >30 cmH2O
    if plateau > 30:
        alerts.append({
            "level": "critical",
            "title": "Plateau Pressure Cao - Nguy Hiểm",
            "message": f"Plateau pressure ({plateau} cmH2O) > 30 cmH2O - Vượt ngưỡng an toàn",
            "action": "Giảm Vt ngay lập tức",
            "details": [
                f"Giảm Vt xuống {max(int(vt * 0.85), int(pbw * 6)):.0f} mL (nếu có thể)",
                "Theo dõi lại plateau pressure sau 15-30 phút",
                "Nếu vẫn cao, cân nhắc giảm Vt thêm hoặc tăng PEEP (nếu phù hợp)",
                "Kiểm tra compliance - có thể phổi cứng"
            ],
            "reference": "ARDSNet Protocol: Plateau ≤30 cmH2O"
        })
    
    # Driving pressure >15 cmH2O
    if driving_pressure and driving_pressure > 15:
        alerts.append({
            "level": "critical",
            "title": "Driving Pressure Cao - Nguy Hiểm",
            "message": f"Driving pressure ({driving_pressure:.1f} cmH2O) > 15 cmH2O",
            "action": "Giảm Vt hoặc tăng PEEP (nếu phù hợp)",
            "details": [
                f"Driving pressure = Plateau ({plateau}) - PEEP ({peep})",
                "Mục tiêu: ≤15 cmH2O",
                "Có thể giảm Vt hoặc tăng PEEP (nếu không làm tăng plateau)",
                "Theo dõi compliance và oxy hóa"
            ],
            "reference": "Amato et al. 2015: Driving pressure ≤15 cmH2O"
        })
    
    # Severe hypoxemia (P/F <100)
    if pf_ratio and pf_ratio < 100:
        alerts.append({
            "level": "critical",
            "title": "Thiếu Oxy Rất Nặng",
            "message": f"P/F ratio ({pf_ratio:.0f}) < 100 - ARDS rất nặng",
            "action": "Tăng PEEP và FiO₂ ngay lập tức",
            "details": [
                "Theo bảng PEEP/FiO2 ARDSNet",
                "Cân nhắc PEEP 18-24 cmH2O",
                "FiO₂ có thể cần 0.8-1.0",
                "Cân nhắc prone positioning nếu phù hợp",
                "Theo dõi huyết động khi tăng PEEP"
            ],
            "reference": "ARDSNet Protocol: P/F <100 = ARDS nặng"
        })
    
    # Severe acidosis
    if ph < 7.15:
        alerts.append({
            "level": "critical",
            "title": "Toan Máu Rất Nặng",
            "message": f"pH ({ph:.2f}) < 7.15 - Toan máu rất nặng",
            "action": "Tăng thông khí ngay lập tức",
            "details": [
                "Tăng RR lên 30-35 lần/phút",
                "Kiểm tra Vt có đủ không",
                "Cân nhắc tăng flow rate",
                "Theo dõi pH sau 15-30 phút",
                "Cân nhắc NaHCO₃ nếu cần (theo chỉ định)"
            ],
            "reference": "Permissive hypercapnia: pH ≥7.15"
        })
    
    # Warning alerts (cần theo dõi)
    
    # P/F ratio 100-200
    if pf_ratio and 100 <= pf_ratio < 200:
        alerts.append({
            "level": "warning",
            "title": "Thiếu Oxy Nặng",
            "message": f"P/F ratio ({pf_ratio:.0f}) 100-200 - ARDS trung bình",
            "action": "Tăng PEEP và/hoặc FiO₂",
            "details": [
                "Theo bảng PEEP/FiO2 ARDSNet",
                "Cân nhắc PEEP 14-18 cmH2O",
                "FiO₂ có thể cần 0.6-0.8",
                "Theo dõi oxy hóa và huyết động"
            ],
            "reference": "ARDSNet Protocol: P/F 100-200 = ARDS trung bình"
        })
    
    # Vt/kg >8 mL/kg
    if vt_per_kg and vt_per_kg > 8:
        alerts.append({
            "level": "warning",
            "title": "Vt/kg Cao - Không Lung-Protective",
            "message": f"Vt/kg ({vt_per_kg:.1f} mL/kg) > 8 mL/kg",
            "action": "Giảm Vt để lung-protective",
            "details": [
                f"Đề xuất: Giảm Vt xuống {int(pbw * 6)} mL (6 mL/kg PBW)",
                "Lung-protective: Vt ≤6-8 mL/kg PBW",
                "Theo dõi PaCO₂ và pH sau khi giảm",
                "Cho phép hypercapnia nhẹ nếu cần (pH ≥7.15)"
            ],
            "reference": "ARDSNet Protocol: Vt ≤6-8 mL/kg PBW"
        })
    
    # Compliance <30 mL/cmH2O
    if compliance and compliance < 30:
        alerts.append({
            "level": "warning",
            "title": "Compliance Thấp - Phổi Cứng",
            "message": f"Compliance ({compliance:.1f} mL/cmH2O) < 30 - Phổi cứng",
            "action": "Cân nhắc điều chỉnh PEEP và Vt",
            "details": [
                "Compliance thấp = phổi cứng, khó thông khí",
                "Có thể cần giảm Vt",
                "Cân nhắc tăng PEEP nếu phù hợp (recruitment)",
                "Theo dõi driving pressure",
                "Kiểm tra nguyên nhân (ARDS, xẹp phổi, etc.)"
            ],
            "reference": "Normal compliance: 30-50 mL/cmH2O"
        })
    
    # Hypercapnia moderate
    if 45 < pco2 <= 55:
        alerts.append({
            "level": "warning",
            "title": "Tăng CO₂ Máu",
            "message": f"PaCO₂ ({pco2:.1f} mmHg) > 45 mmHg",
            "action": "Tăng thông khí",
            "details": [
                "Tăng RR 2-4 lần/phút",
                "Kiểm tra Vt có đủ không",
                "Kiểm tra auto-PEEP",
                "Theo dõi pH"
            ],
            "reference": "Normal PaCO₂: 35-45 mmHg"
        })
    
    # Info alerts (thông tin)
    
    # P/F ratio 200-300
    if pf_ratio and 200 <= pf_ratio < 300:
        alerts.append({
            "level": "info",
            "title": "Thiếu Oxy Nhẹ",
            "message": f"P/F ratio ({pf_ratio:.0f}) 200-300 - ARDS nhẹ",
            "action": "Theo dõi, có thể cần tăng PEEP nhẹ",
            "details": [
                "Theo bảng PEEP/FiO2 ARDSNet",
                "Có thể tăng PEEP 8-12 cmH2O",
                "Theo dõi oxy hóa"
            ],
            "reference": "ARDSNet Protocol: P/F 200-300 = ARDS nhẹ"
        })
    
    return alerts


def display_alerts(alerts):
    """Hiển thị cảnh báo với format đẹp"""
    if not alerts:
        st.success("✅ Không có cảnh báo - Tất cả thông số trong giới hạn an toàn")
        return
    
    # Sort by level (critical first)
    level_order = {"critical": 0, "warning": 1, "info": 2}
    sorted_alerts = sorted(alerts, key=lambda x: level_order.get(x["level"], 3))
    
    st.markdown("### ⚠️ Hệ Thống Cảnh Báo")
    
    for alert in sorted_alerts:
        if alert["level"] == "critical":
            st.error(f"""
            **🔴 {alert['title']}**
            
            {alert['message']}
            
            **💡 Hành động:** {alert['action']}
            
            **Chi tiết:**
            """)
            for detail in alert["details"]:
                st.markdown(f"- {detail}")
            st.caption(f"📚 {alert['reference']}")
            
        elif alert["level"] == "warning":
            st.warning(f"""
            **🟡 {alert['title']}**
            
            {alert['message']}
            
            **💡 Hành động:** {alert['action']}
            
            **Chi tiết:**
            """)
            for detail in alert["details"]:
                st.markdown(f"- {detail}")
            st.caption(f"📚 {alert['reference']}")
            
        else:
            st.info(f"""
            **🔵 {alert['title']}**
            
            {alert['message']}
            
            **💡 Hành động:** {alert['action']}
            
            **Chi tiết:**
            """)
            for detail in alert["details"]:
                st.markdown(f"- {detail}")
            st.caption(f"📚 {alert['reference']}")
        
        st.markdown("---")


def get_alert_summary(alerts):
    """Tóm tắt số lượng cảnh báo theo mức độ"""
    summary = {
        "critical": 0,
        "warning": 0,
        "info": 0
    }
    
    for alert in alerts:
        level = alert["level"]
        if level in summary:
            summary[level] += 1
    
    return summary

