"""
Stevens-Johnson Syndrome (SJS) / Toxic Epidermal Necrolysis (TEN) Protocol
Severe cutaneous adverse reaction
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Stevens-Johnson Syndrome / Toxic Epidermal Necrolysis Protocol"""
    st.subheader("🩹 Hội chứng Stevens-Johnson / Hoại tử biểu bì nhiễm độc (SJS/TEN)")
    st.caption("Severe Cutaneous Adverse Reaction - Life-threatening condition")
    
    st.error("""
    **⚠️ SJS/TEN = CẤP CỨU Y TẾ - TỶ LỆ TỬ VONG 5-30%**
    
    **Định nghĩa:**
    - **SJS:** Tổn thương da <10% diện tích cơ thể
    - **SJS/TEN Overlap:** 10-30% diện tích
    - **TEN:** >30% diện tích
    - Phản ứng dị ứng nặng, đe dọa tính mạng
    
    **Nguyên nhân:**
    - **Thuốc (90%):** Allopurinol, Sulfonamides, NSAIDs, Anticonvulsants, Antibiotics
    - **Nhiễm trùng:** Mycoplasma, HSV
    - **Vaccine:** Hiếm
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn chẩn đoán")
    
    st.warning("""
    **Chẩn đoán SJS/TEN khi có:**
    
    1. **Tổn thương da:**
       - Ban đỏ, mụn nước
       - Bong tróc da (Nikolsky sign dương tính)
       - Tổn thương niêm mạc (mắt, miệng, sinh dục)
    
    2. **Phân loại theo diện tích:**
       - **SJS:** <10% diện tích cơ thể
       - **SJS/TEN Overlap:** 10-30%
       - **TEN:** >30%
    
    3. **Tiền sử:**
       - Dùng thuốc mới (1-3 tuần trước)
       - Hoặc nhiễm trùng gần đây
    
    **SCORTEN Score (Tiên lượng):**
    - Tuổi >40
    - Nhiễm trùng huyết
    - Diện tích bong tróc >10%
    - BUN >28 mg/dL
    - Glucose >252 mg/dL
    - Bicarbonate <20 mEq/L
    - Nhịp tim >120/phút
    
    **Tỷ lệ tử vong:** 0.8% (0 điểm) → 90% (≥5 điểm)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL FEATURES ==========
    st.markdown("### 🔍 Triệu chứng lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Triệu chứng sớm (1-3 ngày):**
        - Sốt
        - Mệt mỏi
        - Đau họng
        - Đau mắt
        - Ban đỏ không đặc hiệu
        
        **Triệu chứng da:**
        - Ban đỏ, mụn nước
        - Bong tróc da
        - Nikolsky sign (+)
        - Tổn thương niêm mạc
        """)
    
    with col2:
        st.markdown("""
        **Triệu chứng nặng:**
        - Bong tróc da diện rộng
        - Tổn thương niêm mạc nặng
        - Nhiễm trùng
        - Mất dịch, rối loạn điện giải
        - Suy đa tạng
        
        **Biến chứng:**
        - Nhiễm trùng huyết
        - Suy thận cấp
        - Suy hô hấp
        - Tử vong (5-30%)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: IMMEDIATE MANAGEMENT ==========
    st.markdown("### 🚨 Xử trí ngay lập tức")
    
    st.error("""
    **1. Ngừng ngay thuốc nghi ngờ:**
    - Ngừng tất cả thuốc không cần thiết
    - Đặc biệt: Thuốc mới dùng trong 1-3 tuần
    
    **2. Chuyển đến trung tâm chuyên khoa:**
    - Burn unit hoặc ICU
    - Có đội ngũ đa chuyên khoa
    
    **3. ABC:**
    - Đảm bảo đường thở (có thể cần đặt nội khí quản)
    - Oxygen nếu cần
    - 2 đường truyền tĩnh mạch lớn
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.markdown("#### **1. Hỗ trợ (Supportive Care) - QUAN TRỌNG NHẤT**")
    
    st.success("""
    **A. Chăm sóc vết thương:**
    - Rửa sạch bằng nước muối sinh lý
    - Băng vết thương (như bỏng)
    - Tránh bóc da
    - Chăm sóc mắt: Rửa mắt, tra thuốc mỡ
    
    **B. Bù dịch:**
    - Truyền dịch tích cực (như bỏng)
    - Công thức Parkland: 4 mL/kg/% diện tích bong tróc
    - Theo dõi cân bằng dịch
    
    **C. Dinh dưỡng:**
    - Nuôi dưỡng qua ống thông mũi-dạ dày (nếu tổn thương miệng)
    - Hoặc TPN nếu cần
    
    **D. Phòng ngừa nhiễm trùng:**
    - Môi trường vô trùng
    - Kháng sinh dự phòng: Có thể (nhưng còn tranh cãi)
    """)
    
    st.markdown("---")
    
    st.markdown("#### **2. Điều trị đặc hiệu (Còn tranh cãi)**")
    
    st.warning("""
    **Cyclosporine:**
    - **Liều:** 3-5 mg/kg/ngày PO/IV
    - **Thời gian:** 2-3 tuần
    - **Lưu ý:** Có thể giảm tỷ lệ tử vong
    
    **IVIG (Intravenous Immunoglobulin):**
    - **Liều:** 1-2 g/kg (tổng liều, truyền trong 3-5 ngày)
    - **Lưu ý:** Hiệu quả còn tranh cãi
    
    **Corticosteroids:**
    - **Lưu ý:** Thường KHÔNG khuyến cáo (tăng nguy cơ nhiễm trùng)
    - Có thể dùng liều cao, ngắn hạn trong một số trường hợp
    
    **TNF-α inhibitors (Infliximab, Etanercept):**
    - Đang nghiên cứu
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Cần theo dõi:**
    - **Dấu hiệu sinh tồn:** Liên tục
    - **Diện tích bong tróc:** Mỗi ngày
    - **Lượng nước tiểu:** Mỗi giờ (cần >0.5-1 mL/kg/h)
    - **CBC:** Mỗi ngày
    - **Chức năng thận, gan:** Mỗi ngày
    - **Điện giải:** Mỗi 12 giờ
    - **Cấy máu, dịch:** Nếu nghi ngờ nhiễm trùng
    - **Mắt:** Khám mắt hàng ngày
    
    **Dấu hiệu cải thiện:**
    - Ngừng bong tróc da
    - Lành vết thương
    - Cải thiện niêm mạc
    - Ổn định dấu hiệu sinh tồn
    
    **Dấu hiệu xấu đi:**
    - Bong tróc tiếp tục
    - Nhiễm trùng huyết
    - Suy đa tạng
    - Tăng SCORTEN score
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.info("""
    **Biến chứng cấp:**
    - Nhiễm trùng huyết
    - Suy thận cấp
    - Suy hô hấp
    - Mất dịch, rối loạn điện giải
    - Tử vong (5-30%)
    
    **Biến chứng mạn:**
    - Sẹo da
    - Tổn thương mắt (khô mắt, dính mi, mù)
    - Hẹp thực quản
    - Hẹp niệu đạo, âm đạo
    - Rối loạn sắc tố da
    
    **Phòng ngừa:**
    - Tránh thuốc gây bệnh
    - Tư vấn bệnh nhân
    - Theo dõi mắt lâu dài
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: REFERENCES ==========
    references = get_references("Stevens-Johnson Syndrome")
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
        1. **Bastuji-Garin S, et al. SCORTEN: a severity-of-illness score for toxic epidermal necrolysis.** J Invest Dermatol. 2000
        2. **Schneider JA, Cohen PR. Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis: A Concise Review with a Comprehensive Summary of Therapeutic Interventions Emphasizing Supportive Measures.** Adv Ther. 2017
        3. **UpToDate:** Stevens-Johnson Syndrome and Toxic Epidermal Necrolysis - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

