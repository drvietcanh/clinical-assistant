"""
LEMON Assessment Calculator
Đánh giá đường thở khó (Look, Evaluate, Mallampati, Obstruction, Neck mobility)
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_lemon(look, evaluate, mallampati, obstruction, neck_mobility):
    """
    Tính điểm LEMON Assessment
    
    Parameters:
    - look: Look externally (0=normal, 1=abnormal)
    - evaluate: Evaluate 3-3-2 rule (0=pass, 1=fail)
    - mallampati: Mallampati class (0=I-II, 1=III-IV)
    - obstruction: Obstruction (0=no, 1=yes)
    - neck_mobility: Neck mobility (0=normal, 1=limited)
    
    Returns:
    - dict với total_score và interpretation
    """
    total = look + evaluate + mallampati + obstruction + neck_mobility
    
    # Interpretation
    if total == 0:
        risk = "Nguy cơ thấp"
        difficulty = "Đặt NKQ dễ dàng"
        recommendation = "Gây mê tiêu chuẩn"
        color = "green"
    elif total <= 2:
        risk = "Nguy cơ trung bình"
        difficulty = "Có thể đặt NKQ khó"
        recommendation = "Chuẩn bị dụng cụ đường thở khó, có bác sĩ gây mê giàu kinh nghiệm"
        color = "orange"
    else:  # ≥3
        risk = "Nguy cơ cao"
        difficulty = "Đặt NKQ khó - Cần chuẩn bị đặc biệt"
        recommendation = "Bắt buộc có bác sĩ gây mê giàu kinh nghiệm, chuẩn bị đầy đủ dụng cụ, cân nhắc đặt NKQ tỉnh"
        color = "red"
    
    return {
        "total_score": total,
        "risk": risk,
        "difficulty": difficulty,
        "recommendation": recommendation,
        "color": color
    }


def render():
    """Render LEMON Assessment interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'lemon':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🍋 LEMON Assessment</h2>
    <p style='text-align: center;'><em>Đánh giá đường thở khó (Look, Evaluate, Mallampati, Obstruction, Neck)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về LEMON Assessment"):
        st.markdown("""
        **LEMON Assessment** là công cụ đánh giá đường thở khó được sử dụng rộng rãi,
        đặc biệt trong cấp cứu và phẫu thuật.
        
        **5 thành phần LEMON:**
        1. **L - Look externally:** Nhìn bên ngoài (dị dạng, chấn thương, béo phì)
        2. **E - Evaluate 3-3-2 rule:** Đánh giá quy tắc 3-3-2
           - Mở miệng ≥3 ngón tay (≈4.5cm)
           - Khoảng cách hyoid-mentum ≥3 ngón tay (≈4.5cm)
           - Khoảng cách thyroid notch-mouth ≥2 ngón tay (≈3cm)
        3. **M - Mallampati:** Phân loại Mallampati (I-II vs III-IV)
        4. **O - Obstruction:** Tắc nghẽn đường thở (khối u, phù nề, dị vật)
        5. **N - Neck mobility:** Cử động cổ (bình thường vs hạn chế)
        
        **Điểm số:**
        - **0 điểm:** Nguy cơ thấp
        - **1-2 điểm:** Nguy cơ trung bình
        - **≥3 điểm:** Nguy cơ cao
        
        **Ưu điểm:**
        - Đơn giản, dễ nhớ
        - Nhanh chóng đánh giá
        - Phù hợp cấp cứu
        
        **Reference:** Reed MJ, et al. Can the airway assessment score predict 
        difficult intubation in the emergency department? Emerg Med J. 2007;24(2):99-100.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 5 thành phần LEMON")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="lemon",
            calculator_name="LEMON Assessment",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # L - Look
    st.markdown("### L - Look externally (Nhìn bên ngoài)")
    look = st.radio(
        "Có bất thường bên ngoài:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Bình thường (không có dị dạng, chấn thương, béo phì nặng)",
            1: "1 điểm - Bất thường (dị dạng mặt, chấn thương, béo phì nặng, râu dài)"
        }[x],
        key="lemon_look",
        horizontal=False
    )
    
    # E - Evaluate 3-3-2
    st.markdown("### E - Evaluate 3-3-2 rule")
    st.markdown("""
    **Quy tắc 3-3-2:**
    - **3 ngón:** Mở miệng ≥3 ngón tay (≈4.5cm)
    - **3 ngón:** Khoảng cách hyoid-mentum ≥3 ngón tay (≈4.5cm)
    - **2 ngón:** Khoảng cách thyroid notch-mouth ≥2 ngón tay (≈3cm)
    """)
    evaluate = st.radio(
        "Quy tắc 3-3-2:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Đạt cả 3 tiêu chuẩn",
            1: "1 điểm - Không đạt ≥1 tiêu chuẩn"
        }[x],
        key="lemon_evaluate",
        horizontal=False
    )
    
    # M - Mallampati
    st.markdown("### M - Mallampati Classification")
    mallampati = st.radio(
        "Phân loại Mallampati:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Class I-II (Dễ đặt NKQ)",
            1: "1 điểm - Class III-IV (Khó đặt NKQ)"
        }[x],
        key="lemon_mallampati",
        horizontal=False
    )
    st.caption("Xem Mallampati Classification calculator để đánh giá chi tiết")
    
    # O - Obstruction
    st.markdown("### O - Obstruction (Tắc nghẽn)")
    obstruction = st.radio(
        "Có tắc nghẽn đường thở:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Không có tắc nghẽn",
            1: "1 điểm - Có tắc nghẽn (khối u, phù nề, dị vật, chấn thương)"
        }[x],
        key="lemon_obstruction",
        horizontal=False
    )
    
    # N - Neck mobility
    st.markdown("### N - Neck mobility (Cử động cổ)")
    neck_mobility = st.radio(
        "Cử động cổ:",
        options=[0, 1],
        format_func=lambda x: {
            0: "0 điểm - Bình thường (duỗi cổ tốt)",
            1: "1 điểm - Hạn chế (không thể duỗi cổ đầy đủ)"
        }[x],
        key="lemon_neck",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm LEMON", type="primary", use_container_width=True):
        try:
            result = calculate_lemon(look, evaluate, mallampati, obstruction, neck_mobility)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Tổng điểm", f"{result['total_score']}/5")
            
            with col2:
                st.metric("Nguy cơ", result['risk'])
            
            st.markdown("---")
            
            # Risk interpretation
            if result['color'] == "green":
                st.success(f"**{result['risk']}** - {result['difficulty']}")
            elif result['color'] == "orange":
                st.warning(f"**{result['risk']}** - {result['difficulty']}")
            else:
                st.error(f"**{result['risk']}** - {result['difficulty']}")
            
            st.markdown("---")
            
            st.subheader("💡 Khuyến nghị")
            st.markdown(f"""
            {result['recommendation']}
            """)
            
            st.markdown("---")
            
            # Show which factors are present
            st.subheader("📋 Yếu tố nguy cơ hiện tại")
            factors_list = []
            if look == 1:
                factors_list.append("⚠️ L - Bất thường bên ngoài")
            if evaluate == 1:
                factors_list.append("⚠️ E - Không đạt quy tắc 3-3-2")
            if mallampati == 1:
                factors_list.append("⚠️ M - Mallampati III-IV")
            if obstruction == 1:
                factors_list.append("⚠️ O - Có tắc nghẽn đường thở")
            if neck_mobility == 1:
                factors_list.append("⚠️ N - Hạn chế cử động cổ")
            
            if factors_list:
                for factor in factors_list:
                    st.markdown(f"- {factor}")
            else:
                st.markdown("- ✅ Tất cả yếu tố bình thường")
            
            # Prepare data for history and share
            inputs_dict = {
                "L - Look": "Bất thường" if look == 1 else "Bình thường",
                "E - Evaluate 3-3-2": "Không đạt" if evaluate == 1 else "Đạt",
                "M - Mallampati": "III-IV" if mallampati == 1 else "I-II",
                "O - Obstruction": "Có" if obstruction == 1 else "Không",
                "N - Neck mobility": "Hạn chế" if neck_mobility == 1 else "Bình thường"
            }
            
            results_dict = {
                "Tổng điểm": f"{result['total_score']}/5",
                "Nguy cơ": result['risk'],
                "Độ khó": result['difficulty'],
                "Khuyến nghị": result['recommendation']
            }
            
            # Save to history
            # Export section
            render_export_section(
                title="LEMON Assessment",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="LEMON Assessment"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="lemon",
                calculator_name="LEMON Assessment",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="lemon",
                calculator_name="LEMON Assessment",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="lemon", show_actions=True)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("LEMON")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

