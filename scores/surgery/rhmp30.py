"""
RHMP-30 (Rotterdam Hip Fracture Mortality Prediction-30 Days)
=============================================================

Predicts 30-day mortality risk after hip fracture surgery.

Reference:
- Moerman S, et al. Thirty-day mortality after hip fracture surgery: 
  predictive factors and the effect of hospital volume. 
  Bone Joint J. 2016;98-B(3):341-348.

RHMP-30 Components:
- Age
- Sex
- ASA classification
- Type of fracture
- Preoperative hemoglobin
- Preoperative creatinine
- Time to surgery
- Type of anesthesia

Output:
- 30-day mortality risk (%)

Clinical Utility:
- Preoperative risk assessment
- Guides treatment decisions
- Helps with patient counseling
- Used in orthopedic surgery
"""

import streamlit as st
from scores.utils.validation import validate_age, validate_lab_value
from components.ui.validation import render_validation_errors
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_rhmp30(
    age: int,
    is_female: bool,
    asa_class: int,
    fracture_type: str,
    hemoglobin: float,
    creatinine: float,
    time_to_surgery_hours: float,
    general_anesthesia: bool
) -> dict:
    """
    Calculate RHMP-30 Score
    
    Args:
        age: Age (years)
        is_female: Female sex
        asa_class: ASA classification (1-5)
        fracture_type: Type of fracture (intracapsular, extracapsular, subtrochanteric)
        hemoglobin: Preoperative hemoglobin (g/dL)
        creatinine: Preoperative creatinine (mg/dL)
        time_to_surgery_hours: Time to surgery (hours)
        general_anesthesia: General anesthesia (vs regional)
    
    Returns:
        Dictionary with 30-day mortality risk and interpretation
    """
    score = 0
    details = []
    
    # Age (major factor)
    if age >= 90:
        age_points = 4
        score += age_points
        details.append(f"Tuổi {age} (≥90) → +{age_points} điểm")
    elif age >= 80:
        age_points = 3
        score += age_points
        details.append(f"Tuổi {age} (80-89) → +{age_points} điểm")
    elif age >= 70:
        age_points = 2
        score += age_points
        details.append(f"Tuổi {age} (70-79) → +{age_points} điểm")
    elif age >= 60:
        age_points = 1
        score += age_points
        details.append(f"Tuổi {age} (60-69) → +{age_points} điểm")
    else:
        details.append(f"Tuổi {age} (<60) → 0 điểm")
    
    # Sex (males higher risk)
    if not is_female:
        score += 1
        details.append("Giới tính nam → +1 điểm")
    else:
        details.append("Giới tính nữ → 0 điểm")
    
    # ASA classification
    if asa_class >= 4:
        asa_points = 3
        score += asa_points
        details.append(f"ASA {asa_class} (≥4) → +{asa_points} điểm")
    elif asa_class == 3:
        asa_points = 2
        score += asa_points
        details.append(f"ASA {asa_class} → +{asa_points} điểm")
    elif asa_class == 2:
        asa_points = 1
        score += asa_points
        details.append(f"ASA {asa_class} → +{asa_points} điểm")
    else:
        details.append(f"ASA {asa_class} (1) → 0 điểm")
    
    # Fracture type
    if fracture_type == "subtrochanteric":
        fracture_points = 2
        score += fracture_points
        details.append(f"Gãy dưới mấu chuyển → +{fracture_points} điểm")
    elif fracture_type == "extracapsular":
        fracture_points = 1
        score += fracture_points
        details.append(f"Gãy ngoài bao khớp → +{fracture_points} điểm")
    else:
        details.append(f"Gãy trong bao khớp → 0 điểm")
    
    # Hemoglobin
    if hemoglobin < 10:
        hb_points = 2
        score += hb_points
        details.append(f"Hemoglobin {hemoglobin:.1f} g/dL (<10) → +{hb_points} điểm")
    elif hemoglobin < 12:
        hb_points = 1
        score += hb_points
        details.append(f"Hemoglobin {hemoglobin:.1f} g/dL (10-11.9) → +{hb_points} điểm")
    else:
        details.append(f"Hemoglobin {hemoglobin:.1f} g/dL (≥12) → 0 điểm")
    
    # Creatinine
    if creatinine >= 2.0:
        cr_points = 2
        score += cr_points
        details.append(f"Creatinine {creatinine:.2f} mg/dL (≥2.0) → +{cr_points} điểm")
    elif creatinine >= 1.5:
        cr_points = 1
        score += cr_points
        details.append(f"Creatinine {creatinine:.2f} mg/dL (1.5-1.9) → +{cr_points} điểm")
    else:
        details.append(f"Creatinine {creatinine:.2f} mg/dL (<1.5) → 0 điểm")
    
    # Time to surgery
    if time_to_surgery_hours >= 48:
        time_points = 2
        score += time_points
        details.append(f"Thời gian đến phẫu thuật {time_to_surgery_hours:.1f}h (≥48h) → +{time_points} điểm")
    elif time_to_surgery_hours >= 24:
        time_points = 1
        score += time_points
        details.append(f"Thời gian đến phẫu thuật {time_to_surgery_hours:.1f}h (24-47.9h) → +{time_points} điểm")
    else:
        details.append(f"Thời gian đến phẫu thuật {time_to_surgery_hours:.1f}h (<24h) → 0 điểm")
    
    # Anesthesia type
    if general_anesthesia:
        score += 1
        details.append("Gây mê toàn thân → +1 điểm")
    else:
        details.append("Gây mê vùng → 0 điểm")
    
    # Calculate mortality risk (simplified model)
    # Higher score = higher mortality
    if score <= 3:
        mortality_risk = 2.0
        risk_category = "Nguy cơ thấp"
    elif score <= 6:
        mortality_risk = 5.0
        risk_category = "Nguy cơ trung bình"
    elif score <= 9:
        mortality_risk = 10.0
        risk_category = "Nguy cơ cao"
    else:
        mortality_risk = 20.0
        risk_category = "Nguy cơ rất cao"
    
    return {
        "score": score,
        "mortality_risk": mortality_risk,
        "risk_category": risk_category,
        "details": details
    }


