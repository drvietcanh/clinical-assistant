"""
Sepsis Protocols and Management
Sepsis recognition (SIRS, qSOFA, Sepsis-3), management bundles, lactate monitoring
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert

# Import existing calculators
try:
    from scores.emergency.qsofa import render as render_qsofa
    from scores.infectious.sirs import render as render_sirs
    from scores.emergency.sofa import render as render_sofa
except ImportError:
    render_qsofa = None
    render_sirs = None
    render_sofa = None


def calculate_lactate_clearance(initial_lactate: float, repeat_lactate: float, hours: float = 2.0) -> dict:
    """
    Calculate lactate clearance
    
    Args:
        initial_lactate: Initial lactate level (mmol/L)
        repeat_lactate: Repeat lactate level (mmol/L)
        hours: Time between measurements (hours)
    
    Returns:
        Dictionary with lactate clearance calculation
    """
    if initial_lactate <= 0:
        return {
            "clearance_percent": None,
            "clearance_per_hour": None,
            "interpretation": None,
            "color": None
        }
    
    clearance_percent = ((initial_lactate - repeat_lactate) / initial_lactate) * 100
    clearance_per_hour = clearance_percent / hours if hours > 0 else None
    
    # Interpretation
    if clearance_percent >= 20:
        interpretation = "Tốt - Lactate clearance ≥20%"
        color = "success"
    elif clearance_percent >= 10:
        interpretation = "Trung bình - Lactate clearance 10-20%"
        color = "warning"
    else:
        interpretation = "Kém - Lactate clearance <10%"
        color = "error"
    
    return {
        "clearance_percent": clearance_percent,
        "clearance_per_hour": clearance_per_hour,
        "interpretation": interpretation,
        "color": color,
        "initial_lactate": initial_lactate,
        "repeat_lactate": repeat_lactate,
        "hours": hours
    }


def render_sepsis_recognition():
    """Render sepsis recognition tools (SIRS, qSOFA, Sepsis-3)"""
    st.subheader("🔍 Sepsis Recognition")
    st.caption("Sàng lọc và chẩn đoán sepsis")
    
    st.markdown("""
    **Sepsis-3 Definition (2016):**
    - **Sepsis:** Nhiễm trùng + SOFA ≥2
    - **Septic Shock:** Sepsis + Vasopressor (MAP ≥65) + Lactate >2 mmol/L
    
    **Screening Tools:**
    - **qSOFA:** Sàng lọc nhanh ngoài ICU (≥2 = concerning)
    - **SIRS:** Tiêu chuẩn cũ, vẫn hữu ích
    - **SOFA:** Đánh giá suy cơ quan (≥2 = sepsis)
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3 = st.tabs([
        "🔍 qSOFA",
        "🔥 SIRS",
        "📊 SOFA"
    ])
    
    with tab1:
        if render_qsofa:
            render_qsofa()
        else:
            st.error("qSOFA calculator không khả dụng")
    
    with tab2:
        if render_sirs:
            render_sirs()
        else:
            st.error("SIRS calculator không khả dụng")
    
    with tab3:
        if render_sofa:
            render_sofa()
        else:
            st.error("SOFA calculator không khả dụng")


