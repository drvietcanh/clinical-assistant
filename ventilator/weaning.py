"""
Ventilator Weaning Protocol
Hỗ trợ cai máy thở
"""

import streamlit as st


def calculate_rsbi(rr, vt_liters):
    """
    Tính Rapid Shallow Breathing Index (RSBI)
    RSBI = RR / Vt (L)
    """
    if vt_liters > 0:
        return rr / vt_liters
    return None


def interpret_rsbi(rsbi):
    """Đánh giá RSBI"""
    if rsbi is None:
        return None, None, None
    
    if rsbi < 105:
        return "Tốt", "success", "RSBI <105 - Có thể cai máy thở"
    elif rsbi < 130:
        return "Trung bình", "warning", "RSBI 105-130 - Cần theo dõi"
    else:
        return "Kém", "error", "RSBI >130 - Khó cai máy thở"
    
    return None, None, None


def assess_weaning_readiness(abg_data, vent_settings, vitals, neurological, other_factors):
    """
    Đánh giá sẵn sàng cai máy thở
    Dựa trên nhiều tiêu chí
    """
    criteria = {
        "passed": [],
        "failed": [],
        "warnings": []
    }
    
    # ABG criteria
    pf_ratio = abg_data.get("po2", 0) / (abg_data.get("fio2", 100) / 100) if abg_data.get("fio2", 0) > 0 else None
    ph = abg_data.get("ph", 7.40)
    pco2 = abg_data.get("pco2", 40)
    hco3 = abg_data.get("hco3", 24)
    
    if pf_ratio and pf_ratio >= 200:
        criteria["passed"].append("P/F ratio ≥200")
    elif pf_ratio:
        criteria["failed"].append(f"P/F ratio thấp ({pf_ratio:.0f})")
    
    if 7.30 <= ph <= 7.50:
        criteria["passed"].append("pH 7.30-7.50")
    else:
        criteria["failed"].append(f"pH ngoài giới hạn ({ph:.2f})")
    
    if 35 <= pco2 <= 50:
        criteria["passed"].append("PaCO₂ 35-50 mmHg")
    elif pco2 > 50:
        criteria["failed"].append(f"PaCO₂ cao ({pco2:.1f} mmHg)")
    else:
        criteria["warnings"].append(f"PaCO₂ thấp ({pco2:.1f} mmHg)")
    
    # Ventilator settings criteria
    peep = vent_settings.get("peep", 0)
    fio2 = vent_settings.get("fio2", 100)
    
    if peep <= 8:
        criteria["passed"].append(f"PEEP ≤8 cmH2O ({peep} cmH2O)")
    else:
        criteria["failed"].append(f"PEEP cao ({peep} cmH2O)")
    
    if fio2 <= 50:
        criteria["passed"].append(f"FiO₂ ≤50% ({fio2}%)")
    else:
        criteria["failed"].append(f"FiO₂ cao ({fio2}%)")
    
    # Vital signs
    hr = vitals.get("hr", 0)
    bp_systolic = vitals.get("bp_systolic", 0)
    temp = vitals.get("temp", 37)
    
    if 60 <= hr <= 120:
        criteria["passed"].append(f"HR 60-120 bpm ({hr} bpm)")
    else:
        criteria["warnings"].append(f"HR ngoài giới hạn ({hr} bpm)")
    
    if 90 <= bp_systolic <= 180:
        criteria["passed"].append(f"SBP 90-180 mmHg ({bp_systolic} mmHg)")
    else:
        criteria["warnings"].append(f"SBP ngoài giới hạn ({bp_systolic} mmHg)")
    
    if 36 <= temp <= 38.5:
        criteria["passed"].append(f"Temp 36-38.5°C ({temp}°C)")
    else:
        criteria["warnings"].append(f"Temp ngoài giới hạn ({temp}°C)")
    
    # Neurological
    gcs = neurological.get("gcs", 15)
    if gcs >= 13:
        criteria["passed"].append(f"GCS ≥13 ({gcs})")
    else:
        criteria["failed"].append(f"GCS thấp ({gcs})")
    
    # Other factors
    if other_factors.get("no_sepsis", False):
        criteria["passed"].append("Không có nhiễm trùng huyết")
    else:
        criteria["warnings"].append("Có nhiễm trùng huyết")
    
    if other_factors.get("no_acidosis", False):
        criteria["passed"].append("Không có toan máu nặng")
    else:
        criteria["warnings"].append("Có toan máu")
    
    if other_factors.get("hemodynamically_stable", False):
        criteria["passed"].append("Huyết động ổn định")
    else:
        criteria["failed"].append("Huyết động không ổn định")
    
    # Calculate score
    total_criteria = len(criteria["passed"]) + len(criteria["failed"]) + len(criteria["warnings"])
    passed_ratio = len(criteria["passed"]) / total_criteria if total_criteria > 0 else 0
    
    # Determine readiness
    if len(criteria["failed"]) == 0 and passed_ratio >= 0.7:
        readiness = "Sẵn sàng"
        readiness_color = "success"
    elif len(criteria["failed"]) <= 2 and passed_ratio >= 0.6:
        readiness = "Có thể thử"
        readiness_color = "warning"
    else:
        readiness = "Chưa sẵn sàng"
        readiness_color = "error"
    
    return criteria, readiness, readiness_color, passed_ratio


