"""
ABG-based Ventilator Adjustment Advisor
Tư vấn điều chỉnh máy thở dựa trên ABG
"""

import streamlit as st


def analyze_abg_for_ventilator(abg_data):
    """Phân tích ABG và đề xuất điều chỉnh máy thở"""
    recommendations = []
    
    # Acid-base analysis
    ph = abg_data["ph"]
    pco2 = abg_data["pco2"]
    hco3 = abg_data["hco3"]
    
    # Respiratory acidosis
    if ph < 7.35 and pco2 > 45:
        severity = "nặng" if ph < 7.20 else "trung bình"
        recommendations.append({
            "type": "error",
            "title": "Toan hô hấp",
            "message": f"PaCO₂ cao ({pco2:.1f} mmHg), pH thấp ({ph:.2f}) - {severity}",
            "actions": [
                "Tăng RR để tăng thông khí (tăng 2-4 lần/phút)",
                "Kiểm tra Vt có đủ không (6-8 mL/kg PBW)",
                "Kiểm tra auto-PEEP (có thể làm giảm thông khí)",
                "Cân nhắc tăng flow rate nếu cần",
                "Theo dõi pH, nếu <7.15 có thể cần điều chỉnh mạnh hơn"
            ],
            "priority": "high"
        })
    
    # Respiratory alkalosis
    elif ph > 7.45 and pco2 < 35:
        recommendations.append({
            "type": "warning",
            "title": "Kiềm hô hấp",
            "message": f"PaCO₂ thấp ({pco2:.1f} mmHg), pH cao ({ph:.2f})",
            "actions": [
                "Giảm RR nếu quá cao (giảm 2-4 lần/phút)",
                "Kiểm tra Vt có quá lớn không",
                "Có thể do thở máy quá mức - cân nhắc giảm hỗ trợ"
            ],
            "priority": "medium"
        })
    
    # Metabolic acidosis
    if ph < 7.35 and hco3 < 22:
        severity = "nặng" if hco3 < 15 else "trung bình"
        recommendations.append({
            "type": "warning",
            "title": "Toan Chuyển Hóa",
            "message": f"HCO₃ thấp ({hco3:.1f} mEq/L) - {severity}",
            "actions": [
                "Điều trị nguyên nhân (sepsis, shock, lactic acidosis, etc.)",
                "Có thể tăng RR nhẹ để bù (tăng 2-4 lần/phút)",
                "Cân nhắc NaHCO₃ nếu nặng và pH <7.15",
                "Theo dõi lactate, anion gap"
            ],
            "priority": "high"
        })
    
    # Metabolic alkalosis
    elif ph > 7.45 and hco3 > 26:
        recommendations.append({
            "type": "info",
            "title": "Kiềm Chuyển Hóa",
            "message": f"HCO₃ cao ({hco3:.1f} mEq/L)",
            "actions": [
                "Điều trị nguyên nhân (mất acid, truyền HCO₃, etc.)",
                "Có thể giảm RR nhẹ nếu không cần thiết",
                "Theo dõi điện giải (K+, Cl-)"
            ],
            "priority": "low"
        })
    
    return recommendations


