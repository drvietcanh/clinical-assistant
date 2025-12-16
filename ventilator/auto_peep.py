"""
Auto-PEEP Estimation and Analysis
Ước tính và phân tích auto-PEEP
"""

import streamlit as st


def estimate_auto_peep(plateau, peep, end_expiratory_pause_pressure=None):
    """
    Ước tính auto-PEEP
    Auto-PEEP = End-expiratory pause pressure - Set PEEP
    Hoặc ước tính từ plateau và PEEP nếu không có end-expiratory pause
    """
    if end_expiratory_pause_pressure is not None:
        auto_peep = end_expiratory_pause_pressure - peep
        return max(0, auto_peep)  # Không thể âm
    
    # Ước tính từ plateau (nếu có)
    # Nếu plateau cao và PEEP thấp, có thể có auto-PEEP
    if plateau > 0 and peep >= 0:
        # Ước tính thô: nếu plateau cao so với PEEP, có thể có auto-PEEP
        # Đây chỉ là ước tính, cần đo thực tế
        estimated = None  # Không thể ước tính chính xác mà không có end-expiratory pause
        return estimated
    
    return None


def interpret_auto_peep(auto_peep):
    """Đánh giá mức độ auto-PEEP"""
    if auto_peep is None:
        return None, None, None
    
    if auto_peep < 2:
        return "Không đáng kể", "success", "Auto-PEEP thấp, không cần điều chỉnh"
    elif auto_peep < 5:
        return "Nhẹ", "info", "Auto-PEEP nhẹ, theo dõi"
    elif auto_peep < 10:
        return "Trung bình", "warning", "Auto-PEEP trung bình, cần điều chỉnh"
    else:
        return "Nặng", "error", "Auto-PEEP nặng, cần điều chỉnh ngay"
    
    return None, None, None


def get_auto_peep_recommendations(auto_peep, rr, ie_ratio, vt, peep):
    """Đề xuất điều chỉnh để giảm auto-PEEP"""
    recommendations = []
    
    if auto_peep is None or auto_peep < 2:
        return recommendations
    
    # Reduce RR
    if rr > 12:
        new_rr = max(rr - 2, 8)
        recommendations.append({
            "parameter": "RR",
            "current": rr,
            "suggested": new_rr,
            "reason": f"Auto-PEEP {auto_peep:.1f} cmH2O - Giảm RR để tăng thời gian thở ra",
            "priority": "high" if auto_peep >= 5 else "medium"
        })
    
    # Increase I:E ratio (longer expiratory time)
    if ie_ratio:
        # Parse I:E ratio (e.g., "1:2" -> 1/2 = 0.5)
        try:
            parts = ie_ratio.split(":")
            if len(parts) == 2:
                i_ratio = float(parts[0])
                e_ratio = float(parts[1])
                current_ie = i_ratio / e_ratio
                # Increase expiratory time (decrease I:E ratio)
                if current_ie > 0.3:  # If I:E > 1:3
                    new_e_ratio = e_ratio + 1
                    new_ie = f"{int(i_ratio)}:{int(new_e_ratio)}"
                    recommendations.append({
                        "parameter": "I:E Ratio",
                        "current": ie_ratio,
                        "suggested": new_ie,
                        "reason": f"Auto-PEEP {auto_peep:.1f} cmH2O - Tăng thời gian thở ra",
                        "priority": "high" if auto_peep >= 5 else "medium"
                    })
        except:
            pass
    
    # Reduce Vt if too high
    if vt > 0:
        recommendations.append({
            "parameter": "Vt",
            "current": vt,
            "suggested": f"Giảm {int(vt * 0.1)}-{int(vt * 0.2)} mL",
            "reason": f"Auto-PEEP {auto_peep:.1f} cmH2O - Giảm Vt để giảm thời gian thở ra",
            "priority": "medium"
        })
    
    # Increase PEEP to counter auto-PEEP (external PEEP)
    if auto_peep >= 5:
        new_peep = min(peep + int(auto_peep * 0.5), peep + 5)
        recommendations.append({
            "parameter": "PEEP",
            "current": peep,
            "suggested": new_peep,
            "reason": f"Auto-PEEP {auto_peep:.1f} cmH2O - Tăng PEEP để chống auto-PEEP (external PEEP)",
            "priority": "high",
            "note": "External PEEP nên bằng 75-85% auto-PEEP"
        })
    
    return recommendations


