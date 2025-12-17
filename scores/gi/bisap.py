"""
BISAP Score (Bedside Index for Severity in Acute Pancreatitis)
Tiên lượng viêm tụy cấp - đơn giản, nhanh chóng
"""

import streamlit as st
from scores.utils.validation import (
    validate_age,
    validate_lab_value
)
from components.ui.validation import render_validation_errors
from components.ui.scoring import render_score_result, render_score_breakdown
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def render():
    """Render BISAP Score interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🩺 BISAP Score</h2>
    <p style='text-align: center;'><em>Bedside Index for Severity in Acute Pancreatitis</em></p>
    """, unsafe_allow_html=True)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'bisap':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Thông tin về BISAP
    with st.expander("ℹ️ Giới thiệu về BISAP Score"):
        st.markdown("""
        **BISAP Score** là hệ thống đánh giá mức độ nặng và tiên lượng tử vong trong 
        **viêm tụy cấp** dựa trên 5 tiêu chí đơn giản trong **24 giờ đầu**.
        
        **Ưu điểm:**
        - ✅ **RẤT ĐƠN GIẢN** - Chỉ 5 tiêu chí, dễ nhớ (B-I-S-A-P)
        - ✅ **NHANH** - Có thể tính trong vài phút
        - ✅ **SỚM** - Áp dụng trong 24h đầu
        - ✅ **CHÍNH XÁC** - Tương đương Ranson nhưng đơn giản hơn nhiều
        - ✅ **Không cần CT** - Chỉ cần lâm sàng + xét nghiệm cơ bản
        
        **So với Ranson Criteria:**
        - Ranson: 11 tiêu chí, cần 48h
        - BISAP: 5 tiêu chí, chỉ cần 24h
        - BISAP đơn giản hơn nhưng độ chính xác tương đương
        
        **Khi nào dùng:**
        - Tất cả bệnh nhân viêm tụy cấp
        - Đặc biệt hữu ích trong 24h đầu nhập viện
        - Hướng dẫn quyết định chuyển ICU
        
        **5 tiêu chí BISAP (mỗi tiêu chí = 1 điểm):**
        - **B**UN > 25 mg/dL (>8.93 mmol/L)
        - **I**mpaired mental status (Lú lẫn, GCS < 15)
        - **S**IRS (≥2 tiêu chí SIRS)
        - **A**ge > 60 tuổi
        - **P**leural effusion (tràn dịch màng phổi trên X-quang)
        
        **Điểm tối đa:** 5 điểm
        """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="bisap",
            calculator_name="BISAP Score",
            category="Tiêu Hóa",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input form
    st.subheader("📝 Nhập thông tin bệnh nhân")
    
    st.markdown("**Đánh giá 5 tiêu chí BISAP (mỗi tiêu chí = 1 điểm):**")
    
    st.markdown("---")
    
    # 1. BUN
    st.markdown("### 🧪 B - BUN (Blood Urea Nitrogen)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        bun_unit = st.radio(
            "Đơn vị BUN",
            options=["mmol/L", "mg/dL"],
            index=0,
            horizontal=True
        )
        
        if bun_unit == "mmol/L":
            bun_mmol = st.number_input(
                "BUN (mmol/L)",
                min_value=0.0,
                max_value=70.0,
                value=5.4,
                step=0.1,
                format="%.1f",
                help="Bình thường: 2.5-7.1 mmol/L"
            )
            bun = bun_mmol * 2.8
            st.caption(f"💡 = {_format_num(bun, 1)} mg/dL")
        else:
            bun = st.number_input(
                "BUN (mg/dL)",
                min_value=0.0,
                max_value=200.0,
                value=20.0,
                step=1.0,
                format="%.0f",
                help="Bình thường: 7-20 mg/dL"
            )
            bun_mmol = bun / 2.8
            st.caption(f"💡 = {_format_num(bun_mmol, 1)} mmol/L")
    
    with col2:
        bun_positive = bun > 25
        if bun_positive:
            st.error("✅ **BUN > 25**\n\n+1 điểm")
        else:
            st.success("❌ BUN ≤ 25\n\n0 điểm")
    
    st.markdown("---")
    
    # 2. Impaired mental status
    st.markdown("### 🧠 I - Impaired Mental Status (Lú lẫn)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        gcs = st.number_input(
            "Thang điểm hôn mê Glasgow (GCS) - Thang điểm hôn mê Glasgow",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            help="GCS bình thường = 15"
        )
        
        mental_impaired = st.checkbox(
            "Có lú lẫn, định hướng kém, hoặc bất thường ý thức",
            value=(gcs < 15),
            help="Bao gồm: disorientation, lethargy, coma"
        )
    
    with col2:
        if mental_impaired or gcs < 15:
            st.error("✅ **Lú lẫn**\n\n+1 điểm")
        else:
            st.success("❌ Tỉnh táo\n\n0 điểm")
    
    st.markdown("---")
    
    # 3. SIRS
    st.markdown("### 🌡️ S - SIRS (Systemic Inflammatory Response Syndrome)")
    
    st.info("""
    **SIRS dương tính khi có ≥ 2 trong 4 tiêu chí sau:**
    - Nhiệt độ > 38°C hoặc < 36°C
    - Nhịp tim > 90 nhịp/phút
    - Nhịp thở > 20 lần/phút hoặc PaCO₂ < 32 mmHg
    - WBC > 12,000 hoặc < 4,000 hoặc > 10% tế bào non
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        temp = st.number_input(
            "Nhiệt độ (°C)",
            min_value=30.0,
            max_value=42.0,
            value=37.0,
            step=0.1
        )
        temp_abnormal = (temp > 38.0) or (temp < 36.0)
        if temp_abnormal:
            st.caption("✓ Bất thường")
    
    with col2:
        hr = st.number_input(
            "Nhịp tim (bpm)",
            min_value=20,
            max_value=200,
            value=80,
            step=1
        )
        hr_abnormal = hr > 90
        if hr_abnormal:
            st.caption("✓ Nhanh")
    
    with col3:
        rr = st.number_input(
            "Nhịp thở (/phút)",
            min_value=5,
            max_value=60,
            value=16,
            step=1
        )
        rr_abnormal = rr > 20
        if rr_abnormal:
            st.caption("✓ Nhanh")
    
    with col4:
        wbc = st.number_input(
            "WBC (×10³/µL)",
            min_value=0.0,
            max_value=50.0,
            value=8.0,
            step=0.5
        )
        wbc_abnormal = (wbc > 12.0) or (wbc < 4.0)
        if wbc_abnormal:
            st.caption("✓ Bất thường")
    
    sirs_count = sum([temp_abnormal, hr_abnormal, rr_abnormal, wbc_abnormal])
    sirs_positive = sirs_count >= 2
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.metric(
            "Số tiêu chí SIRS",
            f"{sirs_count}/4",
            help="Cần ≥2 để SIRS dương tính"
        )
    
    with col2:
        if sirs_positive:
            st.error("✅ **SIRS (+)**\n\n+1 điểm")
        else:
            st.success("❌ SIRS (-)\n\n0 điểm")
    
    st.markdown("---")
    
    # 4. Age
    st.markdown("### 👴 A - Age (Tuổi)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        age = st.number_input(
            "Tuổi",
            min_value=0,
            max_value=120,
            value=50,
            step=1
        )
    
    with col2:
        age_positive = age > 60
        if age_positive:
            st.error("✅ **Tuổi > 60**\n\n+1 điểm")
        else:
            st.success("❌ Tuổi ≤ 60\n\n0 điểm")
    
    st.markdown("---")
    
    # 5. Pleural effusion
    st.markdown("### 🫁 P - Pleural Effusion (Tràn dịch màng phổi)")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        pleural = st.checkbox(
            "Có tràn dịch màng phổi trên X-quang ngực",
            help="Dựa trên X-quang ngực hoặc CT"
        )
    
    with col2:
        if pleural:
            st.error("✅ **Có tràn dịch**\n\n+1 điểm")
        else:
            st.success("❌ Không\n\n0 điểm")
    
    st.markdown("---")
    
    # Calculate button
    if st.button("📊 Tính BISAP Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Validate BUN
        if bun_unit == "mmol/L":
            is_valid_bun, bun_error = validate_lab_value(bun_mmol, "BUN (mmol/L)", 0.0, 70.0)
        else:
            is_valid_bun, bun_error = validate_lab_value(bun, "BUN (mg/dL)", 0.0, 200.0)
        if not is_valid_bun:
            validation_errors.append(bun_error)
        
        # Validate GCS
        from scores.utils.validation import validate_gcs
        is_valid_gcs, gcs_error = validate_gcs(gcs)
        if not is_valid_gcs:
            validation_errors.append(gcs_error)
        
        # Validate vital signs
        from scores.utils.validation import validate_temperature, validate_heart_rate, validate_respiratory_rate
        is_valid_temp, temp_error = validate_temperature(temp, "celsius")
        if not is_valid_temp:
            validation_errors.append(temp_error)
        
        is_valid_hr, hr_error = validate_heart_rate(hr)
        if not is_valid_hr:
            validation_errors.append(hr_error)
        
        is_valid_rr, rr_error = validate_respiratory_rate(rr)
        if not is_valid_rr:
            validation_errors.append(rr_error)
        
        # Validate WBC
        is_valid_wbc, wbc_error = validate_lab_value(wbc, "WBC (×10³/µL)", 0.0, 50.0)
        if not is_valid_wbc:
            validation_errors.append(wbc_error)
        
        # Validate age
        is_valid_age, age_error = validate_age(age, 0, 120)
        if not is_valid_age:
            validation_errors.append(age_error)
        
        if validation_errors:
            render_validation_errors(validation_errors)
        
        # Calculate total score
        bisap_score = sum([
            bun_positive,
            mental_impaired or (gcs < 15),
            sirs_positive,
            age_positive,
            pleural
        ])
        
        # Mortality risk
        mortality_rates = {
            0: "<1%",
            1: "~2%",
            2: "~10-15%",
            3: "~20-25%",
            4: "~40-50%",
            5: ">50%"
        }
        
        mortality = mortality_rates[bisap_score]
        
        # Severity classification
        if bisap_score == 0:
            severity = "Nhẹ"
            color = "#28a745"
            icon = "✅"
        elif bisap_score <= 2:
            severity = "Trung bình"
            color = "#ffc107"
            icon = "⚠️"
        else:
            severity = "Nặng"
            color = "#dc3545"
            icon = "🚨"
        
        # Display results
        st.markdown("## 📊 Kết quả")
        
        # Use render_score_result for main score display
        render_score_result(
            title="BISAP Score",
            score=bisap_score,
            interpretation=f"Viêm tụy cấp {severity}",
            mortality=f"Tử vong: {mortality}",
            color=color,
            icon=icon,
            size="large"
        )
        
        # Build breakdown of component scores
        component_scores = {}
        if bun_positive:
            component_scores["B - BUN >25"] = 1
        if mental_impaired or (gcs < 15):
            component_scores["I - Rối loạn ý thức"] = 1
        if sirs_positive:
            component_scores["S - SIRS ≥2"] = 1
        if age_positive:
            component_scores["A - Tuổi >60"] = 1
        if pleural:
            component_scores["P - Tràn dịch MP"] = 1
        
        if component_scores:
            render_score_breakdown(
                title="Tiêu chí BISAP",
                subscores=component_scores,
                total_score=bisap_score
            )
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết:")
        
        components = []
        if bun_positive:
            components.append("✓ **B**UN > 25 mg/dL")
        if mental_impaired or (gcs < 15):
            components.append("✓ **I**mpaired mental status")
        if sirs_positive:
            components.append("✓ **S**IRS ≥ 2 tiêu chí")
        if age_positive:
            components.append("✓ **A**ge > 60 tuổi")
        if pleural:
            components.append("✓ **P**leural effusion")
        
        if components:
            for comp in components:
                st.markdown(f"- {comp}")
        else:
            st.markdown("- *Không có tiêu chí nào dương tính*")
        
        st.markdown("---")
        
        # Prognosis
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Mức độ nặng",
                severity,
                help="Phân loại dựa trên BISAP score"
            )
        
        with col2:
            st.metric(
                "Tử vong trong viện",
                mortality,
                help="Tỷ lệ tử vong ước tính"
            )
        
        # Clinical management
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo điều trị")
        
        if bisap_score == 0:
            st.success("""
            **BISAP = 0 - Viêm tụy nhẹ**
            
            **Tiên lượng:**
            - ✅ Nguy cơ tử vong RẤT THẤP (<1%)
            - ✅ Ít biến chứng
            - ✅ Hồi phục nhanh
            
            **Quản lý:**
            - 🏥 **Điều trị nội khoa thường quy:**
              - Nhịn ăn cho đến khi đỡ đau
              - Dịch truyền tích cực (250-500 mL/h)
              - Giảm đau (tránh morphine)
              - Kiểm soát nôn
            
            - 🍽️ **Dinh dưỡng:**
              - Bắt đầu ăn sớm khi đỡ đau (24-48h)
              - Bắt đầu từ thức ăn lỏng
            
            - 📊 **Theo dõi:**
              - Dấu hiệu sinh tồn
              - Lượng nước tiểu
              - Tái đánh giá BISAP mỗi ngày
            
            - 🏥 **Nơi điều trị:** Buồng thường
            
            - ⏱️ **Thời gian nằm viện:** 3-5 ngày
            """)
        
        elif bisap_score <= 2:
            st.warning("""
            **BISAP 1-2 - Viêm tụy trung bình**
            
            **Tiên lượng:**
            - ⚠️ Nguy cơ tử vong 2-15%
            - ⚠️ Có thể có biến chứng
            - ⚠️ Cần theo dõi chặt
            
            **Quản lý:**
            - 🏥 **Điều trị tích cực:**
              - Dịch truyền mạnh (250-500 mL/h Lactated Ringer)
              - Monitor huyết động chặt chẽ
              - Giảm đau hiệu quả
              - Xét nghiệm theo dõi: Ca, Mg, glucose, lipase hàng ngày
            
            - 🧪 **Xét nghiệm thêm:**
              - CT bụng có cản quang (nếu chưa làm)
              - Đánh giá hoại tử tụy
              - Theo dõi CRP, procalcitonin
            
            - 🍽️ **Dinh dưỡng:**
              - Ăn sớm qua đường miệng nếu được
              - Cân nhắc nuôi dưỡng qua sonde mũi-hỗng tràng nếu không ăn được
            
            - 🏥 **Nơi điều trị:** 
              - Buồng theo dõi sát (step-down unit)
              - Hoặc ICU nếu cần
            
            - ⏱️ **Thời gian nằm viện:** 5-10 ngày
            
            - 🚨 **Cân nhắc:**
              - Hội chẩn ngoại khoa nếu nghi ngờ hoại tử
              - Chuyển ICU nếu xấu đi
            """)
        
        else:  # bisap_score >= 3
            st.error("""
            **BISAP ≥ 3 - Viêm tụy nặng**
            
            **Tiên lượng:**
            - 🚨 Nguy cơ tử vong CAO (20-50%+)
            - 🚨 Nguy cơ cao biến chứng nghiêm trọng
            - 🚨 Có thể cần phẫu thuật
            
            **Quản lý:**
            - 🏥 **CHUYỂN ICU NGAY:**
              - Monitor xâm nhập (arterial line, CVP)
              - Hô hấp: theo dõi sát, cân nhắc thông khí
              - Huyết động: dịch mạnh, có thể cần vasopressor
            
            - 💧 **Dịch truyền tích cực:**
              - 250-500 mL/h Lactated Ringer
              - Mục tiêu: UOP > 0.5 mL/kg/h
              - Theo dõi quá tải dịch (phù phổi)
            
            - 🧪 **Xét nghiệm & Hình ảnh:**
              - **CT bụng có cản quang** (đánh giá hoại tử)
              - Xét nghiệm hàng ngày: CBC, CMP, Ca, Mg, lipase, CRP
              - Procalcitonin (đánh giá nhiễm khuẩn)
              - Cân nhắc ERCP nếu sỏi mật + cholangitis
            
            - 🍽️ **Dinh dưỡng:**
              - **Nuôi dưỡng qua đường tiêu hóa** (sonde mũi-hỗng tràng)
              - Nếu không dung nạp: TPN (nuôi ăn tĩnh mạch)
              - MỤC TIÊU: 25-35 kcal/kg/ngày
            
            - 💊 **Kháng sinh:**
              - KHÔNG dùng dự phòng thường quy
              - Chỉ dùng nếu có nhiễm khuẩn hoại tử tụy được chứng minh:
                - Imipenem, Meropenem, hoặc
                - Quinolone + Metronidazole
            
            - 🔪 **Can thiệp:**
              - **Hội chẩn ngoại khoa/can thiệp** NGAY
              - Cân nhắc:
                - Necrosectomy (nếu hoại tử nhiễm khuẩn)
                - Drainage (nếu áp xe, dịch tụy)
                - ERCP (nếu sỏi mật + cholangitis)
            
            - 🏥 **Nơi điều trị:** ICU
            
            - ⏱️ **Thời gian nằm viện:** 2-4 tuần hoặc lâu hơn
            
            **Biến chứng thường gặp:**
            - Hoại tử tụy nhiễm khuẩn
            - Giả nang tụy
            - ARDS
            - AKI
            - Sepsis
            - Chảy máu tiêu hóa
            """)
        
        # Comparison with other scores
        with st.expander("📊 So sánh BISAP với các thang điểm khác"):
            st.markdown("""
            | Thang điểm | Số tiêu chí | Thời gian | Độ phức tạp | Độ chính xác |
            |:-----------|:------------|:----------|:------------|:-------------|
            | **BISAP** | 5 | 24h | ⭐ Rất đơn giản | ⭐⭐⭐⭐ Cao |
            | **Ranson** | 11 | 48h | ⭐⭐⭐ Phức tạp | ⭐⭐⭐⭐ Cao |
            | **APACHE II** | ~12 | 24h | ⭐⭐⭐⭐ Rất phức tạp | ⭐⭐⭐⭐⭐ Rất cao |
            | **CT Severity Index** | 2 | Khi có CT | ⭐⭐ Đơn giản | ⭐⭐⭐⭐ Cao |
            
            ---
            
            ### Khi nào dùng thang điểm nào?
            
            **BISAP (Khuyến cáo - ưu tiên #1):**
            - ✅ Dùng cho TẤT CẢ bệnh nhân viêm tụy cấp
            - ✅ Đặc biệt tốt trong 24h đầu
            - ✅ Đơn giản, nhanh, chính xác
            
            **Ranson:**
            - Lịch sử, vẫn dùng rộng rãi
            - Cần 48h → chậm hơn BISAP
            - Phức tạp hơn BISAP
            
            **APACHE II:**
            - Tốt nhất cho bệnh nhân ICU
            - Quá phức tạp cho sử dụng thường quy
            - Tốt cho nghiên cứu
            
            **CT Severity Index:**
            - Cần khi có CT
            - Đánh giá hoại tử tốt
            - Kết hợp với BISAP
            
            ---
            
            ### Khuyến cáo hiện tại:
            
            **American College of Gastroenterology (ACG) Guidelines:**
            - Dùng BISAP hoặc APACHE II để đánh giá mức độ nặng
            - BISAP đơn giản hơn → khuyến cáo dùng BISAP
            """)
        
        # Causes and workup
        with st.expander("🔍 Nguyên nhân và đánh giá nguyên nhân viêm tụy"):
            st.markdown("""
            ### Nguyên nhân viêm tụy cấp (nhớ: I GET SMASHED):
            
            - **I** - Idiopathic (Không rõ nguyên nhân) - ~10-15%
            - **G** - Gallstones (Sỏi mật) - ~40%
            - **E** - Ethanol (Rượu) - ~30%
            - **T** - Trauma (Chấn thương, post-ERCP) - ~5%
            - **S** - Steroids (Corticosteroids)
            - **M** - Mumps/viruses (Virus quai bị, CMV, HIV...)
            - **A** - Autoimmune (Tự miễn)
            - **S** - Scorpion sting/Hyperlipidemia/Hypercalcemia
            - **H** - Hypothermia
            - **E** - ERCP
            - **D** - Drugs (Azathioprine, Thiazides, Valproic acid...)
            
            ---
            
            ### Xét nghiệm đánh giá nguyên nhân:
            
            **Tất cả bệnh nhân:**
            - ✅ **Lipase** hoặc Amylase (>3x bình thường)
            - ✅ **Siêu âm bụng** (tìm sỏi mật)
            - ✅ **ALT, AST** (ALT > 150 gợi ý sỏi)
            - ✅ **Ca, Triglycerides** (nếu không rõ nguyên nhân)
            
            **Nếu nặng hoặc không rõ nguyên nhân:**
            - **CT bụng có cản quang** (sau 48-72h)
            - **IgG4** (nếu nghi ngờ tự miễn)
            - **Genetic testing** (nếu < 35 tuổi, tái phát nhiều)
            
            **Nếu nghi sỏi mật:**
            - **MRCP** hoặc **EUS** (siêu âm nội soi)
            - **ERCP** (nếu có cholangitis hoặc sỏi đã chứng minh)
            """)
        
            # Prepare inputs and results for export/history
            inputs_dict = {
                "BUN": f"{bun:.1f} mg/dL ({bun_mmol:.1f} mmol/L)" if bun_unit == "mmol/L" else f"{bun:.1f} mg/dL",
                "GCS": str(gcs),
                "Mental Impaired": "Có" if (mental_impaired or gcs < 15) else "Không",
                "Temperature": f"{temp:.1f}°C",
                "Heart Rate": f"{hr} bpm",
                "Respiratory Rate": f"{rr} /min",
                "WBC": f"{wbc:.1f} ×10³/µL",
                "SIRS Count": f"{sirs_count}/4",
                "SIRS Positive": "Có" if sirs_positive else "Không",
                "Age": str(age),
                "Pleural Effusion": "Có" if pleural else "Không"
            }
            
            results_dict = {
                "BISAP Score": f"{bisap_score}/5",
                "Severity": severity,
                "Mortality": mortality,
                "Components": ", ".join(components) if components else "Không có"
            }
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"BISAP Score = {bisap_score}/5",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="BISAP Score",
                filename="bisap_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="bisap",
                calculator_name="BISAP Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="bisap",
                calculator_name="BISAP Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="bisap", show_actions=True)
            
            # References section
            references = get_references("BISAP")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
            else:
                # Fallback to manual references
                with st.expander("📚 Tài liệu tham khảo"):
                    st.markdown("""
                    1. **Wu BU, Johannes RS, Sun X, Tabak Y, Conwell DL, Banks PA.** 
                       The early prediction of mortality in acute pancreatitis: a large population-based study. 
                       *Gut.* 2008;57(12):1698-703.
                    
                    2. **Singh VK, Wu BU, Bollen TL, et al.** A prospective evaluation of the bedside index for severity in acute pancreatitis score in assessing mortality and intermediate markers of severity in acute pancreatitis. 
                       *Am J Gastroenterol.* 2009;104(4):966-71.
                    
                    3. **Tenner S, Baillie J, DeWitt J, Vege SS; American College of Gastroenterology.** 
                       American College of Gastroenterology guideline: management of acute pancreatitis. 
                       *Am J Gastroenterol.* 2013;108(9):1400-15.
                    
                    4. **Papachristou GI, Muddana V, Yadav D, et al.** Comparison of BISAP, Ranson's, APACHE-II, and CTSI scores in predicting organ failure, complications, and mortality in acute pancreatitis. 
                       *Am J Gastroenterol.* 2010;105(2):435-41.
                    
                    5. **Boxhoorn L, Voermans RP, Bouwense SA, et al.** Acute pancreatitis. 
                       *Lancet.* 2020;396(10252):726-734.
                    """)
    
    # Always show references at the bottom
    references = get_references("BISAP")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    # Quick reference
    st.markdown("---")
    st.markdown("### 📋 Tóm tắt BISAP:")
    
    st.markdown("""
    | Tiêu chí | Dương tính khi | Điểm |
    |:---------|:---------------|:-----|
    | **B**UN | > 25 mg/dL (>8.93 mmol/L) | 1 |
    | **I**mpaired mental status | GCS < 15 hoặc lú lẫn | 1 |
    | **S**IRS | ≥ 2 tiêu chí SIRS | 1 |
    | **A**ge | > 60 tuổi | 1 |
    | **P**leural effusion | Có trên X-quang | 1 |
    
    **Tổng điểm:** 0-5
    
    **Tiên lượng tử vong:**
    - **0 điểm:** <1% - Nhẹ
    - **1 điểm:** ~2% - Nhẹ-Trung bình
    - **2 điểm:** ~10-15% - Trung bình
    - **3 điểm:** ~20-25% - Nặng
    - **4 điểm:** ~40-50% - Rất nặng
    - **5 điểm:** >50% - Cực nặng
    """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **BISAP ≥ 3** → Viêm tụy nặng → Chuyển ICU
    
    2. **Đánh giá trong 24h đầu** → Sớm hơn Ranson (48h)
    
    3. **Đơn giản** → Dễ nhớ (B-I-S-A-P), dễ tính
    
    4. **Chính xác** → Tương đương Ranson, APACHE II
    
    5. **Tái đánh giá hàng ngày** → BISAP có thể thay đổi
    
    6. **Luôn tìm nguyên nhân** → Sỏi mật, rượu là phổ biến nhất
    """)


if __name__ == "__main__":
    render()

