"""
Universal Antibiotic Dosing Calculator
Tính liều kháng sinh tự động dựa trên eGFR/CrCl cho bất kỳ kháng sinh nào
"""

import streamlit as st
from .antibiotics_data import ANTIBIOTICS_DATABASE


def get_renal_category(crcl, egfr=None):
    """
    Determine renal function category based on CrCl or eGFR
    
    Returns: 'normal', '30_60', '15_30', 'under_15', 'hemodialysis'
    """
    if crcl is None or crcl <= 0:
        return 'normal'
    
    if crcl >= 60:
        return 'normal'
    elif crcl >= 30:
        return '30_60'
    elif crcl >= 15:
        return '15_30'
    else:
        return 'under_15'


def calculate_adjusted_dose(antibiotic_name, crcl, egfr=None, base_dose=None, indication="standard"):
    """
    Calculate adjusted antibiotic dose based on renal function
    
    Args:
        antibiotic_name: Name of antibiotic from database
        crcl: Creatinine clearance (mL/min)
        egfr: eGFR (optional, for reference)
        base_dose: Base dose if not in database (e.g., custom dosing)
        indication: Type of infection (standard, severe, meningitis, etc.)
    
    Returns:
        dict with adjusted dose information
    """
    if antibiotic_name not in ANTIBIOTICS_DATABASE:
        return {
            "error": f"Kháng sinh '{antibiotic_name}' không có trong database",
            "recommendation": "Vui lòng tra cứu hướng dẫn riêng"
        }
    
    ab_data = ANTIBIOTICS_DATABASE[antibiotic_name]
    renal_category = get_renal_category(crcl, egfr)
    
    # Get base dosage information
    dosage = ab_data.get('dosage', {})
    renal_adj = ab_data.get('renal_adjustment', {})
    
    # Determine base dose based on indication
    if indication == "severe" and 'adult_iv_severe' in dosage:
        base_info = dosage['adult_iv_severe']
    elif indication == "meningitis" and 'meningitis_iv' in dosage:
        base_info = dosage['meningitis_iv']
    elif 'adult_iv' in dosage:
        base_info = dosage['adult_iv']
    elif 'adult_standard' in dosage:
        base_info = dosage['adult_standard']
    elif 'adult_im' in dosage:
        base_info = dosage['adult_im']
    else:
        base_info = "Liều chuẩn theo hướng dẫn"
    
    # Get renal adjustment recommendation
    if renal_category in renal_adj:
        adjustment_text = renal_adj[renal_category]
    elif renal_category == 'normal':
        adjustment_text = renal_adj.get('normal', 'Không đổi')
    else:
        adjustment_text = "Tham khảo hướng dẫn cụ thể"
    
    # Additional notes
    notes = dosage.get('notes', '')
    monitoring = ab_data.get('monitoring', '')
    
    return {
        "antibiotic": antibiotic_name,
        "base_dose": base_info,
        "renal_category": renal_category,
        "crcl": crcl,
        "egfr": egfr,
        "adjustment": adjustment_text,
        "recommended_dose": adjustment_text,
        "notes": notes,
        "monitoring": monitoring,
        "full_renal_guide": renal_adj
    }


