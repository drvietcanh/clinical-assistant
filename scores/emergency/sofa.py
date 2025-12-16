"""
SOFA Score (Sequential Organ Failure Assessment)
=================================================

Multi-organ dysfunction assessment for ICU patients

Reference:
- Vincent JL, et al. The SOFA (Sepsis-related Organ Failure Assessment) score to
  describe organ dysfunction/failure. Intensive Care Med. 1996;22(7):707-710.
- Singer M, et al. The Third International Consensus Definitions for Sepsis and
  Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-810.

SOFA Components (6 organ systems):
1. Respiratory: PaO₂/FiO₂ ratio
2. Coagulation: Platelets
3. Liver: Bilirubin
4. Cardiovascular: Mean arterial pressure (MAP) or vasopressors
5. Central Nervous System: Thang điểm hôn mê Glasgow
6. Renal: Creatinine or urine output

Score: 0-4 points per organ system → Total: 0-24 points

Clinical Utility:
- Assess organ dysfunction severity
- Monitor disease progression
- Predict mortality in ICU
- Sepsis-3 definition: SOFA ≥2 = sepsis
"""

import streamlit as st
from components.ui.scoring import (
    render_score_result,
    render_score_breakdown,
    render_quick_reference_table,
)
from .sofa_lookup import (
    get_respiratory_score,
    get_coagulation_score,
    get_liver_score,
    get_cns_score,
    get_renal_score,
)
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================
from scores.utils.validation import (
    validate_gcs,
    validate_blood_pressure,
    validate_heart_rate,
    validate_respiratory_rate,
    validate_lab_value,
    safe_divide,
    validate_ratio
)


def calculate_sofa(
    pao2_fio2: float,
    platelets: float,
    bilirubin: float,
    map_value: float,
    use_vasopressor: bool,
    vasopressor_type: str,
    vasopressor_dose: float,
    gcs: int,
    creatinine: float,
    urine_output: float
) -> dict:
    """
    Calculate SOFA Score
    
    Args:
        pao2_fio2: PaO2/FiO2 ratio (mmHg)
        platelets: Platelet count (×10³/μL)
        bilirubin: Total bilirubin (mg/dL)
        map_value: Mean arterial pressure (mmHg)
        use_vasopressor: Whether patient is on vasopressors
        vasopressor_type: Type of vasopressor (dopamine/dobutamine/epi/norepi)
        vasopressor_dose: Vasopressor dose (mcg/kg/min)
        gcs: Thang điểm hôn mê Glasgow
        creatinine: Serum creatinine (mg/dL)
        urine_output: Urine output (mL/day)
    
    Returns:
        Dictionary containing SOFA score, subscores, interpretation
    """
    
    subscores = {}
    details = []
    
    # 1. RESPIRATORY (PaO2/FiO2) - Using lookup table
    subscores['respiratory'] = get_respiratory_score(pao2_fio2)
    details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → {subscores['respiratory']} điểm")
    
    # 2. COAGULATION (Platelets) - Using lookup table
    subscores['coagulation'] = get_coagulation_score(platelets)
    details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → {subscores['coagulation']} điểm")
    
    # 3. LIVER (Bilirubin) - Using lookup table
    subscores['liver'] = get_liver_score(bilirubin)
    details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → {subscores['liver']} điểm")
    
    # 4. CARDIOVASCULAR
    if use_vasopressor:
        # On vasopressor
        if vasopressor_type == "Dopamine" and vasopressor_dose < 5:
            subscores['cardiovascular'] = 2
            details.append(f"**Tim mạch:** Dopamine <5 mcg/kg/min → 2 điểm")
        elif vasopressor_type == "Dopamine" and vasopressor_dose <= 15:
            subscores['cardiovascular'] = 3
            details.append(f"**Tim mạch:** Dopamine 5-15 mcg/kg/min → 3 điểm")
        elif vasopressor_type == "Dopamine" and vasopressor_dose > 15:
            subscores['cardiovascular'] = 4
            details.append(f"**Tim mạch:** Dopamine >15 mcg/kg/min → 4 điểm")
        elif vasopressor_type == "Dobutamine":
            subscores['cardiovascular'] = 2
            details.append(f"**Tim mạch:** Dobutamine (any dose) → 2 điểm")
        elif vasopressor_type in ["Epinephrine", "Norepinephrine"]:
            if vasopressor_dose <= 0.1:
                subscores['cardiovascular'] = 3
                details.append(f"**Tim mạch:** Epi/Norepi ≤0.1 mcg/kg/min → 3 điểm")
            else:
                subscores['cardiovascular'] = 4
                details.append(f"**Tim mạch:** Epi/Norepi >0.1 mcg/kg/min → 4 điểm")
    else:
        # No vasopressor - use MAP
        if map_value >= 70:
            subscores['cardiovascular'] = 0
            details.append(f"**Tim mạch:** MAP = {map_value:.0f} mmHg → 0 điểm")
        else:
            subscores['cardiovascular'] = 1
            details.append(f"**Tim mạch:** MAP = {map_value:.0f} mmHg → 1 điểm")
    
    # 5. CENTRAL NERVOUS SYSTEM (GCS) - Using lookup table
    subscores['cns'] = get_cns_score(gcs)
    details.append(f"**Thần kinh:** GCS = {gcs} → {subscores['cns']} điểm")
    
    # 6. RENAL - Using lookup table (combines creatinine and urine output)
    subscores['renal'], renal_detail = get_renal_score(creatinine, urine_output)
    details.append(renal_detail)
    
    # Calculate total
    total_score = sum(subscores.values())
    
    # Interpretation
    if total_score == 0:
        interpretation = "Không có suy cơ quan"
        mortality = "<10%"
        risk_class = "LOW"
        color = "🟢"
    elif total_score <= 6:
        interpretation = "Suy cơ quan nhẹ"
        mortality = "~10-20%"
        risk_class = "MILD"
        color = "🟡"
    elif total_score <= 11:
        interpretation = "Suy cơ quan trung bình"
        mortality = "~20-40%"
        risk_class = "MODERATE"
        color = "🟠"
    elif total_score <= 14:
        interpretation = "Suy cơ quan nặng"
        mortality = "~40-60%"
        risk_class = "SEVERE"
        color = "🔴"
    else:
        interpretation = "Suy cơ quan rất nặng"
        mortality = ">60%"
        risk_class = "CRITICAL"
        color = "🔴"
    
    # Management based on score
    if total_score >= 2:
        sepsis_note = f"""
        **⚠️ SOFA ≥2 điểm:**
        - Đáp ứng tiêu chuẩn **SEPSIS-3** (nếu có nhiễm trùng/nghi ngờ nhiễm trùng)
        - Cần đánh giá và xử trí nhiễm trùng huyết NGAY
        - Xem xét Sepsis Bundle (SSC 2021)
        """
    else:
        sepsis_note = ""
    
    return {
        'total_score': total_score,
        'subscores': subscores,
        'interpretation': interpretation,
        'mortality': mortality,
        'risk_class': risk_class,
        'color': color,
        'details': details,
        'sepsis_note': sepsis_note
    }


