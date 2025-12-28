"""
Weight-based Levothyroxine Dose Calculator for Hypothyroidism in Adults
========================================================================

Determines a weight-based levothyroxine dose for treatment of primary hypothyroidism.

Reference:
- Various clinical guidelines and studies on levothyroxine dosing
- Standard practice: 1.6-1.8 mcg/kg/day for adults
- Adjustments for age, cardiac disease, pregnancy

Calculation:
- Base dose: Weight (kg) × 1.6-1.8 mcg/kg/day
- Age adjustments: Lower dose for elderly
- Cardiac considerations: Start lower if cardiac disease
- Pregnancy: Higher dose needed

Output:
- Recommended starting dose (mcg/day)
- Dose adjustments based on clinical factors
- Monitoring recommendations

Clinical Utility:
- Initial dose calculation for hypothyroidism
- Used daily in endocrinology and primary care
- Helps prevent over/under treatment
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


def calculate_levothyroxine_dose(
    weight_kg: float,
    age: int,
    cardiac_disease: bool,
    pregnancy: bool,
    severe_hypothyroidism: bool
) -> dict:
    """
    Calculate weight-based levothyroxine dose
    
    Args:
        weight_kg: Weight in kilograms
        age: Age in years
        cardiac_disease: Presence of cardiac disease
        pregnancy: Pregnant
        severe_hypothyroidism: Severe hypothyroidism (TSH >50)
    
    Returns:
        Dictionary with recommended dose and adjustments
    """
    # Base dose calculation: 1.6-1.8 mcg/kg/day
    base_dose_per_kg = 1.7  # Average of 1.6-1.8
    base_dose = weight_kg * base_dose_per_kg
    
    adjustments = []
    final_dose = base_dose
    
    # Age adjustments
    if age >= 70:
        # Elderly: reduce by 20-25%
        age_adjustment = -0.25
        final_dose = final_dose * (1 + age_adjustment)
        adjustments.append(f"Tuổi ≥70: Giảm 25% (nguy cơ tim mạch)")
    elif age >= 60:
        # Older adults: reduce by 10-15%
        age_adjustment = -0.15
        final_dose = final_dose * (1 + age_adjustment)
        adjustments.append(f"Tuổi 60-69: Giảm 15%")
    
    # Cardiac disease: start lower
    if cardiac_disease:
        cardiac_adjustment = -0.25
        final_dose = final_dose * (1 + cardiac_adjustment)
        adjustments.append("Bệnh tim mạch: Giảm 25% (bắt đầu thấp hơn)")
    
    # Pregnancy: increase dose
    if pregnancy:
        pregnancy_adjustment = 0.3
        final_dose = final_dose * (1 + pregnancy_adjustment)
        adjustments.append("Mang thai: Tăng 30% (nhu cầu tăng)")
    
    # Severe hypothyroidism: may need higher starting dose
    if severe_hypothyroidism and not cardiac_disease and age < 60:
        severe_adjustment = 0.1
        final_dose = final_dose * (1 + severe_adjustment)
        adjustments.append("Suy giáp nặng (TSH >50): Tăng 10%")
    
    # Round to nearest 12.5 or 25 mcg (common tablet strengths)
    # Common strengths: 25, 50, 75, 88, 100, 112, 125, 137, 150, 175, 200 mcg
    if final_dose <= 25:
        rounded_dose = 25
    elif final_dose <= 37.5:
        rounded_dose = 37.5  # 25 + 12.5
    elif final_dose <= 50:
        rounded_dose = 50
    elif final_dose <= 62.5:
        rounded_dose = 62.5  # 50 + 12.5
    elif final_dose <= 75:
        rounded_dose = 75
    elif final_dose <= 87.5:
        rounded_dose = 87.5  # 75 + 12.5
    elif final_dose <= 100:
        rounded_dose = 100
    elif final_dose <= 112.5:
        rounded_dose = 112.5  # 100 + 12.5
    elif final_dose <= 125:
        rounded_dose = 125
    elif final_dose <= 137.5:
        rounded_dose = 137.5  # 125 + 12.5
    elif final_dose <= 150:
        rounded_dose = 150
    elif final_dose <= 175:
        rounded_dose = 175
    elif final_dose <= 200:
        rounded_dose = 200
    else:
        rounded_dose = round(final_dose / 25) * 25  # Round to nearest 25
    
    # Dose range
    dose_range_low = rounded_dose - 12.5
    dose_range_high = rounded_dose + 12.5
    
    return {
        "base_dose": base_dose,
        "final_dose": final_dose,
        "rounded_dose": rounded_dose,
        "dose_range": (dose_range_low, dose_range_high),
        "adjustments": adjustments,
        "dose_per_kg": final_dose / weight_kg if weight_kg > 0 else 0
    }


def render():
    """Render Weight-based Levothyroxine Dose Calculator interface"""
    import streamlit as st
    
    st.set_page_config(page_title="Levothyroxine Dose Calculator", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>💉 Weight-based Levothyroxine Dose Calculator</h2>
    <p style='text-align: center; color: #6B7280;'>
    Xác định liều levothyroxine dựa trên cân nặng để điều trị suy giáp nguyên phát ở người lớn
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Levothyroxine Dose Calculator"):
        st.markdown("""
        **Weight-based Levothyroxine Dose Calculator** là công cụ tính liều levothyroxine 
        dựa trên cân nặng để điều trị suy giáp nguyên phát ở người lớn.
        
        ### Công thức cơ bản:
        - **Liều cơ bản:** 1.6-1.8 mcg/kg/ngày
        - **Trung bình:** 1.7 mcg/kg/ngày
        
        ### Điều chỉnh liều:
        - **Tuổi ≥70:** Giảm 25% (nguy cơ tim mạch)
        - **Tuổi 60-69:** Giảm 15%
        - **Bệnh tim mạch:** Giảm 25% (bắt đầu thấp hơn)
        - **Mang thai:** Tăng 30% (nhu cầu tăng)
        - **Suy giáp nặng (TSH >50):** Tăng 10% (nếu không có bệnh tim, tuổi <60)
        
        ### Theo dõi:
        - Kiểm tra TSH sau 6-8 tuần
        - Điều chỉnh liều theo TSH
        - Mục tiêu TSH: 0.5-2.5 mIU/L (người trẻ) hoặc 1-3 mIU/L (người già)
        
        ### Ứng dụng lâm sàng:
        - Tính liều ban đầu cho suy giáp
        - Dùng hàng ngày trong nội tiết và chăm sóc ban đầu
        - Giúp tránh điều trị quá mức/thiếu
        """)
    
    # Input section
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=200.0,
            value=70.0,
            step=0.5,
            format="%.1f",
            key="levo_weight"
        )
        
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=50,
            step=1,
            key="levo_age"
        )
    
    with col2:
        cardiac_disease = st.checkbox(
            "Có bệnh tim mạch",
            key="levo_cardiac",
            help="Bệnh mạch vành, suy tim, rối loạn nhịp tim"
        )
        
        pregnancy = st.checkbox(
            "Đang mang thai",
            key="levo_pregnancy"
        )
        
        severe_hypothyroidism = st.checkbox(
            "Suy giáp nặng (TSH >50)",
            key="levo_severe"
        )
    
    if st.button("🔬 Tính liều Levothyroxine", type="primary", use_container_width=True):
        # Validation
        errors = []
        if weight_kg < 30 or weight_kg > 200:
            errors.append("Cân nặng phải từ 30-200 kg")
        if age < 18 or age > 120:
            errors.append("Tuổi phải từ 18-120")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_levothyroxine_dose(
                weight_kg=weight_kg,
                age=age,
                cardiac_disease=cardiac_disease,
                pregnancy=pregnancy,
                severe_hypothyroidism=severe_hypothyroidism
            )
            
            # Display results
            st.markdown("---")
            st.markdown("### 📋 Kết quả tính liều")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Liều cơ bản",
                    f"{result['base_dose']:.0f} mcg/ngày"
                )
            
            with col2:
                st.metric(
                    "Liều đề xuất",
                    f"{result['rounded_dose']:.0f} mcg/ngày"
                )
            
            with col3:
                st.metric(
                    "Liều/kg",
                    f"{result['dose_per_kg']:.2f} mcg/kg/ngày"
                )
            
            # Adjustments
            if result['adjustments']:
                st.markdown("### 📝 Các điều chỉnh")
                for adjustment in result['adjustments']:
                    st.markdown(f"- {adjustment}")
            
            # Dose range
            st.info(f"**Khoảng liều:** {result['dose_range'][0]:.0f} - {result['dose_range'][1]:.0f} mcg/ngày")
            
            # Clinical recommendations
            st.markdown("### 💡 Khuyến nghị lâm sàng")
            
            st.markdown(f"""
            **Liều khởi đầu đề xuất: {result['rounded_dose']:.0f} mcg/ngày**
            
            **Cách dùng:**
            - Uống khi đói, 30-60 phút trước bữa ăn
            - Uống vào buổi sáng, cùng thời điểm mỗi ngày
            - Tránh dùng cùng với: sắt, canxi, thuốc kháng acid, cà phê
            
            **Theo dõi:**
            - Kiểm tra TSH sau **6-8 tuần**
            - Điều chỉnh liều theo TSH:
              - TSH > mục tiêu: Tăng liều 12.5-25 mcg
              - TSH < mục tiêu: Giảm liều 12.5-25 mcg
            - Mục tiêu TSH:
              - Người trẻ (<70 tuổi): 0.5-2.5 mIU/L
              - Người già (≥70 tuổi): 1-3 mIU/L
            
            **Lưu ý đặc biệt:**
            """)
            
            if cardiac_disease:
                st.warning("""
                - **Bệnh tim mạch:** Bắt đầu với liều thấp hơn, tăng dần từ từ
                - Theo dõi triệu chứng tim mạch
                - Tăng liều mỗi 4-6 tuần, mỗi lần 12.5-25 mcg
                """)
            
            if pregnancy:
                st.warning("""
                - **Mang thai:** Nhu cầu tăng 30-50%
                - Kiểm tra TSH mỗi 4 tuần trong tam cá nguyệt đầu
                - Mục tiêu TSH: <2.5 mIU/L trong tam cá nguyệt đầu, <3.0 mIU/L sau đó
                """)
            
            if age >= 70:
                st.info("""
                - **Người già:** Bắt đầu với liều thấp hơn
                - Tăng liều từ từ, theo dõi triệu chứng
                - Mục tiêu TSH: 1-3 mIU/L (tránh điều trị quá mức)
                """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="levothyroxine_dose",
                calculator_name="Levothyroxine Dose Calculator",
                inputs={
                    "Cân nặng": f"{weight_kg:.1f} kg",
                    "Tuổi": f"{age}",
                    "Bệnh tim": "Có" if cardiac_disease else "Không",
                    "Mang thai": "Có" if pregnancy else "Không",
                    "Suy giáp nặng": "Có" if severe_hypothyroidism else "Không"
                },
                result={
                    "Liều đề xuất": f"{result['rounded_dose']:.0f} mcg/ngày",
                    "Liều/kg": f"{result['dose_per_kg']:.2f} mcg/kg/ngày"
                }
            )
            
            # Share and export
            render_share_section(
                calculator_id="levothyroxine_dose",
                calculator_name="Levothyroxine Dose Calculator"
            )
            
            render_export_section(
                calculator_id="levothyroxine_dose",
                calculator_name="Levothyroxine Dose Calculator",
                data={
                    "inputs": {
                        "weight_kg": weight_kg,
                        "age": age,
                        "cardiac_disease": cardiac_disease,
                        "pregnancy": pregnancy,
                        "severe_hypothyroidism": severe_hypothyroidism
                    },
                    "result": result
                }
            )
    
    # History
    render_history_ui(calculator_id="levothyroxine_dose", show_actions=True)
    
    # References
    references = get_references("Levothyroxine Dose Calculator")
    if references:
        render_references_section(references)

