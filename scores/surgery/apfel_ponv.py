"""
Apfel PONV Risk Score Calculator
Nguy cơ buồn nôn nôn sau mổ (Postoperative Nausea and Vomiting)
"""

import streamlit as st
from scores.utils.anesthesia_validation import validate_ponv_risk_factors


def calculate_apfel_ponv(female, non_smoker, history_ponv, opioids):
    """
    Tính điểm Apfel PONV Risk Score
    
    Parameters:
    - female: Nữ giới
    - non_smoker: Không hút thuốc
    - history_ponv: Tiền sử PONV hoặc say tàu xe
    - opioids: Dùng opioid sau mổ
    
    Returns:
    - dict với risk_score, risk_percentage, và recommendations
    """
    risk_factors = sum([female, non_smoker, history_ponv, opioids])
    
    # Risk percentages based on Apfel et al. 1999
    risk_percentages = {
        0: 10,   # 10% risk
        1: 21,   # 21% risk
        2: 39,   # 39% risk
        3: 61,   # 61% risk
        4: 79    # 79% risk
    }
    
    risk_pct = risk_percentages.get(risk_factors, 10)
    
    # Recommendations
    if risk_factors == 0:
        recommendation = "Nguy cơ thấp - Không cần dự phòng thường quy"
        prophylaxis = "Không cần thiết"
    elif risk_factors == 1:
        recommendation = "Nguy cơ trung bình - Cân nhắc dự phòng"
        prophylaxis = "Có thể dùng 1 thuốc chống nôn (ondansetron, dexamethasone, hoặc droperidol)"
    elif risk_factors == 2:
        recommendation = "Nguy cơ cao - Nên dự phòng"
        prophylaxis = "Dùng 2 thuốc chống nôn kết hợp (ondansetron + dexamethasone)"
    else:  # 3-4 factors
        recommendation = "Nguy cơ rất cao - Bắt buộc dự phòng đa thuốc"
        prophylaxis = "Dùng 2-3 thuốc chống nôn kết hợp:\n- Ondansetron 4mg IV\n- Dexamethasone 4-8mg IV\n- Droperidol 0.625-1.25mg IV (nếu không chống chỉ định)\n- Cân nhắc TIVA (Total Intravenous Anesthesia) thay vì gây mê hô hấp"
    
    return {
        "risk_factors": risk_factors,
        "risk_percentage": risk_pct,
        "recommendation": recommendation,
        "prophylaxis": prophylaxis
    }


def render():
    """Render Apfel PONV Risk Score interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🤢 Apfel PONV Risk Score</h2>
    <p style='text-align: center;'><em>Nguy cơ buồn nôn nôn sau mổ (Postoperative Nausea and Vomiting)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Apfel PONV Risk Score"):
        st.markdown("""
        **Apfel PONV Risk Score** là thang điểm đơn giản và hiệu quả để dự đoán nguy cơ 
        buồn nôn nôn sau mổ (PONV), giúp bác sĩ gây mê quyết định chiến lược dự phòng.
        
        **4 yếu tố nguy cơ:**
        1. **Nữ giới** - Nguy cơ cao hơn nam giới
        2. **Không hút thuốc** - Người hút thuốc có nguy cơ thấp hơn
        3. **Tiền sử PONV hoặc say tàu xe** - Yếu tố dự đoán mạnh nhất
        4. **Dùng opioid sau mổ** - Opioid làm tăng nguy cơ PONV
        
        **Nguy cơ theo số yếu tố:**
        - **0 yếu tố:** 10% nguy cơ
        - **1 yếu tố:** 21% nguy cơ
        - **2 yếu tố:** 39% nguy cơ
        - **3 yếu tố:** 61% nguy cơ
        - **4 yếu tố:** 79% nguy cơ
        
        **Khuyến nghị:**
        - ≥2 yếu tố: Nên dự phòng với 2 thuốc chống nôn
        - ≥3 yếu tố: Dự phòng đa thuốc + cân nhắc TIVA
        
        **Reference:** Apfel CC, et al. A simplified risk score for predicting postoperative nausea and vomiting. 
        Anesthesiology. 1999;91(3):693-700.
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá 4 yếu tố nguy cơ")
    
    # Risk factors
    female = st.checkbox("1️⃣ Nữ giới", key="apfel_female")
    non_smoker = st.checkbox("2️⃣ Không hút thuốc", key="apfel_nonsmoker")
    history_ponv = st.checkbox("3️⃣ Tiền sử PONV hoặc say tàu xe", key="apfel_history")
    opioids = st.checkbox("4️⃣ Dùng opioid sau mổ", key="apfel_opioids")
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm Apfel PONV", type="primary", use_container_width=True):
        # Validation
        is_valid, error_msg = validate_ponv_risk_factors(female, non_smoker, history_ponv, opioids)
        
        if not is_valid:
            st.error(f"❌ Lỗi: {error_msg}")
            return
        
        try:
            result = calculate_apfel_ponv(female, non_smoker, history_ponv, opioids)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Số yếu tố nguy cơ", f"{result['risk_factors']}/4")
            
            with col2:
                st.metric("Nguy cơ PONV", f"{result['risk_percentage']}%")
            
            st.markdown("---")
            
            # Risk interpretation
            if result['risk_factors'] == 0:
                st.success(f"**{result['recommendation']}**")
            elif result['risk_factors'] == 1:
                st.info(f"**{result['recommendation']}**")
            elif result['risk_factors'] == 2:
                st.warning(f"**{result['recommendation']}**")
            else:
                st.error(f"**{result['recommendation']}**")
            
            st.markdown("---")
            
            st.subheader("💊 Khuyến nghị dự phòng")
            st.markdown(f"""
            {result['prophylaxis']}
            """)
            
            st.markdown("---")
            
            # Additional information
            with st.expander("📚 Thông tin bổ sung"):
                st.markdown("""
            **Thuốc chống nôn thường dùng:**
            
            1. **Ondansetron (5-HT₃ antagonist)**
               - Liều: 4mg IV trước khi kết thúc gây mê
               - Tác dụng: 4-6 giờ
               - Lưu ý: Có thể gây QT kéo dài
            
            2. **Dexamethasone (Corticosteroid)**
               - Liều: 4-8mg IV khi bắt đầu gây mê
               - Tác dụng: 24 giờ
               - Lưu ý: Có thể tăng đường huyết
            
            3. **Droperidol (Dopamine antagonist)**
               - Liều: 0.625-1.25mg IV
               - Tác dụng: 6-8 giờ
               - Lưu ý: Có thể gây QT kéo dài, cần ECG monitoring
            
            4. **Metoclopramide (Prokinetic)**
               - Liều: 10mg IV
               - Tác dụng: 4-6 giờ
               - Lưu ý: Ít hiệu quả hơn các thuốc trên
            
            **Chiến lược gây mê:**
            - Cân nhắc TIVA (Total Intravenous Anesthesia) thay vì gây mê hô hấp
            - Tránh N₂O (nitrous oxide) - làm tăng nguy cơ PONV
            - Đảm bảo đủ dịch truyền (giảm nguy cơ PONV)
            """)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return