def sbt_protocol():
    """SBT (Spontaneous Breathing Trial) Protocol"""
    return {
        "steps": [
            {
                "step": 1,
                "title": "Chuẩn bị",
                "actions": [
                    "Đảm bảo bệnh nhân tỉnh táo, hợp tác",
                    "Kiểm tra huyết động ổn định",
                    "Kiểm tra ABG gần nhất",
                    "Chuẩn bị theo dõi sát"
                ]
            },
            {
                "step": 2,
                "title": "Cài đặt SBT",
                "actions": [
                    "Chuyển sang CPAP mode",
                    "PEEP: 5-8 cmH2O",
                    "FiO₂: Giữ nguyên hoặc tăng 10%",
                    "PSV: 5-8 cmH2O (nếu dùng)",
                    "Thời gian: 30-120 phút"
                ]
            },
            {
                "step": 3,
                "title": "Theo dõi trong SBT",
                "actions": [
                    "Theo dõi RR, SpO₂, HR, BP mỗi 5-15 phút",
                    "Kiểm tra dấu hiệu suy hô hấp",
                    "Theo dõi tình trạng bệnh nhân"
                ]
            },
            {
                "step": 4,
                "title": "Đánh giá kết quả",
                "actions": [
                    "Nếu thành công: Tiếp tục cai máy thở",
                    "Nếu thất bại: Quay lại thông số cũ, đánh giá lại sau 24h"
                ]
            }
        ],
        "success_criteria": [
            "RR: 8-35 lần/phút",
            "SpO₂: ≥88-90%",
            "HR: Thay đổi <20%",
            "SBP: Thay đổi <20%",
            "Không có dấu hiệu suy hô hấp",
            "Bệnh nhân thoải mái"
        ],
        "failure_criteria": [
            "RR >35 hoặc <8",
            "SpO₂ <88%",
            "HR tăng >20%",
            "SBP tăng/giảm >20%",
            "Dấu hiệu suy hô hấp (co kéo, thở nhanh, etc.)",
            "Bệnh nhân lo lắng, khó chịu"
        ]
    }


