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
from config.theme import COLORS
import math
from components.ui.scoring import (
    render_score_result,
    render_score_breakdown,
)
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================

# ========== NEW COMPONENTS (Phase 1 & 2) ==========
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.score_charts import render_risk_gauge_chart, render_risk_bar_chart
from components.scores_export import render_export_section as render_scores_export
# ========== PHASE 1: CALCULATOR ENHANCEMENTS ==========
try:
    from components.calculator_enhancements import (
        render_calculator_explanation,
        render_evidence_citation,
        render_result_interpretation
    )
    CALCULATOR_ENHANCEMENTS_AVAILABLE = True
except ImportError:
    CALCULATOR_ENHANCEMENTS_AVAILABLE = False
# ===================================================

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
from scores.utils.validation import (
    validate_age,
    validate_gcs,
    validate_blood_pressure,
    validate_heart_rate,
    validate_respiratory_rate,
    validate_temperature,
    validate_lab_value
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
        color = COLORS["success"]
    elif total_score < 15:
        interpretation = "Mức độ nặng TRUNG BÌNH"
        mortality_range = "10-25%"
        color = COLORS["warning"]
    elif total_score < 20:
        interpretation = "Mức độ nặng CAO"
        mortality_range = "25-40%"
        color = COLORS["warning"]
    elif total_score < 25:
        interpretation = "Mức độ nặng RẤT CAO"
        mortality_range = "40-55%"
        color = COLORS["error"]
    else:
        interpretation = "Mức độ nặng CỰC KỲ CAO"
        mortality_range = ">55%"
        color = COLORS["error"]
    
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
    
    # st.title("🏥 APACHE II Score")
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🏥 APACHE II Score</h2>
    <p style='text-align: center;'><em>Acute Physiology and Chronic Health Evaluation II - Dự đoán tử vong ICU</em></p>
    """, unsafe_allow_html=True)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'apache2':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Smart Suggestions (sidebar)
    with st.sidebar:
        render_suggestions(
            calculator_id="apache2",
            calculator_name="APACHE II Score",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Educational information - Enhanced with Phase 1
    if CALCULATOR_ENHANCEMENTS_AVAILABLE:
        render_calculator_explanation(
            title="Về APACHE II Score",
            content="""
            **APACHE II (Acute Physiology and Chronic Health Evaluation II)** là thang điểm:
            
            - Dự đoán tử vong bệnh viện trong ICU
            - Đánh giá mức độ nặng bệnh
            - So sánh chất lượng chăm sóc ICU
            - Nghiên cứu & phân tầng bệnh nhân
            
            **3 thành phần:**
            1. **Acute Physiology Score (0-60):** 12 biến số sinh lý
            2. **Age Points (0-6):** Điểm tuổi
            3. **Chronic Health (0-5):** Bệnh mạn tính
            
            **Tổng điểm: 0-71 điểm**
            """,
            when_to_use="""
            **Sử dụng APACHE II khi:**
            - Bệnh nhân ICU cần đánh giá tiên lượng
            - So sánh chất lượng chăm sóc giữa các ICU
            - Nghiên cứu và phân tầng bệnh nhân
            - Đánh giá mức độ nặng bệnh
            """,
            limitations="""
            **Hạn chế:**
            - Tính trong 24h đầu vào ICU
            - Cần có đầy đủ 12 biến số sinh lý
            - Không áp dụng cho bệnh nhân <16 tuổi
            - Không áp dụng cho bệnh nhân burn, cardiac surgery
            - Chỉ dự đoán tử vong bệnh viện, không phải tử vong ICU
            """,
            clinical_context="""
            **Bối cảnh lâm sàng:**
            - APACHE II được tính trong 24h đầu vào ICU
            - Điểm cao (>25) liên quan đến tử vong cao
            - Sử dụng kết hợp với lâm sàng, không chỉ dựa vào điểm số
            - APACHE IV là phiên bản mới hơn nhưng APACHE II vẫn được dùng rộng rãi
            """
        )
        
        # Evidence citation
        render_evidence_citation(
            citation_text="Knaus WA, et al. APACHE II: a severity of disease classification system. Crit Care Med. 1985;13(10):818-829.",
            doi="10.1097/00003246-198510000-00009"
        )
    else:
        # Fallback to original expander
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
        # Validate inputs before calculation
        validation_errors = []
        
        is_valid_age, age_error = validate_age(age, 0, 120)
        if not is_valid_age:
            validation_errors.append(age_error)
        
        is_valid_gcs, gcs_error = validate_gcs(gcs)
        if not is_valid_gcs:
            validation_errors.append(gcs_error)
        
        is_valid_temp, temp_error = validate_temperature(temperature)
        if not is_valid_temp:
            validation_errors.append(temp_error)
        
        is_valid_hr, hr_error = validate_heart_rate(heart_rate)
        if not is_valid_hr:
            validation_errors.append(hr_error)
        
        is_valid_rr, rr_error = validate_respiratory_rate(respiratory_rate)
        if not is_valid_rr:
            validation_errors.append(rr_error)
        
        is_valid_na, na_error = validate_lab_value(sodium, "Sodium", 80, 200)
        if not is_valid_na:
            validation_errors.append(na_error)
        
        is_valid_k, k_error = validate_lab_value(potassium, "Potassium", 1.5, 10.0)
        if not is_valid_k:
            validation_errors.append(k_error)
        
        is_valid_cr, cr_error = validate_lab_value(creatinine, "Creatinine", 0.0, 20.0)
        if not is_valid_cr:
            validation_errors.append(cr_error)
        
            if validation_errors:
                from components.ui.validation import render_validation_errors
                render_validation_errors(validation_errors)
        
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
        
        # Determine risk level for color coding
        if result['total_score'] < 10:
            risk_level_code = "low"
        elif result['total_score'] < 15:
            risk_level_code = "moderate"
        elif result['total_score'] < 20:
            risk_level_code = "high"
        elif result['total_score'] < 25:
            risk_level_code = "very_high"
        else:
            risk_level_code = "critical"
        
        # Display score with color coding badge
        st.markdown(f"## APACHE II Score = {result['total_score']}/71")
        render_risk_badge(
            risk_level=risk_level_code,
            label=result['interpretation'],
            value=result['total_score']
        )
        
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
        
        # Interpretation - Enhanced with Phase 1
        if CALCULATOR_ENHANCEMENTS_AVAILABLE:
            # Determine recommendations
            recommendations = []
            if result['total_score'] >= 25:
                recommendations.append("Nguy cơ tử vong >40%, cần hồi sức tích cực")
                recommendations.append("Xem xét mức độ chăm sóc và tiên lượng")
                recommendations.append("Thảo luận với gia đình về mục tiêu điều trị")
            elif result['total_score'] >= 20:
                recommendations.append("Nguy cơ tử vong cao, theo dõi sát")
            else:
                recommendations.append("Tiếp tục điều trị và theo dõi")
            
            recommendations.append("APACHE II dự đoán tử vong BỆNH VIỆN, không phải ICU")
            recommendations.append("Tính 1 LẦN trong 24h đầu nhập ICU (giá trị tệ nhất)")
            
            render_result_interpretation(
                result=f"{result['total_score']}/71",
                interpretation=f"Nguy cơ tử vong bệnh viện: {result['mortality']}",
                recommendations=recommendations,
                risk_level="high" if result['total_score'] >= 25 else "moderate" if result['total_score'] >= 20 else "low"
            )
        else:
            # Fallback to original
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
        
        # Visual Charts
        st.markdown("---")
        st.markdown("### 📊 Biểu Đồ Nguy cơ")
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            render_risk_gauge_chart(
                value=result['total_score'],
                min_value=0,
                max_value=71,
                thresholds={
                    'Low': 10,
                    'Moderate': 15,
                    'High': 20,
                    'Very High': 25
                },
                title="APACHE II Score"
            )
        
        with col_chart2:
            render_risk_bar_chart(
                value=result['total_score'],
                thresholds={
                    'Low': 10,
                    'Moderate': 15,
                    'High': 20,
                    'Very High': 25
                },
                max_value=71,
                title="Risk Level",
                show_value=True
            )
        
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
            "APACHE II Score": f"{result['total_score']}/71",
            "Predicted Mortality": f"{result['predicted_mortality']:.1f}%",
            "Mortality Range": result['mortality_range'],
            "Interpretation": result['interpretation'],
            "Risk Level": risk_level_code,
            "APS": f"{result['aps']}/60 điểm",
            "Age Points": f"{result['age_points']}/6 điểm",
            "Chronic Health Points": f"{result['chronic_points']}/5 điểm"
        }
        
        # Export section (new component)
        st.markdown("---")
        render_scores_export(
            calculator_name="APACHE II Score",
            inputs=inputs_dict,
            results=results_dict,
            specialty="Cấp cứu & Hồi sức"
        )
        
        # Keep old export for compatibility
        st.markdown("---")
        from components.export import render_export_section
        render_export_section(
            title=f"APACHE II = {result['total_score']} điểm",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="APACHE II Score",
            filename="apache2_result"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="apache2",
            calculator_name="APACHE II Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="apache2",
            calculator_name="APACHE II Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="apache2", show_actions=True)
        
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
    
    # References section
    references = get_references("APACHE II")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