def recommend_ventilator_adjustments(abg_data, vent_settings, pbw):
    """Đề xuất điều chỉnh thông số máy thở dựa trên ABG và thông số hiện tại"""
    recommendations = []
    
    pf_ratio = abg_data["po2"] / (abg_data["fio2"] / 100) if abg_data["fio2"] > 0 else None
    ph = abg_data["ph"]
    pco2 = abg_data["pco2"]
    
    # Hypoxemia (P/F ratio thấp)
    if pf_ratio and pf_ratio < 200:
        # PEEP adjustment
        current_peep = vent_settings.get("peep", 0)
        if pf_ratio < 100:  # ARDS nặng
            suggested_peep = max(current_peep + 2, 18)
            if suggested_peep <= 24:
                recommendations.append({
                    "parameter": "PEEP",
                    "current": current_peep,
                    "suggested": suggested_peep,
                    "reason": f"P/F ratio rất thấp ({pf_ratio:.0f}) - ARDS nặng, cần tăng PEEP",
                    "priority": "high"
                })
        elif pf_ratio < 200:  # ARDS trung bình
            suggested_peep = max(current_peep + 2, 14)
            if suggested_peep <= 18:
                recommendations.append({
                    "parameter": "PEEP",
                    "current": current_peep,
                    "suggested": suggested_peep,
                    "reason": f"P/F ratio thấp ({pf_ratio:.0f}) - Cần tăng PEEP",
                    "priority": "high"
                })
        
        # FiO2 adjustment
        current_fio2 = abg_data["fio2"]
        if current_fio2 < 60:
            suggested_fio2 = min(current_fio2 + 10, 100)
            recommendations.append({
                "parameter": "FiO₂",
                "current": current_fio2,
                "suggested": suggested_fio2,
                "reason": "Oxy hóa kém - Cần tăng FiO₂",
                "priority": "high"
            })
    
    # Hypercapnia (PaCO2 cao)
    if pco2 > 45:
        current_rr = vent_settings.get("rr", 0)
        if current_rr < 25:
            suggested_rr = min(current_rr + 2, 35)
            recommendations.append({
                "parameter": "RR",
                "current": current_rr,
                "suggested": suggested_rr,
                "reason": f"PaCO₂ cao ({pco2:.1f} mmHg) - Cần tăng thông khí",
                "priority": "high"
            })
        
        # Check Vt
        current_vt = vent_settings.get("vt", 0)
        if current_vt > 0 and pbw > 0:
            vt_per_kg = current_vt / pbw
            if vt_per_kg < 6:
                suggested_vt = int(pbw * 6)
                recommendations.append({
                    "parameter": "Vt",
                    "current": current_vt,
                    "suggested": suggested_vt,
                    "reason": "Vt/kg thấp - Có thể tăng Vt để tăng thông khí",
                    "priority": "medium"
                })
    
    # Hypocapnia (PaCO2 thấp)
    elif pco2 < 35:
        current_rr = vent_settings.get("rr", 0)
        if current_rr > 12:
            suggested_rr = max(current_rr - 2, 8)
            recommendations.append({
                "parameter": "RR",
                "current": current_rr,
                "suggested": suggested_rr,
                "reason": f"PaCO₂ thấp ({pco2:.1f} mmHg) - Có thể giảm RR",
                "priority": "medium"
            })
    
    # Severe acidosis
    if ph < 7.20:
        current_rr = vent_settings.get("rr", 0)
        if current_rr < 30:
            suggested_rr = min(current_rr + 4, 35)
            recommendations.append({
                "parameter": "RR",
                "current": current_rr,
                "suggested": suggested_rr,
                "reason": f"pH rất thấp ({ph:.2f}) - Cần tăng thông khí mạnh",
                "priority": "critical"
            })
    
    return recommendations


def get_ventilator_adjustment_summary(abg_data, vent_settings, pbw):
    """Tổng hợp tất cả khuyến nghị điều chỉnh"""
    abg_recommendations = analyze_abg_for_ventilator(abg_data)
    vent_recommendations = recommend_ventilator_adjustments(abg_data, vent_settings, pbw)
    
    return {
        "abg_analysis": abg_recommendations,
        "ventilator_adjustments": vent_recommendations
    }


def display_abg_recommendations(recommendations):
    """Hiển thị khuyến nghị từ ABG analysis"""
    if not recommendations:
        return
    
    st.markdown("### 🔬 Phân tích ABG & Khuyến nghị")
    
    # Sort by priority
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    sorted_recs = sorted(recommendations, key=lambda x: priority_order.get(x.get("priority", "low"), 3))
    
    for rec in sorted_recs:
        if rec["type"] == "error":
            st.error(f"**🔴 {rec['title']}**\n\n{rec['message']}")
        elif rec["type"] == "warning":
            st.warning(f"**🟡 {rec['title']}**\n\n{rec['message']}")
        else:
            st.info(f"**🔵 {rec['title']}**\n\n{rec['message']}")
        
        st.markdown("**💡 Hành động đề xuất:**")
        for i, action in enumerate(rec["actions"], 1):
            st.markdown(f"{i}. {action}")
        
        st.markdown("---")


def display_ventilator_adjustments(recommendations):
    """Hiển thị khuyến nghị điều chỉnh thông số máy thở"""
    if not recommendations:
        st.success("✅ Không có khuyến nghị điều chỉnh thông số máy thở")
        return
    
    st.markdown("### ⚙️ Khuyến nghị điều chỉnh Thông Số Máy Thở")
    
    # Group by parameter
    by_parameter = {}
    for rec in recommendations:
        param = rec["parameter"]
        if param not in by_parameter:
            by_parameter[param] = []
        by_parameter[param].append(rec)
    
    # Display by parameter
    for param, recs in by_parameter.items():
        # Get highest priority
        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        highest_priority = min(recs, key=lambda x: priority_order.get(x.get("priority", "low"), 3))
        
        rec = highest_priority
        priority_icon = "🔴" if rec["priority"] == "critical" else "🟡" if rec["priority"] == "high" else "🔵"
        
        st.markdown(f"**{priority_icon} {param}:**")
        st.markdown(f"- **Hiện tại:** {rec['current']}")
        st.markdown(f"- **Đề xuất:** {rec['suggested']}")
        st.markdown(f"- **Lý do:** {rec['reason']}")
        st.markdown("---")

