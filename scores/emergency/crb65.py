"""
CRB-65 Score for Pneumonia Severity
====================================

Stratifies community-acquired pneumonia (CAP) severity to determine 
inpatient versus outpatient treatment without requiring lab work.

Reference:
- Lim WS, et al. Defining community acquired pneumonia severity on 
  presentation to hospital: an international derivation and validation study. 
  Thorax. 2003;58(5):377-382.

CRB-65 Components (4 factors):
- C: Confusion (new onset)
- R: Respiratory rate ≥30/min
- B: Blood pressure (SBP <90 or DBP ≤60 mmHg)
- 65: Age ≥65 years

Total: 0-4 points

Risk Categories:
- 0 points: Low risk → Outpatient treatment
- 1-2 points: Moderate risk → Consider inpatient treatment
- 3-4 points: High risk → Inpatient/hospital treatment

Clinical Utility:
- Simple bedside assessment
- No lab work required
- Quick decision-making in emergency
- Used daily in emergency and respiratory medicine
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_age, validate_blood_pressure
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================

# ========== NEW COMPONENTS (Phase 1 & 2) ==========
from components.risk_color_coding import render_risk_badge, get_risk_level
from components.score_charts import render_risk_gauge_chart, render_risk_bar_chart
from components.scores_export import render_export_section as render_scores_export
# ===================================================


def calculate_crb65(
    age: int,
    confusion: bool,
    respiratory_rate: int,
    sbp: float,
    dbp: float
) -> dict:
    """
    Calculate CRB-65 Score
    
    Args:
        age: Age (years)
        confusion: New onset confusion
        respiratory_rate: Respiratory rate (breaths/min)
        sbp: Systolic blood pressure (mmHg)
        dbp: Diastolic blood pressure (mmHg)
    
    Returns:
        Dictionary with score, risk category, and treatment recommendation
    """
    score = 0
    details = []
    
    # Confusion
    if confusion:
        score += 1
        details.append("Lú lẫn mới khởi phát → +1 điểm")
    else:
        details.append("Không lú lẫn → 0 điểm")
    
    # Respiratory rate
    if respiratory_rate >= 30:
        score += 1
        details.append(f"Tần số thở {respiratory_rate}/phút (≥30) → +1 điểm")
    else:
        details.append(f"Tần số thở {respiratory_rate}/phút (<30) → 0 điểm")
    
    # Blood pressure
    if sbp < 90 or dbp <= 60:
        score += 1
        details.append(f"Huyết áp {sbp}/{dbp} mmHg (SBP <90 hoặc DBP ≤60) → +1 điểm")
    else:
        details.append(f"Huyết áp {sbp}/{dbp} mmHg (bình thường) → 0 điểm")
    
    # Age
    if age >= 65:
        score += 1
        details.append(f"Tuổi {age} (≥65) → +1 điểm")
    else:
        details.append(f"Tuổi {age} (<65) → 0 điểm")
    
    # Risk category
    if score == 0:
        risk_category = "Nguy cơ thấp"
        treatment = "Điều trị ngoại trú"
        mortality_risk = "<1%"
    elif score <= 2:
        risk_category = "Nguy cơ trung bình"
        treatment = "Cân nhắc điều trị nội trú"
        mortality_risk = "5-10%"
    else:  # 3-4
        risk_category = "Nguy cơ cao"
        treatment = "Điều trị nội trú/bệnh viện"
        mortality_risk = "15-30%"
    
    return {
        "score": score,
        "risk_category": risk_category,
        "treatment": treatment,
        "mortality_risk": mortality_risk,
        "details": details
    }


def render():
    """Render CRB-65 Score interface"""
    import streamlit as st
    
    st.set_page_config(page_title="CRB-65 Score", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🫁 CRB-65 Score</h2>
    <p style='text-align: center; color: #6B7280;'>
    Phân tầng mức độ nặng viêm phổi cộng đồng<br>
    Quyết định điều trị nội trú vs ngoại trú (không cần xét nghiệm)
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về CRB-65 Score"):
        st.markdown("""
        **CRB-65 Score** là thang điểm đơn giản để đánh giá mức độ nặng của 
        viêm phổi cộng đồng (CAP) mà không cần xét nghiệm.
        
        ### Các thành phần (4 yếu tố):
        1. **C - Confusion:** Lú lẫn mới khởi phát
        2. **R - Respiratory rate:** Tần số thở ≥30/phút
        3. **B - Blood pressure:** Huyết áp tâm thu <90 hoặc tâm trương ≤60 mmHg
        4. **65 - Age:** Tuổi ≥65
        
        ### Phân loại nguy cơ:
        - **0 điểm:** Nguy cơ thấp → Điều trị ngoại trú (tử vong <1%)
        - **1-2 điểm:** Nguy cơ trung bình → Cân nhắc điều trị nội trú (tử vong 5-10%)
        - **3-4 điểm:** Nguy cơ cao → Điều trị nội trú/bệnh viện (tử vong 15-30%)
        
        ### Ưu điểm:
        - Đơn giản, nhanh chóng
        - Không cần xét nghiệm
        - Dùng tại giường bệnh
        - Hữu ích trong cấp cứu
        """)
    
    # Input section
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=65,
            step=1,
            key="crb65_age"
        )
        
        confusion = st.checkbox(
            "Lú lẫn mới khởi phát",
            key="crb65_confusion"
        )
    
    with col2:
        respiratory_rate = st.number_input(
            "Tần số thở (lần/phút)",
            min_value=0,
            max_value=60,
            value=20,
            step=1,
            key="crb65_rr"
        )
        
        col_bp1, col_bp2 = st.columns(2)
        with col_bp1:
            sbp = st.number_input(
                "Huyết áp tâm thu (mmHg)",
                min_value=0,
                max_value=300,
                value=120,
                step=1,
                key="crb65_sbp"
            )
        with col_bp2:
            dbp = st.number_input(
                "Huyết áp tâm trương (mmHg)",
                min_value=0,
                max_value=200,
                value=80,
                step=1,
                key="crb65_dbp"
            )
    
    if st.button("🔬 Tính điểm CRB-65", type="primary", use_container_width=True):
        # Validation
        errors = []
        if age < 18 or age > 120:
            errors.append("Tuổi phải từ 18-120")
        if respiratory_rate < 0 or respiratory_rate > 60:
            errors.append("Tần số thở phải từ 0-60/phút")
        if sbp < 0 or sbp > 300:
            errors.append("Huyết áp tâm thu phải từ 0-300 mmHg")
        if dbp < 0 or dbp > 200:
            errors.append("Huyết áp tâm trương phải từ 0-200 mmHg")
        if dbp >= sbp:
            errors.append("Huyết áp tâm trương phải nhỏ hơn tâm thu")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_crb65(
                age=age,
                confusion=confusion,
                respiratory_rate=respiratory_rate,
                sbp=sbp,
                dbp=dbp
            )
            
            # Display results
            st.markdown("---")
            st.markdown("### 📋 Kết quả CRB-65")
            
            # Determine risk level for color coding
            if result['score'] == 0:
                risk_level_code = "low"
            elif result['score'] <= 2:
                risk_level_code = "moderate"
            else:
                risk_level_code = "high"
            
            # Display score with color coding badge
            st.markdown(f"## CRB-65 Score = {result['score']}/4")
            render_risk_badge(
                risk_level=risk_level_code,
                label=result['risk_category'],
                value=result['score']
            )
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Điểm CRB-65", f"{result['score']}/4")
            
            with col2:
                st.metric("Nguy cơ", result['risk_category'])
            
            with col3:
                st.metric("Nguy cơ tử vong", result['mortality_risk'])
            
            # Visual Charts
            st.markdown("---")
            st.markdown("### 📊 Biểu Đồ Nguy cơ")
            col_chart1, col_chart2 = st.columns(2)
            
            with col_chart1:
                render_risk_gauge_chart(
                    value=result['score'],
                    min_value=0,
                    max_value=4,
                    thresholds={
                        'Low': 0,
                        'Moderate': 1,
                        'High': 3
                    },
                    title="CRB-65 Score"
                )
            
            with col_chart2:
                render_risk_bar_chart(
                    value=result['score'],
                    thresholds={
                        'Low': 0,
                        'Moderate': 1,
                        'High': 3
                    },
                    max_value=4,
                    title="Risk Level",
                    show_value=True
                )
            
            # Details
            st.markdown("---")
            st.markdown("### 📝 Chi tiết tính điểm")
            for detail in result['details']:
                st.markdown(f"- {detail}")
            
            # Treatment recommendation
            st.markdown("### 💡 Khuyến nghị điều trị")
            
            if result['score'] == 0:
                st.success(f"**{result['treatment']}**")
                st.markdown("""
                - Bệnh nhân có thể điều trị tại nhà
                - Kháng sinh đường uống
                - Theo dõi tại nhà
                - Tái khám nếu không cải thiện
                """)
            elif result['score'] <= 2:
                st.warning(f"**{result['treatment']}**")
                st.markdown("""
                - Cân nhắc nhập viện để theo dõi
                - Có thể điều trị ngoại trú nếu:
                  - Tình trạng ổn định
                  - Có khả năng tuân thủ điều trị
                  - Có người chăm sóc
                - Theo dõi sát tại nhà
                """)
            else:
                st.error(f"**{result['treatment']}**")
                st.markdown("""
                - **Cần nhập viện ngay**
                - Điều trị kháng sinh đường tĩnh mạch
                - Theo dõi sát tại bệnh viện
                - Có thể cần hỗ trợ hô hấp
                - Đánh giá ICU nếu cần
                """)
            
            # Prepare inputs and results for export
            inputs_dict = {
                "Tuổi": f"{age}",
                "Lú lẫn": "Có" if confusion else "Không",
                "Tần số thở": f"{respiratory_rate}/phút",
                "Huyết áp": f"{sbp}/{dbp} mmHg"
            }
            
            results_dict = {
                "CRB-65 Score": f"{result['score']}/4",
                "Nguy cơ": result['risk_category'],
                "Risk Level Code": risk_level_code,
                "Nguy cơ tử vong": result['mortality_risk'],
                "Điều trị": result['treatment'],
                "Chi tiết": "\n".join(result['details'])
            }
            
            # Export section (new component)
            st.markdown("---")
            render_scores_export(
                calculator_name="CRB-65 Score",
                inputs=inputs_dict,
                results=results_dict,
                specialty="Cấp cứu & Hô hấp"
            )
            
            # Keep old export for compatibility
            st.markdown("---")
            render_export_section(
                title=f"CRB-65 = {result['score']}/4",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="CRB-65 Score",
                filename="crb65_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="crb65",
                calculator_name="CRB-65 Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="crb65",
                calculator_name="CRB-65 Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
    
    # History
    render_history_ui(calculator_id="crb65", show_actions=True)
    
    # References
    references = get_references("CRB-65 Score")
    if references:
        render_references_section(references)

