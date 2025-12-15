"""
GRACE Score Calculator
"""

import streamlit as st
from scores.utils.validation import (
    validate_age,
    validate_heart_rate,
    validate_blood_pressure,
    validate_lab_value
)
from components.ui.scoring import render_score_result, render_score_breakdown
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def render():
    """GRACE Score Calculator"""
    st.subheader("📊 GRACE Score")
    st.caption("Tiên lượng Tử vong Trong ACS")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'grace':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.info("""
    **GRACE Score** dự đoán tử vong trong bệnh viện và 6 tháng sau ACS (STEMI/NSTEMI).
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông số lâm sàng")
        
        # Age
        age = st.number_input(
            "**Tuổi** (năm)",
            min_value=20,
            max_value=110,
            value=65,
            step=1,
            format="%d",
            key="grace_age"
        )
        
        # Heart rate
        hr = st.number_input(
            "**Nhịp tim** (lần/phút)",
            min_value=30,
            max_value=250,
            value=80,
            step=1,
            format="%d",
            key="grace_hr"
        )
        
        # Systolic BP
        sbp = st.number_input(
            "**Huyết áp tâm thu** (mmHg)",
            min_value=50,
            max_value=250,
            value=120,
            step=1,
            format="%d",
            key="grace_sbp"
        )
        
        # Creatinine
        st.markdown("**Creatinine máu**")
        scr_unit = st.radio(
            "Đơn vị:",
            ["µmol/L", "mg/dL"],
            horizontal=True,
            index=0,
            key="grace_scr_unit"
        )
        
        if scr_unit == "µmol/L":
            scr_umol = st.number_input(
                "Creatinine (µmol/L)",
                min_value=10.0,
                max_value=1500.0,
                value=88.0,
                step=5.0,
                format="%d",
                key="grace_scr_umol"
            )
            scr_mgdl = scr_umol / 88.4
        else:
            scr_mgdl = st.number_input(
                "Creatinine (mg/dL)",
                min_value=0.1,
                max_value=15.0,
                value=1.0,
                step=0.1,
                format="%.1f",
                key="grace_scr_mgdl"
            )
        
        # Killip class
        killip_options = [
            "I - Không suy tim",
            "II - S3 hoặc ran ẩm phổi",
            "III - Phù phổi cấp",
            "IV - Shock tim"
        ]
        killip = st.selectbox(
            "**Killip Class**",
            killip_options,
            key="grace_killip"
        )
        killip_class = killip_options.index(killip) + 1  # Index 0-3 → Class 1-4
        
        # Cardiac arrest
        cardiac_arrest = st.checkbox(
            "**Ngừng tuần hoàn** khi nhập viện",
            key="grace_arrest"
        )
        
        # ST segment deviation
        st_deviation = st.checkbox(
            "**ST chênh** trên ECG",
            help="ST chênh lên hoặc xuống",
            key="grace_st"
        )
        
        # Elevated cardiac enzymes
        enzymes = st.checkbox(
            "**Enzyme tim tăng** (Troponin/CK-MB)",
            key="grace_enzymes"
        )
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="grace",
            calculator_name="GRACE Score",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        if st.button("🧮 Tính GRACE Score", type="primary", key="grace_calc", use_container_width=True):
            # Validate inputs
            validation_errors = []
            
            is_valid_age, age_error = validate_age(age, 20, 110)
            if not is_valid_age:
                validation_errors.append(age_error)
            
            is_valid_hr, hr_error = validate_heart_rate(hr)
            if not is_valid_hr:
                validation_errors.append(hr_error)
            
            is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
            if not is_valid_sbp:
                validation_errors.append(sbp_error)
            
            # Validate creatinine
            if scr_unit == "µmol/L":
                is_valid_scr, scr_error = validate_lab_value(scr_umol, "Creatinine (µmol/L)", 10, 1500)
            else:
                is_valid_scr, scr_error = validate_lab_value(scr_mgdl, "Creatinine (mg/dL)", 0.1, 15)
            if not is_valid_scr:
                validation_errors.append(scr_error)
            
            if validation_errors:
                st.error("**⚠️ Lỗi validation:**")
                for error in validation_errors:
                    st.error(f"- {error}")
                st.stop()
            
            # Calculate points for each variable
            points = 0
            details = []
            
            # Age points
            if age < 30:
                age_pts = 0
            elif age <= 39:
                age_pts = 8
            elif age <= 49:
                age_pts = 25
            elif age <= 59:
                age_pts = 41
            elif age <= 69:
                age_pts = 58
            elif age <= 79:
                age_pts = 75
            elif age <= 89:
                age_pts = 91
            else:
                age_pts = 100
            points += age_pts
            details.append(f"Tuổi {age}: {age_pts} điểm")
            
            # Heart rate points
            if hr < 50:
                hr_pts = 0
            elif hr <= 69:
                hr_pts = 3
            elif hr <= 89:
                hr_pts = 9
            elif hr <= 109:
                hr_pts = 15
            elif hr <= 149:
                hr_pts = 24
            elif hr <= 199:
                hr_pts = 38
            else:
                hr_pts = 46
            points += hr_pts
            details.append(f"Nhịp tim {hr}: {hr_pts} điểm")
            
            # Systolic BP points
            if sbp < 80:
                sbp_pts = 58
            elif sbp <= 99:
                sbp_pts = 53
            elif sbp <= 119:
                sbp_pts = 43
            elif sbp <= 139:
                sbp_pts = 34
            elif sbp <= 159:
                sbp_pts = 24
            elif sbp <= 199:
                sbp_pts = 10
            else:
                sbp_pts = 0
            points += sbp_pts
            details.append(f"HA tâm thu {sbp}: {sbp_pts} điểm")
            
            # Creatinine points
            if scr_mgdl < 0.4:
                scr_pts = 1
            elif scr_mgdl <= 0.79:
                scr_pts = 4
            elif scr_mgdl <= 1.19:
                scr_pts = 7
            elif scr_mgdl <= 1.59:
                scr_pts = 10
            elif scr_mgdl <= 1.99:
                scr_pts = 13
            elif scr_mgdl <= 3.99:
                scr_pts = 21
            else:
                scr_pts = 28
            points += scr_pts
            details.append(f"Creatinine {scr_mgdl:.2f} mg/dL: {scr_pts} điểm")
            
            # Killip class points
            killip_pts = (killip_class - 1) * 15 + (killip_class - 1) * 5 if killip_class > 1 else 0
            if killip_class == 1:
                killip_pts = 0
            elif killip_class == 2:
                killip_pts = 20
            elif killip_class == 3:
                killip_pts = 39
            else:  # Class 4
                killip_pts = 59
            points += killip_pts
            details.append(f"Killip Class {killip_class}: {killip_pts} điểm")
            
            # Cardiac arrest points
            if cardiac_arrest:
                points += 39
                details.append("Ngừng tuần hoàn: 39 điểm")
            
            # ST deviation points
            if st_deviation:
                points += 28
                details.append("ST chênh: 28 điểm")
            
            # Elevated enzymes points
            if enzymes:
                points += 14
                details.append("Enzyme tăng: 14 điểm")
            
            # Risk calculation
            # In-hospital mortality risk
            if points <= 108:
                risk_category = "Nguy cơ THẤP"
                hospital_mort = "<1%"
                six_month_mort = "<3%"
                color = "#28a745"  # green
                icon = "✅"
            elif points <= 140:
                risk_category = "Nguy cơ TRUNG BÌNH"
                hospital_mort = "1-3%"
                six_month_mort = "3-8%"
                color = "#fd7e14"  # orange
                icon = "⚠️"
            else:
                risk_category = "Nguy cơ CAO"
                hospital_mort = ">3%"
                six_month_mort = ">8%"
                color = "#dc3545"  # red
                icon = "🚨"
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Use render_score_result for main score display
                render_score_result(
                    title="GRACE Score",
                    score=points,
                    interpretation=risk_category,
                    mortality=f"Tử vong bệnh viện: {hospital_mort}",
                    color=color,
                    icon=icon,
                    size="large"
                )
            
            # Build breakdown of component scores
            component_scores = {}
            for d in details:
                # Parse detail string to extract component name and score
                if "Tuổi" in d:
                    component_scores["Tuổi"] = age_pts
                elif "Nhịp tim" in d:
                    component_scores["Nhịp tim"] = hr_pts
                elif "HA tâm thu" in d:
                    component_scores["Huyết áp tâm thu"] = sbp_pts
                elif "Creatinine" in d:
                    component_scores["Creatinine"] = scr_pts
                elif "Killip" in d:
                    component_scores["Killip Class"] = killip_pts
                elif "Ngừng tuần hoàn" in d:
                    component_scores["Ngừng tuần hoàn"] = 39
                elif "ST chênh" in d:
                    component_scores["ST chênh"] = 28
                elif "Enzyme" in d:
                    component_scores["Enzyme tăng"] = 14
            
            if component_scores:
                render_score_breakdown(
                    title="Chi Tiết Điểm Số",
                    subscores=component_scores,
                    total_score=points
                )
            
            st.markdown("---")
            st.markdown("### 💡 Chi tiết điểm")
            for d in details:
                st.write(f"- {d}")
            
            st.markdown("---")
            st.markdown("### 📈 Nguy cơ tử vong")
            
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.metric(
                    label="Tử vong trong viện",
                    value=hospital_mort
                )
            with col_m2:
                st.metric(
                    label="Tử vong 6 tháng",
                    value=six_month_mort
                )
            
            st.markdown("### 💊 Khuyến cáo xử trí")
            
            if risk_category == "thấp":
                st.success(f"""
                **Nguy cơ {risk_category.upper()}**
                
                **Chiến lược:**
                - ✅ Điều trị nội khoa tích cực
                - DAPT (Aspirin + P2Y12 inhibitor)
                - Statin, Beta-blocker, ACE-I
                - Có thể cân nhắc xuất viện sớm nếu ổn định
                - Theo dõi ngoại trú
                - Cân nhắc stress test hoặc CT angiography
                """)
            
            elif risk_category == "trung bình":
                st.warning(f"""
                **Nguy cơ {risk_category.upper()}**
                
                **Chiến lược:**
                - ⚠️ Điều trị tích cực
                - DAPT tối ưu
                - Anticoagulation
                - Cân nhắc chiến lược xâm lấn sớm
                - Coronary angiography trong 24-72h
                - Hội chẩn tim mạch
                - Theo dõi sát tại bệnh viện
                """)
            
            else:
                st.error(f"""
                **Nguy cơ {risk_category.upper()}**
                
                **Chiến lược:**
                - 🚨 Điều trị tích cực tối đa
                - DAPT + Anticoagulation
                - Xử trí biến chứng (suy tim, shock)
                - **Coronary angiography KHẨN CẤP**
                - Chuẩn bị can thiệp/CABG
                - ICU/CCU monitoring
                - Hỗ trợ tuần hoàn nếu cần (IABP, ECMO)
                - Hội chẩn đa chuyên khoa
                """)
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            
            # Prepare inputs for export
            inputs_dict = {
                "Age": f"{age} tuổi",
                "Nhịp tim": f"{hr} /min",
                "Systolic BP": f"{sbp} mmHg",
                "Creatinine": f"{scr_mgdl:.2f} mg/dL",
                "Killip Class": f"{killip_class}",
                "Cardiac Arrest": "Có" if cardiac_arrest else "Không",
                "ST Deviation": "Có" if st_deviation else "Không",
                "Elevated Enzymes": "Có" if enzymes else "Không"
            }
            
            # Prepare results for export
            results_dict = {
                "GRACE Score": f"{points} điểm",
                "Risk Category": risk_category.upper(),
                "Hospital Mortality": hospital_mort,
                "6-Month Mortality": six_month_mort,
                "Details": "\n".join(details)
            }
            
            render_export_section(
                title=f"GRACE = {points} điểm",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="GRACE Score",
                filename="grace_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="grace",
                calculator_name="GRACE Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="grace",
                calculator_name="GRACE Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            from components.calculation_history import render_history_ui
            render_history_ui(calculator_id="grace", show_actions=True)
            
            # References section
            references = get_references("GRACE")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
            else:
                # Fallback to manual references if not in config
                with st.expander("📚 Tài liệu tham khảo"):
                    st.markdown("""
                **GRACE (Global Registry of Acute Coronary Events) Risk Score**
                
                **8 Biến số:**
                1. Age (tuổi)
                2. Heart rate (nhịp tim)
                3. Systolic BP (HA tâm thu)
                4. Creatinine (creatinine máu)
                5. Killip class (phân loại suy tim)
                6. Cardiac arrest at admission (ngừng tuần hoàn)
                7. ST segment deviation (ST chênh)
                8. Elevated cardiac biomarkers (enzyme tim)
                
                **Tổng điểm: 1-372**
                
                **Phân tầng nguy cơ:**
                - **≤108**: Low risk (<1% in-hospital, <3% 6-month mortality)
                - **109-140**: Intermediate risk (1-3% in-hospital, 3-8% 6-month)
                - **>140**: High risk (>3% in-hospital, >8% 6-month mortality)
                
                **Validation:**
                - GRACE Registry (>100,000 patients)
                - Multiple international validations
                
                **Guidelines:**
                - ESC 2020 ACS Guidelines (Class I recommendation)
                - AHA/ACC Guidelines
                
                **References:**
                - Granger CB et al. Arch Intern Med. 2003;163(19):2345-2353.
                - Fox KAA et al. BMJ. 2006;333(7578):1091.
                
                **Link:**
                - https://www.mdcalc.com/grace-acs-risk-mortality-calculator
                """)
    
    # Always show references at the bottom (even before calculation)
    references = get_references("GRACE")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")
