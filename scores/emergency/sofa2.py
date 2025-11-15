"""
SOFA-2 Score (Sequential Organ Failure Assessment - Version 2, 2025)
====================================================================

Updated version reflecting modern critical care practice
Based on big data from millions of ICU patients

Reference:
- Published October 2025
- Adjusted thresholds for improved accuracy
- Integrated modern organ support measures

SOFA-2 Improvements:
1. Adjusted thresholds based on big data
2. Modern respiratory support: HFNC, ECMO
3. Enhanced vasopressor scoring
4. Renal replacement therapy (RRT) integration
5. Improved predictive accuracy

Components (6 organ systems - same as SOFA):
1. Respiratory: PaO₂/FiO₂, HFNC, ECMO
2. Coagulation: Platelets
3. Liver: Bilirubin
4. Cardiovascular: MAP, modern vasopressors
5. Central Nervous System: Glasgow Coma Scale
6. Renal: Creatinine, urine output, RRT

Score: 0-4 points per organ system → Total: 0-24 points
"""

import streamlit as st




from .sofa2_helpers import (
    _get_respiratory_score_sofa2,
    _get_coagulation_score_sofa2,
    _get_liver_score_sofa2,
    _get_cardiovascular_score_sofa2,
    _get_cns_score_sofa2,
    _get_renal_score_sofa2,
    _interpret_sofa2_score
)

def calculate_sofa2(
    pao2_fio2: float,
    respiratory_support: str,  # "none", "oxygen", "hfnc", "niv", "mv", "ecmo"
    hfnc_flow: float = None,  # L/min for HFNC
    platelets: float = None,
    bilirubin: float = None,
    map_value: float = None,
    use_vasopressor: bool = False,
    vasopressor_type: str = "",
    vasopressor_dose: float = 0.0,
    gcs: int = None,
    creatinine: float = None,
    urine_output: float = None,
    on_rrt: bool = False  # Renal Replacement Therapy
) -> dict:
    """
    Calculate SOFA-2 Score (2025 version)
    
    Args:
        pao2_fio2: PaO2/FiO2 ratio (mmHg)
        respiratory_support: Type of respiratory support
        hfnc_flow: HFNC flow rate (L/min) if applicable
        platelets: Platelet count (×10³/μL)
        bilirubin: Total bilirubin (mg/dL)
        map_value: Mean arterial pressure (mmHg)
        use_vasopressor: Whether patient is on vasopressors
        vasopressor_type: Type of vasopressor
        vasopressor_dose: Vasopressor dose (mcg/kg/min)
        gcs: Glasgow Coma Scale
        creatinine: Serum creatinine (mg/dL)
        urine_output: Urine output (mL/day)
        on_rrt: Whether patient is on RRT
    
    Returns:
        Dictionary containing SOFA-2 score, subscores, interpretation
    """
    
    subscores = {}
    details = []
    
    # 1. RESPIRATORY - Updated with HFNC and ECMO
    respiratory_score = _get_respiratory_score_sofa2(
        pao2_fio2, respiratory_support, hfnc_flow
    )
    subscores['respiratory'] = respiratory_score['score']
    details.append(respiratory_score['detail'])
    
    # 2. COAGULATION - Adjusted thresholds
    if platelets is not None:
        coagulation_score = _get_coagulation_score_sofa2(platelets)
        subscores['coagulation'] = coagulation_score['score']
        details.append(coagulation_score['detail'])
    
    # 3. LIVER - Adjusted thresholds
    if bilirubin is not None:
        liver_score = _get_liver_score_sofa2(bilirubin)
        subscores['liver'] = liver_score['score']
        details.append(liver_score['detail'])
    
    # 4. CARDIOVASCULAR - Enhanced vasopressor scoring
    if use_vasopressor or map_value is not None:
        cv_score = _get_cardiovascular_score_sofa2(
            map_value, use_vasopressor, vasopressor_type, vasopressor_dose
        )
        subscores['cardiovascular'] = cv_score['score']
        details.append(cv_score['detail'])
    
    # 5. CENTRAL NERVOUS SYSTEM - Same as original
    if gcs is not None:
        cns_score = _get_cns_score_sofa2(gcs)
        subscores['cns'] = cns_score['score']
        details.append(cns_score['detail'])
    
    # 6. RENAL - Updated with RRT
    if creatinine is not None or urine_output is not None or on_rrt:
        renal_score = _get_renal_score_sofa2(creatinine, urine_output, on_rrt)
        subscores['renal'] = renal_score['score']
        details.append(renal_score['detail'])
    
    # Calculate total
    total_score = sum(subscores.values())
    
    # Interpretation - Updated based on big data
    interpretation_data = _interpret_sofa2_score(total_score)
    
    # Sepsis-3 criteria (SOFA-2 still uses ≥2 for sepsis)
    if total_score >= 2:
        sepsis_note = f"""
        **⚠️ SOFA-2 ≥2 điểm:**
        - Đáp ứng tiêu chuẩn **SEPSIS-3** (nếu có nhiễm trùng/nghi ngờ nhiễm trùng)
        - Cần đánh giá và xử trí nhiễm trùng huyết NGAY
        - Xem xét Sepsis Bundle (SSC 2021)
        """
    else:
        sepsis_note = ""
    
    return {
        'total_score': total_score,
        'subscores': subscores,
        'interpretation': interpretation_data['interpretation'],
        'mortality': interpretation_data['mortality'],
        'risk_class': interpretation_data['risk_class'],
        'color': interpretation_data['color'],
        'details': details,
        'sepsis_note': sepsis_note,
        'version': 'SOFA-2 (2025)'
    }



