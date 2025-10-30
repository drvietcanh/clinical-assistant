"""
APACHE II Score (Acute Physiology and Chronic Health Evaluation II)
====================================================================

ICU mortality prediction scoring system

Reference:
- Knaus WA, et al. APACHE II: a severity of disease classification system.
  Crit Care Med. 1985;13(10):818-829.

APACHE II Components:
1. Acute Physiology Score (APS): 12 physiological variables (0-60 points)
2. Age points (0-6 points)
3. Chronic Health points (0-5 points)

Total: 0-71 points

Clinical Utility:
- Predict ICU mortality
- Stratify disease severity
- Research and quality improvement
- ICU resource allocation
"""

import streamlit as st
import math


def get_temp_score(temp: float) -> int:
    """Temperature score"""
    if temp >= 41:
        return 4
    elif temp >= 39:
        return 3
    elif temp >= 38.5:
        return 1
    elif temp >= 36:
        return 0
    elif temp >= 34:
        return 1
    elif temp >= 32:
        return 2
    elif temp >= 30:
        return 3
    else:
        return 4


def get_map_score(map_val: float) -> int:
    """Mean arterial pressure score"""
    if map_val >= 160:
        return 4
    elif map_val >= 130:
        return 3
    elif map_val >= 110:
        return 2
    elif map_val >= 70:
        return 0
    elif map_val >= 50:
        return 2
    else:
        return 4


def get_hr_score(hr: float) -> int:
    """Heart rate score"""
    if hr >= 180:
        return 4
    elif hr >= 140:
        return 3
    elif hr >= 110:
        return 2
    elif hr >= 70:
        return 0
    elif hr >= 55:
        return 2
    elif hr >= 40:
        return 3
    else:
        return 4


def get_rr_score(rr: float) -> int:
    """Respiratory rate score"""
    if rr >= 50:
        return 4
    elif rr >= 35:
        return 3
    elif rr >= 25:
        return 1
    elif rr >= 12:
        return 0
    elif rr >= 10:
        return 1
    elif rr >= 6:
        return 2
    else:
        return 4


def get_oxygenation_score(fio2: float, pao2: float, paco2: float, ph: float) -> int:
    """Oxygenation score - A-a gradient if FiO2≥0.5, else PaO2"""
    if fio2 >= 50:  # Use A-a gradient
        # A-a gradient = [(FiO2 × (Patm - PH2O)) - (PaCO2/0.8)] - PaO2
        # Simplified: ≈ (FiO2 × 713) - (PaCO2/0.8) - PaO2
        aa_gradient = (fio2 * 7.13) - (paco2 / 0.8) - pao2
        if aa_gradient >= 500:
            return 4
        elif aa_gradient >= 350:
            return 3
        elif aa_gradient >= 200:
            return 2
        elif aa_gradient < 200:
            return 0
    else:  # Use PaO2
        if pao2 < 55:
            return 4
        elif pao2 < 60:
            return 3
        elif pao2 < 70:
            return 1
        else:
            return 0
    return 0


def get_ph_score(ph: float) -> int:
    """Arterial pH score"""
    if ph >= 7.7:
        return 4
    elif ph >= 7.6:
        return 3
    elif ph >= 7.5:
        return 1
    elif ph >= 7.33:
        return 0
    elif ph >= 7.25:
        return 2
    elif ph >= 7.15:
        return 3
    else:
        return 4


def get_na_score(na: float) -> int:
    """Serum sodium score"""
    if na >= 180:
        return 4
    elif na >= 160:
        return 3
    elif na >= 155:
        return 2
    elif na >= 150:
        return 1
    elif na >= 130:
        return 0
    elif na >= 120:
        return 2
    elif na >= 111:
        return 3
    else:
        return 4


def get_k_score(k: float) -> int:
    """Serum potassium score"""
    if k >= 7:
        return 4
    elif k >= 6:
        return 3
    elif k >= 5.5:
        return 1
    elif k >= 3.5:
        return 0
    elif k >= 3:
        return 1
    elif k >= 2.5:
        return 2
    else:
        return 4


def get_cr_score(cr: float, has_arf: bool) -> int:
    """Serum creatinine score (double if acute renal failure)"""
    if cr >= 3.5:
        base_score = 4
    elif cr >= 2:
        base_score = 3
    elif cr >= 1.5:
        base_score = 2
    elif cr >= 0.6:
        base_score = 0
    else:
        base_score = 2
    
    return base_score * 2 if has_arf else base_score


def get_hct_score(hct: float) -> int:
    """Hematocrit score"""
    if hct >= 60:
        return 4
    elif hct >= 50:
        return 2
    elif hct >= 46:
        return 1
    elif hct >= 30:
        return 0
    elif hct >= 20:
        return 2
    else:
        return 4


