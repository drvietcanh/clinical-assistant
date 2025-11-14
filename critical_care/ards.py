"""
ARDS (Acute Respiratory Distress Syndrome) Protocols
ARDSNet protocol calculator, PEEP/FiO2 table, ventilator settings
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert
from .ventilator import calculate_ibw, calculate_tidal_volume, get_peep_fio2_table, recommend_peep


def classify_ards_severity(pf_ratio: float) -> dict:
    """
    Classify ARDS severity based on P/F ratio
    
    Args:
        pf_ratio: PaO2/FiO2 ratio (mmHg)
    
    Returns:
        Dictionary with ARDS classification
    """
    if pf_ratio >= 300:
        return {
            "severity": "Mild ARDS",
            "pf_range": "≥300",
            "color": "info",
            "icon": "ℹ️"
        }
    elif pf_ratio >= 200:
        return {
            "severity": "Moderate ARDS",
            "pf_range": "200-299",
            "color": "warning",
            "icon": "⚠️"
        }
    elif pf_ratio >= 100:
        return {
            "severity": "Severe ARDS",
            "pf_range": "100-199",
            "color": "error",
            "icon": "🚨"
        }
    else:
        return {
            "severity": "Very Severe ARDS",
            "pf_range": "<100",
            "color": "error",
            "icon": "🚨"
        }


def calculate_ardsnet_settings(ibw_kg: float, pf_ratio: float, current_fio2: float = 0.5) -> dict:
    """
    Calculate ARDSNet protocol ventilator settings
    
    Args:
        ibw_kg: Ideal Body Weight in kg
        pf_ratio: PaO2/FiO2 ratio
        current_fio2: Current FiO2 (decimal)
    
    Returns:
        Dictionary with recommended settings
    """
    # Tidal volume: 6 ml/kg IBW
    vt_results = calculate_tidal_volume(ibw_kg, 6.0)
    
    # PEEP recommendation based on FiO2
    peep_rec = recommend_peep(current_fio2)
    
    # ARDS severity
    ards_class = classify_ards_severity(pf_ratio)
    
    return {
        "vt_ml": vt_results["vt_ml"],
        "vt_liters": vt_results["vt_liters"],
        "peep_recommended": peep_rec["peep_recommended"],
        "peep_range": f"{peep_rec['peep_min']}-{peep_rec['peep_max']}",
        "fio2_recommended": current_fio2,
        "ards_severity": ards_class["severity"],
        "pf_ratio": pf_ratio,
        "ibw_kg": ibw_kg
    }


def render_ardsnet_calculator():
    """Render ARDSNet protocol calculator"""
    st.subheader("🫁 ARDSNet Protocol Calculator")
    st.caption("Tính toán cài đặt máy thở theo ARDSNet protocol")
    
    st.markdown("""
    **ARDSNet Protocol (2000):** Lung-protective ventilation strategy
    - Tidal volume: **6 ml/kg IBW** (không dùng actual body weight)
    - Plateau pressure: **< 30 cmH2O**
    - PEEP/FiO2: Theo bảng ARDSNet
    - Target SpO2: **88-95%** hoặc PaO2: **55-80 mmHg**
    """)
    
    st.markdown("---")
    
    # Patient info
    st.markdown("### 📋 Thông Tin Bệnh Nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sex = st.radio(
            "Giới tính:",
            ["Nam", "Nữ"],
            horizontal=True,
            key="ards_sex"
        )
    
    with col2:
        height_cm = st.number_input(
            "Chiều cao (cm):",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            step=0.1,
            key="ards_height"
        )
    
    # Calculate IBW
    ibw = calculate_ibw(sex, height_cm)
    
    st.info(f"**Ideal Body Weight (IBW):** {ibw:.1f} kg")
    
    st.markdown("---")
    
    # ABG/SpO2
    st.markdown("### 🩺 Thông Số Oxy Hóa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        has_abg = st.checkbox("Có ABG (PaO2)", key="ards_has_abg")
        
        if has_abg:
            pao2 = st.number_input(
                "PaO2 (mmHg):",
                min_value=30.0,
                max_value=600.0,
                value=100.0,
                step=1.0,
                key="ards_pao2"
            )
        else:
            pao2 = None
    
    with col2:
        fio2 = st.slider(
            "FiO₂ (%):",
            min_value=30,
            max_value=100,
            value=50,
            step=5,
            key="ards_fio2"
        )
        fio2_decimal = fio2 / 100
    
    # Calculate P/F ratio
    if has_abg and pao2:
        pf_ratio = pao2 / fio2_decimal
    else:
        pf_ratio = None
        st.warning("Nhập PaO2 để tính P/F ratio và phân loại ARDS")
    
    st.markdown("---")
    
    if st.button("Tính toán ARDSNet", type="primary", key="calc_ardsnet"):
        if pf_ratio is None:
            st.error("Cần nhập PaO2 để tính toán")
        else:
            # Calculate settings
            settings = calculate_ardsnet_settings(ibw, pf_ratio, fio2_decimal)
            ards_class = classify_ards_severity(pf_ratio)
            
            st.markdown("### 📊 Kết Quả")
            
            # ARDS Classification
            st.markdown("#### 🏷️ Phân Loại ARDS")
            render_result_box(
                "ARDS Severity",
                ards_class["severity"],
                subtitle=f"P/F ratio: {pf_ratio:.0f} mmHg ({ards_class['pf_range']})",
                color=ards_class["color"],
                icon=ards_class["icon"]
            )
            
            st.markdown("---")
            
            # Ventilator Settings
            st.markdown("#### ⚙️ Cài Đặt Máy Thở (ARDSNet)")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                render_result_box(
                    "Tidal Volume",
                    f"{settings['vt_ml']:.0f} ml",
                    subtitle=f"{settings['vt_liters']:.2f} L (6 ml/kg IBW)",
                    color="primary",
                    icon="💨"
                )
            
            with col2:
                render_result_box(
                    "PEEP",
                    f"{settings['peep_recommended']:.0f} cmH2O",
                    subtitle=f"Range: {settings['peep_range']} cmH2O",
                    color="info",
                    icon="📊"
                )
            
            with col3:
                render_result_box(
                    "FiO₂",
                    f"{fio2}%",
                    subtitle="Theo bảng PEEP/FiO2",
                    color="info"
                )
            
            st.markdown("---")
            
            # Recommendations
            st.markdown("#### 💡 Khuyến Nghị")
            
            recommendations = []
            
            # Tidal volume
            recommendations.append({
                "title": "Tidal Volume",
                "value": f"{settings['vt_ml']:.0f} ml",
                "description": f"6 ml/kg IBW (IBW = {ibw:.1f} kg)"
            })
            
            # PEEP
            recommendations.append({
                "title": "PEEP",
                "value": f"{settings['peep_recommended']:.0f} cmH2O",
                "description": f"FiO2 {fio2}% → PEEP {settings['peep_range']} cmH2O"
            })
            
            # Plateau pressure
            recommendations.append({
                "title": "Plateau Pressure",
                "value": "< 30 cmH2O",
                "description": "Mục tiêu: < 30 cmH2O (lung-protective)"
            })
            
            # Target oxygenation
            recommendations.append({
                "title": "Target SpO2/PaO2",
                "value": "88-95% / 55-80 mmHg",
                "description": "Điều chỉnh PEEP/FiO2 để đạt mục tiêu"
            })
            
            render_result_card("Khuyến Nghị ARDSNet", recommendations, color="info")
            
            st.markdown("---")
            
            # Additional recommendations based on severity
            if ards_class["severity"] == "Severe ARDS" or ards_class["severity"] == "Very Severe ARDS":
                st.warning("""
                **⚠️ ARDS Nặng - Cân Nhắc:**
                1. **Prone positioning:** 16-18 giờ/ngày (nếu P/F < 150)
                2. **Neuromuscular blockade:** Nếu cần (ví dụ: cisatracurium)
                3. **ECMO:** Nếu không đáp ứng với điều trị thông thường
                4. **Recruitment maneuver:** Cẩn thận, có thể gây hại
                5. **Corticosteroids:** Cân nhắc nếu ARDS do COVID-19
                """)
            
            st.info("""
            **📋 Checklist ARDSNet:**
            - ✅ Tidal volume: 6 ml/kg IBW
            - ✅ Plateau pressure: < 30 cmH2O
            - ✅ PEEP/FiO2: Theo bảng ARDSNet
            - ✅ Target SpO2: 88-95% hoặc PaO2: 55-80 mmHg
            - ✅ Theo dõi huyết động khi tăng PEEP
            - ✅ Đánh giá lại sau 30 phút
            """)


def render_peep_fio2_table():
    """Render PEEP/FiO2 table"""
    st.subheader("📊 ARDSNet PEEP/FiO2 Table")
    st.caption("Bảng khuyến nghị PEEP dựa trên FiO2")
    
    st.markdown("""
    **Mục tiêu oxy hóa:**
    - SpO2: **88-95%**
    - PaO2: **55-80 mmHg**
    """)
    
    st.markdown("---")
    
    # Display table
    table = get_peep_fio2_table()
    
    st.markdown("### 📋 Bảng PEEP/FiO2")
    
    for entry in table:
        st.markdown(f"""
        <div style="padding: 10px; margin: 5px 0; background: #f8f9fa; border-left: 4px solid #3b82f6; border-radius: 4px;">
            <strong>FiO₂ {entry['FiO2']*100:.0f}%:</strong> PEEP {entry['PEEP_min']}-{entry['PEEP_max']} cmH2O
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 💡 Hướng Dẫn Sử Dụng")
    
    st.success("""
    **Cách điều chỉnh:**
    
    1. **Nếu SpO2 < 88% hoặc PaO2 < 55 mmHg:**
       - Tăng FiO2 và PEEP theo bảng (đi xuống)
       - Ví dụ: Từ FiO2 40%/PEEP 8 → FiO2 50%/PEEP 10
    
    2. **Nếu SpO2 > 95% hoặc PaO2 > 80 mmHg:**
       - Giảm FiO2 và PEEP theo bảng (đi lên)
       - Ưu tiên giảm FiO2 trước
    
    3. **Điều chỉnh từng bước:**
       - Không nhảy cóc
       - Theo dõi sau mỗi thay đổi
       - Đợi ít nhất 30 phút trước khi đánh giá lại
    """)
    
    st.warning("""
    **⚠️ Lưu ý:**
    - PEEP tối đa: 24 cmH2O
    - Luôn kiểm tra Plateau Pressure ≤ 30 cmH2O
    - Theo dõi huyết động sau khi tăng PEEP
    - Cân nhắc recruitment maneuver nếu PEEP cao
    """)


