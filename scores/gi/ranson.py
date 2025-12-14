"""
Ranson Criteria
Tiên lượng viêm tụy cấp (Acute Pancreatitis)
"""

import streamlit as st


def calculate_ranson(criteria_admission, criteria_48h):
    """
    Calculate Ranson score
    
    Args:
        criteria_admission: Number of criteria met at admission (0-5)
        criteria_48h: Number of criteria met at 48 hours (0-6)
    
    Returns:
        dict: Ranson score and interpretation
    """
    total_score = criteria_admission + criteria_48h
    
    return {
        "admission_criteria": criteria_admission,
        "criteria_48h": criteria_48h,
        "total_score": total_score
    }


def interpret_ranson(total_score):
    """
    Interpret Ranson score
    
    Returns mortality risk
    """
    if total_score < 3:
        return {
            "severity": "Nhẹ",
            "color": "🟢",
            "mortality": "< 1%",
            "recommendation": "Điều trị nội khoa thường quy. Theo dõi",
            "icu_need": "Không cần ICU (thường)",
            "level": "mild"
        }
    elif total_score <= 5:
        return {
            "severity": "Trung bình",
            "color": "🟡",
            "mortality": "10-20%",
            "recommendation": "Theo dõi chặt. Cân nhắc ICU/HDU",
            "icu_need": "Xem xét ICU/HDU",
            "level": "moderate"
        }
    else:  # ≥ 6
        return {
            "severity": "Nặng",
            "color": "🔴",
            "mortality": "> 50%",
            "recommendation": "ICU care. Điều trị tích cực. Xem xét can thiệp",
            "icu_need": "CẦN ICU",
            "level": "severe"
        }