def render_dosing_calculator():
    """Universal antibiotic dosing calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🧮 Tính Liều Kháng Sinh Theo eGFR/CrCl</h2>
    <p style='text-align: center;'><em>Công cụ tính liều tự động cho tất cả kháng sinh dựa trên chức năng thận</em></p>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Công cụ này:**
    - ✅ Tự động tính liều dựa trên CrCl/eGFR
    - ✅ Áp dụng cho tất cả kháng sinh trong database
    - ✅ Hiển thị điều chỉnh theo từng mức chức năng thận
    - ✅ Tích hợp với eGFR calculator
    """)
    
    st.markdown("---")
    
    # Patient information
    st.markdown("### 📋 Thông Số Bệnh Nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=1,
            max_value=120,
            value=65,
            step=1,
            key="dosing_age"
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=10.0,
            max_value=200.0,
            value=70.0,
            step=1.0,
            key="dosing_weight"
        )
        
        height = st.number_input(
            "Chiều cao (cm)",
            min_value=50,
            max_value=220,
            value=170,
            step=1,
            key="dosing_height"
        )
    
    with col2:
        sex = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            key="dosing_sex"
        )
        
        # Creatinine
        st.markdown("#### Creatinine Máu")
        scr_unit = st.radio(
            "Đơn vị:",
            ["µmol/L", "mg/dL"],
            horizontal=True,
            index=0,
            key="dosing_scr_unit"
        )
        
        if scr_unit == "µmol/L":
            scr_value = st.number_input(
                "Creatinine (µmol/L)",
                min_value=10.0,
                max_value=1500.0,
                value=88.0,
                step=5.0,
                key="dosing_scr_umol"
            )
            scr_mgdl = scr_value / 88.4
            st.caption(f"≈ {scr_mgdl:.1f} mg/dL")
        else:
            scr_mgdl = st.number_input(
                "Creatinine (mg/dL)",
                min_value=0.1,
                max_value=15.0,
                value=1.0,
                step=0.1,
                key="dosing_scr_mgdl"
            )
            st.caption(f"≈ {scr_mgdl * 88.4:.0f} µmol/L")
    
    st.markdown("---")
    
    # Calculate CrCl
    if sex == "Nam":
        crcl = ((140 - age) * weight) / (72 * scr_mgdl)
    else:
        crcl = ((140 - age) * weight) / (72 * scr_mgdl) * 0.85
    
    crcl = round(crcl, 1)
    
    # Calculate eGFR (simplified CKD-EPI)
    if sex == "Nam":
        if scr_mgdl <= 0.9:
            egfr = 141 * ((scr_mgdl / 0.9) ** -0.411) * (0.993 ** age)
        else:
            egfr = 141 * ((scr_mgdl / 0.9) ** -1.209) * (0.993 ** age)
    else:
        if scr_mgdl <= 0.7:
            egfr = 144 * ((scr_mgdl / 0.7) ** -0.329) * (0.993 ** age)
        else:
            egfr = 144 * ((scr_mgdl / 0.7) ** -1.209) * (0.993 ** age)
    
    egfr = round(egfr, 1)
    
    # Display renal function
    col1, col2 = st.columns(2)
    with col1:
        st.metric("CrCl (Cockcroft-Gault)", f"{crcl:.1f} mL/min", help="Ưu tiên dùng cho điều chỉnh liều thuốc")
    with col2:
        st.metric("eGFR (CKD-EPI)", f"{egfr:.1f} mL/min/1.73m²", help="Dùng cho phân loại CKD")
    
    # Renal function category
    renal_category = get_renal_category(crcl, egfr)
    category_labels = {
        'normal': '✅ Bình thường (CrCl ≥ 60)',
        '30_60': '⚠️ Suy thận nhẹ-vừa (CrCl 30-59)',
        '15_30': '🔴 Suy thận nặng (CrCl 15-29)',
        'under_15': '🚨 Suy thận rất nặng (CrCl < 15)',
        'hemodialysis': '💉 Đang lọc máu'
    }
    
    category_colors = {
        'normal': '🟢',
        '30_60': '🟡',
        '15_30': '🟠',
        'under_15': '🔴',
        'hemodialysis': '🔵'
    }
    
    st.info(f"{category_colors.get(renal_category, '')} **{category_labels.get(renal_category, 'Chưa xác định')}**")
    
    st.markdown("---")
    
    # Antibiotic selection
    st.markdown("### 💊 Chọn Kháng Sinh")
    
    all_antibiotics = sorted(list(ANTIBIOTICS_DATABASE.keys()))
    selected_ab = st.selectbox(
        "Kháng sinh:",
        all_antibiotics,
        format_func=lambda x: x,
        key="dosing_antibiotic"
    )
    
    # Indication
    indication = st.selectbox(
        "Chỉ định:",
        ["Chuẩn", "Nhiễm khuẩn nặng", "Viêm màng não", "Viêm nội tâm mạc"],
        key="dosing_indication"
    )
    
    indication_map = {
        "Chuẩn": "standard",
        "Nhiễm khuẩn nặng": "severe",
        "Viêm màng não": "meningitis",
        "Viêm nội tâm mạc": "endocarditis"
    }
    
    indication_code = indication_map.get(indication, "standard")
    
    st.markdown("---")
    
    # Calculate dose
    if st.button("🧮 Tính Liều", type="primary", use_container_width=True):
        result = calculate_adjusted_dose(
            selected_ab,
            crcl,
            egfr,
            indication=indication_code
        )
        
        if "error" in result:
            st.error(result["error"])
            st.info(result["recommendation"])
        else:
            ab_data = ANTIBIOTICS_DATABASE[selected_ab]
            
            # Display antibiotic info
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #0EA5E9 0%, #0288D1 100%); color: white; padding: 20px; border-radius: 15px; margin: 20px 0;'>
                <h2 style='margin: 0; color: white;'>💊 {selected_ab}</h2>
                {f"<p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9);'>{ab_data.get('vietnamese_name', '')}</p>" if ab_data.get('vietnamese_name') else ""}
            </div>
            """, unsafe_allow_html=True)
            
            # Base dose
            st.markdown("### 📊 Liều Chuẩn (Chức năng thận bình thường):")
            st.info(f"**{result['base_dose']}**")
            
            if result.get('notes'):
                st.caption(f"💡 {result['notes']}")
            
            st.markdown("---")
            
            # Renal adjustment
            st.markdown("### 🫘 Điều Chỉnh Theo Chức Năng Thận:")
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown(f"""
                **CrCl hiện tại:** {crcl:.1f} mL/min
                
                **Phân loại:** {category_labels.get(renal_category, 'Chưa xác định')}
                """)
            
            with col2:
                st.success(f"""
                **Khuyến cáo điều chỉnh:**
                
                {result['adjustment']}
                """)
            
            # Full renal adjustment table
            st.markdown("---")
            st.markdown("### 📋 Bảng Điều Chỉnh Đầy Đủ:")
            
            renal_guide = result.get('full_renal_guide', {})
            if renal_guide:
                renal_table = {
                    "Chức năng thận": [],
                    "CrCl (mL/min)": [],
                    "Điều chỉnh liều": []
                }
                
                if 'normal' in renal_guide:
                    renal_table["Chức năng thận"].append("Bình thường")
                    renal_table["CrCl (mL/min)"].append("≥ 60")
                    renal_table["Điều chỉnh liều"].append(renal_guide['normal'])
                
                if '30_60' in renal_guide:
                    renal_table["Chức năng thận"].append("Suy thận nhẹ-vừa")
                    renal_table["CrCl (mL/min)"].append("30-59")
                    renal_table["Điều chỉnh liều"].append(renal_guide['30_60'])
                
                if '15_30' in renal_guide:
                    renal_table["Chức năng thận"].append("Suy thận nặng")
                    renal_table["CrCl (mL/min)"].append("15-29")
                    renal_table["Điều chỉnh liều"].append(renal_guide['15_30'])
                
                if 'under_15' in renal_guide:
                    renal_table["Chức năng thận"].append("Suy thận rất nặng")
                    renal_table["CrCl (mL/min)"].append("< 15")
                    renal_table["Điều chỉnh liều"].append(renal_guide['under_15'])
                
                if 'hemodialysis' in renal_guide:
                    renal_table["Chức năng thận"].append("Lọc máu")
                    renal_table["CrCl (mL/min)"].append("HD")
                    renal_table["Điều chỉnh liều"].append(renal_guide['hemodialysis'])
                
                import pandas as pd
                df_renal = pd.DataFrame(renal_table)
                st.dataframe(df_renal, use_container_width=True, hide_index=True)
            
            # Monitoring
            if result.get('monitoring'):
                st.markdown("---")
                st.warning(f"**📊 Theo dõi:** {result['monitoring']}")
            
            # Side effects reminder
            if ab_data.get('side_effects'):
                st.markdown("---")
                with st.expander("⚠️ Tác dụng phụ quan trọng"):
                    for se in ab_data['side_effects'][:3]:  # Show top 3
                        st.markdown(f"- {se}")
            
            # Link to full antibiotic info
            st.markdown("---")
            st.info("💡 **Xem thông tin đầy đủ:** Tra cứu kháng sinh này để xem chỉ định, chống chỉ định, tương tác thuốc chi tiết")
    
    # Integration with eGFR calculator
    st.markdown("---")
    st.info("""
    **🔗 Tích hợp với eGFR Calculator:**
    - Tính eGFR/GFR đầy đủ với nhiều công thức tại trang **Calculators** → **eGFR/GFR Calculator**
    - Tự động chuyển đổi giữa eGFR chuẩn hóa và GFR tuyệt đối
    - Hỗ trợ tính BSA và điều chỉnh cho bệnh nhân béo phì/gầy
    """)

