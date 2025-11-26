"""
Bishop Score
Đánh giá độ chín cổ tử cung và khả năng gây chuyển dạ thành công
"""

import streamlit as st


def calculate_bishop_score(dilation, effacement, station, consistency, position):
    """
    Calculate Bishop Score
    
    Args:
        dilation: Cervical dilation (cm)
        effacement: Cervical effacement (%)
        station: Fetal station
        consistency: Cervical consistency
        position: Cervical position
    
    Returns:
        int: Total Bishop score (0-13)
    """
    # Dilation score
    if dilation == 0:
        dilation_score = 0
    elif dilation <= 2:
        dilation_score = 1
    elif dilation <= 4:
        dilation_score = 2
    else:  # > 4 cm
        dilation_score = 3
    
    # Effacement score
    if effacement <= 30:
        effacement_score = 0
    elif effacement <= 50:
        effacement_score = 1
    elif effacement <= 80:
        effacement_score = 2
    else:  # > 80%
        effacement_score = 3
    
    # Station score (-3 to +2)
    if station <= -3:
        station_score = 0
    elif station == -2:
        station_score = 1
    elif station in [-1, 0]:
        station_score = 2
    else:  # +1, +2
        station_score = 3
    
    # Consistency score
    consistency_scores = {
        "firm": 0,
        "medium": 1,
        "soft": 2
    }
    consistency_score = consistency_scores.get(consistency, 0)
    
    # Position score
    position_scores = {
        "posterior": 0,
        "mid": 1,
        "anterior": 2
    }
    position_score = position_scores.get(position, 0)
    
    total = (dilation_score + effacement_score + station_score + 
             consistency_score + position_score)
    
    return {
        "total": total,
        "dilation_score": dilation_score,
        "effacement_score": effacement_score,
        "station_score": station_score,
        "consistency_score": consistency_score,
        "position_score": position_score
    }


def interpret_bishop_score(total_score, is_nulliparous=True):
    """
    Interpret Bishop Score
    
    Args:
        total_score: Total Bishop score
        is_nulliparous: True if nulliparous (first pregnancy), False if multiparous
    
    Returns:
        dict: Interpretation results
    """
    if total_score <= 5:
        return {
            "favorability": "KHÔNG THUẬN LỢI (Unfavorable)",
            "color": "🔴",
            "induction_success": "Thấp (30-50% nếu nulliparous)",
            "recommendation": "Cân nhắc cervical ripening trước induction",
            "labor_duration": "Có thể kéo dài hoặc thất bại",
            "csection_risk": "Cao (15-25% nếu nulliparous)",
            "ripening": "Nên dùng ripening agents (Prostaglandin, Foley catheter)",
            "severity": "unfavorable"
        }
    elif total_score <= 8:
        return {
            "favorability": "TRUNG BÌNH (Intermediate)",
            "color": "🟡",
            "induction_success": "Trung bình (60-75%)",
            "recommendation": "Có thể induction, cân nhắc ripening",
            "labor_duration": "Bình thường đến hơi kéo dài",
            "csection_risk": "Trung bình (10-15%)",
            "ripening": "Xem xét ripening nếu nulliparous",
            "severity": "intermediate"
        }
    else:  # > 8
        return {
            "favorability": "THUẬN LỢI (Favorable)",
            "color": "🟢",
            "induction_success": "Cao (80-95%)",
            "recommendation": "Induction có khả năng thành công cao",
            "labor_duration": "Bình thường, có thể ngắn",
            "csection_risk": "Thấp (5-10%)",
            "ripening": "Thường không cần ripening",
            "severity": "favorable"
        }


def render():
    """Render the Bishop Score calculator"""
    
    st.title("🤰 Bishop Score")
    st.markdown("""
    ### Đánh Giá Độ Chín Cổ Tử Cung
    
    **Bishop Score:**
    - Đánh giá độ thuận lợi của cổ tử cung cho induction of labor
    - 5 thành phần, điểm từ 0-13
    - Dự đoán khả năng thành công của gây chuyển dạ
    - Công cụ quan trọng nhất trong sản khoa
    
    **5 Thành Phần (Mnemonic: PEEDS):**
    1. **P**osition (Vị trí cổ tử cung)
    2. **E**ffacement (Xóa mỏng cổ tử cung)
    3. **E**ngagement (Lọt)
    4. **D**ilation (Mở cổ tử cung)
    5. **S**oftness (Độ mềm cổ tử cung)
    
    **Phân Loại:**
    - **≤ 5:** Không thuận lợi → Cần ripening
    - **6-8:** Trung bình → Xem xét ripening
    - **> 8:** Thuận lợi → Induction thành công cao
    
    **Ứng dụng:**
    - Quyết định gây chuyển dạ (induction of labor)
    - Lựa chọn phương pháp induction
    - Dự đoán nguy cơ mổ lấy thai
    - Tư vấn cho sản phụ
    """)
    
    st.markdown("---")
    
    # Patient information
    with st.expander("ℹ️ Thông Tin Sản Phụ", expanded=False):
        parity = st.radio(
            "Parity (Thai sản):",
            options=["nulliparous", "multiparous"],
            format_func=lambda x: "Nulliparous (Con so)" if x == "nulliparous" else "Multiparous (Đã sinh)",
            horizontal=True
        )
        is_nulliparous = (parity == "nulliparous")
        
        st.info(f"""
        **Lưu ý:**
        - **Nulliparous:** Tỷ lệ thành công thấp hơn với cùng Bishop score
        - **Multiparous:** Thường thành công hơn, ít cần ripening hơn
        - Bishop ≤ 5 ở nulliparous: Nguy cơ mổ cao (20-25%)
        """)
    
    st.markdown("---")
    
    # Bishop Score Components
    st.subheader("📋 5 Thành Phần Bishop Score")
    
    # 1. Dilation
    st.markdown("### 1️⃣ Dilation - Mở Cổ Tử Cung")
    dilation = st.select_slider(
        "Mở cổ tử cung (cm):",
        options=[0, 1, 2, 3, 4, 5, 6],
        value=0,
        help="Đường kính internal os"
    )
    
    if dilation == 0:
        st.caption("📏 0 điểm: Đóng kín")
    elif dilation <= 2:
        st.caption("📏 1 điểm: 1-2 cm")
    elif dilation <= 4:
        st.caption("📏 2 điểm: 3-4 cm")
    else:
        st.caption("📏 3 điểm: ≥ 5 cm")
    
    st.markdown("---")
    
    # 2. Effacement
    st.markdown("### 2️⃣ Effacement - Xóa Mỏng Cổ Tử Cung")
    effacement = st.slider(
        "Xóa mỏng (%):",
        min_value=0,
        max_value=100,
        value=0,
        step=10,
        help="Phần trăm xóa mỏng cổ tử cung"
    )
    
    if effacement <= 30:
        st.caption("📏 0 điểm: 0-30%")
    elif effacement <= 50:
        st.caption("📏 1 điểm: 40-50%")
    elif effacement <= 80:
        st.caption("📏 2 điểm: 60-80%")
    else:
        st.caption("📏 3 điểm: ≥ 80%")
    
    st.markdown("---")
    
    # 3. Station
    st.markdown("### 3️⃣ Station - Vị Trí Thai Nhi (Lọt)")
    st.caption("Station của presenting part so với ischial spines")
    
    station = st.select_slider(
        "Fetal station:",
        options=[-3, -2, -1, 0, +1, +2],
        value=-3,
        format_func=lambda x: f"{x:+d}",
        help="-3 to +2 (0 = ischial spines)"
    )
    
    if station <= -3:
        st.caption("📏 0 điểm: -3 (chưa lọt)")
    elif station == -2:
        st.caption("📏 1 điểm: -2 (đang lọt)")
    elif station in [-1, 0]:
        st.caption("📏 2 điểm: -1, 0 (lọt)")
    else:
        st.caption("📏 3 điểm: +1, +2 (lọt sâu)")
    
    st.markdown("---")
    
    # 4. Consistency
    st.markdown("### 4️⃣ Consistency - Độ Mềm Cổ Tử Cung")
    consistency = st.radio(
        "Độ mềm khi thăm khám:",
        options=["firm", "medium", "soft"],
        format_func=lambda x: {
            "firm": "Firm (Cứng) - 0 điểm",
            "medium": "Medium (Trung bình) - 1 điểm",
            "soft": "Soft (Mềm) - 2 điểm"
        }[x],
        help="Cảm giác khi palpation"
    )
    
    st.markdown("---")
    
    # 5. Position
    st.markdown("### 5️⃣ Position - Vị Trí Cổ Tử Cung")
    position = st.radio(
        "Vị trí cổ tử cung:",
        options=["posterior", "mid", "anterior"],
        format_func=lambda x: {
            "posterior": "Posterior (Sau) - 0 điểm",
            "mid": "Mid (Giữa) - 1 điểm",
            "anterior": "Anterior (Trước) - 2 điểm"
        }[x],
        help="Hướng của cervical os"
    )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("📊 Tính Bishop Score", type="primary", use_container_width=True):
        # Calculate scores
        scores = calculate_bishop_score(dilation, effacement, station, consistency, position)
        total_score = scores['total']
        
        # Get interpretation
        result = interpret_bishop_score(total_score, is_nulliparous)
        
        st.markdown("---")
        st.subheader("📈 Kết quả Đánh Giá")
        
        # Display total score
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Bishop Score",
                f"{total_score}/13",
                help="Tổng điểm Bishop"
            )
        
        with col2:
            if result['severity'] == "favorable":
                st.success(f"{result['color']} {result['favorability']}")
            elif result['severity'] == "intermediate":
                st.warning(f"{result['color']} {result['favorability']}")
            else:
                st.error(f"{result['color']} {result['favorability']}")
        
        st.markdown("---")
        
        # Score breakdown
        st.subheader("📊 Phân Tích Từng Thành Phần")
        
        components = [
            ("Dilation (Mở cổ tử cung)", scores['dilation_score'], f"{dilation} cm"),
            ("Effacement (Xóa mỏng)", scores['effacement_score'], f"{effacement}%"),
            ("Station (Lọt)", scores['station_score'], f"{station:+d}"),
            ("Consistency (Độ mềm)", scores['consistency_score'], consistency.capitalize()),
            ("Position (Vị trí)", scores['position_score'], position.capitalize())
        ]
        
        for component, score, value in components:
            col1, col2, col3 = st.columns([3, 1, 2])
            with col1:
                st.write(f"**{component}**")
            with col2:
                if score == 0:
                    st.write("🔴 0")
                elif score == 1:
                    st.write("🟡 1")
                elif score == 2:
                    st.write("🟠 2")
                else:
                    st.write("🟢 3")
            with col3:
                st.write(f"*{value}*")
        
        st.markdown("---")
        
        # Interpretation
        st.subheader("🎯 Phân Tích & Khuyến Nghị")
        
        parity_text = "nulliparous (con so)" if is_nulliparous else "multiparous (đã sinh)"
        
        if result['severity'] == "favorable":
            st.success(f"""
            ### {result['color']} {result['favorability']}
            
            **Bishop Score: {total_score}/13** ({'Sản phụ ' + parity_text})
            
            **Đánh Giá:** Cổ tử cung thuận lợi cho gây chuyển dạ
            
            **Tỷ lệ thành công:** {result['induction_success']}
            
            **Nguy cơ mổ lấy thai:** {result['csection_risk']}
            
            **Thời gian chuyển dạ:** {result['labor_duration']}
            
            **Khuyến Nghị:** {result['recommendation']}
            
            **Ripening:** {result['ripening']}
            """)
            
            st.info("""
            ### ✅ Phương Pháp Induction Khuyến Cáo:
            
            **Với Bishop > 8:**
            
            **1. Oxytocin:**
            - Lựa chọn đầu tay
            - Bắt đầu liều thấp, tăng dần
            - Monitor liên tục
            
            **2. Hoặc Amniotomy (nước ối trong):**
            - Có thể dùng đơn độc
            - Thường kết hợp với Oxytocin
            
            **3. Theo dõi:**
            - CTG liên tục
            - Đánh giá tiến triển chuyển dạ
            - Active management of labor
            """)
            
        else:
            st.warning(f"""
            ### {result['color']} {result['favorability']}
            
            **Bishop Score: {total_score}/13** ({'Sản phụ ' + parity_text})
            
            **Đánh Giá:** Cổ tử cung {'chưa' if result['severity'] == 'unfavorable' else 'tương đối'} thuận lợi
            
            **Tỷ lệ thành công:** {result['induction_success']}
            
            **Nguy cơ mổ lấy thai:** {result['csection_risk']}
            
            **Thời gian chuyển dạ:** {result['labor_duration']}
            
            **Khuyến Nghị:** {result['recommendation']}
            
            **Ripening:** {result['ripening']}
            """)
            
            if result['severity'] == "unfavorable":
                st.error(f"""
                ### ⚠️ Bishop ≤ 5 - KHÔNG THUẬN LỢI
                
                **Với {'nulliparous' if is_nulliparous else 'multiparous'}:**
                - Nguy cơ thất bại induction cao
                - {'Nguy cơ mổ lấy thai RẤT CAO (20-25%)' if is_nulliparous else 'Nguy cơ mổ lấy thai cao (10-15%)'}
                - Nên cervical ripening trước
                """)
            
            st.info("""
            ### 🔧 Cervical Ripening Methods:
            
            **Pharmacological:**
            
            **1. Prostaglandins:**
            - **Dinoprostone (PGE2):**
              + Gel/Insert intravaginal
              + Prepidil, Cervidil
            - **Misoprostol (PGE1):**
              + 25 mcg PV q3-6h
              + Hoặc 25-50 mcg PO
              + Rẻ hơn, hiệu quả tương đương
            
            **2. Mifepristone (nếu available):**
            - 200 mg PO
            - Off-label use
            
            **Mechanical:**
            
            **3. Foley Catheter:**
            - Balloon 30-80 mL
            - Để 12-24h
            - An toàn, rẻ
            - Có thể kết hợp Prostaglandin
            
            **4. Hygroscopic dilators:**
            - Laminaria, Dilapan
            - Ít dùng hiện nay
            
            **Lựa chọn:**
            - **Bishop ≤ 5:** Ripening BẮT BUỘC (đặc biệt nulliparous)
            - **Bishop 6-8:** Xem xét ripening (nulliparous)
            - **Bishop > 8:** Thường không cần
            
            **Đánh giá lại:**
            - Sau 12-24h ripening
            - Tính lại Bishop score
            - Quyết định induction hoặc ripening tiếp
            """)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông Tin Bổ Sung")
    
    with st.expander("📊 Chi tiết từng thành phần"):
        st.markdown("""
        ### Bishop Score Components:
        
        | Component | 0 | 1 | 2 | 3 |
        |-----------|---|---|---|---|
        | **Dilation** | Closed | 1-2 cm | 3-4 cm | ≥5 cm |
        | **Effacement** | 0-30% | 40-50% | 60-80% | ≥80% |
        | **Station** | -3 | -2 | -1, 0 | +1, +2 |
        | **Consistency** | Firm | Medium | Soft | - |
        | **Position** | Posterior | Mid | Anterior | - |
        
        ### Giải thích:
        
        **Dilation (Mở cổ tử cung):**
        - Đường kính internal os
        - Đo bằng cm (0-10 cm)
        - 10 cm = Fully dilated
        
        **Effacement (Xóa mỏng):**
        - Độ mỏng của cervix
        - 0% = Thick (2-3 cm)
        - 100% = Paper-thin
        - Thường xảy ra TRƯỚC dilation ở nulliparous
        - Có thể xảy ra CÙNG LÚC dilation ở multiparous
        
        **Station (Lọt):**
        - Vị trí presenting part (thường là đầu thai)
        - So với ischial spines (điểm mốc)
        - **0 = At spines** (engaged)
        - Âm (-) = Trên spines (chưa lọt)
        - Dương (+) = Dưới spines (lọt sâu)
        - +2 = Gần crowning
        
        **Consistency (Độ mềm):**
        - Cảm giác khi palpation
        - **Firm:** Cứng như mũi
        - **Medium:** Như môi
        - **Soft:** Như má trong miệng
        
        **Position (Vị trí):**
        - Hướng của cervical os
        - **Posterior:** Hướng về sau (khó khám)
        - **Mid:** Giữa
        - **Anterior:** Hướng về trước (dễ khám)
        - Khi labor tiến triển → Từ posterior → anterior
        """)
    
    with st.expander("🎯 Chỉ Định Gây Chuyển Dạ"):
        st.markdown("""
        ### Indications for Induction of Labor:
        
        **Chỉ định thai/bào:**
        - Thai quá ngày (≥ 41-42 tuần)
        - Vỡ ối non không chuyển dạ (PROM)
        - Nhiễm khuẩn ối
        - Chậm phát triển thai nội tử cung (IUGR)
        - Biến chứng đa thai
        - Thai chết lưu
        - Bất thường NST/biophysical profile
        
        **Chỉ định mẹ:**
        - Tiền sản giật/sản giật
        - Đái tháo đường thai kỳ không kiểm soát
        - Bệnh lý nội khoa nặng
        - Chorioamnionitis
        
        **Chỉ định khác:**
        - Elective (39-40 tuần, cervix favorable)
        - Logistic reasons (xa bệnh viện, tiền sử chuyển dạ nhanh)
        
        **Chống Chỉ Định:**
        - Chống chỉ định ngôi thường (placenta previa, etc.)
        - Cổ tử cung sẹo > 1
        - Herpes sinh dục active
        - Vị trí bất thường (ngang, chếch, etc.)
        - Suy thai cấp
        """)
    
    with st.expander("📈 Tỷ Lệ Thành Công Theo Bishop"):
        st.markdown("""
        ### Success Rates:
        
        **Nulliparous:**
        
        | Bishop | Vaginal Delivery | C-section |
        |--------|------------------|-----------|
        | 0-2 | 30-40% | 25-30% |
        | 3-5 | 40-60% | 15-25% |
        | 6-8 | 70-80% | 10-15% |
        | ≥9 | 85-95% | 5-10% |
        
        **Multiparous:**
        
        | Bishop | Vaginal Delivery | C-section |
        |--------|------------------|-----------|
        | 0-2 | 60-70% | 10-15% |
        | 3-5 | 75-85% | 8-12% |
        | 6-8 | 85-95% | 5-8% |
        | ≥9 | 95-98% | 2-5% |
        
        **Yếu tố ảnh hưởng:**
        - Parity (quan trọng nhất)
        - Tuổi mẹ (> 35: Thất bại cao hơn)
        - BMI (Béo phì: Thất bại cao hơn)
        - Cân nặng thai (Macrosomia: Khó hơn)
        - Phương pháp induction
        - Nguyên nhân induction
        """)
    
    with st.expander("🔄 Modified Bishop Score"):
        st.markdown("""
        ### Các biến thể của Bishop Score:
        
        **Modified Bishop Score:**
        - Thêm yếu tố: **+1 điểm nếu preeclampsia**
        - Thêm yếu tố: **+1 điểm nếu PROM**
        - → Tổng có thể lên 15 điểm
        
        **Simplified Bishop:**
        - Chỉ dùng 3 yếu tố: Dilation, Effacement, Station
        - Đơn giản hơn nhưng kém chính xác
        
        **Bishop Score trong nghiên cứu:**
        - Nghiên cứu gốc (Bishop 1964): > 8 = Favorable
        - ACOG: Cutoff ≥ 6-8
        - Một số guidelines: ≥ 5 (multiparous), ≥ 6 (nulliparous)
        
        **Hạn chế:**
        - Chủ quan (inter-observer variation)
        - Không dự đoán hoàn hảo
        - Không bao gồm yếu tố thai (cân nặng, vị trí)
        - Không phân biệt parity rõ ràng
        
        **Công cụ bổ sung:**
        - Transvaginal ultrasound cervical length
        - Fetal fibronectin
        - Oxytocin challenge test
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Bishop EH. Pelvic scoring for elective induction. Obstet Gynecol. 1964;24:266-268
    - ACOG Practice Bulletin No. 107: Induction of labor. Obstet Gynecol. 2009;114(2 Pt 1):386-397
    - Laughon SK, et al. Neonatal and maternal outcomes with prolonged second stage of labor. Obstet Gynecol. 2014;124(1):57-67
    """)


if __name__ == "__main__":
    render()

