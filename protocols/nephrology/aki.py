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
        **Đánh Giá:**
        
        **Labs:**
        - FENa, FEUrea
        - Urine Na, osmolality
        - Urine microscopy
        - BUN/Cr ratio
        
        **Imaging:**
        - US renal nếu nghi postrenal
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều Trị Nguyên Nhân")
    
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
    
    st.markdown("### 1️⃣ Xử Trí Khẩn Cấp")
    
    st.error("""
    **Immediate Actions:**
    
    1. ✅ **Xác định nguyên nhân ngay**
    2. ✅ **Ngừng thuốc độc thận**
    3. ✅ **Optimize perfusion** (nếu prerenal component)
    4. ✅ **Fluid balance** - Euvolemia
    5. ✅ **Monitor electrolytes** (K⁺ đặc biệt quan trọng!)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Điều Trị Nguyên Nhân (Tương Tự Stage 1)")
    
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
    
    st.markdown("### 1️⃣ Xử Trí Khẩn Cấp Ngay")
    
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
    st.markdown("### 4️⃣ RRT Initiation")
    
    st.success("""
    **Timing:**
    - **Early RRT:** Có thể tốt hơn (tùy nghiên cứu)
    - **Không nên trì hoãn** nếu có clear indication
    
    **Access:**
    - **HD:** Temporary catheter (jugular, femoral, subclavian)
    - **CRRT:** Double-lumen catheter
    
    **Prescription:**
    - **HD:** 3-4h sessions, 3×/week
    - **CRRT:** Continuous, UF rate 20-25 ml/kg/h
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Supportive Care Nâng Cao")
    
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

