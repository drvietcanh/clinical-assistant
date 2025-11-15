"""
Creatinine Clearance Calculator
Cockcroft-Gault Formula
"""

import streamlit as st


def render():
    """Creatinine Clearance (CrCl) Calculator - Cockcroft-Gault"""
    st.subheader("🧮 Tính Độ Lọc Cầu Thận (CrCl)")
    st.caption("Công thức Cockcroft-Gault")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Số Bệnh Nhân")
        
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=65,
            step=1
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=200.0,
            value=70.0,
            step=0.5,
            format="%.1f",
            help="Cân nặng thực tế"
        )
        
        # Creatinine with unit conversion
        st.markdown("#### Creatinine Máu")
        scr_unit = st.radio(
            "Đơn vị:",
            ["µmol/L", "mg/dL"],
            horizontal=True,
            index=0,
            key="scr_unit_crcl"
        )
        
        if scr_unit == "µmol/L":
            scr_input = st.number_input(
                "Creatinine (µmol/L)",
                min_value=10.0,
                max_value=1500.0,
                value=88.0,
                step=5.0,
                format="%.1f",
                help="Bình thường: 62-106 µmol/L",
                key="scr_umol"
            )
            scr_mgdl = scr_input / 88.4  # Convert to mg/dL
            st.caption(f"≈ {scr_mgdl:.1f} mg/dL")
        else:  # mg/dL
            scr_input = st.number_input(
                "Creatinine (mg/dL)",
                min_value=0.1,
                max_value=15.0,
                value=1.0,
                step=0.1,
                format="%.1f",
                help="Bình thường: 0.7-1.2 mg/dL",
                key="scr_mgdl"
            )
            scr_mgdl = scr_input
            st.caption(f"≈ {scr_input * 88.4:.0f} µmol/L")
        
        sex = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True
        )
        
        if st.button("🧮 Tính CrCl", type="primary", key="crcl_calc"):
            # Cockcroft-Gault Formula
            crcl = ((140 - age) * weight) / (72 * scr_mgdl)
            if sex == "Nữ":
                crcl *= 0.85
            
            crcl = round(crcl, 1)
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if crcl >= 90:
                    st.success(f"## {crcl} mL/phút")
                    st.success("✅ Chức năng thận bình thường")
                    stage = "Bình thường (G1)"
                elif crcl >= 60:
                    st.success(f"## {crcl} mL/phút")
                    st.info("Giảm nhẹ")
                    stage = "CKD Giai đoạn 2 (G2)"
                elif crcl >= 30:
                    st.warning(f"## {crcl} mL/phút")
                    st.warning("⚠️ Giảm trung bình")
                    stage = "CKD Giai đoạn 3 (G3)"
                elif crcl >= 15:
                    st.error(f"## {crcl} mL/phút")
                    st.error("❗ Giảm nặng")
                    stage = "CKD Giai đoạn 4 (G4)"
                else:
                    st.error(f"## {crcl} mL/phút")
                    st.error("🚨 Suy thận")
                    stage = "CKD Giai đoạn 5 (G5)"
            
            st.markdown("### 💡 Giải Thích")
            st.write(f"**Giai đoạn CKD:** {stage}")
            
            st.markdown("""
            **Ý nghĩa điều chỉnh liều:**
            - Nhiều kháng sinh cần điều chỉnh liều
            - Tham khảo hướng dẫn của bệnh viện
            - Hội chẩn dược sĩ lâm sàng nếu cần
            """)
            
            with st.expander("📐 Formula & Reference"):
                st.markdown(f"""
                **Cockcroft-Gault Formula:**
                ```
                CrCl (mL/min) = [(140 - age) × weight (kg)] / [72 × Scr (mg/dL)]
                (× 0.85 for females)
                ```
                
                **Conversion:**
                - Creatinine: 1 mg/dL = 88.4 µmol/L
                - Scr input: {scr_input} {scr_unit}
                - Scr (mg/dL): {scr_mgdl:.2f}
                - Scr (µmol/L): {scr_mgdl * 88.4:.1f}
                
                **Reference:** 
                Cockcroft DW, Gault MH. Prediction of creatinine clearance from serum creatinine. Nephron. 1976;16(1):31-41.
                """)