def render_sepsis_1hour_bundle():
    """Render Sepsis 1-Hour Bundle"""
    st.subheader("⏱️ Sepsis 1-Hour Bundle")
    st.caption("Surviving Sepsis Campaign 2021")
    
    st.info("""
    **Chẩn đoán Sepsis:**
    - Nhiễm trùng (nghi ngờ hoặc xác định)
    - qSOFA ≥2 hoặc SOFA tăng ≥2 điểm
    - Rối loạn chức năng cơ quan
    
    **Septic Shock:**
    - Sepsis + MAP <65 mmHg sau truyền dịch
    - Hoặc Lactate >2 mmol/L
    """)
    
    st.markdown("---")
    
    st.markdown("### ⏱️ Sepsis 1-Hour Bundle")
    
    st.error("""
    **Thực hiện NGAY trong vòng 1 GIỜ:**
    
    1. ✅ **Đo Lactate**
       - Lactate >2 mmol/L = septic shock
       - Đo lại sau 2-4h nếu tăng
    
    2. ✅ **Cấy máu trước khi kháng sinh**
       - 2 bộ cấy máu (từ 2 vị trí khác nhau)
       - Cấy dịch từ ổ nhiễm (nếu có)
       - ⚠️ Không trì hoãn kháng sinh để chờ cấy máu
    
    3. ✅ **Kháng sinh phổ rộng**
       - Trong vòng 1 giờ
       - Theo guideline địa phương
       - Liều đủ, đường IV
    
    4. ✅ **Truyền dịch nhanh**
       - 30 mL/kg crystalloid
       - Trong 3 giờ đầu
       - Ringer Lactate hoặc Normal Saline
    
    5. ✅ **Vasopressor nếu hạ huyết áp**
       - Nếu MAP <65 mmHg sau truyền dịch
       - Norepinephrine là thuốc đầu tay
       - Mục tiêu MAP ≥65 mmHg
    """)
    
    st.markdown("---")
    
    # Checklist
    st.markdown("### ✅ Checklist 1-Hour Bundle")
    
    checklist_items = [
        ("Đo Lactate", "lactate"),
        ("Cấy máu (2 bộ)", "blood_culture"),
        ("Kháng sinh phổ rộng", "antibiotics"),
        ("Truyền dịch 30 mL/kg", "fluids"),
        ("Vasopressor nếu cần", "vasopressor")
    ]
    
    completed = {}
    for item, key in checklist_items:
        completed[key] = st.checkbox(item, key=f"sepsis_1h_{key}")
    
    if st.button("Đánh giá", type="primary", key="assess_1h_bundle"):
        completed_count = sum(completed.values())
        total = len(checklist_items)
        
        if completed_count == total:
            st.success(f"✅ **Hoàn thành {completed_count}/{total}** - Đã thực hiện đầy đủ 1-hour bundle!")
        elif completed_count >= 3:
            st.warning(f"⚠️ **Hoàn thành {completed_count}/{total}** - Cần hoàn thành các bước còn lại!")
        else:
            st.error(f"🚨 **Hoàn thành {completed_count}/{total}** - Cần thực hiện ngay các bước còn lại!")


