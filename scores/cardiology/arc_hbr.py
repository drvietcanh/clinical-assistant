"""
ARC-HBR (Academic Research Consortium for High Bleeding Risk) Criteria
======================================================================

Identifies patients undergoing percutaneous coronary intervention (PCI) 
who are at high risk of major bleeding or intracranial hemorrhage.

Reference:
- Urban P, et al. Defining high bleeding risk in patients undergoing 
  percutaneous coronary intervention: a consensus document from the Academic 
  Research Consortium for High Bleeding Risk. Circulation. 2019;140(3):240-261.

ARC-HBR Criteria:
Major Criteria (1 = HBR):
- Severe or end-stage CKD (eGFR <30 mL/min/1.73m²)
- Hemoglobin <11 g/dL or history of bleeding
- Spontaneous ICH at any time
- Recent (<12 months) GI bleeding
- Moderate/severe thrombocytopenia (<100,000/μL)
- Chronic oral anticoagulation
- Recent (<3 months) major surgery/trauma
- Recent (<30 days) major bleeding

Minor Criteria (≥2 = HBR):
- Age ≥75 years
- Moderate CKD (eGFR 30-59 mL/min/1.73m²)
- Hemoglobin 11-12.9 g/dL (men) or 11-11.9 g/dL (women)
- Spontaneous ICH >12 months ago
- Any ICH at any time
- Recent (<12 months) minor bleeding
- Long-term NSAID/steroid use
- Any ischemic stroke at any time

Clinical Utility:
- Used daily in cardiology practice
- Guides DAPT duration after PCI
- Helps balance ischemic vs bleeding risk
- Alternative/complement to HAS-BLED
"""

import streamlit as st
from config.theme import COLORS
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


