"""
Hypothermia Protocol
Accidental hypothermia management
Life-threatening low body temperature
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Hypothermia Protocol"""
    st.subheader("❄️ Hạ Thân Nhiệt (Hypothermia)")
    st.caption("Accidental hypothermia - Low body temperature management")
    
    st.error("""
    **⚠️ HẠ THÂN NHIỆT = CẤP CỨU Y TẾ**
    
    **Định nghĩa:**
    - Nhiệt độ cơ thể <35°C (<95°F)
    - Phân loại: Nhẹ (32-35°C), Trung bình (28-32°C), Nặng (<28°C)
    - Tỷ lệ tử vong: 10-40% tùy mức độ
    
    **Nguyên nhân:**
    - Phơi nhiễm lạnh (nước, không khí)
    - Người già, trẻ em
    - Bệnh lý kèm theo
    - Thuốc (rượu, thuốc an thần)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: RISK ASSESSMENT ==========
    st.markdown("### 📊 Đánh Giá Nguy Cơ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        body_temp = st.number_input(
            "**Nhiệt độ cơ thể (°C):**",
            min_value=20.0,
            max_value=37.0,
            value=37.0,
            step=0.1,
            help="Nhiệt độ đo được (nên đo trực tràng hoặc thực quản)"
        )
        
        exposure_duration = st.number_input(
            "**Thời gian phơi nhiễm (giờ):**",
            min_value=0.0,
            max_value=72.0,
            value=0.0,
            step=0.5,
            help="Thời gian ở môi trường lạnh"
        )
        
        has_cardiac_arrest = st.checkbox("Ngừng tim", value=False)
    
    with col2:
        if body_temp > 0:
            temp_f = body_temp * 9/5 + 32
            st.info(f"""
            **Nhiệt độ:** {body_temp:.1f}°C ({temp_f:.1f}°F)
            
            **Phân loại:**
            - **Bình thường:** 36-37.5°C
            - **Nhẹ:** 32-35°C
            - **Trung bình:** 28-32°C
            - **Nặng:** <28°C
            """)
            
            if body_temp < 28:
                st.error("🚨 **HẠ THÂN NHIỆT NẶNG** - Nguy cơ ngừng tim!")
            elif body_temp < 32:
                st.warning("⚠️ **HẠ THÂN NHIỆT TRUNG BÌNH** - Cần điều trị tích cực")
            elif body_temp < 35:
                st.warning("⚠️ **HẠ THÂN NHIỆT NHẸ** - Cần điều trị")
            else:
                st.success("✅ **NHIỆT ĐỘ BÌNH THƯỜNG**")
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL PRESENTATION ==========
    st.markdown("### 🔍 Triệu Chứng Lâm Sàng")
    
    st.markdown("""
    **Hạ thân nhiệt nhẹ (32-35°C):**
    - Run rẩy
    - Lú lẫn nhẹ
    - Nhịp tim nhanh
    - Thở nhanh
    
    **Hạ thân nhiệt trung bình (28-32°C):**
    - Ngừng run (dấu hiệu xấu)
    - Lú lẫn nặng
    - Nhịp tim chậm
    - Thở chậm
    - Giảm phản xạ
    
    **Hạ thân nhiệt nặng (<28°C):**
    - Hôn mê
    - Nhịp tim rất chậm hoặc rung thất
    - Ngừng thở
    - Giãn đồng tử
    - Có thể xuất hiện như đã chết
    """)
    
    st.markdown("---")
    
    # ========== SECTION 3: DIAGNOSIS ==========
    st.markdown("### 📋 Chẩn Đoán")
    
    st.warning("""
    **Chẩn đoán:**
    - **Nhiệt độ cơ thể <35°C**
    - Đo trực tràng hoặc thực quản là chính xác nhất
    - Nhiệt độ da có thể thấp hơn nhiều
    
    **Lưu ý:**
    - "Không ai chết cho đến khi ấm và chết"
    - Không tuyên bố tử vong cho đến khi nhiệt độ >32°C
    - Có thể hồi sức thành công sau khi làm ấm
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT PROTOCOL ==========
    st.markdown("### 💊 Phác Đồ Điều Trị")
    
    severity = st.radio(
        "**Mức độ nghiêm trọng:**",
        ["Nhẹ (32-35°C)", "Trung bình (28-32°C)", "Nặng (<28°C)", "Ngừng tim"],
        key="hypothermia_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_hypothermia()
    elif "Trung bình" in severity:
        render_moderate_hypothermia()
    elif "Nặng" in severity:
        render_severe_hypothermia()
    else:
        render_cardiac_arrest()
    
    st.markdown("---")
    
    # ========== SECTION 5: REWARMING METHODS ==========
    st.markdown("### 🔥 Phương Pháp Làm Ấm")
    
    st.info("""
    **Làm ấm ngoài (Passive & Active External):**
    
    **1. Làm ấm thụ động:**
    - Cởi quần áo ướt
    - Ủ ấm bằng chăn
    - Di chuyển đến nơi ấm
    
    **2. Làm ấm chủ động ngoài:**
    - Chăn ấm
    - Túi nước ấm (40-42°C)
    - Đèn sưởi
    - Chỉ dùng cho hạ thân nhiệt nhẹ
    
    **Làm ấm xâm lấn (Active Internal):**
    
    **1. Làm ấm đường thở:**
    - Oxy ấm ẩm (40-45°C)
    - Thở máy với khí ấm
    
    **2. Truyền dịch ấm:**
    - NS hoặc LR ấm (40-42°C)
    - 1-2L
    
    **3. Rửa khoang:**
    - Rửa dạ dày: Nước ấm
    - Rửa bàng quang: Nước ấm
    - Rửa màng phổi: Nước muối ấm
    
    **4. Lọc máu:**
    - Hemodialysis với dịch ấm
    - ECMO với làm ấm
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: CARDIAC ARREST ==========
    st.markdown("### 💔 Ngừng Tim Do Hạ Thân Nhiệt")
    
    st.error("""
    **Đặc điểm:**
    - Nhịp tim rất chậm hoặc rung thất
    - Không có mạch
    - Có thể xuất hiện như đã chết
    
    **Nguyên tắc:**
    - "Không ai chết cho đến khi ấm và chết"
    - Không tuyên bố tử vong cho đến khi nhiệt độ >32°C
    - Có thể hồi sức thành công sau khi làm ấm
    
    **Điều trị:**
    1. **CPR:** Ngay lập tức
    2. **Làm ấm:** Tích cực
    3. **Defibrillation:** Nếu VF/VT (có thể kháng trị khi lạnh)
    4. **Thuốc:** Thận trọng (chuyển hóa chậm khi lạnh)
    5. **ECMO:** Nếu có thể, làm ấm nhanh nhất
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: SPECIAL CONSIDERATIONS ==========
    st.markdown("### 👥 Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người già:**
        - Nguy cơ cao hơn
        - Có thể hạ thân nhiệt ở nhiệt độ phòng
        - Bệnh lý kèm theo
        
        **Trẻ em:**
        - Tỷ lệ diện tích/khối lượng cao
        - Mất nhiệt nhanh hơn
        - Cần làm ấm tích cực
        
        **Người nghiện rượu:**
        - Giảm cảm giác lạnh
        - Giảm run
        - Nguy cơ cao hơn
        """)
    
    with col2:
        st.markdown("""
        **Ngừng tim:**
        - Không tuyên bố tử vong khi lạnh
        - CPR kéo dài
        - ECMO nếu có thể
        
        **Afterdrop:**
        - Nhiệt độ giảm thêm khi làm ấm
        - Do máu lạnh từ ngoại vi về trung tâm
        - Cần làm ấm từ trong ra ngoài
        
        **Rewarming shock:**
        - Giãn mạch khi làm ấm
        - Hạ huyết áp
        - Cần bù dịch
        """)
    
    st.markdown("---")
    
    # ========== SECTION 8: MONITORING ==========
    st.markdown("### 📈 Theo Dõi")
    
    st.markdown("""
    **Trong quá trình điều trị:**
    
    **Dấu hiệu sinh tồn:**
    - **Nhiệt độ:** Mỗi 15-30 phút (đo trực tràng/thực quản)
    - **Huyết áp:** Continuous
    - **Nhịp tim:** Continuous
    - **ECG:** Continuous (có thể có J wave)
    
    **Xét nghiệm:**
    - **Điện giải:** Mỗi 2-4 giờ
    - **Đường huyết:** Có thể giảm
    - **Chức năng thận:** Creatinine
    - **Đông máu:** PT/INR, platelets
    
    **Dấu hiệu cảnh báo:**
    - 🚨 Ngừng tim
    - 🚨 Nhiệt độ tiếp tục giảm (afterdrop)
    - 🚨 Hạ huyết áp khi làm ấm
    - 🚨 Rối loạn nhịp tim
    """)
    
    st.markdown("---")
    
    # ========== REFERENCES ==========
    render_references_section(get_references("hypothermia"))


def render_mild_hypothermia():
    """Mild Hypothermia Protocol"""
    st.warning("## ⚠️ HẠ THÂN NHIỆT NHẸ (32-35°C)")
    
    st.markdown("""
    **Đặc điểm:**
    - Nhiệt độ: 32-35°C
    - Run rẩy
    - Lú lẫn nhẹ
    - Nhịp tim nhanh
    
    **Điều trị:**
    1. **Di chuyển:** Ra khỏi môi trường lạnh
    2. **Cởi quần áo ướt:** Ngay lập tức
    3. **Ủ ấm:** Chăn ấm
    4. **Làm ấm chủ động:** Túi nước ấm, chăn ấm
    5. **Uống nước ấm:** Nếu tỉnh táo
    
    **Theo dõi:**
    - Nhiệt độ mỗi 30 phút
    - Triệu chứng
    - Có thể xuất viện khi nhiệt độ >35°C và không có triệu chứng
    """)


def render_moderate_hypothermia():
    """Moderate Hypothermia Protocol"""
    st.error("## 🚨 HẠ THÂN NHIỆT TRUNG BÌNH (28-32°C)")
    
    st.markdown("""
    **Đặc điểm:**
    - Nhiệt độ: 28-32°C
    - Ngừng run (dấu hiệu xấu)
    - Lú lẫn nặng
    - Nhịp tim chậm
    
    **Điều trị:**
    1. **Làm ấm tích cực:**
       - Oxy ấm ẩm
       - Truyền dịch ấm (40-42°C)
       - Chăn ấm
    
    2. **Theo dõi:**
       - Nhiệt độ mỗi 15 phút
       - ECG continuous
       - Xét nghiệm: Điện giải, đường huyết
    
    3. **Điều trị hỗ trợ:**
       - Bù dịch
       - Điều chỉnh đường huyết
    
    **Mục tiêu:**
    - Nhiệt độ tăng 0.5-1°C/giờ
    - Nhiệt độ >35°C
    - Không có biến chứng
    """)


def render_severe_hypothermia():
    """Severe Hypothermia Protocol"""
    st.error("## 🚨🚨 HẠ THÂN NHIỆT NẶNG (<28°C) - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Nhiệt độ: <28°C
    - Hôn mê
    - Nhịp tim rất chậm hoặc rung thất
    - Có thể xuất hiện như đã chết
    
    **Điều trị khẩn cấp:**
    1. **ABC:** Ngay lập tức
    2. **Làm ấm tích cực:**
       - Oxy ấm ẩm
       - Truyền dịch ấm
       - Rửa khoang (dạ dày, bàng quang)
       - ECMO nếu có thể
    
    3. **ICU Monitoring:**
       - Continuous monitoring
       - Nhiệt độ mỗi 15 phút
       - ECG continuous
       - Xét nghiệm mỗi 2-4 giờ
    
    **Mục tiêu:**
    - Nhiệt độ tăng 1-2°C/giờ
    - Nhiệt độ >32°C
    - Không có ngừng tim
    """)


def render_cardiac_arrest():
    """Cardiac Arrest in Hypothermia Protocol"""
    st.error("## 🚨🚨🚨 NGỪNG TIM DO HẠ THÂN NHIỆT - ECMO")
    
    st.markdown("""
    **Đặc điểm:**
    - Nhiệt độ: <28°C
    - Không có mạch
    - Rung thất hoặc vô tâm thu
    - Có thể xuất hiện như đã chết
    
    **Nguyên tắc:**
    - "Không ai chết cho đến khi ấm và chết"
    - Không tuyên bố tử vong cho đến khi nhiệt độ >32°C
    
    **Điều trị khẩn cấp:**
    1. **CPR:** Ngay lập tức, kéo dài
    2. **Làm ấm tích cực:**
       - ECMO nếu có thể (làm ấm nhanh nhất)
       - Rửa khoang
       - Truyền dịch ấm
    
    3. **Defibrillation:**
       - Nếu VF/VT
       - Có thể kháng trị khi lạnh
       - Thử lại sau khi làm ấm
    
    4. **Thuốc:**
       - Thận trọng (chuyển hóa chậm)
       - Có thể tích tụ khi lạnh
    
    **Tiên lượng:**
    - Có thể hồi sức thành công sau khi làm ấm
    - ECMO là phương pháp làm ấm nhanh nhất
    """)

