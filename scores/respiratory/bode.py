"""
BODE Index
==========

Multidimensional grading system for COPD prognosis

Reference:
- Celli BR, et al. The body-mass index, airflow obstruction, dyspnea, and exercise
  capacity index in chronic obstructive pulmonary disease. N Engl J Med. 2004;350(10):1005-1012.

BODE Components:
- B: Body mass index (BMI)
- O: Airflow Obstruction (FEV1% predicted)
- D: Dyspnea (mMRC scale)
- E: Exercise capacity (6-minute walk distance)

Total: 0-10 points

Clinical Utility:
- Predict mortality in COPD
- Better than FEV1 alone
- Guide management decisions
- Monitor disease progression
"""

import streamlit as st


def calculate_bode(
    bmi: float,
    fev1_percent: float,
    mmrc_dyspnea: int,
    walk_distance: int
) -> dict:
    """
    Calculate BODE Index
    
    Args:
        bmi: Body Mass Index
        fev1_percent: FEV1 % predicted
        mmrc_dyspnea: Modified MRC dyspnea scale (0-4)
        walk_distance: 6-minute walk distance (meters)
    
    Returns:
        Dictionary with BODE score, mortality risk, recommendations
    """
    
    score = 0
    details = []
    
    # BMI points
    if bmi <= 21:
        bmi_points = 1
        details.append(f"BMI = {bmi:.1f} → 1 điểm (≤21)")
    else:
        bmi_points = 0
        details.append(f"BMI = {bmi:.1f} → 0 điểm (>21)")
    score += bmi_points
    
    # FEV1 points
    if fev1_percent >= 65:
        fev1_points = 0
        details.append(f"FEV1 = {fev1_percent:.0f}% → 0 điểm (≥65%)")
    elif fev1_percent >= 50:
        fev1_points = 1
        details.append(f"FEV1 = {fev1_percent:.0f}% → 1 điểm (50-64%)")
    elif fev1_percent >= 36:
        fev1_points = 2
        details.append(f"FEV1 = {fev1_percent:.0f}% → 2 điểm (36-49%)")
    else:
        fev1_points = 3
        details.append(f"FEV1 = {fev1_percent:.0f}% → 3 điểm (≤35%)")
    score += fev1_points
    
    # mMRC dyspnea points
    mmrc_descriptions = [
        "0: Khó thở khi gắng sức nặng",
        "1: Khó thở khi đi nhanh/lên dốc",
        "2: Đi chậm hơn người cùng tuổi",
        "3: Dừng lại sau đi ~100m",
        "4: Quá khó thở để ra khỏi nhà"
    ]
    
    if mmrc_dyspnea <= 1:
        dyspnea_points = 0
        details.append(f"mMRC = {mmrc_dyspnea} → 0 điểm")
    elif mmrc_dyspnea == 2:
        dyspnea_points = 1
        details.append(f"mMRC = {mmrc_dyspnea} → 1 điểm")
    elif mmrc_dyspnea == 3:
        dyspnea_points = 2
        details.append(f"mMRC = {mmrc_dyspnea} → 2 điểm")
    else:  # mmrc_dyspnea == 4
        dyspnea_points = 3
        details.append(f"mMRC = {mmrc_dyspnea} → 3 điểm")
    score += dyspnea_points
    
    # 6-minute walk distance points
    if walk_distance >= 350:
        walk_points = 0
        details.append(f"6MWD = {walk_distance}m → 0 điểm (≥350m)")
    elif walk_distance >= 250:
        walk_points = 1
        details.append(f"6MWD = {walk_distance}m → 1 điểm (250-349m)")
    elif walk_distance >= 150:
        walk_points = 2
        details.append(f"6MWD = {walk_distance}m → 2 điểm (150-249m)")
    else:
        walk_points = 3
        details.append(f"6MWD = {walk_distance}m → 3 điểm (≤149m)")
    score += walk_points
    
    # Mortality risk interpretation
    if score <= 2:
        quartile = "Quartile 1"
        mortality_4yr = "~20%"
        risk_class = "LOW"
        color = "🟢"
        interpretation = "Nguy cơ THẤP"
        management = """
        **🟢 BODE 0-2 (Nguy cơ Thấp):**
        
        **Điều trị:**
        - LAMA hoặc LABA đơn độc
        - Bỏ thuốc lá (quan trọng nhất!)
        - Vaccine: Flu hàng năm, Pneumococcal
        - Phục hồi chức năng phổi
        - Tập thể dục thường xuyên
        
        **Theo dõi:**
        - FEV1 mỗi 6-12 tháng
        - Tái đánh giá BODE hàng năm
        - Đánh giá đợt cấp
        """
    elif score <= 4:
        quartile = "Quartile 2"
        mortality_4yr = "~30%"
        risk_class = "MODERATE"
        color = "🟡"
        interpretation = "Nguy cơ TRUNG BÌNH"
        management = """
        **🟡 BODE 3-4 (Nguy cơ Trung Bình):**
        
        **Điều trị:**
        - **LAMA + LABA combination**
        - ICS nếu có đợt cấp tái phát
        - Bỏ thuốc lá
        - Vaccine
        - **Phục hồi chức năng phổi BẮT BUỘC**
        - Dinh dưỡng (nếu BMI thấp)
        - Oxy liệu pháp nếu hypoxemia
        
        **Theo dõi:**
        - FEV1 mỗi 3-6 tháng
        - Đánh giá đợt cấp thường xuyên
        - Tái đánh giá BODE 6 tháng
        - Xem xét chương trình phục hồi
        """
    elif score <= 6:
        quartile = "Quartile 3"
        mortality_4yr = "~40-50%"
        risk_class = "HIGH"
        color = "🟠"
        interpretation = "Nguy cơ CAO"
        management = """
        **🟠 BODE 5-6 (Nguy cơ Cao):**
        
        **Điều trị:**
        - **Triple therapy: LAMA + LABA + ICS**
        - PDE4 inhibitor (Roflumilast) xem xét
        - Macrolide dài hạn nếu đợt cấp tái phát
        - **Oxy liệu pháp dài hạn** (LTOT) nếu:
          * PaO2 ≤55 mmHg
          * PaO2 56-59 + polycythemia/cor pulmonale
        - **Phục hồi chức năng tích cực**
        - Hỗ trợ dinh dưỡng
        - NIV nếu hypercapnia
        
        **Xem Xét:**
        - Phẫu thuật giảm thể tích phổi (LVRS) nếu phù hợp
        - Ghép phổi (nếu tuổi <65, không hút thuốc)
        
        **Theo dõi:**
        - FEV1 mỗi 3 tháng
        - ABG định kỳ
        - Đánh giá hypoxemia, hypercapnia
        - Tái đánh giá BODE 3-6 tháng
        """
    else:  # score 7-10
        quartile = "Quartile 4"
        mortality_4yr = ">60%"
        risk_class = "VERY_HIGH"
        color = "🔴"
        interpretation = "Nguy cơ RẤT CAO"
        management = """
        **🔴 BODE 7-10 (Nguy cơ Rất Cao):**
        
        **Điều trị Tích Cực:**
        - **Triple therapy LAMA + LABA + ICS**
        - PDE4 inhibitor
        - Macrolide dài hạn
        - **LTOT bắt buộc** (>15h/ngày)
        - **NIV ban đêm** nếu hypercapnia mạn
        - Morphine liều thấp cho dyspnea nặng
        - Hỗ trợ dinh dưỡng tích cực
        - Phục hồi chức năng (nếu có thể)
        
        **Xem Xét Tích Cực:**
        - **Ghép phổi** (nếu đủ tiêu chuẩn)
        - LVRS (một số trường hợp chọn lọc)
        - Pacer hoặc phẫu thuật giảm thể tích nội soi
        
        **Chăm Sóc Giảm Nhẹ:**
        - Thảo luận mục tiêu điều trị
        - Advance care planning
        - Hỗ trợ tâm lý
        - Chăm sóc giảm nhẹ triệu chứng
        
        **Theo dõi Sát:**
        - FEV1 mỗi 1-3 tháng
        - ABG thường xuyên
        - Đánh giá chất lượng cuộc sống
        - Hospitalization risk cao
        """
    
    return {
        'total_score': score,
        'quartile': quartile,
        'mortality_4yr': mortality_4yr,
        'risk_class': risk_class,
        'color': color,
        'interpretation': interpretation,
        'management': management,
        'details': details
    }


