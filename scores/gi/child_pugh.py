"""
Child-Pugh Score for Cirrhosis Severity
Đánh giá mức độ nặng xơ gan

Scoring Components:
1. Total Bilirubin
2. Serum Albumin
3. INR
4. Ascites
5. Hepatic Encephalopathy

Total score: 5-15 points
- Class A (5-6): Well-compensated
- Class B (7-9): Significant functional compromise
- Class C (10-15): Decompensated disease

Reference:
Pugh RN, et al. Transection of the oesophagus for bleeding oesophageal varices.
Br J Surg. 1973;60(8):646-9.
"""

import streamlit as st


def render():
    """Render Child-Pugh Score Calculator"""
    
    st.subheader("🩸 Child-Pugh Score")
    st.caption("Đánh giá mức độ nặng xơ gan")
    
    st.markdown("""
    **Child-Pugh Score** phân loại mức độ nặng của xơ gan và tiên lượng.
    
    **Ứng dụng:**
    - Đánh giá mức độ suy gan
    - Quyết định điều trị (phẫu thuật, ghép gan)
    - Tiên lượng tử vong
    """)
    
    st.markdown("---")
    
    # Initialize score
    total_score = 0
    score_breakdown = {}
    
    # Input section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔬 Xét nghiệm")
        
        # 1. Total Bilirubin
        st.markdown("#### 1. Bilirubin Toàn Phần")
        
        bili_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "µmol/L (SI)"],
            horizontal=True,
            key="bili_unit"
        )
        
        if "mg/dL" in bili_unit:
            bili = st.number_input(
                "Bilirubin (mg/dL):",
                min_value=0.0,
                max_value=30.0,
                value=1.0,
                step=0.1,
                help="Bình thường: 0.3-1.2 mg/dL"
            )
            bili_mgdl = bili
            st.caption(f"≈ {round(bili * 17.1)} µmol/L")
        else:
            bili = st.number_input(
                "Bilirubin (µmol/L):",
                min_value=0.0,
                max_value=500.0,
                value=17.0,
                step=1.0,
                help="Bình thường: 5-21 µmol/L"
            )
            bili_mgdl = bili / 17.1
            st.caption(f"≈ {_format_num(bili_mgdl, 1)} mg/dL")
        
        # Score bilirubin
        if bili_mgdl < 2:
            bili_score = 1
            bili_level = "<2 mg/dL"
        elif bili_mgdl <= 3:
            bili_score = 2
            bili_level = "2-3 mg/dL"
        else:
            bili_score = 3
            bili_level = ">3 mg/dL"
        
        total_score += bili_score
        score_breakdown["Bilirubin"] = bili_score
        
        if bili_score == 1:
            st.success(f"✅ {bili_level} → +{bili_score} điểm")
        elif bili_score == 2:
            st.warning(f"⚠️ {bili_level} → +{bili_score} điểm")
        else:
            st.error(f"🔴 {bili_level} → +{bili_score} điểm")
        
        # 2. Albumin
        st.markdown("#### 2. Albumin")
        albumin = st.number_input(
            "Albumin (g/dL):",
            min_value=1.0,
            max_value=6.0,
            value=3.5,
            step=0.1,
            format="%.1f",
            help="Bình thường: 3.5-5.5 g/dL"
        )
        st.caption(f"≈ {round(albumin * 10)} g/L")
        
        # Score albumin
        if albumin > 3.5:
            alb_score = 1
            alb_level = ">3.5 g/dL"
        elif albumin >= 2.8:
            alb_score = 2
            alb_level = "2.8-3.5 g/dL"
        else:
            alb_score = 3
            alb_level = "<2.8 g/dL"
        
        total_score += alb_score
        score_breakdown["Albumin"] = alb_score
        
        if alb_score == 1:
            st.success(f"✅ {alb_level} → +{alb_score} điểm")
        elif alb_score == 2:
            st.warning(f"⚠️ {alb_level} → +{alb_score} điểm")
        else:
            st.error(f"🔴 {alb_level} → +{alb_score} điểm")
        
        # 3. INR
        st.markdown("#### 3. INR")
        inr = st.number_input(
            "INR (International Normalized Ratio):",
            min_value=0.8,
            max_value=10.0,
            value=1.0,
            step=0.1,
            help="Bình thường: 0.9-1.1"
        )
        
        # Score INR
        if inr < 1.7:
            inr_score = 1
            inr_level = "<1.7"
        elif inr <= 2.3:
            inr_score = 2
            inr_level = "1.7-2.3"
        else:
            inr_score = 3
            inr_level = ">2.3"
        
        total_score += inr_score
        score_breakdown["INR"] = inr_score
        
        if inr_score == 1:
            st.success(f"✅ {inr_level} → +{inr_score} điểm")
        elif inr_score == 2:
            st.warning(f"⚠️ {inr_level} → +{inr_score} điểm")
        else:
            st.error(f"🔴 {inr_level} → +{inr_score} điểm")
    
    with col2:
        st.markdown("### 🩺 Lâm Sàng")
        
        # 4. Ascites
        st.markdown("#### 4. Cổ Chướng (Ascites)")
        ascites = st.radio(
            "Mức độ cổ chướng:",
            [
                "Không có",
                "Nhẹ (mild) - Kiểm soát được bằng lợi tiểu",
                "Trung bình đến nặng (moderate-severe) - Khó kiểm soát"
            ],
            help="Đánh giá qua khám lâm sàng và siêu âm"
        )
        
        if "Không" in ascites:
            asc_score = 1
            st.success("✅ Không cổ chướng → +1 điểm")
        elif "Nhẹ" in ascites:
            asc_score = 2
            st.warning("⚠️ Cổ chướng nhẹ → +2 điểm")
        else:
            asc_score = 3
            st.error("🔴 Cổ chướng trung bình-nặng → +3 điểm")
        
        total_score += asc_score
        score_breakdown["Ascites"] = asc_score
        
        # 5. Hepatic Encephalopathy
        st.markdown("#### 5. Bệnh Não Gan (Hepatic Encephalopathy)")
        
        st.info("""
        **West Haven Criteria:**
        - **Grade 0:** Không có
        - **Grade 1-2:** Nhẹ (lú lẫn nhẹ, thay đổi tính cách, rối loạn giấc ngủ)
        - **Grade 3-4:** Nặng (lơ mơ, hôn mê)
        """)
        
        enceph = st.radio(
            "Mức độ bệnh não gan:",
            [
                "Không có (Grade 0)",
                "Grade 1-2 (Nhẹ - kiểm soát được)",
                "Grade 3-4 (Nặng - khó kiểm soát)"
            ],
            help="Đánh giá theo West Haven Criteria"
        )
        
        if "Không" in enceph:
            enc_score = 1
            st.success("✅ Không bệnh não gan → +1 điểm")
        elif "1-2" in enceph:
            enc_score = 2
            st.warning("⚠️ Bệnh não gan Grade 1-2 → +2 điểm")
        else:
            enc_score = 3
            st.error("🔴 Bệnh não gan Grade 3-4 → +3 điểm")
        
        total_score += enc_score
        score_breakdown["Encephalopathy"] = enc_score
    
    # Calculate button
    st.markdown("---")
    if st.button("🧮 Tính Child-Pugh Score", type="primary", use_container_width=True):
        
        # Determine Child-Pugh Class
        if total_score <= 6:
            cp_class = "A"
            severity = "XƠ GAN BÙ TRỪ TỐT"
            color = "green"
            survival_1yr = "100%"
            survival_2yr = "85%"
            periop_mortality = "10%"
        elif total_score <= 9:
            cp_class = "B"
            severity = "SUY CHỨC NĂNG GAN ĐÁNG KỂ"
            color = "orange"
            survival_1yr = "81%"
            survival_2yr = "57%"
            periop_mortality = "30%"
        else:
            cp_class = "C"
            severity = "XƠ GAN MẤT BÙ"
            color = "red"
            survival_1yr = "45%"
            survival_2yr = "35%"
            periop_mortality = "82%"
        
        # Display result
        st.markdown("---")
        st.markdown("## 📊 KẾT QUẢ")
        
        st.markdown(f"""
        <div style="background-color: {color}; padding: 20px; border-radius: 10px; text-align: center;">
            <h1 style="color: white; margin: 0;">Child-Pugh Class {cp_class}</h1>
            <p style="color: white; margin: 0; font-size: 1.2rem;">{total_score} điểm</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Child-Pugh Score", f"{total_score}/15")
        
        with col2:
            st.metric("Class", cp_class)
        
        with col3:
            st.metric("Sống sót 1 năm", survival_1yr)
        
        with col4:
            st.metric("Tử vong phẫu thuật", periop_mortality)
        
        st.markdown("---")
        
        # Detailed interpretation
        st.markdown("### 📋 ĐÁNH GIÁ & KHUYẾN NGHỊ")
        
        if cp_class == "A":
            st.success(f"""
            **🟢 CHILD-PUGH CLASS A ({total_score} điểm)**
            
            **Mức độ:** {severity}
            
            **Tiên lượng:**
            - Sống sót 1 năm: {survival_1yr}
            - Sống sót 2 năm: {survival_2yr}
            - Tử vong phẫu thuật bụng: {periop_mortality}
            
            **Đánh giá:** Chức năng gan còn bù trừ tốt, tiên lượng tốt.
            
            **Khuyến Nghị:**
            
            1. **Theo dõi định kỳ:**
               - Khám gan mỗi 3-6 tháng
               - Siêu âm bụng mỗi 6 tháng (sàng lọc HCC)
               - AFP mỗi 6 tháng
               - Nội soi thực quản 1-3 năm/lần (tĩnh mạch giãn)
            
            2. **Điều trị nguyên nhân:**
               - Viêm gan B: Thuốc kháng virus (Entecavir, Tenofovir)
               - Viêm gan C: Điều trị trực tiếp kháng virus (DAA)
               - Xơ gan do rượu: Cai rượu hoàn toàn
               - NASH: Giảm cân, kiểm soát đái tháo đường
            
            3. **Phòng ngừa biến chứng:**
               - Tiêm phòng viêm gan A, B (nếu chưa)
               - Tránh thuốc độc gan (NSAIDs, paracetamol liều cao)
               - Chế độ ăn: Protein đủ, hạn chế muối nếu có cổ chướng
            
            4. **Chỉ định phẫu thuật:**
               - ✅ Có thể phẫu thuật nếu cần (nguy cơ chấp nhận được)
               - Cần đánh giá kỹ và chuẩn bị chu đáo
            
            5. **Ghép gan:**
               - Chưa có chỉ định ghép gan
               - Tiếp tục điều trị bảo tồn
            
            **Tiên lượng:** Tốt với điều trị và theo dõi thích hợp.
            """)
        
        elif cp_class == "B":
            st.warning(f"""
            **🟡 CHILD-PUGH CLASS B ({total_score} điểm)**
            
            **Mức độ:** {severity}
            
            **Tiên lượng:**
            - Sống sót 1 năm: {survival_1yr}
            - Sống sót 2 năm: {survival_2yr}
            - Tử vong phẫu thuật bụng: {periop_mortality}
            
            **Đánh giá:** Chức năng gan suy giảm đáng kể, cần theo dõi sát và điều trị tích cực.
            
            **Khuyến Nghị:**
            
            1. **Theo dõi chặt chẽ:**
               - Khám gan mỗi 2-3 tháng
               - Siêu âm bụng + AFP mỗi 3-6 tháng (sàng lọc HCC)
               - Nội soi thực quản mỗi 1-2 năm
               - Theo dõi xét nghiệm: CBC, LFT, INR, creatinine
            
            2. **Điều trị tích cực:**
               - **Điều trị nguyên nhân:** Như Class A nhưng tích cực hơn
               - **Cổ chướng:**
                 * Hạn chế muối (<2g Na/ngày)
                 * Lợi tiểu: Spironolactone 100mg + Furosemide 40mg
                 * Paracentesis nếu cổ chướng căng + albumin IV
               - **Bệnh não gan:**
                 * Lactulose 20-30ml x 2-3 lần/ngày (mục tiêu 2-3 lần phân mềm/ngày)
                 * Rifaximin 550mg x 2 lần/ngày
                 * Protein: 1-1.5g/kg/ngày (KHÔNG hạn chế)
               - **Tĩnh mạch giãn:**
                 * Beta-blocker (Propranolol, Carvedilol) nếu có
                 * Nội soi thắt vòng nếu giãn độ 2-3
            
            3. **Phòng ngừa biến chứng:**
            - SBP prophylaxis: Norfloxacin 400mg/ngày nếu:
                 * Ascites + protein <1.5 g/dL
                 * Đã có SBP trước đó
               - Tránh TUYỆT ĐỐI: NSAIDs, aminoglycosides, thuốc an thần
               - Cẩn thận với thuốc chống đông
            
            4. **Chỉ định phẫu thuật:**
               - ⚠️ **Nguy cơ CAO** (tử vong ~30%)
               - Chỉ phẫu thuật khi thật cần thiết
               - Cần hội chẩn đa chuyên khoa
               - Tối ưu hóa trước phẫu thuật
            
            5. **Ghép gan:**
               - ✅ **Cân nhắc đánh giá ghép gan**
               - Tham khảo trung tâm ghép gan
               - MELD score để ưu tiên
            
            6. **Dinh dưỡng:**
               - Protein: 1.2-1.5g/kg/ngày
               - Bữa ăn nhỏ nhiều lần (4-6 lần/ngày)
               - Snack trước ngủ (phòng catabolism)
            
            **Tiên lượng:** Trung bình. Cần điều trị tích cực và cân nhắc ghép gan.
            """)
        
        else:  # Class C
            st.error(f"""
            **🔴 CHILD-PUGH CLASS C ({total_score} điểm)**
            
            **Mức độ:** {severity}
            
            **Tiên lượng:**
            - Sống sót 1 năm: {survival_1yr}
            - Sống sót 2 năm: {survival_2yr}
            - Tử vong phẫu thuật bụng: {periop_mortality}
            
            **Đánh giá:** Xơ gan mất bù nặng, tiên lượng xấu, cần điều trị tích cực và ghép gan.
            
            **Khuyến Nghị:**
            
            1. **URGENT - Đánh giá ghép gan:**
               - ✅ **Chỉ định ghép gan**
               - Liên hệ trung tâm ghép gan NGAY
               - Đánh giá tiêu chí Milan (nếu có HCC)
               - Tính MELD score (ưu tiên ghép)
            
            2. **Nhập viện/Theo dõi sát:**
               - Cân nhắc nhập viện nếu không ổn định
               - Khám gan mỗi 1-2 tháng
               - Siêu âm + AFP mỗi 3 tháng
               - Theo dõi biến chứng liên tục
            
            3. **Điều trị biến chứng tích cực:**
               
               **Cổ chướng nặng:**
               - Hạn chế muối nghiêm ngặt (<2g Na/ngày)
               - Lợi tiểu liều cao: Spironolactone 200-400mg + Furosemide 80-160mg
               - Paracentesis thường xuyên + Albumin 6-8g/L dịch rút
               - Xem xét TIPS nếu cổ chướng khó trị
               
               **Bệnh não gan:**
               - Lactulose tích cực (mục tiêu 3-4 lần phân mềm/ngày)
               - Rifaximin 550mg BID
               - Tìm và điều trị yếu tố kích phát:
                 * Nhiễm trùng (SBP, UTI, pneumonia)
                 * Táo bón
                 * GI bleeding
                 * Điện giải rối loạn
                 * Thuốc an thần
               
               **Giãn tĩnh mạch thực quản:**
               - Beta-blocker (nếu huyết áp cho phép)
               - Nội soi thắt vòng/xơ cứng
               - SBP prophylaxis: Norfloxacin 400mg/ngày
               
               **Hội chứng gan thận (HRS):**
               - Terlipressin + Albumin
               - Midodrine + Octreotide + Albumin
               - Dialysis nếu cần (cầu nối đến ghép gan)
            
            4. **Phẫu thuật:**
               - ❌ **CHỐNG CHỈ ĐỊNH phẫu thuật bụng không cấp cứu**
               - Tử vong phẫu thuật rất cao (>80%)
               - Chỉ phẫu thuật khi tính mạng bị đe dọa
            
            5. **Chăm sóc hỗ trợ:**
               - Dinh dưỡng: Protein 1.5g/kg/ngày
               - Phòng nhiễm trùng: Vệ sinh tốt, vaccine
               - Hỗ trợ tâm lý bệnh nhân và gia đình
               - Cân nhắc Palliative Care nếu không ghép gan được
            
            6. **Thảo luận với gia đình:**
               - Tiên lượng xấu
               - Tầm quan trọng của ghép gan
               - Advance directives
               - Goals of care
            
            **Tiên lượng:** Xấu. Ghép gan là phương pháp điều trị duy nhất có thể cải thiện tiên lượng.
            Nếu không ghép gan được, tỷ lệ tử vong cao trong 1-2 năm.
            """)
        
        # Score breakdown
        st.markdown("---")
        with st.expander("📊 Chi tiết điểm số"):
            st.markdown("| Thành Phần | Giá Trị | Điểm |")
            st.markdown("|------------|---------|------|")
            st.markdown(f"| **Bilirubin** | {bili_mgdl:.1f} mg/dL | {score_breakdown['Bilirubin']} |")
            st.markdown(f"| **Albumin** | {albumin:.1f} g/dL | {score_breakdown['Albumin']} |")
            st.markdown(f"| **INR** | {inr:.1f} | {score_breakdown['INR']} |")
            st.markdown(f"| **Ascites** | {ascites.split('-')[0].strip()} | {score_breakdown['Ascites']} |")
            st.markdown(f"| **Encephalopathy** | {enceph.split('(')[1].split(')')[0]} | {score_breakdown['Encephalopathy']} |")
            st.markdown(f"| **TỔNG** | | **{total_score}** |")
        
        # Scoring table
        with st.expander("📈 Bảng Chấm Điểm Child-Pugh"):
            st.markdown("""
            | Parameter | 1 điểm | 2 điểm | 3 điểm |
            |-----------|--------|--------|--------|
            | **Bilirubin** | <2 mg/dL<br>(<34 µmol/L) | 2-3 mg/dL<br>(34-50 µmol/L) | >3 mg/dL<br>(>50 µmol/L) |
            | **Albumin** | >3.5 g/dL<br>(>35 g/L) | 2.8-3.5 g/dL<br>(28-35 g/L) | <2.8 g/dL<br>(<28 g/L) |
            | **INR** | <1.7 | 1.7-2.3 | >2.3 |
            | **Ascites** | Không | Nhẹ | Trung bình-Nặng |
            | **Encephalopathy** | Không | Grade 1-2 | Grade 3-4 |
            
            **Phân loại:**
            - **Class A:** 5-6 điểm (Bù trừ tốt)
            - **Class B:** 7-9 điểm (Suy chức năng đáng kể)
            - **Class C:** 10-15 điểm (Mất bù)
            """)
        
        # Comparison table
        with st.expander("📊 So Sánh Child-Pugh Classes"):
            st.markdown("""
            | Class | Điểm | Mức Độ | Sống sót 1 năm | Sống sót 2 năm | Tử vong PT |
            |-------|------|---------|----------------|----------------|------------|
            | **A** | 5-6 | Bù trừ tốt | 100% | 85% | 10% |
            | **B** | 7-9 | Suy chức năng | 81% | 57% | 30% |
            | **C** | 10-15 | Mất bù | 45% | 35% | 82% |
            """)
        
        # MELD comparison
        with st.expander("🔄 Child-Pugh vs MELD Score"):
            st.markdown("""
            **Hai thang điểm chính đánh giá xơ gan:**
            
            | Đặc điểm | Child-Pugh | MELD |
            |----------|------------|------|
            | **Tham số** | 5 (2 lâm sàng + 3 xét nghiệm) | 3 (chỉ xét nghiệm) |
            | **Tính khách quan** | Chủ quan hơn (ascites, enceph) | Khách quan (công thức) |
            | **Ưu tiên ghép gan** | Không dùng | ✅ Sử dụng |
            | **Tiên lượng ngắn hạn** | Tốt | Rất tốt (3 tháng) |
            | **Phân loại** | 3 class (A, B, C) | Liên tục (6-40) |
            | **Ứng dụng** | Phẫu thuật, điều trị | Ưu tiên ghép gan |
            
            **Khuyến Nghị:** Sử dụng CẢ HAI thang điểm để đánh giá toàn diện!
            """)
        
        # References
        # Export section
        st.markdown("---")
        from components.export import render_export_section
        
        # Prepare inputs for export
        inputs_dict = {
            "Bilirubin": f"{bili_mgdl:.1f} mg/dL",
            "Albumin": f"{albumin:.1f} g/dL",
            "INR": f"{inr:.2f}",
            "Ascites": ascites,
            "Encephalopathy": encephalopathy
        }
        
        # Prepare results for export
        results_dict = {
            "Child-Pugh Score": f"{total_score}/15",
            "Child-Pugh Class": cp_class,
            "Severity": severity,
            "1-Year Survival": survival_1yr,
            "2-Year Survival": survival_2yr,
            "Surgical Mortality": periop_mortality,
            "Score Breakdown": score_breakdown
        }
        
        render_export_section(
            title=f"Child-Pugh Class {cp_class} ({total_score} điểm)",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="Child-Pugh Score",
            filename="child_pugh_result"
        )
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            **Primary Reference:**
            - Pugh RN, Murray-Lyon IM, Dawson JL, Pietroni MC, Williams R. 
              *Transection of the oesophagus for bleeding oesophageal varices.* 
              Br J Surg. 1973 Aug;60(8):646-9. [PMID: 4541913]
            
            **Validation Studies:**
            - Infante-Rivard C, Esnaola S, Villeneuve JP. 
              *Clinical and statistical validity of conventional prognostic factors in predicting short-term survival among cirrhotics.* 
              Hepatology. 1987 Jul-Aug;7(4):660-4.
            
            - Christensen E, Schlichting P, Fauerholdt L, et al. 
              *Prognostic value of Child-Turcotte criteria in medically treated cirrhosis.* 
              Hepatology. 1984 May-Jun;4(3):430-5.
            
            **Guidelines:**
            - EASL Clinical Practice Guidelines on the management of ascites, spontaneous bacterial peritonitis, and hepatorenal syndrome in cirrhosis. 
              J Hepatol. 2010;53(3):397-417.
            
            - Garcia-Tsao G, et al. Management of varices and variceal hemorrhage in cirrhosis. 
              Hepatology. 2007;46(3):922-38.
            
            - Runyon BA; AASLD Practice Guidelines Committee. 
              *Management of adult patients with ascites due to cirrhosis: an update.* 
              Hepatology. 2009;49(6):2087-107.
            """)
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("❓ Child-Pugh Score là gì?"):
        st.markdown("""
        **Child-Pugh Score** (hay Child-Turcotte-Pugh) là thang điểm đánh giá 
        mức độ nặng của xơ gan và tiên lượng bệnh nhân xơ gan.
        
        **Lịch sử:**
        - 1964: Child & Turcotte đề xuất phiên bản gốc
        - 1973: Pugh et al. sửa đổi (thay prothrombin time bằng INR)
        
        **Ưu điểm:**
        - Đơn giản, dễ sử dụng
        - Validated rộng rãi
        - Dự đoán tiên lượng tốt
        - Hướng dẫn quyết định điều trị
        
        **Hạn chế:**
        - Chủ quan (ascites, encephalopathy)
        - Hiệu ứng trần (ceiling effect) ở Class C
        - Không tính yếu tố gây xơ gan
        - Không liên tục (chỉ 3 class)
        """)
    
    with st.expander("⚠️ Biến Chứng Xơ Gan Mất Bù"):
        st.markdown("""
        **Các biến chứng chính cần theo dõi và xử trí:**
        
        **1. Cổ chướng (Ascites):**
        - 50% xơ gan có cổ chướng trong 10 năm
        - Sống sót 2 năm: 50%
        - Điều trị: Hạn chế muối + lợi tiểu
        - Biến chứng: SBP, HRS
        
        **2. Giãn tĩnh mạch thực quản (Varices):**
        - 50% xơ gan có varices
        - Nguy cơ vỡ: 10-15%/năm
        - Tử vong khi vỡ: 20-30%
        - Phòng ngừa: Beta-blocker, nội soi thắt vòng
        
        **3. Bệnh não gan (Hepatic Encephalopathy):**
        - 30-45% xơ gan có HE
        - Nguyên nhân: Ammonia, BCAA giảm
        - Điều trị: Lactulose, Rifaximin
        - Yếu tố kích phát: Nhiễm trùng, táo bón, thuốc an thần
        
        **4. Viêm phúc mạc do vi khuẩn tự phát (SBP):**
        - 10-30% bệnh nhân cổ chướng
        - Tử vong: 20-40%
        - Chẩn đoán: Ascitic fluid PMN >250 cells/µL
        - Điều trị: Ceftriaxone/Cefotaxime + Albumin
        
        **5. Hội chứng gan thận (HRS):**
        - Biến chứng nặng nhất
        - Tử vong cao nếu không ghép gan
        - Type 1: Tiến triển nhanh (<2 tuần)
        - Type 2: Tiến triển chậm
        - Điều trị: Terlipressin + Albumin
        
        **6. Ung thư gan (HCC):**
        - Nguy cơ: 1-6%/năm
        - Sàng lọc: Siêu âm + AFP mỗi 6 tháng
        - Điều trị: Phẫu thuật, RFA, TACE, ghép gan
        """)
    
    with st.expander("🏥 Chỉ Định Ghép Gan"):
        st.markdown("""
        **Chỉ định ghép gan trong xơ gan:**
        
        **Chỉ định chung:**
        - Child-Pugh Class B (7-9 điểm) - Cân nhắc
        - Child-Pugh Class C (≥10 điểm) - Có chỉ định
        - MELD score ≥15 - Nên đánh giá
        - Biến chứng xơ gan không kiểm soát được
        
        **Chỉ định cụ thể:**
        1. **Cổ chướng khó trị** (refractory ascites)
        2. **SBP tái phát** (≥2 lần)
        3. **HRS** (Hepatorenal syndrome)
        4. **Bệnh não gan tái phát** không kiểm soát được
        5. **Xuất huyết tiêu hóa tái phát** do giãn tĩnh mạch
        6. **HCC** trong tiêu chí Milan
        7. **Chất lượng sống kém** do xơ gan
        
        **Tiêu chí Milan cho HCC:**
        - 1 u ≤5cm HOẶC
        - ≤3 u, mỗi u ≤3cm
        - Không xâm lấn mạch máu
        - Không di căn xa
        
        **Chống Chỉ Định:**
        - Ung thư ngoài gan (trừ da không phải melanoma)
        - Nhiễm trùng toàn thân đang hoạt động
        - Bệnh tim phổi nặng
        - Lạm dụng rượu/ma túy đang hoạt động
        - Không tuân thủ điều trị
        - Bệnh tâm thần nặng không kiểm soát
        
        **Ưu tiên ghép gan:** Dựa vào MELD score (càng cao càng ưu tiên)
        """)
    
    # Footer
    st.markdown("---")
    st.caption("📚 Based on: Pugh RN, et al. Br J Surg. 1973;60(8):646-9")
    st.caption("⚠️ Most widely used score for cirrhosis severity")
    st.caption("🏥 Essential for surgical risk assessment and transplant evaluation")

