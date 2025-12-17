"""
MELD-Na (Model for End-Stage Liver Disease with Sodium)
Tiên lượng bệnh gan giai đoạn cuối với điều chỉnh theo Na
"""

import streamlit as st
import math
from scores.utils.validation import (
    validate_lab_value,
    validate_range
)
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def calculate_meld_na(creatinine, bilirubin, inr, sodium, dialysis_twice=False):
    """
    Calculate MELD-Na score
    
    Args:
        creatinine: Serum creatinine (mg/dL or µmol/L based on user selection)
        bilirubin: Total bilirubin (mg/dL or µmol/L based on user selection)
        inr: INR
        sodium: Serum sodium (mEq/L or mmol/L)
        dialysis_twice: Received dialysis ≥2 times in past week
    
    Returns:
        dict: MELD-Na score and interpretation
    """
    # Apply constraints
    creatinine = max(1.0, min(creatinine, 4.0))
    bilirubin = max(1.0, bilirubin)
    inr = max(1.0, inr)
    sodium = max(125, min(sodium, 137))  # Cap between 125-137
    
    # If dialysis twice in past week, creatinine = 4.0
    if dialysis_twice:
        creatinine = 4.0
    
    # Calculate original MELD score
    meld = (
        9.57 * math.log(creatinine) +
        3.78 * math.log(bilirubin) +
        11.2 * math.log(inr) +
        6.43
    )
    
    # Round to nearest integer
    meld = round(meld)
    
    # Apply floor and ceiling
    meld = max(6, min(meld, 40))
    
    # Calculate MELD-Na
    # If MELD ≥ 12, adjust for sodium
    if meld >= 12:
        meld_na = meld + 1.32 * (137 - sodium) - (0.033 * meld * (137 - sodium))
        meld_na = round(meld_na)
        meld_na = max(meld, min(meld_na, 40))  # MELD-Na should be ≥ MELD and ≤ 40
    else:
        meld_na = meld
    
    return {
        "meld": meld,
        "meld_na": meld_na,
        "creatinine_used": creatinine,
        "bilirubin_used": bilirubin,
        "inr_used": inr,
        "sodium_used": sodium,
        "dialysis_applied": dialysis_twice
    }


def interpret_meld_na(meld_na_score):
    """
    Interpret MELD-Na score
    
    Returns mortality risk and transplant priority
    """
    if meld_na_score < 10:
        return {
            "severity": "Rất thấp",
            "color": "🟢",
            "mortality_3mo": "< 2%",
            "mortality_1yr": "< 10%",
            "transplant_priority": "Rất thấp - Thường không list transplant",
            "management": "Điều trị nội khoa. Theo dõi định kỳ.",
            "level": "minimal"
        }
    elif meld_na_score < 15:
        return {
            "severity": "Thấp",
            "color": "🟡",
            "mortality_3mo": "2-6%",
            "mortality_1yr": "10-20%",
            "transplant_priority": "Thấp - Cân nhắc list transplant",
            "management": "Điều trị tối ưu biến chứng. Đánh giá transplant nếu tiến triển.",
            "level": "low"
        }
    elif meld_na_score < 20:
        return {
            "severity": "Trung bình",
            "color": "🟠",
            "mortality_3mo": "6-20%",
            "mortality_1yr": "20-50%",
            "transplant_priority": "Trung bình - NÊN list transplant",
            "management": "Đánh giá transplant gan. Điều trị tích cực biến chứng.",
            "level": "moderate"
        }
    elif meld_na_score < 30:
        return {
            "severity": "Cao",
            "color": "🔴",
            "mortality_3mo": "20-50%",
            "mortality_1yr": "> 50%",
            "transplant_priority": "Cao - Ưu tiên transplant",
            "management": "Transplant gan GẤP. Điều trị tích cực, theo dõi sát.",
            "level": "high"
        }
    else:  # ≥ 30
        return {
            "severity": "Rất cao",
            "color": "🔴",
            "mortality_3mo": "> 50%",
            "mortality_1yr": "> 70%",
            "transplant_priority": "Rất cao - CẦN transplant KHẨN CẤP",
            "management": "Transplant gan KHẨN CẤP. Hỗ trợ tích cực ICU. Xem xét MARS/ECLS.",
            "level": "critical"
        }