def calculate_arc_hbr(
    age: int,
    egfr: float,
    hemoglobin: float,
    is_female: bool,
    platelet_count: float,
    # Major criteria
    severe_ckd: bool = False,
    hemoglobin_low: bool = False,
    bleeding_history: bool = False,
    spontaneous_ich_anytime: bool = False,
    recent_gi_bleeding: bool = False,
    thrombocytopenia: bool = False,
    oral_anticoagulation: bool = False,
    recent_major_surgery: bool = False,
    recent_major_bleeding: bool = False,
    # Minor criteria
    moderate_ckd: bool = False,
    hemoglobin_moderate: bool = False,
    spontaneous_ich_old: bool = False,
    any_ich_anytime: bool = False,
    recent_minor_bleeding: bool = False,
    long_term_nsaid: bool = False,
    any_ischemic_stroke: bool = False
) -> dict:
    """
    Calculate ARC-HBR Criteria
    
    Args:
        age: Age (years)
        egfr: eGFR (mL/min/1.73m²)
        hemoglobin: Hemoglobin (g/dL)
        is_female: Female sex
        platelet_count: Platelet count (×10³/μL)
        severe_ckd: eGFR <30 mL/min/1.73m²
        hemoglobin_low: Hemoglobin <11 g/dL or history of bleeding
        bleeding_history: History of bleeding
        spontaneous_ich_anytime: Spontaneous ICH at any time
        recent_gi_bleeding: Recent (<12 months) GI bleeding
        thrombocytopenia: Moderate/severe thrombocytopenia (<100,000/μL)
        oral_anticoagulation: Chronic oral anticoagulation
        recent_major_surgery: Recent (<3 months) major surgery/trauma
        recent_major_bleeding: Recent (<30 days) major bleeding
        moderate_ckd: Moderate CKD (eGFR 30-59)
        hemoglobin_moderate: Hemoglobin 11-12.9 (men) or 11-11.9 (women)
        spontaneous_ich_old: Spontaneous ICH >12 months ago
        any_ich_anytime: Any ICH at any time
        recent_minor_bleeding: Recent (<12 months) minor bleeding
        long_term_nsaid: Long-term NSAID/steroid use
        any_ischemic_stroke: Any ischemic stroke at any time
    
    Returns:
        Dictionary with HBR status, criteria count, and interpretation
    """
    major_criteria = []
    minor_criteria = []
    
    # Auto-calculate some criteria from inputs
    if egfr < 30:
        severe_ckd = True
    elif 30 <= egfr < 60:
        moderate_ckd = True
    
    if hemoglobin < 11:
        hemoglobin_low = True
    elif (hemoglobin >= 11 and hemoglobin < 13 and not is_female) or \
         (hemoglobin >= 11 and hemoglobin < 12 and is_female):
        hemoglobin_moderate = True
    
    if platelet_count < 100:
        thrombocytopenia = True
    
    if age >= 75:
        minor_criteria.append("Tuổi ≥75")
    
    # Major criteria
    if severe_ckd or egfr < 30:
        major_criteria.append("Suy thận nặng/đến giai đoạn cuối (eGFR <30)")
    
    if hemoglobin_low or hemoglobin < 11:
        major_criteria.append("Hemoglobin <11 g/dL hoặc tiền sử chảy máu")
    elif bleeding_history:
        major_criteria.append("Tiền sử chảy máu")
    
    if spontaneous_ich_anytime:
        major_criteria.append("Xuất huyết nội sọ tự phát bất kỳ lúc nào")
    
    if recent_gi_bleeding:
        major_criteria.append("Chảy máu tiêu hóa gần đây (<12 tháng)")
    
    if thrombocytopenia or platelet_count < 100:
        major_criteria.append("Giảm tiểu cầu trung bình/nặng (<100,000/μL)")
    
    if oral_anticoagulation:
        major_criteria.append("Kháng đông đường uống mạn tính")
    
    if recent_major_surgery:
        major_criteria.append("Phẫu thuật/chấn thương lớn gần đây (<3 tháng)")
    
    if recent_major_bleeding:
        major_criteria.append("Chảy máu lớn gần đây (<30 ngày)")
    
    # Minor criteria
    if moderate_ckd or (30 <= egfr < 60):
        minor_criteria.append("Suy thận trung bình (eGFR 30-59)")
    
    if hemoglobin_moderate:
        if is_female:
            minor_criteria.append("Hemoglobin 11-11.9 g/dL (nữ)")
        else:
            minor_criteria.append("Hemoglobin 11-12.9 g/dL (nam)")
    
    if spontaneous_ich_old:
        minor_criteria.append("Xuất huyết nội sọ tự phát >12 tháng trước")
    
    if any_ich_anytime:
        minor_criteria.append("Bất kỳ xuất huyết nội sọ bất kỳ lúc nào")
    
    if recent_minor_bleeding:
        minor_criteria.append("Chảy máu nhỏ gần đây (<12 tháng)")
    
    if long_term_nsaid:
        minor_criteria.append("Dùng NSAID/steroid dài hạn")
    
    if any_ischemic_stroke:
        minor_criteria.append("Bất kỳ đột quỵ thiếu máu bất kỳ lúc nào")
    
    # Determine HBR status
    major_count = len(major_criteria)
    minor_count = len(minor_criteria)
    
    is_hbr = False
    hbr_reason = ""
    
    if major_count >= 1:
        is_hbr = True
        hbr_reason = f"Có {major_count} tiêu chí MAJOR"
    elif minor_count >= 2:
        is_hbr = True
        hbr_reason = f"Có {minor_count} tiêu chí MINOR (≥2)"
    else:
        hbr_reason = "Không đủ tiêu chí HBR"
    
    return {
        "is_hbr": is_hbr,
        "major_count": major_count,
        "minor_count": minor_count,
        "major_criteria": major_criteria,
        "minor_criteria": minor_criteria,
        "hbr_reason": hbr_reason,
        "total_criteria": major_count + minor_count
    }


