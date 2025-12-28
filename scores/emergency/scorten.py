"""
SCORTEN Score (Severity-of-Illness Score for Toxic Epidermal Necrolysis)
==========================================================================

Estimates mortality risk in patients with Stevens-Johnson syndrome (SJS) 
and/or toxic epidermal necrolysis (TEN).

Reference:
- Bastuji-Garin S, et al. SCORTEN: a severity-of-illness score for toxic 
  epidermal necrolysis. J Invest Dermatol. 2000;115(2):149-153.

SCORTEN Components (7 factors):
- Age ≥40 years
- Heart rate ≥120 bpm
- Malignancy (present)
- Body surface area (BSA) involved ≥10%
- Serum urea >10 mmol/L (>28 mg/dL)
- Serum glucose >14 mmol/L (>252 mg/dL)
- Serum bicarbonate <20 mmol/L

Total: 0-7 points

Mortality Risk:
- 0-1 points: ~3.2%
- 2 points: ~12.1%
- 3 points: ~35.3%
- 4 points: ~58.3%
- ≥5 points: ~90.0%

Clinical Utility:
- Early mortality prediction in SJS/TEN
- Guides treatment intensity
- Helps with prognosis counseling
- Used in dermatology and burn units
"""

import streamlit as st
from scores.utils.validation import validate_age, validate_lab_value
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_scorten(
    age: int,
    heart_rate: int,
    malignancy: bool,
    bsa_involved: float,
    serum_urea: float,
    serum_glucose: float,
    serum_bicarbonate: float
) -> dict:
    """
    Calculate SCORTEN Score
    
    Args:
        age: Age (years)
        heart_rate: Heart rate (bpm)
        malignancy: Presence of malignancy
        bsa_involved: Body surface area involved (%)
        serum_urea: Serum urea (mmol/L) - can input mg/dL
        serum_glucose: Serum glucose (mmol/L) - can input mg/dL
        serum_bicarbonate: Serum bicarbonate (mmol/L)
    
    Returns:
        Dictionary with score, mortality risk, and interpretation
    """
    score = 0
    details = []
    
    # Age ≥40
    if age >= 40:
        score += 1
        details.append(f"Tuổi {age} (≥40) → +1 điểm")
    else:
        details.append(f"Tuổi {age} (<40) → 0 điểm")
    
    # Heart rate ≥120
    if heart_rate >= 120:
        score += 1
        details.append(f"Nhịp tim {heart_rate} bpm (≥120) → +1 điểm")
    else:
        details.append(f"Nhịp tim {heart_rate} bpm (<120) → 0 điểm")
    
    # Malignancy
    if malignancy:
        score += 1
        details.append("Có bệnh ác tính → +1 điểm")
    else:
        details.append("Không có bệnh ác tính → 0 điểm")
    
    # BSA ≥10%
    if bsa_involved >= 10:
        score += 1
        details.append(f"Diện tích tổn thương {bsa_involved}% (≥10%) → +1 điểm")
    else:
        details.append(f"Diện tích tổn thương {bsa_involved}% (<10%) → 0 điểm")
    
    # Serum urea >10 mmol/L (>28 mg/dL)
    # Convert mg/dL to mmol/L if needed (divide by 2.8)
    urea_mmol = serum_urea / 2.8 if serum_urea > 30 else serum_urea
    
    if urea_mmol > 10:
        score += 1
        details.append(f"Urea {serum_urea:.1f} {'mg/dL' if serum_urea > 30 else 'mmol/L'} (>10 mmol/L) → +1 điểm")
    else:
        details.append(f"Urea {serum_urea:.1f} {'mg/dL' if serum_urea > 30 else 'mmol/L'} (≤10 mmol/L) → 0 điểm")
    
    # Serum glucose >14 mmol/L (>252 mg/dL)
    # Convert mg/dL to mmol/L if needed (divide by 18)
    glucose_mmol = serum_glucose / 18 if serum_glucose > 200 else serum_glucose
    
    if glucose_mmol > 14:
        score += 1
        details.append(f"Glucose {serum_glucose:.1f} {'mg/dL' if serum_glucose > 200 else 'mmol/L'} (>14 mmol/L) → +1 điểm")
    else:
        details.append(f"Glucose {serum_glucose:.1f} {'mg/dL' if serum_glucose > 200 else 'mmol/L'} (≤14 mmol/L) → 0 điểm")
    
    # Serum bicarbonate <20 mmol/L
    if serum_bicarbonate < 20:
        score += 1
        details.append(f"Bicarbonate {serum_bicarbonate:.1f} mmol/L (<20) → +1 điểm")
    else:
        details.append(f"Bicarbonate {serum_bicarbonate:.1f} mmol/L (≥20) → 0 điểm")
    
    # Mortality risk based on score
    mortality_risks = {
        0: 3.2,
        1: 3.2,
        2: 12.1,
        3: 35.3,
        4: 58.3,
        5: 90.0,
        6: 90.0,
        7: 90.0
    }
    
    mortality_risk = mortality_risks.get(score, 90.0)
    
    # Risk category
    if score <= 1:
        risk_category = "Nguy cơ tử vong thấp"
    elif score == 2:
        risk_category = "Nguy cơ tử vong trung bình"
    elif score <= 4:
        risk_category = "Nguy cơ tử vong cao"
    else:
        risk_category = "Nguy cơ tử vong rất cao"
    
    return {
        "score": score,
        "mortality_risk": mortality_risk,
        "risk_category": risk_category,
        "details": details
    }


