"""
Aminoglycoside Dosing Calculator
Extended-Interval Dosing (Once-Daily)
"""

import streamlit as st


def render():
    """Aminoglycoside Dosing Calculator"""
    st.subheader("💊 Aminoglycoside - Tính Liều")
    st.caption("Gentamicin, Tobramycin, Amikacin - Extended-Interval Dosing")
    
    st.info("""
    **Extended-Interval Aminoglycoside Dosing** (Once-daily) - An toàn và hiệu quả hơn:
    - Hiệu quả tương đương hoặc tốt hơn multiple daily dosing
    - Giảm độc thận và độc tai
    - Tiện lợi hơn cho bệnh nhân
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Số Bệnh Nhân")
        
        # Drug selection
        drug = st.selectbox(
            "**Chọn Aminoglycoside:**",
            ["Gentamicin", "Tobramycin", "Amikacin"],
            key="ag_drug"
        )
        
        # Patient info
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=65,
            step=1,
            key="ag_age"
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=200.0,
            value=70.0,
            step=0.5,
            key="ag_weight"
        )
        
        height = st.number_input(
            "Chiều cao (cm)",
            min_value=120,
            max_value=220,
            value=170,
            step=1,
            key="ag_height"
        )
        
        sex = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            key="ag_sex"
        )
        
        # Calculate IBW
        if sex == "Nam":
            ibw = 50 + 2.3 * ((height - 152.4) / 2.54)
        else:
            ibw = 45.5 + 2.3 * ((height - 152.4) / 2.54)
        
        # Dosing weight calculation
        if weight > ibw * 1.25:  # Obese
            dosing_weight = ibw + 0.4 * (weight - ibw)
            st.info(f"**Béo phì:** IBW = {ibw:.1f} kg → Dùng ABW = {dosing_weight:.1f} kg")
        else:
            dosing_weight = ibw
            st.caption(f"IBW = {ibw:.1f} kg (dùng IBW để tính liều)")
        
        # Creatinine
        st.markdown("#### Creatinine Máu")
        scr_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "µmol/L"],
            horizontal=True,
            key="ag_scr_unit"
        )
        
        if scr_unit == "mg/dL":
            scr_mgdl = st.number_input(
                "Creatinine (mg/dL)",
                min_value=0.1,
                max_value=15.0,
                value=1.0,
                step=0.1,
                key="ag_scr_mgdl"
            )
        else:
            scr_umol = st.number_input(
                "Creatinine (µmol/L)",
                min_value=10.0,
                max_value=1500.0,
                value=88.0,
                step=5.0,
                key="ag_scr_umol"
            )
            scr_mgdl = scr_umol / 88.4
        
        # Calculate CrCl using IBW
        crcl = ((140 - age) * dosing_weight) / (72 * scr_mgdl)
        if sex == "Nữ":
            crcl *= 0.85
        crcl = round(crcl, 1)
        
        st.metric("CrCl (Cockcroft-Gault)", f"{crcl} mL/phút")
        
        # Indication
        indication = st.selectbox(
            "**Chỉ định sử dụng:**",
            [
                "Nhiễm khuẩn Gram âm nặng",
                "Viêm phổi bệnh viện",
                "Nhiễm khuẩn huyết",
                "Nhiễm khuẩn phức tạp trong ổ bụng",
                "Viêm nội tâm mạc (phối hợp)",
                "Nhiễm khuẩn tiết niệu phức tạp"
            ],
            key="ag_indication"
        )
        
        if st.button(f"🧮 Tính Liều {drug}", type="primary", key="ag_calc"):
            # Extended-interval dosing
            # Gentamicin/Tobramycin: 5-7 mg/kg
            # Amikacin: 15-20 mg/kg
            
            if crcl < 20:
                st.error("""
                ⚠️ **Chức năng thận quá thấp (CrCl <20 mL/min)**
                
                Extended-interval dosing KHÔNG khuyến cáo.
                - Cần điều chỉnh liều đặc biệt
                - Tham khảo dược sĩ lâm sàng
                - Cân nhắc thay thuốc khác
                """)
                return
            
            # Calculate dose
            if drug in ["Gentamicin", "Tobramycin"]:
                # Standard dose: 5-7 mg/kg
                if "nội tâm mạc" in indication:
                    mg_per_kg = 3  # Lower dose for synergy
                    dose = dosing_weight * mg_per_kg
                    st.warning("**Lưu ý:** Viêm nội tâm mạc dùng liều thấp để phối hợp (synergy)")
                else:
                    mg_per_kg = 7 if "nặng" in indication or "viêm phổi" in indication else 5
                    dose = dosing_weight * mg_per_kg
                
                # Round to nearest 10mg
                dose = round(dose / 10) * 10
                
                # Determine interval based on CrCl (Hartford Nomogram simplified)
                if crcl >= 60:
                    interval = 24
                    monitoring = "Lấy mẫu máu 6-14h sau liều đầu"
                elif crcl >= 40:
                    interval = 36
                    monitoring = "Lấy mẫu máu 6-14h sau liều đầu"
                else:
                    interval = 48
                    monitoring = "Lấy mẫu máu 6-14h sau liều đầu"
                
                # Target levels
                target_peak = "16-24 µg/mL (nếu đo peak)"
                target_trough = "<1 µg/mL trước liều tiếp theo"
                
            else:  # Amikacin
                mg_per_kg = 15
                dose = dosing_weight * mg_per_kg
                dose = round(dose / 50) * 50  # Round to nearest 50mg
                
                if crcl >= 60:
                    interval = 24
                elif crcl >= 40:
                    interval = 36
                else:
                    interval = 48
                
                monitoring = "Lấy mẫu máu 6-14h sau liều đầu"
                target_peak = "56-64 µg/mL (nếu đo peak)"
                target_trough = "<5 µg/mL trước liều tiếp theo"
            
            with col2:
                st.markdown("### 📊 Liều Khuyến Cáo")
                st.success(f"## {drug}")
                st.metric("Liều", f"{dose:.0f} mg", f"{mg_per_kg} mg/kg")
                st.metric("Tần suất", f"Mỗi {interval}h")
                st.caption(f"Cân nặng tính liều: {dosing_weight:.1f} kg")
            
            st.markdown("### 💡 Chi Tiết Tính Toán")
            st.write(f"- **Thuốc:** {drug}")
            st.write(f"- **Cân nặng (IBW/ABW):** {dosing_weight:.1f} kg")
            st.write(f"- **CrCl:** {crcl} mL/phút")
            st.write(f"- **Liều:** {mg_per_kg} mg/kg × {dosing_weight:.1f} kg = **{dose:.0f} mg**")
            st.write(f"- **Tần suất:** Mỗi **{interval} giờ**")
            
            st.markdown("---")
            st.markdown("### 🎯 Therapeutic Drug Monitoring (TDM)")
            
            st.info(f"""
            **Thời điểm lấy mẫu máu:**
            - {monitoring}
            - Dùng Hartford Nomogram hoặc tính toán dược động học
            
            **Mục tiêu nồng độ (nếu đo):**
            - **Peak:** {target_peak}
            - **Trough:** {target_trough}
            
            **Lưu ý:** Extended-interval dosing thường KHÔNG cần đo peak/trough thường quy nếu:
            - Thời gian điều trị <7 ngày
            - Chức năng thận ổn định
            - Không béo phì quá mức
            """)
            
            st.markdown("### 📝 Hướng Dẫn Truyền")
            
            if drug in ["Gentamicin", "Tobramycin"]:
                st.info(f"""
                **{drug} {dose:.0f} mg IV**
                
                **Pha thuốc:**
                - Pha trong 50-100 mL NS hoặc D5W
                - Nồng độ tối đa: 10 mg/mL
                
                **Truyền:**
                - Thời gian truyền: 30-60 phút
                - Truyền qua pump
                - Tần suất: Mỗi {interval}h
                
                **Lần đầu:**
                - Cho liều đầu tiên ngay
                - TDM sau 6-14h để điều chỉnh interval
                """)
            else:  # Amikacin
                st.info(f"""
                **Amikacin {dose:.0f} mg IV**
                
                **Pha thuốc:**
                - Pha trong 100-200 mL NS hoặc D5W
                - Nồng độ: 5 mg/mL
                
                **Truyền:**
                - Thời gian truyền: 30-60 phút
                - Truyền qua pump
                - Tần suất: Mỗi {interval}h
                
                **Lần đầu:**
                - Cho liều đầu tiên ngay
                - TDM sau 6-14h để điều chỉnh interval
                """)
            
            st.markdown("### ⚠️ Lưu Ý An Toàn")
            st.warning("""
            **Độc tính của Aminoglycosides:**
            
            **1. Độc thận (Nephrotoxicity):**
            - Theo dõi Creatinine hàng ngày
            - Nguy cơ cao nếu: tuổi cao, suy giảm thể tích, dùng lâu >5-7 ngày
            - Tăng nguy cơ nếu phối hợp vancomycin, NSAID, contrast
            
            **2. Độc tai (Ototoxicity):**
            - Hỏi về ù tai, chóng mặt
            - Có thể KHÔNG hồi phục
            - Nguy cơ cao ở người cao tuổi, thời gian điều trị dài
            
            **3. Chống chỉ định:**
            - Myasthenia gravis (có thể gây suy nhược thần kinh cơ)
            - Thai kỳ (độc thận thai nhi)
            
            **4. Theo dõi:**
            - Creatinine, BUN hàng ngày
            - Cân bằng nước điện giải
            - Hỏi triệu chứng độc tai
            - TDM nếu: dùng >5-7 ngày, chức năng thận không ổn định, béo phì
            """)
            
            st.markdown("### 📊 Hartford Nomogram")
            st.info("""
            **Hartford Nomogram** - Điều chỉnh interval dựa trên nồng độ 6-14h sau liều:
            
            **Gentamicin/Tobramycin:**
            - Nồng độ >6 µg/mL → Interval 48h
            - Nồng độ 3.5-6 µg/mL → Interval 36h
            - Nồng độ 1.5-3.5 µg/mL → Interval 24h
            - Nồng độ <1.5 µg/mL → Interval 24h
            
            **Amikacin:**
            - Nồng độ >18 µg/mL → Interval 48h
            - Nồng độ 10-18 µg/mL → Interval 36h
            - Nồng độ 4.5-10 µg/mL → Interval 24h
            - Nồng độ <4.5 µg/mL → Interval 24h
            
            **Lưu ý:** Cần tham khảo dược sĩ lâm sàng để tính toán chính xác.
            """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **Extended-Interval Aminoglycoside Dosing**
                
                **Advantages:**
                - Equal or better efficacy
                - Reduced nephrotoxicity and ototoxicity
                - Convenient once-daily administration
                - Cost-effective
                
                **Dosing:**
                - **Gentamicin/Tobramycin:** 5-7 mg/kg/dose q24-48h
                - **Amikacin:** 15-20 mg/kg/dose q24-48h
                - Use IBW (or ABW if obese)
                
                **Interval adjustment:**
                - Based on CrCl (initial)
                - Based on Hartford Nomogram or PK calculation (subsequent)
                
                **Monitoring:**
                - Random level 6-14h after first dose
                - Adjust interval using nomogram
                - Daily SCr
                - Assess for ototoxicity
                
                **Contraindications to Extended-Interval:**
                - CrCl <20 mL/min
                - Pregnancy
                - Ascites
                - >20% burns
                - Endocarditis (use traditional dosing for synergy)
                
                **References:**
                - Nicolau DP et al. Clin Infect Dis. 1995;21(3):622-629.
                - Freeman CD et al. Pharmacotherapy. 1997;17(6):1138-1148.
                - Barza M et al. Ann Intern Med. 1996;124(8):717-725.
                
                **Guidelines:**
                - IDSA Guidelines for various infections
                - Sanford Guide to Antimicrobial Therapy
                
                **Link:**
                - https://www.idsociety.org/practice-guideline/
                """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ - Tham khảo dược sĩ lâm sàng và Hartford Nomogram để điều chỉnh chính xác")
