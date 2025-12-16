"""
Pediatric SOFA (pSOFA) Score
Sequential Organ Failure Assessment for pediatric ICU patients

Reference:
Matics TJ, Sanchez-Pinto LN. Adaptation and validation of a pediatric sequential organ failure assessment score and evaluation of the Sepsis-3 definitions in critically ill children.
Am J Respir Crit Care Med. 2017;196(2):208-217.
"""

import streamlit as st
import math
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================


def get_age_adjusted_map(age_years):
    """
    Get age-adjusted MAP threshold for pediatric patients
    
    Args:
        age_years: Age in years
    
    Returns:
        Normal MAP threshold (mmHg)
    """
    if age_years < 1:
        return 50  # < 1 year
    elif age_years < 5:
        return 55  # 1-4 years
    elif age_years < 12:
        return 60  # 5-11 years
    else:
        return 70  # ≥12 years (adult-like)


def get_age_adjusted_creatinine(age_years):
    """
    Get age-adjusted creatinine threshold for pediatric patients
    
    Args:
        age_years: Age in years
    
    Returns:
        Normal creatinine threshold (mg/dL)
    """
    if age_years < 1:
        return 0.8  # < 1 year
    elif age_years < 5:
        return 0.6  # 1-4 years
    elif age_years < 12:
        return 0.8  # 5-11 years
    else:
        return 1.2  # ≥12 years (adult-like)


