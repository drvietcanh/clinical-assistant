"""
Modified Bishop Score
Phiên bản cải tiến của Bishop Score với thêm yếu tố lâm sàng
"""

import streamlit as st


def calculate_modified_bishop(dilation, effacement, station, consistency, position,
                               has_preeclampsia=False, has_prom=False):
    """
    Calculate Modified Bishop Score
    
    Args:
        dilation: Cervical dilation (cm)
        effacement: Cervical effacement (%)
        station: Fetal station
        consistency: Cervical consistency
        position: Cervical position
        has_preeclampsia: Presence of preeclampsia (+1 point)
        has_prom: Premature rupture of membranes (+1 point)
    
    Returns:
        dict: Score breakdown
    """
    # Original Bishop components (same scoring)
    if dilation == 0:
        dilation_score = 0
    elif dilation <= 2:
        dilation_score = 1
    elif dilation <= 4:
        dilation_score = 2
    else:
        dilation_score = 3
    
    if effacement <= 30:
        effacement_score = 0
    elif effacement <= 50:
        effacement_score = 1
    elif effacement <= 80:
        effacement_score = 2
    else:
        effacement_score = 3
    
    if station <= -3:
        station_score = 0
    elif station == -2:
        station_score = 1
    elif station in [-1, 0]:
        station_score = 2
    else:
        station_score = 3
    
    consistency_scores = {"firm": 0, "medium": 1, "soft": 2}
    consistency_score = consistency_scores.get(consistency, 0)
    
    position_scores = {"posterior": 0, "mid": 1, "anterior": 2}
    position_score = position_scores.get(position, 0)
    
    # Modified Bishop additions
    preeclampsia_score = 1 if has_preeclampsia else 0
    prom_score = 1 if has_prom else 0
    
    base_score = (dilation_score + effacement_score + station_score + 
                  consistency_score + position_score)
    
    modifier_score = preeclampsia_score + prom_score
    
    total = base_score + modifier_score
    
    return {
        "total": total,
        "base_score": base_score,
        "dilation_score": dilation_score,
        "effacement_score": effacement_score,
        "station_score": station_score,
        "consistency_score": consistency_score,
        "position_score": position_score,
        "preeclampsia_score": preeclampsia_score,
        "prom_score": prom_score,
        "modifier_score": modifier_score
    }


def interpret_modified_bishop(total_score, is_nulliparous=True):
    """Interpret Modified Bishop Score (cutoffs adjusted for 0-15 scale)"""
    
    if total_score <= 5:
        return {
            "favorability": "KHÔNG THUẬN LỢI",
            "color": "🔴",
            "recommendation": "Cần cervical ripening",
            "success_rate": "30-50% (nullip), 60-70% (multip)",
            "severity": "unfavorable"
        }
    elif total_score <= 8:
        return {
            "favorability": "TRUNG BÌNH",
            "color": "🟡",
            "recommendation": "Xem xét ripening (đặc biệt nulliparous)",
            "success_rate": "60-75% (nullip), 80-90% (multip)",
            "severity": "intermediate"
        }
    else:  # > 8
        return {
            "favorability": "THUẬN LỢI",
            "color": "🟢",
            "recommendation": "Induction khả năng thành công cao",
            "success_rate": "80-95% (nullip), 95-98% (multip)",
            "severity": "favorable"
        }


def render():
    """Render the Modified Bishop Score calculator"""
    
    st.title("🤰 Modified Bishop Score")
    st.markdown("""
    ### Phiên Bản Cải Tiến Bishop Score
    
    **Modified Bishop Score:**
    - Bổ sung thêm yếu tố lâm sàng vào Bishop Score gốc
    - Điểm từ 0-15 (thay vì 0-13)
    - Cải thiện độ chính xác dự đoán
    
    **Bổ sung thêm 2 yếu tố (mỗi +1 điểm):**
    - **Preeclampsia:** Tiền sản giật
    - **PROM:** Vỡ ối non (Premature Rupture of Membranes)
    
    **Lý do bổ sung:**
    - Preeclampsia → Cần chấm dứt thai kỳ sớm → Tăng tính cấp thiết induction
    - PROM → Đã vỡ ối → Tăng khả năng thành công induction
    
    **Phân loại (điều chỉnh cho thang 0-15):**
    - **≤ 5:** Không thuận lợi
    - **6-8:** Trung bình
    - **> 8:** Thuận lợi
    
    **So với Bishop Score gốc:**
    - Giống hệt 5 thành phần chính
    - Thêm 2 modifiers lâm sàng
    - Dự đoán chính xác hơn trong một số trường hợp
    """)
    
    st.markdown("---")
    
    # Patient information
    col1, col2 = st.columns(2)
    
    with col1:
        parity = st.radio(
            "**Parity:**",
            options=["nulliparous", "multiparous"],
            format_func=lambda x: "Nulliparous (Con so)" if x == "nulliparous" else "Multiparous (Đã sinh)",
            horizontal=False
        )
        is_nulliparous = (parity == "nulliparous")
    
    with col2:
        st.markdown("**Yếu tố bổ sung:**")
        has_preeclampsia = st.checkbox("Có Preeclampsia (+1 điểm)")
        has_prom = st.checkbox("Có PROM - Vỡ ối non (+1 điểm)")
    
    if has_preeclampsia or has_prom:
        modifiers = []
        if has_preeclampsia:
            modifiers.append("Preeclampsia")
        if has_prom:
            modifiers.append("PROM")
        st.info(f"🔹 Yếu tố bổ sung: {', '.join(modifiers)} → +{int(has_preeclampsia) + int(has_prom)} điểm")
    
    st.markdown("---")
    
    # Original Bishop components
    st.subheader("📋 5 Thành phần Bishop Score Gốc")
    
    # 1. Dilation
    st.markdown("### 1️⃣ Dilation - Mở Cổ Tử Cung")
    dilation = st.select_slider(
        "Mở cổ (cm):",
        options=[0, 1, 2, 3, 4, 5, 6],
        value=0
    )
    
    st.markdown("---")
    
    # 2. Effacement
    st.markdown("### 2️⃣ Effacement - Xóa Mỏng")
    effacement = st.slider(
        "Xóa mỏng (%):",
        min_value=0,
        max_value=100,
        value=0,
        step=10
    )
    
    st.markdown("---")
    
    # 3. Station
    st.markdown("### 3️⃣ Station - Lọt")
    station = st.select_slider(
        "Fetal station:",
        options=[-3, -2, -1, 0, +1, +2],
        value=-3,
        format_func=lambda x: f"{x:+d}"
    )
    
    st.markdown("---")
    
    # 4. Consistency
    st.markdown("### 4️⃣ Consistency - Độ Mềm")
    consistency = st.radio(
        "Độ mềm:",
        options=["firm", "medium", "soft"],
        format_func=lambda x: {"firm": "Firm (Cứng)", "medium": "Medium", "soft": "Soft (Mềm)"}[x],
        horizontal=True
    )
    
    st.markdown("---")
    
    # 5. Position
    st.markdown("### 5️⃣ Position - Vị Trí")
    position = st.radio(
        "Vị trí:",
        options=["posterior", "mid", "anterior"],
        format_func=lambda x: {"posterior": "Posterior (Sau)", "mid": "Mid", "anterior": "Anterior (Trước)"}[x],
        horizontal=True
    )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("📊 Tính Modified Bishop Score", type="primary", use_container_width=True):
        scores = calculate_modified_bishop(
            dilation, effacement, station, consistency, position,
            has_preeclampsia, has_prom
        )
        
        total_score = scores['total']
        base_score = scores['base_score']
        modifier_score = scores['modifier_score']
        
        result = interpret_modified_bishop(total_score, is_nulliparous)
        
        st.markdown("---")
        st.subheader("📈 Kết quả Đánh giá")
        
        # Display scores
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Bishop Score Gốc",
                f"{base_score}/13",
                help="5 thành phần chính"
            )
        
        with col2:
            st.metric(
                "Modifier Score",
                f"+{modifier_score}",
                help="Preeclampsia + PROM"
            )
        
        with col3:
            st.metric(
                "Modified Bishop",
                f"{total_score}/15",
                help="Tổng điểm"
            )
        
        st.markdown("---")
        
        # Favorability
        if result['severity'] == "favorable":
            st.success(f"{result['color']} {result['favorability']}")
        elif result['severity'] == "intermediate":
            st.warning(f"{result['color']} {result['favorability']}")
        else:
            st.error(f"{result['color']} {result['favorability']}")
        
        st.markdown("---")
        
        # Score breakdown
        st.subheader("📊 Phân tích chi tiết")
        
        st.markdown("**5 thành phần chính:**")
        components = [
            ("Dilation", scores['dilation_score'], f"{dilation} cm"),
            ("Effacement", scores['effacement_score'], f"{effacement}%"),
            ("Station", scores['station_score'], f"{station:+d}"),
            ("Consistency", scores['consistency_score'], consistency.capitalize()),
            ("Position", scores['position_score'], position.capitalize())
        ]
        
        for component, score, value in components:
            col1, col2, col3 = st.columns([3, 1, 2])
            with col1:
                st.write(f"• {component}")
            with col2:
                st.write(f"**{score}**")
            with col3:
                st.write(f"*{value}*")
        
        st.markdown("**Yếu tố bổ sung:**")
        if has_preeclampsia:
            st.write(f"• Preeclampsia: **+{scores['preeclampsia_score']}**")
        if has_prom:
            st.write(f"• PROM: **+{scores['prom_score']}**")
        if not has_preeclampsia and not has_prom:
            st.write("• Không có yếu tố bổ sung")
        
        st.markdown("---")
        
        # Interpretation
        st.subheader("🎯 Khuyến nghị")
        
        parity_text = "nulliparous" if is_nulliparous else "multiparous"
        
        st.info(f"""
        **Modified Bishop Score: {total_score}/15** ({parity_text})
        
        **Đánh giá:** {result['favorability']}
        
        **Tỷ lệ thành công:** {result['success_rate']}
        
        **Khuyến nghị:** {result['recommendation']}
        """)
        
        # Special considerations
        if has_preeclampsia or has_prom:
            st.markdown("### 🔔 Lưu ý đặc biệt")
            
            if has_preeclampsia:
                st.warning("""
                **Với Preeclampsia:**
                - Chỉ định induction/delivery để bảo vệ mẹ
                - Timing phụ thuộc mức độ nặng và tuổi thai
                - Severe preeclampsia ≥ 34 tuần → Delivery
                - Mild preeclampsia ≥ 37 tuần → Xem xét induction
                - Cervix không thuận lợi → Ripening vẫn cần thiết
                - Monitor chặt chẽ hơn trong labor
                - Magnesium sulfate prophylaxis (nếu severe)
                """)
            
            if has_prom:
                st.warning("""
                **Với PROM (Premature Rupture of Membranes):**
                - **Term PROM (≥ 37 tuần):**
                  + Expectant management 12-24h hoặc immediate induction
                  + 50% chuyển dạ tự nhiên trong 12h
                  + 95% trong 24h
                  + GBS prophylaxis nếu chưa screen hoặc (+)
                  + Induction giảm risk chorioamnionitis
                
                - **Preterm PROM (< 37 tuần):**
                  + Expectant management (nếu không có infection)
                  + Antibiotics
                  + Corticosteroids (nếu < 34 tuần)
                  + Delivery nếu có infection/fetal distress
                
                - **Nguy cơ:**
                  + Infection (chorioamnionitis, endometritis)
                  + Cord prolapse (nếu presenting part cao)
                  + Placental abruption
                """)
        
        # Induction recommendations
        if result['severity'] == "favorable":
            st.success("""
            ### ✅ Induction Protocol (Favorable Cervix)
            
            **Oxytocin hoặc Amniotomy:**
            - Không cần ripening
            - Bắt đầu Oxytocin low dose
            - Hoặc amniotomy nếu nước ối trong
            - Monitor liên tục
            """)
        else:
            st.info("""
            ### 🔧 Cervical Ripening Recommended
            
            **Lựa chọn:**
            - **Prostaglandins (PGE):** Dinoprostone hoặc Misoprostol
            - **Mechanical:** Foley catheter
            - **Combination:** Có thể kết hợp
            
            **Đánh giá lại sau 12-24h**
            """)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông tin bổ sung")
    
    with st.expander("🆚 Modified Bishop vs Bishop Score Gốc"):
        st.markdown("""
        ### So sánh 2 phiên bản:
        
        | Đặc điểm | Bishop Gốc | Modified Bishop |
        |----------|------------|-----------------|
        | **Thang điểm** | 0-13 | 0-15 |
        | **Thành phần chính** | 5 | 5 (giống) |
        | **Yếu tố bổ sung** | Không | Preeclampsia + PROM |
        | **Độ phức tạp** | Đơn giản hơn | Phức tạp hơn chút |
        | **Độ chính xác** | Tốt | Tốt hơn (một số TH) |
        | **Phổ biến** | Rất phổ biến | Ít phổ biến hơn |
        
        **Khi nào dùng Modified Bishop:**
        - Có preeclampsia
        - Có PROM
        - Muốn đánh giá chính xác hơn
        
        **Khi nào dùng Bishop gốc:**
        - Không có preeclampsia/PROM
        - Đơn giản, nhanh
        - Đủ cho hầu hết trường hợp
        
        **Lưu ý:**
        - Cả 2 đều là công cụ tốt
        - Không có rule nào là perfect
        - Clinical judgment vẫn quan trọng nhất
        - Nhiều trung tâm chỉ dùng Bishop gốc
        """)
    
    with st.expander("🤰 Preeclampsia và Induction"):
        st.markdown("""
        ### Induction trong Preeclampsia:
        
        **Chỉ định Delivery:**
        
        **Severe Preeclampsia:**
        - ≥ 34 tuần: Delivery trong 24-48h
        - < 34 tuần: Expectant management (nếu stable) hoặc delivery
        - Corticosteroids nếu < 34 tuần
        
        **Mild Preeclampsia:**
        - ≥ 37 tuần: Xem xét induction
        - < 37 tuần: Expectant management với monitoring chặt
        
        **Criteria for severe:**
        - BP ≥ 160/110 persistent
        - Pulmonary edema
        - Thrombocytopenia (< 100,000)
        - Liver enzymes tăng gấp đôi
        - Creatinine > 1.1 hoặc tăng gấp đôi
        - Đau đầu nặng persistent
        - Visual disturbances
        - Đau thượng vị
        
        **Xử trí labor:**
        - IV access
        - MgSO4 (nếu severe)
        - BP control (nếu ≥ 160/110)
        - Monitor BP liên tục
        - Labs q6-12h
        - I/O strict
        - Continuous fetal monitoring
        - Epidural anesthesia OK (giúp giảm BP)
        
        **Postpartum:**
        - MgSO4 tiếp 24h sau delivery
        - Monitor BP, urine output
        - Risk eclampsia cao nhất 48h đầu pp
        """)
    
    with st.expander("💧 PROM Management"):
        st.markdown("""
        ### Quản lý Vỡ Ối Non:
        
        **Chẩn đoán PROM:**
        - Pooling: Nước ối trong âm đạo
        - Nitrazine test: pH > 6.5 (xanh)
        - Ferning test: Hình lá dương xỉ
        - Ultrasound: Oligohydramnios
        
        **Term PROM (≥ 37 tuần):**
        
        **2 chiến lược:**
        
        **1. Immediate Induction:**
        - Ưu điểm: Giảm infection
        - Nhược điểm: Tăng can thiệp y tế
        - Phù hợp: GBS (+), > 12-18h PROM
        
        **2. Expectant Management:**
        - Chờ 12-24h
        - 50% chuyển dạ trong 12h
        - 95% trong 24h
        - Monitor nhiễm trùng
        - Nếu không chuyển dạ → Induction
        
        **ACOG khuyến cáo:**
        - Cả 2 approach đều OK
        - Trao đổi với sản phụ
        - Nếu expectant: Không VE lặp lại
        - GBS prophylaxis
        
        **Preterm PROM (< 37 tuần):**
        - **34-36 tuần:** Delivery
        - **24-33 tuần:** Expectant + Antibiotics + Steroids
        - **< 24 tuần:** Tư vấn, consider termination
        
        **Antibiotics (Preterm PROM):**
        - Ampicillin 2g IV q6h × 48h
        - Sau đó Amoxicillin 250mg PO q8h × 5 ngày
        - Kết hợp Azithromycin 1g PO × 1
        - Kéo dài latency period
        - Giảm chorioamnionitis, neonatal sepsis
        
        **Dấu hiệu Chorioamnionitis:**
        - Sốt ≥ 38°C
        - Tachycardia mẹ
        - Fetal tachycardia
        - Tử cung đau
        - Leucocytosis
        - Dịch âm đạo hôi
        → Antibiotics + Delivery ngay
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Bishop EH. Pelvic scoring for elective induction. Obstet Gynecol. 1964
    - ACOG Practice Bulletin No. 107: Induction of labor. 2009
    - ACOG Practice Bulletin No. 202: Gestational Hypertension and Preeclampsia. 2019
    - ACOG Practice Bulletin No. 188: Prelabor Rupture of Membranes. 2018
    """)


if __name__ == "__main__":
    render()

