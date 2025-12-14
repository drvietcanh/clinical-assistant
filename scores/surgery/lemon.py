"""
LEMON Assessment Calculator
Đánh giá đường thở khó (Look, Evaluate, Mallampati, Obstruction, Neck mobility)
"""

import streamlit as st


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
    
    st.subheader("📝 Đánh giá 5 thành phần LEMON")
    
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
    
    if st.button("🔍 Tính toán", type="primary", use_container_width=True):
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