def render_antibiotic_guide():
    """Render antibiotic selection guide"""
    st.subheader("💊 Lựa chọn kháng sinh thực nghiệm")
    st.caption("Kháng sinh phổ rộng cho sepsis")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **🏠 Nhiễm trùng cộng đồng:**
        
        **Lựa chọn 1:**
        - Ceftriaxone 2g IV q24h
        + Azithromycin 500mg IV q24h
        
        **Lựa chọn 2:**
        - Piperacillin-Tazobactam 4.5g IV q6h
        
        **Lựa chọn 3:**
        - Cefepime 2g IV q8h
        + Vancomycin (nếu nghi MRSA)
        """)
    
    with col2:
        st.warning("""
        **🏥 Nhiễm trùng bệnh viện:**
        
        **Lựa chọn 1:**
        - Piperacillin-Tazobactam 4.5g IV q6h
        + Vancomycin (nếu nghi MRSA)
        
        **Lựa chọn 2:**
        - Meropenem 1g IV q8h
        + Vancomycin
        
        **Lựa chọn 3:**
        - Ceftazidime-Avibactam 2.5g IV q8h
        (nếu nghi kháng carbapenem)
        """)
    
    st.markdown("---")
    
    st.info("""
    **💡 Lưu ý:**
    - Kháng sinh trong vòng **1 giờ** sau khi nghi sepsis
    - Liều đủ, đường **IV**
    - Điều chỉnh theo kết quả cấy máu
    - Xem xét de-escalation sau 48-72h nếu cải thiện
    - Theo guideline địa phương về kháng kháng sinh
    """)


def render_fluid_resuscitation():
    """Render fluid resuscitation protocol"""
    st.subheader("💧 Fluid Resuscitation Protocol")
    st.caption("Truyền dịch cho sepsis và septic shock")
    
    st.markdown("""
    **Surviving Sepsis Campaign 2021:**
    - Truyền dịch 30 mL/kg crystalloid trong 3 giờ đầu
    - Đánh giá đáp ứng sau mỗi bolus
    - Tránh quá tải dịch
    """)
    
    st.markdown("---")
    
    weight_kg = st.number_input(
        "Cân nặng (kg):",
        min_value=30.0,
        max_value=200.0,
        value=50.0,
        step=0.1,
        format="%.1f",
        key="sepsis_weight"
    )
    
    if st.button("Tính toán", type="primary", key="calc_fluid_sepsis"):
        total_fluid_ml = weight_kg * 30
        total_fluid_liters = total_fluid_ml / 1000
        
        st.markdown("### 📊 Kết quả")
        
        render_result_box(
            "Tổng dịch cần truyền",
            f"{total_fluid_ml:.0f} ml",
            subtitle=f"{total_fluid_liters:.2f} L (30 mL/kg)",
            color="primary",
            icon="💧"
        )
        
        st.markdown("---")
        st.info(f"""
        **💡 Khuyến nghị:**
        - **Tổng:** {total_fluid_ml:.0f} ml ({total_fluid_liters:.2f} L) trong 3 giờ đầu
        - **Bolus:** 500-1000 ml mỗi lần
        - **Đánh giá đáp ứng:** Sau mỗi bolus
        - **Dung dịch:** Ringer Lactate hoặc Normal Saline
        - **Mục tiêu:** MAP ≥65 mmHg, giảm lactate
        
        **Dấu hiệu đáp ứng:**
        - MAP tăng
        - Lactate giảm
        - Urine output tăng
        - Cải thiện tưới máu (capillary refill, mạch)
        
        **Dấu hiệu quá tải:**
        - Phù phổi
        - Tăng áp lực tĩnh mạch trung tâm
        - Khó thở
        - Cân nhắc dừng hoặc giảm tốc độ truyền
        """)


def render_lactate_monitoring():
    """Render lactate monitoring calculator"""
    st.subheader("📊 Lactate Monitoring")
    st.caption("Tính toán lactate clearance")
    
    st.markdown("""
    **Lactate Clearance:**
    - Mục tiêu: Giảm ≥20% trong 2-4 giờ đầu
    - Lactate >2 mmol/L = septic shock
    - Theo dõi serial để đánh giá đáp ứng điều trị
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        initial_lactate = st.number_input(
            "Lactate ban đầu (mmol/L):",
            min_value=0.5,
            max_value=20.0,
            value=4.0,
            step=0.1,
            format="%.1f",
            key="lactate_initial"
        )
    
    with col2:
        repeat_lactate = st.number_input(
            "Lactate lặp lại (mmol/L):",
            min_value=0.5,
            max_value=20.0,
            value=3.0,
            step=0.1,
            format="%.1f",
            key="lactate_repeat"
        )
    
    hours = st.number_input(
        "Thời gian giữa 2 lần đo (giờ):",
        min_value=0.5,
        max_value=24.0,
        value=2.0,
        step=0.5,
        format="%.1f",
        key="lactate_hours"
    )
    
    if st.button("Tính toán", type="primary", key="calc_lactate"):
        results = calculate_lactate_clearance(initial_lactate, repeat_lactate, hours)
        
        if results["clearance_percent"] is None:
            st.error("Không thể tính toán. Lactate ban đầu phải > 0.")
        else:
            st.markdown("### 📊 Kết quả")
            
            col1, col2 = st.columns(2)
            
            with col1:
                render_result_box(
                    "Lactate Clearance",
                    f"{results['clearance_percent']:.1f}%",
                    subtitle=results["interpretation"],
                    color=results["color"],
                    icon="📊"
                )
            
            with col2:
                if results["clearance_per_hour"]:
                    render_result_box(
                        "Clearance/giờ",
                        f"{results['clearance_per_hour']:.1f}%/h",
                        subtitle=f"Trong {hours:.1f} giờ",
                        color="info"
                    )
            
            st.markdown("---")
            
            # Lactate levels
            st.markdown("### 📋 Đánh giá Lactate")
            
            if initial_lactate > 2:
                st.error(f"""
                **🚨 Lactate ban đầu cao ({initial_lactate:.1f} mmol/L):**
                - Đáp ứng tiêu chuẩn **Septic Shock**
                - Cần điều trị tích cực
                - Theo dõi lactate mỗi 2-4 giờ
                """)
            else:
                st.success(f"""
                **✅ Lactate ban đầu bình thường ({initial_lactate:.1f} mmol/L):**
                - Không đáp ứng tiêu chuẩn septic shock
                - Vẫn cần theo dõi nếu nghi sepsis
                """)
            
            if results["clearance_percent"] >= 20:
                st.success("""
                **✅ Lactate Clearance Tốt (≥20%):**
                - Đáp ứng tốt với điều trị
                - Tiếp tục điều trị hiện tại
                - Theo dõi tiếp
                """)
            elif results["clearance_percent"] >= 10:
                st.warning("""
                **⚠️ Lactate Clearance Trung Bình (10-20%):**
                - Đáp ứng một phần
                - Cần đánh giá lại điều trị
                - Cân nhắc tăng cường điều trị
                """)
            else:
                st.error("""
                **🚨 Lactate Clearance Kém (<10%):**
                - Không đáp ứng với điều trị
                - Cần đánh giá lại ngay
                - Cân nhắc:
                  - Tăng cường truyền dịch
                  - Tăng liều vasopressor
                  - Đánh giá lại kháng sinh
                  - Tìm ổ nhiễm trùng
                """)


