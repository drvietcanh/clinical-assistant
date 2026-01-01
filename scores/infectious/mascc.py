"""
MASCC Risk Index Calculator
Nguy cơ biến chứng trong sốt giảm bạch cầu hạt
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================
from components.ui.scoring import render_score_result, render_score_breakdown, render_recommendation_box

from scores.utils.validation import validate_age



def calculate_mascc(burden, hypotension, copd, solid_tumor_fungal, dehydration, outpatient, age):
    """Tính MASCC Risk Index"""
    total = burden + hypotension + copd + solid_tumor_fungal + dehydration + outpatient + age
    
    if total >= 21:
        risk = "Thấp"
        mortality = "< 1-5%"
        management = "Có thể điều trị ngoại trú với kháng sinh uống"
        color = COLORS["success"]
        icon = "✅"
    else:
        risk = "Cao"
        mortality = "> 10-20%"
        management = "Cần nhập viện, kháng sinh tĩnh mạch"
        color = COLORS["error"]
        icon = "🚨"
    
    return {
        "total_score": total,
        "risk_level": risk,
        "mortality": mortality,
        "management": management,
        "color": color,
        "icon": icon
    }


def render():
    """Render MASCC Risk Index interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'mascc':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'MASCC Risk Index')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🦠 MASCC Risk Index</h2>
    <p style='text-align: center;'><em>Nguy cơ biến chứng sốt giảm bạch cầu hạt (Febrile Neutropenia)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về MASCC"):
        st.markdown("""
        **MASCC (Multinational Association for Supportive Care in Cancer) Risk Index** 
        đánh giá nguy cơ biến chứng nghiêm trọng ở bệnh nhân ung thư có sốt giảm bạch cầu hạt.
        
        **Sốt giảm bạch cầu hạt:**
        - Nhiệt độ ≥ 38.3°C hoặc ≥ 38°C trong > 1 giờ
        - Số lượng bạch cầu hạt (ANC) < 500/µL
        
        **Mục đích:** Phân loại nguy cơ để quyết định điều trị nội trú hoặc ngoại trú
        
        **Tiêu chuẩn:**
        - ≥ 21 điểm: Nguy cơ thấp → Có thể ngoại trú
        - < 21 điểm: Nguy cơ cao → Nhập viện
        """)
    
    st.markdown("---")
    st.subheader("📝 Đánh giá Các Yếu tố")
    
    burden = st.radio(
        "Mức độ triệu chứng nhiễm trùng",
        options=[5, 3, 0],
        format_func=lambda x: {5: "5 điểm - Không/nhẹ", 3: "3 điểm - Trung bình", 0: "0 điểm - Nặng"}[x]
    )
    
    hypotension = st.radio(
        "Hạ huyết áp (SBP < 90)",
        options=[0, 5],
        format_func=lambda x: "5 điểm - Không" if x == 5 else "0 điểm - Có"
    )
    
    copd = st.radio(
        "COPD (Bệnh phổi tắc nghẽn mạn)",
        options=[0, 4],
        format_func=lambda x: "4 điểm - Không" if x == 4 else "0 điểm - Có"
    )
    
    solid_tumor_fungal = st.radio(
        "U đặc không có nhiễm nấm trước đó",
        options=[0, 4],
        format_func=lambda x: "4 điểm - Có (U đặc, không nhiễm nấm)" if x == 4 else "0 điểm - Không"
    )
    
    dehydration = st.radio(
        "Mất nước cần truyền tĩnh mạch",
        options=[0, 3],
        format_func=lambda x: "3 điểm - Không" if x == 3 else "0 điểm - Có"
    )
    
    outpatient = st.radio(
        "Khởi phát khi đang ngoại trú",
        options=[0, 3],
        format_func=lambda x: "3 điểm - Có" if x == 3 else "0 điểm - Không (đang nội trú)"
    )
    
    
    # Age Helper
    with st.expander("🧮 Hỗ trợ chọn Tuổi"):
         col_age1, col_age2 = st.columns(2)
         with col_age1:
              mascc_age_val = st.number_input("Nhập tuổi (năm)", 0, 120, 50, key="mascc_age_num")
         with col_age2:
              if mascc_age_val < 60:
                   st.success(f"✅ Tuổi {mascc_age_val} < 60 (2 điểm)")
                   mascc_age_auto = 0 # Index 0 is "2 points - Yes" (Wait, format_func says options=[0, 2], index 0 is val 0?)
                   # Let's check options below: options=[0, 2]
                   # format_func: x=2 "2 điểm...", x=0 "0 điểm..."
                   # So if < 60, we want value 2.
                   # options=[0, 2]. So index of 2 is 1. Index of 0 is 0.
                   # Wait, the radio returns the value.
                   pass
              else:
                   st.warning(f"⚠️ Tuổi {mascc_age_val} ≥ 60 (0 điểm)")
                   pass
         
         if st.button("Áp dụng tuổi"):
              st.session_state['mascc_age_auto'] = 2 if mascc_age_val < 60 else 0
              st.rerun()

    # Determine default
    default_age_val = 0 # Default is "0 điểm" (>= 60)
    if 'mascc_age_auto' in st.session_state:
         default_age_val = st.session_state['mascc_age_auto']
         
    # Options are [0, 2]. 
    # If default is 2, index is 1. If 0, index is 0.
    idx_age = 1 if default_age_val == 2 else 0

    age = st.radio(
        "Tuổi < 60",
        options=[0, 2],
        index=idx_age,
        format_func=lambda x: "2 điểm - Có (< 60 tuổi)" if x == 2 else "0 điểm - Không (≥ 60 tuổi)"
    )

    
    st.markdown("---")
    
    if st.button("🔬 Tính MASCC Score", type="primary", use_container_width=True):
        result = calculate_mascc(burden, hypotension, copd, solid_tumor_fungal, dehydration, outpatient, age)
        
        st.markdown("## 📊 Kết quả")
        
        # Use render_score_result for main score display
        render_score_result(
            title="MASCC Risk Index",
            score=result['total_score'],
            interpretation=f"Nguy cơ: {result['risk_level']}",
            mortality=f"Tử vong: {result['mortality']}",
            color=result['color'],
            icon=result['icon'],
            size="large"
        )
        
        # Use render_score_breakdown for component scores
        render_score_breakdown(
            title="Điểm Từng Thành phần",
            subscores={
                "Mức độ triệu chứng": burden,
                "Hạ huyết áp": hypotension,
                "COPD": copd,
                "U đặc không nhiễm nấm": solid_tumor_fungal,
                "Mất nước": dehydration,
                "Khởi phát ngoại trú": outpatient,
                "Tuổi < 60": age
            },
            total_score=result['total_score']
        )
        
        st.markdown("---")
        
        render_recommendation_box(
            title="Quản lý khuyến cáo",
            content=result['management'],
            type="success" if result["color"] == COLORS["success"] else "error"
        )

        
        if result["total_score"] >= 21:
            st.success("""
            ✅ **Nguy cơ thấp - Cân nhắc điều trị ngoại trú**
            
            **Tiêu chuẩn điều trị ngoại trú:**
            - MASCC ≥ 21
            - Bệnh nhân ổn định, không biến chứng
            - Có khả năng tuân thủ, tái khám
            - Kháng sinh: Ciprofloxacin + Amoxicillin-clavulanate
            - Theo dõi sát hàng ngày
            """)
        else:
            st.error("""
            🚨 **Nguy cơ cao - Cần nhập viện**
            
            **Quản lý:**
            - Nhập viện ngay
            - Kháng sinh phổ rộng tĩnh mạch trong 1 giờ
            - Nuôi cấy máu, nước tiểu trước khi kháng sinh
            - G-CSF nếu nguy cơ cao
            - Theo dõi ICU nếu cần
            """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Burden": burden,
            "Hypotension": hypotension,
            "COPD": copd,
            "Solid Tumor/Fungal": solid_tumor_fungal,
            "Dehydration": dehydration,
            "Outpatient": outpatient,
            "Age < 60": age
        }
        
        results_dict = {
            "MASCC Score": f"{result['total_score']}",
            "Risk Level": result['risk_level'],
            "Mortality": result['mortality'],
            "Management": result['management']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="MASCC Risk Index",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="MASCC Risk Index"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="mascc",
            calculator_name="MASCC Risk Index",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="mascc",
            calculator_name="MASCC Risk Index",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="mascc", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="mascc",
            calculator_name="MASCC Risk Index",
            category="Nhiễm khuẩn",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("MASCC Risk Index")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()

