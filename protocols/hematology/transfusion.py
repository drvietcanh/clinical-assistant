"""
Transfusion Protocols
AABB 2016, ASH 2018
Evidence-based blood product transfusion guidelines
"""

import streamlit as st


def render():
    """Transfusion Protocols"""
    st.subheader("🩸 Truyền Máu (Transfusion)")
    st.caption("AABB 2016, ASH 2018 - Blood product transfusion guidelines")
    
    st.info("""
    **Truyền máu và chế phẩm máu:**
    - Cần tuân thủ strict indications
    - Restrictive transfusion strategy (ưu tiên)
    - Mục tiêu: An toàn, hiệu quả, tránh lãng phí
    
    **Nguyên tắc:**
    - Chỉ truyền khi thực sự cần thiết
    - Restrictive thresholds (Hb <7 g/dL)
    - Theo dõi sát phản ứng truyền máu
    """)
    
    st.markdown("---")
    
    st.markdown("### 🩸 Chọn Loại Chế Phẩm Máu")
    
    product_type = st.radio(
        "**Loại chế phẩm máu:**",
        [
            "Hồng cầu (RBC)",
            "Tiểu cầu (Platelets)",
            "Huyết tương tươi đông lạnh (FFP)",
            "Cryoprecipitate",
            "Massive Transfusion Protocol"
        ],
        key="blood_product"
    )
    
    st.markdown("---")
    
    if "Hồng cầu" in product_type or "RBC" in product_type:
        render_rbc_protocol()
    elif "Tiểu cầu" in product_type or "Platelets" in product_type:
        render_platelet_protocol()
    elif "Huyết tương" in product_type or "FFP" in product_type:
        render_ffp_protocol()
    elif "Cryoprecipitate" in product_type:
        render_cryoprecipitate_protocol()
    else:
        render_massive_transfusion()
    
    st.markdown("---")
    
    st.markdown("### 📊 Restrictive vs Liberal Transfusion")
    
    st.warning("""
    **Restrictive Strategy (Ưu tiên):**
    - **RBC:** Hb <7 g/dL (hoặc <8 g/dL nếu có bệnh tim mạch)
    - **Mục tiêu:** Hb 7-9 g/dL
    - **Lợi ích:** Giảm nguy cơ nhiễm trùng, giảm chi phí
    - **Áp dụng:** Hầu hết bệnh nhân
    
    **Liberal Strategy:**
    - **RBC:** Hb <10 g/dL
    - **Mục tiêu:** Hb 10-12 g/dL
    - **Chỉ định:** 
      - Bệnh tim mạch không ổn định
      - Chảy máu cấp tính
      - Thiếu máu nặng có triệu chứng
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Phản Ứng Truyền Máu")
    
    st.error("""
    **Phản ứng truyền máu cấp tính:**
    
    **1. Hemolytic Reaction (Phản ứng tan máu):**
    - Triệu chứng: Sốt, ớn lạnh, đau lưng, nước tiểu đỏ
    - Xử trí: Ngừng truyền ngay, hỗ trợ hô hấp, truyền dịch
    - Tỷ lệ tử vong: 1-10%
    
    **2. Febrile Non-Hemolytic (Sốt không tan máu):**
    - Triệu chứng: Sốt, ớn lạnh
    - Xử trí: Ngừng truyền, hạ sốt
    - Thường nhẹ
    
    **3. Allergic Reaction (Phản ứng dị ứng):**
    - Triệu chứng: Ngứa, phát ban, phù
    - Xử trí: Antihistamine, ngừng truyền nếu nặng
    
    **4. TRALI (Transfusion-Related Acute Lung Injury):**
    - Triệu chứng: Khó thở, phù phổi
    - Xử trí: Hỗ trợ hô hấp, ICU
    
    **5. TACO (Transfusion-Associated Circulatory Overload):**
    - Triệu chứng: Khó thở, phù, tăng huyết áp
    - Xử trí: Lợi tiểu, giảm tốc độ truyền
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Truyền Máu")
    
    checklist_items = [
        "✅ Xác định chỉ định truyền máu",
        "✅ Kiểm tra nhóm máu, crossmatch",
        "✅ Kiểm tra sản phẩm máu (màu sắc, hạn sử dụng)",
        "✅ Xác nhận bệnh nhân (2 người kiểm tra)",
        "✅ Bắt đầu truyền chậm (15 phút đầu)",
        "✅ Theo dõi dấu hiệu sống mỗi 15 phút",
        "✅ Theo dõi phản ứng truyền máu",
        "✅ Hoàn thành trong 4 giờ",
        "✅ Ghi chép đầy đủ"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Cẩn thận với TACO (nguy cơ cao)
        - Truyền chậm hơn
        - Theo dõi sát huyết động
        
        **Bệnh tim mạch:**
        - Có thể cần liberal threshold (Hb <8-9)
        - Truyền chậm
        - Theo dõi huyết động sát
        """)
    
    with col2:
        st.markdown("""
        **Trẻ em:**
        - Liều tính theo kg
        - Truyền chậm
        - Theo dõi sát
        
        **Có thai:**
        - Rh-negative cần RhIg nếu Rh-positive
        - Truyền chậm
        - Monitor thai nhi
        """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **AABB 2016 Guidelines**
       - American Association of Blood Banks
    
    2. **ASH 2018 Guidelines**
       - American Society of Hematology
    
    3. **UpToDate:** Transfusion therapy
       - Last updated: 2024
    
    4. **Medscape:** Blood Transfusion
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_rbc_protocol():
    """RBC transfusion protocol"""
    st.success("## 🩸 Truyền Hồng Cầu (RBC)")
    
    st.markdown("""
    **Chỉ định:**
    
    **1. Restrictive Threshold (Ưu tiên):**
    - Hb <7 g/dL (ổn định)
    - Hb <8 g/dL (có bệnh tim mạch)
    - Mục tiêu: Hb 7-9 g/dL
    
    **2. Liberal Threshold:**
    - Hb <10 g/dL (chỉ khi cần)
    - Bệnh tim mạch không ổn định
    - Chảy máu cấp tính
    
    **3. Chỉ định khác:**
    - Thiếu máu có triệu chứng (khó thở, mệt mỏi)
    - Chảy máu cấp tính
    - Phẫu thuật lớn
    
    **Liều:**
    - **1 đơn vị:** Tăng Hb ~1 g/dL (người lớn)
    - **Trẻ em:** 10-15 mL/kg
    
    **Tốc độ:**
    - Bắt đầu: 15 phút đầu chậm
    - Sau đó: 2-4 giờ/đơn vị
    - Hoàn thành trong 4 giờ
    """)


def render_platelet_protocol():
    """Platelet transfusion protocol"""
    st.warning("## 🩸 Truyền Tiểu Cầu (Platelets)")
    
    st.markdown("""
    **Chỉ định:**
    
    **1. Prophylactic (Dự phòng):**
    - Plt <10,000/μL (không chảy máu)
    - Plt <20,000/μL (nếu có nguy cơ chảy máu)
    
    **2. Therapeutic (Điều trị):**
    - Chảy máu + Plt <50,000/μL
    - Phẫu thuật lớn + Plt <50,000/μL
    - Chảy máu nội sọ + Plt <100,000/μL
    
    **3. Chống chỉ định:**
    - TTP, HUS (trừ khi chảy máu đe dọa tính mạng)
    - ITP (trừ khi chảy máu nặng)
    
    **Liều:**
    - **1 đơn vị apheresis:** Tăng Plt ~30,000-50,000/μL
    - **1 pool (6 đơn vị):** Tương đương 1 đơn vị apheresis
    
    **Tốc độ:**
    - Truyền nhanh (15-30 phút)
    - Hoàn thành trong 4 giờ
    """)


def render_ffp_protocol():
    """FFP transfusion protocol"""
    st.info("## 🩸 Truyền Huyết Tương Tươi Đông Lạnh (FFP)")
    
    st.markdown("""
    **Chỉ định:**
    
    **1. Chảy máu:**
    - Chảy máu + PT/PTT kéo dài
    - Chảy máu + thiếu hụt yếu tố đông máu
    
    **2. Warfarin reversal:**
    - Chảy máu nặng
    - Không có PCC
    - Liều: 10-15 mL/kg
    
    **3. DIC:**
    - Chảy máu + DIC
    - Kết hợp với cryoprecipitate
    
    **4. Chống chỉ định:**
    - Không dùng để bù thể tích
    - Không dùng để tăng albumin
    
    **Liều:**
    - **10-15 mL/kg:** Điều chỉnh PT/PTT
    - **1 đơn vị:** ~200-250 mL
    
    **Tốc độ:**
    - Truyền nhanh nếu chảy máu
    - Hoàn thành trong 4 giờ
    """)


def render_cryoprecipitate_protocol():
    """Cryoprecipitate transfusion protocol"""
    st.info("## 🩸 Truyền Cryoprecipitate")
    
    st.markdown("""
    **Chỉ định:**
    
    **1. Fibrinogen thấp:**
    - Fibrinogen <100 mg/dL + chảy máu
    - Fibrinogen <150 mg/dL + phẫu thuật lớn
    
    **2. DIC:**
    - DIC + fibrinogen thấp
    
    **3. Hemophilia A:**
    - Khi không có factor VIII concentrate
    
    **4. Von Willebrand Disease:**
    - Khi không có vWF concentrate
    
    **Liều:**
    - **1 pool (10 đơn vị):** Tăng fibrinogen ~50-100 mg/dL
    - **Liều thông thường:** 1-2 pools
    
    **Tốc độ:**
    - Truyền nhanh
    - Hoàn thành trong 4 giờ
    """)


def render_massive_transfusion():
    """Massive transfusion protocol"""
    st.error("## 🔴 Massive Transfusion Protocol (MTP)")
    
    st.markdown("""
    **Định nghĩa:**
    - Truyền ≥10 đơn vị RBC trong 24 giờ
    - Hoặc ≥4 đơn vị RBC trong 1 giờ
    - Hoặc mất máu >50% thể tích máu
    
    **Tỷ lệ truyền (1:1:1):**
    - **1 đơn vị RBC**
    - **1 đơn vị FFP**
    - **1 đơn vị Platelets**
    
    **Mục tiêu:**
    - Duy trì Hb >7-8 g/dL
    - Duy trì Plt >50,000/μL
    - Duy trì PT/PTT gần bình thường
    - Duy trì fibrinogen >150 mg/dL
    
    **Theo dõi:**
    - CBC, PT/PTT, fibrinogen mỗi 1-2 giờ
    - Ionized calcium (nguy cơ hạ canxi)
    - pH, lactate (nguy cơ toan chuyển hóa)
    - Nhiệt độ (nguy cơ hạ thân nhiệt)
    
    **Biến chứng:**
    - Hạ canxi (citrate toxicity)
    - Toan chuyển hóa
    - Hạ thân nhiệt
    - Rối loạn đông máu
    """)

