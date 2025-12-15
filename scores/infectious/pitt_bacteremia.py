"""
Pitt Bacteremia Score Calculator
Tiên lượng nhiễm khuẩn huyết
"""

import streamlit as st
from components.ui.scoring import render_score_result, render_score_breakdown


def calculate_pitt(temp, hypotension, ventilator, cardiac_arrest, mental_status):
    """
    Tính Pitt Bacteremia Score
    
    Parameters: Các thành phần điểm
    Returns: dict với total_score và interpretation
    """
    total = temp + hypotension + ventilator + cardiac_arrest + mental_status
    
    # Phân loại
    if total <= 1:
        risk = "Thấp"
        mortality = "1-5%"
        color = "green"
    elif total <= 3:
        risk = "Trung bình"
        mortality = "6-20%"
        color = "orange"
    else:  # >= 4
        risk = "Cao"
        mortality = "> 20%"
        color = "red"
    
    return {
        "total_score": total,
        "risk_level": risk,
        "mortality": mortality,
        "color": color
    }


def render():
    """Render Pitt Bacteremia Score interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #DC2626;'>🦠 Pitt Bacteremia Score</h2>
    <p style='text-align: center;'><em>Tiên lượng tử vong trong nhiễm khuẩn huyết</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Pitt Bacteremia Score"):
        st.markdown("""
        **Pitt Bacteremia Score** đánh giá nguy cơ tử vong ở bệnh nhân nhiễm khuẩn huyết.
        
        **Mục đích:**
        - Dự đoán tử vong trong 30 ngày
        - Đánh giá mức độ nặng
        - Hỗ trợ quyết định điều trị
        
        **Thang điểm:** 0-14 điểm
        - 0-1: Nguy cơ thấp (tử vong 1-5%)
        - 2-3: Nguy cơ trung bình (6-20%)
        - ≥4: Nguy cơ cao (>20%)
        """)
    
    st.markdown("---")
    st.subheader("📝 Đánh giá 5 thành phần")
    
    # Temperature
    temp = st.radio(
        "🌡️ Nhiệt độ",
        options=[0, 2],
        format_func=lambda x: "0 điểm - 35.1-36.0°C hoặc 39.0-39.9°C" if x == 0 else "2 điểm - ≤35°C hoặc ≥40°C",
        help="Nhiệt độ bất thường nặng = 2 điểm"
    )
    
    # Hypotension
    hypotension = st.radio(
        "💓 Hạ huyết áp",
        options=[0, 2],
        format_func=lambda x: "0 điểm - Không hạ huyết áp" if x == 0 else "2 điểm - Có hạ huyết áp (SBP<90 hoặc cần vasopressor)",
        help="Hạ huyết áp hoặc cần thuốc vận mạch = 2 điểm"
    )
    
    # Mechanical ventilation
    ventilator = st.radio(
        "🫁 Thở máy",
        options=[0, 2],
        format_func=lambda x: "0 điểm - Không thở máy" if x == 0 else "2 điểm - Đang thở máy",
        help="Cần thở máy = 2 điểm"
    )
    
    # Cardiac arrest
    cardiac_arrest = st.radio(
        "🫀 Ngưng tim",
        options=[0, 4],
        format_func=lambda x: "0 điểm - Không ngưng tim" if x == 0 else "4 điểm - Có ngưng tim",
        help="Ngưng tim = 4 điểm"
    )
    
    # Mental status
    mental_status = st.radio(
        "🧠 Ý thức",
        options=[0, 2],
        format_func=lambda x: "0 điểm - Alert (tỉnh táo)" if x == 0 else "2 điểm - Lơ mơ/Hôn mê",
        help="Rối loạn ý thức = 2 điểm"
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm Pitt Bacteremia", type="primary", use_container_width=True):
        result = calculate_pitt(temp, hypotension, ventilator, cardiac_arrest, mental_status)
        
        st.markdown("## 📊 Kết quả")
        
        score_color = {
            "green": "#28a745",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }[result["color"]]
        
        icon_map = {
            "green": "✅",
            "orange": "⚠️",
            "red": "🚨"
        }
        icon = icon_map[result["color"]]
        
        interpretation_map = {
            "green": "Nguy cơ thấp",
            "orange": "Nguy cơ trung bình",
            "red": "Nguy cơ cao"
        }
        interpretation = f"{interpretation_map[result['color']]} - Tử vong 30 ngày: {result['mortality']}"
        
        # Use render_score_result for main score display
        render_score_result(
            title="Pitt Bacteremia Score",
            score=result['total_score'],
            interpretation=interpretation,
            mortality=f"Tỷ lệ tử vong: {result['mortality']}",
            color=score_color,
            icon=icon,
            size="large"
        )
        
        # Use render_score_breakdown for component scores
        render_score_breakdown(
            title="Điểm Từng Thành Phần",
            subscores={
                "🌡️ Nhiệt độ": temp,
                "💓 Hạ huyết áp": hypotension,
                "🫁 Thở máy": ventilator,
                "🫀 Ngưng tim": cardiac_arrest,
                "🧠 Ý thức": mental_status
            },
            total_score=result['total_score']
        )
        
        st.markdown("---")
        
        recommendation_text = {
            "green": "✅ Nguy cơ thấp - Điều trị tiêu chuẩn, theo dõi chặt",
            "orange": "⚠️ Nguy cơ trung bình - Điều trị tích cực, cân nhắc ICU",
            "red": "🚨 Nguy cơ cao - Điều trị hồi sức tích cực, ICU ngay"
        }[result["color"]]
        
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>📋 Khuyến cáo</h3>
            <p style='font-size: 1.1em;'>{recommendation_text}</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📊 Bảng phân loại"):
            st.markdown("""
            | Điểm | Nguy cơ | Tử vong 30 ngày |
            |:----:|:--------|:----------------|
            | 0-1 | Thấp | 1-5% |
            | 2-3 | Trung bình | 6-20% |
            | 4-5 | Cao | 20-40% |
            | ≥6 | Rất cao | >40% |
            """)


if __name__ == "__main__":
    render()