def render():
    """Render SCORTEN Score interface"""
    import streamlit as st
    
    st.set_page_config(page_title="SCORTEN Score", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🩺 SCORTEN Score</h2>
    <p style='text-align: center; color: #6B7280;'>
    Severity-of-Illness Score for Toxic Epidermal Necrolysis<br>
    Ước tính nguy cơ tử vong ở bệnh nhân hội chứng Stevens-Johnson (SJS) và/hoặc hoại tử biểu bì nhiễm độc (TEN)
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về SCORTEN Score"):
        st.markdown("""
        **SCORTEN Score** là thang điểm đánh giá mức độ nặng và dự đoán tử vong 
        ở bệnh nhân hội chứng Stevens-Johnson (SJS) và hoại tử biểu bì nhiễm độc (TEN).
        
        ### Các thành phần (7 yếu tố):
        1. Tuổi ≥40
        2. Nhịp tim ≥120 bpm
        3. Có bệnh ác tính
        4. Diện tích tổn thương ≥10%
        5. Urea huyết thanh >10 mmol/L (>28 mg/dL)
        6. Glucose huyết thanh >14 mmol/L (>252 mg/dL)
        7. Bicarbonate huyết thanh <20 mmol/L
        
        ### Nguy cơ tử vong theo điểm:
        - **0-1 điểm:** ~3.2%
        - **2 điểm:** ~12.1%
        - **3 điểm:** ~35.3%
        - **4 điểm:** ~58.3%
        - **≥5 điểm:** ~90.0%
        
        ### Ứng dụng lâm sàng:
        - Dự đoán tử vong sớm trong SJS/TEN
        - Hướng dẫn cường độ điều trị
        - Tư vấn tiên lượng
        - Dùng trong da liễu và đơn vị bỏng
        """)
    
    # Input section
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=0,
            max_value=120,
            value=50,
            step=1,
            key="scorten_age"
        )
        
        heart_rate = st.number_input(
            "Nhịp tim (bpm)",
            min_value=40,
            max_value=200,
            value=80,
            step=1,
            key="scorten_hr"
        )
        
        malignancy = st.checkbox(
            "Có bệnh ác tính",
            key="scorten_malignancy"
        )
    
    with col2:
        bsa_involved = st.number_input(
            "Diện tích tổn thương (%)",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=0.1,
            format="%.1f",
            key="scorten_bsa"
        )
    
    st.markdown("### 🧪 Xét nghiệm")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        serum_urea = st.number_input(
            "Urea huyết thanh (mg/dL hoặc mmol/L)",
            min_value=0.0,
            max_value=200.0,
            value=30.0,
            step=0.1,
            format="%.1f",
            key="scorten_urea",
            help="Nhập mg/dL (nếu >30) hoặc mmol/L (nếu <30)"
        )
    
    with col2:
        serum_glucose = st.number_input(
            "Glucose huyết thanh (mg/dL hoặc mmol/L)",
            min_value=0.0,
            max_value=500.0,
            value=100.0,
            step=1.0,
            format="%.1f",
            key="scorten_glucose",
            help="Nhập mg/dL (nếu >200) hoặc mmol/L (nếu <200)"
        )
    
    with col3:
        serum_bicarbonate = st.number_input(
            "Bicarbonate huyết thanh (mmol/L)",
            min_value=0.0,
            max_value=50.0,
            value=24.0,
            step=0.1,
            format="%.1f",
            key="scorten_bicarb"
        )
    
    if st.button("🔬 Tính điểm SCORTEN", type="primary", use_container_width=True):
        # Validation
        errors = []
        if age < 0 or age > 120:
            errors.append("Tuổi phải từ 0-120")
        if heart_rate < 40 or heart_rate > 200:
            errors.append("Nhịp tim phải từ 40-200 bpm")
        if bsa_involved < 0 or bsa_involved > 100:
            errors.append("Diện tích tổn thương phải từ 0-100%")
        if serum_urea < 0 or serum_urea > 200:
            errors.append("Urea phải từ 0-200")
        if serum_glucose < 0 or serum_glucose > 500:
            errors.append("Glucose phải từ 0-500")
        if serum_bicarbonate < 0 or serum_bicarbonate > 50:
            errors.append("Bicarbonate phải từ 0-50 mmol/L")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_scorten(
                age=age,
                heart_rate=heart_rate,
                malignancy=malignancy,
                bsa_involved=bsa_involved,
                serum_urea=serum_urea,
                serum_glucose=serum_glucose,
                serum_bicarbonate=serum_bicarbonate
            )
            
            # Display results
            st.markdown("---")
            st.markdown("### 📋 Kết quả SCORTEN")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Điểm SCORTEN", f"{result['score']}/7")
            
            with col2:
                st.metric(
                    "Nguy cơ tử vong",
                    f"{result['mortality_risk']:.1f}%"
                )
            
            with col3:
                st.metric(
                    "Phân loại",
                    result['risk_category']
                )
            
            # Details
            st.markdown("### 📝 Chi tiết tính điểm")
            for detail in result['details']:
                st.markdown(f"- {detail}")
            
            # Clinical interpretation
            st.markdown("### 💡 Khuyến nghị lâm sàng")
            
            if result['score'] <= 1:
                st.success(f"**{result['risk_category']}** - Tiên lượng tốt")
                st.markdown("""
                - Điều trị hỗ trợ tích cực
                - Theo dõi sát tại bệnh viện
                - Chăm sóc vết thương da
                - Phòng ngừa nhiễm trùng
                """)
            elif result['score'] == 2:
                st.warning(f"**{result['risk_category']}** - Cần theo dõi sát")
                st.markdown("""
                - Điều trị tại đơn vị chuyên khoa
                - Cân nhắc chuyển ICU
                - Điều trị hỗ trợ toàn diện
                - Tư vấn gia đình về tiên lượng
                """)
            elif result['score'] <= 4:
                st.error(f"**{result['risk_category']}** - Tiên lượng xấu")
                st.markdown("""
                - **Điều trị tại ICU**
                - Điều trị hỗ trợ tích cực
                - Cân nhắc điều trị đặc hiệu (IVIG, cyclosporine)
                - Tư vấn gia đình về tiên lượng nghiêm trọng
                - Chăm sóc giảm nhẹ nếu cần
                """)
            else:
                st.error(f"**{result['risk_category']}** - Tiên lượng rất xấu")
                st.markdown("""
                - **Điều trị tại ICU ngay lập tức**
                - Điều trị hỗ trợ tối đa
                - Cân nhắc tất cả các phương pháp điều trị
                - Tư vấn gia đình về tiên lượng rất nghiêm trọng
                - Chăm sóc giảm nhẹ và hỗ trợ tâm lý
                """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="scorten",
                calculator_name="SCORTEN Score",
                inputs={
                    "Tuổi": f"{age}",
                    "Nhịp tim": f"{heart_rate} bpm",
                    "Bệnh ác tính": "Có" if malignancy else "Không",
                    "Diện tích tổn thương": f"{bsa_involved:.1f}%",
                    "Urea": f"{serum_urea:.1f}",
                    "Glucose": f"{serum_glucose:.1f}",
                    "Bicarbonate": f"{serum_bicarbonate:.1f}"
                },
                result={
                    "Điểm": f"{result['score']}/7",
                    "Nguy cơ tử vong": f"{result['mortality_risk']:.1f}%",
                    "Phân loại": result['risk_category']
                }
            )
            
            # Share and export
            render_share_section(
                calculator_id="scorten",
                calculator_name="SCORTEN Score"
            )
            
            render_export_section(
                calculator_id="scorten",
                calculator_name="SCORTEN Score",
                data={
                    "inputs": {
                        "age": age,
                        "heart_rate": heart_rate,
                        "malignancy": malignancy,
                        "bsa_involved": bsa_involved,
                        "serum_urea": serum_urea,
                        "serum_glucose": serum_glucose,
                        "serum_bicarbonate": serum_bicarbonate
                    },
                    "result": result
                }
            )
    
    # History
    render_history_ui(calculator_id="scorten", show_actions=True)
    
    # References
    references = get_references("SCORTEN Score")
    if references:
        render_references_section(references)