def render():
    """Render RHMP-30 interface"""
    import streamlit as st
    
    st.set_page_config(page_title="RHMP-30", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🦴 RHMP-30</h2>
    <p style='text-align: center; color: #6B7280;'>
    Rotterdam Hip Fracture Mortality Prediction-30 Days<br>
    Dự đoán nguy cơ tử vong 30 ngày sau phẫu thuật gãy xương hông
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về RHMP-30"):
        st.markdown("""
        **RHMP-30 (Rotterdam Hip Fracture Mortality Prediction-30 Days)** là công cụ 
        dự đoán nguy cơ tử vong 30 ngày sau phẫu thuật gãy xương hông.
        
        ### Các yếu tố nguy cơ:
        - Tuổi
        - Giới tính
        - Phân loại ASA
        - Loại gãy xương
        - Hemoglobin trước mổ
        - Creatinine trước mổ
        - Thời gian đến phẫu thuật
        - Loại gây mê
        
        ### Phân loại nguy cơ:
        - **≤3 điểm:** Nguy cơ thấp (~2%)
        - **4-6 điểm:** Nguy cơ trung bình (~5%)
        - **7-9 điểm:** Nguy cơ cao (~10%)
        - **≥10 điểm:** Nguy cơ rất cao (~20%)
        
        ### Ứng dụng lâm sàng:
        - Đánh giá nguy cơ trước mổ
        - Hướng dẫn quyết định điều trị
        - Tư vấn bệnh nhân và gia đình
        - Dùng trong phẫu thuật chỉnh hình
        """)
    
    # Input section
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=50,
            max_value=120,
            value=80,
            step=1,
            key="rhmp30_age"
        )
        
        is_female = st.selectbox(
            "Giới tính",
            ["Nữ", "Nam"],
            key="rhmp30_sex"
        ) == "Nữ"
        
        asa_class = st.selectbox(
            "Phân loại ASA",
            [1, 2, 3, 4, 5],
            key="rhmp30_asa",
            help="1 = Bình thường, 2 = Bệnh nhẹ, 3 = Bệnh nặng, 4 = Bệnh đe dọa tính mạng, 5 = Sắp chết"
        )
    
    with col2:
        fracture_type = st.selectbox(
            "Loại gãy xương",
            ["Intracapsular (Trong bao khớp)", "Extracapsular (Ngoài bao khớp)", "Subtrochanteric (Dưới mấu chuyển)"],
            key="rhmp30_fracture"
        )
        
        fracture_type_key = {
            "Intracapsular (Trong bao khớp)": "intracapsular",
            "Extracapsular (Ngoài bao khớp)": "extracapsular",
            "Subtrochanteric (Dưới mấu chuyển)": "subtrochanteric"
        }[fracture_type]
    
    st.markdown("### 🧪 Xét nghiệm trước mổ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        hemoglobin = st.number_input(
            "Hemoglobin (g/dL)",
            min_value=5.0,
            max_value=20.0,
            value=12.0,
            step=0.1,
            format="%.1f",
            key="rhmp30_hb"
        )
    
    with col2:
        creatinine = st.number_input(
            "Creatinine (mg/dL)",
            min_value=0.5,
            max_value=10.0,
            value=1.0,
            step=0.1,
            format="%.2f",
            key="rhmp30_cr"
        )
    
    st.markdown("### 🏥 Thông tin phẫu thuật")
    
    col1, col2 = st.columns(2)
    
    with col1:
        time_to_surgery_hours = st.number_input(
            "Thời gian đến phẫu thuật (giờ)",
            min_value=0.0,
            max_value=168.0,
            value=24.0,
            step=1.0,
            format="%.1f",
            key="rhmp30_time"
        )
    
    with col2:
        general_anesthesia = st.selectbox(
            "Loại gây mê",
            ["Gây mê vùng", "Gây mê toàn thân"],
            key="rhmp30_anesthesia"
        ) == "Gây mê toàn thân"
    
    if st.button("🔬 Tính nguy cơ RHMP-30", type="primary", use_container_width=True):
        # Validation
        errors = []
        if age < 50 or age > 120:
            errors.append("Tuổi phải từ 50-120")
        if asa_class < 1 or asa_class > 5:
            errors.append("ASA phải từ 1-5")
        if hemoglobin < 5 or hemoglobin > 20:
            errors.append("Hemoglobin phải từ 5-20 g/dL")
        if creatinine < 0.5 or creatinine > 10:
            errors.append("Creatinine phải từ 0.5-10 mg/dL")
        if time_to_surgery_hours < 0 or time_to_surgery_hours > 168:
            errors.append("Thời gian đến phẫu thuật phải từ 0-168 giờ")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_rhmp30(
                age=age,
                is_female=is_female,
                asa_class=asa_class,
                fracture_type=fracture_type_key,
                hemoglobin=hemoglobin,
                creatinine=creatinine,
                time_to_surgery_hours=time_to_surgery_hours,
                general_anesthesia=general_anesthesia
            )
            
            # Display results
            st.markdown("---")
            st.markdown("### 📋 Kết quả RHMP-30")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Điểm số", f"{result['score']}")
            
            with col2:
                st.metric(
                    "Nguy cơ tử vong 30 ngày",
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
            
            # Clinical recommendations
            st.markdown("### 💡 Khuyến nghị lâm sàng")
            
            if result['score'] <= 3:
                st.success(f"**{result['risk_category']}** - Nguy cơ tử vong 30 ngày: ~{result['mortality_risk']:.1f}%")
                st.markdown("""
                - Tiên lượng tốt
                - Phẫu thuật theo tiêu chuẩn
                - Theo dõi thường quy
                """)
            elif result['score'] <= 6:
                st.info(f"**{result['risk_category']}** - Nguy cơ tử vong 30 ngày: ~{result['mortality_risk']:.1f}%")
                st.markdown("""
                - Tối ưu hóa trước mổ (điều chỉnh hemoglobin, chức năng thận)
                - Phẫu thuật sớm nếu có thể (<24-48h)
                - Theo dõi sát sau mổ
                - Phòng ngừa biến chứng
                """)
            elif result['score'] <= 9:
                st.warning(f"**{result['risk_category']}** - Nguy cơ tử vong 30 ngày: ~{result['mortality_risk']:.1f}%")
                st.markdown("""
                - Đánh giá đa chuyên khoa trước mổ
                - Tối ưu hóa tình trạng bệnh nhân
                - Phẫu thuật sớm nếu có thể
                - Theo dõi sát tại ICU sau mổ
                - Phòng ngừa biến chứng tích cực
                - Tư vấn gia đình về tiên lượng
                """)
            else:
                st.error(f"**{result['risk_category']}** - Nguy cơ tử vong 30 ngày: ~{result['mortality_risk']:.1f}%")
                st.markdown("""
                - **Đánh giá đa chuyên khoa ngay**
                - Tối ưu hóa tình trạng bệnh nhân trước mổ
                - Cân nhắc phẫu thuật vs điều trị bảo tồn
                - Nếu phẫu thuật: theo dõi tại ICU
                - Phòng ngừa biến chứng tối đa
                - Tư vấn gia đình về tiên lượng nghiêm trọng
                - Chăm sóc giảm nhẹ nếu cần
                """)
            
            # Save to history
            save_calculation_to_history(
                calculator_id="rhmp30",
                calculator_name="RHMP-30",
                inputs={
                    "Tuổi": f"{age}",
                    "Giới tính": "Nữ" if is_female else "Nam",
                    "ASA": f"{asa_class}",
                    "Loại gãy": fracture_type,
                    "Hemoglobin": f"{hemoglobin:.1f}",
                    "Creatinine": f"{creatinine:.2f}",
                    "Thời gian đến mổ": f"{time_to_surgery_hours:.1f}h"
                },
                result={
                    "Điểm": f"{result['score']}",
                    "Nguy cơ tử vong 30 ngày": f"{result['mortality_risk']:.1f}%",
                    "Phân loại": result['risk_category']
                }
            )
            
            # Share and export
            render_share_section(
                calculator_id="rhmp30",
                calculator_name="RHMP-30"
            )
            
            render_export_section(
                calculator_id="rhmp30",
                calculator_name="RHMP-30",
                data={
                    "inputs": {
                        "age": age,
                        "is_female": is_female,
                        "asa_class": asa_class,
                        "fracture_type": fracture_type_key,
                        "hemoglobin": hemoglobin,
                        "creatinine": creatinine,
                        "time_to_surgery_hours": time_to_surgery_hours,
                        "general_anesthesia": general_anesthesia
                    },
                    "result": result
                }
            )
    
    # History
    render_history_ui(calculator_id="rhmp30", show_actions=True)
    
    # References
    references = get_references("RHMP-30")
    if references:
        render_references_section(references)

