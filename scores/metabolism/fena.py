"""
FENa - Fractional Excretion of Sodium
Phân biệt AKI tiền thận (prerenal) vs thận (intrinsic renal)

Formula:
FENa (%) = (U-Na × P-Cr) / (P-Na × U-Cr) × 100

Interpretation:
- FENa < 1%: Prerenal AKI (hypovolemia, decreased effective circulating volume)
- FENa > 2%: Intrinsic renal AKI (ATN, AIN)
- FENa 1-2%: Indeterminate

Reference:
Espinel CH. The FENa test. Use in the differential diagnosis of acute renal failure.
JAMA. 1976;236(6):579-81.
"""

import streamlit as st


def render():
    """Render FENa Calculator"""
    
    st.subheader("🧪 FENa - Fractional Excretion of Sodium")
    st.caption("Phân Biệt Suy Thận Cấp Tiền Thận vs Thận")
    
    st.markdown("""
    **FENa** giúp phân biệt nguyên nhân suy thận cấp (AKI):
    - **Prerenal** (thiếu tưới máu thận)
    - **Intrinsic renal** (tổn thương nhu mô thận)
    
    **Công thức:** FENa (%) = (U-Na × P-Cr) / (P-Na × U-Cr) × 100
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🔬 Xét Nghiệm Máu (Plasma)")
        
        # Plasma Sodium
        p_na = st.number_input(
            "**Plasma Sodium (P-Na)** mEq/L:",
            min_value=100.0,
            max_value=180.0,
            value=140.0,
            step=1.0,
            format="%.1f",
            help="Bình thường: 135-145 mEq/L"
        )
        
        # Plasma Creatinine
        st.markdown("#### Plasma Creatinine (P-Cr)")
        p_cr_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "µmol/L (SI)"],
            horizontal=True,
            key="p_cr_unit"
        )
        
        if "mg/dL" in p_cr_unit:
            p_cr = st.number_input(
                "P-Cr (mg/dL):",
                min_value=0.1,
                max_value=20.0,
                value=1.5,
                step=0.1,
                format="%.1f",
                help="Bình thường: 0.7-1.3 mg/dL"
            )
            p_cr_mgdl = p_cr
            st.caption(f"≈ {p_cr * 88.4:.0f} µmol/L")
        else:
            p_cr = st.number_input(
                "P-Cr (µmol/L):",
                min_value=0.0,
                max_value=1800.0,
                value=133.0,
                step=5.0,
                format="%.1f",
                help="Bình thường: 62-115 µmol/L"
            )
            p_cr_mgdl = p_cr / 88.4
            st.caption(f"≈ {p_cr_mgdl:.1f} mg/dL")
        
        st.markdown("---")
        st.markdown("### 💧 Xét Nghiệm Nước Tiểu (Urine)")
        
        # Urine Sodium
        u_na = st.number_input(
            "**Urine Sodium (U-Na)** mEq/L:",
            min_value=1.0,
            max_value=300.0,
            value=20.0,
            step=1.0,
            format="%.1f",
            help="Random urine sample"
        )
        
        # Urine Creatinine
        st.markdown("#### Urine Creatinine (U-Cr)")
        u_cr_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "mmol/L (SI)"],
            horizontal=True,
            key="u_cr_unit"
        )
        
        if "mg/dL" in u_cr_unit:
            u_cr = st.number_input(
                "U-Cr (mg/dL):",
                min_value=1.0,
                max_value=500.0,
                value=50.0,
                step=5.0,
                format="%.1f",
                help="Varies widely"
            )
            u_cr_mgdl = u_cr
            st.caption(f"≈ {u_cr / 11.3:.1f} mmol/L")
        else:
            u_cr = st.number_input(
                "U-Cr (mmol/L):",
                min_value=0.1,
                max_value=50.0,
                value=4.4,
                step=0.5,
                format="%.1f",
                help="Varies widely"
            )
            u_cr_mgdl = u_cr * 11.3
            st.caption(f"≈ {u_cr_mgdl:.0f} mg/dL")
        
        st.markdown("---")
        
        # Check if on diuretics
        on_diuretics = st.checkbox(
            "⚠️ Bệnh nhân đang dùng lợi tiểu (diuretics)",
            help="FENa không đáng tin cậy nếu dùng lợi tiểu. Cân nhắc dùng FEUrea thay thế."
        )
        
        if on_diuretics:
            st.warning("""
            **Lưu ý:** Lợi tiểu làm tăng FENa giả tạo
            
            → FENa không đáng tin cậy!
            
            **Khuyến nghị:** Dùng **FEUrea** thay thế (không bị ảnh hưởng bởi lợi tiểu)
            """)
        
        st.markdown("---")
        
        if st.button("🧮 Tính FENa", type="primary", use_container_width=True):
            # Calculate FENa
            fena = ((u_na * p_cr_mgdl) / (p_na * u_cr_mgdl)) * 100
            
            # Interpret
            if fena < 1.0:
                interpretation = "PRERENAL AKI"
                color = "info"
                cause = "Thiếu tưới máu thận"
            elif fena <= 2.0:
                interpretation = "KHÔNG RÕ RÀNG"
                color = "warning"
                cause = "Cần thêm thông tin lâm sàng"
            else:
                interpretation = "INTRINSIC RENAL AKI"
                color = "error"
                cause = "Tổn thương nhu mô thận"
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if color == "info":
                    st.info(f"""
                    **FENa = {fena:.2f}%**
                    
                    **{interpretation}**
                    
                    {cause}
                    """)
                elif color == "warning":
                    st.warning(f"""
                    **FENa = {fena:.2f}%**
                    
                    **{interpretation}**
                    
                    {cause}
                    """)
                else:
                    st.error(f"""
                    **FENa = {fena:.2f}%**
                    
                    **{interpretation}**
                    
                    {cause}
                    """)
                
                st.caption("< 1%: Prerenal | > 2%: Intrinsic")
            
            if on_diuretics:
                st.error("""
                ⚠️ **CẢNH BÁO:** Bệnh nhân đang dùng lợi tiểu!
                
                FENa = {:.2f}% có thể KHÔNG chính xác.
                
                Lợi tiểu làm tăng FENa giả tạo → Có thể chẩn đoán nhầm prerenal thành intrinsic renal.
                
                **Khuyến nghị:** Dùng FEUrea hoặc đánh giá lâm sàng.
                """.format(fena))
            
            st.markdown("---")
            st.markdown("### 💡 GIẢI THÍCH & XỬ TRÍ")
            
            if fena < 1.0:
                st.info(f"""
                **🔵 PRERENAL AKI (FENa < 1%)**
                
                **FENa = {fena:.2f}%**
                
                **Ý nghĩa:**
                - Thận đang hoạt động BÌNHthường
                - Giữ Na⁺ tối đa (compensatory mechanism)
                - Nguyên nhân: **Thiếu tưới máu thận**
                
                **Nguyên nhân Prerenal AKI:**
                
                **1. Hypovolemia (Giảm thể tích thực sự):**
                - **Mất dịch:**
                  * GI: Nôn, tiêu chảy, NGT drainage
                  * Renal: Lợi tiểu, osmotic diuresis (DM), DI
                  * Skin: Bỏng, sweating
                  * Third-spacing: Pancreatitis, ascites
                - **Chảy máu:**
                  * GI bleeding, trauma
                - **Không bù đủ:**
                  * NPO, elderly, decreased thirst
                
                **2. Decreased Effective Circulating Volume:**
                - **Suy tim (CHF):**
                  * Cardiac output thấp → Tưới máu thận giảm
                  * BNP tăng, edema
                - **Xơ gan:**
                  * Splanchnic vasodilation
                  * Effective volume giảm
                - **Hội chứng thận hư:**
                  * Hypoalbuminemia
                  * Fluid shift vào interstitium
                
                **3. Renal Hypoperfusion:**
                - **Thuốc:**
                  * NSAIDs (giảm PGE₂ → giảm vasodilation afferent)
                  * ACE-I/ARB (giảm angiotensin II → giảm vasoconstriction efferent)
                  * Calcineurin inhibitors (Cyclosporine, Tacrolimus)
                - **Hẹp động mạch thận (RAS):**
                  * Đặc biệt khi dùng ACE-I/ARB
                
                **4. Hypotension:**
                - Sepsis, shock
                - Anesthesia
                
                **Dấu hiệu lâm sàng Prerenal:**
                - ✅ Giảm turgor da
                - ✅ Niêm mạc khô
                - ✅ Tachycardia, orthostatic hypotension
                - ✅ Urine output giảm
                - ✅ BUN/Cr ratio > 20:1
                
                **Xét nghiệm hỗ trợ:**
                - **Urine osmolality:** > 500 mOsm/kg (tập trung tối đa)
                - **Urine Na:** < 20 mEq/L
                - **BUN/Cr ratio:** > 20:1
                - **Urine specific gravity:** > 1.020
                
                **XỬ TRÍ:**
                
                **Nguyên tắc:** Cải thiện tưới máu thận
                
                **1. Volume resuscitation:**
                - **Crystalloid:**
                  * NS hoặc LR 500-1000ml bolus
                  * Đánh giá đáp ứng: UO, BP, JVP
                - **Fluid challenge:**
                  * 500ml NS trong 30-60 phút
                  * Nếu Cr cải thiện → xác nhận prerenal
                
                **2. Ngừng thuốc độc thận:**
                - NSAIDs, ACE-I/ARB (tạm thời)
                - Contrast agents
                - Aminoglycosides, Vancomycin
                
                **3. Điều trị nguyên nhân:**
                - Cầm máu nếu bleeding
                - Điều trị nhiễm trùng nếu sepsis
                - Tối ưu cardiac output nếu CHF
                
                **4. Theo dõi:**
                - UO (mục tiêu >0.5 ml/kg/h)
                - Cr, BUN (theo dõi hàng ngày)
                - Volume status
                
                **Tiên lượng:**
                - ✅ **Tốt nếu phát hiện và điều trị sớm**
                - ✅ Thận hoạt động bình thường → Cr về baseline trong 24-48h
                - ⚠️ Nếu kéo dài → Có thể tiến triển thành ATN
                
                **LƯU Ý:**
                - Prerenal AKI là nguyên nhân phổ biến nhất AKI (~60-70%)
                - **Reversible** nếu điều trị kịp thời
                - Nếu không cải thiện sau fluid resuscitation → Xem xét ATN hoặc nguyên nhân khác
                """)
            
            elif fena <= 2.0:
                st.warning(f"""
                **🟡 FENa KHÔNG RÕ RÀNG ({fena:.2f}%)**
                
                **FENa = {fena:.2f}%** (vùng xám 1-2%)
                
                **Ý nghĩa:** Không thể phân biệt rõ ràng prerenal vs intrinsic renal.
                
                **Có thể là:**
                1. **Prerenal AKI đang chuyển sang ATN**
                2. **Tình trạng kết hợp** (prerenal + intrinsic)
                3. **Một số tình trạng đặc biệt:**
                   - AKI do contrast
                   - Rhabdomyolysis giai đoạn sớm
                   - Sepsis
                   - CKD nền
                
                **CẦN ĐÁNH GIÁ THÊM:**
                
                **1. Lâm sàng:**
                - Volume status?
                - Dấu hiệu hypovolemia?
                - Nguyên nhân có thể?
                
                **2. Xét nghiệm bổ sung:**
                - **BUN/Cr ratio:**
                  * > 20:1 → Nghiêng về prerenal
                  * < 15:1 → Nghiêng về intrinsic
                
                - **Urine osmolality:**
                  * > 500 → Prerenal
                  * < 350 → ATN
                
                - **Urine Na:**
                  * < 20 → Prerenal
                  * > 40 → ATN
                
                - **Urine microscopy:**
                  * Muddy brown casts → ATN
                  * WBC casts → AIN
                  * RBC casts → GN
                  * Eosinophils → AIN
                
                **3. FEUrea (nếu dùng lợi tiểu):**
                - < 35% → Prerenal
                - > 50% → Intrinsic
                
                **4. Fluid challenge:**
                - 500ml NS trong 1h
                - Đánh giá đáp ứng Cr, UO
                - Cải thiện → Prerenal
                - Không cải thiện → Intrinsic
                
                **XỬ TRÍ:**
                - Điều trị như prerenal ban đầu (fluid resuscitation)
                - Theo dõi đáp ứng
                - Tránh thuốc độc thận
                - Nếu không cải thiện trong 24-48h → Xem xét ATN
                
                **Tham khảo Nephrology nếu:**
                - Không rõ nguyên nhân
                - Không cải thiện sau 48h
                - Xem xét biopsy thận
                """)
            
            else:  # FENa > 2%
                st.error(f"""
                **🔴 INTRINSIC RENAL AKI (FENa > 2%)**
                
                **FENa = {fena:.2f}%**
                
                **Ý nghĩa:**
                - Thận KHÔNG giữ được Na⁺
                - Tổn thương tubular function
                - Nguyên nhân: **Tổn thương nhu mô thận**
                
                **Phân loại Intrinsic Renal AKI:**
                
                **1. ACUTE TUBULAR NECROSIS (ATN) - Phổ biến nhất (85-90%):**
                
                **A. Ischemic ATN:**
                - Prerenal kéo dài không điều trị
                - Shock prolonged
                - Major surgery
                - Cardiac arrest
                
                **B. Nephrotoxic ATN:**
                - **Thuốc:**
                  * Aminoglycosides (Gentamicin, Amikacin)
                  * Vancomycin
                  * Amphotericin B
                  * Cisplatin, Carboplatin
                  * Acyclovir (high dose)
                  * Tenofovir
                  * NSAIDs
                - **Contrast-induced AKI:**
                  * Sau CT contrast, angiography
                  * Đặc biệt nếu CKD, DM, dehydration
                - **Pigment nephropathy:**
                  * **Rhabdomyolysis** (myoglobin):
                    - Trauma, crush injury
                    - Prolonged immobilization
                    - Seizures, strenuous exercise
                    - Drugs: Statins, cocaine
                    - CK >5000, myoglobin (+)
                    - Dark urine, no RBC
                  * **Hemolysis** (hemoglobin):
                    - Transfusion reaction
                    - G6PD deficiency
                - **Tumor lysis syndrome:**
                  * Chemo trong hematologic malignancy
                  * Uric acid, phosphate tăng cao
                  * Ca giảm
                
                **Dấu hiệu ATN:**
                - Muddy brown casts (U/A)
                - Renal tubular epithelial cells
                - FENa > 2%
                - Urine Na > 40 mEq/L
                - Urine osmolality < 350
                - BUN/Cr < 15:1
                
                **2. ACUTE INTERSTITIAL NEPHRITIS (AIN):**
                - **Thuốc (90%):**
                  * Antibiotics: Penicillins, Cephalosporins, Quinolones, Rifampin
                  * NSAIDs
                  * PPIs
                  * Allopurinol
                  * Diuretics (Furosemide, Thiazides)
                - **Nhiễm trùng:**
                  * Legionella, Leptospirosis
                  * EBV, CMV, HIV
                - **Autoimmune:**
                  * SLE, Sarcoidosis, Sjogren's
                
                **Dấu hiệu AIN:**
                - Triad (chỉ 10-15%): Fever, rash, eosinophilia
                - Eosinophiluria (nhạy nhưng không đặc hiệu)
                - WBC casts
                - Sterile pyuria
                
                **3. ACUTE GLOMERULONEPHRITIS (GN):**
                - **Post-infectious GN:**
                  * Post-streptococcal
                - **IgA nephropathy**
                - **Lupus nephritis**
                - **ANCA vasculitis**
                - **Anti-GBM disease (Goodpasture)**
                
                **Dấu hiệu GN:**
                - **RBC casts** (pathognomonic)
                - Dysmorphic RBC
                - Proteinuria (often nephrotic range)
                - Hematuria
                - HTN, edema
                
                **4. VASCULAR:**
                - **Renal artery thrombosis/stenosis**
                - **Renal vein thrombosis**
                - **Atheroembolic disease:**
                  * Sau can thiệp mạch máu
                  * Livedo reticularis
                  * Eosinophilia
                - **Malignant hypertension**
                - **Scleroderma renal crisis**
                
                **XỬ TRÍ INTRINSIC RENAL AKI:**
                
                **1. Supportive Care (Chủ yếu):**
                - **Ngừng thuốc độc thận NGAY!**
                - **Fluid balance:**
                  * Tránh overload (phù phổi)
                  * Tránh dehydration
                  * Euvolemia
                - **Electrolytes:**
                  * Monitor K⁺ (nguy hiểm nhất!)
                  * Avoid K⁺-rich foods/IV
                  * Phosphate binders if needed
                - **Diuretics:**
                  * Furosemide nếu volume overload
                  * KHÔNG cải thiện kidney function
                  * Chỉ để kiểm soát volume
                
                **2. Điều trị nguyên nhân cụ thể:**
                
                **ATN:**
                - Supportive care
                - Tránh thuốc độc thận
                - Maintain perfusion
                - Usually self-limited (1-3 tuần)
                
                **Rhabdomyolysis:**
                - **Aggressive hydration:**
                  * NS 200-1000ml/h
                  * Mục tiêu UO 200-300ml/h
                - **Alkalinization:**
                  * NaHCO₃ nếu pH < 6.5
                  * Mục tiêu urine pH > 6.5
                - **Mannitol** (có thể)
                - **Dialysis** nếu severe
                
                **AIN:**
                - **Ngừng thuốc gây bệnh!**
                - **Steroids:**
                  * Prednisolone 0.5-1 mg/kg/day
                  * Nếu không cải thiện sau 1 tuần
                  * Tapering 4-6 tuần
                
                **GN:**
                - **Immunosuppression:**
                  * Steroids
                  * Cyclophosphamide
                  * Rituximab
                - Tùy nguyên nhân cụ thể
                
                **3. Chỉ định Dialysis:**
                - **"AEIOU"**
                  * **A**cidosis (pH < 7.1)
                  * **E**lectrolytes (K > 6.5 mEq/L resistant)
                  * **I**ntoxication (toxic alcohols, lithium)
                  * **O**verload (pulmonary edema, không đáp ứng lợi tiểu)
                  * **U**remia symptoms (encephalopathy, pericarditis, bleeding)
                
                **4. Tham vấn Nephrology:**
                - ✅ FENa > 2% (intrinsic renal)
                - ✅ Không rõ nguyên nhân
                - ✅ Không cải thiện sau 72h
                - ✅ Xem xét biopsy thận
                - ✅ Chỉ định dialysis
                
                **Tiên lượng:**
                - ⚠️ **Xấu hơn prerenal**
                - ATN: Recovery trong 1-3 tuần (nếu không biến chứng)
                - AIN: Recovery trong vài tuần-tháng (nếu ngừng thuốc sớm)
                - GN: Tùy nguyên nhân, có thể CKD
                - Tỷ lệ cần dialysis: 10-30%
                - Tỷ lệ tử vong: 40-50% (trong ICU)
                """)
            
            # Additional calculations
            st.markdown("---")
            with st.expander("🧮 Chi Tiết Tính Toán"):
                st.markdown(f"""
                **Công thức FENa:**
                ```
                FENa (%) = (U-Na × P-Cr) / (P-Na × U-Cr) × 100
                ```
                
                **Giá trị của bạn:**
                - U-Na = {u_na:.1f} mEq/L
                - P-Na = {p_na:.1f} mEq/L
                - U-Cr = {u_cr_mgdl:.1f} mg/dL
                - P-Cr = {p_cr_mgdl:.1f} mg/dL
                
                **Tính toán:**
                ```
                FENa = ({u_na:.1f} × {p_cr_mgdl:.1f}) / ({p_na:.1f} × {u_cr_mgdl:.1f}) × 100
                FENa = {(u_na * p_cr_mgdl):.1f} / {(p_na * u_cr_mgdl):.1f} × 100
                FENa = {fena:.2f}%
                ```
                
                **Giải thích:**
                - Tử số: U-Na × P-Cr = Lượng Na được lọc
                - Mẫu số: P-Na × U-Cr = Lượng Na được thải
                - Ratio × 100 = % Na được lọc ra nước tiểu
                """)
            
            with st.expander("📊 FEUrea (Nếu Đang Dùng Lợi Tiểu)"):
                st.markdown("""
                **FEUrea** không bị ảnh hưởng bởi lợi tiểu.
                
                **Công thức:**
                ```
                FEUrea (%) = (U-Urea × P-Cr) / (P-Urea × U-Cr) × 100
                ```
                
                **Giải thích:**
                - **< 35%:** Prerenal AKI
                - **> 50%:** Intrinsic Renal AKI
                - 35-50%: Indeterminate
                
                **Ưu điểm:**
                - Không bị ảnh hưởng lợi tiểu
                - Đáng tin cậy hơn FENa khi dùng diuretics
                
                **Nhược điểm:**
                - Cần xét nghiệm Urea nước tiểu (không phải test thường quy)
                - Ít được validate hơn FENa
                
                **Khi nào dùng:**
                - Bệnh nhân đang dùng lợi tiểu
                - FENa không rõ ràng
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **Primary Reference:**
                - Espinel CH. 
                  *The FENa test. Use in the differential diagnosis of acute renal failure.* 
                  JAMA. 1976 Aug 9;236(6):579-81. [PMID: 947239]
                
                **Guidelines:**
                - KDIGO Clinical Practice Guideline for Acute Kidney Injury. 
                  Kidney Int Suppl. 2012;2(1):1-138.
                
                - Kellum JA, Lameire N; KDIGO AKI Guideline Work Group. 
                  *Diagnosis, evaluation, and management of acute kidney injury: a KDIGO summary (Part 1).* 
                  Crit Care. 2013 Feb 4;17(1):204.
                
                **FEUrea:**
                - Carvounis CP, Nisar S, Guro-Razuman S. 
                  *Significance of the fractional excretion of urea in the differential diagnosis of acute renal failure.* 
                  Kidney Int. 2002 Dec;62(6):2223-9.
                """)
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("❓ FENa Là Gì?"):
        st.markdown("""
        **Fractional Excretion of Sodium (FENa)** đo % sodium được lọc qua cầu thận 
        và được thải ra nước tiểu.
        
        **Sinh lý:**
        - Thận bình thường tái hấp thu >99% Na⁺ được lọc
        - FENa bình thường: <1%
        
        **Khi thiếu tưới máu (prerenal):**
        - Thận cố gắng giữ Na⁺ và nước
        - RAAS activation → tái hấp thu Na⁺ ↑↑
        - → FENa < 1%
        
        **Khi tổn thương tubular (ATN):**
        - Thận không thể tái hấp thu Na⁺
        - Na⁺ thất thoát ra nước tiểu
        - → FENa > 2%
        
        **Ứng dụng:**
        - Phân biệt prerenal vs intrinsic renal AKI
        - Giúp hướng dẫn điều trị
        - Đơn giản, nhanh, rẻ
        """)
    
    with st.expander("⚠️ Hạn Chế Của FENa"):
        st.markdown("""
        **FENa có nhiều hạn chế, cần hiểu rõ:**
        
        **1. Không đáng tin cậy khi:**
        - **Đang dùng lợi tiểu** (giả tăng FENa)
        - **CKD nền** (FENa có thể cao baseline)
        - **Contrast-induced AKI** (FENa có thể <1% ngay cả khi ATN)
        - **Rhabdomyolysis** (giai đoạn sớm FENa có thể <1%)
        - **Sepsis/SIRS** (có thể kết hợp prerenal + ATN)
        - **Cirrhosis với ascites** (FENa có thể <1% ngay cả khi ATN)
        
        **2. Không áp dụng cho:**
        - **Postrenal AKI** (obstructive)
        - **AKI trên nền CKD** stage 4-5
        - Đã điều trị fluid/diuretics
        
        **3. Vùng xám (FENa 1-2%):**
        - Không thể phân biệt rõ
        - Cần thêm thông tin
        
        **4. Exceptions với FENa <1% nhưng vẫn ATN:**
        - Contrast-induced AKI
        - Rhabdomyolysis (sớm)
        - Acute glomerulonephritis
        - Hepatorenal syndrome
        
        **Khuyến nghị:**
        - **Không dựa vào FENa đơn độc!**
        - Kết hợp với lâm sàng
        - Kết hợp xét nghiệm khác:
          * BUN/Cr ratio
          * Urine osmolality
          * Urine microscopy
          * Fluid challenge response
        """)
    
    # Footer
    st.markdown("---")
    st.caption("📚 Essential tool for differentiating prerenal vs intrinsic renal AKI")
    st.caption("⚠️ Not reliable if on diuretics - consider FEUrea instead")
    st.caption("🏥 Always correlate with clinical context and other lab findings")

