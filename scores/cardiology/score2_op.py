"""
SCORE2-OP Calculator
=====================

5-10 year cardiovascular disease risk for older persons (≥70 years)

Reference:
- SCORE2-OP working group. SCORE2-OP risk prediction algorithms: 
  estimated 10-year risk of cardiovascular disease in Europe in older persons.
  Eur Heart J. 2021;42(25):2455-2467.

SCORE2-OP predicts 5 and 10-year risk of CVD in people ≥70 years:
- Fatal and non-fatal myocardial infarction
- Fatal and non-fatal stroke

Note: Shorter time horizons (5 years) more relevant for elderly with limited life expectancy.
"""

import streamlit as st
import math


def calculate_score2_op(
    age: int,
    is_female: bool,
    is_smoker: bool,
    sbp: float,
    total_chol: float,
    hdl_chol: float = None,
    time_horizon: int = 10
) -> dict:
    """
    Calculate SCORE2-OP for older persons (≥70 years)
    
    Simplified estimation for moderate risk regions.
    
    Args:
        age: Age (≥70 years)
        is_female: Female sex
        is_smoker: Current smoker
        sbp: Systolic blood pressure
        total_chol: Total cholesterol (mmol/L)
        hdl_chol: HDL cholesterol (mmol/L)
        time_horizon: 5 or 10 years
    
    Returns:
        Dictionary with risk percentage and category
    """
    
    # Cap age at 95 for calculation
    age_calc = min(age, 95)
    
    # Calculate non-HDL
    if hdl_chol is not None:
        non_hdl = total_chol - hdl_chol
    else:
        non_hdl = total_chol - 1.3
    
    # Simplified risk calculation for elderly
    # Risk is generally higher in elderly, but benefits of treatment need consideration
    
    # Age factor (exponential increase)
    age_factor = math.exp((age_calc - 70) * 0.08)
    
    # Sex factor (converges in elderly)
    sex_factor = 0.75 if is_female else 1.0
    
    # Smoking (smaller relative effect in elderly but still important)
    smoking_factor = 1.6 if is_smoker else 1.0
    
    # SBP contribution
    sbp_factor = 1.0 + ((sbp - 140) / 20) * 0.25 if sbp > 140 else 0.9
    
    # Cholesterol contribution (smaller effect in elderly)
    chol_factor = 1.0 + ((non_hdl - 3.0) / 1) * 0.12 if non_hdl > 3.0 else 0.85
    
    # Baseline risk for elderly
    baseline_risk = 8.0  # Higher baseline for elderly
    
    # Calculate risk
    risk_calculated = baseline_risk * age_factor * sex_factor * smoking_factor * sbp_factor * chol_factor
    
    # Adjust for time horizon
    if time_horizon == 5:
        risk_calculated = risk_calculated * 0.55  # Approximately 55% of 10-year risk
    
    # Cap risk
    risk_calculated = min(risk_calculated, 60.0)
    
    # Risk categories for elderly (more liberal given competing risks)
    if risk_calculated < 7.5:
        risk_category = "Nguy cơ THẤP-TRUNG BÌNH"
        risk_class = "LOW_MODERATE"
        color = "🟢"
        recommendation = f"""
        **🟢 Nguy cơ tim mạch THẤP-TRUNG BÌNH (<7.5% trong {time_horizon} năm):**
        
        **Khuyến cáo cho người cao tuổi:**
        
        1. **Lối sống:**
           - Chế độ ăn lành mạnh (Địa Trung Hải)
           - Hoạt động thể lực vừa phải (theo khả năng)
           - Duy trì cân nặng hợp lý
           - Giảm muối (<5g/ngày)
        
        2. **Thuốc:**
           - **Statin:** Cân nhắc nếu đã dùng trước đó
           - Không bắt đầu mới nếu tuổi thọ dự kiến <5 năm
           - Ưu tiên điều trị các bệnh khác quan trọng hơn
        
        3. **Theo dõi:**
           - Kiểm tra định kỳ mỗi 1-2 năm
           - Đánh giá lại khi có thay đổi sức khỏe
        
        **Lưu ý:** Ở tuổi cao, chất lượng cuộc sống quan trọng hơn số lượng thuốc.
        """
    elif risk_calculated < 15:
        risk_category = "Nguy cơ CAO"
        risk_class = "HIGH"
        color = "🟡"
        recommendation = f"""
        **🟡 Nguy cơ tim mạch CAO (7.5-15% trong {time_horizon} năm):**
        
        **Khuyến cáo:**
        
        1. **Statin:**
           - Khuyến cáo nếu tuổi thọ dự kiến >5 năm
           - Moderate intensity statin
           - Cân nhắc rủi ro/lợi ích cá nhân
           - Theo dõi tác dụng phụ (đau cơ, nhầm lẫn)
        
        2. **Huyết áp:**
           - Mục tiêu <140/90 mmHg (linh hoạt hơn người trẻ)
           - Tránh hạ BP quá thấp (nguy cơ ngã)
           - Đo BP ngồi và đứng (loại trừ hypotension tư thế)
        
        3. **Bỏ thuốc lá:**
           - Vẫn có lợi ngay cả ở tuổi cao
           - Hỗ trợ cai thuốc
        
        4. **Theo dõi:**
           - 6-12 tháng/lần
           - Đánh giá chức năng nhận thức, ngã
        
        **Mục tiêu (linh hoạt):**
        - LDL-C <2.6 mmol/L (100 mg/dL) nếu dung nạp được
        - BP <140/90 mmHg
        """
    else:
        risk_category = "Nguy cơ RẤT CAO"
        risk_class = "VERY_HIGH"
        color = "🟠"
        recommendation = f"""
        **🟠 Nguy cơ tim mạch RẤT CAO (≥15% trong {time_horizon} năm):**
        
        **Khuyến cáo (cân nhắc cá nhân hóa):**
        
        1. **Statin:**
           - Moderate-intensity khuyến cáo
           - High-intensity nếu dung nạp tốt
           - Cân nhắc thêm ezetimibe nếu LDL cao
           - **Lưu ý:** Ngừng nếu tác dụng phụ đáng kể
        
        2. **Huyết áp:**
           - Mục tiêu <140/90 mmHg
           - Có thể <130/80 nếu dung nạp tốt
           - **TRÁNH** <120/70 (nguy cơ ngã, suy thận)
        
        3. **Aspirin:**
           - Xem xét nếu không có chống chỉ định
           - Cân nhắc nguy cơ chảy máu (đặc biệt nếu >80 tuổi)
        
        4. **Theo dõi sát:**
           - 3-6 tháng/lần
           - Đánh giá toàn diện: nhận thức, chức năng, ngã
           - Tái đánh giá khi bệnh nền thay đổi
        
        5. **Cân nhắc quan trọng:**
           - Tuổi thọ dự kiến
           - Chất lượng cuộc sống
           - Số lượng thuốc đang dùng (polypharmacy)
           - Sở thích bệnh nhân
           - Chi phí/lợi ích
        
        **Mục tiêu (cá nhân hóa):**
        - LDL-C <1.8 mmol/L (70 mg/dL) nếu đạt được
        - BP <140/90 (hoặc <130/80 nếu dung nạp)
        
        **⚠️ Quan trọng:** Tránh overtreatment ở người rất cao tuổi!
        """
    
    return {
        'risk': risk_calculated,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'color': color,
        'recommendation': recommendation,
        'non_hdl': non_hdl,
        'time_horizon': time_horizon
    }