def render():
    """Render the MELD-Na calculator"""
    
    st.title("🏥 MELD-Na Score")
    st.markdown("""
    ### Model for End-Stage Liver Disease with Sodium
    
    **MELD-Na:**
    - Phiên bản cải tiến của MELD score
    - Bổ sung yếu tố **Sodium** để dự đoán chính xác hơn
    - Tiên lượng tử vong trong bệnh gan giai đoạn cuối
    - Ưu tiên phân bổ gan transplant (từ 2016)
    
    **Thành phần:**
    - Creatinine (mg/dL)
    - Bilirubin (mg/dL)
    - INR
    - **Sodium (mEq/L)** - Yếu tố mới
    - Dialysis trong tuần qua
    
    **Điểm số:**
    - Từ 6-40
    - Càng cao → Càng nặng
    - ≥ 15: Nên list transplant
    - ≥ 30: Cần transplant khẩn cấp
    
    **Ưu điểm MELD-Na so với MELD:**
    - Dự đoán chính xác hơn (đặc biệt với hyponatremia)
    - Giảm "gaming" (cheat) MELD score
    - Cải thiện công bằng trong phân bổ gan
    - Standard for UNOS từ 2016
    """)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'meld_na':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("---")
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="meld_na",
            calculator_name="MELD-Na Score",
            category="Tiêu Hóa",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông số")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Creatinine
        st.markdown("### Creatinine")
        cre_unit = st.radio(
            "Đơn vị Creatinine:",
            options=["µmol/L", "mg/dL"],
            index=0,
            horizontal=True,
            key="meldna_cre_unit"
        )
        
        if cre_unit == "µmol/L":
            cre_input = st.number_input(
                "Creatinine (µmol/L):",
                min_value=0.0,
                max_value=1000.0,
                value=88.0,
                step=1.0,
                format="%d",
                help="Giá trị bình thường: 60-110 µmol/L"
            )
            creatinine = round(cre_input / 88.4, 2)  # Convert to mg/dL
            st.caption(f"≈ {_format_num(creatinine, 1)} mg/dL")
        else:
            creatinine = st.number_input(
                "Creatinine (mg/dL):",
                min_value=0.0,
                max_value=15.0,
                value=1.0,
                step=0.1,
                format="%.1f",
                help="Giá trị bình thường: 0.7-1.3 mg/dL"
            )
            st.caption(f"≈ {round(creatinine * 88.4)} µmol/L")
        
        st.markdown("---")
        
        # Bilirubin
        st.markdown("### Bilirubin")
        bili_unit = st.radio(
            "Đơn vị Bilirubin:",
            options=["µmol/L", "mg/dL"],
            index=0,
            horizontal=True,
            key="meldna_bili_unit"
        )
        
        if bili_unit == "µmol/L":
            bili_input = st.number_input(
                "Total Bilirubin (µmol/L):",
                min_value=0.0,
                max_value=1000.0,
                value=17.0,
                step=1.0,
                help="Giá trị bình thường: 5-21 µmol/L"
            )
            bilirubin = round(bili_input / 17.1, 2)  # Convert to mg/dL
            st.caption(f"≈ {bilirubin} mg/dL")
        else:
            bilirubin = st.number_input(
                "Total Bilirubin (mg/dL):",
                min_value=0.0,
                max_value=60.0,
                value=1.0,
                step=0.1,
                help="Giá trị bình thường: 0.3-1.2 mg/dL"
            )
            st.caption(f"≈ {round(bilirubin * 17.1, 1)} µmol/L")
    
    with col2:
        # INR
        st.markdown("### INR")
        inr = st.number_input(
            "INR:",
            min_value=0.8,
            max_value=10.0,
            value=1.0,
            step=0.1,
            help="International Normalized Ratio"
        )
        
        st.markdown("---")
        
        # Sodium
        st.markdown("### Sodium (Yếu tố MELD-Na)")
        sodium = st.number_input(
            "Sodium (mEq/L hoặc mmol/L):",
            min_value=110.0,
            max_value=160.0,
            value=140.0,
            step=1.0,
            help="Giá trị bình thường: 135-145 mEq/L"
        )
        
        if sodium < 135:
            st.warning(f"⚠️ Hyponatremia ({sodium} mEq/L) - Tăng MELD-Na")
        elif sodium > 145:
            st.info(f"ℹ️ Hypernatremia ({sodium} mEq/L) - Ít gặp trong cirrhosis")
        
        st.markdown("---")
        
        # Dialysis
        st.markdown("### Dialysis")
        dialysis_twice = st.checkbox(
            "Chạy thận nhân tạo ≥ 2 lần trong tuần qua",
            help="Nếu có, Creatinine tự động = 4.0 mg/dL"
        )
        
        if dialysis_twice:
            st.info("ℹ️ Creatinine sẽ được set = 4.0 mg/dL (tối đa)")
    
    st.markdown("---")
    
    # Calculate button
    if st.button("📊 Tính MELD-Na Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Creatinine validation (depends on unit)
        if cre_unit == "µmol/L":
            is_valid_cre, cre_error = validate_lab_value(cre_input, "Creatinine", 0.0, 1000.0)
            if not is_valid_cre:
                validation_errors.append(f"Creatinine (µmol/L): {cre_error}")
        else:
            is_valid_cre, cre_error = validate_lab_value(creatinine, "Creatinine", 0.0, 15.0)
            if not is_valid_cre:
                validation_errors.append(f"Creatinine (mg/dL): {cre_error}")
        
        # Bilirubin validation (depends on unit)
        if bili_unit == "µmol/L":
            is_valid_bili, bili_error = validate_lab_value(bili_input, "Bilirubin", 0.0, 1000.0)
            if not is_valid_bili:
                validation_errors.append(f"Bilirubin (µmol/L): {bili_error}")
        else:
            is_valid_bili, bili_error = validate_lab_value(bilirubin, "Bilirubin", 0.0, 60.0)
            if not is_valid_bili:
                validation_errors.append(f"Bilirubin (mg/dL): {bili_error}")
        
        # INR validation
        is_valid_inr, inr_error = validate_range(inr, 0.8, 10.0, "INR")
        if not is_valid_inr:
            validation_errors.append(f"INR: {inr_error}")
        
        # Sodium validation
        is_valid_na, na_error = validate_range(sodium, 110.0, 160.0, "Sodium")
        if not is_valid_na:
            validation_errors.append(f"Sodium: {na_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        # Calculate
        result = calculate_meld_na(creatinine, bilirubin, inr, sodium, dialysis_twice)
        
        meld = result['meld']
        meld_na = result['meld_na']
        
        # Get interpretation
        interp = interpret_meld_na(meld_na)
        
        st.markdown("---")
        st.subheader("📈 Kết quả")
        
        # Display scores
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "MELD Score",
                meld,
                help="MELD gốc (không có sodium)"
            )
        
        with col2:
            st.metric(
                "MELD-Na Score",
                meld_na,
                delta=f"+{meld_na - meld}" if meld_na > meld else "0",
                help="MELD điều chỉnh theo sodium"
            )
        
        with col3:
            st.metric(
                "Sodium Effect",
                f"{meld_na - meld:+d}",
                help="Điểm cộng thêm do hyponatremia"
            )
        
        st.markdown("---")
        
        # Severity
        if interp['level'] in ["minimal", "low"]:
            st.success(f"{interp['color']} Mức độ nặng: {interp['severity']}")
        elif interp['level'] == "moderate":
            st.warning(f"{interp['color']} Mức độ nặng: {interp['severity']}")
        else:
            st.error(f"{interp['color']} Mức độ nặng: {interp['severity']}")
        
        st.markdown("---")
        
        # Detailed interpretation
        st.subheader("🎯 Phân tích & tiên lượng")
        
        st.info(f"""
        **MELD-Na Score: {meld_na}/40**
        
        **Mức độ nặng:** {interp['severity']}
        
        **Tử vong 3 tháng:** {interp['mortality_3mo']}
        
        **Tử vong 1 năm:** {interp['mortality_1yr']}
        
        **Ưu tiên transplant:** {interp['transplant_priority']}
        
        **Xử trí:** {interp['management']}
        """)
        
        # Values used in calculation
        with st.expander("📋 Thông số Sử dụng Trong Tính toán"):
            st.markdown(f"""
            - **Creatinine:** {result['creatinine_used']} mg/dL
              {' (Set = 4.0 do dialysis)' if result['dialysis_applied'] else ''}
              {' (Capped at 4.0)' if not result['dialysis_applied'] and result['creatinine_used'] == 4.0 else ''}
              {' (Floored at 1.0)' if result['creatinine_used'] == 1.0 and creatinine < 1.0 else ''}
            
            - **Bilirubin:** {result['bilirubin_used']} mg/dL
              {' (Floored at 1.0)' if result['bilirubin_used'] == 1.0 and bilirubin < 1.0 else ''}
            
            - **INR:** {result['inr_used']}
              {' (Floored at 1.0)' if result['inr_used'] == 1.0 and inr < 1.0 else ''}
            
            - **Sodium:** {result['sodium_used']} mEq/L
              {' (Capped at 137)' if result['sodium_used'] == 137 and sodium > 137 else ''}
              {' (Floored at 125)' if result['sodium_used'] == 125 and sodium < 125 else ''}
            
            **Công thức MELD:**
            - MELD = 9.57 × ln(Cr) + 3.78 × ln(Bili) + 11.2 × ln(INR) + 6.43
            - Làm tròn, giới hạn 6-40
            
            **Công thức MELD-Na (nếu MELD ≥ 12):**
            - MELD-Na = MELD + 1.32 × (137 - Na) - 0.033 × MELD × (137 - Na)
            - Giới hạn: MELD-Na ≥ MELD và ≤ 40
            """)
        
        # Recommendations based on score
        st.markdown("---")
        st.subheader("💡 Khuyến nghị")
        
        if meld_na < 10:
            st.success("""
            ### ✅ MELD-Na < 10 - Bệnh gan còn ổn định
            
            **Theo dõi:**
            - Khám định kỳ 3-6 tháng
            - Labs định kỳ (CBC, LFT, PT/INR, Creatinine, Sodium, AFP)
            - Ultrasound bụng 6 tháng
            - Endoscopy sàng lọc varices
            
            **Điều trị:**
            - Điều trị nguyên nhân (HCV, HBV, alcohol, NASH)
            - Vaccinations (HAV, HBV, influenza, pneumococcal)
            - Tránh hepatotoxic drugs
            - Chế độ ăn phù hợp
            
            **Transplant:**
            - Chưa cần list transplant
            - Tái đánh giá nếu tiến triển
            """)
        
        elif meld_na < 15:
            st.info("""
            ### 📋 MELD-Na 10-14 - Bệnh gan Nặng Dần
            
            **Theo dõi:**
            - Khám định kỳ 2-3 tháng
            - Labs thường xuyên hơn
            - Đánh giá biến chứng (ascites, encephalopathy, varices)
            
            **Điều trị:**
            - Tối ưu điều trị nguyên nhân
            - Điều trị biến chứng tích cực
            - Diuretics cho ascites
            - Lactulose/Rifaximin cho encephalopathy
            - Beta-blockers cho varices
            
            **Transplant:**
            - Cân nhắc evaluation cho transplant
            - Đặc biệt nếu có HCC hoặc biến chứng nặng
            - Xem xét list nếu tiến triển
            """)
        
        elif meld_na < 20:
            st.warning("""
            ### ⚠️ MELD-Na 15-19 - NÊN Transplant
            
            **Theo dõi:**
            - Khám hàng tháng hoặc thường xuyên hơn
            - Labs định kỳ chặt chẽ
            - Monitor biến chứng sát
            
            **Điều trị:**
            - Điều trị tích cực mọi biến chứng
            - Paracentesis cho tense ascites
            - Lactulose liều cao cho encephalopathy
            - SBP prophylaxis (nếu albumin < 1.5 hoặc hx SBP)
            - Xem xét TIPS nếu refractory ascites
            
            **Transplant:**
            - **NÊN LIST TRANSPLANT**
            - Evaluation đầy đủ tại transplant center
            - Chuẩn bị donor tìm kiếm
            - Cải thiện nutritional status
            - Screen & treat contraindications
            """)
        
        else:  # ≥ 20
            st.error("""
            ### 🚨 MELD-Na ≥ 20 - TRANSPLANT KHẨN CẤP
            
            **Theo dõi:**
            - Theo dõi chặt chẽ (có thể nội trú)
            - Labs rất thường xuyên
            - Monitor vitals, mental status
            
            **Điều trị:**
            - ICU care nếu cần
            - Điều trị tích cực biến chứng
            - TIPS cho refractory ascites/bleeding
            - Consider MARS (nếu có)
            - Xem xét ECLS support
            
            **Transplant:**
            - **LIST TRANSPLANT NGAY LẬP TỨC**
            - Ưu tiên cao trong danh sách
            - MELD ≥ 30: Status 1 consideration
            - Xem xét living donor nếu có
            - Transfer về transplant center
            
            **Tiên lượng:**
            - Tử vong rất cao nếu không transplant
            - Cần can thiệp sớm
            """)
        
        # Special considerations
        st.markdown("---")
        with st.expander("⚠️ Lưu ý đặc biệt"):
            st.markdown(f"""
            ### Các yếu tố ảnh hưởng MELD-Na:
            
            **Hyponatremia ({result['sodium_used']} mEq/L):**
            - Gia tăng MELD-Na score
            - Marker của volume overload, poor prognosis
            - Cần fluid restriction
            - Tránh thiazides (gây thêm hypoNa)
            - Xem xét vaptans (hiếm dùng)
            
            **Dialysis:**
            - Creatinine = 4.0 tự động
            - MELD-Na thường rất cao
            - Hepatorenal syndrome?
            - Xem xét transplant khẩn
            
            **HCC (Hepatocellular Carcinoma):**
            - Nếu có HCC trong Milan criteria → Exception points
            - MELD-Na có thể được tăng lên
            - Staging: AFP, CT/MRI
            - Bridging therapy (TACE, RFA)
            
            **MELD-Na limitations:**
            - Không phản ánh một số biến chứng (encephalopathy, QOL)
            - Có thể "gaming" (manipulate)
            - Không dự đoán post-transplant outcome
            - Cần kết hợp clinical judgment
            """)
        
        # Prepare inputs and results for Phase 1
        inputs_dict = {
            "Creatinine": f"{creatinine} mg/dL" if cre_unit == "mg/dL" else f"{cre_input} µmol/L",
            "Bilirubin": f"{bilirubin} mg/dL" if bili_unit == "mg/dL" else f"{bili_input} µmol/L",
            "INR": f"{inr}",
            "Sodium": f"{sodium} mEq/L",
            "Dialysis": "Có (≥2 lần/tuần)" if dialysis_twice else "Không"
        }
        
        results_dict = {
            "MELD Score": f"{meld}",
            "MELD-Na Score": f"{meld_na}",
            "Severity": interp['severity'],
            "Mortality 3mo": interp['mortality_3mo'],
            "Mortality 1yr": interp['mortality_1yr'],
            "Transplant Priority": interp['transplant_priority'],
            "Management": interp['management']
        }
        
        # Save to history
        # Export section
        render_export_section(
                title="MELD-Na Score",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="MELD-Na Score"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="meld_na",
            calculator_name="MELD-Na Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="meld_na",
            calculator_name="MELD-Na Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="meld_na", show_actions=True)
        
        # References section
        references = get_references("MELD-Na")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("🆚 MELD vs MELD-Na"):
        st.markdown("""
        ### So sánh MELD và MELD-Na:
        
        | Đặc điểm | MELD | MELD-Na |
        |----------|------|---------|
        | **Năm ra đời** | 2001 | 2016 |
        | **Thành phần** | Cr, Bili, INR | Cr, Bili, INR, **Na** |
        | **Điểm số** | 6-40 | 6-40 |
        | **Độ chính xác** | Tốt | Tốt hơn |
        | **UNOS standard** | 2002-2016 | 2016-nay |
        
        **Tại sao bổ sung Sodium?**
        
        **Hyponatremia = Poor prognosis:**
        - Marker của volume overload, dilutional
        - Liên quan tăng tử vong trước transplant
        - Tăng complications sau transplant
        
        **MELD có hạn chế:**
        - Không tính hyponatremia
        - Một số bệnh nhân MELD thấp nhưng hypoNa nặng → Tử vong cao
        - Gaming MELD (manipulate labs)
        
        **MELD-Na cải thiện:**
        - Dự đoán chính xác hơn ~5%
        - Giảm waitlist mortality
        - Công bằng hơn trong phân bổ
        - Ít gaming hơn
        
        **Khi nào MELD-Na khác MELD nhiều?**
        - Hyponatremia nặng (< 130)
        - MELD ≥ 12 (công thức chỉ áp dụng từ MELD ≥ 12)
        - MELD < 12 → MELD-Na = MELD
        """)
    
    with st.expander("🏥 Liver Transplant Allocation"):
        st.markdown("""
        ### Hệ thống phân bổ gan transplant (UNOS):
        
        **Ưu tiên theo MELD-Na (cao → thấp):**
        
        **Status 1A/1B (Highest):**
        - Acute liver failure
        - Primary graft non-function
        - Hepatic artery thrombosis < 7 days
        - Acute decompensated Wilson disease
        
        **MELD-Na ≥ 35:**
        - Ưu tiên rất cao
        - Thường được transplant trong vài tuần
        
        **MELD-Na 25-34:**
        - Ưu tiên cao
        - Chờ vài tháng
        
        **MELD-Na 15-24:**
        - Ưu tiên trung bình
        - Chờ 6-12 tháng
        
        **MELD-Na < 15:**
        - Ưu tiên thấp
        - Thường không được list (trừ HCC exception)
        - Chờ rất lâu hoặc không được transplant
        
        **Exception points (HCC):**
        - HCC trong Milan criteria
        - Bắt đầu MELD 28
        - Tăng 3 điểm mỗi 3 tháng
        - Cần bridging therapy
        
        **Other exceptions:**
        - Hepatopulmonary syndrome
        - Portopulmonary hypertension
        - Primary oxalosis
        - Familial amyloidosis
        - Polycystic liver disease
        
        **Geographic allocation:**
        - Local → Regional → National
        - Share 35 rule (MELD ≥ 35)
        - 250 nautical miles circle
        """)
    
    with st.expander("🔬 Lab Considerations"):
        st.markdown("""
        ### Các lưu ý về xét nghiệm:
        
        **Creatinine:**
        - Floored at 1.0 (nếu < 1.0)
        - Capped at 4.0 (nếu > 4.0 hoặc dialysis)
        - Dialysis ≥ 2 lần/tuần → Cr = 4.0
        - Underestimate nếu malnutrition (muscle wasting)
        
        **Bilirubin:**
        - Total bilirubin (không phải direct)
        - Floored at 1.0
        - No upper cap
        - Tăng trong: cholestatic disease, hemolysis
        - Giảm trong: chronic liver disease (lost function)
        
        **INR:**
        - Floored at 1.0
        - No upper cap
        - Standardized PT ratio
        - Affected by Vitamin K def, malnutrition
        - Không dùng nếu đang anticoagulation
        
        **Sodium:**
        - Capped at 137 (nếu > 137)
        - Floored at 125 (nếu < 125)
        - Only applies if MELD ≥ 12
        - Dilutional hypoNa (not true deficit)
        - Avoid thiazides, free water
        
        **Timing:**
        - Labs trong 48h
        - Tái tính MELD-Na định kỳ
        - Mỗi lab mới → Re-calculate
        - Update trên transplant list
        """)
    
    # Always show references at the bottom (even before calculation)
    st.markdown("---")
    references = get_references("MELD-Na")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        # Fallback to manual references if Phase 1 references not found
        st.markdown("---")
        st.caption("""
        **Tài liệu tham khảo:**
        - Kamath PS, et al. A model to predict survival in patients with end-stage liver disease. Hepatology. 2001;33(2):464-470
        - Kim WR, et al. Hyponatremia and mortality among patients on the liver-transplant waiting list. NEJM. 2008;359(10):1018-1026
        - Biggins SW, et al. Serum sodium predicts mortality in patients listed for liver transplantation. Hepatology. 2005;41(1):32-39
        - OPTN/UNOS Policy 9: Allocation of Livers and Liver-Intestines. 2016
        """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")


if __name__ == "__main__":
    render()