def render_sepsis_protocols():
    """Main function to render sepsis protocols"""
    
    st.markdown("## 🦠 Sepsis Protocols & Management")
    st.markdown("""
    Hướng Dẫn Quản Lý Sepsis và Septic Shock:
    - Sepsis recognition (SIRS, qSOFA, Sepsis-3)
    - 1-hour bundle checklist
    - Antibiotic selection guide
    - Fluid resuscitation protocol
    - Lactate monitoring
    """)
    
    st.markdown("---")
    
    # Check if specific tool should be opened
    tool_to_open = st.session_state.get('sepsis_tool_to_open', None)
    default_tab = 0
    
    if tool_to_open:
        tool_tab_map = {
            'lactate': 4,
            'fluid': 3,
            'protocols': 1
        }
        default_tab = tool_tab_map.get(tool_to_open, 0)
        # Clear after using
        if 'sepsis_tool_to_open' in st.session_state:
            del st.session_state['sepsis_tool_to_open']
    
    # Tab selection
    tab_labels = [
        "🔍 Recognition",
        "⏱️ 1-Hour Bundle",
        "💊 Antibiotics",
        "💧 Fluid Resuscitation",
        "📊 Lactate Monitoring"
    ]
    if default_tab is not None and 0 <= default_tab < len(tab_labels):
        tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_labels, selected=default_tab)
    else:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_labels)
    
    with tab1:
        render_sepsis_recognition()
    
    with tab2:
        render_sepsis_1hour_bundle()
    
    with tab3:
        render_antibiotic_guide()
    
    with tab4:
        render_fluid_resuscitation()
    
    with tab5:
        render_lactate_monitoring()
    
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - Các tính toán này chỉ mục đích hỗ trợ quyết định lâm sàng
    - Luôn đánh giá lâm sàng và điều chỉnh theo đáp ứng của bệnh nhân
    - Tuân thủ hướng dẫn của Bộ Y tế, Bệnh viện
    - Surviving Sepsis Campaign 2021 guidelines
    """)