def get_wbc_score(wbc: float) -> int:
    """White blood cell count score"""
    if wbc >= 40:
        return 4
    elif wbc >= 20:
        return 2
    elif wbc >= 15:
        return 1
    elif wbc >= 3:
        return 0
    elif wbc >= 1:
        return 2
    else:
        return 4


def get_gcs_score(gcs: int) -> int:
    """Glasgow Coma Scale score (15 - GCS)"""
    return 15 - gcs


def get_age_score(age: int) -> int:
    """Age points"""
    if age < 45:
        return 0
    elif age < 55:
        return 2
    elif age < 65:
        return 3
    elif age < 75:
        return 5
    else:
        return 6


def get_chronic_health_score(
    has_chronic: bool,
    is_post_emergency_surgery: bool,
    is_nonsurgical: bool
) -> int:
    """Chronic health points"""
    if not has_chronic:
        return 0
    
    if is_nonsurgical or is_post_emergency_surgery:
        return 5
    else:  # Elective post-op
        return 2


def calculate_apache2(params: dict) -> dict:
    """Calculate APACHE II score"""
    
    # Acute Physiology Score
    aps = 0
    details = []
    
    temp_score = get_temp_score(params['temperature'])
    aps += temp_score
    details.append(f"Nhiệt độ {params['temperature']:.1f}°C → {temp_score} điểm")
    
    map_score = get_map_score(params['map'])
    aps += map_score
    details.append(f"MAP {params['map']:.0f} mmHg → {map_score} điểm")
    
    hr_score = get_hr_score(params['heart_rate'])
    aps += hr_score
    details.append(f"Nhịp tim {params['heart_rate']:.0f} /min → {hr_score} điểm")
    
    rr_score = get_rr_score(params['respiratory_rate'])
    aps += rr_score
    details.append(f"Nhịp thở {params['respiratory_rate']:.0f} /min → {rr_score} điểm")
    
    oxy_score = get_oxygenation_score(
        params['fio2'], params['pao2'], params['paco2'], params['ph']
    )
    aps += oxy_score
    if params['fio2'] >= 50:
        details.append(f"A-a gradient (FiO₂ ≥50%) → {oxy_score} điểm")
    else:
        details.append(f"PaO₂ {params['pao2']:.0f} mmHg → {oxy_score} điểm")
    
    ph_score = get_ph_score(params['ph'])
    aps += ph_score
    details.append(f"pH {params['ph']:.2f} → {ph_score} điểm")
    
    na_score = get_na_score(params['sodium'])
    aps += na_score
    details.append(f"Na {params['sodium']:.0f} mEq/L → {na_score} điểm")
    
    k_score = get_k_score(params['potassium'])
    aps += k_score
    details.append(f"K {params['potassium']:.1f} mEq/L → {k_score} điểm")
    
    cr_score = get_cr_score(params['creatinine'], params['has_arf'])
    aps += cr_score
    arf_note = " (×2 vì ARF)" if params['has_arf'] else ""
    details.append(f"Creatinine {params['creatinine']:.1f} mg/dL → {cr_score} điểm{arf_note}")
    
    hct_score = get_hct_score(params['hematocrit'])
    aps += hct_score
    details.append(f"Hematocrit {params['hematocrit']:.1f}% → {hct_score} điểm")
    
    wbc_score = get_wbc_score(params['wbc'])
    aps += wbc_score
    details.append(f"WBC {params['wbc']:.1f} ×10³/μL → {wbc_score} điểm")
    
    gcs_score = get_gcs_score(params['gcs'])
    aps += gcs_score
    details.append(f"GCS {params['gcs']} → {gcs_score} điểm (15 - GCS)")
    
    # Age points
    age_points = get_age_score(params['age'])
    details.append(f"Tuổi {params['age']} → {age_points} điểm")
    
    # Chronic health points
    chronic_points = get_chronic_health_score(
        params['has_chronic_health'],
        params['is_post_emergency_surgery'],
        params['is_nonsurgical']
    )
    if chronic_points > 0:
        details.append(f"Bệnh mạn tính → {chronic_points} điểm")
    
    # Total score
    total_score = aps + age_points + chronic_points
    
    # Predicted mortality (from original APACHE II study)
    # ln(R/(1-R)) = -3.517 + (APACHE II × 0.146)
    logit = -3.517 + (total_score * 0.146)
    predicted_mortality = 100 / (1 + math.exp(-logit))
    
    # Interpretation
    if total_score < 10:
        interpretation = "Mức độ nặng THẤP"
        mortality_range = "<10%"
        color = "🟢"
    elif total_score < 15:
        interpretation = "Mức độ nặng TRUNG BÌNH"
        mortality_range = "10-25%"
        color = "🟡"
    elif total_score < 20:
        interpretation = "Mức độ nặng CAO"
        mortality_range = "25-40%"
        color = "🟠"
    elif total_score < 25:
        interpretation = "Mức độ nặng RẤT CAO"
        mortality_range = "40-55%"
        color = "🟠"
    else:
        interpretation = "Mức độ nặng CỰC KỲ CAO"
        mortality_range = ">55%"
        color = "🔴"
    
    return {
        'total_score': total_score,
        'aps': aps,
        'age_points': age_points,
        'chronic_points': chronic_points,
        'predicted_mortality': predicted_mortality,
        'mortality_range': mortality_range,
        'interpretation': interpretation,
        'color': color,
        'details': details
    }