def render():
    """Render BODE Index calculator"""
    
    st.title("🫁 BODE Index")
    st.markdown("**Tiên lượng tử vong ở bệnh nhân COPD**")
    
    # Educational information
    with st.expander("ℹ️ Thông tin & Cách Sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **BODE Index** là thang điểm đa chiều cho COPD:
        - Dự đoán tử vong tốt hơn FEV1 đơn thuần
        - Kết hợp 4 yếu tố quan trọng
        - Hướng dẫn quản lý COPD
        - Theo dõi diễn tiến bệnh
        
        ### 🎯 4 Thành phần (BODE)
        
        1. **B (Body mass index):** Chỉ số khối cơ thể
        2. **O (Obstruction):** Tắc nghẽn khí đạo (FEV1)
        3. **D (Dyspnea):** Khó thở (mMRC scale)
        4. **E (Exercise):** Khả năng gắng sức (6MWD)
        
        **Tổng điểm:** 0-10
        
        ### 📊 BODE Scoring
        
        | Thành phần | 0 điểm | 1 điểm | 2 điểm | 3 điểm |
        |------------|--------|--------|--------|--------|
        | **BMI** | >21 | ≤21 | - | - |
        | **FEV1 (% predicted)** | ≥65 | 50-64 | 36-49 | ≤35 |
        | **mMRC Dyspnea** | 0-1 | 2 | 3 | 4 |
        | **6MWD (meters)** | ≥350 | 250-349 | 150-249 | ≤149 |
        
        ### 📈 Tử vong 4 Năm
        
        | BODE Score | Quartile | Tử vong 4 Năm |
        |------------|----------|---------------|
        | 0-2 | Q1 | ~20% |
        | 3-4 | Q2 | ~30% |
        | 5-6 | Q3 | ~40-50% |
        | 7-10 | Q4 | >60% |
        
        ### 🩺 mMRC Dyspnea Scale
        
        - **0:** Khó thở khi gắng sức nặng
        - **1:** Khó thở khi đi nhanh hoặc lên dốc nhẹ
        - **2:** Đi chậm hơn người cùng tuổi do khó thở
        - **3:** Phải dừng để nghỉ sau khi đi ~100 mét
        - **4:** Quá khó thở để ra khỏi nhà
        
        ### 📚 Tham khảo
        
        - Celli BR, et al. *N Engl J Med* 2004;350:1005-1012
        - GOLD Guidelines 2024
        """)
    
    st.divider()
    
    # Input section
    st.subheader("📝 Nhập 4 Thông số BODE")
    
    # BMI
    st.markdown("#### 1️⃣ B - Body Mass Index")
    col1, col2, col3 = st.columns(3)
    with col1:
        weight = st.number_input("Cân nặng (kg)", 20.0, 200.0, 60.0, 1.0, format="%d")
    with col2:
        height = st.number_input("Chiều cao (cm)", 100, 250, 170, 1, format="%d")
    with col3:
        bmi = weight / ((height / 100) ** 2)
        st.metric("**BMI**", f"{bmi:.1f}")
        if bmi <= 21:
            st.caption("⚠️ Thiếu cân (1 điểm)")
        else:
            st.caption("✓ Bình thường (0 điểm)")
    
    st.divider()
    
    # FEV1
    st.markdown("#### 2️⃣ O - Airflow Obstruction (FEV1)")
    fev1_percent = st.number_input(
        "**FEV1 % predicted**",
        0.0, 150.0, 50.0, 1.0,
        format="%.1f",
        help="FEV1 sau giãn phế quản / FEV1 predicted × 100%"
    )
    st.caption("💡 Lấy sau khi dùng giãn phế quản")
    
    st.divider()
    
    # Dyspnea
    st.markdown("#### 3️⃣ D - Dyspnea (mMRC Scale)")
    mmrc_options = [
        "0: Khó thở khi gắng sức nặng",
        "1: Khó thở khi đi nhanh/lên dốc",
        "2: Đi chậm hơn người cùng tuổi do khó thở",
        "3: Dừng lại sau đi ~100m",
        "4: Quá khó thở để ra khỏi nhà"
    ]
    mmrc_dyspnea = st.radio(
        "**Modified MRC Dyspnea Scale**",
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: mmrc_options[x],
        help="Đánh giá mức độ khó thở trong sinh hoạt hàng ngày"
    )
    
    st.divider()
    
    # Exercise capacity
    st.markdown("#### 4️⃣ E - Exercise Capacity")
    walk_distance = st.number_input(
        "**6-Minute Walk Distance (meters)**",
        0, 1000, 300, 10,
        format="%d",
        help="Khoảng cách đi được trong 6 phút"
    )
    st.caption("💡 Test 6 phút đi bộ trên mặt phẳng")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính BODE Index", type="primary", use_container_width=True):
        result = calculate_bode(
            bmi=bmi,
            fev1_percent=fev1_percent,
            mmrc_dyspnea=mmrc_dyspnea,
            walk_distance=walk_distance
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric("**BODE Index**", f"{result['total_score']}/10")
            st.caption(f"{result['quartile']}")
        
        with col_r2:
            st.markdown(f"### {result['color']} {result['interpretation']}")
            st.markdown(f"**Tử vong 4 năm: {result['mortality_4yr']}**")
        
        # Details
        with st.expander("📋 Chi tiết tính điểm", expanded=True):
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Management
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo điều trị")
        st.markdown(result['management'])
        
        # Additional info
        st.info("""
        **📌 Lưu ý quan trọng:**
        
        - **BODE tốt hơn FEV1** trong dự đoán tử vong
        - Tính lại BODE định kỳ (6-12 tháng) để theo dõi
        - BODE tăng → tiên lượng xấu đi
        - BODE giảm → đáp ứng điều trị tốt
        
        **Yếu tố làm tăng nguy cơ:**
        - Đợt cấp COPD tái phát
        - Comorbidities (CVD, DM, osteoporosis)
        - Hypoxemia, hypercapnia
        - Cor pulmonale
        """)
        
        if result['risk_class'] in ['HIGH', 'VERY_HIGH']:
            st.error("""
            **🚨 COPD NẶNG - CẦN CAN THIỆP TÍCH CỰC:**
            
            - Xem xét LTOT (long-term oxygen therapy)
            - Phục hồi chức năng phổi
            - Đánh giá chỉ định ghép phổi (nếu tuổi <65)
            - LVRS (lung volume reduction surgery) nếu phù hợp
            - NIV (non-invasive ventilation) nếu hypercapnia
            - Chăm sóc giảm nhẹ nếu giai đoạn cuối
            """)
        
        st.warning("""
        ⚠️ **Cảnh báo:**
        - BODE là công cụ tiên lượng, không phải chẩn đoán
        - Quyết định điều trị dựa trên đánh giá toàn diện
        - Bỏ thuốc lá là quan trọng NHẤT (giảm 50% tử vong)
        """)
        
        st.session_state['bode_result'] = result
    
    # Quick reference
    with st.expander("📖 GOLD Classification & Treatment"):
        st.markdown("""
        ### GOLD 2024 Classification
        
        **Airflow Limitation (FEV1):**
        - GOLD 1 (Mild): FEV1 ≥80% predicted
        - GOLD 2 (Moderate): 50% ≤ FEV1 < 80%
        - GOLD 3 (Severe): 30% ≤ FEV1 < 50%
        - GOLD 4 (Very Severe): FEV1 < 30%
        
        **Treatment by GOLD Group:**
        
        **Group A (Low risk, fewer symptoms):**
        - Bronchodilator monotherapy (LAMA or LABA)
        
        **Group B (Low risk, more symptoms):**
        - LAMA or LABA or LAMA + LABA
        
        **Group E (Exacerbation history):**
        - LAMA + LABA (+ ICS if indicated)
        - Consider Roflumilast, Macrolide
        
        ### Indications for LTOT
        
        - PaO2 ≤55 mmHg (7.3 kPa)
        - PaO2 56-59 mmHg + polycythemia/cor pulmonale/edema
        - SpO2 ≤88% at rest
        
        **Duration:** >15 hours/day (24h best)
        """)

