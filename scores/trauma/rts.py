"""
Revised Trauma Score (RTS)
===========================

Physiological scoring system for triage and outcome prediction in trauma patients

Reference:
- Champion HR, et al. A revision of the Trauma Score. J Trauma. 1989;29(5):623-629.
- Champion HR, et al. The Major Trauma Outcome Study: establishing national norms for
  trauma care. J Trauma. 1990;30(11):1356-1365.

RTS Formula:
RTS = 0.9368 × GCS + 0.7326 × SBP + 0.2908 × RR

Components (coded values):
- Thang điểm hôn mê Glasgow (GCS): 3-15
- Huyết áp tâm thu (SBP): mmHg
- Nhịp thở (RR): breaths/min

Interpretation:
- RTS ranges from 0 (worst) to 7.84 (best)
- Higher score = better prognosis
- Used for triage and TRISS (Trauma and Injury Severity Score)

Clinical Utility:
- Field triage
- Outcome prediction
- Quality improvement
- Combined with ISS for TRISS
"""

import streamlit as st
from scores.utils.validation import (
    validate_gcs,
    validate_blood_pressure,
    validate_respiratory_rate
)
from components.ui.scoring import render_score_result, render_score_breakdown
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions


def code_gcs(gcs: int) -> int:
    """Convert GCS to coded value"""
    if gcs >= 13:
        return 4
    elif gcs >= 9:
        return 3
    elif gcs >= 6:
        return 2
    elif gcs >= 4:
        return 1
    else:
        return 0


def code_sbp(sbp: float) -> int:
    """Convert SBP to coded value"""
    if sbp >= 90:
        return 4
    elif sbp >= 76:
        return 3
    elif sbp >= 50:
        return 2
    elif sbp >= 1:
        return 1
    else:
        return 0


def code_rr(rr: float) -> int:
    """Convert RR to coded value"""
    if 10 <= rr <= 29:
        return 4
    elif rr >= 30:
        return 3
    elif rr >= 6:
        return 2
    elif rr >= 1:
        return 1
    else:
        return 0


def calculate_rts(gcs: int, sbp: float, rr: float) -> dict:
    """
    Calculate Revised Trauma Score
    
    Args:
        gcs: Thang điểm hôn mê Glasgow (3-15)
        sbp: Huyết áp tâm thu (mmHg)
        rr: Nhịp thở (lần/phút)
    
    Returns:
        Dictionary containing RTS, coded values, survival probability, and recommendations
    """
    
    # Code the values
    gcs_coded = code_gcs(gcs)
    sbp_coded = code_sbp(sbp)
    rr_coded = code_rr(rr)
    
    # Calculate RTS
    rts = 0.9368 * gcs_coded + 0.7326 * sbp_coded + 0.2908 * rr_coded
    
    # Estimate survival probability (simplified approximation)
    # Based on historical data from Champion et al.
    if rts >= 7.0:
        survival_prob = ">95%"
        risk_class = "LOW"
        color = "🟢"
        interpretation = "Tỷ lệ sống sót CAO"
    elif rts >= 5.0:
        survival_prob = "70-95%"
        risk_class = "MODERATE"
        color = "🟡"
        interpretation = "Tỷ lệ sống sót TRUNG BÌNH"
    elif rts >= 3.0:
        survival_prob = "30-70%"
        risk_class = "HIGH"
        color = "🟠"
        interpretation = "Tỷ lệ sống sót THẤP"
    else:
        survival_prob = "<30%"
        risk_class = "CRITICAL"
        color = "🔴"
        interpretation = "Tỷ lệ sống sót RẤT THẤP"
    
    # Triage and management recommendations
    if risk_class == "LOW":
        triage = "**Ưu tiên:** Không khẩn cấp hoặc vừa phải"
        management = """
        **Xử trí**
        - Đánh giá toàn diện tổn thương
        - Xử trí các chấn thương cụ thể
        - Theo dõi tiêu chuẩn
        - Tái đánh giá định kỳ
        """
    elif risk_class == "MODERATE":
        triage = "**Ưu tiên:** Khẩn cấp - Cần can thiệp sớm"
        management = """
        **Xử trí**
        - Stabilization ngay lập tức
        - Đánh giá nhanh ABC
        - Hồi sức tích cực
        - Xem xét chuyển trauma center
        - Chuẩn bị phẫu thuật nếu cần
        - Theo dõi sát
        """
    else:  # HIGH or CRITICAL
        triage = "**Ưu tiên:** CẤP CỨU - Can thiệp ngay lập tức"
        management = """
        **Xử trí**
        - **RESUSCITATION NGAY:**
          * Airway: Intubation nếu GCS ≤8
          * Breathing: O2, mechanical ventilation nếu cần
          * Circulation: IV access × 2, fluid resuscitation, blood products
        
        - **Kiểm soát chảy máu:**
          * Direct pressure, tourniquet nếu chảy máu ngoại vi
          * Pelvic binder nếu nghi chấn thương khung chậu
          * FAST exam → phẫu thuật cấp cứu nếu nội xuất huyết
        
        - **Neuroprotection (nếu GCS thấp):**
          * Elevate head 30°
          * Tránh hạ glucose, hạ nhiệt độ
          * CT đầu STAT
        
        - **Chuyển viện:**
          * Trauma center level I/II ngay lập tức
          * Thông báo trước (pre-notification)
        
        - **Massive transfusion protocol:**
          * Activate nếu shock + chảy máu nặng
          * Blood products 1:1:1 (RBC:FFP:Platelets)
        """
    
    return {
        'rts': rts,
        'gcs_coded': gcs_coded,
        'sbp_coded': sbp_coded,
        'rr_coded': rr_coded,
        'survival_prob': survival_prob,
        'risk_class': risk_class,
        'color': color,
        'interpretation': interpretation,
        'triage': triage,
        'management': management
    }


def render():
    """Render RTS calculator in Streamlit"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'rts':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.title("🦴 Revised Trauma Score (RTS)")
    st.markdown("**Đánh giá sinh lý và tiên lượng bệnh nhân chấn thương**")
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Revised Trauma Score (RTS)** là thang điểm:
        - Đánh giá nhanh sinh lý bệnh nhân chấn thương
        - Dự đoán tỷ lệ sống sót
        - Hỗ trợ quyết định triage
        - Đánh giá chất lượng chăm sóc chấn thương
        
        ### 🎯 Thành phần
        
        **3 Thông số Sinh Lý:**
        1. **GCS (Thang điểm hôn mê Glasgow - Thang điểm hôn mê Glasgow):** Mức độ ý thức
        2. **SBP (Huyết áp tâm thu):** Huyết áp tâm thu
        3. **RR (Nhịp thở):** Tần số thở
        
        **Công thức:**
        ```
        RTS = 0.9368 × (GCS coded) + 0.7326 × (SBP coded) + 0.2908 × (RR coded)
        ```
        
        ### 📊 Bảng Mã Hóa (Coding)
        
        #### GCS Coding
        | GCS | Coded Value |
        |-----|-------------|
        | 13-15 | 4 |
        | 9-12 | 3 |
        | 6-8 | 2 |
        | 4-5 | 1 |
        | 3 | 0 |
        
        #### SBP Coding
        | SBP (mmHg) | Coded Value |
        |------------|-------------|
        | ≥90 | 4 |
        | 76-89 | 3 |
        | 50-75 | 2 |
        | 1-49 | 1 |
        | 0 (no pulse) | 0 |
        
        #### RR Coding
        | RR (breaths/min) | Coded Value |
        |------------------|-------------|
        | 10-29 | 4 |
        | ≥30 | 3 |
        | 6-9 | 2 |
        | 1-5 | 1 |
        | 0 (apnea) | 0 |
        
        ### 📈 Phân tầng Nguy cơ
        
        | RTS | Tỷ Lệ Sống Sót | Ưu tiên |
        |-----|----------------|---------|
        | ≥7 | >95% | Không khẩn cấp |
        | 5-6.99 | 70-95% | Khẩn cấp |
        | 3-4.99 | 30-70% | Cấp cứu ngay |
        | <3 | <30% | Hồi sức cấp cứu |
        
        ### 📚 Tài liệu tham khảo
        
        - Champion HR, et al. *J Trauma* 1989;29:623-629
        - Champion HR, et al. *J Trauma* 1990;30:1356-1365
        """)
    
    st.divider()
    
    # Input section
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Nhập sinh hiệu")
        
        col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🧠 Thang điểm hôn mê Glasgow (GCS) - Thang điểm hôn mê Glasgow")
        gcs = st.number_input(
            "**GCS**",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            help="Thang điểm ý thức từ 3 (tệ nhất) đến 15 (tốt nhất)"
        )
        st.caption("3 (tệ nhất) → 15 (bình thường)")
    
    with col2:
        st.markdown("#### 🫀 Huyết áp tâm thu")
        sbp = st.number_input(
            "**SBP (mmHg)**",
            min_value=0.0,
            max_value=300.0,
            value=120.0,
            step=1.0,
            help="Huyết áp tâm thu"
        )
        st.caption("Huyết áp tâm thu")
    
    with col3:
        st.markdown("#### 🫁 Tần số thở")
        rr = st.number_input(
            "**RR (breaths/min)**",
            min_value=0.0,
            max_value=60.0,
            value=16.0,
            step=1.0,
            help="Số lần thở mỗi phút"
        )
        st.caption("Số lần thở/phút")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="rts",
            calculator_name="RTS",
            category="Chấn Thương",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính RTS & Tiên lượng", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_gcs, gcs_error = validate_gcs(gcs)
        if not is_valid_gcs:
            validation_errors.append(gcs_error)
        
        is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
        if not is_valid_sbp:
            validation_errors.append(sbp_error)
        
        is_valid_rr, rr_error = validate_respiratory_rate(rr)
        if not is_valid_rr:
            validation_errors.append(rr_error)
        
        if validation_errors:
            st.error("**⚠️ Lỗi validation:**")
            for error in validation_errors:
                st.error(f"- {error}")
            st.stop()
        
        result = calculate_rts(gcs=gcs, sbp=sbp, rr=rr)
        
        # Display results
        st.markdown("## 📊 Kết quả")
        
        # Map color emoji to hex
        color_map_hex = {
            "🟢": "#28a745",
            "🟡": "#ffc107",
            "🟠": "#fd7e14",
            "🔴": "#dc3545"
        }
        score_color = color_map_hex.get(result['color'], "#6c757d")
        
        # Use render_score_result for main score display
        render_score_result(
            title="Revised Trauma Score (RTS)",
            score=round(result['rts'], 2),
            interpretation=result['interpretation'],
            mortality=f"Tỷ lệ sống sót: {result['survival_prob']}",
            color=score_color,
            icon=result['color'],
            size="large"
        )
        
        # Use render_score_breakdown for component scores
        render_score_breakdown(
            title="Điểm Từng Thành Phần",
            subscores={
                "🧠 GCS": result['gcs_coded'],
                "🫀 SBP": result['sbp_coded'],
                "🫁 RR": result['rr_coded']
            },
            total_score=round(result['rts'], 2)
        )
        
        # Coded values
        with st.expander("📋 Giá trị mã hóa & tính toán", expanded=True):
            st.markdown(f"""
            **Giá trị Đầu Vào:**
            - GCS: {gcs} → Coded: {result['gcs_coded']}
            - SBP: {sbp:.0f} mmHg → Coded: {result['sbp_coded']}
            - RR: {rr:.0f} breaths/min → Coded: {result['rr_coded']}
            
            **Công thức:**
            ```
            RTS = 0.9368 × {result['gcs_coded']} + 0.7326 × {result['sbp_coded']} + 0.2908 × {result['rr_coded']}
            RTS = {0.9368 * result['gcs_coded']:.3f} + {0.7326 * result['sbp_coded']:.3f} + {0.2908 * result['rr_coded']:.3f}
            RTS = {result['rts']:.2f}
            ```
            """)
        
        # Triage
        st.markdown("---")
        st.markdown("### 🚨 Triage & Ưu tiên")
        st.markdown(result['triage'])
        
        # Management
        st.markdown("---")
        st.markdown("### 💊 Xử trí khuyến cáo")
        st.markdown(result['management'])
        
        # Additional info
        st.info("""
        **📌 Lưu ý:**
        
        - **RTS** là công cụ triage và tiên lượng, KHÔNG thay thế đánh giá lâm sàng toàn diện
        - Nên kết hợp với **ISS (Injury Severity Score)** để có TRISS score
        - **TRISS** = RTS + ISS + Age → tiên lượng chính xác hơn
        - RTS có thể thay đổi nhanh → tái đánh giá thường xuyên
        """)
        
        if result['risk_class'] in ['HIGH', 'CRITICAL']:
            st.error("""
            **🚨 BÁO ĐỘNG NGUY KỊCH:**
            
            - Bệnh nhân ở trạng thái NGUY HIỂM đến tính mạng
            - Cần hồi sức và can thiệp CẤP CỨU NGAY LẬP TỨC
            - Xem xét chuyển Trauma Center Level I/II
            - Activate Trauma Team và Massive Transfusion Protocol
            - Golden Hour: Can thiệp sớm = cứu sống
            """)
        
        # Save to session state
        st.session_state['rts_result'] = result
        
        # Prepare data for history and share
        inputs_dict = {
            "GCS": gcs,
            "SBP": sbp,
            "RR": rr
        }
        
        results_dict = {
            "RTS": round(result['rts'], 2),
            "Tỷ lệ sống sót": result['survival_prob'],
            "Mức độ nguy cơ": result['risk_class'],
            "Đánh giá": result['interpretation']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="rts",
            calculator_name="RTS",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="rts",
            calculator_name="RTS",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="rts",
            calculator_name="RTS",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        from components.calculation_history import render_history_ui
        render_history_ui(calculator_id="rts", show_actions=True)
        
        # Warning
        st.warning("""
        ⚠️ **Lưu ý y khoa:**
        - RTS là công cụ hỗ trợ, không thay thế đánh giá lâm sàng
        - Quyết định điều trị và triage cuối cùng thuộc về bác sĩ điều trị
        - Ưu tiên ABC (Airway, Breathing, Circulation) luôn luôn là trên hết
        """)
    
    # Quick reference
    with st.expander("📖 TRISS - Trauma and Injury Severity Score"):
        st.markdown("""
        ### TRISS Score - Tiên lượng chính xác hơn
        
        **TRISS kết hợp:**
        1. **RTS** (Revised Trauma Score) - sinh lý
        2. **ISS** (Injury Severity Score) - giải phẫu
        3. **Age** - tuổi
        4. **Mechanism** - cơ chế chấn thương (blunt vs penetrating)
        
        **Công thức TRISS:**
        ```
        Survival Probability = 1 / (1 + e^(-b))
        
        b = b0 + b1×RTS + b2×ISS + b3×Age
        ```
        
        **Hệ Số (cho blunt trauma):**
        - b0 = -0.4499
        - b1 = 0.8085 (RTS)
        - b2 = -0.0835 (ISS)
        - b3 = -1.7430 (Age: 0 nếu <55, 1 nếu ≥55)
        
        **Ưu Điểm:**
        - Chính xác hơn RTS hoặc ISS đơn lẻ
        - Sử dụng rộng rãi cho quality improvement
        - Benchmark cho trauma care
        
        **Sử dụng:**
        - Cần cả RTS và ISS
        - ISS calculator có sẵn trong cùng module này
        - Kết hợp cả hai để có TRISS
        """)
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("RTS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )

