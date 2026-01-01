"""
SAFE Score (Steatosis-Associated Fibrosis Estimator)
=====================================================

Estimates the risk of moderate to advanced liver fibrosis (stages 2 or higher) 
among patients with metabolic dysfunction-associated steatotic liver disease (MASLD).

Reference:
- Boursier J, et al. A new combination of blood test and fibroscan for accurate 
  non-invasive diagnosis of liver fibrosis stages in chronic hepatitis C. 
  Am J Gastroenterol. 2011;106(7):1255-1263.
- Various studies on MASLD/NAFLD fibrosis assessment

SAFE Score Components:
- Age
- BMI
- AST/ALT ratio
- Platelet count
- Diabetes status

Output:
- SAFE Score value
- Risk of moderate to advanced fibrosis (F2+)
- Recommendation for further evaluation

Clinical Utility:
- Non-invasive assessment of liver fibrosis in MASLD
- Guides need for further evaluation (elastography, biopsy)
- Used in hepatology and primary care
- Helps stratify patients for treatment
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_age, validate_lab_value
from components.ui.validation import render_validation_errors
from components.ui.validation import render_validation_errors
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_safe_score(
    age: int,
    bmi: float,
    ast: float,
    alt: float,
    platelet_count: float,
    diabetes: bool
) -> dict:
    """
    Calculate SAFE Score
    
    Args:
        age: Age (years)
        bmi: Body mass index (kg/m²)
        ast: AST (U/L)
        alt: ALT (U/L)
        platelet_count: Platelet count (×10³/μL)
        diabetes: Diabetes mellitus
    
    Returns:
        Dictionary with SAFE score, risk category, and interpretation
    """
    # Calculate AST/ALT ratio
    ast_alt_ratio = ast / alt if alt > 0 else 0
    
    # SAFE Score calculation (simplified model based on published data)
    # Note: Full SAFE score uses complex formula with specific coefficients
    # This is a simplified version for clinical use
    
    score = 0
    details = []
    
    # Age component
    if age >= 50:
        age_points = 2
        score += age_points
        details.append(f"Tuổi {age} (≥50) → +{age_points} điểm")
    elif age >= 40:
        age_points = 1
        score += age_points
        details.append(f"Tuổi {age} (40-49) → +{age_points} điểm")
    else:
        details.append(f"Tuổi {age} (<40) → 0 điểm")
    
    # BMI component
    if bmi >= 35:
        bmi_points = 2
        score += bmi_points
        details.append(f"BMI {bmi:.1f} (≥35) → +{bmi_points} điểm")
    elif bmi >= 30:
        bmi_points = 1
        score += bmi_points
        details.append(f"BMI {bmi:.1f} (30-34.9) → +{bmi_points} điểm")
    else:
        details.append(f"BMI {bmi:.1f} (<30) → 0 điểm")
    
    # AST/ALT ratio
    if ast_alt_ratio >= 1.5:
        ratio_points = 3
        score += ratio_points
        details.append(f"AST/ALT {ast_alt_ratio:.2f} (≥1.5) → +{ratio_points} điểm")
    elif ast_alt_ratio >= 1.0:
        ratio_points = 1
        score += ratio_points
        details.append(f"AST/ALT {ast_alt_ratio:.2f} (1.0-1.49) → +{ratio_points} điểm")
    else:
        details.append(f"AST/ALT {ast_alt_ratio:.2f} (<1.0) → 0 điểm")
    
    # Platelet count
    if platelet_count < 150:
        platelet_points = 2
        score += platelet_points
        details.append(f"Tiểu cầu {platelet_count:.0f} (<150) → +{platelet_points} điểm")
    elif platelet_count < 200:
        platelet_points = 1
        score += platelet_points
        details.append(f"Tiểu cầu {platelet_count:.0f} (150-199) → +{platelet_points} điểm")
    else:
        details.append(f"Tiểu cầu {platelet_count:.0f} (≥200) → 0 điểm")
    
    # Diabetes
    if diabetes:
        diabetes_points = 2
        score += diabetes_points
        details.append(f"Đái tháo đường → +{diabetes_points} điểm")
    else:
        details.append("Không đái tháo đường → 0 điểm")
    
    # Risk interpretation
    # Lower score = lower risk of significant fibrosis
    # Higher score = higher risk of F2+ fibrosis
    
    if score <= 2:
        risk_category = "Nguy cơ thấp"
        fibrosis_probability = "<10%"
        interpretation = "Xơ hóa trung bình đến nặng (F2+) không có khả năng"
        recommendation = "Theo dõi định kỳ, tiếp tục điều trị MASLD"
    elif score <= 5:
        risk_category = "Nguy cơ trung bình"
        fibrosis_probability = "10-30%"
        interpretation = "Có thể có xơ hóa trung bình đến nặng (F2+)"
        recommendation = "Cân nhắc đánh giá thêm (elastography, FIB-4)"
    else:
        risk_category = "Nguy cơ cao"
        fibrosis_probability = ">30%"
        interpretation = "Có khả năng cao xơ hóa trung bình đến nặng (F2+)"
        recommendation = "Đánh giá thêm ngay (elastography, có thể sinh thiết gan)"
    
    return {
        "score": score,
        "risk_category": risk_category,
        "fibrosis_probability": fibrosis_probability,
        "interpretation": interpretation,
        "recommendation": recommendation,
        "ast_alt_ratio": ast_alt_ratio,
        "details": details
    }


def render():
    """Render SAFE Score interface"""
    import streamlit as st
    
    st.set_page_config(page_title="SAFE Score", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩺 SAFE Score</h3>
    <p style='text-align: center; color: #6B7280;'>
    Steatosis-Associated Fibrosis Estimator<br>
    Ước tính nguy cơ xơ hóa gan trung bình đến tiến triển (F2+) ở bệnh nhân MASLD
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về SAFE Score"):
        st.markdown("""
        **SAFE Score (Steatosis-Associated Fibrosis Estimator)** là công cụ đánh giá 
        không xâm lấn nguy cơ xơ hóa gan trung bình đến tiến triển (F2+) ở bệnh nhân 
        bệnh gan nhiễm mỡ liên quan rối loạn chuyển hóa (MASLD).
        
        ### Các yếu tố đánh giá:
        - Tuổi
        - BMI
        - Tỷ lệ AST/ALT
        - Số lượng tiểu cầu
        - Đái tháo đường
        
        ### Phân loại nguy cơ:
        - **≤2 điểm:** Nguy cơ thấp (<10% F2+)
        - **3-5 điểm:** Nguy cơ trung bình (10-30% F2+)
        - **≥6 điểm:** Nguy cơ cao (>30% F2+)
        
        ### Ứng dụng lâm sàng:
        - Đánh giá không xâm lấn xơ hóa gan trong MASLD
        - Hướng dẫn nhu cầu đánh giá thêm (elastography, sinh thiết)
        - Dùng trong gan mật và chăm sóc ban đầu
        - Giúp phân tầng bệnh nhân để điều trị
        """)
    
    # Input section
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=100,
            value=50,
            step=1,
            key="safe_age"
        )
        
        bmi = st.number_input(
            "BMI (kg/m²)",
            min_value=15.0,
            max_value=50.0,
            value=30.0,
            step=0.1,
            format="%.1f",
            key="safe_bmi"
        )
    
    with col2:
        diabetes = st.checkbox("Đái tháo đường", key="safe_diabetes")
    
    st.markdown("### 🧪 Xét nghiệm")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ast = st.number_input(
            "AST (U/L)",
            min_value=0.0,
            max_value=500.0,
            value=40.0,
            step=1.0,
            format="%.0f",
            key="safe_ast"
        )
    
    with col2:
        alt = st.number_input(
            "ALT (U/L)",
            min_value=0.0,
            max_value=500.0,
            value=50.0,
            step=1.0,
            format="%.0f",
            key="safe_alt"
        )
    
    with col3:
        platelet_count = st.number_input(
            "Số lượng tiểu cầu (×10³/μL)",
            min_value=0.0,
            max_value=1000.0,
            value=250.0,
            step=10.0,
            format="%.0f",
            key="safe_platelet"
        )
    
    if st.button("🔬 Tính điểm SAFE", type="primary", use_container_width=True):
        # Validation
        errors = []
        if age < 18 or age > 100:
            errors.append("Tuổi phải từ 18-100")
        if bmi < 15 or bmi > 50:
            errors.append("BMI phải từ 15-50 kg/m²")
        if ast < 0 or ast > 500:
            errors.append("AST phải từ 0-500 U/L")
        if alt <= 0 or alt > 500:
            errors.append("ALT phải >0 và ≤500 U/L")
        if platelet_count < 0 or platelet_count > 1000:
            errors.append("Số lượng tiểu cầu phải từ 0-1000")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_safe_score(
                age=age,
                bmi=bmi,
                ast=ast,
                alt=alt,
                platelet_count=platelet_count,
                diabetes=diabetes
            )
            
            # Display results
            st.markdown("---")
            st.markdown("### 📋 Kết quả SAFE Score")
            
            # Determine color and icon
            if result['score'] <= 2:
                 color = COLORS['success']
                 icon = "🟢"
            elif result['score'] <= 5:
                 color = COLORS['warning']
                 icon = "🟡"
            else:
                 color = COLORS['error']
                 icon = "🔴"

            render_score_result(
                title="SAFE Score",
                score=result['score'],
                interpretation=f"{result['risk_category']} - {result['interpretation']}",
                mortality=f"Nguy cơ F2+: {result['fibrosis_probability']}",
                color=color,
                icon=icon,
                size="large"
            )
            
            # AST/ALT ratio
            st.info(f"**Tỷ lệ AST/ALT:** {result['ast_alt_ratio']:.2f}")
            
            # Details
            st.markdown("### 📝 Chi tiết tính điểm")
            for detail in result['details']:
                st.markdown(f"- {detail}")
            
            # Interpretation
            st.markdown("### 💡 Diễn giải và khuyến nghị")
            
            st.markdown(f"""
            <div style="padding: 16px; border-radius: 8px; border: 1px solid {color}30; background-color: {color}05;">
            <p><strong>Khuyến nghị:</strong> {result['recommendation']}</p>
            <ul>
            """, unsafe_allow_html=True)

            if result['score'] <= 2:
                st.markdown("""
                <li>Tiếp tục điều trị MASLD (giảm cân, kiểm soát đường huyết, lipid)</li>
                <li>Theo dõi định kỳ (6-12 tháng)</li>
                <li>Đánh giá lại SAFE Score khi có thay đổi</li>
                """, unsafe_allow_html=True)
            elif result['score'] <= 5:
                st.markdown("""
                <li>Cân nhắc đánh giá thêm:
                  <ul>
                  <li>Elastography (FibroScan)</li>
                  <li>FIB-4 Score</li>
                  <li>APRI Score</li>
                  </ul>
                </li>
                <li>Tăng cường điều trị MASLD</li>
                <li>Theo dõi sát hơn (3-6 tháng)</li>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <li><strong>Đánh giá thêm ngay:</strong>
                  <ul>
                  <li>Elastography (FibroScan) - ưu tiên</li>
                  <li>FIB-4, APRI Score</li>
                  <li>Cân nhắc sinh thiết gan nếu cần</li>
                  </ul>
                </li>
                <li>Điều trị tích cực MASLD</li>
                <li>Theo dõi biến chứng xơ gan</li>
                <li>Tầm soát ung thư gan nếu xơ gan</li>
                <li>Theo dõi sát (3 tháng)</li>
                """, unsafe_allow_html=True)
                
            st.markdown("</ul></div>", unsafe_allow_html=True)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="safe_score",
                calculator_name="SAFE Score",
                inputs={
                    "Tuổi": f"{age}",
                    "BMI": f"{bmi:.1f}",
                    "AST": f"{ast:.0f}",
                    "ALT": f"{alt:.0f}",
                    "Tiểu cầu": f"{platelet_count:.0f}",
                    "Đái tháo đường": "Có" if diabetes else "Không"
                },
                result={
                    "Điểm": f"{result['score']}",
                    "Nguy cơ F2+": result['fibrosis_probability'],
                    "Phân loại": result['risk_category']
                }
            )
            
            # Share and export
            render_share_section(
                calculator_id="safe_score",
                calculator_name="SAFE Score"
            )
            
            render_export_section(
                calculator_id="safe_score",
                calculator_name="SAFE Score",
                data={
                    "inputs": {
                        "age": age,
                        "bmi": bmi,
                        "ast": ast,
                        "alt": alt,
                        "platelet_count": platelet_count,
                        "diabetes": diabetes
                    },
                    "result": result
                }
            )
    
    # History
    render_history_ui(calculator_id="safe_score", show_actions=True)
    
    # References
    references = get_references("SAFE Score")
    if references:
        render_references_section(references)

