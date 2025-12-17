"""
Scabies (Ghẻ) Protocol
Parasitic skin infestation
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Scabies (Ghẻ) Protocol"""
    st.subheader("🩹 Ghẻ (Scabies)")
    st.caption("Parasitic skin infestation - Common in Vietnam")
    
    st.info("""
    **Định nghĩa:**
    - Nhiễm ký sinh trùng Sarcoptes scabiei var. hominis
    - Rất dễ lây qua tiếp xúc trực tiếp
    - Phổ biến ở Việt Nam, đặc biệt vùng đông dân cư
    
    **Cơ chế:**
    - Cái ghẻ đào hang trong da, đẻ trứng
    - Gây ngứa do phản ứng dị ứng với phân và trứng
    - Thời gian ủ bệnh: 2-6 tuần (lần đầu), 1-4 ngày (tái nhiễm)
    
    **Yếu tố nguy cơ:**
    - Tiếp xúc gần gũi
    - Điều kiện vệ sinh kém
    - Sống tập thể (ký túc xá, nhà tù)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn chẩn đoán")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        1. **Ngứa:** Nặng hơn về đêm, đặc trưng
        2. **Tổn thương da:**
           - Đường hang (burrow): Đường cong, dài 5-15 mm
           - Mụn nước, sẩn
           - Vị trí: Kẽ ngón tay, cổ tay, khuỷu tay, nách, bẹn, bộ phận sinh dục
        
        3. **Dấu hiệu:**
           - Ngứa ở nhiều người trong gia đình
           - Tổn thương đối xứng
           - Vết gãi, nhiễm trùng thứ phát
        
        **Chẩn đoán xác định:**
        - Tìm thấy cái ghẻ hoặc trứng dưới kính hiển vi
        - Hoặc chẩn đoán lâm sàng điển hình
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL TYPES ==========
    st.markdown("### 🔍 Phân loại")
    
    scabies_type = st.radio(
        "**Loại ghẻ:**",
        ["Ghẻ thường", "Ghẻ vảy (Crusted/Norwegian)"],
        key="scabies_type"
    )
    
    if scabies_type == "Ghẻ vảy (Crusted/Norwegian)":
        st.error("""
        **Ghẻ vảy (Crusted/Norwegian Scabies):**
        - Rất dễ lây, hàng triệu cái ghẻ
        - Tổn thương dày, vảy nhiều
        - Thường gặp ở: Suy giảm miễn dịch, người già, bệnh thần kinh
        - Cần điều trị tích cực hơn
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.success("""
    **Nguyên tắc:**
    1. Điều trị đồng thời tất cả người tiếp xúc
    2. Điều trị đúng cách, đủ liều
    3. Vệ sinh môi trường
    4. Tái khám sau 1-2 tuần
    
    **1. Permethrin 5% (Thuốc đầu tay):**
    - **Cách dùng:**
      - Tắm sạch, lau khô
      - Bôi từ cổ xuống chân, toàn thân
      - Để 8-12 giờ (qua đêm)
      - Tắm lại sáng hôm sau
    - **Lặp lại:** Sau 1 tuần (nếu cần)
    - **An toàn:** Trẻ em >2 tháng, phụ nữ có thai
    
    **2. Ivermectin (Đường uống):**
    - **Liều:** 200 mcg/kg, uống 1 lần
    - **Lặp lại:** Sau 1-2 tuần
    - **Chỉ định:** Ghẻ vảy, không đáp ứng permethrin
    - **Lưu ý:** Không dùng cho trẻ <15 kg, phụ nữ có thai/cho con bú
    
    **3. Benzyl Benzoate 25%:**
    - **Cách dùng:** Bôi toàn thân, để 24 giờ
    - **Lặp lại:** Sau 3 ngày
    - **Lưu ý:** Có thể gây kích ứng
    
    **4. Lindane 1%:**
    - **Cách dùng:** Bôi toàn thân, để 8-12 giờ
    - **Lưu ý:** Độc tính thần kinh, ít dùng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT PROTOCOL ==========
    st.markdown("### 📋 Phác đồ điều trị")
    
    st.markdown("""
    **Ngày 1:**
    1. Tắm sạch, lau khô
    2. Bôi thuốc từ cổ xuống chân (toàn thân)
    3. Đặc biệt: Kẽ ngón tay, cổ tay, khuỷu tay, nách, bẹn, bộ phận sinh dục
    4. Để 8-12 giờ (qua đêm)
    5. Thay quần áo, ga gối
    
    **Ngày 2:**
    1. Tắm lại, thay quần áo sạch
    2. Giặt quần áo, ga gối ở nhiệt độ >60°C
    
    **Ngày 8-14:**
    1. Lặp lại điều trị (nếu cần)
    2. Tái khám đánh giá
    
    **Điều trị người tiếp xúc:**
    - Tất cả người trong gia đình
    - Bạn tình, người tiếp xúc gần
    - Điều trị đồng thời
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: ENVIRONMENTAL MEASURES ==========
    st.markdown("### 🏠 Vệ sinh môi trường")
    
    st.warning("""
    **Vệ sinh quần áo, ga gối:**
    - Giặt ở nhiệt độ >60°C
    - Hoặc phơi nắng 3-5 ngày
    - Hoặc đóng túi kín 1 tuần
    
    **Vệ sinh nhà cửa:**
    - Hút bụi sàn, ghế, giường
    - Lau dọn sạch sẽ
    - Không cần phun thuốc diệt côn trùng
    
    **Lưu ý:**
    - Cái ghẻ sống ngoài da <2-3 ngày
    - Vệ sinh môi trường quan trọng nhưng không quá căng thẳng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: SYMPTOM MANAGEMENT ==========
    st.markdown("### 🧴 Điều trị triệu chứng")
    
    st.markdown("""
    **Ngứa sau điều trị:**
    - Có thể kéo dài 2-4 tuần sau khi hết ghẻ
    - Do phản ứng dị ứng với xác cái ghẻ
    
    **Điều trị:**
    - **Antihistamines:**
      - Cetirizine 10 mg/ngày
      - Loratadine 10 mg/ngày
      - Có thể dùng 2-4 tuần
    
    - **Corticosteroid tại chỗ:**
      - Hydrocortisone 1%
      - Bôi vùng ngứa
    
    - **Dưỡng ẩm:**
      - Bôi kem dưỡng ẩm
      - Giảm khô da, ngứa
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Theo dõi sau điều trị:**
    - **1 tuần:** Đánh giá đáp ứng
    - **2 tuần:** Tái khám, đánh giá lại
    - **4 tuần:** Đánh giá cuối cùng
    
    **Dấu hiệu thành công:**
    - Giảm ngứa sau 2-3 ngày
    - Tổn thương lành dần
    - Không có tổn thương mới
    
    **Dấu hiệu thất bại:**
    - Vẫn ngứa nhiều sau 1 tuần
    - Tổn thương mới xuất hiện
    - Tìm thấy cái ghẻ mới
    
    **Xử trí thất bại:**
    - Kiểm tra lại cách dùng thuốc
    - Điều trị lại với phác đồ khác
    - Điều trị đồng thời tất cả người tiếp xúc
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.info("""
    **Biến chứng:**
    - **Nhiễm trùng thứ phát:** Do gãi
      - Impetigo, Cellulitis
      - Điều trị: Kháng sinh (Cephalexin, Amoxicillin-clavulanate)
    
    - **Eczema hóa:** Da dày, lichen hóa
      - Điều trị: Corticosteroid tại chỗ, dưỡng ẩm
    
    - **Nhiễm trùng huyết:** Hiếm, nếu không điều trị nhiễm trùng
    
    **Phòng ngừa:**
    - Điều trị sớm
    - Không gãi
    - Vệ sinh sạch sẽ
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: REFERENCES ==========
    references = get_references("Scabies")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        1. **Currie BJ, McCarthy JS. Permethrin and ivermectin for scabies.** N Engl J Med. 2010
        2. **Strong M, Johnstone P. Interventions for treating scabies.** Cochrane Database Syst Rev. 2007
        3. **UpToDate:** Scabies - Last updated 2024
        4. **Hướng dẫn chẩn đoán và điều trị bệnh da liễu - Bộ Y tế Việt Nam**
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

