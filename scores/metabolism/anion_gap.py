"""
Anion Gap Calculator
Đánh giá rối loạn acid-base

Formula:
Anion Gap = Na - (Cl + HCO3)

Normal: 8-12 mEq/L (if albumin normal)
High AG: MUDPILES (Metabolic acidosis with high anion gap)

Reference:
Winter SD, Pearson JR, Gabow PA, et al. The fall of the serum anion gap.
Arch Intern Med. 1990;150(2):311-3.
"""

import streamlit as st


def render():
    """Render Anion Gap Calculator"""
    
    st.subheader("🧪 Anion Gap")
    st.caption("Khoảng Trống Anion - Đánh Giá Rối Loạn Acid-Base")
    
    st.markdown("""
    **Anion Gap** giúp phân loại toan chuyển hóa và tìm nguyên nhân rối loạn acid-base.
    
    **Công thức:** AG = Na - (Cl + HCO₃)
    
    **Bình thường:** 8-12 mEq/L (nếu albumin bình thường)
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🔬 Xét Nghiệm Điện Giải")
        
        # Sodium
        na = st.number_input(
            "**Sodium (Na)** mEq/L:",
            min_value=100.0,
            max_value=180.0,
            value=140.0,
            step=1.0,
            help="Bình thường: 135-145 mEq/L"
        )
        
        # Chloride
        cl = st.number_input(
            "**Chloride (Cl)** mEq/L:",
            min_value=70.0,
            max_value=130.0,
            value=105.0,
            step=1.0,
            help="Bình thường: 98-107 mEq/L"
        )
        
        # Bicarbonate
        hco3 = st.number_input(
            "**Bicarbonate (HCO₃)** mEq/L:",
            min_value=5.0,
            max_value=50.0,
            value=24.0,
            step=1.0,
            help="Bình thường: 22-28 mEq/L"
        )
        
        st.markdown("---")
        st.markdown("### 📊 Điều Chỉnh Theo Albumin (Optional)")
        
        st.info("""
        **Lưu ý:** Albumin thấp làm giảm AG giả tạo.
        Mỗi 1 g/dL albumin giảm → AG giảm ~2.5 mEq/L
        """)
        
        adjust_for_albumin = st.checkbox(
            "Điều chỉnh theo Albumin",
            help="Khuyến nghị nếu albumin < 4.0 g/dL"
        )
        
        if adjust_for_albumin:
            albumin = st.number_input(
                "**Albumin** g/dL:",
                min_value=1.0,
                max_value=6.0,
                value=4.0,
                step=0.1,
                help="Bình thường: 3.5-5.5 g/dL"
            )
        
        st.markdown("---")
        
        if st.button("🧮 Tính Anion Gap", type="primary", use_container_width=True):
            # Calculate AG
            ag = na - (cl + hco3)
            
            # Adjust for albumin if needed
            if adjust_for_albumin:
                ag_corrected = ag + (2.5 * (4.0 - albumin))
                st.info(f"""
                **AG chưa điều chỉnh:** {ag:.1f} mEq/L
                **AG điều chỉnh albumin:** {ag_corrected:.1f} mEq/L
                """)
                ag_display = ag_corrected
            else:
                ag_display = ag
            
            # Interpret
            if ag_display < 8:
                interpretation = "THẤP"
                color = "info"
            elif ag_display <= 12:
                interpretation = "BÌNH THƯỜNG"
                color = "success"
            elif ag_display <= 16:
                interpretation = "TĂNG NHẸ"
                color = "warning"
            else:
                interpretation = "TĂNG CAO"
                color = "error"
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if color == "success":
                    st.success(f"## AG = {ag_display:.1f}")
                    st.success(f"**{interpretation}**")
                elif color == "info":
                    st.info(f"## AG = {ag_display:.1f}")
                    st.info(f"**{interpretation}**")
                elif color == "warning":
                    st.warning(f"## AG = {ag_display:.1f}")
                    st.warning(f"**{interpretation}**")
                else:
                    st.error(f"## AG = {ag_display:.1f}")
                    st.error(f"**{interpretation}**")
                
                st.caption("Bình thường: 8-12 mEq/L")
            
            st.markdown("---")
            st.markdown("### 💡 GIẢI THÍCH & NGUYÊN NHÂN")
            
            if ag_display < 8:
                st.info(f"""
                **🔵 ANION GAP THẤP (< 8 mEq/L)**
                
                **AG = {ag_display:.1f} mEq/L**
                
                **Nguyên nhân:**
                
                1. **Giảm albumin** (phổ biến nhất):
                   - Suy dinh dưỡng
                   - Hội chứng thận hư
                   - Xơ gan
                   - → AG giả thấp, cần điều chỉnh
                
                2. **Tăng protein bất thường:**
                   - Multiple myeloma (IgG)
                   - Paraproteinemia
                
                3. **Tăng ion dương không đo được:**
                   - Tăng Ca, Mg, Li
                   - Thuốc: Lithium
                
                4. **Lỗi phòng xét nghiệm:**
                   - Sai số đo Na, Cl
                   - Cần xác minh lại
                
                **Xử trí:**
                - Điều chỉnh AG theo albumin
                - Tìm nguyên nhân cơ bản
                - Điều trị bệnh nền
                """)
            
            elif ag_display <= 12:
                st.success(f"""
                **🟢 ANION GAP BÌNH THƯỜNG (8-12 mEq/L)**
                
                **AG = {ag_display:.1f} mEq/L**
                
                **Đánh giá:** Điện giải cân bằng, không có toan chuyển hóa AG tăng.
                
                **Nếu có toan chuyển hóa (HCO₃ < 22):**
                → **Non-Anion Gap Metabolic Acidosis (NAGMA)**
                
                **Nguyên nhân NAGMA - "HARDUPS":**
                
                **H** - Hyperalimentation (TPN)
                **A** - Acetazolamide, Addison's disease
                **R** - Renal Tubular Acidosis (RTA)
                **D** - Diarrhea (mất HCO₃)
                **U** - Ureterosigmoidostomy
                **P** - Pancreatic fistula
                **S** - Saline (0.9% NaCl - hyperchloremic acidosis)
                
                **Phân biệt:**
                - Tính **Urine Anion Gap** để phân biệt GI vs Renal
                - UAG = (U-Na + U-K) - U-Cl
                - UAG âm: Mất HCO₃ từ GI (diarrhea)
                - UAG dương: RTA
                
                **Xử trí:**
                - Tìm nguyên nhân
                - Điều trị bệnh nền
                - Cân nhắc HCO₃ nếu pH < 7.2
                """)
            
            elif ag_display <= 16:
                st.warning(f"""
                **🟡 ANION GAP TĂNG NHẸ (12-16 mEq/L)**
                
                **AG = {ag_display:.1f} mEq/L**
                
                **Đánh giá:** Có thể bắt đầu toan chuyển hóa AG tăng hoặc tình trạng kết hợp.
                
                **Cần kiểm tra thêm:**
                1. **ABG (Arterial Blood Gas):**
                   - pH, PCO₂, HCO₃
                   - Xác định có toan chuyển hóa không
                
                2. **Lactate:**
                   - Tăng → Lactic acidosis
                
                3. **Ketones:**
                   - Glucose, β-hydroxybutyrate
                   - DKA, Alcoholic ketoacidosis
                
                4. **Creatinine, BUN:**
                   - Suy thận
                
                5. **Osmolar gap:**
                   - Nếu nghi độc methanol, ethylene glycol
                
                **Nguyên nhân có thể - "MUDPILES":**
                - **M**ethanol
                - **U**remia (suy thận)
                - **D**KA (Diabetic Ketoacidosis)
                - **P**ropylene glycol, Paraldehyde
                - **I**soniazid, Iron
                - **L**actic acidosis
                - **E**thylene glycol
                - **S**alicylates
                
                **Xử trí:**
                - Xét nghiệm bổ sung
                - Tìm nguyên nhân
                - Theo dõi sát
                """)
            
            else:  # AG > 16
                st.error(f"""
                **🔴 ANION GAP TĂNG CAO (> 16 mEq/L)** 🚨
                
                **AG = {ag_display:.1f} mEq/L**
                
                **Đánh giá:** Toan chuyển hóa AG tăng - CẦN TÌM NGUYÊN NHÂN KHẨN CẤP!
                
                **Nguyên nhân - "MUDPILES":**
                
                **M - Methanol:**
                - Độc methanol (windshield washer fluid)
                - Osmolar gap tăng
                - Mù lòa, GI symptoms
                - Điều trị: Fomepizole, dialysis
                
                **U - Uremia:**
                - Suy thận cấp/mạn nặng
                - Cr thường >8-10 mg/dL
                - Dialysis nếu triệu chứng
                
                **D - DKA (Diabetic Ketoacidosis):**
                - Glucose >250 mg/dL
                - Ketones (+), β-hydroxybutyrate tăng
                - Điều trị: Insulin, fluid, K+
                
                **P - Propylene glycol:**
                - Loratadine, Diazepam IV
                - Osmolar gap tăng
                
                **I - Isoniazid, Iron:**
                - INH overdose: Seizures
                - Iron: GI bleeding, shock
                
                **L - Lactic acidosis:**
                - **Type A** (thiếu oxy):
                  * Shock, sepsis
                  * Cardiac arrest
                  * Severe anemia
                - **Type B** (không thiếu oxy):
                  * Metformin (suy thận)
                  * Thiamine deficiency
                  * Malignancy
                - Lactate >4 mmol/L = nguy kịch
                
                **E - Ethylene glycol:**
                - Antifreeze ingestion
                - Osmolar gap tăng
                - Calcium oxalate crystals (urine)
                - Suy thận cấp
                - Điều trị: Fomepizole, dialysis
                
                **S - Salicylates:**
                - Aspirin overdose
                - Toan hỗn hợp (metabolic + respiratory)
                - Tinnitus, tachypnea
                - Level >40 mg/dL
                
                **XỬ TRÍ KHẨN CẤP:**
                
                1. **ABC - Hồi sức:**
                   - Đảm bảo đường thở, hô hấp
                   - IV access, fluid resuscitation
                
                2. **Xét nghiệm STAT:**
                   - ABG
                   - Lactate
                   - Glucose, ketones
                   - Cr, BUN
                   - Osmolar gap (nếu nghi độc)
                   - Salicylate, methanol levels
                
                3. **Điều trị nguyên nhân:**
                   - **Lactic acidosis:** Điều trị shock
                   - **DKA:** Insulin + fluid + K+
                   - **Uremia:** Dialysis khẩn
                   - **Độc:** Fomepizole, dialysis
                
                4. **HCO₃ (tranh cãi):**
                   - Chỉ nếu pH < 7.1
                   - Mục tiêu: pH >7.2
                   - KHÔNG dùng trong DKA (trừ pH <6.9)
                
                5. **Dialysis nếu:**
                   - Methanol/Ethylene glycol
                   - Uremia triệu chứng
                   - Salicylate nặng
                   - Lactic acidosis không đáp ứng
                
                **NGUY HIỂM:** AG >20-30 = tình trạng đe dọa tính mạng!
                """)
            
            # Delta-Delta
            st.markdown("---")
            st.markdown("### 🔢 Delta-Delta Ratio (Phân Tích Nâng Cao)")
            
            with st.expander("📊 Tính Delta-Delta"):
                st.markdown(f"""
                **Delta-Delta giúp phát hiện rối loạn acid-base hỗn hợp.**
                
                **Công thức:**
                - Delta AG = AG đo được - AG bình thường (thường lấy 12)
                - Delta HCO₃ = HCO₃ bình thường (24) - HCO₃ đo được
                - **Ratio = Delta AG / Delta HCO₃**
                
                **Giá trị của bạn:**
                - AG = {ag_display:.1f} mEq/L
                - Delta AG = {ag_display:.1f} - 12 = {ag_display - 12:.1f}
                - Delta HCO₃ = 24 - {hco3:.1f} = {24 - hco3:.1f}
                - **Ratio = {(ag_display - 12) / (24 - hco3) if (24 - hco3) != 0 else 0:.2f}**
                
                **Giải thích:**
                - **Ratio < 1:** Toan hỗn hợp (AGMA + NAGMA)
                  * VD: DKA + diarrhea
                - **Ratio 1-2:** Toan AG tăng đơn thuần
                  * VD: Lactic acidosis, DKA
                - **Ratio > 2:** AGMA + Kiềm chuyển hóa
                  * VD: DKA + nôn nhiều
                  * VD: Lactic acidosis + lợi tiểu
                
                **Lưu ý:** Chỉ áp dụng khi có toan chuyển hóa (HCO₃ < 22)
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **References:**
                
                1. Winter SD, Pearson JR, Gabow PA, Schultz AL, Lepoff RB. 
                   *The fall of the serum anion gap.* 
                   Arch Intern Med. 1990 Feb;150(2):311-3.
                
                2. Figge J, Jabor A, Kazda A, Fencl V. 
                   *Anion gap and hypoalbuminemia.* 
                   Crit Care Med. 1998 Nov;26(11):1807-10.
                
                3. Kraut JA, Madias NE. 
                   *Serum anion gap: its uses and limitations in clinical medicine.* 
                   Clin J Am Soc Nephrol. 2007 Jan;2(1):162-74.
                
                **Guidelines:**
                - DKA: ADA Guidelines
                - Lactic acidosis: Surviving Sepsis Campaign
                - Toxic alcohol: EXTRIP Guidelines
                """)
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("❓ Anion Gap là gì?"):
        st.markdown("""
        **Anion Gap** đại diện cho các anion không đo được trong máu.
        
        **Sinh lý:**
        - Máu phải trung hòa điện (cation = anion)
        - Cation chính: Na⁺, K⁺ (thường bỏ K⁺)
        - Anion chính: Cl⁻, HCO₃⁻
        - Anion không đo: Albumin, phosphate, sulfate, lactate, ketones
        
        **AG = Na - (Cl + HCO₃) = "Unmeasured anions"**
        
        **Bình thường:** 8-12 mEq/L (với albumin bình thường)
        
        **Khi nào tăng:**
        - Tích lũy acid hữu cơ (lactate, ketones)
        - Tích lũy acid độc (methanol, ethylene glycol)
        - Suy thận (tích lũy anion)
        - Giảm cation không đo (hypokalemia, hypocalcemia, hypomagnesemia)
        
        **Ứng dụng chính:**
        - Phân loại toan chuyển hóa
        - Tìm nguyên nhân rối loạn acid-base
        - Đánh giá mức độ nặng (AG càng cao càng nặng)
        """)
    
    with st.expander("🔢 Điều Chỉnh Theo Albumin"):
        st.markdown("""
        **Tại sao cần điều chỉnh?**
        
        - **Albumin là anion âm** → Đóng góp vào AG
        - Mỗi 1 g/dL albumin ≈ 2.5 mEq/L AG
        - Albumin thấp → AG giả thấp
        
        **Công thức điều chỉnh:**
        ```
        AG corrected = AG measured + 2.5 × (4.0 - Albumin)
        ```
        
        **Ví dụ:**
        - Albumin = 2.0 g/dL
        - AG đo được = 10 mEq/L
        - AG điều chỉnh = 10 + 2.5×(4.0-2.0) = 10 + 5 = **15 mEq/L**
        - → Thực ra có AG tăng, mặc dù AG đo chỉ 10!
        
        **Khi nào điều chỉnh:**
        - ✅ Albumin < 4.0 g/dL
        - ✅ Bệnh nhân nặng (ICU, sepsis)
        - ✅ Suy dinh dưỡng, xơ gan, thận hư
        - ❌ Không cần nếu albumin bình thường
        
        **Lưu ý:**
        - Một số lab hiện đại dùng AG normal = 10 thay vì 12
        - Check reference range của lab
        """)
    
    with st.expander("🧪 Osmolar Gap"):
        st.markdown("""
        **Osmolar Gap** giúp phát hiện độc chất không đo được.
        
        **Công thức:**
        ```
        Osmolality (calculated) = 2×Na + Glucose/18 + BUN/2.8
        Osmolar Gap = Osmolality (measured) - Osmolality (calculated)
        ```
        
        **Bình thường:** < 10 mOsm/kg
        
        **Osmolar Gap tăng (>10-20) → Nghi:**
        - **Methanol** (windshield washer fluid)
        - **Ethylene glycol** (antifreeze)
        - **Isopropanol** (rubbing alcohol)
        - **Propylene glycol** (medication carrier)
        - **Ethanol** (rượu)
        - **Ketones** (DKA, starvation)
        
        **Khi nào check:**
        - AG tăng + không tìm được nguyên nhân rõ
        - Nghi ngộ độc
        - Tình trạng thần kinh bất thường + AG tăng
        
        **Lưu ý:**
        - Osmolar gap bình thường KHÔNG loại trừ độc
        - Methanol/EG có thể đã chuyển hóa thành acid
        - → Vẫn cần check level nếu nghi ngờ
        """)
    
    # Footer
    st.markdown("---")
    st.caption("📚 Most basic and important calculation in acid-base disorders")
    st.caption("⚠️ Always correlate with ABG and clinical context")
    st.caption("🏥 Remember MUDPILES for high anion gap metabolic acidosis")

