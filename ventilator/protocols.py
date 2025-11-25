"""
Ventilator Protocol Recommendations
Khuyến nghị dựa trên protocol chuẩn
"""

import streamlit as st


def get_ardsnet_recommendations(pbw, pf_ratio, has_ards=True):
    """Khuyến nghị theo ARDSNet protocol"""
    recommendations = []
    
    # Target Vt
    target_vt = pbw * 6
    recommendations.append({
        "parameter": "Vt",
        "target": f"{target_vt:.0f} mL",
        "target_per_kg": "6 mL/kg PBW",
        "reason": "ARDSNet protocol - Lung-protective ventilation",
        "reference": "ARDSNet 2000: Vt = 6 mL/kg PBW"
    })
    
    # Target RR
    recommendations.append({
        "parameter": "RR",
        "target": "20-35 lần/phút",
        "reason": "Điều chỉnh để pH 7.30-7.45",
        "reference": "ARDSNet Protocol"
    })
    
    # PEEP/FiO2 based on P/F ratio
    if pf_ratio:
        if pf_ratio < 100:
            recommendations.append({
                "parameter": "PEEP/FiO₂",
                "target": "PEEP 18-24 cmH2O, FiO₂ 0.8-1.0",
                "reason": "ARDS rất nặng - P/F <100",
                "reference": "ARDSNet PEEP/FiO2 Table"
            })
        elif pf_ratio < 200:
            recommendations.append({
                "parameter": "PEEP/FiO₂",
                "target": "PEEP 14-18 cmH2O, FiO₂ 0.6-0.8",
                "reason": "ARDS trung bình - P/F 100-200",
                "reference": "ARDSNet PEEP/FiO2 Table"
            })
        elif pf_ratio < 300:
            recommendations.append({
                "parameter": "PEEP/FiO₂",
                "target": "PEEP 8-12 cmH2O, FiO₂ 0.4-0.6",
                "reason": "ARDS nhẹ - P/F 200-300",
                "reference": "ARDSNet PEEP/FiO2 Table"
            })
        else:
            recommendations.append({
                "parameter": "PEEP/FiO₂",
                "target": "PEEP 5-8 cmH2O, FiO₂ 0.3-0.4",
                "reason": "P/F >300 - Thiếu oxy nhẹ",
                "reference": "ARDSNet PEEP/FiO2 Table"
            })
    
    # Plateau pressure limit
    recommendations.append({
        "parameter": "Plateau Pressure",
        "target": "≤30 cmH2O",
        "reason": "Giới hạn an toàn theo ARDSNet",
        "reference": "ARDSNet Protocol: Plateau ≤30 cmH2O"
    })
    
    # Driving pressure limit
    recommendations.append({
        "parameter": "Driving Pressure",
        "target": "≤15 cmH2O",
        "reason": "Giới hạn an toàn",
        "reference": "Amato et al. 2015: ΔP ≤15 cmH2O"
    })
    
    return recommendations


def get_sepsis_guidelines_recommendations():
    """Khuyến nghị theo Surviving Sepsis Campaign 2021"""
    return [
        {
            "title": "Lung-Protective Ventilation",
            "recommendations": [
                "Vt ≤6-8 mL/kg PBW (lung-protective)",
                "Plateau pressure ≤30 cmH2O",
                "PEEP ≥5 cmH2O"
            ],
            "reference": "Surviving Sepsis Campaign 2021"
        },
        {
            "title": "Permissive Hypercapnia",
            "recommendations": [
                "Cho phép pH ≥7.15",
                "Không cần điều chỉnh nếu pH >7.15",
                "Theo dõi pH và PaCO₂"
            ],
            "reference": "Surviving Sepsis Campaign 2021"
        },
        {
            "title": "PEEP Titration",
            "recommendations": [
                "Theo bảng PEEP/FiO2 ARDSNet",
                "Tối ưu hóa recruitment",
                "Tránh hyperinflation"
            ],
            "reference": "Surviving Sepsis Campaign 2021"
        }
    ]