def render():
    """Render APACHE II calculator"""
    
    st.title("🏥 APACHE II Score")
    st.markdown("**Acute Physiology and Chronic Health Evaluation II - Dự đoán tử vong ICU**")
    
    # Educational information
    with st.expander("ℹ️ Thông Tin & Cách Sử Dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **APACHE II** là thang điểm ICU:
        - Dự đoán tử vong bệnh viện
        - Đánh giá mức độ nặng
        - So sánh chất lượng chăm sóc ICU
        - Nghiên cứu & phân tầng bệnh nhân
        
        ### 🎯 3 Thành Phần
        
        1. **Acute Physiology Score (0-60):** 12 biến số sinh lý
        2. **Age Points (0-6):** Điểm tuổi
        3. **Chronic Health (0-5):** Bệnh mạn tính
        
        **Tổng điểm:** 0-71
        
        ### 📊 Điểm & Tử Vong
        
        | APACHE II | Tử Vong |
        |-----------|---------|
        | 0-4 | 4% |
        | 5-9 | 8% |
        | 10-14 | 15% |
        | 15-19 | 25% |
        | 20-24 | 40% |
        | 25-29 | 55% |
        | 30-34 | 73% |
        | ≥35 | 85% |
        
        ### ⚠️ Lưu Ý
        
        - Tính trong 24h ĐẦU nhập ICU
        - Lấy giá trị TỆ NHẤT trong 24h
        - Không tính lại trong ICU stay
        
        ### 📚 Tham Khảo
        
        - Knaus WA, et al. *Crit Care Med* 1985;13:818-829
        """)
    
    st.divider()
    
    st.subheader("📝 Nhập Dữ Liệu (Giá trị TỆ NHẤT trong 24h đầu ICU)")
    
    # Demographics
    st.markdown("#### 👤 Thông Tin Chung")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Tuổi", 0, 120, 50, 1)
    with col2:
        gcs = st.number_input("GCS (Glasgow Coma Scale)", 3, 15, 15, 1)
    
    st.divider()
    
    # Vital signs
    st.markdown("#### 🩺 Sinh Hiệu")
    col3, col4, col5 = st.columns(3)
    with col3:
        temperature = st.number_input("Nhiệt độ (°C)", 20.0, 45.0, 37.0, 0.1)
    with col4:
        map_val = st.number_input("MAP (mmHg)", 0.0, 250.0, 70.0, 1.0)
        st.caption("MAP = (SBP + 2×DBP)/3")
    with col5:
        heart_rate = st.number_input("Nhịp tim (/min)", 0.0, 250.0, 80.0, 1.0)
    
    respiratory_rate = st.number_input("Nhịp thở (/min)", 0.0, 70.0, 16.0, 1.0)
    
    st.divider()
    
    # ABG
    st.markdown("#### 🫁 Khí Máu Động Mạch (ABG)")
    col6, col7, col8 = st.columns(3)
    with col6:
        fio2 = st.number_input("FiO₂ (%)", 21.0, 100.0, 21.0, 1.0)
    with col7:
        pao2 = st.number_input("PaO₂ (mmHg)", 0.0, 700.0, 100.0, 1.0)
    with col8:
        paco2 = st.number_input("PaCO₂ (mmHg)", 0.0, 150.0, 40.0, 1.0)
    
    ph = st.number_input("pH", 6.5, 8.0, 7.40, 0.01)
    
    st.divider()
    
    # Labs
    st.markdown("#### 🔬 Xét Nghiệm")
    col9, col10 = st.columns(2)
    with col9:
        sodium = st.number_input("Sodium (mEq/L)", 80.0, 200.0, 140.0, 1.0)
        potassium = st.number_input("Potassium (mEq/L)", 1.5, 10.0, 4.0, 0.1)
        creatinine = st.number_input("Creatinine (mg/dL)", 0.0, 20.0, 1.0, 0.1)
        has_arf = st.checkbox("**Suy thận cấp (ARF)** - nhân đôi điểm Cr")
    
    with col10:
        hematocrit = st.number_input("Hematocrit (%)", 0.0, 80.0, 40.0, 0.1)
        wbc = st.number_input("WBC (×10³/μL)", 0.0, 100.0, 10.0, 0.1)
    
    st.divider()
    
    # Chronic health
    st.markdown("#### 🏥 Bệnh Mạn Tính")
    has_chronic_health = st.checkbox(
        "**Có bệnh mạn tính nặng**",
        help="Suy tim NYHA IV, COPD nặng, xơ gan Child C, HD lâu dài, immunocompromised"
    )
    
    if has_chronic_health:
        col11, col12 = st.columns(2)
        with col11:
            is_nonsurgical = st.checkbox("Bệnh nhân nội khoa (nonsurgical)")
        with col12:
            is_post_emergency_surgery = st.checkbox("Sau phẫu thuật cấp cứu")
    else:
        is_nonsurgical = False
        is_post_emergency_surgery = False
    
    st.divider()
    
    # Calculate
    if st.button("🧮 Tính APACHE II Score", type="primary", use_container_width=True):
        params = {
            'age': age,
            'temperature': temperature,
            'map': map_val,
            'heart_rate': heart_rate,
            'respiratory_rate': respiratory_rate,
            'fio2': fio2,
            'pao2': pao2,
            'paco2': paco2,
            'ph': ph,
            'sodium': sodium,
            'potassium': potassium,
            'creatinine': creatinine,
            'has_arf': has_arf,
            'hematocrit': hematocrit,
            'wbc': wbc,
            'gcs': gcs,
            'has_chronic_health': has_chronic_health,
            'is_post_emergency_surgery': is_post_emergency_surgery,
            'is_nonsurgical': is_nonsurgical
        }
        
        result = calculate_apache2(params)
        
        # Display results
        st.subheader("📊 Kết Quả")
        
        col_r1, col_r2, col_r3 = st.columns(3)
        
        with col_r1:
            st.metric("**APACHE II**", f"{result['total_score']}")
            st.caption("0-71 (cao = nặng)")
        
        with col_r2:
            st.metric("**Tử Vong Dự Đoán**", f"{result['predicted_mortality']:.1f}%")
            st.caption(f"Khoảng: {result['mortality_range']}")
        
        with col_r3:
            st.markdown(f"### {result['color']}")
            st.markdown(f"**{result['interpretation']}**")
        
        # Score breakdown
        with st.expander("📋 Chi Tiết Điểm Số", expanded=True):
            st.markdown(f"""
            - **Acute Physiology Score (APS):** {result['aps']}/60 điểm
            - **Age Points:** {result['age_points']}/6 điểm
            - **Chronic Health Points:** {result['chronic_points']}/5 điểm
            - **TỔNG:** {result['total_score']}/71 điểm
            """)
            
            st.markdown("---")
            st.markdown("**Chi tiết từng biến số:**")
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Interpretation
        st.info("""
        **📌 Diễn Giải:**
        
        - APACHE II dự đoán tử vong BỆNH VIỆN, không phải ICU
        - Tính 1 LẦN trong 24h đầu nhập ICU (giá trị tệ nhất)
        - Điểm càng cao → nguy cơ tử vong càng cao
        - Không nên tính lại trong thời gian nằm ICU
        """)
        
        if result['total_score'] >= 25:
            st.error("""
            **🚨 APACHE II SCORE RẤT CAO:**
            
            - Nguy cơ tử vong >40%
            - Cần hồi sức tích cực
            - Xem xét mức độ chăm sóc và tiên lượng
            - Thảo luận với gia đình về mục tiêu điều trị
            """)
        
        st.warning("""
        ⚠️ **Lưu Ý:**
        - APACHE II chỉ là ước tính, không chính xác 100%
        - Nhiều yếu tố khác ảnh hưởng tiên lượng (bệnh nền, điều trị, biến chứng)
        - Quyết định điều trị dựa trên đánh giá lâm sàng toàn diện
        """)
        
        st.session_state['apache2_result'] = result
    
    # Reference table
    with st.expander("📖 Bảng Tham Khảo APACHE II Scoring"):
        st.markdown("""
        ### APACHE II Chi Tiết
        
        Xem tài liệu gốc Knaus et al. 1985 cho bảng scoring đầy đủ của 12 biến số.
        
        ### Chronic Health Criteria
        
        **Bệnh mạn tính nặng** bao gồm:
        - Suy tim NYHA Class IV
        - COPD nặng (FEV1 <25%, PaCO2 >50, pO2 <55, hoặc polycythemia)
        - Xơ gan Child-Pugh C (cổ trướng, xuất huyết, encephalopathy)
        - Lọc máu mạn tính
        - Immunocompromised (HIV, chemo, corticosteroid)
        
        **Điểm:**
        - Nonsurgical hoặc emergency post-op: **5 điểm**
        - Elective post-op: **2 điểm**
        """)
