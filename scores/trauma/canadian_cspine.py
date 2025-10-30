"""
Canadian C-Spine Rule
Quy tắc quyết định chụp cột sống cổ sau chấn thương
"""

import streamlit as st


def evaluate_canadian_cspine(age, dangerous_mechanism, paresthesias,
                              simple_rear_end_mvc, sitting_position,
                              ambulatory, delayed_neck_pain,
                              midline_tenderness, unable_rotate):
    """
    Evaluate Canadian C-Spine Rule
    
    Returns:
        dict: Evaluation results with imaging recommendation
    """
    # Step 1: High-risk factors
    high_risk = any([
        age >= 65,
        dangerous_mechanism,
        paresthesias
    ])
    
    if high_risk:
        return {
            "imaging": "CẦN CHỤP",
            "step": "Bước 1: Có yếu tố nguy cơ cao",
            "recommendation": "Chụp X-quang/CT cột sống cổ ngay",
            "color": "🔴",
            "safe_to_clear": False,
            "reason": "Có ≥ 1 yếu tố nguy cơ cao"
        }
    
    # Step 2: Low-risk factors allowing assessment
    low_risk = any([
        simple_rear_end_mvc,
        sitting_position,
        ambulatory,
        delayed_neck_pain
    ])
    
    if not low_risk:
        return {
            "imaging": "CẦN CHỤP",
            "step": "Bước 2: Không có yếu tố cho phép đánh giá ROM",
            "recommendation": "Không an toàn để đánh giá ROM → Chụp",
            "color": "🔴",
            "safe_to_clear": False,
            "reason": "Không đủ tiêu chí low-risk để đánh giá ROM"
        }
    
    # Step 3: Able to rotate neck 45° both ways?
    if midline_tenderness or unable_rotate:
        return {
            "imaging": "CẦN CHỤP",
            "step": "Bước 3: Đau midline hoặc không xoay cổ được 45°",
            "recommendation": "Chụp X-quang/CT cột sống cổ",
            "color": "🔴",
            "safe_to_clear": False,
            "reason": "Đau midline hoặc ROM không đầy đủ"
        }
    
    # All criteria passed
    return {
        "imaging": "KHÔNG CẦN CHỤP",
        "step": "Đạt tất cả 3 bước",
        "recommendation": "An toàn loại trừ lâm sàng (clinical clearance)",
        "color": "🟢",
        "safe_to_clear": True,
        "reason": "Không có high-risk, có low-risk, và ROM tốt"
    }