def calculate_pediatric_sofa(
    age_years,
    pao2_fio2,
    platelets,
    bilirubin,
    map_value,
    use_vasopressor,
    vasopressor_type,
    vasopressor_dose,
    pediatric_gcs,
    creatinine,
    urine_output_ml_kg_hour
):
    """
    Calculate Pediatric SOFA Score
    
    Args:
        age_years: Age in years
        pao2_fio2: PaO2/FiO2 ratio (mmHg)
        platelets: Platelet count (×10³/μL)
        bilirubin: Total bilirubin (mg/dL)
        map_value: Mean arterial pressure (mmHg)
        use_vasopressor: Whether patient is on vasopressors
        vasopressor_type: Type of vasopressor
        vasopressor_dose: Vasopressor dose (mcg/kg/min)
        pediatric_gcs: Pediatric GCS (3-15)
        creatinine: Serum creatinine (mg/dL)
        urine_output_ml_kg_hour: Urine output (mL/kg/hour)
    
    Returns:
        dict with total score, subscores, interpretation
    """
    subscores = {}
    details = []
    
    # Age-adjusted thresholds
    normal_map = get_age_adjusted_map(age_years)
    normal_creatinine = get_age_adjusted_creatinine(age_years)
    
    # 1. RESPIRATORY (PaO2/FiO2) - Similar to adult
    if pao2_fio2 >= 400:
        subscores['respiratory'] = 0
        details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → 0 điểm")
    elif pao2_fio2 >= 300:
        subscores['respiratory'] = 1
        details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → 1 điểm")
    elif pao2_fio2 >= 200:
        subscores['respiratory'] = 2
        details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → 2 điểm")
    elif pao2_fio2 >= 100:
        subscores['respiratory'] = 3
        details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → 3 điểm")
    else:
        subscores['respiratory'] = 4
        details.append(f"**Hô hấp:** PaO₂/FiO₂ = {pao2_fio2:.0f} → 4 điểm")
    
    # 2. COAGULATION (Platelets) - Similar to adult
    if platelets >= 150:
        subscores['coagulation'] = 0
        details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → 0 điểm")
    elif platelets >= 100:
        subscores['coagulation'] = 1
        details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → 1 điểm")
    elif platelets >= 50:
        subscores['coagulation'] = 2
        details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → 2 điểm")
    elif platelets >= 20:
        subscores['coagulation'] = 3
        details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → 3 điểm")
    else:
        subscores['coagulation'] = 4
        details.append(f"**Đông máu:** Tiểu cầu = {platelets:.0f} → 4 điểm")
    
    # 3. LIVER (Bilirubin) - Similar to adult
    if bilirubin < 1.2:
        subscores['liver'] = 0
        details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → 0 điểm")
    elif bilirubin < 2.0:
        subscores['liver'] = 1
        details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → 1 điểm")
    elif bilirubin < 6.0:
        subscores['liver'] = 2
        details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → 2 điểm")
    elif bilirubin < 12.0:
        subscores['liver'] = 3
        details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → 3 điểm")
    else:
        subscores['liver'] = 4
        details.append(f"**Gan:** Bilirubin = {bilirubin:.1f} → 4 điểm")
    
    # 4. CARDIOVASCULAR - Age-adjusted MAP
    if use_vasopressor:
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
        # No vasopressor - use age-adjusted MAP
        if map_value >= normal_map:
            subscores['cardiovascular'] = 0
            details.append(f"**Tim mạch:** MAP = {map_value:.0f} mmHg (≥{normal_map} cho tuổi {age_years:.0f}) → 0 điểm")
        else:
            subscores['cardiovascular'] = 1
            details.append(f"**Tim mạch:** MAP = {map_value:.0f} mmHg (<{normal_map} cho tuổi {age_years:.0f}) → 1 điểm")
    
    # 5. CENTRAL NERVOUS SYSTEM (Pediatric GCS)
    if pediatric_gcs == 15:
        subscores['cns'] = 0
        details.append(f"**Thần kinh:** Pediatric GCS = 15 → 0 điểm")
    elif pediatric_gcs >= 13:
        subscores['cns'] = 1
        details.append(f"**Thần kinh:** Pediatric GCS = {pediatric_gcs} → 1 điểm")
    elif pediatric_gcs >= 10:
        subscores['cns'] = 2
        details.append(f"**Thần kinh:** Pediatric GCS = {pediatric_gcs} → 2 điểm")
    elif pediatric_gcs >= 6:
        subscores['cns'] = 3
        details.append(f"**Thần kinh:** Pediatric GCS = {pediatric_gcs} → 3 điểm")
    else:
        subscores['cns'] = 4
        details.append(f"**Thần kinh:** Pediatric GCS = {pediatric_gcs} → 4 điểm")
    
    # 6. RENAL - Age-adjusted creatinine and urine output
    # Check urine output first (more sensitive)
    if urine_output_ml_kg_hour >= 1.0:
        # Normal urine output
        if creatinine <= normal_creatinine:
            subscores['renal'] = 0
            details.append(f"**Thận:** Creatinine = {creatinine:.2f} (≤{normal_creatinine:.1f} cho tuổi {age_years:.0f}), UO ≥1.0 mL/kg/h → 0 điểm")
        elif creatinine <= normal_creatinine * 2:
            subscores['renal'] = 1
            details.append(f"**Thận:** Creatinine = {creatinine:.2f} (1-2× normal cho tuổi {age_years:.0f}), UO ≥1.0 mL/kg/h → 1 điểm")
        elif creatinine <= normal_creatinine * 3:
            subscores['renal'] = 2
            details.append(f"**Thận:** Creatinine = {creatinine:.2f} (2-3× normal cho tuổi {age_years:.0f}), UO ≥1.0 mL/kg/h → 2 điểm")
        elif creatinine <= normal_creatinine * 4:
            subscores['renal'] = 3
            details.append(f"**Thận:** Creatinine = {creatinine:.2f} (3-4× normal cho tuổi {age_years:.0f}), UO ≥1.0 mL/kg/h → 3 điểm")
        else:
            subscores['renal'] = 4
            details.append(f"**Thận:** Creatinine = {creatinine:.2f} (>4× normal cho tuổi {age_years:.0f}), UO ≥1.0 mL/kg/h → 4 điểm")
    else:
        # Low urine output
        if urine_output_ml_kg_hour >= 0.5:
            if creatinine <= normal_creatinine * 2:
                subscores['renal'] = 3
                details.append(f"**Thận:** Creatinine = {creatinine:.2f}, UO 0.5-1.0 mL/kg/h → 3 điểm")
            else:
                subscores['renal'] = 4
                details.append(f"**Thận:** Creatinine = {creatinine:.2f}, UO 0.5-1.0 mL/kg/h → 4 điểm")
        else:
            # Very low or no urine output
            subscores['renal'] = 4
            details.append(f"**Thận:** Creatinine = {creatinine:.2f}, UO <0.5 mL/kg/h → 4 điểm")
    
    # Calculate total score
    total_score = sum(subscores.values())
    
    # Interpretation
    if total_score == 0:
        interpretation = "Không có suy cơ quan"
        color = "success"
        mortality = "< 5%"
    elif total_score <= 6:
        interpretation = "Suy cơ quan nhẹ"
        color = "info"
        mortality = "5-10%"
    elif total_score <= 11:
        interpretation = "Suy cơ quan trung bình"
        color = "warning"
        mortality = "10-25%"
    elif total_score <= 16:
        interpretation = "Suy cơ quan nặng"
        color = "error"
        mortality = "25-50%"
    else:
        interpretation = "Suy đa cơ quan rất nặng"
        color = "error"
        mortality = "> 50%"
    
    # Sepsis note (pSOFA ≥2 suggests sepsis)
    sepsis_note = None
    if total_score >= 2:
        sepsis_note = f"⚠️ **pSOFA ≥2:** Gợi ý nhiễm trùng huyết (sepsis) ở trẻ em. Cần đánh giá toàn diện và điều trị tích cực."
    
    return {
        "total_score": total_score,
        "subscores": subscores,
        "details": details,
        "interpretation": interpretation,
        "color": color,
        "mortality": mortality,
        "sepsis_note": sepsis_note,
        "age_years": age_years,
        "normal_map": normal_map,
        "normal_creatinine": normal_creatinine
    }


