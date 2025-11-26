"""
Delirium Management Protocol
ICU Delirium Guidelines, NICE
Management of delirium in ICU and hospitalized patients
"""

import streamlit as st


def render():
    """Delirium Management Protocol"""
    st.subheader("🧠 Quản Lý Delirium (Delirium Management)")
    st.caption("ICU Delirium Guidelines, NICE - Delirium assessment and management")
    
    st.error("""
    **⚠️ DELIRIUM = TÌNH TRẠNG CẤP TÍNH**
    
    **Định nghĩa:**
    - Rối loạn ý thức cấp tính
    - Khởi phát nhanh (giờ đến ngày)
    - Dao động trong ngày
    - Giảm chú ý
    - Tư duy rối loạn
    
    **Tỷ lệ:**
    - ICU: 20-80%
    - Bệnh nhân lớn tuổi: 30-50%
    - Sau phẫu thuật: 15-50%
    
    **Hậu quả:**
    - Tăng thời gian nằm viện
    - Tăng tỷ lệ tử vong
    - Tăng chi phí
    - Suy giảm nhận thức lâu dài
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 CAM-ICU Assessment (Confusion Assessment Method for ICU)")
    
    st.info("""
    **CAM-ICU:** Tiêu chuẩn vàng để chẩn đoán delirium trong ICU
    
    **4 Tiêu chí (Tất cả phải có):**
    1. **Khởi phát cấp tính + Dao động:** Thay đổi từ baseline, dao động trong ngày
    2. **Giảm chú ý:** Không thể tập trung, dễ phân tâm
    3. **Tư duy rối loạn:** Lú lẫn, không logic, ảo giác
    4. **Thay đổi mức độ ý thức:** Không tỉnh táo hoàn toàn
    
    **Kết quả:**
    - **Dương tính:** Có đủ 4 tiêu chí → Chẩn đoán DELIRIUM
    - **Âm tính:** Thiếu ≥1 tiêu chí → Không có delirium
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Phân Loại Delirium")
    
    delirium_type = st.radio(
        "**Loại delirium:**",
        ["Hyperactive (Kích động)", "Hypoactive (Ức chế)", "Mixed (Hỗn hợp)"],
        key="delirium_type"
    )
    
    st.markdown("---")
    
    if "Hyperactive" in delirium_type:
        render_hyperactive_delirium()
    elif "Hypoactive" in delirium_type:
        render_hypoactive_delirium()
    else:
        render_mixed_delirium()
    
    st.markdown("---")
    
    st.markdown("### 🔍 Tìm Nguyên Nhân (PIMED)")
    
    st.warning("""
    **PIMED - Các Nguyên Nhân Thường Gặp:**
    
    **P - Pain (Đau):**
    - Đau không được kiểm soát
    - Đánh giá đau thường xuyên
    
    **I - Infection (Nhiễm trùng):**
    - Nhiễm trùng huyết
    - Nhiễm trùng đường tiết niệu
    - Viêm phổi
    
    **M - Metabolic (Rối loạn chuyển hóa):**
    - Hạ natri máu
    - Tăng/hạ đường huyết
    - Suy thận, suy gan
    - Thiếu oxy
    
    **E - Electrolyte (Điện giải):**
    - Hạ natri, hạ canxi, hạ magie
    - Rối loạn điện giải khác
    
    **D - Drugs (Thuốc):**
    - Benzodiazepine
    - Opioid
    - Anticholinergic
    - Corticosteroid
    - Nhiều thuốc cùng lúc
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều Trị")
    
    treatment_approach = st.radio(
        "**Phương Pháp Điều Trị:**",
        [
            "Non-Pharmacologic (Không dùng thuốc) - Ưu Tiên",
            "Pharmacologic (Dùng thuốc) - Khi cần"
        ],
        key="delirium_treatment"
    )
    
    st.markdown("---")
    
    if "Non-Pharmacologic" in treatment_approach:
        render_non_pharmacologic()
    else:
        render_pharmacologic()
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Điều Trị")
    
    checklist_items = [
        "✅ Đánh giá CAM-ICU hàng ngày",
        "✅ Tìm Nguyên Nhân (PIMED)",
        "✅ Điều trị nguyên nhân",
        "✅ Non-pharmacologic management (ABCDE bundle)",
        "✅ Đánh giá đau thường xuyên",
        "✅ Đảm bảo giấc ngủ",
        "✅ Định hướng lại (reorientation)",
        "✅ Huy động gia đình",
        "✅ Cân nhắc thuốc nếu kích động nguy hiểm",
        "✅ Theo dõi đáp ứng điều trị"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người Cao Tuổi:**
        - Nguy cơ cao hơn
        - Thường là hypoactive delirium
        - Cẩn thận với thuốc (giảm liều)
        - Phục hồi chậm hơn
        
        **Suy thận:**
        - Điều chỉnh liều thuốc
        - Tránh tích lũy
        - Theo dõi chức năng thận
        """)
    
    with col2:
        st.markdown("""
        **Suy gan:**
        - Điều chỉnh liều thuốc
        - Tránh benzodiazepine nếu có thể
        - Theo dõi chức năng gan
        
        **Trẻ Em:**
        - Delirium ít gặp hơn
        - Cần đánh giá phù hợp lứa tuổi
        - Cẩn thận với thuốc
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục Tiêu Điều Trị")
    
    st.success("""
    **Mục Tiêu:**
    - ✅ Giải quyết nguyên nhân
    - ✅ Cải thiện ý thức
    - ✅ Giảm kích động (nếu có)
    - ✅ Phục hồi chức năng nhận thức
    - ✅ Giảm thời gian nằm viện
    
    **Theo Dõi:**
    - CAM-ICU hàng ngày
    - Dấu hiệu sống
    - Đáp ứng điều trị
    - Tác dụng phụ thuốc
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **ICU Delirium Guidelines**
       - Society of Critical Care Medicine
    
    2. **NICE Guidelines 2019**
       - Delirium: prevention, diagnosis and management
    
    3. **UpToDate:** Delirium in adults
       - Last updated: 2024
    
    4. **Medscape:** Delirium Management
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_hyperactive_delirium():
    """Hyperactive delirium protocol"""
    st.error("## 🔴 Hyperactive Delirium (Kích Động)")
    
    st.markdown("""
    **Triệu Chứng:**
    - Kích động, bồn chồn
    - Kéo ống, rút catheter
    - Đánh, đá, la hét
    - Không hợp tác
    - Nguy hiểm cho bản thân và nhân viên
    
    **Điều Trị:**
    1. **Non-pharmacologic (Ưu Tiên):**
       - Đảm bảo an toàn
       - Giải thích, trấn an
       - Môi trường yên tĩnh
       - Định hướng lại
    
    2. **Pharmacologic (Nếu cần):**
       - **Haloperidol:** 2-5 mg IV q4-6h
       - **Quetiapine:** 25-50 mg PO q12h
       - **Olanzapine:** 2.5-5 mg PO/IM q12h
       - **Risperidone:** 0.5-1 mg PO q12h
    
    3. **Nếu không đáp ứng:**
       - Tăng liều thuốc
       - Cân nhắc dexmedetomidine
       - Cân nhắc benzodiazepine (nếu không phải do benzodiazepine)
    """)


def render_hypoactive_delirium():
    """Hypoactive delirium protocol"""
    st.warning("## 🟡 Hypoactive Delirium (Ức Chế)")
    
    st.markdown("""
    **Triệu Chứng:**
    - Lơ mơ, li bì
    - Giảm vận động
    - Không đáp ứng
    - Rút lui
    - Dễ bỏ sót (không rõ ràng như hyperactive)
    
    **Điều Trị:**
    1. **Non-pharmacologic (Ưu Tiên):**
       - Kích thích nhẹ nhàng
       - Định hướng lại
       - Huy động gia đình
       - Vận động sớm
    
    2. **Pharmacologic:**
       - **Thường không cần thuốc an thần**
       - Chỉ dùng nếu cần thiết
       - Cân nhắc quetiapine hoặc olanzapine (liều thấp)
    
    3. **Quan trọng:**
       - Tìm Nguyên Nhân (thường là nhiễm trùng, rối loạn chuyển hóa)
       - Điều trị nguyên nhân
    """)


def render_mixed_delirium():
    """Mixed delirium protocol"""
    st.error("## 🟠 Mixed Delirium (Hỗn Hợp)")
    
    st.markdown("""
    **Triệu Chứng:**
    - Kết hợp cả hyperactive và hypoactive
    - Dao động giữa kích động và ức chế
    - Khó dự đoán
    
    **Điều Trị:**
    1. **Non-pharmacologic (Ưu Tiên):**
       - Linh hoạt theo từng giai đoạn
       - Đảm bảo an toàn khi kích động
       - Kích thích khi ức chế
    
    2. **Pharmacologic:**
       - **Haloperidol:** 2-5 mg IV q4-6h (khi kích động)
       - **Quetiapine:** 25-50 mg PO q12h
       - **Olanzapine:** 2.5-5 mg PO/IM q12h
    
    3. **Theo Dõi:**
       - Đánh giá thường xuyên
       - Điều chỉnh liều theo triệu chứng
    """)


def render_non_pharmacologic():
    """Non-pharmacologic management"""
    st.success("## ✅ Non-Pharmacologic Management (ABCDE Bundle)")
    
    st.markdown("""
    **ABCDE Bundle - Ưu Tiên Hàng Đầu:**
    
    **A - Assess, Prevent, and Manage Pain:**
    - Đánh giá đau thường xuyên
    - Điều trị đau đầy đủ
    - Multimodal analgesia
    
    **B - Both Spontaneous Awakening Trials (SAT) and Spontaneous Breathing Trials (SBT):**
    - Giảm an thần hàng ngày
    - Thử thở tự nhiên
    - Giảm thời gian thở máy
    
    **C - Choice of Sedation:**
    - Chọn thuốc an thần phù hợp
    - Tránh benzodiazepine nếu có thể
    - Ưu tiên dexmedetomidine, propofol
    
    **D - Delirium Assessment:**
    - CAM-ICU hàng ngày
    - Phát hiện sớm
    - Điều trị kịp thời
    
    **E - Early Mobility:**
    - Vận động sớm
    - Vật lý trị liệu
    - Giảm thời gian nằm liệt
    
    **Các Biện Pháp Khác:**
    - **Định hướng lại:** Nhắc nhở về thời gian, địa điểm, tình huống
    - **Môi trường:** Yên tĩnh, ánh sáng phù hợp, đồng hồ, lịch
    - **Gia đình:** Huy động gia đình tham gia
    - **Giấc ngủ:** Đảm bảo giấc ngủ ban đêm
    - **Thính giác/Thị giác:** Đảm bảo kính, máy trợ thính nếu cần
    """)


def render_pharmacologic():
    """Pharmacologic management"""
    st.warning("## 💊 Pharmacologic Management")
    
    st.markdown("""
    **Chỉ định dùng thuốc:**
    - Kích động nguy hiểm (tự làm hại, làm hại người khác)
    - Không đáp ứng non-pharmacologic
    - Cần an thần để điều trị (thở máy, thủ thuật)
    
    **⚠️ Lưu ý:**
    - Thuốc KHÔNG chữa delirium
    - Chỉ giúp kiểm soát triệu chứng
    - Phải điều trị nguyên nhân
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Haloperidol")
    
    st.info("""
    **Chỉ định:** Kích động nặng
    
    **Liều:**
    - **IV:** 2-5 mg q4-6h
    - **Có thể tăng:** 5-10 mg nếu cần
    - **Tối đa:** 20 mg/ngày
    
    **Ưu điểm:**
    - Tác dụng nhanh
    - Ít ức chế hô hấp
    - Có thể dùng IV
    
    **Nhược điểm:**
    - Nguy cơ QT kéo dài
    - Nguy cơ extrapyramidal symptoms
    - Không dùng nếu QT >500ms
    
    **Theo Dõi:**
    - ECG (QT interval)
    - Đáp ứng
    - Tác dụng phụ
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Quetiapine")
    
    st.info("""
    **Chỉ định:** Delirium nhẹ-trung bình
    
    **Liều:**
    - **Khởi đầu:** 25-50 mg PO q12h
    - **Có thể tăng:** 50-100 mg q12h
    - **Tối đa:** 200 mg/ngày
    
    **Ưu điểm:**
    - Ít tác dụng phụ ngoại tháp
    - An toàn hơn haloperidol
    - Có thể dùng lâu dài
    
    **Nhược điểm:**
    - Chỉ có PO (không có IV)
    - Tác dụng chậm hơn
    - Có thể gây hạ huyết áp
    
    **Theo Dõi:**
    - Huyết áp
    - Đáp ứng
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Olanzapine")
    
    st.info("""
    **Chỉ định:** Delirium nhẹ-trung bình
    
    **Liều:**
    - **PO:** 2.5-5 mg q12h
    - **IM:** 2.5-5 mg q12h (nếu không uống được)
    - **Tối đa:** 10 mg/ngày
    
    **Ưu điểm:**
    - Có cả PO và IM
    - Ít tác dụng phụ ngoại tháp
    - An toàn
    
    **Nhược điểm:**
    - Tác dụng chậm hơn haloperidol
    - Có thể gây hạ huyết áp
    
    **Theo Dõi:**
    - Huyết áp
    - Đáp ứng
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Dexmedetomidine")
    
    st.info("""
    **Chỉ định:** Delirium + Cần an thần nhẹ
    
    **Liều:**
    - **Truyền tĩnh mạch:** 0.2-0.7 µg/kg/h
    - **Mục tiêu RASS:** -2 đến 0
    
    **Ưu điểm:**
    - Giảm nguy cơ delirium
    - An thần nhẹ, dễ đánh thức
    - Ít ức chế hô hấp
    
    **Nhược điểm:**
    - Có thể gây hạ huyết áp, nhịp tim chậm
    - Cần truyền tĩnh mạch liên tục
    - Đắt tiền
    
    **Theo Dõi:**
    - Huyết áp, nhịp tim
    - RASS
    """)