def render():
    """Render SCORE2-OP calculator"""
    
    st.title("👴 SCORE2-OP - ESC 2021")
    st.markdown("**Đánh giá nguy cơ tim mạch ở người cao tuổi (≥70 tuổi)**")
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **SCORE2-OP (Older Persons)** dành cho người ≥70 tuổi:
        - Dự đoán nguy cơ CVD 5 hoặc 10 năm
        - Đặc biệt cho elderly: competing risks, life expectancy
        - Cân nhắc quality of life vs treatment burden
        
        ### 🎯 Yếu tố nguy cơ
        
        Giống SCORE2:
        1. Tuổi (≥70)
        2. Giới tính
        3. Hút thuốc lá
        4. Huyết áp tâm thu
        5. Cholesterol (non-HDL)
        
        ### ⏱️ Thời gian dự đoán
        
        - **10 năm:** Tiêu chuẩn
        - **5 năm:** Phù hợp hơn nếu tuổi thọ dự kiến hạn chế
        
        ### 🧓 Cân Nhắc Đặc Biệt Ở Người cao tuổi
        
        **Lợi ích điều trị:**
        - Giảm events (MI, stroke)
        - Cải thiện chức năng
        
        **Rủi ro điều trị:**
        - Polypharmacy (nhiều thuốc)
        - Tác dụng phụ (nhầm lẫn, ngã, rối loạn điện giải)
        - Chi phí
        - Giảm QoL
        
        **Yếu tố quyết định:**
        - Tuổi thọ dự kiến
        - Comorbidities
        - Frailty status
        - Cognitive function
        - Patient preferences
        
        ### 📊 Mục tiêu linh hoạt hơn
        
        Ở người cao tuổi, mục tiêu điều trị cần **CÁ NHÂN HÓA:**
        - LDL-C: <2.6 mmol/L thay vì <1.4-1.8
        - BP: <140/90 thay vì <130/80
        - HbA1c: <8% thay vì <7% (nếu DM)
        
        ### ⚠️ Khi KHÔNG Điều trị Tích Cực
        
        - Tuổi thọ dự kiến <3-5 năm
        - Frailty nặng
        - Dementia tiến triển
        - Bệnh nền nặng (ung thư giai đoạn cuối, etc.)
        - Bệnh nhân từ chối
        
        ### 📚 Tham khảo
        
        - SCORE2-OP working group. *Eur Heart J* 2021;42:2455-2467
        - ESC Guidelines 2021 on CVD prevention in clinical practice
        """)
    
    st.divider()
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Thông tin")
        age = st.number_input("Tuổi", 70, 100, 75, 1, format="%d", help="SCORE2-OP dành cho ≥70 tuổi")
        
        sex = st.radio("Giới tính", ["Nam", "Nữ"], horizontal=True)
        is_female = (sex == "Nữ")
        
        is_smoker = st.checkbox("**Đang hút thuốc lá**")
        
        time_horizon = st.radio(
            "**Thời gian dự đoán**",
            [10, 5],
            format_func=lambda x: f"{x} năm",
            help="5 năm phù hợp hơn nếu tuổi thọ dự kiến hạn chế"
        )
    
    with col2:
        st.markdown("#### 🩺 Sinh hiệu")
        sbp = st.number_input("Huyết áp tâm thu (mmHg)", 80, 220, 140, 1, format="%d")
    
    st.divider()
    
    # Cholesterol
    st.markdown("#### 🔬 Cholesterol")
    
    chol_unit = st.radio("Đơn vị", ["mmol/L", "mg/dL"], horizontal=True, index=0)
    
    col3, col4 = st.columns(2)
    
    with col3:
        if chol_unit == "mmol/L":
            total_chol = st.number_input("Total Cholesterol (mmol/L)", 2.0, 15.0, 5.5, 0.1, format="%.1f")
        else:
            total_chol_mg = st.number_input("Total Cholesterol (mg/dL)", 80.0, 600.0, 210.0, 1.0, format="%.0f")
            total_chol = total_chol_mg / 38.67
        st.caption(f"= {total_chol * 38.67:.0f} mg/dL")
    
    with col4:
        if chol_unit == "mmol/L":
            hdl_chol = st.number_input("HDL Cholesterol (mmol/L)", 0.5, 4.0, 1.4, 0.1, format="%.1f")
        else:
            hdl_chol_mg = st.number_input("HDL Cholesterol (mg/dL)", 20.0, 150.0, 55.0, 1.0, format="%.0f")
            hdl_chol = hdl_chol_mg / 38.67
        st.caption(f"= {hdl_chol * 38.67:.0f} mg/dL")
    
    st.divider()
    
    # Calculate
    if st.button("🧮 Tính Nguy cơ SCORE2-OP", type="primary", use_container_width=True):
        
        if age < 70:
            st.error("⚠️ SCORE2-OP dành cho người ≥70 tuổi. Sử dụng SCORE2 cho 40-69 tuổi.")
            return
        
        result = calculate_score2_op(
            age=age,
            is_female=is_female,
            is_smoker=is_smoker,
            sbp=sbp,
            total_chol=total_chol,
            hdl_chol=hdl_chol,
            time_horizon=time_horizon
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                f"**Nguy cơ {time_horizon} năm**",
                f"{result['risk']:.1f}%"
            )
            st.caption("Mắc CVD (MI + Stroke)")
        
        with col_r2:
            st.markdown(f"### {result['color']} {result['risk_category']}")
            st.caption(f"Dự đoán trong {time_horizon} năm tới")
        
        # Summary
        with st.expander("📋 Tóm Tắt", expanded=True):
            st.markdown(f"""
            - Tuổi: {age} tuổi
            - Giới tính: {sex}
            - Hút thuốc: {'Có' if is_smoker else 'Không'}
            - SBP: {sbp:.0f} mmHg
            - Total cholesterol: {total_chol:.1f} mmol/L ({total_chol * 38.67:.0f} mg/dL)
            - HDL: {hdl_chol:.1f} mmol/L ({hdl_chol * 38.67:.0f} mg/dL)
            - **Non-HDL: {result['non_hdl']:.1f} mmol/L ({result['non_hdl'] * 38.67:.0f} mg/dL)**
            """)
        
        # Recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo Cho Người cao tuổi")
        st.markdown(result['recommendation'])
        
        # Important considerations
        st.info("""
        **📌 Cân Nhắc Quan Trọng Ở Người cao tuổi:**
        
        1. **Tuổi thọ dự kiến:**
           - <3 năm: Ưu tiên QoL, giảm thiểu thuốc
           - 3-5 năm: Cân nhắc cá nhân
           - >5 năm: Điều trị phù hợp
        
        2. **Frailty:**
           - Robust: Điều trị tích cực
           - Pre-frail: Cân nhắc
           - Frail: Ưu tiên QoL
        
        3. **Polypharmacy:**
           - Đang dùng >5 thuốc → cân nhắc deprescribing
           - Tương tác thuốc
           - Tuân thủ điều trị
        
        4. **Nguy cơ ngã:**
           - Tránh hạ BP quá thấp
           - Tránh thuốc gây chóng mặt
        
        5. **Sở thích bệnh nhân:**
           - Thảo luận mục tiêu điều trị
           - Shared decision making
        """)
        
        st.warning("""
        ⚠️ **Lưu ý:**
        - Đây là công cụ hỗ trợ, không thay thế đánh giá toàn diện
        - Ở người cao tuổi: **QoL > Prolonging life**
        - Tránh overtreatment
        - Cá nhân hóa mục tiêu điều trị
        - Định kỳ tái đánh giá lợi ích/rủi ro
        """)
        
        st.session_state['score2_op_result'] = result
    
    # Quick reference
    with st.expander("📖 Nguyên tắc điều trị người cao tuổi"):
        st.markdown("""
        ### Start Low, Go Slow
        
        **Statin:**
        - Bắt đầu liều thấp (Atorvastatin 10 mg, Rosuvastatin 5 mg)
        - Tăng dần nếu dung nạp tốt
        - Theo dõi đau cơ, rối loạn nhận thức
        
        **Huyết áp:**
        - Mục tiêu <140/90 (không quá thấp)
        - Đo ngồi VÀ đứng
        - Tránh orthostatic hypotension
        
        ### Deprescribing
        
        **Xem xét ngừng thuốc nếu:**
        - Không còn chỉ định
        - Tác dụng phụ > lợi ích
        - Tuổi thọ dự kiến ngắn
        - Bệnh nhân muốn giảm thuốc
        
        ### Shared Decision Making
        
        Thảo luận với bệnh nhân/gia đình:
        - Mục tiêu điều trị
        - Lợi ích vs rủi ro
        - Chất lượng cuộc sống
        - Sở thích cá nhân
        """)