def render():
    """Render SOFA Score calculator in Streamlit"""
    
    st.title("🏥 SOFA Score")
    st.markdown("**Sequential Organ Failure Assessment - Đánh giá suy đa cơ quan**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'sofa':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Smart Suggestions (sidebar)
    with st.sidebar:
        render_suggestions(
            calculator_id="sofa",
            calculator_name="SOFA Score",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **SOFA (Sequential Organ Failure Assessment)** là thang điểm:
        - Đánh giá mức độ suy cơ quan ở bệnh nhân ICU
        - Dự đoán tử vong
        - Theo dõi diễn tiến bệnh
        - **Sepsis-3 definition:** SOFA ≥2 = Sepsis
        
        ### 🎯 6 hệ cơ quan
        
        1. **Hô hấp:** PaO₂/FiO₂ ratio
        2. **Đông máu:** Tiểu cầu
        3. **Gan:** Bilirubin
        4. **Tim mạch:** MAP hoặc vasopressor
        5. **Thần kinh:** Thang điểm hôn mê Glasgow
        6. **Thận:** Creatinine hoặc nước tiểu
        
        Mỗi hệ: 0-4 điểm → Tổng: 0-24 điểm
        
        ### 📊 Điểm & tử vong
        
        | SOFA Score | Tử vong ICU |
        |------------|-------------|
        | 0-6 | <20% |
        | 7-11 | 20-40% |
        | 12-14 | 40-60% |
        | ≥15 | >60% |
        
        ### ⚠️ Sepsis-3 Criteria
        
        **Sepsis = Nhiễm trùng + SOFA ≥2**
        
        - Tăng SOFA ≥2 điểm so với baseline
        - Nếu không biết baseline → giả định = 0
        - qSOFA dùng để screening ngoài ICU
        
        ### 📚 Tài liệu tham khảo
        
        - Vincent JL, et al. *Intensive Care Med* 1996;22:707-710
        - Singer M, et al. *JAMA* 2016;315:801-810 (Sepsis-3)
        """)
    
    st.divider()
    
    # Input section
    st.subheader("📝 Nhập thông số 6 hệ cơ quan")
    
    # Respiratory
    st.markdown("#### 1️⃣ Hô hấp (Respiratory)")
    col1, col2 = st.columns(2)
    with col1:
        pao2 = st.number_input("PaO₂ (mmHg)", 0, 700, 100, 1, format="%d", help="Áp lực oxy máu động mạch", key="sofa_pao2")
    with col2:
        fio2 = st.number_input("FiO₂ (%)", 21, 100, 21, 1, format="%d", help="Nồng độ oxy hít vào", key="sofa_fio2")
    
    # Calculate PaO2/FiO2 ratio safely
    if fio2 > 0:
        pao2_fio2 = (pao2 / (fio2 / 100.0)) if fio2 > 0 else 0
    else:
        pao2_fio2 = 0
    st.caption(f"💡 PaO₂/FiO₂ = {pao2_fio2:.0f} mmHg")
    
    st.divider()
    
    # Coagulation
    st.markdown("#### 2️⃣ Đông máu (Coagulation)")
    platelets = st.number_input("Tiểu cầu (×10³/μL)", 0, 500, 200, 1, format="%d", key="sofa_platelets")
    
    st.divider()
    
    # Liver
    st.markdown("#### 3️⃣ Gan (Liver)")
    bilirubin = st.number_input("Bilirubin toàn phần (mg/dL)", 0.0, 30.0, 1.0, 0.1, format="%.1f", key="sofa_bilirubin")
    st.caption("💡 Chuyển đổi: μmol/L ÷ 17.1 = mg/dL")
    
    st.divider()
    
    # Cardiovascular
    st.markdown("#### 4️⃣ Tim mạch (Cardiovascular)")
    use_vasopressor = st.checkbox("**Bệnh nhân đang dùng thuốc vận mạch (vasopressor)**", key="sofa_use_vasopressor")
    
    if use_vasopressor:
        col3, col4 = st.columns(2)
        with col3:
            vasopressor_type = st.selectbox(
                "Loại thuốc",
                ["Dopamine", "Dobutamine", "Epinephrine", "Norepinephrine"],
                key="sofa_vasopressor_type"
            )
        with col4:
            vasopressor_dose = st.number_input(
                "Liều (mcg/kg/min)",
                0.0, 50.0, 5.0, 0.1,
                format="%.1f",
                help="Liều thuốc vận mạch",
                key="sofa_vasopressor_dose"
            )
        map_value = 70.0  # Default when on vasopressor
    else:
        map_value = st.number_input("MAP - Huyết áp động mạch trung bình (mmHg)", 0, 200, 70, 1, format="%d", key="sofa_map")
        vasopressor_type = ""
        vasopressor_dose = 0.0
        st.caption("💡 MAP = (SBP + 2×DBP) / 3")
    
    st.divider()
    
    # Central Nervous System
    st.markdown("#### 5️⃣ Thần kinh (CNS)")
    gcs = st.number_input("Thang điểm hôn mê Glasgow (GCS) - Thang điểm hôn mê Glasgow", 3, 15, 15, 1, format="%d", key="sofa_gcs")
    st.caption("3 (tệ nhất) → 15 (bình thường)")
    
    st.divider()
    
    # Renal
    st.markdown("#### 6️⃣ Thận (Renal)")
    col5, col6 = st.columns(2)
    with col5:
        creatinine = st.number_input("Creatinine (mg/dL)", 0.0, 20.0, 1.0, 0.1, format="%.1f", key="sofa_creatinine")
        st.caption("💡 μmol/L ÷ 88.4 = mg/dL")
    with col6:
        urine_output = st.number_input("Nước tiểu 24h (mL)", 0, 5000, 1500, 10, format="%d", key="sofa_urine_output")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính SOFA Score", type="primary", use_container_width=True, key="sofa_calculate"):
        # Validate inputs before calculation
        validation_errors = []
        
        is_valid_gcs, gcs_error = validate_gcs(gcs)
        if not is_valid_gcs:
            validation_errors.append(gcs_error)
        
        is_valid_platelets, platelets_error = validate_lab_value(platelets, "Tiểu cầu", 0, 1000)
        if not is_valid_platelets:
            validation_errors.append(platelets_error)
        
        is_valid_bilirubin, bilirubin_error = validate_lab_value(bilirubin, "Bilirubin", 0, 50)
        if not is_valid_bilirubin:
            validation_errors.append(bilirubin_error)
        
        is_valid_creatinine, creatinine_error = validate_lab_value(creatinine, "Creatinine", 0, 20)
        if not is_valid_creatinine:
            validation_errors.append(creatinine_error)
        
        if validation_errors:
            st.error("**⚠️ Lỗi validation:**")
            for error in validation_errors:
                st.error(f"- {error}")
            st.stop()
        
        result = calculate_sofa(
            pao2_fio2=pao2_fio2,
            platelets=platelets,
            bilirubin=bilirubin,
            map_value=map_value,
            use_vasopressor=use_vasopressor,
            vasopressor_type=vasopressor_type,
            vasopressor_dose=vasopressor_dose,
            gcs=gcs,
            creatinine=creatinine,
            urine_output=urine_output
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Color-coded score result (MDCalc style)
        render_score_result(
            title="SOFA Score",
            score=result['total_score'],
            interpretation=result['interpretation'],
            mortality=result['mortality'],
            icon=result['color'],
            thresholds={"low": 6, "moderate": 11, "high": 14},
            size="large"
        )
        
        # Subscores breakdown
        organs_display = {
            "Hô hấp": result['subscores']['respiratory'],
            "Đông máu": result['subscores']['coagulation'],
            "Gan": result['subscores']['liver'],
            "Tim mạch": result['subscores']['cardiovascular'],
            "Thần kinh": result['subscores']['cns'],
            "Thận": result['subscores']['renal']
        }
        
        render_score_breakdown(
            title="📋 Điểm từng hệ cơ quan",
            subscores=organs_display,
            total_score=result['total_score']
        )
        
        # Detailed scoring breakdown
        with st.expander("📝 Chi tiết tính điểm", expanded=False):
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Sepsis note
        if result['sepsis_note']:
            st.warning(result['sepsis_note'])
        
        # Interpretation & Management
        st.info("""
        **📌 Diễn giải SOFA:**
        
        - **Tăng SOFA ≥2 điểm** trong 24-48h → xấu đi, nguy cơ tử vong tăng
        - **SOFA cao liên tục** → tiên lượng xấu
        - **SOFA giảm** → đáp ứng điều trị tốt
        
        **Theo dõi:**
        - Tính SOFA hàng ngày để đánh giá diễn tiến
        - So sánh với baseline để xác định Sepsis (Sepsis-3)
        """)
        
        if result['total_score'] >= 11:
            st.error("""
            **🚨 SOFA SCORE CAO:**
            
            - Bệnh nhân có suy đa cơ quan NẶNG
            - Nguy cơ tử vong CAO (>40%)
            - Cần hồi sức tích cực
            - Xem xét mức độ chăm sóc và tiên lượng
            - Thảo luận với gia đình về mục tiêu điều trị
            """)
        
        # Management recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo xử trí")
        
        recommendations = []
        
        if result['subscores']['respiratory'] >= 3:
            recommendations.append("""
            **Hô hấp (PaO₂/FiO₂ <200):**
            - Xem xét đặt nội khí quản + thở máy
            - ARDSNet protocol nếu ARDS
            - Lung protective ventilation
            """)
        
        if result['subscores']['coagulation'] >= 2:
            recommendations.append("""
            **Đông máu (Tiểu cầu <100):**
            - Tìm Nguyên nhân (DIC, sepsis, thuốc, HIT)
            - Xem xét truyền tiểu cầu nếu chảy máu hoặc thủ thuật
            - Tránh thuốc ảnh hưởng tiểu cầu
            """)
        
        if result['subscores']['liver'] >= 2:
            recommendations.append("""
            **Gan (Bilirubin >2):**
            - Đánh giá chức năng gan (ALT, AST, PT/INR)
            - Loại trừ viêm gan, tắc mật
            - Điều chỉnh liều thuốc
            """)
        
        if result['subscores']['cardiovascular'] >= 2:
            recommendations.append("""
            **Tim mạch (MAP thấp/cần vasopressor):**
            - Hồi sức dịch nếu hypovolemia
            - Vasopressor: Norepinephrine first-line
            - Mục tiêu MAP ≥65 mmHg
            - Echo đánh giá chức năng tim
            - Xem xét inotrope nếu cardiac dysfunction
            """)
        
        if result['subscores']['cns'] >= 2:
            recommendations.append("""
            **Thần kinh (GCS <13):**
            - Bảo vệ đường thở
            - CT đầu nếu cần
            - Loại trừ nguyên nhân: infection, metabolic, structural
            - Sedation scoring nếu đang an thần
            """)
        
        if result['subscores']['renal'] >= 2:
            recommendations.append("""
            **Thận (Cr >2 hoặc UO <500 mL/24h):**
            - Đánh giá theo KDIGO AKI criteria
            - Tìm Nguyên nhân: pre-renal/intrinsic/post-renal
            - Điều chỉnh liều thuốc
            - Theo dõi điện giải (K, PO4)
            - Xem xét RRT nếu chỉ định
            """)
        
        if recommendations:
            for rec in recommendations:
                st.markdown(rec)
        else:
            st.success("✅ Không có cơ quan nào suy nặng - tiếp tục theo dõi")
        
        # Save to session state
        st.session_state['sofa_result'] = result
        
        # Export section
        st.markdown("---")
        from components.export import render_export_section
        
        # Prepare inputs for export
        inputs_dict = {
            "PaO₂/FiO₂": f"{pao2_fio2:.0f}",
            "Platelets": f"{platelets:.0f} ×10³/μL",
            "Bilirubin": f"{bilirubin:.2f} mg/dL",
            "MAP": f"{map_value:.0f} mmHg",
            "Vasopressor": f"{vasopressor_type} ({vasopressor_dose:.2f} mcg/kg/min)" if use_vasopressor else "Không",
            "GCS": f"{gcs}",
            "Creatinine": f"{creatinine:.2f} mg/dL",
            "Urine Output": f"{urine_output:.0f} mL/24h"
        }
        
        # Prepare results for export
        results_dict = {
            "SOFA Score": f"{result['total_score']} điểm",
            "Interpretation": result['interpretation'],
            "Mortality Risk": result['mortality'],
            "Subscores": {
                "Respiratory": result['subscores']['respiratory'],
                "Coagulation": result['subscores']['coagulation'],
                "Liver": result['subscores']['liver'],
                "Cardiovascular": result['subscores']['cardiovascular'],
                "CNS": result['subscores']['cns'],
                "Renal": result['subscores']['renal']
            }
        }
        
        render_export_section(
            title=f"SOFA Score = {result['total_score']} điểm",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="SOFA Score",
            filename="sofa_score_result"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="sofa",
            calculator_name="SOFA Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="sofa",
            calculator_name="SOFA Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        from components.calculation_history import render_history_ui
        render_history_ui(calculator_id="sofa", show_actions=True)
        
        # Warning
        st.warning("""
        ⚠️ **Lưu ý y khoa:**
        - SOFA là công cụ đánh giá, không phải chẩn đoán
        - Cần kết hợp với lâm sàng và xét nghiệm khác
        - SOFA không dự đoán chính xác 100% - chỉ là ước tính
        - Quyết định điều trị cuối cùng thuộc về bác sĩ điều trị
        """)
    
    # Quick reference table
    with st.expander("📖 Bảng SOFA scoring chi tiết", expanded=False):
        render_quick_reference_table(
            title="Bảng SOFA scoring",
            headers=["Hệ cơ quan", "0", "1", "2", "3", "4"],
            rows=[
                ["Hô hấp (PaO₂/FiO₂, mmHg)", "≥400", "<400", "<300", "<200", "<100"],
                ["Đông máu (Platelets, ×10³/μL)", "≥150", "<150", "<100", "<50", "<20"],
                ["Gan (Bilirubin, mg/dL)", "<1.2", "1.2-1.9", "2.0-5.9", "6.0-11.9", "≥12"],
                ["Tim mạch", "MAP≥70", "MAP<70", "Dopa <5* hoặc Dobu", "Dopa 5-15* hoặc Epi/Norepi ≤0.1**", "Dopa >15* hoặc Epi/Norepi >0.1**"],
                ["Thần kinh (GCS)", "15", "13-14", "10-12", "6-9", "3-5"],
                ["Thận (Cr mg/dL hoặc UO)", "<1.2", "1.2-1.9", "2.0-3.4", "3.5-4.9 hoặc <500 mL/d", "≥5.0 hoặc <200 mL/d"],
            ]
        )
        
        st.markdown("""
        **Ghi chú:**
        - * Dopamine liều (mcg/kg/min)  
        - ** Epinephrine/Norepinephrine liều (mcg/kg/min)
        
        ### Sepsis-3 Definitions
        
        - **Sepsis:** Nhiễm trùng + SOFA ≥2 điểm
        - **Septic Shock:** Sepsis + Vasopressor để duy trì MAP ≥65 + Lactate >2 mmol/L
        
        ### Delta SOFA
        
        - Tính thay đổi SOFA so với baseline (nếu biết)
        - Nếu không biết baseline → giả định = 0
        - Tăng ≥2 điểm = có ý nghĩa lâm sàng
        """)
    
    # References section
    references = get_references("SOFA")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
