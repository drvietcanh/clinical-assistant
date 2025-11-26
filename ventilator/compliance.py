"""
Compliance Calculator
Tính toán và phân tích compliance
"""

import streamlit as st


def calculate_static_compliance(vt, plateau, peep):
    """
    Tính Static Compliance
    C_static = Vt / (Plateau - PEEP)
    """
    if plateau > 0 and peep >= 0:
        driving_pressure = plateau - peep
        if driving_pressure > 0 and vt > 0:
            return vt / driving_pressure
    return None


def calculate_dynamic_compliance(vt, peak, peep):
    """
    Tính Dynamic Compliance
    C_dynamic = Vt / (Peak - PEEP)
    """
    if peak > 0 and peep >= 0:
        driving_pressure = peak - peep
        if driving_pressure > 0 and vt > 0:
            return vt / driving_pressure
    return None


def interpret_compliance(compliance, compliance_type="static"):
    """
    Đánh giá compliance
    Normal: 30-50 mL/cmH2O (static), 40-60 mL/cmH2O (dynamic)
    """
    if compliance is None:
        return None, None, None
    
    if compliance_type == "static":
        if compliance < 20:
            return "Rất thấp", "error", "Phổi rất cứng, khó thông khí"
        elif compliance < 30:
            return "Thấp", "error", "Phổi cứng, cần điều chỉnh thông số"
        elif compliance <= 50:
            return "Bình thường", "success", "Compliance trong giới hạn bình thường"
        elif compliance <= 80:
            return "Cao", "info", "Compliance cao, phổi mềm"
        else:
            return "Rất cao", "warning", "Compliance rất cao, có thể do Vt quá lớn"
    else:  # dynamic
        if compliance < 30:
            return "Thấp", "error", "Dynamic compliance thấp"
        elif compliance <= 60:
            return "Bình thường", "success", "Dynamic compliance bình thường"
        else:
            return "Cao", "info", "Dynamic compliance cao"
    
    return None, None, None


def calculate_compliance_change(old_compliance, new_compliance):
    """Tính thay đổi compliance"""
    if old_compliance is None or new_compliance is None:
        return None
    
    if old_compliance == 0:
        return None
    
    change_percent = ((new_compliance - old_compliance) / old_compliance) * 100
    return change_percent


def get_compliance_recommendations(compliance, plateau, peep, vt, pbw):
    """Đề xuất điều chỉnh dựa trên compliance"""
    recommendations = []
    
    if compliance is None:
        return recommendations
    
    # Low compliance
    if compliance < 30:
        recommendations.append({
            "priority": "high",
            "title": "Compliance Thấp - Phổi Cứng",
            "actions": [
                "Giảm Vt để giảm áp lực (target: 6 mL/kg PBW)",
                f"Kiểm tra plateau pressure (hiện tại: {plateau} cmH2O, target: ≤30 cmH2O)",
                "Cân nhắc tăng PEEP nếu phù hợp (recruitment maneuver)",
                "Kiểm tra nguyên nhân: ARDS, xẹp phổi, phù phổi, etc.",
                "Theo dõi driving pressure (target: ≤15 cmH2O)"
            ]
        })
    
    # Very low compliance
    if compliance < 20:
        recommendations.append({
            "priority": "critical",
            "title": "Compliance Rất Thấp - Nguy Hiểm",
            "actions": [
                "Giảm Vt ngay lập tức",
                "Kiểm tra plateau pressure - có thể cần giảm mạnh Vt",
                "Cân nhắc tăng PEEP (nếu không làm tăng plateau)",
                "Theo dõi huyết động chặt chẽ",
                "Cân nhắc prone positioning nếu ARDS"
            ]
        })
    
    # High compliance
    if compliance > 80:
        recommendations.append({
            "priority": "medium",
            "title": "Compliance Rất Cao",
            "actions": [
                "Kiểm tra Vt có quá lớn không",
                "Có thể giảm Vt nếu không cần thiết",
                "Theo dõi để đảm bảo không có barotrauma"
            ]
        })
    
    # Normal compliance but high plateau
    if 30 <= compliance <= 50 and plateau > 30:
        recommendations.append({
            "priority": "high",
            "title": "Compliance Bình Thường Nhưng Plateau Cao",
            "actions": [
                "Giảm Vt để giảm plateau pressure",
                f"Target Vt: {int(pbw * 6)} mL (6 mL/kg PBW)",
                "Theo dõi compliance sau khi điều chỉnh"
            ]
        })
    
    return recommendations