def get_copd_recommendations():
    """Khuyến nghị cho COPD"""
    return [
        {
            "title": "COPD Ventilation Strategy",
            "recommendations": [
                "Vt: 6-8 mL/kg PBW",
                "RR: 10-14 lần/phút (thấp để đảm bảo thời gian thở ra)",
                "PEEP: 5-8 cmH2O (vừa đủ để chống auto-PEEP)",
                "I:E: 1:3 đến 1:4 (thở ra dài)",
                "Flow: 60-80 L/min",
                "Theo dõi auto-PEEP chặt chẽ"
            ],
            "reference": "AARC Clinical Practice Guidelines"
        }
    ]


def get_asthma_recommendations():
    """Khuyến nghị cho Asthma"""
    return [
        {
            "title": "Asthma Ventilation Strategy",
            "recommendations": [
                "Vt: 6-8 mL/kg PBW",
                "RR: 8-12 lần/phút (rất thấp để tránh hyperinflation)",
                "PEEP: 0-5 cmH2O (cẩn thận với PEEP)",
                "I:E: 1:4 đến 1:5 (thở ra rất dài)",
                "Flow: 80-100 L/min",
                "Cho phép hypercapnia (pH có thể xuống 7.0-7.2)",
                "Theo dõi auto-PEEP chặt chẽ"
            ],
            "reference": "ATS/ERS Guidelines"
        }
    ]


def display_protocol_recommendations(protocol_type, **kwargs):
    """Hiển thị khuyến nghị theo protocol"""
    if protocol_type == "ARDSNet":
        pbw = kwargs.get("pbw", 70)
        pf_ratio = kwargs.get("pf_ratio", 200)
        has_ards = kwargs.get("has_ards", True)
        
        recommendations = get_ardsnet_recommendations(pbw, pf_ratio, has_ards)
        
        st.markdown("### 📋 ARDSNet Protocol Recommendations")
        st.info("""
        **ARDSNet Protocol (2000):**
        - Lung-protective ventilation với Vt = 6 mL/kg PBW
        - Plateau pressure ≤30 cmH2O
        - PEEP/FiO2 theo bảng
        - Cho phép hypercapnia nhẹ (pH ≥7.15)
        """)
        
        for rec in recommendations:
            st.markdown(f"**{rec['parameter']}:**")
            st.markdown(f"- **Mục Tiêu:** {rec['target']}")
            if 'target_per_kg' in rec:
                st.markdown(f"- **Theo PBW:** {rec['target_per_kg']}")
            st.markdown(f"- **Lý do:** {rec['reason']}")
            st.caption(f"📚 {rec['reference']}")
            st.markdown("---")
    
    elif protocol_type == "Sepsis":
        recommendations = get_sepsis_guidelines_recommendations()
        
        st.markdown("### 📋 Surviving Sepsis Campaign 2021 Guidelines")
        
        for rec in recommendations:
            st.markdown(f"**{rec['title']}:**")
            for item in rec['recommendations']:
                st.markdown(f"- {item}")
            st.caption(f"📚 {rec['reference']}")
            st.markdown("---")
    
    elif protocol_type == "COPD":
        recommendations = get_copd_recommendations()
        
        st.markdown("### 📋 COPD Ventilation Recommendations")
        
        for rec in recommendations:
            st.markdown(f"**{rec['title']}:**")
            for item in rec['recommendations']:
                st.markdown(f"- {item}")
            st.caption(f"📚 {rec['reference']}")
            st.markdown("---")
    
    elif protocol_type == "Asthma":
        recommendations = get_asthma_recommendations()
        
        st.markdown("### 📋 Asthma Ventilation Recommendations")
        
        for rec in recommendations:
            st.markdown(f"**{rec['title']}:**")
            for item in rec['recommendations']:
                st.markdown(f"- {item}")
            st.caption(f"📚 {rec['reference']}")
            st.markdown("---")


def get_protocol_summary(protocol_type, **kwargs):
    """Tóm tắt protocol recommendations"""
    if protocol_type == "ARDSNet":
        pbw = kwargs.get("pbw", 70)
        pf_ratio = kwargs.get("pf_ratio", 200)
        
        return {
            "vt_target": f"{pbw * 6:.0f} mL (6 mL/kg PBW)",
            "rr_target": "20-35 lần/phút",
            "plateau_limit": "≤30 cmH2O",
            "driving_p_limit": "≤15 cmH2O",
            "peep_fio2": "Theo bảng PEEP/FiO2 dựa trên P/F ratio"
        }
    
    return None

