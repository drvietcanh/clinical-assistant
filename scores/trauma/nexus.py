"""
NEXUS C-Spine Rule
Quy tắc đánh giá cần chụp X-quang cột sống cổ sau chấn thương
"""

import streamlit as st


def evaluate_nexus(midline_tenderness, altered_mental_status, intoxication, 
                    neurological_deficit, distracting_injury):
    """
    Evaluate NEXUS C-Spine criteria
    
    Args:
        midline_tenderness: Posterior midline C-spine tenderness (True/False)
        altered_mental_status: Altered level of consciousness (True/False)
        intoxication: Evidence of intoxication (True/False)
        neurological_deficit: Focal neurological deficit (True/False)
        distracting_injury: Distracting painful injury (True/False)
    
    Returns:
        dict: Evaluation results
    """
    # If ANY criterion is present → Imaging required
    imaging_required = any([
        midline_tenderness,
        altered_mental_status,
        intoxication,
        neurological_deficit,
        distracting_injury
    ])
    
    if imaging_required:
        return {
            "imaging": "CẦN CHỤP",
            "recommendation": "Chỉ định chụp X-quang/CT cột sống cổ",
            "reason": "Có ≥ 1 tiêu chí NEXUS dương tính",
            "sensitivity": "Độ nhạy 99.6% (tin cậy loại trừ tổn thương)",
            "color": "🔴",
            "safe_to_clear": False
        }
    else:
        return {
            "imaging": "KHÔNG CẦN CHỤP",
            "recommendation": "Có thể loại trừ lâm sàng (clinical clearance)",
            "reason": "TẤT CẢ 5 tiêu chí NEXUS âm tính",
            "sensitivity": "Độ nhạy 99.6% - An toàn loại trừ tổn thương C-spine",
            "color": "🟢",
            "safe_to_clear": True
        }


