"""
Paracetamol (Acetaminophen) Overdose Protocol
Rumack-Matthew Nomogram, FDA Guidelines
Life-threatening liver toxicity from acetaminophen overdose
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Paracetamol (Acetaminophen) Overdose Protocol"""
    st.subheader("💊 Ngộ Độc Paracetamol (Acetaminophen)")
    st.caption("Rumack-Matthew Nomogram, FDA Guidelines - Acetaminophen toxicity management")
    
    st.error("""
    **⚠️ NGỘ ĐỘC PARACETAMOL = CẤP CỨU Y TẾ**
    
    **Định nghĩa:**
    - Liều độc: >150 mg/kg hoặc >7.5g ở người lớn
    - Liều gây tử vong: >250 mg/kg
    - Tỷ lệ tử vong: 1-2% nếu không điều trị
    
    **Cơ chế:**
    - Quá tải glutathione → tích tụ NAPQI → tổn thương gan
    - Tổn thương gan xảy ra sau 24-48 giờ
    - Có thể phòng ngừa hoàn toàn nếu điều trị sớm
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: RISK ASSESSMENT ==========
    st.markdown("### 📊 Đánh Giá Nguy Cơ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        time_since_ingestion = st.number_input(
            "**Thời gian từ khi uống (giờ):**",
            min_value=0.0,
            max_value=168.0,
            value=4.0,
            step=0.5,
            help="Nhập số giờ từ khi uống paracetamol"
        )
        
        amount_ingested = st.number_input(
            "**Liều đã uống (mg):**",
            min_value=0,
            max_value=50000,
            value=0,
            step=100,
            help="Tổng liều paracetamol đã uống (mg)"
        )
        
        weight = st.number_input(
            "**Cân nặng (kg):**",
            min_value=1.0,
            max_value=200.0,
            value=70.0,
            step=0.5,
            help="Cân nặng bệnh nhân"
        )
    
    with col2:
        if amount_ingested > 0 and weight > 0:
            dose_per_kg = amount_ingested / weight
            
            st.info(f"""
            **Liều tính theo kg:** {dose_per_kg:.1f} mg/kg
            
            **Đánh giá:**
            - **Liều an toàn:** <150 mg/kg
            - **Liều độc:** ≥150 mg/kg
            - **Liều gây tử vong:** ≥250 mg/kg
            """)
            
            if dose_per_kg >= 250:
                st.error("🚨 **NGUY CƠ RẤT CAO** - Liều gây tử vong!")
            elif dose_per_kg >= 150:
                st.warning("⚠️ **NGUY CƠ CAO** - Liều độc, cần điều trị ngay!")
            elif dose_per_kg >= 100:
                st.warning("⚠️ **NGUY CƠ TRUNG BÌNH** - Cần đánh giá thêm")
            else:
                st.success("✅ **NGUY CƠ THẤP** - Liều an toàn")
    
    st.markdown("---")
    
    # ========== SECTION 2: SERUM LEVEL & NOMOGRAM ==========
    st.markdown("### 📈 Nồng Độ Huyết Thanh & Nomogram")
    
    has_serum_level = st.checkbox("Có kết quả nồng độ paracetamol trong huyết thanh", value=False)
    
    if has_serum_level:
        serum_level = st.number_input(
            "**Nồng độ paracetamol (mcg/mL):**",
            min_value=0.0,
            max_value=500.0,
            value=0.0,
            step=0.1,
            help="Nồng độ paracetamol trong huyết thanh"
        )
        
        if serum_level > 0 and time_since_ingestion >= 4:
            # Rumack-Matthew Nomogram
            # Treatment line: 150 mcg/mL at 4h, 37.5 mcg/mL at 24h
            # Safe line: 200 mcg/mL at 4h, 50 mcg/mL at 24h
            
            if time_since_ingestion <= 24:
                # Interpolate treatment line
                if time_since_ingestion <= 4:
                    treatment_threshold = 150
                elif time_since_ingestion <= 8:
                    treatment_threshold = 150 - (time_since_ingestion - 4) * (150 - 75) / 4
                elif time_since_ingestion <= 12:
                    treatment_threshold = 75 - (time_since_ingestion - 8) * (75 - 50) / 4
                else:
                    treatment_threshold = 50 - (time_since_ingestion - 12) * (50 - 37.5) / 12
                
                if serum_level >= treatment_threshold:
                    st.error(f"""
                    🚨 **CẦN ĐIỀU TRỊ NGAY!**
                    
                    - Nồng độ: {serum_level:.1f} mcg/mL
                    - Ngưỡng điều trị: {treatment_threshold:.1f} mcg/mL
                    - Bệnh nhân ở trên đường điều trị → Cần NAC
                    """)
                else:
                    st.success(f"""
                    ✅ **KHÔNG CẦN ĐIỀU TRỊ**
                    
                    - Nồng độ: {serum_level:.1f} mcg/mL
                    - Ngưỡng điều trị: {treatment_threshold:.1f} mcg/mL
                    - Bệnh nhân ở dưới đường điều trị → An toàn
                    """)
            else:
                st.warning("⚠️ Nomogram chỉ áp dụng trong 24 giờ đầu. Đánh giá dựa trên triệu chứng và xét nghiệm gan.")
    
    st.markdown("---")
    
    # ========== SECTION 3: CLINICAL PRESENTATION ==========
    st.markdown("### 🔍 Triệu Chứng Lâm Sàng")
    
    st.markdown("""
    **Giai đoạn ngộ độc:**
    
    **1. Giai đoạn 1 (0-24 giờ):**
    - Thường không có triệu chứng hoặc triệu chứng nhẹ
    - Buồn nôn, nôn, mệt mỏi
    - Xét nghiệm gan: Bình thường
    
    **2. Giai đoạn 2 (24-72 giờ):**
    - Triệu chứng cải thiện (giai đoạn "yên lặng")
    - Men gan bắt đầu tăng (ALT, AST)
    - Đau bụng vùng gan
    
    **3. Giai đoạn 3 (72-96 giờ):**
    - Suy gan cấp
    - Vàng da, rối loạn đông máu
    - Encephalopathy gan
    - Có thể tử vong
    
    **4. Giai đoạn 4 (4-14 ngày):**
    - Hồi phục hoặc tử vong
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT PROTOCOL ==========
    st.markdown("### 💊 Phác Đồ Điều Trị")
    
    treatment_indication = st.radio(
        "**Chỉ định điều trị:**",
        [
            "Cần điều trị (NAC)",
            "Không cần điều trị",
            "Không chắc chắn - Cần đánh giá thêm"
        ],
        key="paracetamol_treatment"
    )
    
    st.markdown("---")
    
    if "Cần điều trị" in treatment_indication:
        render_nac_protocol(time_since_ingestion)
    elif "Không chắc chắn" in treatment_indication:
        st.warning("""
        **Đánh giá thêm:**
        
        1. **Lấy nồng độ paracetamol:**
           - Nếu <4 giờ: Chờ đến 4 giờ rồi lấy lại
           - Nếu ≥4 giờ: Lấy ngay
        
        2. **Đánh giá yếu tố nguy cơ:**
           - Suy dinh dưỡng
           - Nghiện rượu
           - Dùng thuốc cảm ứng enzyme (rifampin, phenytoin)
           - Bệnh gan mạn tính
        
        3. **Nếu có yếu tố nguy cơ:** Cân nhắc điều trị sớm
        """)
    else:
        st.success("""
        **Theo dõi:**
        - Không cần điều trị
        - Theo dõi triệu chứng
        - Có thể xuất viện nếu không có triệu chứng sau 24 giờ
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SPECIAL CONSIDERATIONS ==========
    st.markdown("### 👥 Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Yếu tố nguy cơ tổn thương gan:**
        - Suy dinh dưỡng
        - Nghiện rượu
        - Dùng thuốc cảm ứng enzyme
        - Bệnh gan mạn tính
        - Trẻ em <6 tuổi (ít nguy cơ hơn)
        
        **Uống kéo dài:**
        - Uống liều cao kéo dài (>4g/ngày)
        - Cần điều trị nếu ALT >1000 hoặc có triệu chứng
        """)
    
    with col2:
        st.markdown("""
        **Điều trị hỗ trợ:**
        - **Than hoạt:** Nếu <1 giờ, không uống NAC cùng lúc
        - **Rửa dạ dày:** Nếu <1 giờ và không có chống chỉ định
        - **Theo dõi:** ALT, AST, PT/INR, Bilirubin
        
        **Chống chỉ định NAC:**
        - Không có chống chỉ định tuyệt đối
        - Dị ứng: Dùng liều thấp hơn hoặc premedication
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: MONITORING ==========
    st.markdown("### 📈 Theo Dõi")
    
    st.markdown("""
    **Trong quá trình điều trị NAC:**
    
    **Xét nghiệm:**
    - **ALT, AST:** Mỗi 12-24 giờ
    - **PT/INR:** Mỗi 12-24 giờ
    - **Bilirubin:** Mỗi 24 giờ
    - **Creatinine:** Mỗi 24 giờ
    
    **Triệu chứng:**
    - Đau bụng vùng gan
    - Vàng da
    - Rối loạn đông máu
    - Encephalopathy gan
    
    **Dấu hiệu cảnh báo:**
    - 🚨 ALT >1000 U/L → Tổn thương gan
    - 🚨 PT >1.5x bình thường → Rối loạn đông máu
    - 🚨 Encephalopathy → Suy gan cấp
    - 🚨 pH <7.3 + Lactate >3.0 → Cần ghép gan
    """)
    
    st.markdown("---")
    
    # ========== REFERENCES ==========
    render_references_section(get_references("paracetamol_overdose"))


def render_nac_protocol(time_since_ingestion: float):
    """N-Acetylcysteine (NAC) Treatment Protocol"""
    st.error("## 💉 PROTOCOL ĐIỀU TRỊ N-ACETYLCYSTEINE (NAC)")
    
    st.markdown("""
    **NAC là thuốc giải độc đặc hiệu:**
    - Bổ sung glutathione
    - Ngăn chặn tổn thương gan
    - Hiệu quả cao nếu điều trị sớm (<8 giờ)
    """)
    
    st.markdown("---")
    
    # IV Protocol
    st.markdown("### 📍 Đường Tĩnh Mạch (IV) - Phổ Biến Nhất")
    
    st.info("""
    **Phác đồ 21 giờ (FDA):**
    
    **Liều nạp (Loading):**
    - 150 mg/kg trong 60 phút
    
    **Liều duy trì 1:**
    - 50 mg/kg trong 4 giờ
    
    **Liều duy trì 2:**
    - 100 mg/kg trong 16 giờ
    
    **Tổng thời gian:** 21 giờ
    **Tổng liều:** 300 mg/kg
    """)
    
    # Calculate doses
    weight = st.number_input(
        "**Cân nặng (kg):**",
        min_value=1.0,
        max_value=200.0,
        value=70.0,
        step=0.5,
        key="nac_weight"
    )
    
    if weight > 0:
        loading_dose = weight * 150
        maintenance_1 = weight * 50
        maintenance_2 = weight * 100
        total_dose = weight * 300
        
        st.success(f"""
        **Liều tính toán (cho {weight:.1f} kg):**
        
        - **Liều nạp:** {loading_dose:.0f} mg trong 60 phút
        - **Liều duy trì 1:** {maintenance_1:.0f} mg trong 4 giờ
        - **Liều duy trì 2:** {maintenance_2:.0f} mg trong 16 giờ
        - **Tổng liều:** {total_dose:.0f} mg
        
        **Pha trong:** D5W hoặc NS
        - Liều nạp: Pha trong 200 mL
        - Liều duy trì: Pha trong 500-1000 mL
        """)
    
    st.markdown("---")
    
    # Oral Protocol
    st.markdown("### 📍 Đường Uống (PO) - Thay Thế")
    
    st.info("""
    **Phác đồ 72 giờ:**
    
    **Liều nạp:**
    - 140 mg/kg
    
    **Liều duy trì:**
    - 70 mg/kg mỗi 4 giờ × 17 liều
    
    **Tổng thời gian:** 72 giờ
    **Tổng liều:** 1330 mg/kg
    
    **Ưu điểm:** Rẻ hơn, không cần IV
    **Nhược điểm:** Dài hơn, có thể nôn
    """)
    
    if weight > 0:
        oral_loading = weight * 140
        oral_maintenance = weight * 70
        
        st.success(f"""
        **Liều tính toán (cho {weight:.1f} kg):**
        
        - **Liều nạp:** {oral_loading:.0f} mg
        - **Liều duy trì:** {oral_maintenance:.0f} mg mỗi 4 giờ × 17 liều
        
        **Dạng:** Mucomyst 20% (200 mg/mL)
        - Pha trong nước hoặc nước trái cây
        - Uống qua ống thông mũi-dạ dày nếu cần
        """)
    
    st.markdown("---")
    
    # Timing
    st.markdown("### ⏰ Thời Điểm Điều Trị")
    
    if time_since_ingestion < 8:
        st.success(f"""
        ✅ **ĐIỀU TRỊ SỚM** ({time_since_ingestion:.1f} giờ)
        
        - Hiệu quả cao nhất
        - Ngăn chặn tổn thương gan hoàn toàn
        - Tiên lượng tốt
        """)
    elif time_since_ingestion < 24:
        st.warning(f"""
        ⚠️ **ĐIỀU TRỊ MUỘN** ({time_since_ingestion:.1f} giờ)
        
        - Vẫn có hiệu quả
        - Cần điều trị đầy đủ
        - Theo dõi chặt chẽ
        """)
    else:
        st.error(f"""
        🚨 **ĐIỀU TRỊ RẤT MUỘN** ({time_since_ingestion:.1f} giờ)
        
        - Hiệu quả giảm nhưng vẫn nên điều trị
        - Tổn thương gan có thể đã xảy ra
        - Cần điều trị hỗ trợ gan
        - Cân nhắc ghép gan nếu suy gan nặng
        """)
    
    st.markdown("---")
    
    # Side Effects
    st.markdown("### ⚠️ Tác Dụng Phụ NAC")
    
    st.warning("""
    **Tác dụng phụ thường gặp:**
    - **IV:** Phản ứng dị ứng (anaphylactoid) - 10-20%
      - Nổi mề đay, ngứa, phù
      - Giảm tốc độ truyền, premedication (diphenhydramine)
    
    - **PO:** Buồn nôn, nôn - 30-50%
      - Pha loãng, uống từng ngụm nhỏ
      - Có thể dùng ondansetron
    
    **Xử trí phản ứng dị ứng:**
    - Tạm dừng truyền
    - Diphenhydramine 25-50 mg IV
    - Giảm tốc độ truyền xuống 50%
    - Tiếp tục điều trị
    """)