def render():
    """Render the Ranson Criteria calculator"""
    
    st.title("🏥 Ranson Criteria")
    st.markdown("""
    ### Tiên lượng viêm tụy cấp
    
    **Ranson Criteria:**
    - Tiên lượng mức độ nặng viêm tụy cấp
    - 11 tiêu chí: 5 lúc nhập viện + 6 sau 48h
    - Điểm từ 0-11
    - Dự đoán tử vong và cần ICU
    
    **2 Bộ Tiêu chí:**
    - **Lúc nhập viện (0h):** 5 tiêu chí
    - **Sau 48 giờ:** 6 tiêu chí
    
    **Phân loại:**
    - **< 3:** Viêm tụy nhẹ (tử vong < 1%)
    - **3-5:** Viêm tụy trung bình (tử vong 10-20%)
    - **≥ 6:** Viêm tụy nặng (tử vong > 50%)
    
    **Lưu ý:**
    - Cần CHỜ 48H để tính đủ điểm
    - Không dùng được ngay lúc nhập viện
    - Atlanta classification và CT severity index là alternatives
    """)
    
    st.markdown("---")
    
    # Important note about etiology
    st.info("""
    **⚠️ Lưu ý quan trọng:**
    
    Ranson Criteria có 2 BỘ KHÁC NHAU:
    - **Gallstone (sỏi mật) pancreatitis:** 1 bộ tiêu chí
    - **Non-gallstone (không sỏi) pancreatitis:** 1 bộ tiêu chí khác
    
    Hệ thống này áp dụng cho **NON-GALLSTONE pancreatitis** (rượu, idiopathic, etc.)
    """)
    
    st.markdown("---")
    
    # Admission criteria (0h)
    st.subheader("📋 Tiêu chí lúc nhập viện (0h)")
    st.markdown("### 5 Tiêu chí ban đầu")
    
    admission_count = 0
    
    # 1. Age
    st.markdown("#### 1️⃣ Tuổi > 55")
    age_gt_55 = st.checkbox("Tuổi > 55", key="ranson_age")
    if age_gt_55:
        admission_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # 2. WBC
    st.markdown("#### 2️⃣ WBC > 16,000/mm³")
    wbc_gt_16 = st.checkbox("WBC > 16,000/mm³ (> 16 × 10⁹/L)", key="ranson_wbc")
    if wbc_gt_16:
        admission_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # 3. Glucose
    st.markdown("#### 3️⃣ Glucose > 200 mg/dL")
    glucose_gt_200 = st.checkbox("Glucose > 200 mg/dL (> 11.1 mmol/L)", key="ranson_glucose")
    if glucose_gt_200:
        admission_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # 4. LDH
    st.markdown("#### 4️⃣ LDH > 350 U/L")
    ldh_gt_350 = st.checkbox("LDH > 350 U/L", key="ranson_ldh")
    if ldh_gt_350:
        admission_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # 5. AST
    st.markdown("#### 5️⃣ AST > 250 U/L")
    ast_gt_250 = st.checkbox("AST (SGOT) > 250 U/L", key="ranson_ast")
    if ast_gt_250:
        admission_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # Summary admission
    st.metric("Tổng Điểm Lúc Nhập Viện", f"{admission_count}/5")
    
    st.markdown("---")
    st.markdown("---")
    
    # 48-hour criteria
    st.subheader("📋 Tiêu chí sau 48 giờ")
    st.markdown("### 6 Tiêu chí Tại 48h")
    
    st.warning("""
    **⏱️ Cần chờ 48 giờ từ khi nhập viện để đánh giá đầy đủ**
    
    So sánh labs tại 48h với labs lúc nhập viện để tính "thay đổi" (delta)
    """)
    
    criteria_48h_count = 0
    
    # 1. Hematocrit fall
    st.markdown("#### 6️⃣ Hematocrit giảm > 10%")
    st.caption("So với giá trị lúc nhập viện")
    hct_fall = st.checkbox("Hematocrit giảm > 10% (points)", key="ranson_hct")
    if hct_fall:
        criteria_48h_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # 2. BUN rise
    st.markdown("#### 7️⃣ BUN tăng > 5 mg/dL")
    st.caption("Tăng so với lúc nhập viện")
    bun_rise = st.checkbox("BUN tăng > 5 mg/dL (> 1.8 mmol/L)", key="ranson_bun")
    if bun_rise:
        criteria_48h_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # 3. Calcium
    st.markdown("#### 8️⃣ Calcium < 8 mg/dL")
    st.caption("Tại thời điểm 48h")
    ca_lt_8 = st.checkbox("Calcium < 8 mg/dL (< 2 mmol/L)", key="ranson_ca")
    if ca_lt_8:
        criteria_48h_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # 4. PaO2
    st.markdown("#### 9️⃣ PaO₂ < 60 mmHg")
    st.caption("Tại thời điểm 48h")
    pao2_lt_60 = st.checkbox("PaO₂ < 60 mmHg (< 8 kPa)", key="ranson_pao2")
    if pao2_lt_60:
        criteria_48h_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # 5. Base deficit
    st.markdown("#### 🔟 Base deficit > 4 mEq/L")
    st.caption("Acidosis chuyển hóa tại 48h")
    base_deficit = st.checkbox("Base deficit > 4 mEq/L", key="ranson_base")
    if base_deficit:
        criteria_48h_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # 6. Fluid sequestration
    st.markdown("#### 1️⃣1️⃣ Fluid sequestration > 6 L")
    st.caption("Lượng dịch truyền để duy trì huyết động trong 48h đầu")
    fluid_seq = st.checkbox("Fluid sequestration > 6 L", key="ranson_fluid")
    if fluid_seq:
        criteria_48h_count += 1
        st.success("✅ +1 điểm")
    
    st.markdown("---")
    
    # Summary 48h
    st.metric("Tổng Điểm Sau 48h", f"{criteria_48h_count}/6")
    
    st.markdown("---")
    
    # Calculate button
    if st.button("📊 Tính Ranson Score", type="primary", use_container_width=True):
        # Calculate
        result = calculate_ranson(admission_count, criteria_48h_count)
        total_score = result['total_score']
        
        # Get interpretation
        interp = interpret_ranson(total_score)
        
        st.markdown("---")
        st.subheader("📈 Kết quả")
        
        # Display scores
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Lúc Nhập Viện",
                f"{admission_count}/5",
                help="Tiêu chí tại 0h"
            )
        
        with col2:
            st.metric(
                "Sau 48 Giờ",
                f"{criteria_48h_count}/6",
                help="Tiêu chí tại 48h"
            )
        
        with col3:
            st.metric(
                "Ranson Score",
                f"{total_score}/11",
                help="Tổng điểm"
            )
        
        st.markdown("---")
        
        # Severity
        if interp['level'] == "mild":
            st.success(f"{interp['color']} Viêm Tụy {interp['severity']}")
        elif interp['level'] == "moderate":
            st.warning(f"{interp['color']} Viêm Tụy {interp['severity']}")
        else:
            st.error(f"{interp['color']} Viêm Tụy {interp['severity']}")
        
        st.markdown("---")
        
        # Interpretation
        st.subheader("🎯 Phân tích & Tiên lượng")
        
        st.info(f"""
        **Ranson Score: {total_score}/11**
        
        **Mức độ nặng:** {interp['severity']}
        
        **Tử vong dự đoán:** {interp['mortality']}
        
        **ICU:** {interp['icu_need']}
        
        **Khuyến nghị:** {interp['recommendation']}
        """)
        
        # Detailed management
        st.markdown("---")
        st.subheader("💡 Xử Trí")
        
        if total_score < 3:
            st.success("""
            ### ✅ Viêm Tụy Nhẹ (Ranson < 3)
            
            **Tiên lượng tốt:**
            - Tử vong < 1%
            - Thường tự khỏi
            - Nội trú điều trị nội khoa
            
            **Xử trí:**
            
            **1. NPO (Nhịn ăn):**
            - NPO ban đầu
            - Feeding khi đau giảm, amylase giảm
            - Low-fat diet khi bắt đầu ăn lại
            
            **2. Dịch truyền:**
            - IV fluids aggressive (Ringer lactate preferred)
            - 250-500 mL/h ban đầu
            - Mục tiêu: UOP > 0.5 mL/kg/h
            
            **3. Giảm đau:**
            - Opioids OK (morphine không tăng sphincter Oddi như trước nghĩ)
            - NSAIDs tránh (nguy cơ renal)
            
            **4. Monitoring:**
            - Vital signs
            - I/O chart
            - Labs hàng ngày (CBC, BUN/Cr, Ca, LFT, amylase/lipase)
            
            **5. Điều trị nguyên nhân:**
            - Gallstone pancreatitis → ERCP hoặc cholecystectomy
            - Alcohol → Counseling, thiamine
            - Hypertriglyceridemia → Fenofibrate, insulin (nếu TG > 1000)
            
            **Xuất viện:**
            - Khi ăn uống được
            - Đau giảm
            - Amylase/lipase giảm
            - Không sốt
            """)
        
        elif total_score <= 5:
            st.warning("""
            ### ⚠️ Viêm Tụy Trung Bình (Ranson 3-5)
            
            **Tiên lượng cẩn trọng:**
            - Tử vong 10-20%
            - Nguy cơ biến chứng
            - Cần monitoring chặt
            
            **Xử trí:**
            
            **1. Nơi điều trị:**
            - Xem xét ICU hoặc HDU (High Dependency Unit)
            - Monitor chặt chẽ
            
            **2. Dịch truyền tích cực:**
            - Aggressive IV fluids
            - Goal-directed therapy
            - CVP monitoring nếu cần
            
            **3. Nutritional support:**
            - NPO ban đầu
            - Enteral nutrition ưu tiên (qua NG/NJ tube)
            - TPN nếu không dung nạp enteral
            - Early feeding (< 48-72h) tốt hơn delayed
            
            **4. Monitoring:**
            - Vital signs liên tục
            - UOP hourly
            - Labs 6-12h
            - Imaging theo dõi (CT nếu tiến triển xấu)
            
            **5. Antibiotics:**
            - KHÔNG prophylactic routine
            - Chỉ khi có infection (cholangitis, infected necrosis)
            - Nếu dùng: Carbapenem hoặc quinolone
            
            **6. ERCP:**
            - Nếu gallstone pancreatitis + cholangitis
            - Hoặc biliary obstruction
            - Trong 72h
            
            **7. Biến chứng:**
            - Monitor cho ARDS, AKI, DIC
            - Pancreatic necrosis (CT sau 48-72h)
            - Pseudocyst formation
            """)
        
        else:  # ≥ 6
            st.error("""
            ### 🚨 Viêm Tụy Nặng (Ranson ≥ 6)
            
            **Tiên lượng nặng:**
            - Tử vong > 50%
            - Nguy cơ cao biến chứng nặng
            - CẦN ICU care
            
            **Xử trí ICU:**
            
            **1. Nội trú ICU:**
            - Monitoring chặt chẽ
            - Invasive monitoring (A-line, CVP)
            - Hourly vitals, UOP
            
            **2. Resuscitation:**
            - Aggressive fluid resuscitation
            - 5-10 L trong 24h đầu thường cần
            - Ringer lactate preferred
            - Vasopressors nếu shock
            - Blood products nếu cần
            
            **3. Respiratory support:**
            - Oxygen therapy
            - HFNC, NIV nếu hypoxia
            - Intubation + MV nếu ARDS
            
            **4. Renal support:**
            - CRRT nếu AKI nặng
            - Monitor electrolytes chặt (Ca, Mg)
            
            **5. Nutrition:**
            - Enteral nutrition ưu tiên (NG/NJ)
            - Bắt đầu sớm (< 48h)
            - TPN nếu enteral fail
            
            **6. Antibiotics:**
            - Prophylaxis KHÔNG recommend (guidelines)
            - Nhưng thực tế nhiều nơi dùng
            - Chỉ định rõ ràng: Infected necrosis, cholangitis
            - Choice: Carbapenem (meropenem, imipenem)
            
            **7. Imaging:**
            - CT contrast-enhanced tại 48-72h
            - Đánh giá necrosis
            - Repeat CT nếu tiến triển xấu
            
            **8. Can thiệp:**
            - **ERCP + sphincterotomy:** Nếu gallstone + cholangitis
            - **Percutaneous drainage:** Nếu infected collection
            - **Necrosectomy:** Nếu infected necrosis (sau 4 tuần nếu có thể)
            - Step-up approach (drain trước, surgery sau)
            
            **9. Biến chứng:**
            - **ARDS:** Common, MV support
            - **AKI:** CRRT
            - **Infected necrosis:** Antibiotics + drainage/necrosectomy
            - **Pseudocyst:** Drain nếu infected/symptomatic
            - **Pancreatic abscess:** Drainage
            - **GI bleeding:** Từ stress ulcer, pseudoaneurysm
            - **DIC:** Blood products, treat underlying
            
            **10. Prognosis:**
            - Mortality rất cao
            - Infected necrosis: Mortality 30-40%
            - Multi-organ failure: Mortality > 50%
            """)
        
        # Criteria interpretation
        with st.expander("📋 Giải thích Từng Tiêu chí"):
            st.markdown(f"""
            ### Tiêu chí lúc nhập viện ({admission_count}/5):
            
            1. **Age > 55:** {'✅' if age_gt_55 else '❌'}
               - Tuổi cao → Tiên lượng xấu hơn
            
            2. **WBC > 16,000:** {'✅' if wbc_gt_16 else '❌'}
               - Phản ứng viêm nặng
            
            3. **Glucose > 200:** {'✅' if glucose_gt_200 else '❌'}
               - Stress hyperglycemia
               - Có thể insulin resistance do inflammation
            
            4. **LDH > 350:** {'✅' if ldh_gt_350 else '❌'}
               - Marker tissue damage
            
            5. **AST > 250:** {'✅' if ast_gt_250 else '❌'}
               - Liver involvement
               - Đặc biệt cao trong gallstone pancreatitis
            
            ### Tiêu chí sau 48h ({criteria_48h_count}/6):
            
            6. **Hct fall > 10%:** {'✅' if hct_fall else '❌'}
               - Sequestration vào third space
               - Hemorrhage
            
            7. **BUN rise > 5:** {'✅' if bun_rise else '❌'}
               - Prerenal AKI (hypovolemia)
               - Protein catabolism
            
            8. **Ca < 8:** {'✅' if ca_lt_8 else '❌'}
               - Saponification (Ca kết tủa với fat necrosis)
               - Hypoalbuminemia
               - PTH resistance
            
            9. **PaO₂ < 60:** {'✅' if pao2_lt_60 else '❌'}
               - ARDS, pleural effusion
               - Atelectasis
            
            10. **Base deficit > 4:** {'✅' if base_deficit else '❌'}
                - Metabolic acidosis
                - Lactic acidosis từ hypoperfusion
            
            11. **Fluid sequestration > 6L:** {'✅' if fluid_seq else '❌'}
                - Third-spacing massive
                - Marker của necrotizing pancreatitis
            """)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("🆚 So sánh các hệ thống tiên lượng"):
        st.markdown("""
        ### Ranson vs APACHE II vs Atlanta:
        
        | Hệ thống | Ưu điểm | Nhược điểm | Timing |
        |----------|---------|------------|--------|
        | **Ranson** | Đơn giản, validate tốt | Cần 48h, không đặc hiệu | 48h |
        | **APACHE II** | Tính được ngay, update hàng ngày | Phức tạp hơn | Mọi lúc |
        | **Atlanta** | Clinical + imaging, toàn diện | Cần CT | 48-72h |
        | **BISAP** | Đơn giản, 24h | Mới hơn, ít validate | 24h |
        | **CT Severity Index** | Đánh giá necrosis | Cần CT, không sớm | 48-72h |
        
        **Khi nào dùng Ranson?**
        - Có đủ 48h
        - Muốn prognostication
        - Tư vấn gia đình
        - Research
        
        **Khi nào dùng APACHE II?**
        - Cần đánh giá sớm
        - ICU scoring
        - Update hàng ngày
        
        **Atlanta Classification (2012):**
        - **Mild:** Không organ failure, không local/systemic complications
        - **Moderate:** Organ failure < 48h và/hoặc local/systemic complications
        - **Severe:** Organ failure > 48h
        """)
    
    with st.expander("🔬 Pathophysiology"):
        st.markdown("""
        ### Cơ chế bệnh sinh viêm tụy cấp:
        
        **Khởi phát:**
        1. Premature activation của trypsinogen → trypsin trong tụy
        2. Trypsin kích hoạt các enzyme khác
        3. Autodigestion của tụy
        
        **Tiến triển:**
        1. **Local inflammation:**
           - Edema
           - Fat necrosis
           - Hemorrhage
           - Parenchymal necrosis
        
        2. **Systemic inflammation (SIRS):**
           - Cytokine release (IL-1, IL-6, TNF-α)
           - Complement activation
           - Neutrophil activation
           - Endothelial injury
        
        3. **Multi-organ dysfunction:**
           - **ARDS:** Capillary leak, ARDS
           - **AKI:** ATN từ hypoperfusion
           - **Cardiovascular:** Distributive shock
           - **GI:** Ileus, bleeding
           - **Metabolic:** Hyperglycemia, hypocalcemia
           - **Hematologic:** DIC
        
        **Phân loại:**
        - **Interstitial edematous (80%):** Nhẹ, tự khỏi
        - **Necrotizing (20%):** Nặng, tử vong cao
        
        **Biến chứng:**
        - **Early (< 2 weeks):** SIRS, organ failure
        - **Late (> 2 weeks):** Infection, pseudocyst, abscess
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Ranson JH, et al. Prognostic signs and the role of operative management in acute pancreatitis. Surg Gynecol Obstet. 1974;139(1):69-81
    - Banks PA, et al. Classification of acute pancreatitis—2012: revision of the Atlanta classification. Gut. 2013;62(1):102-111
    - Tenner S, et al. American College of Gastroenterology guideline: management of acute pancreatitis. Am J Gastroenterol. 2013;108(9):1400-1415
    """)


if __name__ == "__main__":
    render()