def display_auto_peep_analysis(auto_peep, plateau, peep, rr, ie_ratio, vt):
    """Hiển thị phân tích auto-PEEP"""
    st.markdown("### 💨 Phân tích Auto-PEEP")
    
    if auto_peep is None:
        st.info("""
        **Cần đo End-Expiratory Pause Pressure để tính auto-PEEP chính xác:**
        
        1. Giữ hơi thở ở cuối thì thở ra (end-expiratory pause)
        2. Đọc áp lực trên máy thở
        3. Auto-PEEP = End-expiratory pause pressure - Set PEEP
        """)
        return
    
    # Display auto-PEEP value
    interpretation, color, description = interpret_auto_peep(auto_peep)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Auto-PEEP")
        if color == "success":
            st.success(f"**{auto_peep:.1f}** cmH2O ✓")
        elif color == "error":
            st.error(f"**{auto_peep:.1f}** cmH2O ⚠️")
        elif color == "warning":
            st.warning(f"**{auto_peep:.1f}** cmH2O ⚠️")
        else:
            st.info(f"**{auto_peep:.1f}** cmH2O")
        st.caption(f"{interpretation} - {description}")
    
    with col2:
        st.markdown("#### Set PEEP")
        st.info(f"**{peep}** cmH2O")
        st.caption("PEEP đã cài đặt")
    
    # Recommendations
    recommendations = get_auto_peep_recommendations(auto_peep, rr, ie_ratio, vt, peep)
    if recommendations:
        st.markdown("---")
        st.markdown("#### 💡 Khuyến nghị điều chỉnh")
        for rec in recommendations:
            priority_icon = "🔴" if rec["priority"] == "high" else "🟡" if rec["priority"] == "medium" else "🔵"
            st.markdown(f"**{priority_icon} {rec['parameter']}:**")
            st.markdown(f"- **Hiện tại:** {rec['current']}")
            st.markdown(f"- **Đề xuất:** {rec['suggested']}")
            st.markdown(f"- **Lý do:** {rec['reason']}")
            if "note" in rec:
                st.caption(f"💡 {rec['note']}")
            st.markdown("---")
    
    # Information
    with st.expander("📚 Thông tin về Auto-PEEP"):
        st.markdown("""
        **Auto-PEEP (Intrinsic PEEP):**
        - Áp lực dương còn lại trong phổi ở cuối thì thở ra
        - Xảy ra khi thời gian thở ra không đủ để đẩy hết khí ra ngoài
        
        **Nguyên nhân:**
        - RR quá cao
        - I:E ratio không phù hợp (thời gian thở ra ngắn)
        - Vt quá lớn
        - Airway resistance cao (COPD, Asthma)
        - Compliance thấp
        
        **Hậu quả:**
        - Giảm thông khí
        - Tăng áp lực trong lồng ngực
        - Ảnh hưởng huyết động
        - Barotrauma
        
        **Điều trị:**
        - Giảm RR
        - Tăng thời gian thở ra (giảm I:E ratio)
        - Giảm Vt
        - Tăng PEEP external (75-85% auto-PEEP) để chống auto-PEEP
        - Điều trị nguyên nhân (bronchodilators, etc.)
        
        **Đo auto-PEEP:**
        - End-expiratory pause maneuver
        - Auto-PEEP = End-expiratory pause pressure - Set PEEP
        """)