def render():
    """Render SOFA-2 Score calculator in Streamlit"""
    
    st.title("🏥 SOFA-2 Score")
    st.markdown("**Sequential Organ Failure Assessment - Version 2 (2025) - Đánh giá suy đa cơ quan**")
    
    # Badge for new version
    st.info("✨ **Version 2025:** Điều chỉnh ngưỡng từ dữ liệu lớn, tích hợp hỗ trợ cơ quan hiện đại")
    
    # Educational information
    with st.expander("ℹ️ Thông Tin SOFA-2 (2025) & Cách Sử Dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu SOFA-2
        
        **SOFA-2 (Sequential Organ Failure Assessment - Version 2)** là phiên bản cập nhật:
        - Công bố tháng 10/2025
        - Dựa trên dữ liệu lớn từ hàng triệu bệnh nhân ICU
        - Phản ánh thực hành hồi sức hiện đại
        - Tăng tính chính xác và khả năng tiên đoán
        
        ### 🆕 Cải Tiến So Với SOFA Gốc
        
        1. **Ngưỡng điều chỉnh:** Dựa trên big data 2025
        2. **Hỗ trợ hô hấp hiện đại:**
           - HFNC (High Flow Nasal Cannula)
           - ECMO (Extracorporeal Membrane Oxygenation)
           - NIV (Non-Invasive Ventilation)
        3. **Vasopressor mới:**
           - Vasopressin
           - Phenylephrine
           - Liều chuẩn hóa tốt hơn
        4. **Thận:**
           - Tích hợp RRT (Renal Replacement Therapy)
        5. **Tiên đoán tử vong:** Cải thiện độ chính xác
        
        ### 🎯 6 Hệ Cơ Quan (Giữ Nguyên Cấu Trúc)
        
        1. **Hô hấp:** PaO₂/FiO₂ + hỗ trợ (HFNC, ECMO, MV, NIV)
        2. **Đông máu:** Tiểu cầu
        3. **Gan:** Bilirubin
        4. **Tim mạch:** MAP hoặc vasopressor hiện đại
        5. **Thần kinh:** Glasgow Coma Scale
        6. **Thận:** Creatinine, nước tiểu, RRT
        
        Mỗi hệ: 0-4 điểm → Tổng: 0-24 điểm
        
        ### 📊 Điểm & Tử Vong (Cập Nhật 2025)
        
        | SOFA-2 Score | Tử Vong ICU | So Với SOFA Gốc |
        |--------------|-------------|-----------------|
        | 0 | <8% | Cải thiện |
        | 1-6 | 8-18% | Chính xác hơn |
        | 7-11 | 18-38% | Chính xác hơn |
        | 12-14 | 38-58% | Chính xác hơn |
        | ≥15 | >58% | Chính xác hơn |
        
        ### ⚠️ Sepsis-3 Criteria (Vẫn Giữ Nguyên)
        
        **Sepsis = Nhiễm trùng + SOFA-2 ≥2**
        
        - Tăng SOFA-2 ≥2 điểm so với baseline
        - Nếu không biết baseline → giả định = 0
        
        ### 📚 Tài Liệu Tham Khảo
        
        - SOFA-2 Publication (October 2025)
        - Vincent JL, et al. *Intensive Care Med* 1996;22:707-710 (Original SOFA)
        - Singer M, et al. *JAMA* 2016;315:801-810 (Sepsis-3)
        """)
    
    st.divider()
    
    # Input section
    st.subheader("📝 Nhập Thông Số 6 Hệ Cơ Quan")
    
    # Respiratory
    st.markdown("#### 1️⃣ Hô Hấp (Respiratory) - Với Hỗ Trợ Hiện Đại")
    col1, col2 = st.columns(2)
    with col1:
        pao2 = st.number_input("PaO₂ (mmHg)", 0, 700, 100, 1, format="%d")
    with col2:
        fio2 = st.number_input("FiO₂ (%)", 21, 100, 21, 1, format="%d")
    
    pao2_fio2 = (pao2 / fio2) * 100 if fio2 > 0 else 0
    st.caption(f"💡 PaO₂/FiO₂ = {pao2_fio2:.0f} mmHg")
    
    respiratory_support = st.selectbox(
        "Hỗ trợ hô hấp",
        ["none", "oxygen", "hfnc", "niv", "mv", "ecmo"],
        format_func=lambda x: {
            "none": "Tự thở",
            "oxygen": "Oxy thông thường",
            "hfnc": "HFNC (High Flow Nasal Cannula)",
            "niv": "NIV (Non-Invasive Ventilation)",
            "mv": "Thở máy (Mechanical Ventilation)",
            "ecmo": "ECMO (Extracorporeal Membrane Oxygenation)"
        }[x]
    )
    
    hfnc_flow = None
    if respiratory_support == "hfnc":
        hfnc_flow = st.number_input("HFNC Flow (L/min)", 20, 70, 50, 1, format="%d")
    
    st.divider()
    
    # Coagulation
    st.markdown("#### 2️⃣ Đông Máu (Coagulation)")
    platelets = st.number_input("Tiểu cầu (×10³/μL)", 0, 500, 200, 1, format="%d")
    
    st.divider()
    
    # Liver
    st.markdown("#### 3️⃣ Gan (Liver)")
    bilirubin = st.number_input("Bilirubin toàn phần (mg/dL)", 0.0, 30.0, 1.0, 0.1, format="%.1f")
    st.caption("💡 Chuyển đổi: μmol/L ÷ 17.1 = mg/dL")
    
    st.divider()
    
    # Cardiovascular
    st.markdown("#### 4️⃣ Tim Mạch (Cardiovascular) - Vasopressor Hiện Đại")
    use_vasopressor = st.checkbox("**Bệnh nhân đang dùng thuốc vận mạch**")
    
    if use_vasopressor:
        col3, col4 = st.columns(2)
        with col3:
            vasopressor_type = st.selectbox(
                "Loại thuốc",
                ["Norepinephrine", "Epinephrine", "Vasopressin", "Phenylephrine", "Dopamine", "Dobutamine"]
            )
        with col4:
            if vasopressor_type in ["Norepinephrine", "Epinephrine", "Phenylephrine", "Dopamine", "Dobutamine"]:
                unit = "mcg/kg/min"
                max_val = 5.0
            else:  # Vasopressin
                unit = "U/min"
                max_val = 0.2
            
            vasopressor_dose = st.number_input(
                f"Liều ({unit})",
                0.0, max_val, 0.1 if unit == "mcg/kg/min" else 0.03, 0.01,
                format="%.2f"
            )
        map_value = 70.0
    else:
        map_value = st.number_input("MAP - Mean Arterial Pressure (mmHg)", 0, 200, 70, 1, format="%d")
        vasopressor_type = ""
        vasopressor_dose = 0.0
        st.caption("💡 MAP = (SBP + 2×DBP) / 3")
    
    st.divider()
    
    # Central Nervous System
    st.markdown("#### 5️⃣ Thần Kinh (CNS)")
    gcs = st.number_input("Glasgow Coma Scale (GCS)", 3, 15, 15, 1, format="%d")
    st.caption("3 (tệ nhất) → 15 (bình thường)")
    
    st.divider()
    
    # Renal
    st.markdown("#### 6️⃣ Thận (Renal) - Với RRT")
    on_rrt = st.checkbox("**Đang lọc máu (RRT - Renal Replacement Therapy)**")
    
    col5, col6 = st.columns(2)
    with col5:
        creatinine = st.number_input("Creatinine (mg/dL)", 0.0, 20.0, 1.0, 0.1, format="%.1f")
        st.caption("💡 μmol/L ÷ 88.4 = mg/dL")
    with col6:
        urine_output = st.number_input("Nước tiểu 24h (mL)", 0, 5000, 1500, 10, format="%d")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính SOFA-2 Score", type="primary", use_container_width=True):
        result = calculate_sofa2(
            pao2_fio2=pao2_fio2,
            respiratory_support=respiratory_support,
            hfnc_flow=hfnc_flow,
            platelets=platelets,
            bilirubin=bilirubin,
            map_value=map_value,
            use_vasopressor=use_vasopressor,
            vasopressor_type=vasopressor_type,
            vasopressor_dose=vasopressor_dose,
            gcs=gcs,
            creatinine=creatinine,
            urine_output=urine_output,
            on_rrt=on_rrt
        )
        
        # Display results
        st.subheader("📊 Kết Quả SOFA-2")
        
        # Score box
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                label="**SOFA-2 Score**",
                value=f"{result['total_score']} điểm"
            )
            st.caption("0-24 điểm (cao = nặng hơn)")
            st.caption(f"Version: {result['version']}")
        
        with col_r2:
            st.markdown(f"### {result['color']} {result['interpretation']}")
            st.markdown(f"**Tử vong ước tính: {result['mortality']}**")
            st.caption("(Cải thiện độ chính xác so với SOFA gốc)")
        
        # Subscores table
        with st.expander("📋 Điểm Từng Hệ Cơ Quan", expanded=True):
            cols = st.columns(6)
            organs = [
                ("Hô hấp", "respiratory"),
                ("Đông máu", "coagulation"),
                ("Gan", "liver"),
                ("Tim mạch", "cardiovascular"),
                ("Thần kinh", "cns"),
                ("Thận", "renal")
            ]
            
            for col, (name, key) in zip(cols, organs):
                with col:
                    score = result['subscores'].get(key, 0)
                    st.metric(name, f"{score}")
            
            st.markdown("---")
            st.markdown("**Chi tiết tính điểm:**")
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Sepsis note
        if result['sepsis_note']:
            st.warning(result['sepsis_note'])
        
        # Interpretation & Management
        st.info("""
        **📌 Diễn Giải SOFA-2:**
        
        - **Tăng SOFA-2 ≥2 điểm** trong 24-48h → xấu đi, nguy cơ tử vong tăng
        - **SOFA-2 cao liên tục** → tiên lượng xấu
        - **SOFA-2 giảm** → đáp ứng điều trị tốt
        
        **Theo dõi:**
        - Tính SOFA-2 hàng ngày để đánh giá diễn tiến
        - So sánh với baseline để xác định Sepsis (Sepsis-3)
        - SOFA-2 có độ chính xác cao hơn SOFA gốc nhờ big data 2025
        """)
        
        if result['total_score'] >= 11:
            st.error("""
            **🚨 SOFA-2 SCORE CAO:**
            
            - Bệnh nhân có suy đa cơ quan NẶNG
            - Nguy cơ tử vong CAO (>38%)
            - Cần hồi sức tích cực
            - Xem xét mức độ chăm sóc và tiên lượng
            - Thảo luận với gia đình về mục tiêu điều trị
            """)
        
        # Management recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến Cáo Xử Trí")
        
        recommendations = []
        
        if result['subscores'].get('respiratory', 0) >= 3:
            recommendations.append("""
            **Hô hấp (SOFA-2 ≥3):**
            - Xem xét nâng cấp hỗ trợ hô hấp
            - HFNC → NIV → MV → ECMO
            - ARDSNet protocol nếu ARDS
            - Lung protective ventilation
            """)
        
        if result['subscores'].get('coagulation', 0) >= 2:
            recommendations.append("""
            **Đông máu (Tiểu cầu <120):**
            - Tìm nguyên nhân (DIC, sepsis, thuốc, HIT)
            - Xem xét truyền tiểu cầu nếu chảy máu hoặc thủ thuật
            - Tránh thuốc ảnh hưởng tiểu cầu
            """)
        
        if result['subscores'].get('liver', 0) >= 2:
            recommendations.append("""
            **Gan (Bilirubin >2):**
            - Đánh giá chức năng gan (ALT, AST, PT/INR)
            - Loại trừ viêm gan, tắc mật
            - Điều chỉnh liều thuốc
            """)
        
        if result['subscores'].get('cardiovascular', 0) >= 2:
            recommendations.append("""
            **Tim mạch (MAP thấp/cần vasopressor):**
            - Hồi sức dịch nếu hypovolemia
            - Vasopressor: Norepinephrine first-line
            - Mục tiêu MAP ≥65 mmHg
            - Echo đánh giá chức năng tim
            - Xem xét inotrope nếu cardiac dysfunction
            """)
        
        if result['subscores'].get('cns', 0) >= 2:
            recommendations.append("""
            **Thần kinh (GCS <13):**
            - Bảo vệ đường thở
            - CT đầu nếu cần
            - Loại trừ nguyên nhân: infection, metabolic, structural
            - Sedation scoring nếu đang an thần
            """)
        
        if result['subscores'].get('renal', 0) >= 2:
            recommendations.append("""
            **Thận (Cr >2, UO <500, hoặc RRT):**
            - Đánh giá theo KDIGO AKI criteria
            - Tìm nguyên nhân: pre-renal/intrinsic/post-renal
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
        st.session_state['sofa2_result'] = result
        
        # Warning
        st.warning("""
        ⚠️ **Lưu Ý Y Khoa:**
        - SOFA-2 là công cụ đánh giá, không phải chẩn đoán
        - Cần kết hợp với lâm sàng và xét nghiệm khác
        - SOFA-2 có độ chính xác cao hơn SOFA gốc nhờ big data 2025
        - Quyết định điều trị cuối cùng thuộc về bác sĩ điều trị
        """)
    
    # Comparison with original SOFA
    with st.expander("🔍 So Sánh SOFA-2 vs SOFA Gốc"):
        st.markdown("""
        ### Điểm Khác Biệt Chính
        
        | Tính Năng | SOFA Gốc (1996) | SOFA-2 (2025) |
        |-----------|----------------|---------------|
        | **Ngưỡng** | Dựa trên dữ liệu cũ | Điều chỉnh từ big data 2025 |
        | **Hỗ trợ hô hấp** | Chỉ MV | HFNC, NIV, MV, ECMO |
        | **Vasopressor** | Dopamine, Dobu, Epi/Norepi | Thêm Vasopressin, Phenylephrine |
        | **RRT** | Không tích hợp | Có tích hợp RRT |
        | **Độ chính xác** | Dựa trên dữ liệu 1990s | Cải thiện từ big data 2025 |
        | **Tiên đoán tử vong** | Tổng quát | Chính xác hơn |
        
        ### Khi Nào Dùng SOFA-2?
        
        - ✅ Bệnh nhân có hỗ trợ hô hấp hiện đại (HFNC, ECMO)
        - ✅ Bệnh nhân dùng vasopressor mới (Vasopressin, Phenylephrine)
        - ✅ Bệnh nhân đang lọc máu (RRT)
        - ✅ Cần độ chính xác cao hơn trong tiên đoán
        
        ### Khi Nào Dùng SOFA Gốc?
        
        - ✅ So sánh với dữ liệu lịch sử
        - ✅ Nghiên cứu yêu cầu SOFA gốc
        - ✅ Thiếu dữ liệu về hỗ trợ hiện đại
        """)



