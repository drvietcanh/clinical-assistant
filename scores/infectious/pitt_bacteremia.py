"""
Pitt Bacteremia Score Calculator
Tiên lượng nhiễm khuẩn huyết
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================
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
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'pitt_bacteremia':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Pitt Bacteremia Score')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
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
            title="Điểm Từng Thành phần",
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
        
        # Prepare data for history and share
        inputs_dict = {
            "Temperature": temp,
            "Hypotension": hypotension,
            "Ventilator": ventilator,
            "Cardiac Arrest": cardiac_arrest,
            "Mental Status": mental_status
        }
        
        results_dict = {
            "Pitt Bacteremia Score": f"{result['total_score']}",
            "Risk Level": result['risk_level'],
            "Mortality": result['mortality']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="Pitt Bacteremia Score",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="Pitt Bacteremia Score"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="pitt_bacteremia",
            calculator_name="Pitt Bacteremia Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="pitt_bacteremia",
            calculator_name="Pitt Bacteremia Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="pitt_bacteremia", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="pitt_bacteremia",
            calculator_name="Pitt Bacteremia Score",
            category="Nhiễm khuẩn",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("Pitt Bacteremia Score")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()