def render():
    """Render ARC-HBR Criteria interface"""
    import streamlit as st
    
    st.set_page_config(page_title="ARC-HBR Criteria", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>❤️ ARC-HBR Criteria</h2>
    <p style='text-align: center; color: #6B7280;'>
    Academic Research Consortium for High Bleeding Risk<br>
    Xác định nguy cơ chảy máu cao ở bệnh nhân can thiệp mạch vành qua da
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về ARC-HBR Criteria"):
        st.markdown("""
        **ARC-HBR (Academic Research Consortium for High Bleeding Risk)** là tiêu chuẩn đồng thuận 
        để xác định bệnh nhân có nguy cơ chảy máu cao khi can thiệp mạch vành qua da (PCI).
        
        ### Tiêu chí Major (1 = HBR):
        - Suy thận nặng/đến giai đoạn cuối (eGFR <30)
        - Hemoglobin <11 g/dL hoặc tiền sử chảy máu
        - Xuất huyết nội sọ tự phát bất kỳ lúc nào
        - Chảy máu tiêu hóa gần đây (<12 tháng)
        - Giảm tiểu cầu trung bình/nặng (<100,000/μL)
        - Kháng đông đường uống mạn tính
        - Phẫu thuật/chấn thương lớn gần đây (<3 tháng)
        - Chảy máu lớn gần đây (<30 ngày)
        
        ### Tiêu chí Minor (≥2 = HBR):
        - Tuổi ≥75
        - Suy thận trung bình (eGFR 30-59)
        - Hemoglobin 11-12.9 (nam) hoặc 11-11.9 (nữ)
        - Xuất huyết nội sọ tự phát >12 tháng trước
        - Bất kỳ xuất huyết nội sọ bất kỳ lúc nào
        - Chảy máu nhỏ gần đây (<12 tháng)
        - Dùng NSAID/steroid dài hạn
        - Bất kỳ đột quỵ thiếu máu bất kỳ lúc nào
        
        ### Ứng dụng lâm sàng:
        - Hướng dẫn thời gian DAPT sau PCI
        - Cân bằng nguy cơ thiếu máu vs chảy máu
        - Thay thế/bổ sung cho HAS-BLED
        - Dùng hàng ngày trong thực hành tim mạch
        """)
    
    # Input section
    st.markdown("### 📊 Thông tin bệnh nhân")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=65,
            step=1,
            key="arc_hbr_age"
        )
    
    with col2:
        is_female = st.selectbox(
            "Giới tính",
            ["Nam", "Nữ"],
            key="arc_hbr_sex"
        ) == "Nữ"
    
    with col3:
        egfr = st.number_input(
            "eGFR (mL/min/1.73m²)",
            min_value=0.0,
            max_value=200.0,
            value=60.0,
            step=1.0,
            format="%.1f",
            key="arc_hbr_egfr"
        )
    
    col4, col5 = st.columns(2)
    
    with col4:
        hemoglobin = st.number_input(
            "Hemoglobin (g/dL)",
            min_value=0.0,
            max_value=20.0,
            value=13.0,
            step=0.1,
            format="%.1f",
            key="arc_hbr_hb"
        )
    
    with col5:
        platelet_count = st.number_input(
            "Số lượng tiểu cầu (×10³/μL)",
            min_value=0.0,
            max_value=1000.0,
            value=250.0,
            step=10.0,
            format="%.0f",
            key="arc_hbr_platelet"
        )
    
    # Major criteria
    st.markdown("### 🔴 Tiêu chí Major (1 = HBR)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        bleeding_history = st.checkbox("Tiền sử chảy máu", key="arc_hbr_bleeding_hist")
        spontaneous_ich_anytime = st.checkbox("Xuất huyết nội sọ tự phát bất kỳ lúc nào", key="arc_hbr_ich_anytime")
        recent_gi_bleeding = st.checkbox("Chảy máu tiêu hóa gần đây (<12 tháng)", key="arc_hbr_gi_bleeding")
        oral_anticoagulation = st.checkbox("Kháng đông đường uống mạn tính", key="arc_hbr_oac")
    
    with col2:
        recent_major_surgery = st.checkbox("Phẫu thuật/chấn thương lớn gần đây (<3 tháng)", key="arc_hbr_surgery")
        recent_major_bleeding = st.checkbox("Chảy máu lớn gần đây (<30 ngày)", key="arc_hbr_major_bleeding")
        # Auto-calculated from inputs above
    
    # Minor criteria
    st.markdown("### 🟡 Tiêu chí Minor (≥2 = HBR)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        spontaneous_ich_old = st.checkbox("Xuất huyết nội sọ tự phát >12 tháng trước", key="arc_hbr_ich_old")
        any_ich_anytime = st.checkbox("Bất kỳ xuất huyết nội sọ bất kỳ lúc nào", key="arc_hbr_any_ich")
        recent_minor_bleeding = st.checkbox("Chảy máu nhỏ gần đây (<12 tháng)", key="arc_hbr_minor_bleeding")
        long_term_nsaid = st.checkbox("Dùng NSAID/steroid dài hạn", key="arc_hbr_nsaid")
    
    with col2:
        any_ischemic_stroke = st.checkbox("Bất kỳ đột quỵ thiếu máu bất kỳ lúc nào", key="arc_hbr_stroke")
        # Age ≥75 and moderate CKD are auto-calculated
    
    if st.button("🔬 Đánh giá ARC-HBR", type="primary", use_container_width=True):
        # Validation
        errors = []
        if age < 18 or age > 120:
            errors.append("Tuổi phải từ 18-120")
        if egfr < 0 or egfr > 200:
            errors.append("eGFR phải từ 0-200")
        if hemoglobin < 0 or hemoglobin > 20:
            errors.append("Hemoglobin phải từ 0-20 g/dL")
        if platelet_count < 0 or platelet_count > 1000:
            errors.append("Số lượng tiểu cầu phải từ 0-1000")
        
        if errors:
            render_validation_errors(errors)
        else:
            result = calculate_arc_hbr(
            age=age,
            egfr=egfr,
            hemoglobin=hemoglobin,
            is_female=is_female,
            platelet_count=platelet_count,
            bleeding_history=bleeding_history,
            spontaneous_ich_anytime=spontaneous_ich_anytime,
            recent_gi_bleeding=recent_gi_bleeding,
            oral_anticoagulation=oral_anticoagulation,
            recent_major_surgery=recent_major_surgery,
            recent_major_bleeding=recent_major_bleeding,
            spontaneous_ich_old=spontaneous_ich_old,
            any_ich_anytime=any_ich_anytime,
            recent_minor_bleeding=recent_minor_bleeding,
            long_term_nsaid=long_term_nsaid,
            any_ischemic_stroke=any_ischemic_stroke
        )
        
        # Display results
        st.markdown("---")
        st.markdown("### 📋 Kết quả ARC-HBR")
        
        if result["is_hbr"]:
            st.error(f"⚠️ **NGUY CƠ CHẢY MÁU CAO (HBR)** - {result['hbr_reason']}")
        else:
            st.success(f"✅ **KHÔNG PHẢI HBR** - {result['hbr_reason']}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Tiêu chí Major", f"{result['major_count']}")
            if result['major_criteria']:
                st.markdown("**Các tiêu chí Major:**")
                for criterion in result['major_criteria']:
                    st.markdown(f"- {criterion}")
        
        with col2:
            st.metric("Tiêu chí Minor", f"{result['minor_count']}")
            if result['minor_criteria']:
                st.markdown("**Các tiêu chí Minor:**")
                for criterion in result['minor_criteria']:
                    st.markdown(f"- {criterion}")
        
        # Clinical interpretation
        st.markdown("### 💡 Khuyến nghị lâm sàng")
        
        if result["is_hbr"]:
            st.markdown("""
            **Bệnh nhân có nguy cơ chảy máu cao (HBR):**
            
            1. **Thời gian DAPT ngắn hơn:**
               - Xem xét DAPT 1-3 tháng thay vì 12 tháng
               - Cân nhắc DAPT đơn trị liệu sớm
            
            2. **Lựa chọn stent:**
               - Ưu tiên stent phủ thuốc thế hệ mới (DES)
               - Có thể cân nhắc stent tự tiêu (BVS)
            
            3. **Theo dõi:**
               - Theo dõi sát dấu hiệu chảy máu
               - Đánh giá lại nguy cơ định kỳ
            
            4. **Cân bằng nguy cơ:**
               - Cân nhắc giảm liều antiplatelet nếu cần
               - Tránh triple therapy nếu có thể
            """)
        else:
            st.markdown("""
            **Bệnh nhân không phải HBR:**
            
            1. **Thời gian DAPT tiêu chuẩn:**
               - DAPT 12 tháng sau PCI với DES
               - Có thể kéo dài hơn nếu nguy cơ thiếu máu cao
            
            2. **Theo dõi:**
               - Theo dõi theo tiêu chuẩn
               - Đánh giá lại nếu có thay đổi tình trạng
            """)
        
        # Save to history
        save_calculation_to_history(
            calculator_id="arc_hbr",
            calculator_name="ARC-HBR Criteria",
            inputs={
                "Tuổi": f"{age}",
                "Giới tính": "Nữ" if is_female else "Nam",
                "eGFR": f"{egfr:.1f}",
                "Hemoglobin": f"{hemoglobin:.1f}",
                "Tiểu cầu": f"{platelet_count:.0f}"
            },
            result={
                "HBR": "Có" if result["is_hbr"] else "Không",
                "Tiêu chí Major": result["major_count"],
                "Tiêu chí Minor": result["minor_count"]
            }
        )
        
        # Share and export
        render_share_section(
            calculator_id="arc_hbr",
            calculator_name="ARC-HBR Criteria"
        )
        
        render_export_section(
            calculator_id="arc_hbr",
            calculator_name="ARC-HBR Criteria",
            data={
                "inputs": {
                    "age": age,
                    "sex": "female" if is_female else "male",
                    "egfr": egfr,
                    "hemoglobin": hemoglobin,
                    "platelet_count": platelet_count
                },
                "result": result
            }
        )
    
    # History
    render_history_ui(calculator_id="arc_hbr", show_actions=True)
    
    # References
    references = get_references("ARC-HBR Criteria")
    if references:
        render_references_section(references)

