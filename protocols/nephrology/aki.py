"""
AKI Management Protocol
KDIGO-based AKI Management
"""

import streamlit as st


def render():
    """AKI Management Protocol"""
    st.subheader("🧪 AKI Management Protocol")
    st.caption("KDIGO-based Acute Kidney Injury Management")
    
    st.info("""
    **AKI Definition (KDIGO):**
    - ↑ SCr ≥0.3 mg/dL trong 48h HOẶC
    - ↑ SCr ≥1.5× baseline trong 7 ngày HOẶC
    - UO <0.5 mL/kg/h trong 6h
    """)
    
    st.markdown("---")
    
    # Stage selection
    aki_stage = st.radio(
        "**KDIGO Stage:**",
        ["Stage 1", "Stage 2", "Stage 3", "Chưa xác định"],
        key="aki_stage"
    )
    
    st.markdown("---")
    
    if "Stage 1" in aki_stage:
        render_aki_stage1()
    elif "Stage 2" in aki_stage:
        render_aki_stage2()
    elif "Stage 3" in aki_stage:
        render_aki_stage3()
    else:
        render_aki_unknown()


def render_aki_stage1():
    """AKI Stage 1 Management"""
    
    st.warning("## ⚠️ AKI STAGE 1 PROTOCOL")
    
    st.markdown("### 1️⃣ Xác Định Nguyên Nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Nguyên nhân thường gặp:**
        
        **Prerenal (60-70%):**
        - Volume depletion
        - Heart failure
        - Hypotension
        - Sepsis
        
        **Intrinsic (25-30%):**
        - ATN (ischemic, toxic)
        - AIN (drug-induced)
        - GN
        - Rhabdomyolysis
        
        **Postrenal (5-10%):**
        - Obstruction
        """)
    
    with col2:
        st.warning("""
        **Đánh giá:**
        
        **Labs:**
        - FENa, FEUrea
        - Urine Na, osmolality
        - Urine microscopy
        - BUN/Cr ratio
        
        **Imaging:**
        - US renal nếu nghi postrenal
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều trị Nguyên Nhân")
    
    st.success("""
    **Prerenal AKI:**
    - **Volume resuscitation:**
      * NS 0.9% hoặc LR
      * Bolus 500-1000ml
      * Đánh giá đáp ứng (UO, BP)
    - **Optimize perfusion:**
      * Vasopressors nếu cần
      * Inotropes nếu HF
    
    **Intrinsic AKI:**
    - **Ngừng thuốc độc thận ngay!**
    - **Điều trị nguyên nhân:**
      * Rhabdo: Aggressive hydration, alkalinization
      * AIN: Ngừng thuốc, steroids nếu cần
      * GN: Tùy nguyên nhân
    
    **Postrenal AKI:**
    - **Relieve obstruction:**
      * Urethral catheter
      * Nephrostomy
      * Urologic consult
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Supportive Care")
    
    st.info("""
    **Fluid Management:**
    - Euvolemia
    - Tránh overload
    - Monitor: Input/output, weights, CVP (nếu có)
    
    **Medications:**
    - Tránh NSAIDs
    - Điều chỉnh liều thuốc theo CrCl
    - Tránh contrast (nếu có thể)
    
    **Monitoring:**
    - SCr mỗi 24-48h
    - UO mỗi giờ
    - Electrolytes (K⁺, PO₄⁻, Ca²⁺)
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ When to Consult Nephrology")
    
    st.warning("""
    **Consult nếu:**
    - Không rõ nguyên nhân
    - Không cải thiện sau 48-72h
    - Rhabdomyolysis nặng
    - GN (suspected)
    - AIN không cải thiện sau ngừng thuốc
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Prognosis")
    
    st.success("""
    **Tiên lượng:**
    - Prerenal: Thường hồi phục nhanh nếu điều trị sớm
    - Intrinsic: Phụ thuộc nguyên nhân
    - Recovery: 1-2 tuần (ATN)
    """)


def render_aki_stage2():
    """AKI Stage 2 Management"""
    
    st.error("## 🚨 AKI STAGE 2 PROTOCOL")
    
    st.markdown("### 1️⃣ Xử tríKhẩn Cấp")
    
    st.error("""
    **Immediate Actions:**
    
    1. ✅ **Xác định nguyên nhân ngay**
    2. ✅ **Ngừng thuốc độc thận**
    3. ✅ **Optimize perfusion** (nếu prerenal component)
    4. ✅ **Fluid balance** - Euvolemia
    5. ✅ **Theo dõi electrolytes** (K⁺ đặc biệt quan trọng!)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều trị Nguyên Nhân (Tương Tự Stage 1)")
    
    st.info("""
    **Nhưng tích cực hơn:**
    
    **Prerenal:**
    - Aggressive volume resuscitation
    - Vasopressors/inotropes sớm
    
    **Intrinsic:**
    - Rhabdo: Hydration + alkalinization tích cực
    - AIN: Steroids sớm (nếu cần)
    
    **Postrenal:**
    - Relieve obstruction ngay
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Supportive Care Nâng Cao")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Electrolytes:**
        
        **Hyperkalemia:**
        - K >5.5: Kayexalate, furosemide
        - K >6.5: Calcium, insulin/D50, albuterol
        
        **Hyperphosphatemia:**
        - PO₄ binders
        
        **Hypocalcemia:**
        - Ca gluconate nếu symptomatic
        
        **Acidosis:**
        - NaHCO₃ nếu pH <7.1
        """)
    
    with col2:
        st.error("""
        **Fluid Overload:**
        
        - **Diuretics:**
          * Furosemide IV (bolus hoặc continuous)
          * Tăng liều nếu không đáp ứng
        
        - **Lưu ý:**
          * Diuretics KHÔNG cải thiện kidney function
          * Chỉ để kiểm soát volume
          * Tránh dùng nếu hypovolemic
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Indications for RRT (Dialysis)")
    
    st.error("""
    **AEIOU Indications:**
    
    **A**cidosis (pH <7.1, không đáp ứng NaHCO₃)
    
    **E**lectrolytes (K >6.5, không đáp ứng điều trị)
    
    **I**ntoxication (toxic alcohols, lithium, salicylates)
    
    **O**verload (pulmonary edema, không đáp ứng diuretics)
    
    **U**remia symptoms:
    - Encephalopathy
    - Pericarditis
    - Bleeding (uremic platelet dysfunction)
    
    **Hoặc:**
    - BUN >100-150 mg/dL
    - Uremic symptoms
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Nephrology Consult")
    
    st.warning("""
    **Consult ngay nếu:**
    - Stage 2 không cải thiện sau 24-48h
    - Có indication cho RRT
    - Không rõ nguyên nhân
    - GN hoặc AIN nặng
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Prognosis")
    
    st.info("""
    **Tiên lượng:**
    - Xấu hơn Stage 1
    - Tỷ lệ cần RRT: 20-30%
    - Recovery: 2-4 tuần (nếu không biến chứng)
    """)


def render_aki_stage3():
    """AKI Stage 3 Management"""
    
    st.error("## 🚨🚨 AKI STAGE 3 PROTOCOL - NẶNG")
    
    st.markdown("### 1️⃣ Xử tríKhẩn Cấp Ngay")
    
    st.error("""
    **Immediate Actions (< 1h):**
    
    1. ✅ **Nephrology consult NGAY**
    2. ✅ **Check K⁺ ngay** - Nếu >6.5 → Xử trí hyperkalemia khẩn
    3. ✅ **Check pH** - Nếu <7.1 → Xem xét NaHCO₃ hoặc RRT
    4. ✅ **Assess fluid status** - Overload? → Xem xét RRT
    5. ✅ **Stop nephrotoxic drugs**
    6. ✅ **Prepare for RRT**
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ RRT Decision")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **Indications cho RRT:**
        
        ✅ **AEIOU** (xem Stage 2)
        
        ✅ **Anuria >12h** với:
          * Fluid overload
          * Acidosis
          * Hyperkalemia
        
        ✅ **Oliguria (<0.3 mL/kg/h)** >24h
        
        ✅ **Uremic symptoms:**
          * Encephalopathy
          * Pericarditis
          * Bleeding
        """)
    
    with col2:
        st.warning("""
        **Modalities:**
        
        **Intermittent HD:**
        - Stable hemodynamically
        - Uremia removal tốt
        
        **CRRT/CVVH:**
        - Hemodynamically unstable
        - ICU patients
        - Fluid overload nặng
        
        **PD:**
        - Không có access
        - Trẻ em
        - Hemodynamically unstable
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Pre-RRT Management")
    
    st.info("""
    **Trong khi chờ RRT:**
    
    **Hyperkalemia:**
    - Ca gluconate 1g IV (cardiovascular protection)
    - Insulin 10U + D50 50ml IV
    - Albuterol 10-20mg nebulized
    - Kayexalate 15-30g PO/NGT
    
    **Acidosis:**
    - NaHCO₃ nếu pH <7.1
    - Calculate dose: (Base deficit × 0.5 × weight) / 2
    
    **Fluid Overload:**
    - Furosemide continuous infusion
    - Tăng liều nếu không đáp ứng
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ RRT Decision Support Tools")
    
    tab1, tab2, tab3 = st.tabs(["RRT Indication Calculator", "Timing Decision", "Modality Selection"])
    
    with tab1:
        st.markdown("#### 📊 RRT Indication Calculator (AEIOU)")
        
        st.markdown("**Nhập thông tin bệnh nhân:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # A - Acidosis
            st.markdown("**A - Acidosis:**")
            ph = st.number_input(
                "**pH:**",
                min_value=6.5,
                max_value=7.5,
                value=7.35,
                step=0.01,
                key="rrt_ph"
            )
            hco3 = st.number_input(
                "**HCO₃⁻ (mEq/L):**",
                min_value=5.0,
                max_value=50.0,
                value=24.0,
                step=0.5,
                key="rrt_hco3"
            )
            bicarbonate_responsive = st.checkbox("**Đáp ứng NaHCO₃**", key="rrt_bicarb_resp")
            
            # E - Electrolytes
            st.markdown("---")
            st.markdown("**E - Electrolytes:**")
            k = st.number_input(
                "**K⁺ (mEq/L):**",
                min_value=2.0,
                max_value=10.0,
                value=4.5,
                step=0.1,
                key="rrt_k"
            )
            k_ecg_changes = st.checkbox("**ECG changes (peaked T, QRS widening)**", key="rrt_k_ecg")
            k_treatment_responsive = st.checkbox("**Đáp ứng điều trị**", key="rrt_k_resp")
        
        with col2:
            # I - Intoxication
            st.markdown("**I - Intoxication:**")
            intoxication = st.selectbox(
                "**Loại ngộ độc:**",
                ["Không", "Toxic alcohols (methanol, ethylene glycol)", "Lithium", "Salicylates", "Theophylline"],
                key="rrt_intoxication"
            )
            
            # O - Overload
            st.markdown("---")
            st.markdown("**O - Overload:**")
            pulmonary_edema = st.checkbox("**Pulmonary edema**", key="rrt_pe")
            anasarca = st.checkbox("**Anasarca**", key="rrt_anasarca")
            diuretic_responsive = st.checkbox("**Đáp ứng diuretics**", key="rrt_diuretic_resp")
            fluid_overload_pct = st.number_input(
                "**% Fluid overload:**",
                min_value=0.0,
                max_value=50.0,
                value=0.0,
                step=0.5,
                key="rrt_fluid_pct",
                help="(Current weight - Dry weight) / Dry weight × 100"
            )
            
            # U - Uremia
            st.markdown("---")
            st.markdown("**U - Uremia:**")
            bun = st.number_input(
                "**BUN (mg/dL):**",
                min_value=0.0,
                max_value=300.0,
                value=50.0,
                step=1.0,
                key="rrt_bun"
            )
            encephalopathy = st.checkbox("**Encephalopathy**", key="rrt_encephalopathy")
            pericarditis = st.checkbox("**Pericarditis**", key="rrt_pericarditis")
            uremic_bleeding = st.checkbox("**Uremic bleeding**", key="rrt_bleeding")
        
        st.markdown("---")
        
        # Calculate indications
        indications = []
        indication_count = 0
        
        # A - Acidosis
        if ph < 7.1 or (ph < 7.15 and not bicarbonate_responsive):
            indications.append("🚨 **A - Acidosis:** pH <7.1 hoặc <7.15 không đáp ứng NaHCO₃")
            indication_count += 1
        
        # E - Electrolytes
        if k > 6.5 or (k > 6.0 and k_ecg_changes) or (k > 6.0 and not k_treatment_responsive):
            indications.append("🚨 **E - Hyperkalemia:** K⁺ >6.5 hoặc >6.0 với ECG changes/không đáp ứng")
            indication_count += 1
        
        # I - Intoxication
        if intoxication != "Không":
            indications.append(f"🚨 **I - Intoxication:** {intoxication}")
            indication_count += 1
        
        # O - Overload
        if (pulmonary_edema and not diuretic_responsive) or (anasarca and fluid_overload_pct > 10):
            indications.append("🚨 **O - Fluid Overload:** Pulmonary edema/anasarca không đáp ứng diuretics")
            indication_count += 1
        
        # U - Uremia
        if encephalopathy or pericarditis or uremic_bleeding or (bun > 100):
            uremia_reasons = []
            if encephalopathy:
                uremia_reasons.append("Encephalopathy")
            if pericarditis:
                uremia_reasons.append("Pericarditis")
            if uremic_bleeding:
                uremia_reasons.append("Bleeding")
            if bun > 100:
                uremia_reasons.append(f"BUN >100 ({bun:.0f} mg/dL)")
            indications.append(f"🚨 **U - Uremia:** {', '.join(uremia_reasons)}")
            indication_count += 1
        
        # Display results
        col1, col2 = st.columns([2, 1])
        
        with col1:
            if indication_count > 0:
                st.error(f"### ❌ **CÓ {indication_count} CHỈ ĐỊNH RRT**")
                for ind in indications:
                    st.error(ind)
                st.warning("**Khuyến cáo:** Bắt đầu RRT ngay trong vòng 12-24h")
            else:
                st.success("### ✅ **CHƯA CÓ CHỈ ĐỊNH RRT RÕ RÀNG**")
                st.info("Tiếp tục theo dõi và điều trị bảo tồn. Đánh giá lại nếu có thay đổi.")
        
        with col2:
            st.markdown("### 📊 Tóm Tắt")
            st.metric("**Số chỉ định:**", f"{indication_count}/5")
            
            if indication_count >= 2:
                st.error("**Khẩn cấp**")
            elif indication_count == 1:
                st.warning("**Cân nhắc RRT**")
            else:
                st.success("**Chưa cần RRT**")
    
    with tab2:
        st.markdown("#### ⏱️ Timing Decision: Early vs Late RRT")
        
        # Additional inputs for timing
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Thông tin bổ sung:**")
            
            aki_stage = st.selectbox(
                "**KDIGO Stage:**",
                ["Stage 1", "Stage 2", "Stage 3"],
                key="timing_stage"
            )
            
            uo_24h = st.number_input(
                "**UO trong 24h (mL/kg/h):**",
                min_value=0.0,
                max_value=5.0,
                value=0.5,
                step=0.1,
                key="timing_uo"
            )
            
            anuria_hours = st.number_input(
                "**Anuria (giờ):**",
                min_value=0,
                max_value=72,
                value=0,
                step=1,
                key="timing_anuria"
            )
            
            improving = st.checkbox("**Đang cải thiện (SCr giảm, UO tăng)**", key="timing_improving")
            stable = st.checkbox("**Bệnh nhân ổn định**", key="timing_stable")
        
        with col2:
            st.markdown("**Kết quả:**")
            
            # Timing decision logic
            timing_recommendation = "Unknown"
            timing_reason = ""
            
            if indication_count >= 2:
                timing_recommendation = "Early RRT"
                timing_reason = "Có ≥2 chỉ định AEIOU - Bắt đầu RRT trong 12-24h"
            elif indication_count == 1:
                if "Stage 3" in aki_stage:
                    timing_recommendation = "Early RRT"
                    timing_reason = "Stage 3 + 1 chỉ định - Bắt đầu RRT trong 24-48h"
                elif uo_24h < 0.3 or anuria_hours >= 12:
                    timing_recommendation = "Early RRT"
                    timing_reason = "Oliguria/Anuria + chỉ định - Bắt đầu RRT trong 24-48h"
                else:
                    timing_recommendation = "Delayed RRT"
                    timing_reason = "1 chỉ định nhưng ổn định - Theo dõi, RRT nếu xấu đi"
            else:
                if improving and stable:
                    timing_recommendation = "Delayed RRT"
                    timing_reason = "Không có chỉ định rõ + đang cải thiện - Tiếp tục điều trị bảo tồn"
                else:
                    timing_recommendation = "Monitor"
                    timing_reason = "Theo dõi sát, đánh giá lại mỗi 12-24h"
            
            if timing_recommendation == "Early RRT":
                st.error(f"### 🚨 **{timing_recommendation}**")
                st.error(timing_reason)
                st.info("**Timing:** Bắt đầu trong 12-48h")
            elif timing_recommendation == "Delayed RRT":
                st.warning(f"### ⚠️ **{timing_recommendation}**")
                st.warning(timing_reason)
                st.info("**Timing:** Theo dõi, RRT nếu có indication mới hoặc xấu đi")
            else:
                st.success(f"### ✅ **{timing_recommendation}**")
                st.info(timing_reason)
        
        st.markdown("---")
        st.markdown("#### 📋 Early vs Late RRT Comparison")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **Early RRT Strategy:**
            
            **Chỉ định:**
            - ≥2 AEIOU criteria
            - Stage 3 AKI
            - Oliguria <0.3 mL/kg/h × 24h
            - Anuria × 12h với complications
            
            **Lợi ích:**
            - Kiểm soát electrolytes tốt hơn
            - Giảm fluid overload
            - Tránh biến chứng nặng
            - Có thể giảm mortality (một số nghiên cứu)
            
            **Timing:** 12-48h từ khi có indication
            """)
        
        with col2:
            st.warning("""
            **Delayed RRT Strategy:**
            
            **Chỉ định:**
            - Stage 1-2 AKI
            - 0-1 AEIOU criteria
            - Đang cải thiện
            - Bệnh nhân ổn định
            
            **Lợi ích:**
            - Tránh unnecessary RRT
            - Giảm complications từ access
            - Cho phép recovery tự nhiên
            
            **Lưu ý:** Không nên trì hoãn quá mức
            """)
    
    with tab3:
        st.markdown("#### 🔄 Modality Selection Decision Tree")
        
        st.markdown("**Nhập thông tin bệnh nhân:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            hemodynamically_stable = st.checkbox("**Hemodynamically stable**", key="modality_stable", value=True)
            in_icu = st.checkbox("**Đang ở ICU**", key="modality_icu")
            needs_icu = st.checkbox("**Cần ICU monitoring**", key="modality_icu_need")
            fluid_overload_severe = st.checkbox("**Fluid overload nặng**", key="modality_fluid")
            needs_tight_control = st.checkbox("**Cần kiểm soát electrolytes chặt chẽ**", key="modality_tight")
        
        with col2:
            has_access = st.checkbox("**Đã có vascular access**", key="modality_access")
            brain_edema = st.checkbox("**Brain edema/↑ICP**", key="modality_brain")
            sepsis = st.checkbox("**Sepsis**", key="modality_sepsis")
            needs_uremia_clearance = st.checkbox("**Cần uremia clearance tốt**", key="modality_uremia")
        
        st.markdown("---")
        
        # Modality decision logic
        recommended_modality = "Unknown"
        modality_reason = ""
        alternatives = []
        
        if not hemodynamically_stable or in_icu or needs_icu or fluid_overload_severe or brain_edema:
            recommended_modality = "CRRT (CVVHDF)"
            modality_reason = "Hemodynamically unstable, ICU, fluid overload nặng, hoặc brain edema"
            alternatives = ["SLED (nếu không có ICU bed)", "IHD (nếu ổn định sau hồi sức)"]
        elif needs_tight_control and not has_access:
            recommended_modality = "SLED"
            modality_reason = "Cần kiểm soát tốt nhưng không unstable, không có ICU bed"
            alternatives = ["IHD (nếu ổn định)", "CRRT (nếu có ICU bed)"]
        elif needs_uremia_clearance and hemodynamically_stable:
            recommended_modality = "IHD"
            modality_reason = "Hemodynamically stable, cần uremia clearance tốt"
            alternatives = ["SLED (nếu cần ổn định hơn)", "CRRT (nếu unstable)"]
        else:
            recommended_modality = "IHD hoặc SLED"
            modality_reason = "Bệnh nhân ổn định, không có yêu cầu đặc biệt"
            alternatives = ["CRRT (nếu có chỉ định ICU)"]
        
        # Display recommendation
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 📊 Khuyến Nghị")
            st.success(f"### ✅ **{recommended_modality}**")
            st.info(modality_reason)
            
            if alternatives:
                st.markdown("**Phương án thay thế:**")
                for alt in alternatives:
                    st.caption(f"- {alt}")
        
        with col2:
            st.markdown("### ⚙️ Prescription")
            if "CRRT" in recommended_modality:
                st.info("""
                **CVVHDF:**
                - Blood: 150-200 ml/min
                - UF: 20-25 ml/kg/h
                - Dialysate: 1-2 L/h
                - Replacement: 1-2 L/h
                """)
            elif "IHD" in recommended_modality:
                st.info("""
                **IHD:**
                - Duration: 3-4h
                - Frequency: 3×/week
                - Blood: 300-400 ml/min
                """)
            elif "SLED" in recommended_modality:
                st.info("""
                **SLED:**
                - Duration: 6-12h
                - Frequency: Daily
                - Blood: 200 ml/min
                """)
    
    st.markdown("---")
    st.markdown("#### 🔄 Modality Selection: CRRT vs IHD vs SLED")
    
    tab1, tab2, tab3 = st.tabs(["CRRT (Continuous)", "IHD (Intermittent)", "SLED (Hybrid)"])
    
    with tab1:
        st.markdown("##### 🔄 CRRT - Continuous Renal Replacement Therapy")
        
        st.success("""
        **Chỉ định (Ưu tiên):**
        - ✅ Hemodynamically unstable (shock, vasopressors)
        - ✅ ICU patients
        - ✅ Fluid overload nặng
        - ✅ Cần kiểm soát electrolytes chặt chẽ
        - ✅ Brain edema, ↑ICP
        
        **Modalities:**
        - **CVVH (Continuous Veno-Venous Hemofiltration):**
          * UF rate: 20-25 ml/kg/h
          * Chủ yếu để fluid removal
        - **CVVHD (Continuous Veno-Venous Hemodialysis):**
          * Dialysate flow: 1-2 L/h
          * Chủ yếu để solute clearance
        - **CVVHDF (Continuous Veno-Venous Hemodiafiltration):**
          * Kết hợp cả hai
          * UF + Dialysate
          * **Ưu tiên** cho AKI nặng
        
        **Prescription:**
        - **Blood flow:** 150-200 ml/min
        - **UF rate:** 20-25 ml/kg/h (≥35 ml/kg/h nếu sepsis)
        - **Dialysate flow:** 1-2 L/h (CVVHD/CVVHDF)
        - **Replacement fluid:** 1-2 L/h (CVVH/CVVHDF)
        - **Anticoagulation:** 
          * Heparin (aPTT 1.5-2× normal)
          * Citrate (ưu tiên nếu không chống chỉ định)
          * Không dùng nếu có chống chỉ định
        
        **Ưu điểm:**
        - Hemodynamically stable hơn
        - Kiểm soát fluid tốt
        - Clearance liên tục
        - Ít biến động electrolytes
        
        **Nhược điểm:**
        - Cần ICU monitoring
        - Anticoagulation risk
        - Chi phí cao
        - Cần trained staff
        """)
    
    with tab2:
        st.markdown("##### ⏸️ IHD - Intermittent Hemodialysis")
        
        st.info("""
        **Chỉ định:**
        - ✅ Hemodynamically stable
        - ✅ Không cần ICU
        - ✅ Uremia removal tốt
        - ✅ Không có fluid overload nặng
        
        **Prescription:**
        - **Duration:** 3-4 giờ/session
        - **Frequency:** 3×/week (có thể tăng nếu cần)
        - **Blood flow:** 300-400 ml/min
        - **Dialysate flow:** 500-800 ml/min
        - **UF rate:** Tùy fluid removal goal
        
        **Access:**
        - **Temporary catheter:**
          * **Jugular (ưu tiên):** Ít biến chứng, dễ chăm sóc
          * **Femoral:** Dễ đặt, nhưng tăng nguy cơ nhiễm trùng
          * **Subclavian:** Tránh nếu có thể (stenosis risk)
        - **Size:** 11.5-13.5 Fr, double-lumen
        
        **Ưu điểm:**
        - Uremia clearance tốt
        - Không cần ICU
        - Chi phí thấp hơn
        - Staff quen thuộc
        
        **Nhược điểm:**
        - Hemodynamically unstable
        - Biến động electrolytes
        - Khó kiểm soát fluid nếu overload nặng
        """)
    
    with tab3:
        st.markdown("##### 🔀 SLED - Sustained Low-Efficiency Dialysis")
        
        st.warning("""
        **Chỉ định (Hybrid approach):**
        - ✅ Hemodynamically unstable nhưng không cần CRRT
        - ✅ Cần clearance tốt hơn CRRT
        - ✅ Không có ICU bed cho CRRT
        
        **Prescription:**
        - **Duration:** 6-12 giờ/session
        - **Frequency:** Daily hoặc q12h
        - **Blood flow:** 200 ml/min
        - **Dialysate flow:** 100-300 ml/min
        - **UF rate:** Tùy fluid goal
        
        **Ưu điểm:**
        - Hemodynamically stable hơn IHD
        - Clearance tốt hơn CRRT
        - Có thể làm ngoài ICU
        - Chi phí trung bình
        
        **Nhược điểm:**
        - Không liên tục như CRRT
        - Vẫn có biến động hơn CRRT
        - Cần staff training
        """)
    
    st.markdown("---")
    st.markdown("#### 🩺 Vascular Access Placement")
    
    st.error("""
    **Catheter Selection:**
    
    **Site Priority:**
    1. **Right Internal Jugular** (ưu tiên nhất)
       - Ít biến chứng
       - Dễ chăm sóc
       - Tỷ lệ nhiễm trùng thấp
       - Không gây stenosis
    
    2. **Left Internal Jugular**
       - Tương tự right nhưng có thể khó hơn
    
    3. **Femoral**
       - Dễ đặt, nhanh
       - Tăng nguy cơ nhiễm trùng
       - Chỉ dùng tạm thời (<72h)
       - Không dùng nếu có thể
    
    4. **Subclavian** (tránh nếu có thể)
       - Tăng nguy cơ stenosis
       - Khó chăm sóc
       - Chỉ dùng nếu không có lựa chọn khác
    
    **Catheter Size:**
    - **11.5-13.5 Fr** double-lumen
    - **Length:** 
      * Jugular: 15-20 cm
      * Femoral: 20-24 cm
      * Subclavian: 15-20 cm
    
    **Ultrasound-guided:** Bắt buộc cho jugular/subclavian
    
    **Complications:**
    - Pneumothorax (subclavian)
    - Hemorrhage
    - Infection
    - Thrombosis
    - Stenosis (subclavian)
    """)
    
    st.markdown("---")
    st.markdown("#### 📋 RRT Prescription Details")
    
    st.info("""
    **CRRT Prescription:**
    
    **CVVHDF (Recommended):**
    - Blood flow: 150-200 ml/min
    - UF rate: 20-25 ml/kg/h (≥35 ml/kg/h nếu sepsis)
    - Dialysate flow: 1-2 L/h
    - Replacement fluid: 1-2 L/h
    - Anticoagulation: Citrate (ưu tiên) hoặc Heparin
    
    **IHD Prescription:**
    - Duration: 3-4h
    - Frequency: 3×/week (có thể daily nếu cần)
    - Blood flow: 300-400 ml/min
    - Dialysate flow: 500-800 ml/min
    - UF goal: Tùy fluid status
    
    **SLED Prescription:**
    - Duration: 6-12h
    - Frequency: Daily hoặc q12h
    - Blood flow: 200 ml/min
    - Dialysate flow: 100-300 ml/min
    
    **Monitoring:**
    - Pre-RRT: K⁺, PO₄⁻, Ca²⁺, Hgb
    - During RRT: BP, access function
    - Post-RRT: Labs, fluid balance
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ KDIGO RRT Indications - Chi tiết")
    
    st.markdown("#### 📊 KDIGO 2012 Recommendations")
    
    st.error("""
    **Absolute Indications (Must Start RRT):**
    
    1. **Severe Hyperkalemia:**
       - K⁺ >6.5 mEq/L không đáp ứng điều trị
       - K⁺ >6.0 với ECG changes (peaked T, QRS widening)
    
    2. **Severe Acidosis:**
       - pH <7.1 không đáp ứng NaHCO₃
       - pH <7.15 với hemodynamic instability
    
    3. **Severe Fluid Overload:**
       - Pulmonary edema không đáp ứng diuretics
       - Anasarca với organ dysfunction
    
    4. **Uremic Complications:**
       - Encephalopathy
       - Pericarditis
       - Uremic bleeding (platelet dysfunction)
       - BUN >100-150 mg/dL với symptoms
    
    5. **Intoxication:**
       - Toxic alcohols (methanol, ethylene glycol)
       - Lithium
       - Salicylates (nếu không đáp ứng alkalinization)
       - Theophylline
    """)
    
    st.markdown("---")
    st.markdown("#### ⚖️ Early vs Delayed RRT")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Early RRT Strategy:**
        
        **Start trong 12-24h nếu:**
        - Stage 3 AKI
        - Oliguria <0.3 mL/kg/h × 24h
        - Anuria × 12h
        - ≥2 AEIOU criteria
        - BUN >100 mg/dL
        
        **Evidence:**
        - Một số RCT cho thấy có lợi
        - Giảm fluid overload
        - Kiểm soát electrolytes tốt hơn
        
        **Khuyến cáo:** Cân nhắc early RRT nếu có indication
        """)
    
    with col2:
        st.warning("""
        **Delayed RRT Strategy:**
        
        **Chờ recovery nếu:**
        - Stage 1-2 AKI
        - Không có AEIOU indication
        - Đang cải thiện (SCr giảm, UO tăng)
        - Bệnh nhân ổn định
        
        **Evidence:**
        - Một số RCT không thấy lợi ích early
        - Tránh unnecessary RRT
        - Giảm complications từ access
        
        **Lưu ý:** Không nên trì hoãn quá mức
        """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Supportive Care Nâng Cao")
    
    st.warning("""
    **Nutrition:**
    - Protein: 1.2-1.5 g/kg/day (trong AKI)
    - Kcal: 25-30 kcal/kg/day
    - Phosphate, K⁺ restrictions
    
    **Medications:**
    - Điều chỉnh tất cả thuốc theo CrCl
    - Tránh nephrotoxins
    - Dosing for RRT patients
    
    **Monitoring:**
    - Labs mỗi 12-24h
    - K⁺, PO₄⁻, Ca²⁺ trước mỗi RRT
    - Fluid balance
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Prognosis")
    
    st.error("""
    **Tiên lượng:**
    - **Tỷ lệ cần RRT:** 50-70%
    - **Recovery:** 3-6 tuần (nếu không CKD)
    - **Mortality:** 40-50% (ICU patients)
    - **CKD risk:** 30-50% sẽ CKD sau AKI Stage 3
    """)


def render_aki_unknown():
    """Protocol when AKI stage unknown"""
    
    st.warning("## ⚠️ CHƯA XÁC ĐỊNH KDIGO STAGE")
    
    st.error("""
    **Đánh giá ngay:**
    
    1. ✅ **Calculate KDIGO stage** (dùng KDIGO calculator)
    2. ✅ **Check labs:** SCr, UO, electrolytes
    3. ✅ **Determine cause:** Prerenal, intrinsic, postrenal?
    4. ✅ **Stop nephrotoxic drugs**
    5. ✅ **Optimize perfusion** (nếu prerenal)
    6. ✅ **Nephrology consult** (nếu Stage 2-3 hoặc không rõ)
    
    **Timeline:**
    - KDIGO calculation ngay
    - Labs trong 1h
    - Nephrology consult nếu Stage 2-3
    """)

