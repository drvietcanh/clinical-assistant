"""
Serum Osmolality Calculator
Tính độ thẩm thấu huyết thanh và osmolal gap
"""

import streamlit as st


def render():
    """Render Osmolality Calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🧪 Serum Osmolality Calculator</h2>
    <p style='text-align: center;'><em>Tính độ thẩm thấu huyết thanh & Osmolal Gap</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **Serum Osmolality** đo nồng độ các chất hòa tan trong huyết thanh.
        
        **Công thức tính (mOsm/kg):**
        - **Công thức chuẩn:** 2 × Na + Glucose/18 + BUN/2.8
        - **Đơn giản hóa:** 2 × Na + Glucose + Urea (nếu dùng mmol/L)
        
        **Osmolal Gap = Đo trực tiếp - Tính toán**
        
        **Ý nghĩa:**
        - **Gap bình thường:** < 10 mOsm/kg
        - **Gap tăng:** Nghi ngờ chất độc (methanol, ethylene glycol, ethanol...)
        
        **Khi nào dùng:**
        - Đánh giá rối loạn Na
        - Nghi ngờ ngộ độc (methanol, ethylene glycol...)
        - Đánh giá toan chuyển hóa
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Nhập số liệu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        na = st.number_input(
            "Sodium - Na (mmol/L)",
            min_value=100.0,
            max_value=180.0,
            value=140.0,
            step=1.0,
            help="Bình thường: 135-145 mmol/L"
        )
        
        glucose_unit = st.radio(
            "Đơn vị Glucose",
            options=["mmol/L", "mg/dL"],
            index=0,
            horizontal=True
        )
        
        if glucose_unit == "mmol/L":
            glucose_mmol = st.number_input(
                "Glucose (mmol/L)",
                min_value=0.0,
                max_value=50.0,
                value=5.0,
                step=0.1,
                help="Bình thường: 3.9-6.1 mmol/L"
            )
            glucose_mg = glucose_mmol * 18
            st.caption(f"= {glucose_mg:.0f} mg/dL")
        else:
            glucose_mg = st.number_input(
                "Glucose (mg/dL)",
                min_value=0.0,
                max_value=900.0,
                value=90.0,
                step=5.0,
                help="Bình thường: 70-110 mg/dL"
            )
            glucose_mmol = glucose_mg / 18
            st.caption(f"= {glucose_mmol:.1f} mmol/L")
    
    with col2:
        bun_unit = st.radio(
            "Đơn vị BUN/Urea",
            options=["mmol/L (Urea)", "mg/dL (BUN)"],
            index=0,
            horizontal=True
        )
        
        if bun_unit == "mmol/L (Urea)":
            urea_mmol = st.number_input(
                "Urea (mmol/L)",
                min_value=0.0,
                max_value=100.0,
                value=5.0,
                step=0.5,
                help="Bình thường: 2.5-7.1 mmol/L"
            )
            bun_mg = urea_mmol * 2.8
            st.caption(f"= {bun_mg:.1f} mg/dL BUN")
        else:
            bun_mg = st.number_input(
                "BUN (mg/dL)",
                min_value=0.0,
                max_value=300.0,
                value=14.0,
                step=1.0,
                help="Bình thường: 7-20 mg/dL"
            )
            urea_mmol = bun_mg / 2.8
            st.caption(f"= {urea_mmol:.1f} mmol/L Urea")
    
    # Measured osmolality (optional)
    st.markdown("---")
    measured_available = st.checkbox(
        "Có kết quả đo trực tiếp Osmolality (để tính Osmolal Gap)",
        help="Nếu có kết quả đo từ máy osmometer"
    )
    
    if measured_available:
        measured_osm = st.number_input(
            "Osmolality đo trực tiếp (mOsm/kg)",
            min_value=200.0,
            max_value=500.0,
            value=290.0,
            step=1.0,
            help="Bình thường: 275-295 mOsm/kg"
        )
    
    st.markdown("---")
    
    if st.button("🔬 Tính Osmolality", type="primary", use_container_width=True):
        # Calculate osmolality
        calc_osm = 2 * na + glucose_mg/18 + bun_mg/2.8
        
        st.markdown("## 📊 Kết quả")
        
        # Calculated osmolality
        if calc_osm < 275:
            osm_status = "Thấp"
            osm_color = "#ffc107"
        elif calc_osm <= 295:
            osm_status = "Bình thường"
            osm_color = "#28a745"
        else:
            osm_status = "Cao"
            osm_color = "#dc3545"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {osm_color}22 0%, {osm_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {osm_color}; margin: 20px 0;'>
            <h2 style='color: {osm_color}; margin: 0; text-align: center;'>
                Calculated Osmolality = {calc_osm:.1f} mOsm/kg
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                ({osm_status})
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Breakdown
        st.markdown("### 📋 Thành phần:")
        st.markdown(f"""
        - **2 × Na:** 2 × {na} = {2*na:.0f}
        - **Glucose/18:** {glucose_mg:.0f}/18 = {glucose_mg/18:.1f}
        - **BUN/2.8:** {bun_mg:.0f}/2.8 = {bun_mg/2.8:.1f}
        
        **Tổng:** {calc_osm:.1f} mOsm/kg
        """)
        
        # Osmolal gap if measured available
        if measured_available:
            osm_gap = measured_osm - calc_osm
            
            st.markdown("---")
            
            if osm_gap < 10:
                gap_status = "Bình thường"
                gap_color = "#28a745"
                gap_icon = "✅"
            elif osm_gap < 20:
                gap_status = "Tăng nhẹ"
                gap_color = "#ffc107"
                gap_icon = "⚠️"
            else:
                gap_status = "Tăng rõ rệt"
                gap_color = "#dc3545"
                gap_icon = "🚨"
            
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, {gap_color}22 0%, {gap_color}44 100%); 
                        padding: 30px; border-radius: 15px; border-left: 5px solid {gap_color}; margin: 20px 0;'>
                <h2 style='color: {gap_color}; margin: 0; text-align: center;'>
                    {gap_icon} Osmolal Gap = {osm_gap:.1f} mOsm/kg
                </h2>
                <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                    {gap_status}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            **Tính toán:**
            - Đo trực tiếp: {measured_osm:.1f}
            - Tính toán: {calc_osm:.1f}
            - **Gap = {measured_osm:.1f} - {calc_osm:.1f} = {osm_gap:.1f}**
            """)
            
            if osm_gap >= 10:
                st.error("""
                **🚨 OSMOLAL GAP TĂNG - Nghi ngờ chất độc!**
                
                **Nguyên nhân Osmolal Gap tăng (nhớ: ME DIE):**
                
                - **M**ethanol (ngộ độc cồn công nghiệp)
                - **E**thanol (rượu)
                - **D**iethylene glycol / Propylene glycol
                - **I**sopropanol (cồn y tế)
                - **E**thylene glycol (chất chống đông)
                
                **Khác:**
                - Mannitol
                - Glycerol
                - Acetone (DKA)
                - Suy thận nặng
                
                ---
                
                **XỬ TRÍ KHẨN:**
                
                1️⃣ **Xác định chất độc:**
                - **Anion gap metabolic acidosis + Osmolal gap tăng:**
                  - → Nghi ngờ **Methanol** hoặc **Ethylene glycol**
                - **Không acidosis nhưng gap tăng:**
                  - → Nghi ngờ **Ethanol** hoặc **Isopropanol**
                
                2️⃣ **Xét nghiệm:**
                - Methanol level
                - Ethylene glycol level
                - Lactic acid
                - Ketones
                - Anion gap
                - Xét nghiệm nước tiểu (oxalate crystals trong ethylene glycol)
                
                3️⃣ **Điều trị ngộ độc Methanol/Ethylene glycol:**
                
                **A. Fomepizole (Ưu tiên #1):**
                - Loading: 15 mg/kg IV
                - Maintenance: 10 mg/kg q12h × 4 liều, sau đó 15 mg/kg q12h
                - Tiếp tục cho đến methanol/EG < 20 mg/dL
                
                **B. Ethanol (nếu không có Fomepizole):**
                - Loading: 0.6 g/kg (= 7.6 mL/kg ethanol 10%) IV
                - Maintenance: 100-150 mg/kg/h
                - Mục tiêu: Ethanol level 100-150 mg/dL
                
                **C. Lọc máu:**
                - Chỉ định:
                  - Methanol > 50 mg/dL hoặc Ethylene glycol > 50 mg/dL
                  - Suy thận
                  - Toan chuyển hóa nặng (pH < 7.25)
                  - Bất thường điện giải nặng
                  - Rối loạn thị giác (methanol)
                
                **D. Điều chỉnh acidosis:**
                - Sodium bicarbonate nếu pH < 7.3
                - Mục tiêu pH > 7.3
                
                **E. Folinic acid (methanol):**
                - 50 mg IV q4h × 6 liều
                - Tăng chuyển hóa formic acid
                
                **F. Thiamine + Pyridoxine (ethylene glycol):**
                - Giúp chuyển hóa glyoxylic acid → glycine
                """)
            else:
                st.success("""
                **✅ Osmolal Gap bình thường**
                
                - Không có bằng chứng chất độc osmotically active
                - Nếu vẫn nghi ngờ ngộ độc → Xét nghiệm trực tiếp methanol, ethylene glycol
                """)
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Giải thích:")
        
        if calc_osm < 275:
            st.warning("""
            **Hypo-osmolality (Osmolality thấp)**
            
            **Nguyên nhân:**
            - **Hạ Na máu** (phổ biến nhất)
            - SIADH
            - Suy thận
            - Suy tim, xơ gan
            - Uống nước quá nhiều
            - Thiazide diuretics
            
            **Xử trí:** Tùy nguyên nhân gây hạ Na
            """)
        
        elif calc_osm > 295:
            st.warning("""
            **Hyper-osmolality (Osmolality cao)**
            
            **Nguyên nhân:**
            - **Tăng Na máu:**
                - Mất nước (tiêu chảy, lợi tiểu, sốt)
                - Thiểu năng ADH (diabetes insipidus)
                - Uống NaCl
            
            - **Tăng đường huyết:**
                - Đái tháo đường
                - DKA, HHS
            
            - **Tăng BUN:**
                - Suy thận
                - Chảy máu tiêu hóa
                - Catabolism tăng
            
            - **Chất độc:**
                - Methanol, ethylene glycol
                - Ethanol, isopropanol
            
            **Xử trí:** Tùy nguyên nhân
            """)
        
        else:
            st.success("""
            **✅ Osmolality bình thường (275-295 mOsm/kg)**
            
            Cân bằng nước và điện giải bình thường.
            """)
        
        # Clinical uses
        with st.expander("📚 Ứng dụng lâm sàng"):
            st.markdown("""
            ### 1. Đánh giá Hạ Na máu:
            
            **Bước 1:** Đo Serum Osmolality
            
            - **< 275 (hypo-osmolar):** Hạ Na máu thật
              - Đo Urine Osm
              - Đánh giá thể tích
            
            - **275-295 (iso-osmolar):** Pseudo-hyponatremia
              - Lipid cao
              - Protein cao
            
            - **> 295 (hyper-osmolar):** Chuyển dịch nước
              - Đường huyết cao
              - Mannitol
            
            ---
            
            ### 2. Nghi ngờ ngộ độc:
            
            **Tính Osmolal Gap:**
            
            - **Gap < 10:** Bình thường
            - **Gap ≥ 10:** Nghi ngờ chất độc
            
            **Kết hợp Anion Gap:**
            
            - **AG tăng + Osm gap tăng:**
              - Methanol
              - Ethylene glycol
            
            - **AG bình thường + Osm gap tăng:**
              - Ethanol
              - Isopropanol
            
            ---
            
            ### 3. Ước tính nồng độ Ethanol:
            
            **Công thức:**
            - Ethanol (mg/dL) = Osmolal Gap × 4.6
            
            **Ví dụ:**
            - Gap = 20 → Ethanol ≈ 92 mg/dL
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Purssell RA, Lynd LD, Koga Y.** The use of the osmole gap as a screening test for the presence of exogenous substances. 
               *Toxicol Rev.* 2004;23(3):189-202.
            
            2. **Kraut JA, Kurtz I.** Toxic alcohol ingestions: clinical features, diagnosis, and management. 
               *Clin J Am Soc Nephrol.* 2008;3(1):208-25.
            
            3. **Lepeytre F, Ghannoum M, Ammann H, Madore F, Troyanov S.** Ethylene glycol poisoning: A rare but life-threatening cause of metabolic acidosis-A single-centre experience. 
               *Nephrology (Carlton).* 2017;22(4):312-316.
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **Công thức:** 2 × Na + Glucose/18 + BUN/2.8
    
    2. **Osmolal Gap = Đo - Tính**
    
    3. **Gap ≥ 10:** Nghi ngờ chất độc (Methanol, Ethylene glycol, Ethanol...)
    
    4. **Gap tăng + Anion gap tăng:** Methanol hoặc Ethylene glycol → CẤP CỨU!
    
    5. **Điều trị:** Fomepizole + Lọc máu
    """)


if __name__ == "__main__":
    render()

