"""
Dengue Fever Protocol (Sốt Xuất Huyết Dengue)
Very common in Vietnam, especially during rainy season
WHO 2009, 2012 guidelines
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Dengue Fever Protocol"""
    st.subheader("🦟 Sốt Xuất Huyết Dengue (Dengue Fever)")
    st.caption("WHO Guidelines 2009, 2012 - Bệnh phổ biến tại Việt Nam, đặc biệt mùa mưa")
    
    st.error("""
    **⚠️ SỐT XUẤT HUYẾT DENGUE = CẤP CỨU Y TẾ**
    
    **Đặc điểm:**
    - Bệnh do virus Dengue (4 serotype: DEN-1, DEN-2, DEN-3, DEN-4)
    - Vector: Muỗi Aedes aegypti, Aedes albopictus
    - Phân bố: Khắp cả nước, đặc biệt mùa mưa (tháng 6-11)
    - Tỷ lệ mắc: Rất cao tại Việt Nam
    
    **Phân loại (WHO 2009):**
    - Sốt xuất huyết Dengue (Dengue Fever - DF)
    - Sốt xuất huyết Dengue có dấu hiệu cảnh báo (Dengue with Warning Signs)
    - Sốt xuất huyết Dengue nặng (Severe Dengue)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLINICAL ASSESSMENT ==========
    st.markdown("### 📊 Đánh giá lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        days_of_illness = st.number_input(
            "**Số ngày bệnh:**",
            min_value=1,
            max_value=14,
            value=3,
            step=1,
            help="Số ngày từ khi khởi phát sốt"
        )
        
        fever_temp = st.number_input(
            "**Nhiệt độ hiện tại (°C):**",
            min_value=35.0,
            max_value=42.0,
            value=38.5,
            step=0.1,
            help="Nhiệt độ đo được"
        )
        
        has_warning_signs = st.checkbox("Có dấu hiệu cảnh báo", value=False)
    
    with col2:
        if days_of_illness > 0:
            st.info(f"""
            **Giai đoạn bệnh:**
            - **Ngày 1-3:** Giai đoạn sốt
            - **Ngày 3-7:** Giai đoạn nguy hiểm (có thể sốc)
            - **Ngày 7-10:** Giai đoạn hồi phục
            
            **Hiện tại:** Ngày {days_of_illness}
            {"⚠️ Giai đoạn nguy hiểm!" if 3 <= days_of_illness <= 7 else "✅ Giai đoạn an toàn hơn"}
            """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CLASSIFICATION ==========
    st.markdown("### 🔍 Phân loại theo WHO 2009")
    
    tab1, tab2, tab3 = st.tabs(["Sốt xuất huyết Dengue", "Có dấu hiệu cảnh báo", "Sốt xuất huyết Dengue nặng"])
    
    with tab1:
        st.markdown("""
        **Sốt xuất huyết Dengue (Dengue Fever - DF):**
        
        **Tiêu chuẩn:**
        - Sốt cấp tính (2-7 ngày)
        - Có ≥2 trong các dấu hiệu:
          - Đau đầu
          - Đau sau hốc mắt
          - Đau cơ, đau khớp
          - Ban xuất huyết
          - Dấu hiệu dây thắt dương tính
          - Giảm bạch cầu
        
        **Xử trí:**
        - Điều trị ngoại trú
        - Hạ sốt (Paracetamol)
        - Uống nhiều nước
        - Theo dõi tại nhà
        - Tái khám nếu có dấu hiệu cảnh báo
        """)
    
    with tab2:
        st.markdown("""
        **Sốt xuất huyết Dengue có dấu hiệu cảnh báo:**
        
        **Dấu hiệu cảnh báo:**
        - Đau bụng hoặc đau khi ấn bụng
        - Nôn liên tục
        - Tích tụ dịch (tràn dịch màng phổi, cổ chướng)
        - Chảy máu niêm mạc
        - Bồn chồn, lừ đừ
        - Gan to
        - Tăng Hct kèm giảm tiểu cầu nhanh
        
        **Xử trí:**
        - Nhập viện
        - Truyền dịch
        - Theo dõi sát
        - Chuẩn bị xử trí sốc
        """)
    
    with tab3:
        st.markdown("""
        **Sốt xuất huyết Dengue nặng (Severe Dengue):**
        
        **Tiêu chuẩn:**
        - Sốc do sốt xuất huyết Dengue (DSS)
        - Chảy máu nặng
        - Suy tạng nặng
        
        **Sốc do sốt xuất huyết Dengue:**
        - Sốc: Hạ huyết áp hoặc mạch nhanh nhỏ, chi lạnh
        - Kèm theo: Tăng Hct, giảm tiểu cầu
        
        **Xử trí:**
        - ICU
        - Truyền dịch tích cực
        - Hồi sức
        - Điều trị sốc
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: CLINICAL SIGNS ==========
    st.markdown("### 🔍 Triệu chứng lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Triệu chứng thường gặp:**
        - Sốt cao đột ngột (39-40°C)
        - Đau đầu dữ dội
        - Đau sau hốc mắt
        - Đau cơ, đau khớp
        - Mệt mỏi
        - Buồn nôn, nôn
        - Ban xuất huyết
        - Dấu hiệu dây thắt (+)
        """)
    
    with col2:
        st.markdown("""
        **Dấu hiệu cảnh báo:**
        - Đau bụng
        - Nôn liên tục
        - Chảy máu niêm mạc
        - Bồn chồn, lừ đừ
        - Gan to
        - Tích tụ dịch
        
        **Dấu hiệu sốc:**
        - Hạ huyết áp
        - Mạch nhanh nhỏ
        - Chi lạnh, vã mồ hôi
        - Lừ đừ, vật vã
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: LABORATORY ==========
    st.markdown("### 🧪 Xét nghiệm")
    
    col1, col2 = st.columns(2)
    
    with col1:
        wbc = st.number_input(
            "**Bạch cầu (x10³/µL):**",
            min_value=0.0,
            max_value=50.0,
            value=5.0,
            step=0.1,
            help="Bình thường: 4-10"
        )
        
        platelet = st.number_input(
            "**Tiểu cầu (x10³/µL):**",
            min_value=0.0,
            max_value=500.0,
            value=150.0,
            step=1.0,
            help="Bình thường: 150-400"
        )
    
    with col2:
        hct = st.number_input(
            "**Hematocrit (%):**",
            min_value=20.0,
            max_value=60.0,
            value=40.0,
            step=0.1,
            help="Bình thường: 35-45%"
        )
        
        ns1_antigen = st.selectbox(
            "**NS1 Antigen:**",
            ["Chưa làm", "Dương tính", "Âm tính"]
        )
    
    # Assessment based on lab values
    if platelet < 100:
        st.warning(f"⚠️ Giảm tiểu cầu: {platelet:.0f} x10³/µL - Cần theo dõi sát")
    if hct > 45:
        st.warning(f"⚠️ Tăng Hct: {hct:.1f}% - Có thể cô đặc máu, cần truyền dịch")
    if wbc < 3:
        st.info(f"ℹ️ Giảm bạch cầu: {wbc:.1f} x10³/µL - Điển hình của sốt xuất huyết")
    
    st.markdown("---")
    
    # ========== SECTION 5: TREATMENT PROTOCOL ==========
    st.markdown("### 💊 Phác đồ điều trị")
    
    classification = st.radio(
        "**Phân loại:**",
        ["Sốt xuất huyết Dengue", "Có dấu hiệu cảnh báo", "Sốt xuất huyết Dengue nặng"],
        key="dengue_classification"
    )
    
    st.markdown("---")
    
    if "Sốt xuất huyết Dengue" in classification and "Có dấu hiệu" not in classification:
        render_dengue_fever()
    elif "Có dấu hiệu" in classification:
        render_dengue_with_warning()
    else:
        render_severe_dengue()
    
    st.markdown("---")
    
    # ========== SECTION 6: FLUID MANAGEMENT ==========
    st.markdown("### 💧 Quản lý dịch truyền")
    
    st.warning("""
    **⚠️ QUAN TRỌNG: Quản lý dịch là then chốt trong điều trị sốt xuất huyết**
    
    **Nguyên tắc:**
    - Bù dịch đủ nhưng không quá tải
    - Theo dõi Hct, tiểu cầu
    - Điều chỉnh theo đáp ứng
    
    **Dịch truyền:**
    - **Crystalloid:** NaCl 0.9%, Ringer Lactate
    - **Colloid:** Dextran, Gelatin (nếu sốc)
    - **Máu:** Nếu mất máu nhiều
    
    **Theo dõi:**
    - Dấu hiệu sống mỗi 2-4 giờ
    - Hct mỗi 6-12 giờ
    - Lượng nước tiểu
    - Dấu hiệu quá tải dịch
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Theo dõi tại nhà (DF):**
        - Nhiệt độ mỗi 4-6 giờ
        - Lượng nước uống
        - Lượng nước tiểu
        - Dấu hiệu cảnh báo
        - Tái khám nếu có dấu hiệu cảnh báo
        
        **Theo dõi tại viện:**
        - Dấu hiệu sống mỗi 2-4 giờ
        - Hct, tiểu cầu mỗi 6-12 giờ
        - Lượng nước tiểu
        - Dấu hiệu sốc
        """)
    
    with col2:
        st.markdown("""
        **Dấu hiệu cần nhập viện:**
        - Có dấu hiệu cảnh báo
        - Giảm tiểu cầu <100
        - Tăng Hct >20% so với bình thường
        - Không uống được
        - Nôn nhiều
        
        **Dấu hiệu cần ICU:**
        - Sốc
        - Chảy máu nặng
        - Suy tạng
        - Cần thở máy
        """)
    
    st.markdown("---")
    
    # ========== SECTION 8: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.error("""
    **Biến chứng có thể gặp:**
    
    **1. Sốc do sốt xuất huyết Dengue (DSS):**
    - Thường ngày 3-7
    - Hạ huyết áp
    - Tăng Hct
    - Giảm tiểu cầu
    - Cần truyền dịch tích cực
    
    **2. Chảy máu:**
    - Chảy máu niêm mạc
    - Xuất huyết tiêu hóa
    - Xuất huyết não (hiếm)
    - Cần truyền máu, tiểu cầu
    
    **3. Suy tạng:**
    - Suy gan
    - Suy thận
    - Suy tim
    - Rối loạn chức năng đa cơ quan
    
    **4. Hội chứng sốc Dengue:**
    - Sốc kéo dài
    - Cần hồi sức tích cực
    
    **Xử trí:**
    - Điều trị theo triệu chứng
    - Hồi sức tích cực
    - Theo dõi sát
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    **Khuyến cáo phòng ngừa:**
    
    **1. Diệt muỗi:**
    - Phun thuốc diệt muỗi
    - Diệt lăng quăng (bọ gậy)
    - Loại bỏ nơi đẻ trứng
    
    **2. Tránh muỗi đốt:**
    - Mặc quần áo dài
    - Dùng kem chống muỗi
    - Ngủ màn
    - Dùng lưới chống muỗi
    
    **3. Vệ sinh môi trường:**
    - Đậy kín dụng cụ chứa nước
    - Thay nước thường xuyên
    - Loại bỏ vật chứa nước không cần thiết
    
    **4. Vaccine:**
    - Dengvaxia (cho người đã từng mắc)
    - Qdenga (mới, cho người chưa mắc)
    """)
    
    st.markdown("---")
    
    # ========== REFERENCES ==========
    render_references_section(get_references("dengue_fever"))


def render_dengue_fever():
    """Dengue Fever Protocol"""
    st.success("## ✅ SỐT XUẤT HUYẾT DENGUE (DF)")
    
    st.markdown("""
    **Điều trị ngoại trú:**
    
    **1. Hạ sốt:**
    - Paracetamol: 10-15 mg/kg/lần, mỗi 4-6 giờ
    - Tối đa: 4g/ngày (người lớn)
    - **KHÔNG dùng:** Aspirin, NSAID (tăng nguy cơ chảy máu)
    
    **2. Bù dịch:**
    - Uống nhiều nước: Oresol, nước lọc
    - Lượng: 2-3 L/ngày (người lớn)
    - Theo dõi lượng nước tiểu
    
    **3. Nghỉ ngơi:**
    - Nghỉ tại giường
    - Tránh vận động mạnh
    
    **4. Theo dõi:**
    - Nhiệt độ mỗi 4-6 giờ
    - Dấu hiệu cảnh báo
    - Tái khám nếu có dấu hiệu cảnh báo
    
    **Xuất viện khi:**
    - Hết sốt 24-48 giờ
    - Tổng trạng tốt
    - Không có dấu hiệu cảnh báo
    - Hct ổn định
    """)


def render_dengue_with_warning():
    """Dengue with Warning Signs Protocol"""
    st.error("## 🚨 SỐT XUẤT HUYẾT DENGUE CÓ DẤU HIỆU CẢNH BÁO")
    
    st.markdown("""
    **Nhập viện ngay:**
    
    **1. Truyền dịch:**
    - NaCl 0.9% hoặc Ringer Lactate
    - Liều: 10-20 mL/kg trong 1-2 giờ đầu
    - Sau đó: 5-10 mL/kg/giờ
    - Điều chỉnh theo đáp ứng
    
    **2. Theo dõi sát:**
    - Dấu hiệu sống mỗi 2-4 giờ
    - Hct, tiểu cầu mỗi 6-12 giờ
    - Lượng nước tiểu
    - Dấu hiệu sốc
    
    **3. Điều trị hỗ trợ:**
    - Hạ sốt: Paracetamol
    - Chống nôn nếu cần
    - Điều chỉnh điện giải
    
    **4. Chuẩn bị:**
    - Sẵn sàng xử trí sốc
    - Có thể cần truyền máu
    - Có thể cần ICU
    
    **Tiêu chuẩn xuất viện:**
    - Hết sốt 24-48 giờ
    - Không có dấu hiệu cảnh báo
    - Hct ổn định
    - Tiểu cầu tăng
    - Tổng trạng tốt
    """)


def render_severe_dengue():
    """Severe Dengue Protocol"""
    st.error("## 🚨🚨 SỐT XUẤT HUYẾT DENGUE NẶNG - ICU")
    
    st.markdown("""
    **Xử trí khẩn cấp:**
    
    **1. Sốc do sốt xuất huyết Dengue (DSS):**
    - **Giai đoạn sốc:**
      - Truyền dịch: 20 mL/kg trong 15 phút
      - Lặp lại nếu cần
      - Colloid nếu không đáp ứng
    
    - **Giai đoạn sốc nặng:**
      - Colloid: Dextran 40, Gelatin
      - Liều: 10-20 mL/kg
      - Có thể cần vasopressor
    
    **2. Chảy máu nặng:**
    - Truyền máu: 10-20 mL/kg
    - Truyền tiểu cầu nếu <50
    - Truyền FFP nếu cần
    - Điều chỉnh đông máu
    
    **3. Hồi sức:**
    - Đường thở: Đảm bảo thông thoáng
    - Hô hấp: Oxy, có thể thở máy
    - Tuần hoàn: Truyền dịch, vasopressor
    
    **4. ICU Monitoring:**
    - Continuous monitoring
    - Hct, tiểu cầu mỗi 4-6 giờ
    - Theo dõi chức năng đa cơ quan
    
    **Tiên lượng:**
    - Cần điều trị tích cực
    - Thời gian nằm viện: 5-10 ngày
    - Tỷ lệ tử vong: 1-5% nếu điều trị đúng
    """)

