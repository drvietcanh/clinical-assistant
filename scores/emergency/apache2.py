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
from components.ui.scoring import (
    render_score_result,
    render_score_breakdown,
)
from .apache2_lookup import (
    get_temp_score,
    get_map_score,
    get_hr_score,
    get_rr_score,
    get_oxygenation_score,
    get_ph_score,
    get_na_score,
    get_k_score,
    get_cr_score,
    get_hct_score,
    get_wbc_score,
    get_gcs_score,
    get_age_score,
    get_chronic_health_score
)


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
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **APACHE II** là thang điểm ICU:
        - Dự đoán tử vong bệnh viện
        - Đánh giá mức độ nặng
        - So sánh chất lượng chăm sóc ICU
        - Nghiên cứu & phân tầng bệnh nhân
        
        ### 🎯 3 Thành phần
        
        1. **Acute Physiology Score (0-60):** 12 biến số sinh lý
        2. **Age Points (0-6):** Điểm tuổi
        3. **Chronic Health (0-5):** Bệnh mạn tính
        
        **Tổng điểm:** 0-71
        
        ### 📊 Điểm & Tử vong
        
        | APACHE II | Tử vong |
        |-----------|---------|
        | 0-4 | 4% |
        | 5-9 | 8% |
        | 10-14 | 15% |
        | 15-19 | 25% |
        | 20-24 | 40% |
        | 25-29 | 55% |
        | 30-34 | 73% |
        | ≥35 | 85% |
        
        ### ⚠️ Lưu ý
        
        - Tính trong 24h ĐẦU nhập ICU
        - Lấy giá trị TỆ NHẤT trong 24h
        - Không tính lại trong ICU stay
        
        ### 📚 Tham khảo
        
        - Knaus WA, et al. *Crit Care Med* 1985;13:818-829
        """)
    
    st.divider()
    
    st.subheader("📝 Nhập dữ liệu (Giá trị TỆ NHẤT trong 24h đầu ICU)")
    
    # Demographics
    st.markdown("#### 👤 Thông tin chung")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Tuổi", 0, 120, 50, 1, format="%d")
    with col2:
        gcs = st.number_input("GCS (Thang điểm hôn mê Glasgow) - Thang điểm hôn mê Glasgow", 3, 15, 15, 1, format="%d")
    
    st.divider()
    
    # Vital signs
    st.markdown("#### 🩺 Sinh hiệu")
    col3, col4, col5 = st.columns(3)
    with col3:
        temperature = st.number_input("Nhiệt độ (°C)", 20, 45, 37, 1, format="%d")
    with col4:
        map_val = st.number_input("MAP (mmHg)", 0, 250, 70, 1, format="%d")
        st.caption("MAP = (SBP + 2×DBP)/3")
    with col5:
        heart_rate = st.number_input("Nhịp tim (/min)", 0, 250, 80, 1, format="%d")
    
    respiratory_rate = st.number_input("Nhịp thở (/min)", 0, 70, 16, 1, format="%d")
    
    st.divider()
    
    # ABG
    st.markdown("#### 🫁 Khí máu động mạch (ABG)")
    col6, col7, col8 = st.columns(3)
    with col6:
        fio2 = st.number_input("FiO₂ (%)", 21, 100, 21, 1, format="%d")
    with col7:
        pao2 = st.number_input("PaO₂ (mmHg)", 0, 700, 100, 1, format="%d")
    with col8:
        paco2 = st.number_input("PaCO₂ (mmHg)", 0, 150, 40, 1, format="%d")
    
    ph = st.number_input("pH", 6.5, 8.0, 7.40, 0.01, format="%.2f")
    
    st.divider()
    
    # Labs
    st.markdown("#### 🔬 Xét nghiệm")
    col9, col10 = st.columns(2)
    with col9:
        sodium = st.number_input("Sodium (mEq/L)", 80.0, 200.0, 140.0, 1.0, format="%.1f")
        potassium = st.number_input("Potassium (mEq/L)", 1.5, 10.0, 4.0, 0.1, format="%.1f")
        creatinine = st.number_input("Creatinine (mg/dL)", 0.0, 20.0, 1.0, 0.1, format="%.1f")
        has_arf = st.checkbox("**Suy thận cấp (ARF)** - nhân đôi điểm Cr")
    
    with col10:
        hematocrit = st.number_input("Hematocrit (%)", 0.0, 80.0, 40.0, 0.1, format="%.1f")
        wbc = st.number_input("WBC (×10³/μL)", 0.0, 100.0, 10.0, 0.1, format="%.1f")
    
    st.divider()
    
    # Chronic health
    st.markdown("#### 🏥 Bệnh mạn tính")
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
        st.subheader("📊 Kết quả")
        
        # Color-coded score result (MDCalc style)
        mortality_text = f"{result['predicted_mortality']:.1f}% (Khoảng: {result['mortality_range']})"
        render_score_result(
            title="APACHE II Score",
            score=result['total_score'],
            interpretation=result['interpretation'],
            mortality=mortality_text,
            icon=result['color'],
            thresholds={"low": 15, "moderate": 25, "high": 35},  # APACHE II thresholds
            size="large"
        )
        
        # Score breakdown
        breakdown_scores = {
            "Acute Physiology Score (APS)": result['aps'],
            "Age Points": result['age_points'],
            "Chronic Health Points": result['chronic_points'],
        }
        
        render_score_breakdown(
            title="📋 Chi tiết điểm số",
            subscores=breakdown_scores,
            total_score=result['total_score']
        )
        
        # Detailed scoring breakdown
        with st.expander("📝 Chi tiết từng biến số", expanded=False):
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Interpretation
        st.info("""
        **📌 Diễn giải:**
        
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
        
        # Export section
        st.markdown("---")
        from components.export import render_export_section
        
        # Prepare inputs for export
        # Format chronic health status
        if not has_chronic_health:
            chronic_health = "Không"
        elif is_nonsurgical:
            chronic_health = "Có (Nonsurgical)"
        elif is_post_emergency_surgery:
            chronic_health = "Có (Sau phẫu thuật cấp cứu)"
        else:
            chronic_health = "Có (Sau phẫu thuật chương trình)"
        
        inputs_dict = {
            "Age": f"{age} tuổi",
            "Temperature": f"{temperature:.1f}°C",
            "MAP": f"{map_val:.0f} mmHg",
            "Nhịp tim": f"{heart_rate:.0f} /min",
            "Nhịp thở": f"{respiratory_rate:.0f} /min",
            "FiO₂": f"{fio2:.0f}%",
            "PaO₂": f"{pao2:.0f} mmHg",
            "PaCO₂": f"{paco2:.0f} mmHg",
            "pH": f"{ph:.2f}",
            "Sodium": f"{sodium:.0f} mEq/L",
            "Potassium": f"{potassium:.1f} mEq/L",
            "Creatinine": f"{creatinine:.1f} mg/dL",
            "Has ARF": "Có" if params['has_arf'] else "Không",
            "Hematocrit": f"{hematocrit:.1f}%",
            "WBC": f"{wbc:.1f} ×10³/μL",
            "GCS": f"{gcs}",
            "Chronic Health": chronic_health
        }
        
        # Prepare results for export
        results_dict = {
            "APACHE II Score": f"{result['total_score']} điểm",
            "Predicted Mortality": f"{result['predicted_mortality']:.1f}%",
            "Mortality Range": result['mortality_range'],
            "Interpretation": result['interpretation'],
            "APS": f"{result['aps']}/60 điểm",
            "Age Points": f"{result['age_points']}/6 điểm",
            "Chronic Health Points": f"{result['chronic_points']}/5 điểm"
        }
        
        render_export_section(
            title=f"APACHE II = {result['total_score']} điểm",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="APACHE II Score",
            filename="apache2_result"
        )
        
        st.warning("""
        ⚠️ **Lưu ý:**
        - APACHE II chỉ là ước tính, không chính xác 100%
        - Nhiều yếu tố khác ảnh hưởng tiên lượng (bệnh nền, điều trị, biến chứng)
        - Quyết định điều trị dựa trên đánh giá lâm sàng toàn diện
        """)
        
        st.session_state['apache2_result'] = result
    
    # Reference table
    with st.expander("📖 Bảng tham khảo APACHE II Scoring"):
        st.markdown("""
        ### APACHE II Chi tiết
        
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
