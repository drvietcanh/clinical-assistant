"""
eGFR Calculator - Results Display UI Components
Handles all results display sections
"""

import streamlit as st


def render_results_display(
    age, gender, height_cm, weight_kg, race, creatinine_unit, creatinine, creatinine_mg,
    use_abw, abw, bmi, bsa_formula, bsa, bsa_mosteller, bsa_dubois, bsa_haycock, 
    bsa_boyd, bsa_shuter, egfr_ckd_epi, egfr_mdrd, crcl, gfr_absolute_ckd_epi, 
    gfr_absolute_mdrd, interpretation, recommended, reason
):
    """Render all results display sections"""
    
    st.markdown("## 📊 Kết quả")
    
    # Patient info summary
    st.markdown(f"""
    <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <h4 style='margin-top: 0;'>📋 Thông tin bệnh nhân</h4>
        <p><strong>Tuổi:</strong> {age}, <strong>Giới:</strong> {"Nam" if gender == "male" else "Nữ"}, 
           <strong>BMI:</strong> {bmi:.1f} kg/m²</p>
        <p><strong>BSA:</strong> {bsa:.2f} m² (Mosteller)</p>
        <p><strong>Creatinine:</strong> {creatinine:.1f} {creatinine_unit.replace("/", "/")} ({creatinine_mg:.2f} mg/dL)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main result - CKD-EPI
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {interpretation["color"]}22 0%, {interpretation["color"]}44 100%); 
                padding: 30px; border-radius: 15px; border-left: 5px solid {interpretation["color"]}; margin: 20px 0;'>
        <h2 style='color: {interpretation["color"]}; margin: 0; text-align: center;'>
            {interpretation["icon"]} eGFR (CKD-EPI): {egfr_ckd_epi:.1f} mL/min/1.73m²
        </h2>
        <p style='text-align: center; font-size: 1.2em; margin-top: 10px; font-weight: bold;'>
            {interpretation['stage']}
        </p>
        <p style='text-align: center; font-size: 1.1em; margin-top: 5px;'>
            {interpretation['description']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Recommendation
    if recommended.startswith("Cockcroft-Gault"):
        st.info(f"""
        💡 **Khuyến cáo:** {recommended}
        
        {reason}
        
        **CrCl hiện tại:** {crcl:.1f} mL/min (Cockcroft-Gault)
        - Dùng cho điều chỉnh liều thuốc
        """)
    else:
        st.info(f"""
        💡 **Khuyến cáo:** {recommended}
        
        {reason}
        """)
    
    # All formulas comparison
    st.markdown("---")
    st.markdown("### 📊 So sánh tất cả công thức")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**eGFR Chuẩn hóa (1.73m²)**")
        st.metric("CKD-EPI", f"{egfr_ckd_epi:.1f}", help="Khuyến cáo cho chẩn đoán CKD")
        st.metric("MDRD", f"{egfr_mdrd:.1f}", delta=f"{egfr_mdrd - egfr_ckd_epi:+.1f}", 
                 help="Công thức cũ")
        st.metric("CrCl (Cockcroft-Gault)", f"{crcl:.1f}", 
                 help="Ưu tiên cho điều chỉnh liều thuốc")
    
    with col2:
        st.markdown("**GFR Tuyệt đối (mL/min)**")
        st.metric("CKD-EPI → GFR", f"{gfr_absolute_ckd_epi:.1f}", 
                 help="Từ CKD-EPI chuyển đổi")
        st.metric("MDRD → GFR", f"{gfr_absolute_mdrd:.1f}", 
                 delta=f"{gfr_absolute_mdrd - gfr_absolute_ckd_epi:+.1f}",
                 help="Từ MDRD chuyển đổi")
        st.metric("CrCl = GFR", f"{crcl:.1f}", 
                 help="CrCl = GFR tuyệt đối (không chuẩn hóa)")
    
    with col3:
        st.markdown("**Thông tin khác**")
        bsa_name = {"mosteller": "Mosteller", "dubois": "Du Bois", "haycock": "Haycock", 
                   "boyd": "Boyd", "shuter_aslani": "Shuter & Aslani"}[bsa_formula]
        st.metric("BSA (đã chọn)", f"{bsa:.2f} m²", delta=f"{bsa_name}", 
                 help="Diện tích da cơ thể")
        st.metric("BSA vs Mosteller", f"{bsa_mosteller:.2f}", 
                 delta=f"{bsa - bsa_mosteller:+.3f}",
                 help="So sánh với Mosteller")
        st.metric("Chuyển đổi", f"{bsa / 1.73:.3f}", 
                 help="BSA_actual / 1.73")
    
    # Interpretation and action
    st.markdown("---")
    st.markdown(f"""
    <div style='background-color: {interpretation["color"]}22; padding: 20px; border-radius: 10px; border: 2px solid {interpretation["color"]};'>
        <h3 style='color: {interpretation["color"]}; margin-top: 0;'>
            {interpretation["icon"]} Hành động đề xuất
        </h3>
        <p style='font-size: 1.2em; color: {interpretation["color"]}; font-weight: bold; margin: 10px 0;'>
            {interpretation['action']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Clinical guidance
    st.markdown("---")
    st.markdown("### 💊 Hướng dẫn điều chỉnh liều thuốc")
    
    # Choose the appropriate GFR value for dosing
    if bmi >= 30 or use_abw:
        dosing_gfr = crcl  # Use Cockcroft-Gault for obesity
        dosing_source = f"Cockcroft-Gault (với ABW: {abw:.1f} kg)"
    else:
        dosing_gfr = gfr_absolute_ckd_epi  # Use absolute GFR from CKD-EPI
        dosing_source = "CKD-EPI (GFR tuyệt đối)"
    
    st.markdown(f"""
    **GFR dùng cho điều chỉnh liều: {dosing_gfr:.1f} mL/min**
    - *Nguồn: {dosing_source}*
    
    **Công thức chuyển đổi:**
    ```
    GFR_tuyệt_đối = eGFR_chuẩn × (BSA_thực / 1.73)
    GFR_tuyệt_đối = {egfr_ckd_epi:.1f} × ({bsa:.2f} / 1.73)
    GFR_tuyệt_đối = {egfr_ckd_epi:.1f} × {bsa / 1.73:.3f}
    GFR_tuyệt_đối = {gfr_absolute_ckd_epi:.1f} mL/min
    ```
    """)
    
    # Export section
    st.markdown("---")
    from components.export import render_export_section
    
    # Prepare inputs for export
    inputs_dict = {
        "Age": f"{age} tuổi",
        "Gender": "Nam" if gender == "male" else "Nữ",
        "Height": f"{height_cm} cm",
        "Weight": f"{weight_kg} kg" + (f" (ABW: {abw:.1f} kg)" if use_abw else ""),
        "Creatinine": f"{creatinine:.1f} {creatinine_unit} ({creatinine_mg:.2f} mg/dL)",
        "Race": "Châu Phi / Da đen" if race == "black" else "Khác",
        "BSA Formula": bsa_name,
        "Used ABW": "Có" if use_abw else "Không"
    }
    
    # Prepare results for export
    results_dict = {
        "eGFR (CKD-EPI)": f"{egfr_ckd_epi:.1f} mL/min/1.73m²",
        "eGFR (MDRD)": f"{egfr_mdrd:.1f} mL/min/1.73m²",
        "CrCl (Cockcroft-Gault)": f"{crcl:.1f} mL/min",
        "GFR Absolute (CKD-EPI)": f"{gfr_absolute_ckd_epi:.1f} mL/min",
        "GFR Absolute (MDRD)": f"{gfr_absolute_mdrd:.1f} mL/min",
        "BSA": f"{bsa:.2f} m²",
        "CKD Stage": interpretation['stage'],
        "Recommendation": recommended
    }
    
    render_export_section(
        title=f"eGFR = {egfr_ckd_epi:.1f} mL/min/1.73m² ({interpretation['stage']})",
        inputs=inputs_dict,
        results=results_dict,
        calculator_name="eGFR Calculator",
        filename="egfr_result"
    )
    
    # Save to session state for antibiotic dosing calculator
    st.session_state['patient_crcl'] = crcl
    st.session_state['patient_egfr'] = egfr_ckd_epi
    st.session_state['gfr_absolute'] = dosing_gfr
    
    # Dosing recommendations
    if dosing_gfr >= 60:
        st.success("""
        ✅ **GFR ≥ 60 mL/min - Chức năng thận gần bình thường**
        
        **Hầu hết các thuốc:** Dùng liều bình thường, không cần điều chỉnh.
        
        💡 **CrCl/eGFR đã được lưu** - Có thể sử dụng trong Antibiotic Dosing Calculator
        """)
    elif dosing_gfr >= 30:
        st.warning(f"""
        ⚠️ **GFR 30-59 mL/min - Suy thận mạn**
        
        **GFR hiện tại: {dosing_gfr:.0f} mL/min**
        
        **Cần điều chỉnh liều nhiều thuốc:**
        - Beta-lactams, Fluoroquinolones, Aminoglycosides
        - Vancomycin (monitor nồng độ)
        - Digoxin, LMWH, NOACs
        - Metformin (tránh nếu < 45)
        - SGLT2i (tránh nếu < 45)
        
        ⚠️ **Tra cứu hướng dẫn cụ thể cho từng thuốc!**
        """)
    else:
        st.error(f"""
        🚨 **GFR < 30 mL/min - Suy thận nặng**
        
        **GFR hiện tại: {dosing_gfr:.0f} mL/min**
        
        **⚠️ NGUY HIỂM - Hội chẩn dược sĩ/thận ngay!**
        
        **Nhiều thuốc CHỐNG CHỈ ĐỊNH hoặc giảm liều mạnh:**
        - ❌ Metformin (chống chỉ định)
        - ❌ SGLT2i (chống chỉ định)
        - ❌ NSAIDs (tránh hoặc chống chỉ định)
        - ✅ Hầu hết thuốc cần điều chỉnh liều đáng kể
        
        **Khuyến cáo:** 📞 Hội chẩn dược lâm sàng cho MỌI đơn thuốc!
        """)
    
    return dosing_gfr