def render_prone_positioning_guide():
    """Render prone positioning guide"""
    st.subheader("🔄 Prone Positioning Guide")
    st.caption("Hướng dẫn nằm sấp cho ARDS nặng")
    
    st.markdown("""
    **Prone positioning** được khuyến nghị cho ARDS nặng (P/F ratio < 150) để cải thiện oxy hóa.
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Chỉ Định")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **✅ Chỉ định:**
        - ARDS nặng (P/F ratio < 150)
        - FiO2 ≥ 60% và PEEP ≥ 10 cmH2O
        - Không đáp ứng với điều trị thông thường
        """)
    
    with col2:
        st.error("""
        **❌ Chống chỉ định:**
        - Gãy cột sống không ổn định
        - Tăng áp lực nội sọ
        - Shock nặng không ổn định
        - Vừa phẫu thuật bụng
        """)
    
    st.markdown("---")
    
    st.markdown("### ⏱️ Thời Gian")
    
    st.info("""
    **Thời gian nằm sấp:**
    - **16-18 giờ/ngày** (khuyến nghị)
    - Có thể chia thành 2-3 lần
    - Nằm ngửa 2-4 giờ giữa các lần
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Trước Khi Nằm Sấp")
    
    checklist = [
        "Kiểm tra đường thở (ETT cố định chắc chắn)",
        "Kiểm tra tất cả đường truyền (IV, arterial line, etc.)",
        "Đảm bảo an toàn (giảm nguy cơ decubitus)",
        "Chuẩn bị đệm, gối hỗ trợ",
        "Kiểm tra huyết động ổn định",
        "Thông báo cho gia đình"
    ]
    
    for item in checklist:
        st.markdown(f"- ✅ {item}")
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Theo Dõi")
    
    st.warning("""
    **Theo dõi trong khi nằm sấp:**
    - SpO2, PaO2 (ABG sau 1-2 giờ)
    - Huyết động (MAP, HR)
    - Vị trí ETT (có thể bị di chuyển)
    - Áp lực đường thở (plateau pressure)
    - Tình trạng da (decubitus)
    """)


def render_ards_protocols():
    """Main function to render ARDS protocols"""
    
    st.markdown("## 🫁 ARDS Protocols")
    st.markdown("""
    Hướng dẫn quản lý ARDS (Acute Respiratory Distress Syndrome):
    - ARDSNet protocol calculator
    - PEEP/FiO2 table
    - Prone positioning guide
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3 = st.tabs([
        "🫁 ARDSNet Calculator",
        "📊 PEEP/FiO2 Table",
        "🔄 Prone Positioning"
    ])
    
    with tab1:
        render_ardsnet_calculator()
    
    with tab2:
        render_peep_fio2_table()
    
    with tab3:
        render_prone_positioning_guide()
    
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - Các tính toán này chỉ mục đích hỗ trợ quyết định lâm sàng
    - Luôn đánh giá lâm sàng và điều chỉnh theo đáp ứng của bệnh nhân
    - Tuân thủ hướng dẫn địa phương và quy định bệnh viện
    - ARDSNet protocol dựa trên nghiên cứu năm 2000, có thể có cập nhật mới
    """)