def display_compliance_analysis(static_compliance, dynamic_compliance, plateau, peak, peep, vt, pbw):
    """Hiển thị phân tích compliance đầy đủ"""
    st.markdown("### 📊 Phân tích Compliance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Static Compliance")
        if static_compliance:
            interpretation, color, description = interpret_compliance(static_compliance, "static")
            if color == "success":
                st.success(f"**{static_compliance:.1f}** mL/cmH2O ✓")
            elif color == "error":
                st.error(f"**{static_compliance:.1f}** mL/cmH2O ⚠️")
            elif color == "warning":
                st.warning(f"**{static_compliance:.1f}** mL/cmH2O")
            else:
                st.info(f"**{static_compliance:.1f}** mL/cmH2O")
            st.caption(f"{interpretation} - {description}")
        else:
            st.info("Cần nhập Plateau & PEEP")
    
    with col2:
        st.markdown("#### Dynamic Compliance")
        if dynamic_compliance:
            interpretation, color, description = interpret_compliance(dynamic_compliance, "dynamic")
            if color == "success":
                st.success(f"**{dynamic_compliance:.1f}** mL/cmH2O ✓")
            elif color == "error":
                st.error(f"**{dynamic_compliance:.1f}** mL/cmH2O ⚠️")
            else:
                st.info(f"**{dynamic_compliance:.1f}** mL/cmH2O")
            st.caption(f"{interpretation} - {description}")
        else:
            st.info("Cần nhập Peak & PEEP")
    
    # Comparison
    if static_compliance and dynamic_compliance:
        st.markdown("---")
        st.markdown("#### So Sánh Static vs Dynamic")
        difference = dynamic_compliance - static_compliance
        if abs(difference) < 5:
            st.success("Static và Dynamic compliance gần nhau - Không có sự khác biệt đáng kể")
        else:
            st.warning(f"Chênh lệch: {difference:.1f} mL/cmH2O")
            st.caption("Chênh lệch lớn có thể do airway resistance cao")
    
    # Recommendations
    recommendations = get_compliance_recommendations(static_compliance, plateau, peep, vt, pbw)
    if recommendations:
        st.markdown("---")
        st.markdown("#### 💡 Khuyến nghị Dựa Trên Compliance")
        for rec in recommendations:
            if rec["priority"] == "critical":
                st.error(f"**🔴 {rec['title']}**")
            elif rec["priority"] == "high":
                st.warning(f"**🟡 {rec['title']}**")
            else:
                st.info(f"**🔵 {rec['title']}**")
            
            for action in rec["actions"]:
                st.markdown(f"- {action}")
            st.markdown("---")
    
    # Formula explanation
    with st.expander("📐 Công Thức Compliance"):
        st.markdown("""
        **Static Compliance:**
        ```
        C_static = Vt / (Plateau - PEEP)
        ```
        
        **Dynamic Compliance:**
        ```
        C_dynamic = Vt / (Peak - PEEP)
        ```
        
        **Ý nghĩa:**
        - **Static compliance:** Đo khi không có flow (giữ hơi thở) - phản ánh độ đàn hồi của phổi
        - **Dynamic compliance:** Đo khi có flow - phản ánh cả độ đàn hồi và airway resistance
        
        **Bình thường:**
        - Static: 30-50 mL/cmH2O
        - Dynamic: 40-60 mL/cmH2O
        
        **Thấp (<30):** Phổi cứng, khó thông khí
        **Cao (>80):** Có thể do Vt quá lớn hoặc phổi quá mềm
        """)

