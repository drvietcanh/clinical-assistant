"""
Gupta Perioperative Cardiac Risk Index Calculator
Đánh giá nguy cơ tim mạch trong phẫu thuật không tim
"""

import streamlit as st


def calculate_gupta_cardiac(age, history_cad, history_chf, history_cva, diabetes_insulin, creatinine):
    """
    Tính điểm Gupta Perioperative Cardiac Risk Index
    
    Parameters:
    - age: Tuổi (0=<60, 1=60-74, 2=≥75)
    - history_cad: Tiền sử bệnh mạch vành (0=no, 1=yes)
    - history_chf: Tiền sử suy tim (0=no, 1=yes)
    - history_cva: Tiền sử đột quỵ/TIA (0=no, 1=yes)
    - diabetes_insulin: Đái tháo đường dùng insulin (0=no, 1=yes)
    - creatinine: Creatinine (0=<1.5, 1=1.5-1.9, 2=≥2.0)
    
    Returns:
    - dict với risk_score, risk_percentage, và interpretation
    """
    risk_score = age + history_cad + history_chf + history_cva + diabetes_insulin + creatinine
    
    # Risk percentages based on Gupta et al. 2011
    if risk_score == 0:
        risk_pct = 0.4
        risk_level = "Nguy cơ rất thấp"
        color = "green"
    elif risk_score == 1:
        risk_pct = 0.9
        risk_level = "Nguy cơ thấp"
        color = "green"
    elif risk_score == 2:
        risk_pct = 2.0
        risk_level = "Nguy cơ trung bình"
        color = "orange"
    elif risk_score == 3:
        risk_pct = 5.4
        risk_level = "Nguy cơ cao"
        color = "orange"
    elif risk_score == 4:
        risk_pct = 11.0
        risk_level = "Nguy cơ rất cao"
        color = "red"
    else:  # ≥5
        risk_pct = 20.0
        risk_level = "Nguy cơ cực cao"
        color = "red"
    
    return {
        "risk_score": risk_score,
        "risk_percentage": risk_pct,
        "risk_level": risk_level,
        "color": color
    }


