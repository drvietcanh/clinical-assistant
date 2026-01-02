"""
Stroke Management Protocol
AHA/ASA Guidelines 2021
Ischemic & Hemorrhagic Stroke
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section
from components.evidence_badge import (
    render_evidence_badge,
    render_evidence_summary,
    Citation
)
from components.phase1_protocol_enhancer import (
    render_protocol_header,
    render_recommendation_with_evidence,
    render_protocol_footer
)
# CDS Decision Tree integration
try:
    from components.cds_decision_trees import get_decision_tree, render_decision_tree
    CDS_DECISION_TREES_AVAILABLE = True
except ImportError:
    CDS_DECISION_TREES_AVAILABLE = False


def render():
    """Stroke Management Protocol"""
    st.subheader("🧠 Stroke Management Protocol")
    st.caption("AHA/ASA Guidelines 2021 - Ischemic & Hemorrhagic Stroke")
    
    # Enhanced header with Phase 1 components
    render_protocol_header(
        protocol_name="Stroke Management",
        guideline_source="AHA/ASA 2024",
        show_version=True,
        show_evidence_summary=True
    )
    
    st.info("""
    **Triệu chứng Stroke (BE FAST):**
    - **B**alance: Mất thăng bằng
    - **E**yes: Mất thị lực
    - **F**ace: Méo mặt
    - **A**rms: Yếu tay
    - **S**peech: Nói khó
    - **T**ime: Gọi cấp cứu ngay!
    """)
    
    # CDS Decision Tree (optional)
    if CDS_DECISION_TREES_AVAILABLE:
        with st.expander("🧭 Cây quyết định lâm sàng (CDS)", expanded=False):
            stroke_tree = get_decision_tree("stroke")
            if stroke_tree:
                render_decision_tree(stroke_tree, title="Stroke Decision Tree")
        st.markdown("---")
    
    st.markdown("---")
    
    # Stroke type selection
    stroke_type = st.radio(
        "**Loại Stroke:**",
        ["Đột quỵ thiếu máu (Ischemic)", "Đột quỵ xuất huyết (Hemorrhagic)", "Dự phòng Đột quỵ (Prevention)", "Chưa xác định"],
        key="stroke_type"
    )
    
    st.markdown("---")
    
    if "thiếu máu" in stroke_type or "Ischemic" in stroke_type:
        render_ischemic_stroke()
    elif "xuất huyết" in stroke_type or "Hemorrhagic" in stroke_type:
        render_hemorrhagic_stroke()
    elif "Dự phòng" in stroke_type or "Prevention" in stroke_type:
        render_prevention()
    else:
        render_unknown_stroke()


def render_ischemic_stroke():
    """Ischemic Stroke Protocol"""
    
    st.error("## 🚨 ISCHEMIC STROKE PROTOCOL")
    st.error("**TIME IS BRAIN - Mỗi phút = 1.9 triệu tế bào não mất đi!**")
    
    st.markdown("### ⏱️ Timeline Goals")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Door-to-CT", "≤25 phút", "🎯 Mục tiêu")
    with col2:
        st.metric("Door-to-Needle (tPA)", "≤60 phút", "🎯 Mục tiêu")
    with col3:
        st.metric("Door-to-Puncture (MT)", "≤90 phút", "🎯 Mục tiêu")
    
    st.markdown("---")
    st.markdown("### 1️⃣ Xử tríTức Thì (< 10 phút)")
    
    st.error("""
    **ABC - Đường thở, Hô hấp, Tuần hoàn:**
    
    **A - Airway:**
    - Đảm bảo đường thở thông thoáng
    - Cân nhắc đặt nội khí quản nếu GCS <8, không bảo vệ được đường thở
    
    **B - Breathing:**
    - O₂ để duy trì SpO₂ >94%
    - Tránh hyperoxia (O₂ không cần thiết nếu SpO₂ >94%)
    
    **C - Circulation:**
    - 2 đường truyền tĩnh mạch
    - Kiểm tra đường huyết
    - Hạ đường huyết: Glucose 50% 50ml IV (nếu <60 mg/dL)
    - Tăng đường huyết: Insulin (nếu >180-200 mg/dL)
    
    **D - Disability:**
    - Đánh giá GCS, NIHSS
    - Thần kinh ngay
    
    **E - Exposure:**
    - ECG
    - CBC, PT/INR, aPTT
    - Đường huyết
    - Troponin (không loại trừ MI)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Chẩn đoán - CT Scan")
    
    st.warning("""
    **CT Head NGAY (trong 25 phút):**
    
    **Mục đích:**
    - Loại trừ xuất huyết não
    - Tìm dấu hiệu sớm của nhồi máu (loss of gray-white differentiation, sulcal effacement)
    - Đánh giá ASPECTS score (nếu MT candidate)
    
    **CT Angiography (CTA):**
    - Nếu trong cửa sổ MT (thường <24h)
    - Tìm tắc mạch lớn (large vessel occlusion)
    - Đánh giá collateral flow
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Thrombolysis - tPA Criteria")
    
    st.markdown("#### ✅ Chỉ định tPA (Alteplase)")
    
    st.markdown("##### ⏱️ Time Windows")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("""
        **Standard Window:**
        - **0-3 giờ:** Tất cả bệnh nhân đủ tiêu chuẩn
        - **3-4.5 giờ:** Thêm tiêu chuẩn:
          * Tuổi ≤80
          * NIHSS ≤25
          * Không có tiền sử đột quỵ + đái tháo đường
        """)
    
    with col2:
        st.info("""
        **Wake-Up Stroke:**
        - **MRI DWI-FLAIR mismatch:** Có thể dùng tPA
        - **CT Perfusion:** Có thể dùng nếu mismatch
        - **Thời gian:** <4.5h từ khi thức dậy
        """)
    
    with col3:
        st.warning("""
        **Extended Window:**
        - **Tenecteplase:** Có thể thay thế alteplase (AHA/ASA 2023)
        - **Mechanical Thrombectomy:** <24h với imaging (DAWN/DEFUSE-3)
        """)
    
    st.markdown("---")
    
    # Tenecteplase option
    st.markdown("#### 💉 Tenecteplase (TNK-tPA) - Alternative to Alteplase")
    
    st.info("""
    **AHA/ASA 2023 Update:**
    - **Tenecteplase** có thể thay thế alteplase trong một số trường hợp
    - **Ưu điểm:** Single IV bolus (không cần infusion), tiện lợi hơn
    - **Liều:** 0.25 mg/kg IV bolus (max 25mg)
    - **Chỉ định:** Tương tự alteplase (0-4.5h window)
    """)
    
    use_tenecteplase = st.radio(
        "**Lựa chọn thuốc thrombolytic:**",
        ["Alteplase (tPA) - Standard", "Tenecteplase (TNK-tPA) - Alternative"],
        key="stroke_thrombolytic_choice"
    )
    
    if use_tenecteplase == "Tenecteplase (TNK-tPA) - Alternative":
        weight_kg = st.number_input(
            "**Cân nặng (kg):**",
            min_value=40.0,
            max_value=150.0,
            value=70.0,
            step=1.0,
            key="tenecteplase_weight"
        )
        
        tnk_dose = min(weight_kg * 0.25, 25.0)
        
        st.success(f"""
        **Tenecteplase Dosing:**
        - **Liều:** {tnk_dose:.1f} mg IV bolus
        - **Cách dùng:** Single IV bolus trong 5-10 giây
        - **Không cần:** Continuous infusion (khác với alteplase)
        
        **Monitoring:** Tương tự alteplase
        - BP mỗi 15 phút trong 2h đầu
        - Neurologic checks mỗi 1h trong 24h
        - CT scan nếu có triệu chứng xuất huyết
        """)
    
    st.markdown("---")
    st.markdown("#### 📋 Interactive tPA Eligibility Checklist")
    
    # Time window
    time_from_onset = st.number_input(
        "**Thời gian từ khi khởi phát triệu chứng (giờ):**",
        min_value=0.0,
        max_value=24.0,
        value=2.0,
        step=0.1,
        key="tpa_time_onset",
        help="Nhập thời gian từ khi bắt đầu có triệu chứng"
    )
    
    # Age
    age = st.number_input(
        "**Tuổi:**",
        min_value=18,
        max_value=120,
        value=65,
        step=1,
        key="tpa_age"
    )
    
    # NIHSS
    nihss = st.number_input(
        "**NIHSS Score:**",
        min_value=0,
        max_value=42,
        value=10,
        step=1,
        key="tpa_nihss"
    )
    
    # Blood pressure
    col1, col2 = st.columns(2)
    with col1:
        sbp = st.number_input(
            "**SBP (mmHg):**",
            min_value=80,
            max_value=250,
            value=160,
            step=1,
            key="tpa_sbp"
        )
    with col2:
        dbp = st.number_input(
            "**DBP (mmHg):**",
            min_value=40,
            max_value=150,
            value=90,
            step=1,
            key="tpa_dbp"
        )
    
    # Lab values
    st.markdown("**Xét nghiệm:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        glucose = st.number_input(
            "**Đường huyết (mg/dL):**",
            min_value=0.0,
            max_value=500.0,
            value=120.0,
            step=1.0,
            key="tpa_glucose"
        )
        platelet = st.number_input(
            "**Platelet (×10³/µL):**",
            min_value=0,
            max_value=1000,
            value=250,
            step=10,
            key="tpa_platelet"
        )
    with col2:
        inr = st.number_input(
            "**INR:**",
            min_value=0.5,
            max_value=10.0,
            value=1.0,
            step=0.1,
            key="tpa_inr",
            help="Nếu không dùng warfarin, nhập 1.0"
        )
        aptt = st.selectbox(
            "**aPTT:**",
            ["Bình thường", "Tăng", "Không biết"],
            key="tpa_aptt"
        )
    with col3:
        noac_use = st.selectbox(
            "**Đang dùng NOAC (Xa inhibitor)?**",
            ["Không", "Có, <48h", "Có, >48h hoặc đã đảo ngược"],
            key="tpa_noac"
        )
    
    # Exclusion criteria checkboxes
    st.markdown("**Chống chỉ định:**")
    col1, col2 = st.columns(2)
    with col1:
        has_hemorrhage = st.checkbox("🚫 Xuất huyết não trên CT", key="tpa_hemorrhage")
        large_infarct = st.checkbox("🚫 Early infarct >1/3 MCA", key="tpa_large_infarct")
        hx_ich = st.checkbox("🚫 Tiền sử xuất huyết nội sọ", key="tpa_hx_ich")
        recent_stroke = st.checkbox("🚫 Đột quỵ <3 tháng", key="tpa_recent_stroke")
        recent_trauma = st.checkbox("🚫 Chấn thương đầu <3 tháng", key="tpa_trauma")
    with col2:
        recent_surgery = st.checkbox("🚫 Phẫu thuật lớn <14 ngày", key="tpa_surgery")
        gi_bleed = st.checkbox("🚫 Xuất huyết tiêu hóa <21 ngày", key="tpa_gi_bleed")
        diabetes_stroke = st.checkbox("⚠️ Tiểu đường + tiền sử đột quỵ (3-4.5h)", key="tpa_diabetes_stroke")
    
    # Eligibility calculation
    st.markdown("---")
    
    # Check eligibility
    eligible = True
    warnings = []
    errors = []
    
    # Time window check
    if time_from_onset > 4.5:
        eligible = False
        errors.append("❌ Thời gian >4.5 giờ - Ngoài cửa sổ tPA")
    elif time_from_onset > 3.0:
        if age > 80:
            eligible = False
            errors.append("❌ Tuổi >80 - Chống chỉ định trong cửa sổ 3-4.5h")
        if nihss > 25:
            eligible = False
            errors.append("❌ NIHSS >25 - Chống chỉ định trong cửa sổ 3-4.5h")
        if diabetes_stroke:
            eligible = False
            errors.append("❌ Tiểu đường + tiền sử đột quỵ - Chống chỉ định trong cửa sổ 3-4.5h")
    
    # Age check
    if age < 18:
        eligible = False
        errors.append("❌ Tuổi <18 - Chống chỉ định")
    
    # Blood pressure check
    if sbp > 185 or dbp > 110:
        warnings.append("⚠️ Huyết áp cao - Cần điều chỉnh trước tPA")
    
    # Lab checks
    if glucose < 50:
        eligible = False
        errors.append("❌ Đường huyết <50 mg/dL")
    if platelet < 100:
        eligible = False
        errors.append("❌ Platelet <100,000/µL")
    if inr > 1.7:
        eligible = False
        errors.append("❌ INR >1.7 (đang dùng warfarin)")
    if aptt == "Tăng":
        warnings.append("⚠️ aPTT tăng - Kiểm tra lại")
    if noac_use == "Có, <48h":
        eligible = False
        errors.append("❌ Đang dùng NOAC <48h - Cần đảo ngược trước")
    
    # Exclusion criteria
    if has_hemorrhage:
        eligible = False
        errors.append("❌ Xuất huyết não trên CT - Chống chỉ định tuyệt đối")
    if large_infarct:
        eligible = False
        errors.append("❌ Early infarct >1/3 MCA - Chống chỉ định tuyệt đối")
    if hx_ich:
        eligible = False
        errors.append("❌ Tiền sử xuất huyết nội sọ - Chống chỉ định tuyệt đối")
    if recent_stroke:
        eligible = False
        errors.append("❌ Đột quỵ <3 tháng - Chống chỉ định tuyệt đối")
    if recent_trauma:
        eligible = False
        errors.append("❌ Chấn thương đầu <3 tháng - Chống chỉ định tuyệt đối")
    if recent_surgery:
        eligible = False
        errors.append("❌ Phẫu thuật lớn <14 ngày - Chống chỉ định tuyệt đối")
    if gi_bleed:
        eligible = False
        errors.append("❌ Xuất huyết tiêu hóa <21 ngày - Chống chỉ định tuyệt đối")
    
    # Display result
    if eligible and len(warnings) == 0:
        st.success("### ✅ **ĐỦ TIÊU CHUẨN DÙNG tPA**")
        st.info("Bệnh nhân đủ tiêu chuẩn dùng Alteplase (tPA). Tiếp tục với dosing calculator bên dưới.")
    elif eligible and len(warnings) > 0:
        st.warning("### ⚠️ **ĐỦ TIÊU CHUẨN NHƯNG CẦN LƯU Ý**")
        for warning in warnings:
            st.warning(warning)
        st.info("Có thể dùng tPA sau khi xử lý các vấn đề trên.")
    else:
        st.error("### ❌ **KHÔNG ĐỦ TIÊU CHUẨN DÙNG tPA**")
        for error in errors:
            st.error(error)
        if warnings:
            st.warning("**Cảnh báo thêm:**")
            for warning in warnings:
                st.warning(warning)
        st.info("Cân nhắc Mechanical Thrombectomy nếu đủ tiêu chuẩn (xem phần dưới).")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Inclusion Criteria:**
        
        ✅ **Thời gian:** < 4.5 giờ từ khi khởi phát triệu chứng
        ✅ **Tuổi:** ≥18 tuổi (3-4.5h: ≤80)
        ✅ **NIHSS:** Có triệu chứng thần kinh đo được (3-4.5h: ≤25)
        ✅ **CT:** Không có xuất huyết, không có early infarct >1/3 MCA
        ✅ **Huyết áp:** SBP <185, DBP <110 mmHg (có thể điều chỉnh)
        ✅ **Đường huyết:** ≥50 mg/dL
        ✅ **Platelet:** ≥100,000/µL
        ✅ **INR:** ≤1.7 (nếu dùng warfarin)
        ✅ **aPTT:** Bình thường (nếu dùng heparin gần đây)
        ✅ **NOAC:** Không dùng trong 48h (hoặc đã đảo ngược)
        """)
    
    with col2:
        st.error("""
        **Exclusion Criteria (Tuyệt đối):**
        
        🚫 **Thời gian:** > 4.5 giờ từ khi khởi phát (standard)
        🚫 **Xuất huyết:** Xuất huyết não trên CT
        🚫 **Early infarct:** >1/3 MCA territory trên CT
        🚫 **Tăng áp nặng:** SBP >185 hoặc DBP >110 (không kiểm soát được sau điều trị)
        🚫 **Tiền sử xuất huyết nội sọ**
        🚫 **Đột quỵ gần đây:** < 3 tháng
        🚫 **Chấn thương đầu gần đây:** < 3 tháng
        🚫 **Phẫu thuật lớn gần đây:** < 14 ngày
        🚫 **Đang dùng Warfarin và INR >1.7**
        🚫 **Đang dùng NOAC (Xa inhibitor) <48h** (chưa đảo ngược)
        🚫 **Platelet <100,000/µL**
        🚫 **Tiền sử xuất huyết tiêu hóa <21 ngày**
        
        **Exclusion (Tương đối - 3-4.5h):**
        ⚠️ Tuổi >80
        ⚠️ Tiểu đường + tiền sử đột quỵ
        ⚠️ NIHSS >25
        """)
    
    st.markdown("---")
    st.markdown("#### 💉 tPA Dosing Calculator")
    
    if not eligible:
        st.info("💡 **Lưu ý:** Bệnh nhân không đủ tiêu chuẩn tPA. Calculator này chỉ để tham khảo.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        weight = st.number_input(
            "**Cân nặng (kg):**",
            min_value=40.0,
            max_value=150.0,
            value=70.0,
            step=0.1,
            key="tpa_weight"
        )
        
        # Alteplase vial selection
        vial_size = st.selectbox(
            "**Kích thước lọ Alteplase:**",
            ["50 mg", "100 mg"],
            key="tpa_vial_size",
            help="Chọn kích thước lọ có sẵn"
        )
        
        if weight > 0:
            total_dose = min(weight * 0.9, 90.0)  # Max 90 mg
            bolus_dose = total_dose * 0.1
            infusion_dose = total_dose * 0.9
            
            # Calculate volumes
            # Standard: 1 mg/ml concentration
            bolus_volume = bolus_dose  # ml (if 1 mg/ml)
            infusion_volume = infusion_dose  # ml (if 1 mg/ml)
            infusion_rate = infusion_volume  # ml/h (to infuse in 60 min)
            
            # Determine how many vials needed
            vial_mg = 50 if vial_size == "50 mg" else 100
            vials_needed = 1 if total_dose <= vial_mg else 2
            
            st.markdown("### 📊 Kết quả tính liều")
            st.metric("**Tổng liều:**", f"{total_dose:.1f} mg", help="0.9 mg/kg, tối đa 90 mg")
            st.metric("**Bolus (10%):**", f"{bolus_dose:.1f} mg", help="Truyền trong 1 phút")
            st.metric("**Infusion (90%):**", f"{infusion_dose:.1f} mg", help="Truyền trong 60 phút")
            
            st.markdown("---")
            st.markdown("### 💧 Thể tích & tốc độ truyền")
            st.metric("**Bolus volume:**", f"{bolus_volume:.1f} ml", help="Nếu pha 1 mg/ml")
            st.metric("**Infusion volume:**", f"{infusion_volume:.1f} ml", help="Nếu pha 1 mg/ml")
            st.metric("**Infusion rate:**", f"{infusion_rate:.1f} ml/h", help="Trong 60 phút")
            
            st.markdown("---")
            st.markdown("### 📦 Chuẩn bị thuốc")
            st.info(f"**Cần {vials_needed} lọ {vial_size}**")
            if vials_needed == 1:
                st.success(f"Pha {vial_mg}mg trong {vial_mg}ml NS = 1 mg/ml")
            else:
                st.success(f"Pha {vial_mg * 2}mg trong {vial_mg * 2}ml NS = 1 mg/ml")
    
    with col2:
        st.markdown("### 📋 Hướng dẫn pha & truyền")
        
        st.info("""
        **Alteplase (tPA) Protocol:**
        
        **Liều:** 0.9 mg/kg (max 90 mg)
        - **10% của tổng liều:** Bolus IV trong 1 phút
        - **90% còn lại:** Truyền trong 60 phút
        
        **Cách pha:**
        - Alteplase 50mg pha trong 50ml NS = 1 mg/ml
        - Hoặc 100mg pha trong 100ml NS = 1 mg/ml
        - **Lưu ý:** Pha ngay trước khi dùng, không để quá 8 giờ
        
        **Quy trình truyền:**
        1. **Bolus:** Rút {bolus_volume:.1f}ml từ lọ đã pha, truyền nhanh trong 1 phút
        2. **Infusion:** Còn lại {infusion_volume:.1f}ml, truyền với tốc độ {infusion_rate:.1f} ml/h trong 60 phút
        3. **Hoàn thành:** Tổng thời gian 61 phút (1 phút bolus + 60 phút infusion)
        
        **Lưu ý quan trọng:**
        - ❌ Không trộn với các thuốc khác
        - ❌ Dùng đường truyền riêng (không dùng chung với dịch truyền khác)
        - ✅ Hoàn thành trong 60 phút (không được kéo dài)
        - ✅ Theo dõi sát trong khi truyền (xem monitoring protocol)
        - ✅ Dừng ngay nếu có dấu hiệu xuất huyết
        """.format(
            bolus_volume=bolus_volume if weight > 0 else 0,
            infusion_volume=infusion_volume if weight > 0 else 0,
            infusion_rate=infusion_rate if weight > 0 else 0
        ))
        
        st.markdown("---")
        st.markdown("### ⏱️ Timeline")
        
        timeline_data = {
            "Thời điểm": ["0 phút", "1 phút", "61 phút"],
            "Hành động": [
                "Bắt đầu bolus",
                "Bắt đầu infusion",
                "Hoàn thành tPA"
            ],
            "Theo dõi": [
                "Huyết áp, thần kinh",
                "Huyết áp mỗi 15 phút",
                "CT Head sau 24h"
            ]
        }
        
        import pandas as pd
        st.dataframe(pd.DataFrame(timeline_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("#### 📊 Post-tPA Monitoring Protocol")
    
    # Monitoring checklist tabs
    tab1, tab2, tab3 = st.tabs(["⏱️ Trong khi truyền (0-60 phút)", "🕐 0-24 giờ", "🚨 Xử trí xuất huyết"])
    
    with tab1:
        st.warning("### Theo dõi trong khi truyền tPA (60 phút)")
        
        st.markdown("**Checklist theo dõi:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Huyết áp (mỗi 15 phút):**")
            bp_0min = st.checkbox("0 phút", key="bp_0")
            bp_15min = st.checkbox("15 phút", key="bp_15")
            bp_30min = st.checkbox("30 phút", key="bp_30")
            bp_45min = st.checkbox("45 phút", key="bp_45")
            bp_60min = st.checkbox("60 phút", key="bp_60")
            
            st.markdown("**Mục tiêu:** SBP <185 mmHg, DBP <110 mmHg")
            
            current_sbp = st.number_input(
                "**SBP hiện tại (mmHg):**",
                min_value=80,
                max_value=250,
                value=160,
                key="monitor_sbp"
            )
            current_dbp = st.number_input(
                "**DBP hiện tại (mmHg):**",
                min_value=40,
                max_value=150,
                value=90,
                key="monitor_dbp"
            )
            
            if current_sbp > 185 or current_dbp > 110:
                st.error("⚠️ **Huyết áp cao!** Cần điều trị ngay:")
                st.info("""
                - **Labetalol:** 10-20mg IV, có thể lặp lại mỗi 10-15 phút
                - **Nicardipine:** 5mg/h IV, tăng đến 15mg/h
                - **Mục tiêu:** SBP <185, DBP <110 mmHg
                """)
        
        with col2:
            st.markdown("**Thần kinh (mỗi 30 phút):**")
            neuro_0min = st.checkbox("0 phút", key="neuro_0")
            neuro_30min = st.checkbox("30 phút", key="neuro_30")
            neuro_60min = st.checkbox("60 phút", key="neuro_60")
            
            st.markdown("**Đánh giá:**")
            neuro_change = st.selectbox(
                "**Thay đổi thần kinh:**",
                ["Không", "Có - Đau đầu", "Có - Buồn nôn/nôn", "Có - Thay đổi ý thức", "Có - Yếu liệt nặng lên"],
                key="neuro_change"
            )
            
            if neuro_change != "Không":
                st.error("🚨 **DỪNG tPA NGAY!**")
                st.error("""
                **Xử trí ngay:**
                1. Dừng tPA ngay lập tức
                2. CT Head ngay (không chờ)
                3. Gọi thần kinh/ICU
                4. Chuẩn bị đảo ngược nếu có xuất huyết
                """)
        
        st.markdown("---")
        st.markdown("**Dấu hiệu xuất huyết cần theo dõi:**")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            headache = st.checkbox("Đau đầu đột ngột", key="sx_headache")
        with col2:
            nausea = st.checkbox("Buồn nôn/nôn", key="sx_nausea")
        with col3:
            loc_change = st.checkbox("Thay đổi ý thức", key="sx_loc")
        with col4:
            bp_surge = st.checkbox("Tăng HA đột ngột", key="sx_bp")
        
        if headache or nausea or loc_change or bp_surge:
            st.error("🚨 **Có dấu hiệu xuất huyết!** Xem tab 'Xử trí xuất huyết'")
    
    with tab2:
        st.error("### Monitoring Sau tPA (24 giờ đầu)")
        
        time_period = st.radio(
            "**Chọn giai đoạn:**",
            ["0-2 giờ", "2-8 giờ", "8-24 giờ"],
            key="monitor_period"
        )
        
        if time_period == "0-2 giờ":
            st.markdown("**Checklist 0-2 giờ:**")
            st.checkbox("✅ Huyết áp mỗi 15 phút", key="check_0_2_bp")
            st.checkbox("✅ Neurologic checks mỗi 30 phút", key="check_0_2_neuro")
            st.checkbox("✅ Theo dõi dấu hiệu xuất huyết", key="check_0_2_bleed")
            st.checkbox("✅ Đánh giá NIHSS nếu có thay đổi", key="check_0_2_nihss")
            
            st.info("""
            **Mục tiêu:**
            - Huyết áp: SBP <185, DBP <110 mmHg
            - Thần kinh: Ổn định hoặc cải thiện
            - Không có dấu hiệu xuất huyết
            """)
        
        elif time_period == "2-8 giờ":
            st.markdown("**Checklist 2-8 giờ:**")
            st.checkbox("✅ Huyết áp mỗi 30 phút", key="check_2_8_bp")
            st.checkbox("✅ Neurologic checks mỗi 1 giờ", key="check_2_8_neuro")
            st.checkbox("✅ CT Head nếu có triệu chứng xuất huyết", key="check_2_8_ct")
            st.checkbox("✅ Đánh giá lại NIHSS", key="check_2_8_nihss")
            
            st.info("""
            **Mục tiêu:**
            - Tiếp tục ổn định
            - Nếu có triệu chứng xuất huyết → CT Head ngay
            """)
        
        else:  # 8-24 giờ
            st.markdown("**Checklist 8-24 giờ:**")
            st.checkbox("✅ Huyết áp mỗi 1 giờ", key="check_8_24_bp")
            st.checkbox("✅ Neurologic checks mỗi 2 giờ", key="check_8_24_neuro")
            st.checkbox("✅ CT Head sau 24h (routine)", key="check_8_24_ct")
            st.checkbox("✅ Đánh giá mRS, NIHSS", key="check_8_24_scores")
            st.checkbox("✅ Bắt đầu antiplatelet (sau 24h)", key="check_8_24_antiplatelet")
            
            st.info("""
            **Mục tiêu:**
            - CT Head routine sau 24h để đánh giá
            - Bắt đầu antiplatelet sau 24h (nếu không có xuất huyết)
            - Đánh giá kết quả điều trị
            """)
    
    with tab3:
        st.error("### 🚨 Xử tríNếu Có Xuất huyết")
        
        st.markdown("**Checklist xử trí xuất huyết:**")
        
        st.checkbox("1️⃣ Dừng tPA ngay lập tức", key="bleed_stop_tpa")
        st.checkbox("2️⃣ CT Head ngay (không chờ)", key="bleed_ct")
        st.checkbox("3️⃣ Gọi thần kinh/ICU ngay", key="bleed_consult")
        st.checkbox("4️⃣ Đảo ngược tPA", key="bleed_reverse")
        st.checkbox("5️⃣ Neurosurgery consult", key="bleed_neurosurgery")
        st.checkbox("6️⃣ ICU monitoring", key="bleed_icu")
        
        st.markdown("---")
        st.error("### Đảo Ngược tPA")
        
        st.warning("""
        **Cryoprecipitate + FFP:**
        - **Cryoprecipitate:** 10 units IV
        - **FFP:** 2 units IV
        - **Mục tiêu:** Đảo ngược tác dụng tPA
        
        **Hoặc (nếu không có Cryoprecipitate):**
        - **FFP:** 4-6 units IV
        - **Platelet:** 1 unit (nếu platelet <100,000)
        
        **Theo dõi sau đảo ngược:**
        - CT Head lặp lại
        - Neurologic checks liên tục
        - Huyết áp liên tục
        - Cân nhắc phẫu thuật nếu hematoma lớn
        """)
        
        st.markdown("---")
        st.info("""
        **Tiên lượng xuất huyết sau tPA:**
        - Tỷ lệ: 2-7% bệnh nhân dùng tPA
        - Tử vong: 40-50% nếu có xuất huyết nặng
        - Phụ thuộc vào: Kích thước hematoma, vị trí, tuổi, GCS
        """)
    
    st.markdown("---")
    st.markdown("#### 🚫 Chống chỉ định điều chỉnh huyết áp")
    
    st.info("""
    **Nếu SBP >185 hoặc DBP >110 trước tPA:**
    
    **Điều trị để đạt mục tiêu:**
    - **Labetalol:** 10-20mg IV, có thể lặp lại mỗi 10-15 phút
    - **Nicardipine:** 5mg/h IV, tăng dần đến 15mg/h
    - **Clevidipine:** 1-2 mg/h IV (nếu có)
    
    **Mục tiêu:**
    - SBP <185 mmHg
    - DBP <110 mmHg
    - Đạt được trong 60 phút để không bỏ lỡ cửa sổ tPA
    
    **Nếu không kiểm soát được:** Không dùng tPA
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Lấy huyết khối cơ học (Mechanical Thrombectomy)")
    
    st.markdown("#### ✅ Chỉ định MT (Endovascular Thrombectomy)")
    
    st.info("""
    **AHA/ASA 2023 Update - Extended Windows:**
    - **DAWN Trial:** Up to 24h với clinical-imaging mismatch
    - **DEFUSE-3 Trial:** Up to 16h với perfusion mismatch
    - **CT Perfusion** hoặc **MRI DWI-FLAIR** để xác định salvageable tissue
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Time Windows:**
        
        **0-6 giờ (Standard):**
        ✅ **Thời gian:** < 6 giờ từ khi khởi phát
        ✅ **Loại mạch:** Large vessel occlusion
          * ICA (Internal Carotid Artery)
          * M1 (Middle Cerebral Artery M1)
          * M2 (Middle Cerebral Artery M2)
          * Basilar artery
        ✅ **NIHSS:** ≥6
        ✅ **ASPECTS:** ≥6 (NCCT) hoặc ≥5 (MRI DWI)
        ✅ **CTA/MRA:** Xác nhận tắc mạch lớn
        
        **6-24 giờ (Extended Window - DAWN/DEFUSE-3):**
        ✅ **Thời gian:** 6-24 giờ từ khi khởi phát
        ✅ **Imaging:** CT Perfusion hoặc MRI DWI-FLAIR mismatch
        ✅ **Core infarct:** <70ml (CT Perfusion)
        ✅ **Penumbra:** >15ml mismatch
        ✅ **Age:** ≥18 tuổi
        ✅ **NIHSS:** ≥6
        """)
    
    with col2:
        st.warning("""
        **Chống chỉ định:**
        
        🚫 **Thời gian:** >24 giờ (trừ basilar occlusion)
        🚫 **Core infarct lớn:** >70ml trên CT Perfusion
        🚫 **ASPECTS:** <6 (NCCT) hoặc <5 (MRI)
        🚫 **Mất >1/3 MCA territory** trên CT
        🚫 **Không có tắc mạch lớn** trên CTA/MRA
        🚫 **NIHSS:** <6 (trừ aphasia/neglect)
        🚫 **Tiền sử xuất huyết nội sọ**
        🚫 **Chống chỉ định chụp mạch**
        
        **Basilar Occlusion (Đặc biệt):**
        ✅ Có thể MT đến 24-48 giờ
        ✅ NIHSS có thể thấp hơn (do triệu chứng khác)
        ✅ Cân nhắc MT ngay cả khi core lớn
        """)
    
    st.markdown("---")
    st.markdown("#### ⏱️ Timeline Goals")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("**Door-to-CT**", "≤25 phút", "🎯")
    with col2:
        st.metric("**CT-to-CTA**", "≤15 phút", "🎯")
    with col3:
        st.metric("**Door-to-Puncture**", "≤90 phút", "🎯")
    with col4:
        st.metric("**Door-to-Reperfusion**", "≤120 phút", "🎯")
    
    st.markdown("---")
    st.markdown("#### 🔗 Bridge Therapy (tPA + MT)")
    
    st.info("""
    **Kết hợp tPA và MT:**
    
    **Ưu điểm:**
    - tPA có thể làm tan một phần huyết khối
    - Giảm thời gian tắc mạch
    - Có thể cải thiện kết quả
    
    **Chỉ định:**
    - Bệnh nhân đủ tiêu chuẩn cả tPA và MT
    - Tắc mạch lớn (ICA, M1)
    - Trong cửa sổ tPA (<4.5h)
    
    **Quy trình:**
    1. Bắt đầu tPA ngay (nếu đủ tiêu chuẩn)
    2. Chuyển đến trung tâm MT
    3. MT ngay sau khi đến (không cần chờ tPA xong)
    4. Tiếp tục tPA trong khi MT (nếu chưa xong)
    
    **MT đơn độc (nếu chống chỉ định tPA):**
    - Có thể dùng MT đơn độc
    - Hiệu quả tương đương trong một số trường hợp
    """)
    
    st.markdown("---")
    st.markdown("#### 📊 Post-MT Monitoring")
    
    st.success("""
    **Monitoring Sau MT:**
    
    **0-24 giờ:**
    - Neurologic checks mỗi 1 giờ
    - Huyết áp: Mỗi 15 phút × 2h, sau đó mỗi 30 phút
    - Mục tiêu SBP: <180 mmHg (sau reperfusion)
    - CT Head sau 24h (hoặc sớm hơn nếu có triệu chứng)
    
    **Đánh giá kết quả:**
    - **TICI Score:** 2b-3 (reperfusion tốt)
    - **mRS:** Đánh giá sau 90 ngày
    - **NIHSS:** Cải thiện ≥4 điểm hoặc về 0
    
    **Biến chứng:**
    - Xuất huyết sau MT (5-10%)
    - Tái tắc mạch (5-10%)
    - Distal embolization
    - Vessel dissection
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Hỗ trợ y tế & quản lý huyết áp")
    
    st.markdown("#### 💊 Quản lý Huyết áp Chi Tiết (AHA/ASA Guidelines)")
    
    bp_scenario = st.radio(
        "**Tình huống:**",
        [
            "Trước tPA/MT",
            "Trong và sau tPA (0-24h)",
            "Sau MT (sau reperfusion)",
            "Không dùng tPA/MT"
        ],
        key="bp_scenario"
    )
    
    if bp_scenario == "Trước tPA/MT":
        st.error("""
        **Mục tiêu:** SBP <185 mmHg, DBP <110 mmHg
        
        **Lý do:** Cần đạt mục tiêu này để đủ tiêu chuẩn tPA/MT
        
        **Thuốc điều trị:**
        
        **1. Labetalol (Ưu tiên):**
        - **Liều:** 10-20mg IV bolus
        - **Lặp lại:** Mỗi 10-15 phút nếu cần
        - **Tối đa:** 300mg total
        - **Ưu điểm:** Tác dụng nhanh, ít tác dụng phụ
        
        **2. Nicardipine:**
        - **Liều:** 5mg/h IV infusion
        - **Titrate:** Tăng 2.5mg/h mỗi 5-15 phút
        - **Tối đa:** 15mg/h
        - **Ưu điểm:** Kiểm soát tốt, có thể titrate
        
        **3. Clevidipine (Nếu có):**
        - **Liều:** 1-2 mg/h IV infusion
        - **Titrate:** Tăng 1-2 mg/h mỗi 2-5 phút
        - **Tối đa:** 21 mg/h
        - **Ưu điểm:** Tác dụng rất nhanh, thời gian bán hủy ngắn
        
        **Monitoring:**
        - BP mỗi 5-10 phút khi đang điều trị
        - Đánh giá đáp ứng sau mỗi liều
        
        **⚠️ Nếu không kiểm soát được:** Không dùng tPA
        """)
    
    elif bp_scenario == "Trong và sau tPA (0-24h)":
        st.warning("""
        **Mục tiêu:** SBP <185 mmHg, DBP <110 mmHg (trong 24h đầu)
        
        **Lý do:** Giảm nguy cơ xuất huyết sau tPA
        
        **Theo dõi:**
        - **0-2h:** BP mỗi 15 phút
        - **2-8h:** BP mỗi 30 phút
        - **8-24h:** BP mỗi 1 giờ
        
        **Điều trị nếu SBP >185 hoặc DBP >110:**
        - **Labetalol:** 10-20mg IV, lặp lại mỗi 10-15 phút
        - **Nicardipine:** 5mg/h IV, titrate đến 15mg/h
        - **Clevidipine:** 1-2 mg/h IV, titrate
        
        **Tránh:**
        - Hạ BP quá nhanh (có thể gây hypoperfusion)
        - Nitroprusside (có thể tăng ICP)
        
        **Nếu BP không kiểm soát được:**
        - CT Head ngay để loại trừ xuất huyết
        - Xem xét đảo ngược tPA nếu có xuất huyết
        """)
    
    elif bp_scenario == "Sau MT (sau reperfusion)":
        st.info("""
        **Mục tiêu:** SBP <180 mmHg (sau reperfusion)
        
        **Lý do:** 
        - Giảm nguy cơ xuất huyết sau reperfusion
        - Tối ưu hóa tưới máu vùng đã được tái tưới
        
        **Theo dõi:**
        - **0-2h:** BP mỗi 15 phút
        - **2-24h:** BP mỗi 30 phút - 1 giờ
        
        **Điều trị nếu SBP >180:**
        - **Labetalol:** 10-20mg IV, lặp lại
        - **Nicardipine:** 5mg/h IV, titrate
        - **Clevidipine:** 1-2 mg/h IV, titrate
        
        **Đặc biệt:**
        - Nếu TICI 2b-3 (reperfusion tốt): Có thể cho phép SBP cao hơn một chút
        - Nếu TICI 0-2a (reperfusion kém): Cần kiểm soát BP chặt chẽ hơn
        """)
    
    else:  # Không dùng tPA/MT
        st.success("""
        **Mục tiêu:** Cho phép SBP đến 220 mmHg (trong 24h đầu)
        
        **Lý do:** 
        - Tăng tưới máu vùng penumbra (vùng thiếu máu nhưng chưa hoại tử)
        - Permissive hypertension có thể cải thiện outcomes
        
        **Điều trị nếu SBP >220 mmHg:**
        - **Điều trị từ từ:** Tránh hạ quá nhanh
        - **Mục tiêu:** Giảm 15-25% trong 24h đầu
        - **Thuốc:** Labetalol, nicardipine, hoặc clevidipine
        
        **Điều trị ngay nếu:**
        - SBP >220 mmHg với triệu chứng (đau đầu, đau ngực)
        - Có bằng chứng suy tim, bóc tách động mạch chủ, hoặc bệnh lý khác
        
        **Sau 24h:**
        - Bắt đầu điều trị tăng huyết áp nếu BP vẫn cao
        - Mục tiêu: SBP <140 mmHg (nếu không có chống chỉ định)
        """)
    
    st.markdown("---")
    st.markdown("#### 📊 Blood Pressure Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_sbp = st.number_input(
            "**SBP hiện tại (mmHg):**",
            min_value=80,
            max_value=300,
            value=180,
            key="bp_current_sbp"
        )
        
        current_dbp = st.number_input(
            "**DBP hiện tại (mmHg):**",
            min_value=40,
            max_value=150,
            value=100,
            key="bp_current_dbp"
        )
    
    with col2:
        if bp_scenario == "Trước tPA/MT":
            target_sbp = 185
            target_dbp = 110
        elif bp_scenario == "Trong và sau tPA (0-24h)":
            target_sbp = 185
            target_dbp = 110
        elif bp_scenario == "Sau MT (sau reperfusion)":
            target_sbp = 180
            target_dbp = 110
        else:
            target_sbp = 220
            target_dbp = 120
        
        st.metric("**Mục tiêu SBP:**", f"<{target_sbp} mmHg")
        st.metric("**Mục tiêu DBP:**", f"<{target_dbp} mmHg")
        
        if current_sbp > target_sbp or current_dbp > target_dbp:
            reduction_needed = current_sbp - target_sbp
            st.warning(f"**Cần giảm:** ~{reduction_needed} mmHg")
            st.info("**Khuyến nghị:** Điều trị với labetalol hoặc nicardipine")
        else:
            st.success("**✅ BP trong mục tiêu**")
    
    st.markdown("---")
    
    st.markdown("---")
    st.markdown("#### 🌡️ Quản lý sốt")
    
    st.info("""
    **Sốt sau đột quỵ:**
    - **Tỷ lệ:** 30-50% bệnh nhân đột quỵ
    - **Ảnh hưởng:** Tăng tổn thương não, tăng tử vong
    
    **Điều trị:**
    - **Acetaminophen:** 650-1000mg PO/PR mỗi 4-6h
    - **Mục tiêu:** Nhiệt độ <37.5°C
    - **Nếu sốt kéo dài:** Tìm nguyên nhân (nhiễm trùng, DVT)
    """)
    
    st.markdown("---")
    st.markdown("#### 🍽️ Nuôi dưỡng")
    
    st.warning("""
    **Đánh giá nuốt:**
    - **Trước khi cho ăn:** Đánh giá nuốt (bedside swallow test)
    - **Nếu dysphagia:** NPO, đặt NGT
    - **NGT:** Cho ăn trong 24-48h đầu
    - **PEG:** Nếu dysphagia kéo dài >2 tuần
    
    **Lưu ý:**
    - Tránh aspiration
    - Đánh giá lại nuốt sau 24-48h
    """)
    
    st.markdown("---")
    st.markdown("#### 🩸 Dự phòng DVT")
    
    st.success("""
    **Dự phòng DVT sau đột quỵ:**
    
    **Nếu dùng tPA:**
    - **Không dùng heparin trong 24h đầu**
    - **Sau 24h:** Heparin SC 5000 units q12h hoặc enoxaparin 40mg SC q24h
    - **Hoặc:** Intermittent pneumatic compression
    
    **Nếu không dùng tPA:**
    - **Bắt đầu ngay:** Heparin SC hoặc compression
    - **Nếu liệt nửa người:** Ưu tiên compression + heparin
    
    **Thời gian:**
    - Đến khi bệnh nhân đi lại được
    - Thường 7-14 ngày
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Điều trị sau giai đoạn cấp")
    
    st.markdown("#### 💊 Antiplatelet Therapy - Timing & Selection")
    
    st.info("""
    **AHA/ASA Guidelines - Antiplatelet Timing:**
    """)
    
    antiplatelet_timing = st.radio(
        "**Tình huống:**",
        [
            "Đã dùng tPA",
            "Không dùng tPA - Ischemic stroke",
            "TIA hoặc Minor stroke (NIHSS ≤3)",
            "Chống chỉ định aspirin"
        ],
        key="antiplatelet_timing"
    )
    
    if antiplatelet_timing == "Đã dùng tPA":
        st.warning("""
        **Timing:**
        - **KHÔNG dùng aspirin trong 24h đầu** sau tPA
        - **Sau 24h:** Bắt đầu aspirin nếu không có xuất huyết trên CT
        
        **Liều:**
        - **Aspirin 81-325mg PO** mỗi ngày
        - **Hoặc Clopidogrel 75mg PO** mỗi ngày (nếu dị ứng aspirin)
        
        **Monitoring:**
        - CT Head sau 24h để đảm bảo không có xuất huyết
        - Nếu có xuất huyết: Không dùng antiplatelet
        
        **Lưu ý:**
        - Không dùng DAPT (aspirin + clopidogrel) trong 24h đầu
        """)
    
    elif antiplatelet_timing == "Không dùng tPA - Ischemic stroke":
        st.success("""
        **Timing:**
        - **Có thể bắt đầu ngay** (trong 24-48h đầu)
        - **Hoặc sau 24h** nếu muốn đợi CT Head follow-up
        
        **Lựa chọn:**
        - **Aspirin 81-325mg PO** mỗi ngày (ưu tiên)
        - **Hoặc Clopidogrel 75mg PO** mỗi ngày (nếu dị ứng aspirin)
        
        **Không dùng DAPT** trong 21 ngày đầu (trừ TIA/minor stroke)
        """)
    
    elif antiplatelet_timing == "TIA hoặc Minor stroke (NIHSS ≤3)":
        st.info("""
        **Dual Antiplatelet Therapy (DAPT) - CHANCE/POINT Trials:**
        
        **Chỉ định:**
        - TIA hoặc Minor ischemic stroke (NIHSS ≤3)
        - Không có chống chỉ định
        
        **Liều:**
        - **Aspirin 75-100mg PO** mỗi ngày
        - **+ Clopidogrel 75mg PO** mỗi ngày
        
        **Thời gian:**
        - **21 ngày** (CHANCE trial) hoặc **90 ngày** (POINT trial)
        - Sau đó chuyển sang aspirin đơn độc
        
        **Lợi ích:**
        - Giảm nguy cơ tái phát stroke trong 21-90 ngày đầu
        - Tăng nguy cơ chảy máu nhẹ
        
        **Monitoring:**
        - Theo dõi dấu hiệu chảy máu
        - Đánh giá lại sau 21-90 ngày
        """)
    
    else:  # Chống chỉ định aspirin
        st.error("""
        **Chống chỉ định Aspirin:**
        - Dị ứng aspirin
        - Xuất huyết đang hoạt động
        - Rối loạn đông máu nặng
        
        **Lựa chọn thay thế:**
        - **Clopidogrel 75mg PO** mỗi ngày
        - **Hoặc Ticagrelor 90mg PO** bid (nếu có)
        """)
    
    st.markdown("---")
    st.markdown("#### 🍽️ Dysphagia Screening")
    
    st.warning("""
    **⚠️ QUAN TRỌNG: Screen tất cả bệnh nhân stroke trước khi cho ăn/uống!**
    
    **AHA/ASA Guidelines:**
    - Screen tất cả bệnh nhân stroke trong 24h đầu
    - NPO cho đến khi screen negative
    """)
    
    dysphagia_screen = st.radio(
        "**Kết quả Dysphagia Screen:**",
        ["Chưa screen", "Screen negative (an toàn)", "Screen positive (có nguy cơ)", "Không rõ"],
        key="dysphagia_screen"
    )
    
    if dysphagia_screen == "Chưa screen":
        st.error("""
        **🚨 CẦN SCREEN NGAY!**
        
        **Bedside Swallow Test:**
        1. **Water swallow test:** 50-90ml nước
        2. **Đánh giá:**
           - Ho, sặc
           - Thay đổi giọng nói (wet voice)
           - Khó nuốt
           - Nước chảy ra mũi
        
        **Nếu screen positive:** NPO, đặt NGT
        **Nếu screen negative:** Có thể cho ăn/uống, nhưng theo dõi sát
        """)
    
    elif dysphagia_screen == "Screen negative (an toàn)":
        st.success("""
        **✅ Screen Negative - Có thể cho ăn/uống**
        
        **Lưu ý:**
        - Bắt đầu với thức ăn mềm, dễ nuốt
        - Theo dõi sát trong 24-48h đầu
        - Đánh giá lại nếu có triệu chứng
        
        **Dấu hiệu cần đánh giá lại:**
        - Ho, sặc khi ăn/uống
        - Thay đổi giọng nói
        - Sốt (có thể do aspiration)
        """)
    
    elif dysphagia_screen == "Screen positive (có nguy cơ)":
        st.error("""
        **🚨 Screen Positive - NPO, đặt NGT**
        
        **Xử trí:**
        1. **NPO ngay:** Không cho ăn/uống bằng miệng
        2. **Đặt NGT:** Cho ăn qua ống thông mũi-dạ dày
        3. **Formal swallow evaluation:** Bởi speech therapist trong 24-48h
        
        **NGT Feeding:**
        - Bắt đầu trong 24-48h đầu
        - Đảm bảo đủ dinh dưỡng và nước
        
        **Đánh giá lại:**
        - **Sau 24-48h:** Formal swallow evaluation
        - **Nếu cải thiện:** Có thể thử ăn/uống lại
        - **Nếu không cải thiện:** Xem xét PEG (nếu >2 tuần)
        
        **PEG (Percutaneous Endoscopic Gastrostomy):**
        - Chỉ định: Dysphagia kéo dài >2 tuần
        - Ưu điểm: Thoải mái hơn NGT, giảm nguy cơ viêm phổi
        """)
    
    st.markdown("---")
    st.markdown("#### 💊 Statin & Risk Factor Control")
    
    st.success("""
    **Statin (High-Intensity):**
    - **Atorvastatin 80mg PO** mỗi ngày (ưu tiên)
    - **Hoặc Rosuvastatin 40mg PO** mỗi ngày
    - **Bắt đầu:** Trong 24-48h đầu (nếu không có chống chỉ định)
    
    **Kiểm soát yếu tố nguy cơ:**
    - **Huyết áp:** ACE-I hoặc ARB (mục tiêu <140/90)
    - **Đường huyết:** Kiểm soát HbA1c <7% (nếu có đái tháo đường)
    - **Bỏ thuốc lá:** Tư vấn và hỗ trợ
    - **Lối sống:** Tập thể dục, chế độ ăn lành mạnh
    """)
    
    st.markdown("---")
    st.markdown("### 7️⃣ Thời điểm bắt đầu anticoagulation")
    
    st.warning("""
    **Nếu có chỉ định anticoagulation (AF, DVT/PE):**
    
    **Timing:**
    - **TIA:** Có thể bắt đầu ngay
    - **Minor stroke (NIHSS <4):** Sau 3 ngày
    - **Moderate stroke (NIHSS 5-15):** Sau 7-14 ngày
    - **Severe stroke (NIHSS >15):** Sau 14-21 ngày
    
    **Lựa chọn:**
    - DOAC (Apixaban, Rivaroxaban) ưu tiên hơn Warfarin
    - Nếu Warfarin: INR mục tiêu 2.0-3.0
    """)


def render_hemorrhagic_stroke():
    """Hemorrhagic Stroke (ICH) Protocol"""
    
    st.error("## 🚨 HEMORRHAGIC STROKE (ICH) PROTOCOL")
    st.error("**CODE STROKE - Xử trí khẩn cấp!**")
    
    st.markdown("### 1️⃣ Xử tríTức Thì")
    
    st.error("""
    **ABC tương tự Ischemic Stroke:**
    
    **Điểm khác biệt quan trọng:**
    - **KHÔNG dùng tPA**
    - **Hạ huyết áp ngay:** SBP <140 mmHg (nếu có thể)
    - **Đảo ngược anticoagulation** nếu đang dùng
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Kiểm soát Huyết áp")
    
    st.warning("""
    **Mục tiêu huyết áp:**
    
    **Nếu SBP 150-220 mmHg:**
    - Hạ từ từ đến SBP 140 mmHg
    - Tránh hạ quá nhanh (có thể giảm tưới máu não)
    
    **Nếu SBP >220 mmHg:**
    - Hạ tích cực hơn
    - Có thể cần nitroprusside (nếu có monitoring invasif)
    
    **Thuốc:**
    - Labetalol 10-20mg IV, có thể lặp lại
    - Nicardipine infusion: 5-15 mg/h
    - Clevidipine (nếu có)
    
    **Tránh:**
    - Hạ SBP <140 quá nhanh
    - Hydralazine (không kiểm soát được)
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Đảo ngược anticoagulation")
    
    st.error("""
    **Warfarin (Vitamin K antagonist):**
    - **PCC (Prothrombin Complex Concentrate):** 25-50 U/kg
    - **Vitamin K:** 10mg IV
    - Mục tiêu INR: <1.4 trong 1h
    
    **DOAC (Xa inhibitors):**
    - **Andexanet alfa:** Nếu có (Xa inhibitors)
    - **4F-PCC:** 50 U/kg (nếu không có Andexanet)
    
    **DOAC (Thrombin inhibitors - Dabigatran):**
    - **Idarucizumab:** 5g IV (2 bolus 2.5g)
    
    **Heparin:**
    - Protamine sulfate: 1mg/100 U heparin
    
    **Thời gian:** Đảo ngược càng sớm càng tốt
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Đánh giá & Quyết định phẫu thuật")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Chỉ định phẫu thuật:**
        
        ✅ **Hematoma lớn (>30ml):**
        - Supratentorial >30ml
        - Cerebellar >15ml
        
        ✅ **Dấu hiệu tăng áp nội sọ:**
        - GCS giảm
        - Midline shift >5mm
        - Hydrocephalus
        
        ✅ **Cerebellar hematoma:**
        - >3cm đường kính
        - Có dấu hiệu chèn ép
        """)
    
    with col2:
        st.warning("""
        **Chống chỉ định tương đối:**
        
        ⚠️ **GCS ≤4** (tiên lượng xấu)
        ⚠️ **Tuổi >80** (cân nhắc cẩn thận)
        ⚠️ **Hematoma nhỏ** (<30ml supratentorial)
        ⚠️ **Basal ganglia nhỏ** (thường bảo tồn)
        
        **Lưu ý:** Quyết định phẫu thuật phải cân nhắc:
        - Tuổi, GCS trước phẫu thuật
        - Kích thước và vị trí hematoma
        - Tình trạng thần kinh hiện tại
        """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Điều trị Hỗ trợ")
    
    st.info("""
    **ICP Management (nếu có monitoring ICP):**
    - Mục tiêu ICP: <20 mmHg
    - CPP: 50-70 mmHg
    
    **Hỗ trợ thở máy:**
    - Mục tiêu PaCO₂: 35-40 mmHg
    - Tránh hyperventilation kéo dài
    
    **Sốt:**
    - Hạ sốt: Acetaminophen
    - Mục tiêu: <37.5°C
    
    **Động kinh:**
    - Dự phòng: Không khuyến cáo thường quy
    - Điều trị nếu có cơn: Levetiracetam, Phenytoin
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Theo dõi")
    
    st.success("""
    **Monitoring:**
    - Neurologic checks mỗi 1-2 giờ
    - Huyết áp liên tục
    - CT Head lặp lại nếu:
      * GCS giảm ≥2 điểm
      * Focal deficit nặng lên
      * ICP tăng
      * Sau 24h (đánh giá tiến triển)
    
    **Tiên lượng:**
    - ICH Score: 0-6 (đánh giá tử vong 30 ngày)
    - Phụ thuộc vào:
      * Tuổi
      * GCS
      * Kích thước hematoma
      * Vị trí (infratentorial)
      * OTT (intraventricular hemorrhage)
    """)


def render_unknown_stroke():
    """Protocol when stroke type unknown"""
    
    st.warning("## ⚠️ CHƯA XÁC ĐỊNH LOẠI STROKE")
    
    st.error("""
    **Xử trí ngay trong khi chờ CT:**
    
    1. ✅ **ABC** - Đường thở, Hô hấp, Tuần hoàn
    2. ✅ **2 đường truyền** tĩnh mạch
    3. ✅ **Lấy máu:** CBC, PT/INR, aPTT, Glucose
    4. ✅ **ECG**
    5. ✅ **Gọi CT ngay** (< 25 phút)
    6. ✅ **Thần kinh consult**
    
    **KHÔNG:**
    ❌ Dùng tPA cho đến khi có CT
    ❌ Hạ huyết áp quá mức (chờ CT)
    ❌ Dùng aspirin (nếu nghi xuất huyết)
    
    **Timeline:**
    - CT trong 25 phút
    - Sau khi có CT → quyết định Ischemic vs Hemorrhagic protocol
    """)
    
    # Enhanced footer with Phase 1 component
    render_protocol_footer("Stroke Management")


def render_prevention():
    """Primary Prevention of Stroke (AHA 2024)"""
    st.subheader("🛡️ Dự phòng Đột quỵ Tiên phát (AHA 2024)")
    st.caption("AHA 2024 Guideline for the Primary Prevention of Stroke")
    
    st.info("""
    **Cập nhật AHA 2024:**
    - Tập trung vào **Life's Essential 8** để giảm nguy cơ.
    - Khuyến cáo mới về **GLP-1 Receptor Agonists** cho bệnh nhân tiểu đường.
    - Mục tiêu huyết áp tích cực hơn (**<130/80 mmHg**).
    """)
    
    st.markdown("### 1️⃣ Life's Essential 8 (8 Yếu tố Cốt lõi)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Yếu tố Hành vi:**
        1. **Chế độ ăn (Diet):** Địa Trung Hải, DASH. Hạn chế muối, đường.
        2. **Hoạt động thể lực (Activity):** 150 phút/tuần trung bình hoặc 75 phút/tuần mạnh.
        3. **Ngưng thuốc lá (Nicotine):** Bao gồm cả thuốc lá điện tử.
        4. **Giấc ngủ (Sleep):** 7-9 giờ/đêm. Điều trị ngưng thở khi ngủ (OSA) nếu có.
        """)
        
    with col2:
        st.warning("""
        **Yếu tố Sức khỏe:**
        5. **BMI:** Duy trì BMI 18.5-24.9.
        6. **Lipid máu:** Kiểm soát Non-HDL và LDL.
        7. **Đường huyết:** HbA1c <7%.
        8. **Huyết áp:** <130/80 mmHg.
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Khuyến cáo Thuốc (Pharmacotherapy)")
    
    with st.expander("💊 Xem chi tiết khuyến cáo thuốc", expanded=True):
        st.markdown("""
        **1. Bệnh nhân Đái tháo đường:**
        - **GLP-1 Receptor Agonists:** (Semaglutide, Liraglutide) được khuyến cáo để giảm nguy cơ đột quỵ ở bệnh nhân ĐTĐ type 2 và nguy cơ tim mạch cao. (Class 1)
        - **SGLT2 Inhibitors:** Cũng có lợi ích trên tim mạch và thận.
        
        **2. Huyết áp:**
        - Mục tiêu: **<130/80 mmHg** cho hầu hết bệnh nhân.
        - Thuốc: Thiazide, ACEi/ARB, CCB (Calcium Channel Blocker).
        
        **3. Lipid máu (Primary Prevention):**
        - Nguy cơ tim mạch 10 năm (ASCVD Risk) ≥7.5% hoặc ĐTĐ: Dùng Statin cường độ trung bình-cao.
        - Mục tiêu LDL: Giảm ≥50% hoặc <70 mg/dL (nguy cơ cao).
        
        **4. Aspirin:**
        - **KHÔNG** khuyến cáo Aspirin liều thấp thường quy cho dự phòng *tiên phát* (do nguy cơ xuất huyết > lợi ích).
        - Chỉ cân nhắc ở nhóm nguy cơ tim mạch rất cao và nguy cơ xuất huyết thấp (Class 2b).
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Sàng lọc Rung nhĩ (Atrial Fibrillation)")
    st.info("""
    - Sàng lọc rung nhĩ cho người **>65 tuổi** (bắt mạch, ECG, thiết bị đeo).
    - Nếu phát hiện Rung nhĩ: Đánh giá điểm **CHA₂DS₂-VASc**.
    - **CHA₂DS₂-VASc ≥2 (nam) hoặc ≥3 (nữ):** Chỉ định thuốc chống đông đường uống (DOAC ưu tiên hơn Warfarin).
    """)
    
    render_protocol_footer("Stroke Prevention")


