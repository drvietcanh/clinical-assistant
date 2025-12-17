"""
Diabetic Ketoacidosis (DKA) Protocol
DKA Management Protocol
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def calculate_fluid_deficit(weight_kg, current_na, baseline_na=140):
    """
    Calculate fluid deficit in DKA
    
    Args:
        weight_kg: Body weight
        current_na: Current sodium
        baseline_na: Natri ban đầu (thường là 140 mEq/L)
    
    Returns:
        Fluid deficit in liters
    """
    # Simplified: Assume 10% dehydration in severe DKA
    fluid_deficit_l = weight_kg * 0.1
    
    # Điều chỉnh dựa trên Na (nếu Na cao → mất nước nhiều hơn)
    if current_na > baseline_na:
        correction = (current_na - baseline_na) * 2  # Rough estimate
        fluid_deficit_l += correction
    
    return round(fluid_deficit_l, 1)


def calculate_insulin_rate(weight_kg):
    """
    Calculate initial insulin infusion rate
    
    Args:
        weight_kg: Body weight
    
    Returns:
        Insulin rate in U/h
    """
    # Standard: 0.1 U/kg/h
    rate = weight_kg * 0.1
    return round(rate, 1)


def render():
    """DKA Protocol"""
    st.subheader("🍭 DKA Protocol")
    st.caption("Diabetic Ketoacidosis Management - ADA/ISPAD Guidelines")
    
    st.error("""
    **DKA Diagnostic Criteria:**
    - Glucose >250 mg/dL (thường >300)
    - pH <7.3 HOẶC HCO₃⁻ <18 mEq/L
    - Ketones (+)
    - Anion gap >12
    """)
    
    st.markdown("---")
    
    # DKA Precipitants
    st.markdown("### 🔍 Tìm Nguyên nhân Gây DKA (DKA Precipitants)")
    
    st.warning("""
    **⚠️ QUAN TRỌNG: Luôn tìm nguyên nhân gây DKA!**
    
    **Nguyên nhân thường gặp:**
    1. **Nhiễm trùng** (40-50%)
       - Viêm phổi, UTI, nhiễm trùng da
       - Cần cấy máu, nước tiểu, X-quang ngực
    2. **Bỏ liều insulin** (20-30%)
       - Quên tiêm, hết insulin, không mua được
    3. **Đái tháo đường mới phát hiện** (10-20%)
       - Type 1 diabetes mới
    4. **Nhồi máu cơ tim / Đột quỵ** (5-10%)
       - Cần ECG, troponin, CT Head
    5. **Thuốc** (5%)
       - Steroids, thiazides, SGLT2 inhibitors
    6. **Bệnh lý cấp tính khác**
       - Viêm tụy, chấn thương, phẫu thuật
    """)
    
    precipitant = st.multiselect(
        "**Nguyên nhân nghi ngờ:**",
        [
            "Nhiễm trùng (viêm phổi, UTI, v.v.)",
            "Bỏ liều insulin",
            "Đái tháo đường mới phát hiện",
            "Nhồi máu cơ tim",
            "Đột quỵ",
            "Thuốc (steroids, thiazides, SGLT2i)",
            "Viêm tụy",
            "Chấn thương/Phẫu thuật",
            "Khác",
            "Chưa xác định"
        ],
        key="dka_precipitants"
    )
    
    if precipitant:
        st.info(f"""
        **Nguyên nhân đã xác định:** {', '.join(precipitant)}
        
        **Workup cần thiết:**
        - **Nhiễm trùng:** Cấy máu, nước tiểu, X-quang ngực, CRP, PCT
        - **Tim mạch:** ECG, troponin, BNP
        - **Thần kinh:** CT Head nếu có triệu chứng
        - **Tụy:** Lipase, amylase, CT bụng nếu nghi ngờ
        - **Thuốc:** Review medication list
        
        **Điều trị nguyên nhân:**
        - Điều trị nhiễm trùng nếu có
        - Xử trí tim mạch nếu có MI/stroke
        - Điều chỉnh thuốc nếu cần
        """)
    else:
        st.warning("""
        **⚠️ Chưa xác định nguyên nhân**
        
        **Workup cần thiết:**
        - Cấy máu, nước tiểu
        - X-quang ngực
        - ECG, troponin
        - Review medication list
        - Hỏi về compliance với insulin
        """)
    
    st.markdown("---")
    
    # Severity selection
    severity = st.radio(
        "**Mức độ DKA:**",
        ["Nhẹ", "Trung bình", "Nặng"],
        key="dka_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_dka()
    elif "Trung bình" in severity:
        render_moderate_dka()
    else:
        render_severe_dka()


def render_mild_dka():
    """Mild DKA Management"""
    
    st.warning("## ⚠️ MILD DKA PROTOCOL")
    
    st.markdown("### Criteria:")
    st.info("""
    - pH: 7.25-7.30
    - HCO₃⁻: 15-18 mEq/L
    - Anion gap: 10-12
    - Mental status: Alert
    """)
    
    st.markdown("---")
    st.markdown("### 1️⃣ Resuscitation")
    
    st.success("""
    **Fluids:**
    - NS 0.9%: 1-1.5L trong 1-2h đầu
    - Sau đó: NS hoặc 0.45% NS dựa trên Na⁺
    - Mục tiêu: Correct trong 24-48h
    
    **Insulin:**
    - **IV Insulin:** 0.1 U/kg/h
    - Hoặc **SC insulin:** Rapid-acting mỗi 1-2h
    - Mục tiêu: Glucose drop 50-75 mg/dL/h
    
    **Monitoring:**
    - Glucose mỗi 1-2h
    - ABG/VBG mỗi 4h
    - Electrolytes mỗi 4h
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Transition to SC Insulin")
    
    st.info("""
    **Khi nào chuyển SC:**
    - pH >7.3
    - HCO₃⁻ >18
    - Anion gap <12
    - Bệnh nhân ăn được
    - Glucose <250 mg/dL
    """)
    
    st.markdown("#### 📊 SC Insulin Transition Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_iv_rate = st.number_input(
            "**IV Insulin rate hiện tại (U/h):**",
            min_value=0.0,
            max_value=20.0,
            value=7.0,
            step=0.1,
            key="dka_iv_rate"
        )
        
        weight_kg_trans = st.number_input(
            "**Cân nặng (kg):**",
            min_value=40.0,
            max_value=150.0,
            value=70.0,
            step=1.0,
            key="dka_trans_weight"
        )
        
        eating_status = st.radio(
            "**Bệnh nhân có ăn được?**",
            ["Có", "Chưa"],
            key="dka_eating"
        )
    
    with col2:
        # Calculate total daily dose from IV rate
        # IV rate × 24h = approximate daily requirement
        # But usually need 1.5-2× for SC (due to absorption)
        estimated_daily_dose = current_iv_rate * 24 * 1.5  # Conservative estimate
        
        # Basal insulin (50% of total)
        basal_dose = estimated_daily_dose * 0.5
        
        # Bolus insulin (50% divided by meals)
        bolus_per_meal = (estimated_daily_dose * 0.5) / 3
        
        st.markdown("**📊 Tính toán liều SC Insulin:**")
        st.metric("**Tổng liều ước tính:**", f"{estimated_daily_dose:.0f} U/day", 
                 help="Từ IV rate × 24h × 1.5")
        st.metric("**Basal (Long-acting):**", f"{basal_dose:.0f} U/day",
                 help="50% của tổng liều")
        st.metric("**Bolus (Rapid-acting):**", f"{bolus_per_meal:.0f} U/meal",
                 help="50% chia cho 3 bữa")
    
    if eating_status == "Có":
        st.success("""
        **✅ Sẵn sàng chuyển SC Insulin:**
        
        **Protocol:**
        1. **Cho SC insulin 30-60 phút TRƯỚC khi ngừng IV**
        2. **Basal insulin:** 
           - Glargine hoặc Detemir: {basal_dose:.0f} U SC ngay
           - Tiêm vào buổi tối hoặc sáng (tùy thói quen)
        3. **Bolus insulin:**
           - Lispro, Aspart, hoặc Glulisine: {bolus_per_meal:.0f} U trước mỗi bữa ăn
           - Cho trước bữa ăn đầu tiên
        4. **Ngừng IV insulin:** Sau khi đã cho SC 30-60 phút
        5. **Overlap:** Đảm bảo overlap để tránh rebound hyperglycemia
        
        **Monitoring sau chuyển:**
        - Glucose mỗi 2-4h trong 24h đầu
        - Điều chỉnh liều nếu cần
        - Đảm bảo glucose 140-180 mg/dL
        """.format(basal_dose=basal_dose, bolus_per_meal=bolus_per_meal))
    else:
        st.warning("""
        **⚠️ Chưa sẵn sàng chuyển SC:**
        
        **Lý do:** Bệnh nhân chưa ăn được
        
        **Tiếp tục:**
        - Tiếp tục IV insulin
        - Đợi bệnh nhân ăn được
        - Khi ăn được → chuyển SC như trên
        """)
    
    st.markdown("---")
    st.markdown("#### ⚠️ Lưu ý khi chuyển SC")
    
    st.warning("""
    **Tránh rebound hyperglycemia:**
    - Phải overlap IV và SC insulin
    - Không ngừng IV trước khi cho SC
    - Đảm bảo SC insulin đã bắt đầu tác dụng
    
    **Tránh hypoglycemia:**
    - Không cho quá nhiều SC insulin
    - Điều chỉnh liều dựa trên glucose
    - Có sẵn D50W nếu cần
    
    **Điều chỉnh liều:**
    - Nếu glucose cao sau chuyển: Tăng liều
    - Nếu glucose thấp: Giảm liều
    - Đánh giá lại sau 24-48h
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Tiêu chuẩn xuất viện")
    
    st.success("""
    - pH >7.3
    - HCO₃⁻ >18
    - Bệnh nhân ăn được
    - Có kế hoạch điều trị tại nhà
    """)


def render_moderate_dka():
    """Moderate DKA Management"""
    
    st.error("## 🚨 MODERATE DKA PROTOCOL")
    
    st.markdown("### Criteria:")
    st.warning("""
    - pH: 7.00-7.24
    - HCO₃⁻: 10-15 mEq/L
    - Anion gap: 12-15
    - Mental status: Alert or drowsy
    """)
    
    st.markdown("---")
    st.markdown("### 1️⃣ Immediate Resuscitation")
    
    st.error("""
    **< 1 Hour:**
    
    1. ✅ **IV access:** 2 lines
    2. ✅ **Labs:** Glucose, ABG, CBC, CMP, ketones
    3. ✅ **ECG** (tìm hypokalemia)
    4. ✅ **Fluid bolus:** 1-1.5L NS 0.9% trong 1h
    5. ✅ **Insulin:** 0.1 U/kg/h IV (không bolus!)
    6. ✅ **K⁺ replacement:** Nếu K <5.5 và urine output tốt
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Fluid Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Calculate Fluid Deficit:**
        
        **Typical deficit:** 6-10% body weight
        
        **Timeline:**
        - **0-2h:** 1-1.5L NS
        - **2-12h:** 50% của deficit
        - **12-24h:** 50% còn lại
        
        **Type:**
        - Na <135: NS 0.9%
        - Na normal/high: 0.45% NS hoặc NS
        """)
    
    with col2:
        st.warning("""
        **Monitoring:**
        
        **Signs of over-resuscitation:**
        - Na drop >5 mEq/L/h
        - Headache, confusion
        - Cerebral edema risk (peds)
        
        **Signs of under-resuscitation:**
        - Persistent hypotension
        - Low UO
        - Tachycardia
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Insulin Protocol")
    
    st.success("""
    **IV Insulin Infusion:**
    
    **Rate:** 0.1 U/kg/h (no bolus!)
    
    **Example:** 70kg patient
    - Rate: 7 U/h
    
    **Titration:**
    - Mục tiêu: Glucose drop 50-75 mg/dL/h
    - Nếu drop <50: Tăng 1-2 U/h
    - Nếu drop >100: Giảm 50% rate
    
    **Khi Glucose <250 mg/dL:**
    - Add D5W hoặc D10W
    - Continue insulin cho đến khi:
      * pH >7.3
      * HCO₃⁻ >18
      * Anion gap <12
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Potassium Replacement")
    
    st.error("""
    **⚠️ CRITICAL: K⁺ thường thấp nhưng K⁺ máu có thể bình thường/cao do acidosis!**
    
    **Check K⁺ mỗi 2-4h**
    
    **K⁺ <3.5:** Thêm K⁺ vào IV fluids
    - 20-40 mEq/L NS (max 40 mEq/L)
    - Mục tiêu: K⁺ 4-5 mEq/L
    
    **K⁺ 3.5-5.0:** Thêm 20 mEq/L vào fluids
    
    **K⁺ >5.0:** KHÔNG cho K⁺ (nhưng check lại sau khi insulin)
    
    **⚠️ Nếu anuria/oliguria:** Cẩn thận với K⁺
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Bicarbonate Therapy")
    
    st.markdown("#### 📋 Khi nào DÙNG Bicarbonate:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **✅ CHỈ ĐỊNH (Dùng):**
        
        1. **pH <6.9** với:
           - Hemodynamic instability (shock)
           - Không đáp ứng với insulin + fluids
           - Cardiac dysfunction do acidosis
        
        2. **pH <7.0** với:
           - Severe cardiac arrhythmias
           - Severe respiratory depression
           - Coma/obtundation
        
        3. **Hyperkalemia nặng** với acidosis
           - Bicarbonate giúp đẩy K⁺ vào tế bào
        """)
    
    with col2:
        st.success("""
        **❌ CHỐNG CHỈ ĐỊNH (KHÔNG dùng):**
        
        1. **pH ≥7.0** và stable
           - Insulin + fluids đủ để điều chỉnh
        
        2. **pH >7.0** không có instability
           - Không cải thiện outcomes
           - Tăng nguy cơ tác dụng phụ
        
        3. **Anuria/oliguria nặng**
           - Không thể bài tiết HCO₃⁻
           - Nguy cơ fluid overload
        
        4. **Hypocalcemia nặng**
           - Bicarbonate có thể làm nặng thêm
        
        5. **Alkalosis**
           - Chống chỉ định tuyệt đối
        """)
    
    st.markdown("---")
    
    use_bicarbonate = st.radio(
        "**Đánh giá chỉ định bicarbonate:**",
        ["Có chỉ định (pH <6.9 với instability)", "Không chỉ định (pH ≥7.0 hoặc stable)", "Cần đánh giá thêm"],
        key="dka_bicarbonate"
    )
    
    if use_bicarbonate == "Có chỉ định (pH <6.9 với instability)":
        st.error("""
        **⚠️ CHỈ ĐỊNH BICARBONATE - ĐIỀU TRỊ:**
        
        **Liều và cách dùng:**
        - **50-100 mEq NaHCO₃** pha trong 500ml D5W
        - **Truyền trong 1-2 giờ** (không nhanh hơn!)
        - **Mục tiêu:** pH 7.1-7.2 (KHÔNG normalize hoàn toàn!)
        - **Lặp lại:** Chỉ nếu pH vẫn <6.9 sau 1-2h
        
        **Cách tính liều:**
        - **Công thức:** (Desired HCO₃⁻ - Current HCO₃⁻) × Weight (kg) × 0.5
        - **Ví dụ:** (15 - 5) × 70 × 0.5 = 350 mEq deficit
        - **Nhưng chỉ cho 50-100 mEq** mỗi lần (conservative approach)
        
        **⚠️ Tác dụng phụ cần theo dõi:**
        1. **Hypokalemia:** Bicarbonate đẩy K⁺ vào tế bào
           - Check K⁺ mỗi 2h sau khi cho bicarbonate
           - Bổ sung K⁺ nếu cần
        
        2. **Paradoxical CSF acidosis:** 
           - Hiếm nhưng nguy hiểm
           - Có thể xảy ra khi normalize pH quá nhanh
        
        3. **Overcorrection:**
           - Tránh normalize pH quá nhanh
           - Mục tiêu chỉ là pH 7.1-7.2
        
        4. **Hypocalcemia:**
           - Bicarbonate có thể làm giảm Ca²⁺ tự do
           - Check Ca²⁺ nếu có triệu chứng
        
        5. **Fluid overload:**
           - Đặc biệt ở bệnh nhân suy tim/thận
        """)
        
        # Bicarbonate calculator
        st.markdown("**🧮 Tính toán liều:**")
        col1, col2 = st.columns(2)
        with col1:
            current_ph = st.number_input(
                "**pH hiện tại:**",
                min_value=6.5,
                max_value=7.5,
                value=6.8,
                step=0.1,
                key="dka_current_ph"
            )
            current_hco3 = st.number_input(
                "**HCO₃⁻ hiện tại (mEq/L):**",
                min_value=0.0,
                max_value=30.0,
                value=5.0,
                step=1.0,
                key="dka_current_hco3"
            )
        with col2:
            weight_kg = st.number_input(
                "**Cân nặng (kg):**",
                min_value=40.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                key="dka_bicarb_weight"
            )
            target_hco3 = st.number_input(
                "**Mục tiêu HCO₃⁻ (mEq/L):**",
                min_value=10.0,
                max_value=25.0,
                value=15.0,
                step=1.0,
                key="dka_target_hco3"
            )
        
        if current_ph < 6.9:
            deficit = (target_hco3 - current_hco3) * weight_kg * 0.5
            dose = min(100, max(50, deficit * 0.3))  # Conservative: chỉ cho 30% của deficit
            
            st.warning(f"""
            **📊 Kết quả tính toán:**
            - **HCO₃⁻ deficit:** {deficit:.0f} mEq
            - **Liều khuyến nghị:** {dose:.0f} mEq NaHCO₃
            - **Pha:** {dose:.0f} mEq trong 500ml D5W
            - **Tốc độ truyền:** Trong 1-2 giờ (không nhanh hơn!)
            - **Theo dõi:** ABG/VBG sau 1-2h, K⁺ mỗi 2h
            """)
    
    elif use_bicarbonate == "Không chỉ định (pH ≥7.0 hoặc stable)":
        st.success("""
        **✅ KHÔNG CẦN BICARBONATE:**
        
        **Lý do không dùng:**
        1. **pH ≥7.0:** Insulin và fluids đủ để điều chỉnh
        2. **Không có bằng chứng:** Không cải thiện outcomes trong DKA
        3. **Tác dụng phụ:** Có thể gây hypokalemia, overcorrection
        4. **Tự điều chỉnh:** pH sẽ cải thiện khi anion gap đóng lại với insulin
        
        **Điều trị thay thế:**
        - ✅ Tiếp tục **insulin IV** 0.1 U/kg/h
        - ✅ Tiếp tục **fluids** để bù dịch
        - ✅ Theo dõi pH, HCO₃⁻ mỗi 2-4h
        - ✅ pH sẽ cải thiện khi ketones giảm
        
        **Khi nào đánh giá lại:**
        - Nếu pH giảm <6.9 và có instability
        - Nếu không đáp ứng với insulin sau 4-6h
        """)
    
    else:  # Cần đánh giá thêm
        st.info("""
        **🔍 ĐÁNH GIÁ CHỈ ĐỊNH BICARBONATE:**
        
        **Câu hỏi cần trả lời:**
        1. **pH hiện tại là bao nhiêu?**
           - <6.9: Cân nhắc nếu có instability
           - ≥7.0: Không cần
        
        2. **Có hemodynamic instability không?**
           - Shock, hypotension: Cân nhắc nếu pH <6.9
           - Stable: Không cần
        
        3. **Đã điều trị insulin + fluids bao lâu?**
           - <4h: Chưa đủ thời gian, tiếp tục điều trị
           - >4h không đáp ứng: Cân nhắc nếu pH <6.9
        
        4. **Có cardiac dysfunction không?**
           - Arrhythmias do acidosis: Cân nhắc
           - Stable: Không cần
        
        **Khuyến nghị:**
        - **pH >7.0 và stable:** Không cần bicarbonate
        - **pH <6.9 và unstable:** Cân nhắc bicarbonate
        - **pH 6.9-7.0:** Đánh giá từng trường hợp
        """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Phosphate Replacement")
    
    st.markdown("#### 📋 Khi nào DÙNG Phosphate:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **✅ CHỈ ĐỊNH (Dùng):**
        
        1. **Phosphate <1.0 mg/dL** (0.32 mmol/L)
           - Nguy cơ cao: weakness, rhabdomyolysis
           - Cần bổ sung ngay
        
        2. **Phosphate 1.0-1.5 mg/dL** với:
           - Triệu chứng: weakness, rhabdomyolysis
           - Nguy cơ giảm thêm (insulin sẽ làm giảm thêm)
        
        3. **Rhabdomyolysis** do hypophosphatemia
        """)
    
    with col2:
        st.success("""
        **❌ KHÔNG CẦN (Không dùng):**
        
        1. **Phosphate ≥1.5 mg/dL** và không có triệu chứng
           - Sẽ được bổ sung tự nhiên qua IV fluids
        
        2. **Phosphate bình thường** (>2.5 mg/dL)
           - Không cần bổ sung
        
        3. **Suy thận nặng** (eGFR <30)
           - Nguy cơ hyperphosphatemia
           - Cẩn thận khi bổ sung
        """)
    
    st.markdown("---")
    
    current_phosphate = st.number_input(
        "**Phosphate hiện tại (mg/dL):**",
        min_value=0.0,
        max_value=10.0,
        value=2.5,
        step=0.1,
        key="dka_phosphate"
    )
    
    if current_phosphate < 1.0:
        st.error("""
        **⚠️ PHOSPHATE THẤP NẶNG (<1.0 mg/dL) - CẦN BỔ SUNG NGAY**
        
        **Tại sao quan trọng:**
        - Phosphate cần thiết cho ATP, 2,3-DPG
        - Thiếu phosphate → weakness, rhabdomyolysis, respiratory failure
        - Insulin làm giảm phosphate thêm (đẩy vào tế bào)
        
        **Liều và cách dùng:**
        - **20-30 mmol IV** trong 6-12 giờ
        - **Hoặc:** Potassium Phosphate 15-30 mmol IV trong 6h
        - **Hoặc:** Sodium Phosphate 20-30 mmol IV trong 6h
        - **Max:** 0.5 mmol/kg trong 6h (không vượt quá!)
        - **Pha trong:** NS hoặc D5W
        
        **⚠️ Tác dụng phụ cần theo dõi:**
        1. **Hypocalcemia:** 
           - Phosphate có thể gây hypocalcemia
           - Check Ca²⁺ mỗi 4-6h
           - Nếu Ca²⁺ <8.5 mg/dL: Bổ sung Ca²⁺ trước
        
        2. **Hyperphosphatemia:**
           - Tránh cho quá nhiều
           - Đặc biệt ở suy thận
        
        3. **Hyperkalemia:**
           - Nếu dùng Potassium Phosphate
           - Check K⁺ trước khi cho
        
        4. **Suy thận:**
           - Cẩn thận nếu eGFR <30
           - Giảm liều hoặc tránh dùng
        """)
        
        weight_kg_phos = st.number_input(
            "**Cân nặng (kg):**",
            min_value=40.0,
            max_value=150.0,
            value=70.0,
            step=1.0,
            key="dka_phos_weight"
        )
        
        max_dose = weight_kg_phos * 0.5
        recommended_dose = min(30, max(20, max_dose * 0.6))
        
        st.warning(f"""
        **📊 Tính toán liều:**
        - **Max dose an toàn:** {max_dose:.0f} mmol trong 6h
        - **Liều khuyến nghị:** {recommended_dose:.0f} mmol
        - **Cho:** {recommended_dose:.0f} mmol trong 6-12h
        - **Theo dõi:** Phosphate và Ca²⁺ mỗi 4-6h
        """)
    
    elif current_phosphate < 1.5:
        st.warning("""
        **⚠️ PHOSPHATE THẤP NHẸ (1.0-1.5 mg/dL)**
        
        **Đánh giá:**
        - ✅ Có triệu chứng (weakness, rhabdomyolysis)?
        - ✅ Có nguy cơ giảm thêm? (insulin sẽ làm giảm thêm)
        - ✅ Có bệnh lý tim phổi?
        
        **Nếu có triệu chứng hoặc nguy cơ cao:**
        - Cân nhắc bổ sung **15-20 mmol** trong 6h
        - Theo dõi phosphate mỗi 4-6h
        
        **Nếu không có triệu chứng:**
        - Theo dõi, có thể tự cải thiện
        - Check lại sau 4-6h
        - Bổ sung nếu giảm <1.0 mg/dL
        """)
    
    else:
        st.success("""
        **✅ PHOSPHATE BÌNH THƯỜNG (≥1.5 mg/dL)**
        
        **Không cần bổ sung:**
        - Phosphate sẽ được bổ sung tự nhiên qua IV fluids
        - Theo dõi mỗi 4-6h
        - Bổ sung nếu giảm <1.0 mg/dL
        
        **Lưu ý:**
        - Insulin có thể làm giảm phosphate
        - Theo dõi sát trong 12-24h đầu
        """)
    
    st.markdown("---")
    st.markdown("### 7️⃣ Cerebral Edema Prevention (Pediatric)")
    
    st.warning("""
    **⚠️ QUAN TRỌNG: Phòng ngừa cerebral edema ở trẻ em**
    
    **Yếu tố nguy cơ:**
    - Tuổi <5 tuổi (đặc biệt <3 tuổi)
    - Na⁺ giảm nhanh (>5 mEq/L trong 4h)
    - Bù dịch quá nhanh
    
    **Phòng ngừa:**
    1. **Bù dịch chậm:** Không quá 20 ml/kg trong giờ đầu
    2. **Theo dõi Na⁺:** Mỗi 2h trong 6h đầu
    3. **Tránh Na⁺ giảm >5 mEq/L:** Giảm tốc độ truyền dịch nếu cần
    4. **Theo dõi neurologic:** Mỗi 1h trong 12h đầu
    
    **Dấu hiệu cảnh báo:**
    - Headache, confusion, irritability, vomiting
    - Nếu có: Dừng dịch, đánh giá ngay
    
    **Xem chi tiết ở phần Severe DKA**
    """)
    
    st.markdown("---")
    st.markdown("### 8️⃣ Monitoring")
    
    st.info("""
    **Labs:**
    - Glucose: Mỗi 1-2h
    - ABG/VBG: Mỗi 2-4h
    - Electrolytes: Mỗi 4h (Na⁺ mỗi 2h trong 6h đầu nếu trẻ em)
    - Ketones: Mỗi 4-6h
    - Phosphate: Mỗi 4-6h (nếu <1.5)
    - Ca²⁺: Mỗi 4-6h (nếu bổ sung phosphate)
    
    **Clinical:**
    - Dấu hiệu sống mỗi 1-2h
    - Mental status (mỗi 1h nếu trẻ em)
    - UO
    - Neurologic exam (nếu trẻ em)
    """)
    
    st.markdown("---")
    st.markdown("### 9️⃣ Resolution Criteria")
    
    st.success("""
    **DKA resolved khi:**
    - pH >7.3
    - HCO₃⁻ >18
    - Anion gap <12
    - Glucose <250 (có thể chuyển SC insulin)
    
    **Timing:** Thường 12-24h
    """)


def render_severe_dka():
    """Severe DKA Management"""
    
    st.error("## 🚨🚨 SEVERE DKA PROTOCOL - ICU")
    
    st.markdown("### Criteria:")
    st.error("""
    - pH: <7.00
    - HCO₃⁻: <10 mEq/L
    - Anion gap: >15
    - Mental status: Obtunded, coma
    - OR: Hemodynamic instability
    """)
    
    st.markdown("---")
    st.markdown("### 1️⃣ Immediate ICU Care")
    
    st.error("""
    **< 30 Minutes:**
    
    1. ✅ **ICU admission**
    2. ✅ **2 IV lines** (16-18G)
    3. ✅ **Arterial line** (nếu shock)
    4. ✅ **Foley catheter**
    5. ✅ **Labs ngay:**
       * Glucose, ABG, CBC, CMP
       * Lactate, ketones
       * Troponin (không loại trừ MI)
    6. ✅ **ECG** (tìm hypokalemia, MI)
    7. ✅ **Chest X-ray** (nếu respiratory distress)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Aggressive Resuscitation")
    
    st.error("""
    **Fluid:**
    - **Bolus:** 1-2L NS trong 30-60 phút
    - **Sau đó:** Aggressive hydration
    - **Monitor:** CVP, UO, Na trends
    
    **Insulin:**
    - **IV:** 0.1 U/kg/h (NO bolus!)
    - **Titrate:** Aggressively để control glucose
    - **Add D5W/D10W:** Khi glucose <250
    
    **K⁺:**
    - **Check ngay và thường xuyên**
    - **Replace aggressively** (20-40 mEq/L)
    - **Theo dõi ECG**
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Bicarbonate Therapy")
    
    st.markdown("#### 📋 Khi nào DÙNG Bicarbonate:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **✅ CHỈ ĐỊNH (Dùng):**
        
        1. **pH <6.9** với:
           - Hemodynamic instability (shock)
           - Không đáp ứng với insulin + fluids
           - Cardiac dysfunction
        
        2. **pH <7.0** với:
           - Severe cardiac arrhythmias
           - Severe respiratory depression
           - Coma/obtundation
        
        3. **Hyperkalemia nặng** với acidosis
        """)
    
    with col2:
        st.success("""
        **❌ CHỐNG CHỈ ĐỊNH (KHÔNG dùng):**
        
        1. **pH ≥7.0** và stable
        2. **pH >7.0** không có instability
        3. **Anuria/oliguria nặng**
        4. **Hypocalcemia nặng**
        5. **Trẻ em:** Tăng nguy cơ cerebral edema
        """)
    
    st.markdown("---")
    
    st.warning("""
    **⚠️ LƯU Ý ĐẶC BIỆT Ở TRẺ EM:**
    
    Bicarbonate **TĂNG NGUY CƠ** cerebral edema ở trẻ em!
    - Chỉ dùng khi **thực sự cần thiết** (pH <6.9 với instability)
    - Tránh dùng nếu có thể
    - Theo dõi neurologic status sát nếu dùng
    """)
    
    st.error("""
    **Nếu có chỉ định bicarbonate:**
    
    **Liều:**
    - **50-100 mEq NaHCO₃** pha trong 500ml D5W
    - **Truyền trong 1-2 giờ** (không nhanh hơn!)
    - **Mục tiêu:** pH 7.1-7.2 (KHÔNG normalize hoàn toàn!)
    
    **⚠️ Tác dụng phụ:**
    1. **Hypokalemia:** Check K⁺ mỗi 2h
    2. **Cerebral edema:** Đặc biệt ở trẻ em
    3. **Paradoxical CSF acidosis**
    4. **Overcorrection:** Tránh normalize pH quá nhanh
    
    **Monitoring:**
    - ABG/VBG mỗi 1-2h sau khi cho
    - K⁺ mỗi 2h
    - Neurologic status mỗi 1h (nếu trẻ em)
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Cerebral Edema Prevention (Pediatric Focus)")
    
    st.error("""
    **⚠️⚠️⚠️ CEREBRAL EDEMA - BIẾN CHỨNG NGUY HIỂM NHẤT Ở TRẺ EM ⚠️⚠️⚠️**
    
    **Tỷ lệ tử vong:** 20-25% nếu xảy ra
    **Tỷ lệ tàn tật:** 15-25% sống sót
    """)
    
    st.markdown("#### 🎯 Yếu tố nguy cơ:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Yếu tố nguy cơ cao:**
        1. **Tuổi <5 tuổi** (đặc biệt <3 tuổi)
        2. **Na⁺ giảm nhanh** (>5 mEq/L trong 4h đầu)
        3. **Bù dịch quá nhanh** (>50ml/kg trong 4h đầu)
        4. **HCO₃⁻ bình thường/thấp** khi nhập viện
        5. **Bicarbonate therapy** (có thể làm nặng thêm)
        6. **Severe acidosis** ban đầu
        """)
    
    with col2:
        st.info("""
        **Dấu hiệu sớm (cần phát hiện ngay!):**
        1. **Headache** (đau đầu)
        2. **Confusion** (lú lẫn)
        3. **Irritability** (kích thích)
        4. **Lethargy** (li bì)
        5. **Vomiting** (nôn)
        6. **Bradycardia** (nhịp chậm)
        
        **Dấu hiệu muộn (nguy hiểm!):**
        - Seizures (co giật)
        - Coma (hôn mê)
        - Fixed/dilated pupils
        - Cushing triad (HTN, bradycardia, irregular breathing)
        """)
    
    st.markdown("---")
    st.markdown("#### 🛡️ PHÒNG NGỪA CEREBRAL EDEMA:")
    
    st.success("""
    **1. Bù dịch CHẬM và THẬN TRỌNG:**
    
    **Trẻ em (<18 tuổi):**
    - **Giờ 1:** 10-20 ml/kg NS (không quá 20 ml/kg!)
    - **Giờ 2-4:** 5-10 ml/kg/h
    - **Sau 4h:** 2.5-5 ml/kg/h
    - **Tổng:** Không quá 50 ml/kg trong 4h đầu
    
    **Người lớn:**
    - Có thể bù nhanh hơn nhưng vẫn cẩn thận
    - Tránh Na⁺ giảm >5 mEq/L trong 4h
    
    **2. Theo dõi Na⁺ sát:**
    - Check Na⁺ mỗi 2h trong 6h đầu
    - **Nếu Na⁺ giảm >5 mEq/L trong 4h:** 
      * Giảm tốc độ truyền dịch
      * Cân nhắc dùng NS 0.9% thay vì 0.45%
      * Theo dõi neurologic status
    
    **3. TRÁNH bicarbonate (trừ khi pH <6.9):**
    - Bicarbonate có thể làm tăng nguy cơ cerebral edema
    - Chỉ dùng khi thực sự cần thiết
    
    **4. Điều chỉnh glucose CHẬM:**
    - Mục tiêu: Glucose giảm 50-75 mg/dL/h
    - Tránh giảm quá nhanh (>100 mg/dL/h)
    - Khi glucose <250: Add D5W/D10W (không ngừng insulin!)
    
    **5. Theo dõi neurologic status:**
    - **Mỗi 1h** trong 12h đầu
    - Đánh giá: GCS, pupils, reflexes
    - Nếu có dấu hiệu bất thường: Dừng ngay và đánh giá
    """)
    
    st.markdown("---")
    st.markdown("#### 🚨 XỬ TRÍ KHI CÓ CEREBRAL EDEMA:")
    
    st.error("""
    **Nếu nghi ngờ cerebral edema:**
    
    1. **DỪNG NGAY truyền dịch** (hoặc giảm xuống maintenance)
    
    2. **Mannitol:**
       - **0.5-1 g/kg IV** trong 15-30 phút
       - Có thể lặp lại sau 2h nếu cần
       - Theo dõi osmolality (không để >320 mOsm/kg)
    
    3. **Hypertonic Saline (3%):**
       - **5-10 ml/kg** IV trong 30 phút
       - Có thể dùng thay thế hoặc kết hợp với mannitol
    
    4. **Hyperventilation:**
       - Mục tiêu: PaCO₂ 25-30 mmHg
       - Chỉ dùng nếu đang thở máy
       - Tránh hyperventilation quá mức
    
    5. **Elevate head:** 30° (nếu không có shock)
    
    6. **Gọi ngay:** Neurosurgery, ICU, Neurology
    
    7. **CT scan:** Nếu stable để chẩn đoán
    
    **⚠️ QUAN TRỌNG:** Phòng ngừa tốt hơn điều trị!
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Other Complications to Watch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **Hypokalemia:**
        - Xảy ra sau insulin (đẩy K⁺ vào tế bào)
        - Check K⁺ mỗi 2-4h
        - Bổ sung ngay nếu <3.5
        
        **Hypophosphatemia:**
        - Xảy ra sau insulin
        - Check phosphate mỗi 4-6h
        - Bổ sung nếu <1.0 mg/dL
        """)
    
    with col2:
        st.warning("""
        **Hypoglycemia:**
        - Khi glucose <250
        - Add D5W/D10W
        - Don't stop insulin!
        
        **Hyponatremia:**
        - Do hyperglycemia (pseudohyponatremia)
        - Corrected Na = Na + 1.6 × (Glucose - 100)/100
        - Theo dõi sát để phát hiện cerebral edema
        """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Monitoring")
    
    st.info("""
    **ICU Monitoring:**
    - ECG liên tục
    - Arterial BP
    - CVP (nếu cần)
    - Pulse oximetry
    
    **Labs:**
    - Glucose: Mỗi 1h
    - ABG: Mỗi 2-4h
    - Electrolytes: Mỗi 2-4h
    - Ketones: Mỗi 4h
    
    **Clinical:**
    - Neurologic checks mỗi 1-2h
    - Dấu hiệu sống liên tục
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Resolution & Transition")
    
    st.success("""
    **When stable:**
    - pH >7.3
    - HCO₃⁻ >18
    - Hemodynamically stable
    - Transition to floor
    
    **When eating:**
    - Switch to SC insulin
    - Overlap IV and SC
    
    **Timing:** Usually 24-48h
    """)
    
    # References section
    references = get_references("DKA")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