def render_weaning_calculator():
    """Weaning Calculator - Main function"""
    st.subheader("🫁 Cai Máy Thở - Weaning Protocol")
    st.caption("Đánh giá sẵn sàng cai máy thở và hướng dẫn SBT")
    
    st.info("""
    **💡 Hướng dẫn:**
    - Đánh giá sẵn sàng cai máy thở dựa trên nhiều tiêu chí
    - Tính RSBI (Rapid Shallow Breathing Index)
    - Hướng dẫn SBT (Spontaneous Breathing Trial)
    """)
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📊 RSBI Calculator", "✅ Weaning Readiness", "📋 SBT Protocol"])
    
    with tab1:
        st.markdown("### 📊 RSBI Calculator")
        st.caption("Rapid Shallow Breathing Index")
        
        col1, col2 = st.columns(2)
        
        with col1:
            rr = st.number_input(
                "RR (lần/phút)",
                0, 60, 20, 1,
                format="%d",
                key="weaning_rsbi_rr",
                help="Tần số thở"
            )
            vt_ml = st.number_input(
                "Vt (mL)",
                0, 1000, 0, 10,
                format="%d",
                key="weaning_rsbi_vt",
                help="Thể tích khí lưu thông"
            )
        
        with col2:
            if vt_ml > 0:
                vt_liters = vt_ml / 1000
                rsbi = calculate_rsbi(rr, vt_liters)
                
                if rsbi:
                    interpretation, color, description = interpret_rsbi(rsbi)
                    
                    st.markdown("#### Kết quả")
                    if color == "success":
                        st.success(f"**RSBI: {rsbi:.0f}** ✓")
                    elif color == "warning":
                        st.warning(f"**RSBI: {rsbi:.0f}** ⚠️")
                    else:
                        st.error(f"**RSBI: {rsbi:.0f}** ⚠️")
                    
                    st.caption(f"{interpretation} - {description}")
                    
                    st.markdown("---")
                    st.markdown("**💡 Khuyến nghị:**")
                    if rsbi < 105:
                        st.success("✅ RSBI <105 - Có thể tiến hành cai máy thở")
                    elif rsbi < 130:
                        st.warning("⚠️ RSBI 105-130 - Cần theo dõi, có thể thử cai máy thở")
                    else:
                        st.error("❌ RSBI >130 - Khó cai máy thở, cần cải thiện trước")
            else:
                st.info("Nhập Vt để tính RSBI")
        
        with st.expander("📚 Thông tin về RSBI"):
            st.markdown("""
            **RSBI (Rapid Shallow Breathing Index):**
            - **Công thức:** RSBI = RR / Vt (L)
            - **Ý nghĩa:** Đánh giá hiệu quả thở tự nhiên
            
            **Giá trị:**
            - **<105:** Tốt - Có thể cai máy thở
            - **105-130:** Trung bình - Cần theo dõi
            - **>130:** Kém - Khó cai máy thở
            
            **Lưu ý:**
            - RSBI chỉ là một chỉ số, cần đánh giá toàn diện
            - Kết hợp với các tiêu chí khác (ABG, huyết động, etc.)
            """)
    
    with tab2:
        st.markdown("### ✅ Đánh giá Sẵn Sàng Cai Máy Thở")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 💨 ABG")
            abg_ph = st.number_input("pH", 6.8, 7.8, 7.40, 0.01, format="%.2f", key="weaning_abg_ph")
            abg_pco2 = st.number_input("PaCO₂ (mmHg)", 10.0, 100.0, 40.0, 0.1, format="%.1f", key="weaning_abg_pco2")
            abg_po2 = st.number_input("PaO₂ (mmHg)", 30.0, 600.0, 95.0, 1.0, format="%.0f", key="weaning_abg_po2")
            abg_hco3 = st.number_input("HCO₃ (mEq/L)", 5.0, 50.0, 24.0, 0.1, format="%.1f", key="weaning_abg_hco3")
            abg_fio2 = st.number_input("FiO₂ (%)", 21.0, 100.0, 40.0, 1.0, format="%.0f", key="weaning_abg_fio2")
        
        with col2:
            st.markdown("#### ⚙️ Máy Thở")
            vent_peep = st.number_input("PEEP (cmH2O)", 0, 30, 5, 1, format="%d", key="weaning_vent_peep")
            vent_fio2 = st.number_input("FiO₂ (%)", 21, 100, 40, 1, format="%d", key="weaning_vent_fio2")
            
            st.markdown("#### 💓 Sinh Tồn")
            vitals_hr = st.number_input("HR (bpm)", 0, 200, 80, 1, format="%d", key="weaning_vitals_hr")
            vitals_bp_systolic = st.number_input("SBP (mmHg)", 0, 300, 120, 1, format="%d", key="weaning_vitals_sbp")
            vitals_temp = st.number_input("Temp (°C)", 30.0, 42.0, 37.0, 0.1, format="%.1f", key="weaning_vitals_temp")
            
            st.markdown("#### 🧠 Thần kinh")
            neuro_gcs = st.number_input("GCS", 3, 15, 15, 1, format="%d", key="weaning_neuro_gcs")
        
        st.markdown("---")
        st.markdown("#### 📋 Yếu tố Khác")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            no_sepsis = st.checkbox("Không có nhiễm trùng huyết", key="weaning_no_sepsis")
            no_acidosis = st.checkbox("Không có toan máu nặng", key="weaning_no_acidosis")
        with col2:
            hemodynamically_stable = st.checkbox("Huyết động ổn định", key="weaning_hemo_stable")
        
        if st.button("🧮 Đánh giá Sẵn Sàng", type="primary", use_container_width=True):
            abg_data = {
                "ph": abg_ph,
                "pco2": abg_pco2,
                "po2": abg_po2,
                "hco3": abg_hco3,
                "fio2": abg_fio2
            }
            
            vent_settings = {
                "peep": vent_peep,
                "fio2": vent_fio2
            }
            
            vitals = {
                "hr": vitals_hr,
                "bp_systolic": vitals_bp_systolic,
                "temp": vitals_temp
            }
            
            neurological = {
                "gcs": neuro_gcs
            }
            
            other_factors = {
                "no_sepsis": no_sepsis,
                "no_acidosis": no_acidosis,
                "hemodynamically_stable": hemodynamically_stable
            }
            
            criteria, readiness, readiness_color, passed_ratio = assess_weaning_readiness(
                abg_data, vent_settings, vitals, neurological, other_factors
            )
            
            st.markdown("---")
            st.markdown("### 📊 Kết quả Đánh giá")
            
            # Overall readiness
            if readiness_color == "success":
                st.success(f"**{readiness}** - {len(criteria['passed'])}/{len(criteria['passed']) + len(criteria['failed']) + len(criteria['warnings'])} tiêu chí đạt")
            elif readiness_color == "warning":
                st.warning(f"**{readiness}** - {len(criteria['passed'])}/{len(criteria['passed']) + len(criteria['failed']) + len(criteria['warnings'])} tiêu chí đạt")
            else:
                st.error(f"**{readiness}** - {len(criteria['passed'])}/{len(criteria['passed']) + len(criteria['failed']) + len(criteria['warnings'])} tiêu chí đạt")
            
            st.markdown("---")
            
            # Passed criteria
            if criteria["passed"]:
                st.markdown("#### ✅ Tiêu chí Đạt")
                for criterion in criteria["passed"]:
                    st.success(f"✓ {criterion}")
            
            # Failed criteria
            if criteria["failed"]:
                st.markdown("#### ❌ Tiêu chí Không Đạt")
                for criterion in criteria["failed"]:
                    st.error(f"✗ {criterion}")
            
            # Warnings
            if criteria["warnings"]:
                st.markdown("#### ⚠️ Cảnh báo")
                for criterion in criteria["warnings"]:
                    st.warning(f"⚠ {criterion}")
            
            # Recommendations
            st.markdown("---")
            st.markdown("### 💡 Khuyến nghị")
            
            if readiness == "Sẵn sàng":
                st.success("""
                **Có thể tiến hành SBT (Spontaneous Breathing Trial):**
                1. Chuyển sang CPAP mode với PEEP 5-8 cmH2O
                2. Theo dõi sát trong 30-120 phút
                3. Nếu thành công, tiếp tục cai máy thở
                """)
            elif readiness == "Có thể thử":
                st.warning("""
                **Có thể thử SBT nhưng cần theo dõi chặt chẽ:**
                1. Điều chỉnh các tiêu chí chưa đạt nếu có thể
                2. Thử SBT với thời gian ngắn hơn (30 phút)
                3. Theo dõi sát và sẵn sàng quay lại thông số cũ
                """)
            else:
                st.error("""
                **Chưa sẵn sàng cai máy thở:**
                1. Điều chỉnh các tiêu chí chưa đạt
                2. Đánh giá lại sau 24-48 giờ
                3. Không nên tiến hành SBT lúc này
                """)
    
    with tab3:
        st.markdown("### 📋 SBT Protocol - Spontaneous Breathing Trial")
        
        protocol = sbt_protocol()
        
        st.info("""
        **SBT (Spontaneous Breathing Trial):**
        - Thử nghiệm thở tự nhiên để đánh giá khả năng cai máy thở
        - Thời gian: 30-120 phút
        - Theo dõi sát các dấu hiệu suy hô hấp
        """)
        
        st.markdown("---")
        
        # Steps
        for step_info in protocol["steps"]:
            st.markdown(f"#### Bước {step_info['step']}: {step_info['title']}")
            for action in step_info["actions"]:
                st.markdown(f"- {action}")
            st.markdown("---")
        
        # Success criteria
        st.markdown("#### ✅ Tiêu chí Thành Công")
        for criterion in protocol["success_criteria"]:
            st.success(f"✓ {criterion}")
        
        st.markdown("---")
        
        # Failure criteria
        st.markdown("#### ❌ Tiêu chí Thất Bại")
        for criterion in protocol["failure_criteria"]:
            st.error(f"✗ {criterion}")
        
        st.markdown("---")
        
        with st.expander("📚 Thông tin thêm"):
            st.markdown("""
            **SBT Protocol:**
            - **Mục đích:** Đánh giá khả năng thở tự nhiên của bệnh nhân
            - **Thời gian:** 30-120 phút (thường 30-60 phút)
            - **Mode:** CPAP hoặc T-piece
            
            **Lưu ý:**
            - Theo dõi sát trong suốt quá trình SBT
            - Nếu có dấu hiệu suy hô hấp, quay lại thông số cũ ngay
            - Đánh giá lại sau 24h nếu thất bại
            
            **Reference:**
            - ATS/ERS Guidelines on Weaning
            - Surviving Sepsis Campaign 2021
            """)


def render():
    """Main render function for weaning module"""
    render_weaning_calculator()