def render():
    """Render the NEXUS C-Spine Rule calculator"""
    
    st.title("🦴 NEXUS C-Spine Rule")
    st.markdown("""
    ### Quy Tắc Loại Trừ Tổn Thương Cột Sống Cổ
    
    **NEXUS (National Emergency X-Radiography Utilization Study):**
    - Công cụ quyết định lâm sàng để loại trừ tổn thương cột sống cổ
    - Giúp GIẢM chụp X-quang/CT không cần thiết
    - Độ nhạy 99.6% (rất an toàn)
    - Validate trên > 34,000 bệnh nhân
    
    **5 Tiêu Chí NEXUS (Mnemonic: NSAID):**
    1. **N**o midline tenderness (Không đau chính giữa)
    2. **S**ober/Normal mental status (Không rối loạn ý thức)
    3. **A**lert (Không say rượu/ma túy)
    4. **I**njury not distracting (Không có tổn thương gây mất tập trung)
    5. **D**eficit, no neurological (Không có triệu chứng thần kinh)
    
    **Quy tắc:**
    - **TẤT CẢ 5 tiêu chí âm tính** → Không cần chụp (an toàn loại trừ lâm sàng)
    - **BẤT KỲ tiêu chí nào dương tính** → Cần chụp X-quang/CT
    
    **Lưu ý:**
    - Chỉ áp dụng cho chấn thương KHÔNG xuyên thủng
    - Đánh giá TRƯỚC khi tháo cổ cứng
    - Độ nhạy cao (99.6%) nhưng độ đặc hiệu thấp (12.9%)
    """)
    
    st.markdown("---")
    
    # Inclusion/Exclusion criteria
    with st.expander("⚠️ Tiêu Chí Áp Dụng NEXUS", expanded=True):
        st.markdown("""
        ### ✅ Áp dụng cho:
        - Bệnh nhân chấn thương BẤT KỲ cơ chế nào
        - Nghi ngờ tổn thương cột sống cổ
        - Chấn thương cùn (blunt trauma)
        - Mọi lứa tuổi (kể cả trẻ em ≥ 2 tuổi)
        
        ### ❌ KHÔNG áp dụng nếu:
        - Chấn thương xuyên thủng (penetrating trauma)
        - Có tổn thương C-spine đã biết
        - Đã chụp hình ảnh C-spine rồi
        - < 2 tuổi
        - Bệnh nhân không đánh giá được (hôn mê sâu, đặt nội khí quản)
        
        ### 🚨 Luôn chụp nếu:
        - Cơ chế chấn thương nguy hiểm cao (rơi > 3m, tai nạn xe tốc độ cao)
        - Bệnh nhân có triệu chứng thần kinh khu trú
        - Bất tỉnh kéo dài
        - Gãy nhiều xương sọ
        """)
    
    st.markdown("---")
    
    # NEXUS Criteria Evaluation
    st.subheader("📋 Đánh Giá 5 Tiêu Chí NEXUS")
    
    st.info("""
    **Hướng dẫn:** Đánh giá từng tiêu chí. Tick vào ô nếu tiêu chí DƯƠNG TÍNH (có bất thường)
    """)
    
    # 1. Midline tenderness
    st.markdown("### 1️⃣ Đau Chính Giữa Cột Sống Cổ")
    midline_tenderness = st.checkbox(
        "**Có đau khi ấn chính giữa (midline) cột sống cổ sau**",
        help="Palpation từ C1 đến C7/T1. Đau ở midline (KHÔNG phải cạnh cột sống)"
    )
    if midline_tenderness:
        st.warning("⚠️ Tiêu chí 1 DƯƠNG TÍNH → CẦN CHỤP")
    
    st.markdown("---")
    
    # 2. Altered mental status
    st.markdown("### 2️⃣ Rối Loạn Ý Thức")
    altered_mental_status = st.checkbox(
        "**Có rối loạn mức độ ý thức (GCS < 15, lú lẫn, mất định hướng)**",
        help="GCS < 15 HOẶC không trả lời đúng person/place/time/event"
    )
    if altered_mental_status:
        st.warning("⚠️ Tiêu chí 2 DƯƠNG TÍNH → CẦN CHỤP")
    
    st.markdown("---")
    
    # 3. Intoxication
    st.markdown("### 3️⃣ Say Rượu / Ma Túy")
    intoxication = st.checkbox(
        "**Có bằng chứng say rượu hoặc sử dụng chất kích thích**",
        help="Lâm sàng say rượu HOẶC dùng thuốc/ma túy ảnh hưởng đến đánh giá"
    )
    if intoxication:
        st.warning("⚠️ Tiêu chí 3 DƯƠNG TÍNH → CẦN CHỤP")
    
    st.markdown("---")
    
    # 4. Neurological deficit
    st.markdown("### 4️⃣ Triệu Chứng Thần Kinh Khu Trú")
    neurological_deficit = st.checkbox(
        "**Có triệu chứng thần kinh khu trú (yếu chi, tê, giảm cảm giác)**",
        help="Motor weakness, sensory deficit, reflex abnormality"
    )
    if neurological_deficit:
        st.error("🚨 Tiêu chí 4 DƯƠNG TÍNH → CẦN CHỤP NGAY")
    
    st.markdown("---")
    
    # 5. Distracting injury
    st.markdown("### 5️⃣ Tổn Thương Gây Mất Tập Trung")
    st.caption("Tổn thương đau nặng ở vị trí khác làm bệnh nhân không chú ý đến cột sống cổ")
    distracting_injury = st.checkbox(
        "**Có tổn thương gây đau nặng, mất tập trung (fracture chi dài, bỏng nặng, v.v.)**",
        help="Ví dụ: gãy xương đùi, bỏng diện rộng, rách gan/lách cần phẫu thuật"
    )
    if distracting_injury:
        st.warning("⚠️ Tiêu chí 5 DƯƠNG TÍNH → CẦN CHỤP")
    
    st.markdown("---")
    
    # Evaluate button
    if st.button("📊 Đánh Giá NEXUS C-Spine", type="primary", use_container_width=True):
        # Evaluate
        result = evaluate_nexus(
            midline_tenderness,
            altered_mental_status,
            intoxication,
            neurological_deficit,
            distracting_injury
        )
        
        st.markdown("---")
        st.subheader("📈 Kết Quả Đánh Giá")
        
        # Summary
        positive_count = sum([
            midline_tenderness,
            altered_mental_status,
            intoxication,
            neurological_deficit,
            distracting_injury
        ])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Tiêu Chí Dương Tính",
                f"{positive_count}/5",
                help="Số tiêu chí dương tính"
            )
        
        with col2:
            if result['safe_to_clear']:
                st.success(f"{result['color']} {result['imaging']}")
            else:
                st.error(f"{result['color']} {result['imaging']}")
        
        st.markdown("---")
        
        # Detailed result
        st.subheader("🎯 Khuyến Nghị")
        
        if result['safe_to_clear']:
            st.success(f"""
            ### ✅ {result['imaging']}
            
            **Lý do:** {result['reason']}
            
            **Khuyến nghị:** {result['recommendation']}
            
            **Độ tin cậy:** {result['sensitivity']}
            
            ---
            
            ### 📝 Clinical Clearance Protocol:
            
            **1. Xác nhận lại:**
            - ✅ KHÔNG đau midline C-spine
            - ✅ GCS 15, alert & oriented
            - ✅ KHÔNG say rượu/ma túy
            - ✅ KHÔNG triệu chứng thần kinh
            - ✅ KHÔNG tổn thương gây mất tập trung
            
            **2. Đánh giá range of motion:**
            - Bệnh nhân tỉnh, hợp tác
            - Tháo cổ cứng (nếu có)
            - Yêu cầu từ từ xoay cổ trái/phải
            - Cúi/ngửa cổ
            - Nếu đau → Dừng, xem xét chụp
            
            **3. An toàn loại trừ nếu:**
            - Range of motion đầy đủ, không đau
            - Có thể tự xoay cổ 45° mỗi bên
            - Không đau khi active mobilization
            
            **4. Ghi nhận hồ sơ:**
            - "NEXUS negative (0/5 positive criteria)"
            - "Clinically cleared C-spine"
            - "No imaging required"
            """)
            
        else:
            st.error(f"""
            ### 🔴 {result['imaging']}
            
            **Lý do:** {result['reason']}
            
            **Khuyến nghị:** {result['recommendation']}
            
            **Tiêu chí dương tính:** {positive_count}/5
            """)
            
            # List positive criteria
            st.markdown("### Các Tiêu Chí Dương Tính:")
            if midline_tenderness:
                st.markdown("- ⚠️ Đau chính giữa cột sống cổ")
            if altered_mental_status:
                st.markdown("- ⚠️ Rối loạn ý thức")
            if intoxication:
                st.markdown("- ⚠️ Say rượu/ma túy")
            if neurological_deficit:
                st.markdown("- 🚨 Triệu chứng thần kinh khu trú")
            if distracting_injury:
                st.markdown("- ⚠️ Tổn thương gây mất tập trung")
            
            st.markdown("---")
            
            st.warning("""
            ### 🏥 Xử Trí Tiếp Theo:
            
            **1. Giữ nguyên cổ cứng**
            
            **2. Chụp hình ảnh:**
            - **CT C-spine:** Lựa chọn đầu tay (nhanh, chính xác)
            - **X-quang 3 tư thế:** Nếu không có CT (AP, lateral, odontoid)
            - **MRI:** Nếu có triệu chứng thần kinh hoặc nghi ngờ tổn thương ligament
            
            **3. Trong khi chờ kết quả:**
            - Giữ C-spine precautions
            - Hạn chế di chuyển
            - Log-roll nếu cần di chuyển
            
            **4. Nếu CT/X-quang bình thường nhưng:**
            - Vẫn đau midline → MRI
            - Triệu chứng thần kinh → MRI, Neurosurgery consult
            - Say rượu → Chờ tỉnh rồi tái đánh giá lâm sàng
            """)
    
    # Educational content
    st.markdown("---")
    st.subheader("📚 Thông Tin Bổ Sung")
    
    with st.expander("📊 Độ Chính Xác Của NEXUS"):
        st.markdown("""
        ### Nghiên cứu gốc (Hoffman et al., NEJM 2000):
        
        **Quy mô:** 34,069 bệnh nhân chấn thương cùn
        
        **Kết quả:**
        - **Độ nhạy (Sensitivity):** 99.6% (99.0-100%)
        - **Độ đặc hiệu (Specificity):** 12.9%
        - **NPV (Negative Predictive Value):** 99.8%
        
        **Ý nghĩa:**
        - Độ nhạy cao → An toàn loại trừ tổn thương
        - NPV cao → NEXUS (-) rất tin cậy không có tổn thương
        - Độ đặc hiệu thấp → Nhiều false positive (chụp không cần thiết)
        
        **Tổn thương bỏ sót:**
        - 8/818 tổn thương C-spine bị miss (0.98%)
        - Tất cả đều không cần can thiệp
        - Không có tổn thương quan trọng bị bỏ sót
        
        **So với không dùng rule:**
        - Giảm 20-30% số chụp X-quang
        - Tiết kiệm chi phí
        - Giảm radiation exposure
        """)
    
    with st.expander("🆚 NEXUS vs Canadian C-Spine Rule"):
        st.markdown("""
        ### So sánh 2 quy tắc phổ biến:
        
        | Đặc điểm | NEXUS | Canadian C-Spine |
        |----------|-------|------------------|
        | **Độ nhạy** | 99.6% | 99.4% |
        | **Độ đặc hiệu** | 12.9% | 45.1% |
        | **Đơn giản** | Đơn giản hơn (5 tiêu chí) | Phức tạp hơn (algorithm) |
        | **Giảm chụp** | 20-30% | 40-50% |
        | **Dễ nhớ** | Dễ nhớ (NSAID) | Khó nhớ hơn |
        | **Validation** | Rất tốt | Rất tốt |
        
        **NEXUS:**
        - ✅ Đơn giản, dễ áp dụng
        - ✅ Mọi nhân viên y tế có thể dùng
        - ❌ Nhiều false positive hơn
        
        **Canadian C-Spine:**
        - ✅ Giảm chụp nhiều hơn
        - ✅ Có đánh giá range of motion
        - ❌ Phức tạp hơn, cần training
        
        **Khuyến cáo:**
        - Chọn rule nào tùy cơ sở
        - Quan trọng là DÙNG một rule
        - Không dùng rule → Lạm dụng chụp
        - Cả 2 rule đều an toàn và hiệu quả
        """)
    
    with st.expander("💡 Chi Tiết Từng Tiêu Chí"):
        st.markdown("""
        ### 1. Midline Tenderness:
        
        **Cách đánh giá:**
        - Palpation từ occiput đến T1
        - Ấn trực tiếp lên spinous processes
        - Chính giữa (midline), KHÔNG phải cạnh
        - Hỏi: "Đau chỗ nào nhất?"
        
        **Dương tính nếu:**
        - Đau khi ấn midline C-spine
        - Bệnh nhân kêu đau rõ ràng
        
        **Âm tính nếu:**
        - Không đau hoặc đau nhẹ không rõ
        - Đau ở cơ cạnh cột sống (paraspinal muscles)
        
        ### 2. Altered Mental Status:
        
        **Đánh giá:**
        - GCS: Phải = 15
        - Orientation: Person, Place, Time, Event
        - Memory: Nhớ được sự kiện trước/sau chấn thương
        
        **Dương tính nếu:**
        - GCS < 15
        - Không trả lời đúng orientation
        - Lú lẫn, mất trí nhớ
        
        **Âm tính:**
        - GCS 15
        - Alert & oriented ×4
        
        ### 3. Intoxication:
        
        **Evidence:**
        - Lâm sàng say rượu (mùi, nói khó, đi loạng choạng)
        - Sử dụng drugs/medications ảnh hưởng đến đánh giá
        - Lịch sử dùng chất trước chấn thương
        
        **Dương tính nếu:**
        - Bất kỳ bằng chứng nào của intoxication
        - Nghi ngờ clinical judgment bị ảnh hưởng
        
        **Lưu ý:**
        - Không cần BAC/drug screen
        - Đánh giá lâm sàng
        - Nếu nghi ngờ → Coi là (+)
        
        ### 4. Neurological Deficit:
        
        **Đánh giá:**
        - Motor: Sức cơ 4 chi
        - Sensory: Đối xứng 2 bên?
        - Reflexes: Tăng? Giảm? Babinski?
        
        **Dương tính:**
        - Yếu chi
        - Tê, giảm cảm giác
        - Reflex bất thường
        - Mất kiểm soát tiểu/tiện
        
        **Âm tính:**
        - Motor 5/5 toàn bộ
        - Sensory intact
        - Reflexes bình thường
        
        ### 5. Distracting Injury:
        
        **Định nghĩa:**
        - Tổn thương đau nặng
        - Làm bệnh nhân "mất tập trung" không chú ý cột sống cổ
        - Clinical judgment
        
        **Ví dụ dương tính:**
        - Gãy xương đùi, xương cánh tay
        - Bỏng nặng diện rộng
        - Đa chấn thương nặng
        - Chấn thương bụng cần phẫu thuật
        - Pneumothorax có triệu chứng
        
        **Ví dụ âm tính:**
        - Rách da nhỏ
        - Bầm tím đơn thuần
        - Gãy ngón tay/chân
        
        **Tranh cãi:**
        - Tiêu chí chủ quan nhất
        - Không định nghĩa rõ ràng
        - Khi nghi ngờ → Coi là (+)
        """)
    
    with st.expander("🚨 Các Tình Huống Đặc Biệt"):
        st.markdown("""
        ### 1. Trẻ em:
        
        **< 2 tuổi:**
        - NEXUS KHÔNG validated
        - Đánh giá khó (không hợp tác)
        - Liberal indication for imaging
        
        **≥ 2 tuổi:**
        - Có thể dùng NEXUS
        - Cần điều chỉnh criteria
        - Distracting injury khó đánh giá
        
        **PECARN (Pediatric Emergency Care Applied Research Network):**
        - Rule riêng cho trẻ em
        - Tham khảo nếu có
        
        ### 2. Người cao tuổi:
        
        **Lưu ý:**
        - Nguy cơ tổn thương cao hơn
        - Cơ chế chấn thương nhẹ cũng có thể gãy
        - Osteoporosis, spondylosis
        
        **Liberal imaging nếu:**
        - Cơ chế nguy hiểm (rơi cầu thang)
        - Đau cổ kéo dài
        - Có bệnh lý cột sống trước đó
        
        ### 3. Ankylosing Spondylitis (AS):
        
        **Nguy cơ rất cao:**
        - Cột sống cứng như "bamboo spine"
        - Dễ gãy với chấn thương nhẹ
        - Thường gãy C6-C7 hoặc cervicothoracic junction
        
        **Khuyến cáo:**
        - Không dùng NEXUS
        - LUÔN chụp nếu có chấn thương
        - CT toàn bộ C-spine + T-spine
        
        ### 4. Bệnh nhân đặt nội khí quản:
        
        **Vấn đề:**
        - Không đánh giá được mental status
        - Không đánh giá được distracting injury
        - Có thể có thuốc진정/giãn cơ
        
        **Khuyến cáo:**
        - Không dùng NEXUS
        - Chụp CT C-spine thường quy
        - Hoặc chờ tỉnh để clinical clearance
        
        ### 5. Down Syndrome:
        
        **Nguy cơ cao:**
        - 10-20% có atlantoaxial instability
        - Dễ tổn thương C1-C2
        
        **Khuyến cáo:**
        - Liberal imaging
        - CT include C1-C2 chi tiết
        - Neurosurgery consult
        """)
    
    with st.expander("📋 Protocol Loại Trừ Lâm Sàng"):
        st.markdown("""
        ### C-Spine Clinical Clearance Algorithm:
        
        **Bước 1: Đánh giá có thể evaluate không?**
        - GCS 15, alert & oriented?
        - Không say rượu/ma túy?
        - Hợp tác, trả lời được câu hỏi?
        
        → Nếu KHÔNG → Chụp CT
        
        **Bước 2: Đánh giá NEXUS (hoặc Canadian C-Spine)**
        - Tất cả 5 tiêu chí âm tính?
        
        → Nếu CÓ bất kỳ tiêu chí (+) → Chụp
        
        **Bước 3: Tháo cổ cứng**
        - Giải thích cho bệnh nhân
        - Yêu cầu ngồi hoặc nằm thoải mái
        
        **Bước 4: Đánh giá đau tự nhiên**
        - "Bây giờ cổ có đau không?"
        
        → Nếu ĐAU → Giữ cổ cứng, chụp
        
        **Bước 5: Active range of motion**
        - "Từ từ xoay cổ sang trái"
        - "Xoay sang phải"
        - "Cúi cổ về phía trước"
        - "Ngửa cổ về phía sau"
        
        → Nếu ĐAU hoặc không làm được → Chụp
        
        **Bước 6: Nếu ROM đầy đủ, không đau**
        - Yêu cầu xoay cổ 45° mỗi bên
        - Nếu làm được → C-spine cleared!
        
        **Bước 7: Ghi nhận**
        - "NEXUS negative (0/5)"
        - "Active ROM full, painless"
        - "C-spine clinically cleared"
        - "Collar removed, discharge instructions given"
        
        **Tư vấn xuất viện:**
        - Có thể đau cơ cổ vài ngày (bình thường)
        - Paracetamol/NSAID nếu cần
        - Tái khám nếu:
          + Đau nặng, kéo dài > 1 tuần
          + Yếu chi, tê bì
          + Mất kiểm soát tiểu/tiện
        """)
    
    # References
    st.markdown("---")
    st.caption("""
    **Tài liệu tham khảo:**
    - Hoffman JR, et al. Validity of a set of clinical criteria to rule out injury to the cervical spine in patients with blunt trauma. NEJM. 2000;343(2):94-99
    - Stiell IG, et al. The Canadian C-spine rule versus the NEXUS low-risk criteria. NEJM. 2003;349(26):2510-2518
    - Panacek EA, et al. Test performance of the NEXUS low-risk clinical screening criteria. Ann Emerg Med. 2001;38(1):22-25
    """)


if __name__ == "__main__":
    render()