def render():
    """Render the Canadian C-Spine Rule calculator"""
    
    st.title("🍁 Canadian C-Spine Rule")
    st.markdown("""
    ### Quy Tắc Quyết Định Chụp Cột Sống Cổ
    
    **Canadian C-Spine Rule:**
    - Quy tắc 3 bước để quyết định cần chụp C-spine không
    - Độ nhạy 99.4% (tương đương NEXUS)
    - Độ đặc hiệu 45.1% (CAO HƠN NEXUS 12.9%)
    - **Giảm chụp 40-50%** (tốt hơn NEXUS 20-30%)
    
    **3 Bước Đánh Giá:**
    
    **Bước 1: Có yếu tố NGUY CƠ CAO không?**
    - Tuổi ≥ 65
    - Cơ chế chấn thương nguy hiểm
    - Tê bì tay/chân
    
    → Nếu CÓ → **CHỤP**
    
    **Bước 2: Có yếu tố NGUY CƠ THẤP cho phép đánh giá ROM?**
    - Tai nạn xe đâm đuôi đơn giản
    - Ngồi được ở cấp cứu
    - Đi lại được bất kỳ lúc nào
    - Đau cổ xuất hiện muộn (delayed onset)
    
    → Nếu KHÔNG → **CHỤP**
    
    **Bước 3: Có thể xoay cổ 45° sang 2 bên?**
    - Active rotation 45° trái + phải
    - Không đau midline
    
    → Nếu KHÔNG → **CHỤP**
    → Nếu CÓ → **KHÔNG CẦN CHỤP**
    
    **Lưu ý:**
    - Chỉ áp dụng cho chấn thương cùn
    - Bệnh nhân alert (GCS 15)
    - Không áp dụng < 16 tuổi
    """)
    
    st.markdown("---")
    
    # Inclusion/Exclusion
    with st.expander("⚠️ Tiêu Chí Áp Dụng", expanded=True):
        st.markdown("""
        ### ✅ Áp dụng cho:
        - Chấn thương cùn (blunt trauma)
        - Alert (GCS 15)
        - Stable vital signs
        - ≥ 16 tuổi
        
        ### ❌ KHÔNG áp dụng nếu:
        - < 16 tuổi
        - Chấn thương xuyên thủng
        - GCS < 15
        - Không ổn định huyết động
        - Tổn thương C-spine đã biết
        - Paralysis do chấn thương cấp
        """)
    
    st.markdown("---")
    
    # Step 1: High-Risk Factors
    st.subheader("🔴 Bước 1: Yếu Tố Nguy Cơ Cao")
    st.info("Nếu có BẤT KỲ yếu tố nào → CHỤP ngay, không cần đánh giá tiếp")
    
    age = st.number_input(
        "**Tuổi**",
        min_value=16,
        max_value=120,
        value=35,
        step=1
    )
    
    high_risk_age = age >= 65
    if high_risk_age:
        st.warning(f"⚠️ Tuổi ≥ 65 ({age} tuổi) → NGUY CƠ CAO → CẦN CHỤP")
    
    st.markdown("---")
    
    dangerous_mechanism = st.checkbox(
        "**Cơ chế chấn thương nguy hiểm**",
        help="Xem danh sách chi tiết bên dưới"
    )
    
    if dangerous_mechanism:
        st.warning("⚠️ Cơ chế nguy hiểm → NGUY CƠ CAO → CẦN CHỤP")
    
    with st.expander("📋 Cơ Chế Chấn Thương Nguy Hiểm"):
        st.markdown("""
        **Cơ chế nguy hiểm bao gồm:**
        - Rơi từ độ cao ≥ 1 m (≥ 3 feet) hoặc 5 bậc cầu thang
        - Tải trọng trục lên đầu (diving, surfing)
        - Tai nạn xe máy tốc độ cao
        - Tai nạn ô tô:
          + Tốc độ > 100 km/h
          + Lật xe (rollover)
          + Người bị văng ra ngoài (ejection)
        - Tai nạn xe đạp va chạm với vật cứng
        - Chấn thương do thiết bị motorized recreation
        """)
    
    st.markdown("---")
    
    paresthesias = st.checkbox(
        "**Tê bì/dị cảm tại tứ chi**",
        help="Paresthesias trong tay, chân sau chấn thương"
    )
    
    if paresthesias:
        st.error("🚨 Tê bì tứ chi → NGUY CƠ CAO → CẦN CHỤP NGAY")
    
    st.markdown("---")
    
    # Step 2: Low-Risk Factors
    st.subheader("🟡 Bước 2: Yếu Tố Cho Phép Đánh Giá ROM")
    st.info("Cần có ≥ 1 yếu tố để AN TOÀN đánh giá range of motion")
    
    simple_rear_end_mvc = st.checkbox(
        "**Tai nạn xe đâm đuôi đơn giản**",
        help="Không lật, không đẩy vào xe khác, không xe bus/xe tải, tốc độ thấp"
    )
    
    with st.expander("📋 Tiêu Chí 'Tai Nạn Đâm Đuôi Đơn Giản'"):
        st.markdown("""
        **Phải thỏa TẤT CẢ:**
        - Xe bị đâm từ phía sau
        - KHÔNG lật xe
        - KHÔNG đẩy vào xe khác
        - KHÔNG bus hoặc xe tải lớn
        - KHÔNG tốc độ cao
        
        **Nếu không đủ tiêu chí → Không tích vào ô này**
        """)
    
    sitting_position = st.checkbox(
        "**Ngồi được ở cấp cứu**",
        help="Bệnh nhân có thể tự ngồi (trên giường hoặc ghế)"
    )
    
    ambulatory = st.checkbox(
        "**Đi lại được bất kỳ lúc nào sau chấn thương**",
        help="Đã đi lại được (kể cả tại hiện trường) - không nhất thiết lúc này"
    )
    
    delayed_neck_pain = st.checkbox(
        "**Đau cổ xuất hiện muộn (delayed onset)**",
        help="Không đau cổ ngay sau chấn thương, đau xuất hiện sau đó"
    )
    
    st.markdown("---")
    
    # Step 3: ROM Assessment
    st.subheader("🔵 Bước 3: Đánh Giá Xoay Cổ")
    st.info("Chỉ đánh giá nếu ĐỦ điều kiện từ Bước 1 và 2")
    
    midline_tenderness = st.checkbox(
        "**Đau khi ấn midline cột sống cổ**",
        help="Palpation chính giữa C-spine từ occiput đến C7"
    )
    
    if midline_tenderness:
        st.warning("⚠️ Đau midline → CẦN CHỤP")
    
    unable_rotate = st.checkbox(
        "**Không thể xoay cổ 45° sang cả 2 bên**",
        help="Active rotation trái và phải, mỗi bên 45°"
    )
    
    if unable_rotate:
        st.warning("⚠️ ROM không đầy đủ → CẦN CHỤP")
    
    with st.expander("📋 Cách Đánh Giá ROM Chính Xác"):
        st.markdown("""
        ### Active Range of Motion Test:
        
        **Chuẩn bị:**
        1. Bệnh nhân ngồi hoặc nằm thoải mái
        2. Giải thích: "Tôi sẽ yêu cầu anh/chị xoay cổ. Nếu đau, hãy dừng ngay."
        3. Tháo cổ cứng
        
        **Thực hiện:**
        1. "Từ từ xoay cổ sang bên trái"
        2. Quan sát: Xoay được 45° không? (nhìn qua vai)
        3. "Từ từ xoay cổ sang bên phải"
        4. Quan sát: Xoay được 45° không?
        
        **Đánh giá:**
        - **PASS:** Xoay được 45° cả 2 bên, không đau
        - **FAIL:** Xoay < 45° hoặc đau khi xoay
        
        **45° = Nhìn thấy qua vai**
        - Không cần đo chính xác
        - Ước lượng lâm sàng
        - Nếu nghi ngờ → Coi như FAIL
        """)
    
    st.markdown("---")
    
    # Evaluate button
    if st.button("📊 Đánh Giá Canadian C-Spine Rule", type="primary", use_container_width=True):
        result = evaluate_canadian_cspine(
            age, dangerous_mechanism, paresthesias,
            simple_rear_end_mvc, sitting_position, ambulatory, delayed_neck_pain,
            midline_tenderness, unable_rotate
        )
        
        st.markdown("---")
        st.subheader("📈 Kết Quả Đánh Giá")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Kết Luận",
                result['step'],
                help="Bước kết luận trong algorithm"
            )
        
        with col2:
            if result['safe_to_clear']:
                st.success(f"{result['color']} {result['imaging']}")
            else:
                st.error(f"{result['color']} {result['imaging']}")
        
        st.markdown("---")
        
        # Detailed result
        if result['safe_to_clear']:
            st.success(f"""
            ### ✅ {result['imaging']}
            
            **Lý do:** {result['reason']}
            
            **Khuyến nghị:** {result['recommendation']}
            
            **Độ tin cậy:** Độ nhạy 99.4%, NPV 100%
            
            ---
            
            ### 📝 Clinical Clearance Completed:
            
            **✅ Bước 1:** KHÔNG có yếu tố nguy cơ cao
            - Tuổi < 65
            - Cơ chế không nguy hiểm
            - Không tê bì
            
            **✅ Bước 2:** CÓ yếu tố cho phép đánh giá ROM
            - Có ≥ 1 yếu tố low-risk
            
            **✅ Bước 3:** ROM đầy đủ
            - Không đau midline
            - Xoay cổ 45° cả 2 bên
            
            **→ AN TOÀN loại trừ lâm sàng**
            
            **Ghi nhận:**
            - "Canadian C-Spine Rule negative"
            - "Able to rotate 45° bilaterally"
            - "C-spine clinically cleared"
            - "Collar removed"
            """)
            
        else:
            st.error(f"""
            ### 🔴 {result['imaging']}
            
            **{result['step']}**
            
            **Lý do:** {result['reason']}
            
            **Khuyến nghị:** {result['recommendation']}
            """)
            
            st.warning("""
            ### 🏥 Xử Trí:
            
            **1. Giữ cổ cứng**
            
            **2. Chụp hình ảnh:**
            - **CT C-spine:** Lựa chọn đầu (nhanh, chính xác, đặc biệt nếu có high-risk)
            - **X-quang 3 tư thế:** Nếu không có CT
            
            **3. Theo dõi:**
            - C-spine precautions cho đến có kết quả
            - Log-roll khi di chuyển
            """)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông Tin Bổ Sung")
    
    with st.expander("📊 Độ Chính Xác"):
        st.markdown("""
        ### Nghiên cứu gốc (Stiell et al., NEJM 2001):
        
        **Quy mô:** 8,924 bệnh nhân
        
        **Kết quả:**
        - **Độ nhạy:** 99.4% (96.0-100%)
        - **Độ đặc hiệu:** 45.1%
        - **NPV:** 100%
        
        **So với NEXUS (head-to-head, NEJM 2003):**
        
        | Metric | Canadian C-Spine | NEXUS |
        |--------|------------------|-------|
        | Độ nhạy | 99.4% | 90.7% |
        | Độ đặc hiệu | 45.1% | 36.8% |
        | Giảm chụp | 42.5% | 12.6% |
        
        **Ưu điểm Canadian C-Spine:**
        - Giảm chụp NHIỀU HƠN (40-50% vs 20-30%)
        - Độ đặc hiệu cao hơn
        - NPV 100% (rất tin cậy)
        
        **Nhược điểm:**
        - Phức tạp hơn (3 bước, nhiều tiêu chí)
        - Cần training và practice
        - Cần đánh giá ROM (không phải lúc nào cũng làm được)
        """)
    
    with st.expander("💡 Tips Áp Dụng Thành Công"):
        st.markdown("""
        ### Bí quyết sử dụng hiệu quả:
        
        **1. Nhớ algorithm:**
        - In ra poster dán tường
        - Pocket card
        - App trên điện thoại
        
        **2. Practice makes perfect:**
        - Dùng cho MỌI bệnh nhân chấn thương
        - Càng dùng càng quen
        - Thảo luận cases khó với đồng nghiệp
        
        **3. ROM assessment:**
        - Tháo cổ cứng trước (nếu an toàn)
        - Yêu cầu ACTIVE rotation (bệnh nhân tự xoay)
        - KHÔNG passive (bác sĩ xoay)
        - Nếu nghi ngờ → Chụp
        
        **4. Documentation:**
        - Ghi rõ từng bước
        - Đặc biệt ROM assessment
        - "Rotated 45° bilaterally without pain"
        
        **5. Khi nào nên chụp dù rule (-):**
        - Bệnh nhân/gia đình lo lắng nhiều
        - Không tự tin về assessment
        - Cơ chế thực sự đáng ngại
        - Ankylosing spondylitis
        - Rheumatoid arthritis với C1-C2 instability
        
        **"When in doubt, image!"**
        """)
    
    # References
    st.caption("""
    **Tài liệu tham khảo:**
    - Stiell IG, et al. The Canadian C-spine rule for radiography in alert and stable trauma patients. JAMA. 2001;286(15):1841-1848
    - Stiell IG, et al. The Canadian C-spine rule versus the NEXUS low-risk criteria. NEJM. 2003;349(26):2510-2518
    """)


if __name__ == "__main__":
    render()