def render():
    """Pediatric SOFA Score Calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'pediatric_sofa':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Pediatric SOFA')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.subheader("👶 Pediatric SOFA (pSOFA) Score")
    st.caption("Sequential Organ Failure Assessment for Pediatric ICU Patients")
    
    st.info("""
    **Pediatric SOFA (pSOFA)** đánh giá mức độ suy đa cơ quan ở trẻ em ICU.
    
    **6 Hệ thống cơ quan:**
    - Hô hấp (Respiratory)
    - Đông máu (Coagulation)
    - Gan (Liver)
    - Tim mạch (Cardiovascular) - **Điều chỉnh theo tuổi**
    - Thần kinh (Central Nervous System) - **Pediatric GCS**
    - Thận (Renal) - **Điều chỉnh theo tuổi**
    
    **Điểm số:** 0-24 (càng cao = càng nặng)
    **pSOFA ≥2:** Gợi ý nhiễm trùng huyết (sepsis)
    """)
    
    st.markdown("---")
    
    # Patient info
    st.markdown("### 📋 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age_years = st.number_input(
            "Tuổi (năm)",
            min_value=0.0,
            max_value=18.0,
            value=5.0,
            step=0.1,
            format="%.1f",
            key="psofa_age"
        )
        
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=0.5,
            max_value=100.0,
            value=20.0,
            step=0.5,
            format="%.1f",
            key="psofa_weight"
        )
    
    with col2:
        # Display age-adjusted thresholds
        normal_map = get_age_adjusted_map(age_years)
        normal_creatinine = get_age_adjusted_creatinine(age_years)
        
        st.info(f"""
        **Ngưỡng theo tuổi:**
        - MAP bình thường: **≥{normal_map} mmHg**
        - Creatinine bình thường: **≤{normal_creatinine:.1f} mg/dL**
        """)
    
    st.markdown("---")
    
    # Organ system inputs
    st.markdown("### 🩺 Thông số Cơ Quan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Respiratory
        st.markdown("#### 1️⃣ Hô hấp")
        pao2 = st.number_input(
            "PaO₂ (mmHg):",
            min_value=30.0,
            max_value=600.0,
            value=100.0,
            step=1.0,
            key="psofa_pao2"
        )
        
        fio2 = st.slider(
            "FiO₂ (%):",
            min_value=21,
            max_value=100,
            value=50,
            step=1,
            key="psofa_fio2"
        )
        fio2_decimal = fio2 / 100
        pao2_fio2 = pao2 / fio2_decimal
        
        st.info(f"**PaO₂/FiO₂ = {pao2_fio2:.0f} mmHg**")
        
        st.markdown("---")
        
        # Coagulation
        st.markdown("#### 2️⃣ Đông máu")
        platelets = st.number_input(
            "Tiểu cầu (×10³/μL):",
            min_value=0.0,
            max_value=1000.0,
            value=200.0,
            step=10.0,
            key="psofa_platelets"
        )
        
        st.markdown("---")
        
        # Liver
        st.markdown("#### 3️⃣ Gan")
        bilirubin = st.number_input(
            "Bilirubin toàn phần (mg/dL):",
            min_value=0.0,
            max_value=30.0,
            value=1.0,
            step=0.1,
            format="%.1f",
            key="psofa_bilirubin"
        )
    
    with col2:
        # Cardiovascular
        st.markdown("#### 4️⃣ Tim mạch")
        map_value = st.number_input(
            f"MAP (mmHg) [Bình thường ≥{normal_map} cho tuổi {age_years:.0f}]:",
            min_value=30.0,
            max_value=150.0,
            value=float(normal_map),
            step=1.0,
            key="psofa_map"
        )
        
        use_vasopressor = st.checkbox(
            "Đang dùng vasopressor",
            key="psofa_vasopressor"
        )
        
        if use_vasopressor:
            vasopressor_type = st.selectbox(
                "Loại vasopressor:",
                ["Dopamine", "Dobutamine", "Epinephrine", "Norepinephrine"],
                key="psofa_vasopressor_type"
            )
            
            vasopressor_dose = st.number_input(
                "Liều (mcg/kg/min):",
                min_value=0.0,
                max_value=50.0,
                value=5.0,
                step=0.1,
                format="%.1f",
                key="psofa_vasopressor_dose"
            )
        else:
            vasopressor_type = ""
            vasopressor_dose = 0.0
        
        st.markdown("---")
        
        # CNS
        st.markdown("#### 5️⃣ Thần kinh")
        pediatric_gcs = st.number_input(
            "Pediatric GCS (3-15):",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            key="psofa_gcs"
        )
        
        st.markdown("---")
        
        # Renal
        st.markdown("#### 6️⃣ Thận")
        creatinine = st.number_input(
            f"Creatinine (mg/dL) [Bình thường ≤{normal_creatinine:.1f} cho tuổi {age_years:.0f}]:",
            min_value=0.1,
            max_value=10.0,
            value=normal_creatinine,
            step=0.1,
            format="%.2f",
            key="psofa_creatinine"
        )
        
        urine_output_ml_kg_hour = st.number_input(
            "Lượng nước tiểu (mL/kg/giờ):",
            min_value=0.0,
            max_value=10.0,
            value=1.0,
            step=0.1,
            format="%.1f",
            key="psofa_urine"
        )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🧮 Tính pSOFA Score", type="primary", use_container_width=True, key="psofa_calculate"):
        result = calculate_pediatric_sofa(
            age_years=age_years,
            pao2_fio2=pao2_fio2,
            platelets=platelets,
            bilirubin=bilirubin,
            map_value=map_value,
            use_vasopressor=use_vasopressor,
            vasopressor_type=vasopressor_type,
            vasopressor_dose=vasopressor_dose,
            pediatric_gcs=pediatric_gcs,
            creatinine=creatinine,
            urine_output_ml_kg_hour=urine_output_ml_kg_hour
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Color-coded score
        if result["color"] == "success":
            st.success(f"## **pSOFA Score: {result['total_score']}/24**")
        elif result["color"] == "info":
            st.info(f"## **pSOFA Score: {result['total_score']}/24**")
        elif result["color"] == "warning":
            st.warning(f"## **pSOFA Score: {result['total_score']}/24**")
        else:
            st.error(f"## **pSOFA Score: {result['total_score']}/24**")
        
        st.markdown(f"**Đánh giá:** {result['interpretation']}")
        st.markdown(f"**Tỷ lệ tử vong ước tính:** {result['mortality']}")
        
        # Sepsis note
        if result["sepsis_note"]:
            st.warning(result["sepsis_note"])
        
        st.markdown("---")
        
        # Subscores breakdown
        st.markdown("### 📋 Điểm từng hệ cơ quan")
        
        organs_display = {
            "Hô hấp": result['subscores']['respiratory'],
            "Đông máu": result['subscores']['coagulation'],
            "Gan": result['subscores']['liver'],
            "Tim mạch": result['subscores']['cardiovascular'],
            "Thần kinh": result['subscores']['cns'],
            "Thận": result['subscores']['renal']
        }
        
        col1, col2, col3 = st.columns(3)
        
        for i, (organ, score) in enumerate(organs_display.items()):
            with col1 if i % 3 == 0 else (col2 if i % 3 == 1 else col3):
                st.metric(organ, f"{score}/4")
        
        st.markdown("---")
        
        # Detailed scoring
        with st.expander("📝 Chi tiết tính điểm", expanded=False):
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        st.markdown("---")
        
        # Clinical implications
        st.markdown("### 💊 Ý nghĩa lâm sàng")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Theo dõi:**
            - Đánh giá lại pSOFA mỗi 24 giờ
            - Theo dõi xu hướng (tăng/giảm)
            - Delta pSOFA (thay đổi) quan trọng hơn giá trị tuyệt đối
            
            **Điều trị:**
            - pSOFA ≥2: Cân nhắc điều trị nhiễm trùng huyết
            - pSOFA tăng: Cần can thiệp tích cực hơn
            - pSOFA giảm: Đáp ứng điều trị tốt
            """)
        
        with col2:
            st.markdown("""
            **Tiên lượng:**
            - pSOFA 0-6: Tiên lượng tốt
            - pSOFA 7-11: Tiên lượng trung bình
            - pSOFA 12-16: Tiên lượng xấu
            - pSOFA >16: Tiên lượng rất xấu
            
            **⚠️ Lưu ý:**
            - pSOFA chỉ là công cụ hỗ trợ
            - Cần đánh giá lâm sàng toàn diện
            - Tuổi ảnh hưởng đến thresholds
            """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Age (years)": age_years,
            "PaO2/FiO2": pao2_fio2,
            "Platelets": platelets,
            "Bilirubin": bilirubin,
            "MAP": map_value,
            "Vasopressor": "Yes" if use_vasopressor else "No",
            "Pediatric GCS": pediatric_gcs,
            "Creatinine": creatinine,
            "Urine Output": urine_output_ml_kg_hour
        }
        
        results_dict = {
            "Pediatric SOFA": f"{result['total_score']}/24",
            "Respiratory": result['subscores']['respiratory'],
            "Coagulation": result['subscores']['coagulation'],
            "Liver": result['subscores']['liver'],
            "Cardiovascular": result['subscores']['cardiovascular'],
            "CNS": result['subscores']['cns'],
            "Renal": result['subscores']['renal']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="pediatric_sofa",
            calculator_name="Pediatric SOFA",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="pediatric_sofa",
            calculator_name="Pediatric SOFA",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="pediatric_sofa",
            calculator_name="Pediatric SOFA",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="pediatric_sofa", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="pediatric_sofa",
            calculator_name="Pediatric SOFA",
            category="Nhi khoa",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.markdown("---")
    
    # References
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **Matics TJ, Sanchez-Pinto LN.** Adaptation and validation of a pediatric sequential organ failure assessment score and evaluation of the Sepsis-3 definitions in critically ill children.
       Am J Respir Crit Care Med. 2017;196(2):208-217.
    
    2. **UpToDate:** Pediatric Sepsis - Last updated 2024
       - pSOFA score
       - Sepsis-3 definitions for pediatrics
    
    3. **Vincent JL, et al.** The SOFA (Sepsis-related Organ Failure Assessment) score to describe organ dysfunction/failure.
       Intensive Care Med. 1996;22(7):707-710.
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Pediatric SOFA chỉ mang tính tham khảo. Quyết định điều trị phải dựa trên đánh giá toàn diện bởi bác sĩ có kinh nghiệm. Các ngưỡng được điều chỉnh theo tuổi để phù hợp với sinh lý trẻ em.")
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("Pediatric SOFA")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )

