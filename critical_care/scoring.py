"""
Critical Care Scoring Systems
Tổng hợp các scoring systems quan trọng cho ICU
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert


# Import existing calculators from scores module
try:
    from scores.emergency.apache2 import render as render_apache2
    from scores.emergency.sofa import render as render_sofa
    from scores.emergency.saps2 import render as render_saps2
    from scores.neurology.gcs import render as render_gcs
    from scores.nephrology.kdigo import render as render_kdigo
    from scores.nephrology.rifle import render as render_rifle
except ImportError:
    # Fallback if imports fail
    render_apache2 = None
    render_sofa = None
    render_saps2 = None
    render_gcs = None
    render_kdigo = None
    render_rifle = None


# RASS Scale definitions (from sedation.py)
RASS_SCALE = {
    "+4": "Combative - Overtly combative, violent, immediate danger to staff",
    "+3": "Very Agitated - Pulls or removes tube(s) or catheter(s); aggressive",
    "+2": "Agitated - Frequent non-purposeful movement, fights ventilator",
    "+1": "Restless - Anxious but movements not aggressive or vigorous",
    "0": "Alert and Calm",
    "-1": "Drowsy - Not fully alert, but has sustained awakening (eye-opening/eye contact) to voice (>10 seconds)",
    "-2": "Light Sedation - Briefly awakens with eye contact to voice (<10 seconds)",
    "-3": "Moderate Sedation - Movement or eye opening to voice (but no eye contact)",
    "-4": "Deep Sedation - No response to voice, but movement or eye opening to physical stimulation",
    "-5": "Unarousable - No response to voice or physical stimulation"
}


def render_rass_calculator():
    """Render RASS (Richmond Agitation-Sedation Scale) calculator"""
    st.subheader("📊 RASS (Richmond Agitation-Sedation Scale)")
    st.caption("Đánh giá mức độ an thần và kích động ở ICU")
    
    st.markdown("""
    **RASS** là thang điểm tiêu chuẩn để đánh giá mức độ an thần và kích động ở ICU.
    Được sử dụng hàng ngày để theo dõi và điều chỉnh liều an thần.
    """)
    
    st.markdown("---")
    
    # RASS selection
    st.markdown("### 🎯 Chọn RASS Score")
    
    rass_options = list(RASS_SCALE.keys())
    rass_selected = st.selectbox(
        "RASS Score:",
        rass_options,
        index=5,  # Default to 0
        format_func=lambda x: f"{x} - {RASS_SCALE[x].split(' - ')[0]}",
        key="rass_score"
    )
    
    # Display description
    rass_num = int(rass_selected) if rass_selected.lstrip('-').isdigit() else 0
    
    if rass_num > 0:
        color = "error"
        icon = "⚠️"
        severity = "Kích động"
    elif rass_num == 0:
        color = "success"
        icon = "✅"
        severity = "Tỉnh táo"
    else:
        color = "info"
        icon = "💤"
        severity = "An thần"
    
    st.markdown("---")
    st.markdown(f"### 📊 Kết quả")
    
    render_result_box(
        "RASS Score",
        f"{rass_selected}",
        subtitle=RASS_SCALE[rass_selected],
        color=color,
        icon=icon
    )
    
    st.markdown("---")
    st.markdown("### 💡 Khuyến Nghị")
    
    # Recommendations based on RASS
    if rass_num >= +2:
        st.error("""
        **🚨 Kích động nặng:**
        - Cần an thần ngay lập tức
        - Cân nhắc Propofol hoặc Midazolam
        - Mục tiêu: RASS -1 to -2
        - Theo dõi sát
        """)
    elif rass_num == +1:
        st.warning("""
        **⚠️ Kích động nhẹ:**
        - Có thể cần tăng liều an thần
        - Mục tiêu: RASS 0 to -1
        - Đánh giá nguyên nhân kích động
        """)
    elif rass_num == 0:
        st.success("""
        **✅ Tỉnh táo:**
        - Mức độ lý tưởng cho bệnh nhân tỉnh
        - Phù hợp cho cai máy thở
        - Không cần điều chỉnh
        """)
    elif rass_num == -1:
        st.info("""
        **💤 An thần nhẹ:**
        - Phù hợp cho an thần thủ thuật
        - Mức độ lý tưởng cho cai máy thở
        - Có thể giảm liều nếu muốn tỉnh hơn
        """)
    elif rass_num == -2:
        st.info("""
        **💤 An thần vừa:**
        - Phù hợp cho an thần thủ thuật
        - Mức độ tốt cho bệnh nhân thở máy
        - Có thể giảm liều nếu muốn tỉnh hơn
        """)
    elif rass_num <= -3:
        st.warning("""
        **⚠️ An thần sâu:**
        - Chỉ dùng khi cần thiết (thủ thuật đau, ARDS nặng)
        - Cân nhắc giảm liều để tránh an thần quá sâu
        - Mục tiêu: RASS -2 to -3
        - Theo dõi sát chức năng hô hấp
        """)
    
    st.markdown("---")
    st.markdown("### 📋 Bảng RASS Scale")
    
    # Display full scale
    for rass, description in RASS_SCALE.items():
        if rass.startswith('+'):
            border_color = "#ef4444"
            bg_color = "#fee2e2"
        elif rass == '0':
            border_color = "#10b981"
            bg_color = "#d1fae5"
        else:
            border_color = "#3b82f6"
            bg_color = "#dbeafe"
        
        st.markdown(f"""
        <div style="padding: 10px; margin: 5px 0; border-left: 4px solid {border_color}; background: {bg_color}; border-radius: 4px;">
            <strong>RASS {rass}:</strong> {description}
        </div>
        """, unsafe_allow_html=True)


def render_cam_icu_calculator():
    """Render CAM-ICU (Confusion Assessment Method for ICU) calculator"""
    st.subheader("🧠 CAM-ICU (Confusion Assessment Method for ICU)")
    st.caption("Sàng lọc delirium ở ICU")
    
    st.markdown("""
    **CAM-ICU** là công cụ sàng lọc delirium ở bệnh nhân ICU, đặc biệt hữu ích cho bệnh nhân 
    không thể giao tiếp bằng lời nói (thở máy, an thần).
    
    **Chẩn đoán Delirium:** Cần có cả 4 tiêu chí:
    1. Khởi phát cấp + dao động
    2. Giảm chú ý
    3. Tư duy rối loạn
    4. Thay đổi mức độ ý thức
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Đánh Giá CAM-ICU")
    
    # Feature 1: Acute onset or fluctuating course
    st.markdown("#### 1️⃣ Khởi phát cấp và dao động")
    feature1_q1 = st.checkbox(
        "Có thay đổi cấp tính trạng thái tâm thần so với ban đầu?",
        key="cam_icu_f1_q1"
    )
    feature1_q2 = st.checkbox(
        "Có dao động trong ngày (tốt hơn/tệ hơn)?",
        key="cam_icu_f1_q2"
    )
    feature1 = feature1_q1 or feature1_q2
    
    # Feature 2: Inattention
    st.markdown("#### 2️⃣ Giảm chú ý")
    st.markdown("**Test chú ý (chọn 1):**")
    
    attention_test = st.radio(
        "Chọn test:",
        ["SAVE (5 letters)", "Vigilance A (10 letters)", "Không thể test"],
        key="cam_icu_attention_test"
    )
    
    if attention_test == "SAVE (5 letters)":
        st.info("""
        **Hướng dẫn:**
        - Đọc 5 chữ cái: S-A-V-E-A
        - Yêu cầu bệnh nhân giơ tay khi nghe chữ "A"
        - **Dương tính:** Bỏ sót ≥2 lần hoặc không làm được
        """)
        save_errors = st.number_input(
            "Số lần bỏ sót:",
            min_value=0,
            max_value=5,
            value=0,
            format="%d",
            key="cam_icu_save_errors"
        )
        feature2 = save_errors >= 2
    elif attention_test == "Vigilance A (10 letters)":
        st.info("""
        **Hướng dẫn:**
        - Đọc 10 chữ cái, có nhiều chữ "A"
        - Yêu cầu bệnh nhân giơ tay khi nghe chữ "A"
        - **Dương tính:** Bỏ sót ≥3 lần hoặc không làm được
        """)
        vigilance_errors = st.number_input(
            "Số lần bỏ sót:",
            min_value=0,
            max_value=10,
            value=0,
            format="%d",
            key="cam_icu_vigilance_errors"
        )
        feature2 = vigilance_errors >= 3
    else:
        feature2 = st.checkbox(
            "Không thể test do bệnh nhân không hợp tác?",
            key="cam_icu_attention_unable"
        )
    
    # Feature 3: Disorganized thinking
    st.markdown("#### 3️⃣ Tư duy rối loạn")
    feature3_q1 = st.checkbox(
        "Câu trả lời không mạch lạc, lan man?",
        key="cam_icu_f3_q1"
    )
    feature3_q2 = st.checkbox(
        "Không thể trả lời câu hỏi đơn giản?",
        key="cam_icu_f3_q2"
    )
    feature3 = feature3_q1 or feature3_q2
    
    # Feature 4: Altered level of consciousness
    st.markdown("#### 4️⃣ Thay đổi mức độ ý thức")
    consciousness_level = st.selectbox(
        "Mức độ ý thức hiện tại:",
        [
            "Tỉnh táo bình thường",
            "Li bì (drowsy)",
            "Lơ mơ (stupor)",
            "Hôn mê (coma)"
        ],
        key="cam_icu_consciousness"
    )
    feature4 = consciousness_level != "Tỉnh táo bình thường"
    
    st.markdown("---")
    
    # Calculate result
    if st.button("🔬 Đánh Giá CAM-ICU", type="primary", key="cam_icu_calculate"):
        has_delirium = feature1 and feature2 and feature3 and feature4
        
        st.markdown("### 📊 Kết quả")
        
        if has_delirium:
            render_warning_alert(
                "🚨 DƯƠNG TÍNH - Chẩn đoán DELIRIUM",
                title="Chẩn đoán"
            )
            
            st.markdown("""
            **Đáp ứng đủ 4 tiêu chí CAM-ICU:**
            - ✅ Tiêu chí 1: Khởi phát cấp + dao động
            - ✅ Tiêu chí 2: Giảm chú ý
            - ✅ Tiêu chí 3: Tư duy rối loạn
            - ✅ Tiêu chí 4: Thay đổi mức độ ý thức
            
            **Xử trí:**
            1. Tìm nguyên nhân (nhiễm trùng, thuốc, rối loạn chuyển hóa, thiếu oxy...)
            2. Điều trị nguyên nhân
            3. Non-pharmacological: Định hướng lại, môi trường yên tĩnh, huy động gia đình
            4. Pharmacological (nếu kích động nguy hiểm): Haloperidol, Quetiapine, hoặc Dexmedetomidine
            5. Theo dõi hàng ngày với CAM-ICU
            """)
        else:
            st.success("""
            ✅ **ÂM TÍNH - Không đủ tiêu chí Delirium**
            
            Không đáp ứng đủ 4 tiêu chí CAM-ICU. Tuy nhiên:
            - Theo dõi tiếp, đánh giá lại hàng ngày
            - Đánh giá lại nếu có thay đổi trạng thái tâm thần
            - Cân nhắc nguyên nhân khác của thay đổi tâm thần
            """)
        
        st.markdown("---")
        st.markdown("### 📋 Phân Loại Delirium")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info("""
            **Hyperactive:**
            - Kích động
            - Ảo giác
            - Dễ nhận biết
            """)
        
        with col2:
            st.info("""
            **Hypoactive:**
            - Lơ mơ, ít nói
            - Dễ bỏ sót
            - Tiên lượng xấu hơn
            """)
        
        with col3:
            st.info("""
            **Mixed:**
            - Kết hợp cả hai
            - Thay đổi theo thời gian
            """)


def render_aki_staging_quick():
    """Render quick AKI staging calculator"""
    st.subheader("🧪 AKI Staging (KDIGO)")
    st.caption("Phân loại suy thận cấp")
    
    st.markdown("""
    **KDIGO (2012)** là tiêu chuẩn quốc tế hiện tại để phân loại AKI.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        baseline_cr = st.number_input(
            "Creatinine ban đầu (mg/dL):",
            min_value=0.1,
            max_value=10.0,
            value=1.0,
            step=0.1,
            format="%.1f",
            key="aki_baseline_cr"
        )
        
        current_cr = st.number_input(
            "Creatinine hiện tại (mg/dL):",
            min_value=0.1,
            max_value=10.0,
            value=1.5,
            step=0.1,
            format="%.1f",
            key="aki_current_cr"
        )
    
    with col2:
        baseline_uo = st.number_input(
            "Lượng nước tiểu ban đầu (ml/kg/h):",
            min_value=0.0,
            max_value=5.0,
            value=1.0,
            step=0.1,
            format="%.1f",
            key="aki_baseline_uo",
            help="Thường là 0.5-1.0 ml/kg/h"
        )
        
        current_uo = st.number_input(
            "Lượng nước tiểu hiện tại (ml/kg/h):",
            min_value=0.0,
            max_value=5.0,
            value=0.3,
            step=0.1,
            format="%.1f",
            key="aki_current_uo"
        )
    
    if st.button("🔬 Đánh Giá AKI", type="primary", key="aki_calculate"):
        # Calculate AKI stage based on KDIGO
        cr_increase = (current_cr - baseline_cr) / baseline_cr if baseline_cr > 0 else 0
        cr_absolute_increase = current_cr - baseline_cr
        
        # Stage based on creatinine
        if current_cr >= baseline_cr * 3.0 or current_cr >= 4.0:
            stage_cr = 3
        elif current_cr >= baseline_cr * 2.0:
            stage_cr = 2
        elif current_cr >= baseline_cr * 1.5 or cr_absolute_increase >= 0.3:
            stage_cr = 1
        else:
            stage_cr = 0
        
        # Stage based on urine output
        if current_uo < 0.3:
            stage_uo = 3
        elif current_uo < 0.5:
            stage_uo = 2
        elif current_uo < baseline_uo * 0.5:
            stage_uo = 1
        else:
            stage_uo = 0
        
        # Final stage (worst of the two)
        final_stage = max(stage_cr, stage_uo)
        
        st.markdown("### 📊 Kết quả")
        
        if final_stage == 0:
            color = "success"
            icon = "✅"
            stage_name = "Không có AKI"
        elif final_stage == 1:
            color = "warning"
            icon = "⚠️"
            stage_name = "AKI Stage 1"
        elif final_stage == 2:
            color = "error"
            icon = "🚨"
            stage_name = "AKI Stage 2"
        else:
            color = "error"
            icon = "🚨"
            stage_name = "AKI Stage 3"
        
        render_result_box(
            "AKI Stage",
            stage_name,
            subtitle=f"Stage {final_stage}",
            color=color,
            icon=icon
        )
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            **Theo Creatinine:**
            - Ban đầu: {baseline_cr:.2f} mg/dL
            - Hiện tại: {current_cr:.2f} mg/dL
            - Tăng: {cr_increase*100:.1f}%
            - **Stage: {stage_cr}**
            """)
        
        with col2:
            st.markdown(f"""
            **Theo Lượng nước tiểu:**
            - Ban đầu: {baseline_uo:.2f} ml/kg/h
            - Hiện tại: {current_uo:.2f} ml/kg/h
            - **Stage: {stage_uo}**
            """)
        
        if final_stage >= 1:
            st.warning("""
            **⚠️ Xử trí:**
            1. Tìm nguyên nhân (prerenal, intrinsic, postrenal)
            2. Điều trị nguyên nhân
            3. Theo dõi creatinine và lượng nước tiểu
            4. Cân nhắc RRT nếu Stage 3
            5. Tránh nephrotoxic drugs
            """)


def render_scoring_calculator():
    """Main function to render scoring systems calculator"""
    
    st.markdown("## 📊 Critical Care Scoring Systems")
    st.markdown("""
    Tổng hợp các scoring systems quan trọng cho ICU:
    - APACHE II, SOFA, SAPS II: Đánh giá độ nặng và tiên lượng
    - GCS: Đánh giá mức độ ý thức
    - RASS: Đánh giá an thần
    - CAM-ICU: Sàng lọc delirium
    - AKI Staging: Phân loại suy thận cấp
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📊 APACHE II",
        "📊 SOFA",
        "📊 SAPS II",
        "🧠 GCS",
        "📊 RASS",
        "🧠 CAM-ICU",
        "🧪 AKI Staging"
    ])
    
    # Tab 1: APACHE II
    with tab1:
        if render_apache2:
            render_apache2()
        else:
            st.error("APACHE II calculator không khả dụng")
    
    # Tab 2: SOFA
    with tab2:
        if render_sofa:
            render_sofa()
        else:
            st.error("SOFA calculator không khả dụng")
    
    # Tab 3: SAPS II
    with tab3:
        if render_saps2:
            render_saps2()
        else:
            st.error("SAPS II calculator không khả dụng")
    
    # Tab 4: GCS
    with tab4:
        if render_gcs:
            render_gcs()
        else:
            st.error("GCS calculator không khả dụng")
    
    # Tab 5: RASS
    with tab5:
        render_rass_calculator()
    
    # Tab 6: CAM-ICU
    with tab6:
        render_cam_icu_calculator()
    
    # Tab 7: AKI Staging
    with tab7:
        render_aki_staging_quick()
        
        st.markdown("---")
        st.info("""
        **💡 Lưu ý:**
        - Đây là calculator nhanh, dựa trên KDIGO criteria
        - Để tính toán chi tiết, sử dụng KDIGO calculator trong module Scores
        - Stage cuối cùng = stage cao nhất giữa creatinine và lượng nước tiểu
        """)

