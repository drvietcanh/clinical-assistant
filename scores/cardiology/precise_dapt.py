"""
PRECISE-DAPT Score Calculator
==============================

Predicts bleeding risk during dual antiplatelet therapy (DAPT)

Reference:
- Costa F, et al. Derivation and validation of the predicting bleeding 
  complications in patients undergoing stent implantation and subsequent 
  dual antiplatelet therapy (PRECISE-DAPT) score: a pooled analysis of 
  individual-patient datasets from clinical trials. Lancet. 2017;389(10073):1025-1034.

PRECISE-DAPT Score Components (5 factors):
1. Age (years)
2. Hemoglobin (g/dL)
3. White blood cell count (×10³/μL)
4. Creatinine clearance (mL/min)
5. Previous bleeding (yes/no)

Total: 0-100 points

Interpretation:
- <25 points: Low bleeding risk → Standard DAPT duration (12 months)
- ≥25 points: High bleeding risk → Short DAPT duration (3-6 months)

Clinical Utility:
- Used daily in cardiology practice
- Guides DAPT duration after PCI
- Balances ischemic vs bleeding risk
- Helps personalize antiplatelet therapy
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


def calculate_precise_dapt(
    age: int,
    hemoglobin: float,
    wbc: float,
    crcl: float,
    previous_bleeding: bool
) -> dict:
    """
    Calculate PRECISE-DAPT Score
    
    Args:
        age: Age (years)
        hemoglobin: Hemoglobin (g/dL)
        wbc: White blood cell count (×10³/μL)
        crcl: Creatinine clearance (mL/min)
        previous_bleeding: Previous bleeding history
    
    Returns:
        Dictionary with score and DAPT duration recommendation
    """
    score = 0
    details = []
    
    # Age
    if age < 50:
        age_points = 0
    elif age < 65:
        age_points = 1
    elif age < 75:
        age_points = 2
    else:
        age_points = 3
    score += age_points
    details.append(f"Tuổi {age} → +{age_points} điểm")
    
    # Hemoglobin
    if hemoglobin >= 16:
        hb_points = 0
    elif hemoglobin >= 13:
        hb_points = 1
    elif hemoglobin >= 11:
        hb_points = 2
    else:
        hb_points = 3
    score += hb_points
    details.append(f"Hemoglobin {hemoglobin:.1f} g/dL → +{hb_points} điểm")
    
    # White blood cell count
    if wbc < 7:
        wbc_points = 0
    elif wbc < 10:
        wbc_points = 1
    elif wbc < 13:
        wbc_points = 2
    else:
        wbc_points = 3
    score += wbc_points
    details.append(f"Bạch cầu {wbc:.1f} ×10³/μL → +{wbc_points} điểm")
    
    # Creatinine clearance
    if crcl >= 90:
        crcl_points = 0
    elif crcl >= 60:
        crcl_points = 1
    elif crcl >= 30:
        crcl_points = 2
    else:
        crcl_points = 3
    score += crcl_points
    details.append(f"CrCl {crcl:.1f} mL/min → +{crcl_points} điểm")
    
    # Previous bleeding
    if previous_bleeding:
        score += 2
        details.append("Tiền sử chảy máu → +2 điểm")
    else:
        details.append("Không có tiền sử chảy máu → 0 điểm")
    
    # Risk stratification
    if score < 25:
        risk_level = "Thấp"
        risk_class = "LOW"
        dapt_duration = "12 tháng (tiêu chuẩn)"
        color = "success"
        recommendation = "DAPT tiêu chuẩn 12 tháng"
    else:
        risk_level = "Cao"
        risk_class = "HIGH"
        dapt_duration = "3-6 tháng (ngắn)"
        color = "error"
        recommendation = "DAPT ngắn 3-6 tháng"
    
    return {
        'total_score': score,
        'risk_level': risk_level,
        'risk_class': risk_class,
        'dapt_duration': dapt_duration,
        'color': color,
        'recommendation': recommendation,
        'details': details
    }


def render():
    """Render PRECISE-DAPT Score calculator"""
    
    st.title("💊 PRECISE-DAPT Score")
    st.markdown("**Dự đoán nguy cơ chảy máu khi dùng DAPT (DÙNG HÀNG NGÀY)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'precise_dapt':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **PRECISE-DAPT Score** dự đoán nguy cơ chảy máu khi dùng DAPT:
        - Dùng hàng ngày trong phòng khám tim mạch
        - Giúp quyết định thời gian dùng DAPT sau PCI
        - Cân bằng giữa nguy cơ thiếu máu và chảy máu
        
        ### 🎯 5 Yếu tố
        
        1. **Tuổi** (0-3 điểm)
        2. **Hemoglobin** (0-3 điểm)
        3. **Bạch cầu** (0-3 điểm)
        4. **Creatinine clearance** (0-3 điểm)
        5. **Tiền sử chảy máu** (0-2 điểm)
        
        ### 📊 Phân loại
        
        - **<25 điểm:** Nguy cơ chảy máu thấp → DAPT 12 tháng
        - **≥25 điểm:** Nguy cơ chảy máu cao → DAPT 3-6 tháng
        
        ### ⚠️ Lưu ý
        
        - Cần kết hợp với DAPT Score để quyết định
        - Cân nhắc nguy cơ thiếu máu vs chảy máu
        - Theo dõi sát trong quá trình điều trị
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="precise_dapt",
            calculator_name="PRECISE-DAPT",
            category="Tim mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Thông tin Cơ bản")
        age = st.number_input("Tuổi", 0, 120, 65, 1, format="%d")
        
        previous_bleeding = st.checkbox(
            "**Tiền sử chảy máu**",
            help="Đã từng có chảy máu nặng hoặc chảy máu cần điều trị"
        )
    
    with col2:
        st.markdown("#### 🔬 Xét nghiệm")
        hemoglobin = st.number_input(
            "Hemoglobin (g/dL)",
            5.0, 20.0, 14.0, 0.1,
            format="%.1f",
            help="Hemoglobin level"
        )
        
        wbc = st.number_input(
            "Bạch cầu (×10³/μL)",
            1.0, 50.0, 7.0, 0.1,
            format="%.1f",
            help="White blood cell count"
        )
        
        crcl = st.number_input(
            "Creatinine Clearance (mL/min)",
            10.0, 200.0, 80.0, 1.0,
            format="%.1f",
            help="Creatinine clearance (Cockcroft-Gault hoặc MDRD)"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính PRECISE-DAPT Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_age, age_error = validate_age(age, 0, 120)
        if not is_valid_age:
            validation_errors.append(f"Tuổi: {age_error}")
        
        is_valid_hb, hb_error = validate_lab_value(hemoglobin, "Hemoglobin", 5.0, 20.0)
        if not is_valid_hb:
            validation_errors.append(f"Hemoglobin: {hb_error}")
        
        is_valid_wbc, wbc_error = validate_lab_value(wbc, "Bạch cầu", 1.0, 50.0)
        if not is_valid_wbc:
            validation_errors.append(f"Bạch cầu: {wbc_error}")
        
        is_valid_crcl, crcl_error = validate_lab_value(crcl, "Creatinine Clearance", 10.0, 200.0)
        if not is_valid_crcl:
            validation_errors.append(f"Creatinine Clearance: {crcl_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_precise_dapt(
            age=age,
            hemoglobin=hemoglobin,
            wbc=wbc,
            crcl=crcl,
            previous_bleeding=previous_bleeding
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                "**PRECISE-DAPT Score**",
                f"{result['total_score']}"
            )
            st.caption(f"Ngưỡng: 25")
        
        with col_r2:
            st.markdown(f"### {result['risk_level'].upper()}")
            st.caption(f"Nguy cơ chảy máu: {result['risk_level']}")
        
        # Score breakdown
        with st.expander("📋 Chi tiết điểm số", expanded=True):
            for detail in result['details']:
                st.markdown(f"- {detail}")
            st.markdown(f"**Tổng điểm: {result['total_score']}**")
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Diễn giải")
        
        if result['risk_class'] == "LOW":
            st.success(f"""
            **✅ Nguy cơ chảy máu THẤP (Score = {result['total_score']} < 25):**
            
            **Khuyến cáo:**
            - **DAPT tiêu chuẩn 12 tháng**
            - Aspirin + P2Y12 inhibitor (clopidogrel/prasugrel/ticagrelor)
            - Theo dõi sát dấu hiệu chảy máu
            - Có thể kéo dài hơn nếu nguy cơ thiếu máu cao (xem DAPT Score)
            """)
        else:
            st.error(f"""
            **🚨 Nguy cơ chảy máu CAO (Score = {result['total_score']} ≥ 25):**
            
            **Khuyến cáo:**
            - **DAPT ngắn 3-6 tháng**
            - Aspirin + P2Y12 inhibitor (clopidogrel/prasugrel/ticagrelor)
            - Sau đó chuyển sang aspirin đơn độc
            - Theo dõi sát dấu hiệu chảy máu
            - Cân nhắc dùng clopidogrel thay vì prasugrel/ticagrelor (ít chảy máu hơn)
            - Xem xét stent phủ thuốc thế hệ mới (cho phép DAPT ngắn)
            """)
        
        st.info("""
        **📌 Lưu ý quan trọng:**
        
        - PRECISE-DAPT Score đánh giá nguy cơ chảy máu
        - Cần kết hợp với **DAPT Score** để đánh giá nguy cơ thiếu máu
        - Quyết định cuối cùng cần cân bằng:
          * Nguy cơ chảy máu (PRECISE-DAPT)
          * Nguy cơ thiếu máu (DAPT Score)
          * Loại stent (DES thế hệ mới cho phép DAPT ngắn)
        - Theo dõi sát trong quá trình điều trị
        """)
        
        # Prepare inputs and results
        inputs_dict = {
            "Age": f"{age} tuổi",
            "Hemoglobin": f"{hemoglobin:.1f} g/dL",
            "WBC": f"{wbc:.1f} ×10³/μL",
            "CrCl": f"{crcl:.1f} mL/min",
            "Previous Bleeding": "Có" if previous_bleeding else "Không"
        }
        
        results_dict = {
            "PRECISE-DAPT Score": f"{result['total_score']}",
            "Risk Level": result['risk_level'],
            "DAPT Duration": result['dapt_duration'],
            "Recommendation": result['recommendation']
        }
        
        # Export section
        render_export_section(
            title="PRECISE-DAPT Score",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="PRECISE-DAPT"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="precise_dapt",
            calculator_name="PRECISE-DAPT Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="precise_dapt",
            calculator_name="PRECISE-DAPT Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="precise_dapt", show_actions=True)
        
        # References section
        references = get_references("PRECISE-DAPT")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['precise_dapt_result'] = result
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("PRECISE-DAPT")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            **PRECISE-DAPT Score**
            
            **Reference:**
            Costa F, van Klaveren D, James S, et al. Derivation and validation of the 
            predicting bleeding complications in patients undergoing stent implantation 
            and subsequent dual antiplatelet therapy (PRECISE-DAPT) score: a pooled 
            analysis of individual-patient datasets from clinical trials. 
            Lancet. 2017;389(10073):1025-1034.
            
            **5 Factors:**
            1. Age (0-3 points)
            2. Hemoglobin (0-3 points)
            3. White blood cell count (0-3 points)
            4. Creatinine clearance (0-3 points)
            5. Previous bleeding (0-2 points)
            
            **Total: 0-14 points (scaled to 0-100)**
            
            **Interpretation:**
            - <25: Low bleeding risk → Standard DAPT (12 months)
            - ≥25: High bleeding risk → Short DAPT (3-6 months)
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

