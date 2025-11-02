"""
Multi-Antibiotic Dosing Comparison
So sánh liều dùng của nhiều kháng sinh cùng lúc
"""

import streamlit as st
import pandas as pd
from .antibiotics_data import ANTIBIOTICS_DATABASE
from .dosing_calculator import (
    calculate_adjusted_dose, 
    calculate_detailed_dose,
    check_warnings,
    get_renal_category,
    calculate_ibw,
    calculate_abw,
    calculate_bmi
)


def render_multi_comparison():
    """Compare multiple antibiotics side by side"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🔬 So Sánh Liều Nhiều Kháng Sinh</h2>
    <p style='text-align: center;'><em>So sánh liều dùng và điều chỉnh của nhiều kháng sinh cùng lúc</em></p>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Công cụ này giúp:**
    - ✅ So sánh liều của nhiều kháng sinh cùng lúc
    - ✅ Xem điều chỉnh theo chức năng thận
    - ✅ Phát hiện tương tác thuốc khi phối hợp
    - ✅ Chọn kháng sinh phù hợp nhất
    """)
    
    st.markdown("---")
    
    # Patient info (simplified - reuse from main calculator if available)
    st.markdown("### 📋 Thông Số Bệnh Nhân (Tóm Tắt)")
    
    # Try to get from session state first
    patient_crcl = st.session_state.get('patient_crcl', None)
    patient_egfr = st.session_state.get('patient_egfr', None)
    
    if patient_crcl:
        st.success(f"📥 **Đã có CrCl/eGFR từ calculator:** CrCl = {patient_crcl:.1f} mL/min | eGFR = {patient_egfr:.1f} mL/min/1.73m²")
        use_session = st.checkbox("Sử dụng giá trị từ calculator", value=True, key="multi_use_session")
        
        if use_session:
            crcl = patient_crcl
            egfr = patient_egfr
        else:
            # Manual input
            col1, col2 = st.columns(2)
            with col1:
                crcl = st.number_input("CrCl (mL/min)", min_value=0.0, max_value=200.0, value=float(patient_crcl), step=1.0, key="multi_crcl")
            with col2:
                egfr = st.number_input("eGFR (mL/min/1.73m²)", min_value=0.0, max_value=200.0, value=float(patient_egfr), step=1.0, key="multi_egfr")
    else:
        col1, col2 = st.columns(2)
        with col1:
            crcl = st.number_input("CrCl (mL/min)", min_value=0.0, max_value=200.0, value=70.0, step=1.0, key="multi_crcl")
        with col2:
            egfr = st.number_input("eGFR (mL/min/1.73m²)", min_value=0.0, max_value=200.0, value=70.0, step=1.0, key="multi_egfr")
    
    # Weight for dose calculation
    weight = st.number_input("Cân nặng (kg) - để tính liều cụ thể", min_value=10.0, max_value=200.0, value=70.0, step=1.0, key="multi_weight")
    height = st.number_input("Chiều cao (cm) - để tính IBW/ABW", min_value=50, max_value=220, value=170, step=1, key="multi_height")
    sex = st.radio("Giới tính", ["Nam", "Nữ"], horizontal=True, key="multi_sex")
    
    # Calculate IBW/ABW
    ibw = calculate_ibw(height, sex)
    bmi = calculate_bmi(weight, height)
    is_obese = bmi > 30 or weight > ibw * 1.25
    abw = calculate_abw(weight, ibw) if is_obese else weight
    
    st.markdown("---")
    
    # Select antibiotics
    st.markdown("### 💊 Chọn Kháng Sinh Để So Sánh")
    
    all_antibiotics = sorted(list(ANTIBIOTICS_DATABASE.keys()))
    
    # Multi-select antibiotics
    selected_antibiotics = st.multiselect(
        "Chọn kháng sinh (có thể chọn nhiều):",
        all_antibiotics,
        default=[],
        key="multi_selected_ab",
        help="Chọn từ 2-5 kháng sinh để so sánh"
    )
    
    if len(selected_antibiotics) == 0:
        st.info("👆 Chọn ít nhất 1 kháng sinh để bắt đầu so sánh")
        st.markdown("---")
        st.markdown("### 💡 Gợi Ý Các Phối Hợp Thường Dùng:")
        
        suggestions = {
            "Phối hợp MRSA": ["Vancomycin", "Piperacillin-Tazobactam"],
            "Phối hợp Pseudomonas": ["Piperacillin-Tazobactam", "Ciprofloxacin"],
            "Phối hợp Nhiễm Khuẩn Huyết": ["Vancomycin", "Meropenem"],
            "Phối hợp Viêm Phổi": ["Ceftriaxone", "Azithromycin"],
            "Phối hợp Độc Thận (CẨN THẬN)": ["Vancomycin", "Gentamicin"]
        }
        
        for combo_name, combo_abs in suggestions.items():
            if st.button(f"📋 {combo_name}: {', '.join(combo_abs)}", key=f"suggest_{combo_name}", use_container_width=True):
                st.session_state['multi_selected_ab'] = combo_abs
                st.rerun()
        return
    
    if len(selected_antibiotics) > 5:
        st.warning("⚠️ Chọn quá nhiều kháng sinh (max 5). Sẽ chỉ hiển thị 5 kháng sinh đầu tiên.")
        selected_antibiotics = selected_antibiotics[:5]
    
    # Indication
    indication = st.selectbox(
        "Chỉ định:",
        ["Chuẩn", "Nhiễm khuẩn nặng", "Viêm màng não", "Viêm nội tâm mạc"],
        key="multi_indication"
    )
    
    indication_map = {
        "Chuẩn": "standard",
        "Nhiễm khuẩn nặng": "severe",
        "Viêm màng não": "meningitis",
        "Viêm nội tâm mạc": "endocarditis"
    }
    indication_code = indication_map.get(indication, "standard")
    
    st.markdown("---")
    
    # Calculate for all selected antibiotics
    if st.button("🔬 So Sánh Kháng Sinh", type="primary", use_container_width=True):
        renal_category = get_renal_category(crcl, egfr)
        
        # Prepare comparison data
        comparison_data = []
        
        for ab_name in selected_antibiotics:
            if ab_name not in ANTIBIOTICS_DATABASE:
                continue
            
            ab_data = ANTIBIOTICS_DATABASE[ab_name]
            
            # Get dosing info
            result = calculate_adjusted_dose(ab_name, crcl, egfr, indication=indication_code)
            detailed = calculate_detailed_dose(ab_name, weight, ibw, abw, crcl, indication_code, is_pediatric=False)
            warnings_list = check_warnings(ab_name, crcl, 65, other_drugs=selected_antibiotics)
            
            # Calculate warnings count
            high_warnings = len([w for w in warnings_list if w['level'] == 'high'])
            medium_warnings = len([w for w in warnings_list if w['level'] == 'medium'])
            
            comparison_data.append({
                "Kháng sinh": ab_name,
                "Nhóm": ab_data.get('group', ''),
                "Đường dùng": ", ".join(ab_data.get('administration', [])),
                "Liều chuẩn": result.get('base_dose', 'N/A'),
                "Điều chỉnh (CrCl)": result.get('adjustment', 'N/A'),
                "Liều tính (mg)": f"{detailed['calculated_dose_mg']:.0f}" if detailed and detailed.get('calculated_dose_mg') else "N/A",
                "Khoảng cách (h)": f"{detailed['interval_hours']:.0f}" if detailed and detailed.get('interval_hours') else "N/A",
                "Cảnh báo cao": high_warnings,
                "Cảnh báo trung bình": medium_warnings,
                "AWaRe": ab_data.get('aware_classification', ''),
                "Pregnancy": ab_data.get('pregnancy', '')
            })
        
        # Display comparison table
        st.markdown("### 📊 Bảng So Sánh")
        
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Detailed comparison cards
        st.markdown("---")
        st.markdown("### 📋 Chi Tiết Từng Kháng Sinh:")
        
        cols = st.columns(min(len(selected_antibiotics), 3))
        
        for idx, ab_name in enumerate(selected_antibiotics):
            col_idx = idx % 3
            with cols[col_idx]:
                ab_data = ANTIBIOTICS_DATABASE[ab_name]
                result = calculate_adjusted_dose(ab_name, crcl, egfr, indication=indication_code)
                detailed = calculate_detailed_dose(ab_name, weight, ibw, abw, crcl, indication_code, is_pediatric=False)
                warnings_list = check_warnings(ab_name, crcl, 65, other_drugs=selected_antibiotics)
                
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #0EA5E9 0%, #0288D1 100%); color: white; padding: 15px; border-radius: 10px; margin: 10px 0;'>
                    <h3 style='margin: 0; color: white; font-size: 1.2em;'>💊 {ab_name}</h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Base dose
                st.markdown(f"**Liều chuẩn:** {result.get('base_dose', 'N/A')}")
                
                # Adjusted dose
                st.markdown(f"**Điều chỉnh:** {result.get('adjustment', 'N/A')}")
                
                # Detailed dose
                if detailed and detailed.get('calculated_dose_mg'):
                    st.markdown(f"**Liều tính:** {detailed['calculated_dose_mg']:.0f} mg")
                    if detailed.get('interval_hours'):
                        st.markdown(f"**Mỗi:** {detailed['interval_hours']:.0f} giờ")
                
                # Warnings
                if warnings_list:
                    high_w = [w for w in warnings_list if w['level'] == 'high']
                    if high_w:
                        st.error(f"🚨 {len(high_w)} cảnh báo cao")
                    else:
                        st.warning(f"⚠️ {len(warnings_list)} cảnh báo")
                else:
                    st.success("✅ Không có cảnh báo")
        
        # Interaction warnings
        st.markdown("---")
        st.markdown("### ⚠️ Cảnh Báo Tương Tác Khi Phối Hợp:")
        
        # Check for dangerous combinations
        dangerous_combos = []
        if "Vancomycin" in selected_antibiotics:
            nephrotoxic = ["Gentamicin", "Amikacin", "Tobramycin"]
            if any(drug in selected_antibiotics for drug in nephrotoxic):
                dangerous_combos.append("🚨 **Vancomycin + Aminoglycoside:** Tăng nguy cơ độc thận rất cao!")
        
        if "Piperacillin-Tazobactam" in selected_antibiotics and "Vancomycin" in selected_antibiotics:
            dangerous_combos.append("⚠️ **Piperacillin-Tazobactam + Vancomycin:** Có thể tăng nguy cơ độc thận (nghiên cứu mới)")
        
        if dangerous_combos:
            for combo in dangerous_combos:
                st.error(combo)
        else:
            st.success("✅ Không phát hiện phối hợp nguy hiểm")
        
        # Recommendations
        st.markdown("---")
        st.markdown("### 💡 Khuyến Cáo:")
        
        # Find best option (fewest warnings, appropriate dosing)
        best_options = []
        for ab_name in selected_antibiotics:
            warnings_list = check_warnings(ab_name, crcl, 65, other_drugs=selected_antibiotics)
            high_w = len([w for w in warnings_list if w['level'] == 'high'])
            if high_w == 0:
                best_options.append(ab_name)
        
        if best_options:
            st.success(f"✅ **Kháng sinh an toàn nhất:** {', '.join(best_options)}")
        else:
            st.warning("⚠️ Tất cả kháng sinh đều có cảnh báo. Cần hội chẩn dược lâm sàng.")
        
        # Dosing convenience
        convenience_scores = {}
        for ab_name in selected_antibiotics:
            detailed = calculate_detailed_dose(ab_name, weight, ibw, abw, crcl, indication_code, is_pediatric=False)
            if detailed and detailed.get('interval_hours'):
                # Prefer q24h or q12h (more convenient)
                interval = detailed['interval_hours']
                if interval >= 24:
                    score = 5
                elif interval >= 12:
                    score = 4
                elif interval >= 8:
                    score = 3
                else:
                    score = 2
                convenience_scores[ab_name] = score
        
        if convenience_scores:
            best_convenient = max(convenience_scores.items(), key=lambda x: x[1])
            st.info(f"💡 **Dùng tiện nhất:** {best_convenient[0]} (mỗi {detailed['interval_hours']:.0f} giờ)")