def render():
    """Render Gupta Cardiac Risk Index interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>❤️ Gupta Perioperative Cardiac Risk Index</h2>
    <p style='text-align: center;'><em>Đánh giá nguy cơ tim mạch trong phẫu thuật không tim</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Gupta Cardiac Risk Index"):
        st.markdown("""
        **Gupta Perioperative Cardiac Risk Index** là thang điểm đánh giá nguy cơ biến chứng tim mạch
        trong phẫu thuật không tim, được phát triển từ NSQIP database.
        
        **6 yếu tố nguy cơ:**
        
        1. **Tuổi**
           - 0 điểm: <60 tuổi
           - 1 điểm: 60-74 tuổi
           - 2 điểm: ≥75 tuổi
        
        2. **Tiền sử bệnh mạch vành (CAD)**
           - 0 điểm: Không
           - 1 điểm: Có (nhồi máu cơ tim, đặt stent, CABG)
        
        3. **Tiền sử suy tim (CHF)**
           - 0 điểm: Không
           - 1 điểm: Có
        
        4. **Tiền sử đột quỵ/TIA**
           - 0 điểm: Không
           - 1 điểm: Có
        
        5. **Đái tháo đường dùng insulin**
           - 0 điểm: Không hoặc không dùng insulin
           - 1 điểm: Có và đang dùng insulin
        
        6. **Creatinine**
           - 0 điểm: <1.5 mg/dL
           - 1 điểm: 1.5-1.9 mg/dL
           - 2 điểm: ≥2.0 mg/dL
        
        **Nguy cơ biến chứng tim mạch:**
        - **0 điểm:** 0.4% nguy cơ
        - **1 điểm:** 0.9% nguy cơ
        - **2 điểm:** 2.0% nguy cơ
        - **3 điểm:** 5.4% nguy cơ
        - **4 điểm:** 11.0% nguy cơ
        - **≥5 điểm:** 20.0% nguy cơ
        
        **Biến chứng tim mạch:**
        - Nhồi máu cơ tim
        - Suy tim
        - Loạn nhịp tim nghiêm trọng
        - Tử vong do tim mạch
        
        **So sánh với RCRI:**
        - Gupta: Dựa trên NSQIP database, chính xác hơn
        - RCRI: Đơn giản hơn, vẫn được dùng rộng rãi
        
        **Reference:** Gupta PK, et al. Development and validation of a risk calculator 
        for prediction of cardiac risk after surgery. Circulation. 2011;124(4):381-7.
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá 6 yếu tố nguy cơ")
    
    # Age
    st.markdown("### 1️⃣ Tuổi")
    age = st.radio(
        "Tuổi:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - <60 tuổi",
            1: "1 điểm - 60-74 tuổi",
            2: "2 điểm - ≥75 tuổi"
        }[x],
        key="gupta_age",
        horizontal=False
    )
    
    # History CAD
    st.markdown("### 2️⃣ Tiền sử bệnh mạch vành (CAD)")
    history_cad = st.checkbox(
        "Có tiền sử bệnh mạch vành (nhồi máu cơ tim, đặt stent, CABG)",
        key="gupta_cad"
    )
    
    # History CHF
    st.markdown("### 3️⃣ Tiền sử suy tim (CHF)")
    history_chf = st.checkbox(
        "Có tiền sử suy tim",
        key="gupta_chf"
    )
    
    # History CVA
    st.markdown("### 4️⃣ Tiền sử đột quỵ/TIA")
    history_cva = st.checkbox(
        "Có tiền sử đột quỵ hoặc TIA",
        key="gupta_cva"
    )
    
    # Diabetes insulin
    st.markdown("### 5️⃣ Đái tháo đường dùng insulin")
    diabetes_insulin = st.checkbox(
        "Đái tháo đường và đang dùng insulin",
        key="gupta_diabetes"
    )
    
    # Creatinine
    st.markdown("### 6️⃣ Creatinine")
    creatinine = st.radio(
        "Creatinine:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "0 điểm - <1.5 mg/dL",
            1: "1 điểm - 1.5-1.9 mg/dL",
            2: "2 điểm - ≥2.0 mg/dL"
        }[x],
        key="gupta_creatinine",
        horizontal=False
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm Gupta Cardiac Risk", type="primary", use_container_width=True):
        try:
            result = calculate_gupta_cardiac(age, history_cad, history_chf, history_cva, diabetes_insulin, creatinine)
            
            # Display results
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Risk Score", f"{result['risk_score']}")
            
            with col2:
                st.metric("Nguy cơ", result['risk_level'])
            
            with col3:
                st.metric("Biến chứng tim mạch", f"{result['risk_percentage']:.1f}%")
            
            st.markdown("---")
            
            # Risk interpretation
            if result['color'] == "green":
                st.success(f"**{result['risk_level']}** - Tỷ lệ biến chứng tim mạch: {result['risk_percentage']:.1f}%")
            elif result['color'] == "orange":
                st.warning(f"**{result['risk_level']}** - Tỷ lệ biến chứng tim mạch: {result['risk_percentage']:.1f}%")
            else:
                st.error(f"**{result['risk_level']}** - Tỷ lệ biến chứng tim mạch: {result['risk_percentage']:.1f}%")
            
            st.markdown("---")
            
            # Additional information
            with st.expander("📚 Khuyến nghị theo nguy cơ"):
                st.markdown("""
                **Nguy cơ thấp (0-1 điểm):**
                - Phẫu thuật an toàn
                - Theo dõi thường quy
                
                **Nguy cơ trung bình (2 điểm):**
                - Cân nhắc đánh giá tim mạch trước mổ
                - Theo dõi sát sau mổ
                
                **Nguy cơ cao (3-4 điểm):**
                - Đánh giá tim mạch trước mổ (ECG, siêu âm tim)
                - Có thể cần tư vấn tim mạch
                - Theo dõi sát sau mổ, có thể cần monitoring
                
                **Nguy cơ rất cao (≥5 điểm):**
                - Bắt buộc đánh giá tim mạch đầy đủ
                - Tư vấn tim mạch
                - Cân nhắc hoãn phẫu thuật nếu có thể
                - Theo dõi tích cực sau mổ, có thể cần ICU
                """)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return

