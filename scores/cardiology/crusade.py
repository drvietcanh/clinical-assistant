"""
CRUSADE Bleeding Risk Score Calculator
======================================

Predicts in-hospital bleeding risk in patients with ACS (NSTEMI/STEMI)

Reference:
- Subherwal S, et al. Baseline risk of bleeding complications with antiplatelet therapy 
  in patients with acute coronary syndrome. Circulation. 2009;119(14):1873-1882.

CRUSADE Score Components (8 factors):
- Hematocrit (%)
- Creatinine clearance (CrCl, mL/min)
- Heart rate (HR, bpm)
- Sex (female)
- Prior vascular disease
- Diabetes
- Systolic blood pressure (SBP, mmHg)
- Signs of heart failure at presentation

Total: 0-100 points

Risk Categories:
- Very Low: ≤20
- Low: 21-30
- Moderate: 31-40
- High: 41-50
- Very High: >50

Clinical Utility:
- Predict in-hospital major bleeding risk
- Guide antiplatelet/anticoagulation therapy
- Risk-benefit assessment for dual antiplatelet therapy
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import (
    validate_age,
    validate_blood_pressure,
    validate_lab_value
)
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


def calculate_crusade_score(
    hematocrit: float,
    crcl: float,
    heart_rate: int,
    is_female: bool,
    prior_vascular_disease: bool,
    diabetes: bool,
    sbp: float,
    heart_failure_signs: bool
) -> dict:
    """
    Calculate CRUSADE Bleeding Risk Score
    
    Args:
        hematocrit: Hematocrit (%)
        crcl: Creatinine clearance (mL/min)
        heart_rate: Heart rate (bpm)
        is_female: Female sex
        prior_vascular_disease: Prior vascular disease
        diabetes: Diabetes
        sbp: Systolic blood pressure (mmHg)
        heart_failure_signs: Signs of heart failure at presentation
    
    Returns:
        Dictionary with score, risk category, and interpretation
    """
    score = 0
    details = []
    
    # Hematocrit scoring
    if hematocrit < 31:
        score += 9
        details.append(f"Hematocrit {hematocrit:.1f}% (<31%) → +9 điểm")
    elif hematocrit < 34:
        score += 7
        details.append(f"Hematocrit {hematocrit:.1f}% (31-33.9%) → +7 điểm")
    elif hematocrit < 37:
        score += 3
        details.append(f"Hematocrit {hematocrit:.1f}% (34-36.9%) → +3 điểm")
    elif hematocrit < 40:
        score += 2
        details.append(f"Hematocrit {hematocrit:.1f}% (37-39.9%) → +2 điểm")
    else:
        details.append(f"Hematocrit {hematocrit:.1f}% (≥40%) → 0 điểm")
    
    # Creatinine clearance scoring
    if crcl < 15:
        score += 39
        details.append(f"CrCl {crcl:.0f} mL/min (<15) → +39 điểm")
    elif crcl < 30:
        score += 35
        details.append(f"CrCl {crcl:.0f} mL/min (15-29.9) → +35 điểm")
    elif crcl < 60:
        score += 28
        details.append(f"CrCl {crcl:.0f} mL/min (30-59.9) → +28 điểm")
    elif crcl < 90:
        score += 17
        details.append(f"CrCl {crcl:.0f} mL/min (60-89.9) → +17 điểm")
    elif crcl < 120:
        score += 7
        details.append(f"CrCl {crcl:.0f} mL/min (90-119.9) → +7 điểm")
    else:
        details.append(f"CrCl {crcl:.0f} mL/min (≥120) → 0 điểm")
    
    # Heart rate scoring
    if heart_rate > 120:
        score += 11
        details.append(f"HR {heart_rate} bpm (>120) → +11 điểm")
    elif heart_rate > 110:
        score += 8
        details.append(f"HR {heart_rate} bpm (111-120) → +8 điểm")
    elif heart_rate > 100:
        score += 3
        details.append(f"HR {heart_rate} bpm (101-110) → +3 điểm")
    elif heart_rate > 80:
        score += 1
        details.append(f"HR {heart_rate} bpm (81-100) → +1 điểm")
    else:
        details.append(f"HR {heart_rate} bpm (≤80) → 0 điểm")
    
    # Sex (female)
    if is_female:
        score += 8
        details.append("Giới tính nữ → +8 điểm")
    else:
        details.append("Giới tính nam → 0 điểm")
    
    # Prior vascular disease
    if prior_vascular_disease:
        score += 7
        details.append("Tiền sử bệnh mạch máu → +7 điểm")
    else:
        details.append("Không có tiền sử bệnh mạch máu → 0 điểm")
    
    # Diabetes
    if diabetes:
        score += 6
        details.append("Đái tháo đường → +6 điểm")
    else:
        details.append("Không có đái tháo đường → 0 điểm")
    
    # Systolic blood pressure scoring
    if sbp < 90:
        score += 10
        details.append(f"SBP {sbp:.0f} mmHg (<90) → +10 điểm")
    elif sbp < 100:
        score += 8
        details.append(f"SBP {sbp:.0f} mmHg (90-99) → +8 điểm")
    elif sbp < 110:
        score += 5
        details.append(f"SBP {sbp:.0f} mmHg (100-109) → +5 điểm")
    elif sbp < 120:
        score += 1
        details.append(f"SBP {sbp:.0f} mmHg (110-119) → +1 điểm")
    else:
        details.append(f"SBP {sbp:.0f} mmHg (≥120) → 0 điểm")
    
    # Signs of heart failure
    if heart_failure_signs:
        score += 6
        details.append("Dấu hiệu suy tim khi nhập viện → +6 điểm")
    else:
        details.append("Không có dấu hiệu suy tim → 0 điểm")
    
    # Risk stratification
    if score <= 20:
        risk_category = "Rất thấp"
        risk_class = "VERY_LOW"
        bleeding_risk = "<3.1%"
        color = COLORS["success"]
    elif score <= 30:
        risk_category = "Thấp"
        risk_class = "LOW"
        bleeding_risk = "3.1-5.5%"
        color = COLORS["success"]
    elif score <= 40:
        risk_category = "Trung bình"
        risk_class = "MODERATE"
        bleeding_risk = "5.5-8.6%"
        color = COLORS["warning"]
    elif score <= 50:
        risk_category = "Cao"
        risk_class = "HIGH"
        bleeding_risk = "8.6-11.9%"
        color = COLORS["error"]
    else:
        risk_category = "Rất cao"
        risk_class = "VERY_HIGH"
        bleeding_risk = ">11.9%"
        color = COLORS["error"]
    
    return {
        'total_score': score,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'bleeding_risk': bleeding_risk,
        'color': color,
        'details': details
    }


def render():
    """Render CRUSADE Score calculator"""
    
    # st.title("🩸 CRUSADE Bleeding Risk Score")
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩸 CRUSADE Bleeding Risk Score</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Dự đoán nguy cơ chảy máu trong viện ở bệnh nhân ACS**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'crusade':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **CRUSADE Score** dự đoán nguy cơ chảy máu trong viện ở bệnh nhân ACS (NSTEMI/STEMI):
        - Được phát triển từ CRUSADE registry (n=71,277)
        - Dự đoán nguy cơ chảy máu nặng trong viện
        - Hỗ trợ quyết định điều trị kháng đông/kháng tiểu cầu
        
        ### 🎯 Yếu tố nguy cơ (8 yếu tố)
        
        1. **Hematocrit** (%)
        2. **Creatinine clearance** (mL/min)
        3. **Heart rate** (bpm)
        4. **Giới tính** (nữ)
        5. **Tiền sử bệnh mạch máu**
        6. **Đái tháo đường**
        7. **Huyết áp tâm thu** (mmHg)
        8. **Dấu hiệu suy tim** khi nhập viện
        
        ### 📊 Phân loại nguy cơ
        
        | Điểm | Phân loại | Nguy cơ chảy máu |
        |------|-----------|------------------|
        | ≤20 | Rất thấp | <3.1% |
        | 21-30 | Thấp | 3.1-5.5% |
        | 31-40 | Trung bình | 5.5-8.6% |
        | 41-50 | Cao | 8.6-11.9% |
        | >50 | Rất cao | >11.9% |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân ACS (NSTEMI/STEMI)
        - Đánh giá tại thời điểm nhập viện
        - Kết hợp với TIMI/GRACE để đánh giá toàn diện
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="crusade",
            calculator_name="CRUSADE Score",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🩺 Sinh hiệu & Xét nghiệm")
        hematocrit = st.number_input(
            "Hematocrit (%)",
            10.0, 60.0, 40.0, 0.1,
            format="%.1f",
            help="Hematocrit khi nhập viện"
        )
        
        crcl = st.number_input(
            "Creatinine Clearance (mL/min)",
            0.0, 200.0, 80.0, 1.0,
            format="%.0f",
            help="CrCl tính theo Cockcroft-Gault hoặc eGFR"
        )
        
        heart_rate = st.number_input(
            "Heart Rate (bpm)",
            40, 200, 80, 1,
            format="%d",
            help="Nhịp tim khi nhập viện"
        )
        
        sbp = st.number_input(
            "Systolic Blood Pressure (mmHg)",
            50.0, 250.0, 120.0, 1.0,
            format="%.0f",
            help="Huyết áp tâm thu khi nhập viện"
        )
    
    with col2:
        st.markdown("#### 👤 Thông tin Bệnh nhân")
        sex = st.radio("Giới tính", ["Nam", "Nữ"], horizontal=True)
        is_female = (sex == "Nữ")
        
        prior_vascular_disease = st.checkbox(
            "**Tiền sử bệnh mạch máu**",
            help="PAD, stroke, TIA, hoặc bệnh mạch vành trước đây"
        )
        
        diabetes = st.checkbox(
            "**Đái tháo đường**",
            help="Đái tháo đường type 1 hoặc type 2"
        )
        
        heart_failure_signs = st.checkbox(
            "**Dấu hiệu suy tim khi nhập viện**",
            help="Rales, JVD, hoặc phù phổi trên X-quang"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính CRUSADE Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Hematocrit validation
        is_valid_hct, hct_error = validate_lab_value(hematocrit, "Hematocrit", 10.0, 60.0)
        if not is_valid_hct:
            validation_errors.append(f"Hematocrit: {hct_error}")
        
        # CrCl validation
        is_valid_crcl, crcl_error = validate_lab_value(crcl, "Creatinine Clearance", 0.0, 200.0)
        if not is_valid_crcl:
            validation_errors.append(f"Creatinine Clearance: {crcl_error}")
        
        # Heart rate validation
        if heart_rate < 40 or heart_rate > 200:
            validation_errors.append(f"Heart Rate: Phải trong khoảng 40-200 bpm")
        
        # SBP validation
        is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
        if not is_valid_sbp:
            validation_errors.append(f"Systolic Blood Pressure: {sbp_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_crusade_score(
            hematocrit=hematocrit,
            crcl=crcl,
            heart_rate=heart_rate,
            is_female=is_female,
            prior_vascular_disease=prior_vascular_disease,
            diabetes=diabetes,
            sbp=sbp,
            heart_failure_signs=heart_failure_signs
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Use render_score_result for main score display
        icon_map = {
            "VERY_LOW": "✅",
            "LOW": "✅",
            "MODERATE": "⚠️",
            "HIGH": "🚨",
            "VERY_HIGH": "🚨"
        }
        icon = icon_map.get(result['risk_class'], "🩸")
        
        render_score_result(
            title="CRUSADE Score",
            score=result['total_score'],
            interpretation=f"{result['risk_category'].upper()} Risk - {result['bleeding_risk']}",
            mortality=None,
            color=result['color'],
            icon=icon,
            size="large"
        )
        
        # Risk factors summary
        with st.expander("📋 Chi tiết điểm số", expanded=True):
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo điều trị")
        
        if result['risk_class'] == "VERY_LOW":
            st.success(f"""
            **✅ Nguy cơ chảy máu RẤT THẤP ({result['bleeding_risk']}):**
            
            **Khuyến cáo:**
            - Dùng DAPT (Dual Antiplatelet Therapy) an toàn
            - Aspirin + P2Y12 inhibitor (Clopidogrel/Ticagrelor/Prasugrel)
            - Anticoagulation theo chỉ định (Enoxaparin/UFH)
            - Theo dõi thường quy
            """)
        elif result['risk_class'] == "LOW":
            st.success(f"""
            **✅ Nguy cơ chảy máu THẤP ({result['bleeding_risk']}):**
            
            **Khuyến cáo:**
            - Dùng DAPT an toàn
            - Cân nhắc dùng Clopidogrel thay vì Ticagrelor/Prasugrel nếu lo ngại
            - Anticoagulation theo chỉ định
            - Theo dõi sát hơn
            """)
        elif result['risk_class'] == "MODERATE":
            st.warning(f"""
            **⚠️ Nguy cơ chảy máu TRUNG BÌNH ({result['bleeding_risk']}):**
            
            **Khuyến cáo:**
            - Dùng DAPT nhưng thận trọng
            - Ưu tiên Clopidogrel hơn Ticagrelor/Prasugrel
            - Cân nhắc giảm liều P2Y12 inhibitor
            - Tránh GP IIb/IIIa inhibitor nếu không cần thiết
            - Theo dõi sát dấu hiệu chảy máu
            - Cân nhắc PPI bảo vệ dạ dày
            """)
        elif result['risk_class'] == "HIGH":
            st.error(f"""
            **🚨 Nguy cơ chảy máu CAO ({result['bleeding_risk']}):**
            
            **Khuyến cáo:**
            - **THẬN TRỌNG** khi dùng DAPT
            - Ưu tiên Clopidogrel 75mg/ngày
            - Tránh Ticagrelor/Prasugrel liều cao
            - Tránh GP IIb/IIIa inhibitor
            - Cân nhắc giảm liều hoặc rút ngắn thời gian DAPT
            - **BẮT BUỘC** dùng PPI
            - Theo dõi sát dấu hiệu chảy máu
            - Cân nhắc Hgb/Hct hàng ngày
            """)
        else:  # VERY_HIGH
            st.error(f"""
            **🚨🚨 Nguy cơ chảy máu RẤT CAO ({result['bleeding_risk']}):**
            
            **Khuyến cáo:**
            - **CỰC KỲ THẬN TRỌNG** khi dùng DAPT
            - Chỉ dùng Clopidogrel 75mg/ngày (tránh Ticagrelor/Prasugrel)
            - Cân nhắc đơn trị liệu Aspirin nếu nguy cơ huyết khối thấp
            - **TRÁNH** GP IIb/IIIa inhibitor
            - **BẮT BUỘC** dùng PPI
            - Theo dõi sát dấu hiệu chảy máu (Hgb/Hct hàng ngày)
            - Cân nhắc rút ngắn thời gian DAPT (3-6 tháng thay vì 12 tháng)
            - Hội chẩn tim mạch
            """)
        
        st.info("""
        **📌 Lưu ý quan trọng:**
        
        - CRUSADE Score chỉ đánh giá nguy cơ chảy máu, KHÔNG đánh giá nguy cơ huyết khối
        - Cần cân bằng giữa nguy cơ chảy máu và nguy cơ huyết khối (dùng TIMI/GRACE)
        - Quyết định điều trị cuối cùng thuộc về bác sĩ lâm sàng
        - Điều chỉnh liều thuốc dựa trên đánh giá toàn diện
        """)
        
        # Prepare inputs and results for Phase 1
        inputs_dict = {
            "Hematocrit": f"{hematocrit:.1f}%",
            "Creatinine Clearance": f"{crcl:.0f} mL/min",
            "Heart Rate": f"{heart_rate} bpm",
            "Gender": sex,
            "Prior Vascular Disease": "Có" if prior_vascular_disease else "Không",
            "Diabetes": "Có" if diabetes else "Không",
            "Systolic BP": f"{sbp:.0f} mmHg",
            "Heart Failure Signs": "Có" if heart_failure_signs else "Không"
        }
        
        results_dict = {
            "CRUSADE Score": f"{result['total_score']}/100",
            "Risk Category": result['risk_category'],
            "Bleeding Risk": result['bleeding_risk'],
            "Risk Class": result['risk_class']
        }
        
        # Export section
        render_export_section(
            title="CRUSADE Score",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="CRUSADE Score"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="crusade",
            calculator_name="CRUSADE Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="crusade",
            calculator_name="CRUSADE Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="crusade", show_actions=True)
        
        # References section
        references = get_references("CRUSADE")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['crusade_result'] = result
    
    # Quick reference
    with st.expander("📖 Bảng điểm CRUSADE"):
        st.markdown("""
        ### Bảng điểm chi tiết
        
        **Hematocrit (%):**
        - <31: +9 điểm
        - 31-33.9: +7 điểm
        - 34-36.9: +3 điểm
        - 37-39.9: +2 điểm
        - ≥40: 0 điểm
        
        **Creatinine Clearance (mL/min):**
        - <15: +39 điểm
        - 15-29.9: +35 điểm
        - 30-59.9: +28 điểm
        - 60-89.9: +17 điểm
        - 90-119.9: +7 điểm
        - ≥120: 0 điểm
        
        **Heart Rate (bpm):**
        - >120: +11 điểm
        - 111-120: +8 điểm
        - 101-110: +3 điểm
        - 81-100: +1 điểm
        - ≤80: 0 điểm
        
        **Giới tính:**
        - Nữ: +8 điểm
        - Nam: 0 điểm
        
        **Tiền sử bệnh mạch máu:** +7 điểm
        
        **Đái tháo đường:** +6 điểm
        
        **Systolic BP (mmHg):**
        - <90: +10 điểm
        - 90-99: +8 điểm
        - 100-109: +5 điểm
        - 110-119: +1 điểm
        - ≥120: 0 điểm
        
        **Dấu hiệu suy tim:** +6 điểm
        """)
    
    # Always show references at the bottom (even before calculation)
    st.markdown("---")
    references = get_references("CRUSADE")
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
            **CRUSADE Bleeding Risk Score**
            
            **Reference:**
            Subherwal S, Bach RG, Chen AY, et al. Baseline risk of bleeding complications 
            with antiplatelet therapy in patients with acute coronary syndrome. 
            Circulation. 2009;119(14):1873-1882.
            
            **Purpose:**
            Predict in-hospital major bleeding risk in ACS patients.
            
            **Validation:**
            - Derived from CRUSADE registry (n=71,277)
            - Validated in multiple cohorts
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

