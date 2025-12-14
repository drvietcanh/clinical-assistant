"""
Anticoagulation Reversal Protocol
ACCP 2018, ASH 2018
Reversal of anticoagulants in bleeding or urgent procedures
"""

import streamlit as st


def render():
    """Anticoagulation Reversal Protocol"""
    st.subheader("🩸 Đảo Ngược Chống Đông (Anticoagulation Reversal)")
    st.caption("ACCP 2018, ASH 2018 - Anticoagulation reversal guidelines")
    
    st.error("""
    **⚠️ CẤP CỨU - Cần đảo ngược chống đông khi:**
    - Chảy máu nặng hoặc đe dọa tính mạng
    - Phẫu thuật cấp cứu
    - Thủ thuật xâm lấn cấp cứu
    - INR/PTT tăng cao + chảy máu
    
    **Nguyên tắc:**
    - Xác định loại thuốc chống đông
    - Đánh giá mức độ chảy máu
    - Chọn chất đối kháng phù hợp
    - Theo dõi đáp ứng
    """)
    
    st.markdown("---")
    
    st.markdown("### 🩸 Chọn Loại Thuốc Chống Đông Cần Đảo Ngược")
    
    anticoagulant_type = st.radio(
        "**Loại thuốc chống đông:**",
        [
            "Warfarin",
            "DOAC - Dabigatran",
            "DOAC - Xa Inhibitors (Apixaban, Rivaroxaban, Edoxaban)",
            "Heparin (UFH)",
            "LMWH (Enoxaparin, Dalteparin)"
        ],
        key="anticoagulant_type"
    )
    
    st.markdown("---")
    
    if "Warfarin" in anticoagulant_type:
        render_warfarin_reversal()
    elif "Dabigatran" in anticoagulant_type:
        render_dabigatran_reversal()
    elif "Xa Inhibitors" in anticoagulant_type:
        render_xa_inhibitor_reversal()
    elif "Heparin" in anticoagulant_type and "LMWH" not in anticoagulant_type:
        render_heparin_reversal()
    else:
        render_lmwh_reversal()
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân loại mức độ Chảy Máu")
    
    bleeding_severity = st.radio(
        "**Mức độ chảy máu:**",
        ["Không chảy máu (INR cao)", "Chảy máu nhẹ", "Chảy máu trung bình", "Chảy máu nặng"],
        key="bleeding_severity"
    )
    
    st.markdown("---")
    
    if "Không chảy máu" in bleeding_severity:
        render_no_bleeding()
    elif "nhẹ" in bleeding_severity:
        render_mild_bleeding()
    elif "trung bình" in bleeding_severity:
        render_moderate_bleeding()
    else:
        render_severe_bleeding()
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh sách kiểm tra đảo ngược")
    
    checklist_items = [
        "✅ Xác định loại thuốc chống đông",
        "✅ Đánh giá mức độ chảy máu",
        "✅ Kiểm tra INR/PTT/anti-Xa (nếu có)",
        "✅ Chọn chất đối kháng phù hợp",
        "✅ Tính liều chính xác",
        "✅ Chuẩn bị thuốc đối kháng",
        "✅ Theo dõi đáp ứng sau khi dùng",
        "✅ Kiểm tra lại INR/PTT sau 30-60 phút",
        "✅ Theo dõi chảy máu",
        "✅ Cân nhắc liều lặp lại nếu cần"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm bệnh nhân đặc biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Cẩn thận với liều cao (nguy cơ quá liều)
        - Theo dõi sát hơn
        - Cân nhắc giảm liều nếu suy thận
        
        **Suy thận:**
        - DOAC: Cần điều chỉnh liều đối kháng
        - Protamine: Cẩn thận tích lũy
        - Theo dõi chức năng thận
        """)
    
    with col2:
        st.markdown("""
        **Suy gan:**
        - Warfarin: Có thể cần liều vitamin K cao hơn
        - PCC: Cẩn thận với nguy cơ huyết khối
        - Theo dõi chức năng gan
        
        **Phụ nữ có thai:**
        - Vitamin K an toàn
        - PCC: Cân nhắc cẩn thận
        - Protamine: Có thể dùng nếu cần
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục tiêu điều trị")
    
    st.success("""
    **Mục tiêu:**
    - ✅ INR <1.5 (warfarin)
    - ✅ PTT bình thường (heparin)
    - ✅ Cầm máu hiệu quả
    - ✅ Không tái phát chảy máu
    - ✅ Không biến chứng huyết khối
    
    **Theo dõi:**
    - INR/PTT sau 30-60 phút
    - Dấu hiệu sống
    - Tình trạng chảy máu
    - Dấu hiệu huyết khối (nếu dùng PCC)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **ACCP 2018 Guidelines**
       - American College of Chest Physicians
       - Antithrombotic Therapy and Prevention of Thrombosis
    
    2. **ASH 2018 Guidelines**
       - American Society of Hematology
       - Management of Anticoagulation
    
    3. **UpToDate:** Anticoagulation reversal
       - Last updated: 2024
    
    4. **Medscape:** Anticoagulation Reversal
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_warfarin_reversal():
    """Warfarin reversal protocol"""
    st.warning("## 💊 Đảo Ngược Warfarin")
    
    st.markdown("""
    **Warfarin (Coumadin):**
    - Cơ chế: Ức chế tổng hợp yếu tố đông máu phụ thuộc vitamin K (II, VII, IX, X)
    - Thời gian bán hủy: 20-60 giờ
    - Đánh giá: INR
    
    **Chất đối kháng:**
    1. **Vitamin K (Phytomenadione)**
    2. **Fresh Frozen Plasma (FFP)**
    3. **Prothrombin Complex Concentrate (PCC)** ⭐ Ưu tiên
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Vitamin K")
    
    st.info("""
    **Chỉ định:**
    - INR tăng cao (>5.0) không chảy máu
    - Chảy máu nhẹ-trung bình
    - Bổ sung cho FFP/PCC
    
    **Liều:**
    - **PO (Không chảy máu, INR >10):** 2.5-5 mg
    - **IV (Chảy máu):** 5-10 mg
    - **Tác dụng:** Bắt đầu sau 6-12 giờ (PO) hoặc 1-2 giờ (IV)
    - **Thời gian:** 24-48 giờ để đạt hiệu quả tối đa
    
    **Lưu ý:**
    - IV: Truyền chậm (≥10 phút) để tránh phản ứng phản vệ
    - Có thể gây kháng warfarin trong 1-2 tuần
    """)
    
    st.markdown("---")
    
    st.markdown("### 🩸 Fresh Frozen Plasma (FFP)")
    
    st.info("""
    **Chỉ định:**
    - Chảy máu nặng khi không có PCC
    - Cần đảo ngược ngay lập tức
    
    **Liều:**
    - **10-15 mL/kg IV**
    - **Tác dụng:** Ngay lập tức
    - **Thời gian:** 12-24 giờ
    
    **Nhược điểm:**
    - Cần thời gian rã đông
    - Nguy cơ TRALI, TACO
    - Thể tích lớn
    """)
    
    st.markdown("---")
    
    st.markdown("### ⭐ Prothrombin Complex Concentrate (PCC)")
    
    st.success("""
    **Chỉ định:** ⭐ ƯU TIÊN cho chảy máu nặng
    
    **Liều:**
    - **25-50 units/kg IV** (dựa trên yếu tố IX)
    - **Tác dụng:** Ngay lập tức
    - **Thời gian:** 12-24 giờ
    
    **Ưu điểm:**
    - Tác dụng nhanh
    - Thể tích nhỏ
    - Không cần nhóm máu
    - Hiệu quả tốt hơn FFP
    
    **Nhược điểm:**
    - Nguy cơ huyết khối (1-2%)
    - Chi phí cao
    - Không có ở tất cả bệnh viện
    """)


def render_dabigatran_reversal():
    """Dabigatran reversal protocol"""
    st.warning("## 💊 Đảo Ngược Dabigatran (Pradaxa)")
    
    st.markdown("""
    **Dabigatran:**
    - Cơ chế: Ức chế trực tiếp thrombin (IIa)
    - Thời gian bán hủy: 12-17 giờ (bình thường), 27 giờ (suy thận)
    - Đánh giá: aPTT, TT (thrombin time)
    
    **Chất đối kháng:**
    - **Idarucizumab (Praxbind)** ⭐ Chuyên biệt
    - **PCC** (nếu không có idarucizumab)
    """)
    
    st.markdown("---")
    
    st.markdown("### ⭐ Idarucizumab (Praxbind)")
    
    st.success("""
    **Chỉ định:** ⭐ ĐẢO NGƯỢC CHUYÊN BIỆT cho dabigatran
    
    **Liều:**
    - **5 g IV** (2 lọ 2.5g)
    - **Truyền:** 2 lọ truyền nhanh liên tiếp
    - **Tác dụng:** Ngay lập tức
    - **Thời gian:** 24 giờ
    
    **Ưu điểm:**
    - Đảo ngược hoàn toàn
    - An toàn
    - Tác dụng nhanh
    
    **Lưu ý:**
    - Đắt tiền
    - Có thể cần liều lặp lại nếu tái chảy máu
    """)
    
    st.markdown("---")
    
    st.markdown("### 🩸 PCC (Nếu Không Có Idarucizumab)")
    
    st.info("""
    **Chỉ định:**
    - Chảy máu nặng
    - Không có idarucizumab
    
    **Liều:**
    - **50 units/kg IV** (yếu tố IX)
    - **Tác dụng:** Một phần
    
    **Lưu ý:**
    - Không đảo ngược hoàn toàn
    - Cần theo dõi sát
    """)


def render_xa_inhibitor_reversal():
    """Xa inhibitor reversal protocol"""
    st.warning("## 💊 Đảo Ngược Xa Inhibitors")
    
    st.markdown("""
    **Xa Inhibitors:**
    - **Apixaban (Eliquis)**
    - **Rivaroxaban (Xarelto)**
    - **Edoxaban (Savaysa)**
    
    **Cơ chế:** Ức chế trực tiếp yếu tố Xa
    **Thời gian bán hủy:** 5-15 giờ
    **Đánh giá:** Anti-Xa assay (nếu có)
    
    **Chất đối kháng:**
    - **Andexanet Alfa (Andexxa)** ⭐ Chuyên biệt
    - **PCC** (nếu không có andexanet)
    """)
    
    st.markdown("---")
    
    st.markdown("### ⭐ Andexanet Alfa (Andexxa)")
    
    st.success("""
    **Chỉ định:** ⭐ ĐẢO NGƯỢC CHUYÊN BIỆT cho Xa inhibitors
    
    **Liều:**
    - **Low dose:** 400 mg IV bolus, sau đó 4 mg/min x 120 phút
    - **High dose:** 800 mg IV bolus, sau đó 8 mg/min x 120 phút
    - **Chọn liều:** Dựa trên liều Xa inhibitor gần nhất
    
    **Tác dụng:** Ngay lập tức
    **Thời gian:** 1-2 giờ
    
    **Ưu điểm:**
    - Đảo ngược hiệu quả
    - Tác dụng nhanh
    
    **Nhược điểm:**
    - Đắt tiền
    - Nguy cơ huyết khối (10-15%)
    - Cần truyền liên tục
    """)
    
    st.markdown("---")
    
    st.markdown("### 🩸 PCC (Nếu Không Có Andexanet)")
    
    st.info("""
    **Chỉ định:**
    - Chảy máu nặng
    - Không có andexanet
    
    **Liều:**
    - **50 units/kg IV** (yếu tố IX)
    - **Tác dụng:** Một phần
    
    **Lưu ý:**
    - Không đảo ngược hoàn toàn
    - Cần theo dõi sát
    """)


def render_heparin_reversal():
    """Heparin reversal protocol"""
    st.warning("## 💊 Đảo Ngược Heparin (UFH)")
    
    st.markdown("""
    **Heparin (UFH):**
    - Cơ chế: Tăng cường antithrombin III
    - Thời gian bán hủy: 1-2 giờ
    - Đánh giá: aPTT
    
    **Chất đối kháng:**
    - **Protamine Sulfate** ⭐
    """)
    
    st.markdown("---")
    
    st.markdown("### ⭐ Protamine Sulfate")
    
    st.success("""
    **Chỉ định:**
    - Chảy máu nặng do heparin
    - Phẫu thuật cấp cứu
    - aPTT kéo dài + chảy máu
    
    **Liều:**
    - **1 mg protamine cho mỗi 100 units heparin** còn lại
    - **Tối đa:** 50 mg mỗi lần
    - **Truyền:** Chậm IV (≥10 phút)
    
    **Tính liều:**
    - Nếu vừa ngừng heparin: 1 mg/100 units liều cuối
    - Nếu đã ngừng >30 phút: Giảm liều 50%
    - Nếu đã ngừng >2 giờ: Có thể không cần
    
    **Tác dụng:** Ngay lập tức
    
    **Tác dụng phụ:**
    - Hạ huyết áp (truyền quá nhanh)
    - Phản ứng phản vệ (người dùng insulin protamine)
    - Tăng nguy cơ huyết khối (quá liều)
    """)


def render_lmwh_reversal():
    """LMWH reversal protocol"""
    st.warning("## 💊 Đảo Ngược LMWH")
    
    st.markdown("""
    **LMWH (Enoxaparin, Dalteparin):**
    - Cơ chế: Tăng cường antithrombin III
    - Thời gian bán hủy: 3-5 giờ
    - Đánh giá: Anti-Xa assay
    
    **Chất đối kháng:**
    - **Protamine Sulfate** (đảo ngược một phần)
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Protamine Sulfate (Đảo Ngược Một Phần)")
    
    st.info("""
    **Chỉ định:**
    - Chảy máu nặng do LMWH
    - Phẫu thuật cấp cứu
    
    **Liều:**
    - **1 mg protamine cho mỗi 1 mg enoxaparin** (hoặc 100 units anti-Xa)
    - **Nếu >8 giờ sau liều cuối:** 0.5 mg protamine/1 mg enoxaparin
    - **Tối đa:** 50 mg mỗi lần
    - **Truyền:** Chậm IV (≥10 phút)
    
    **Hiệu quả:**
    - Đảo ngược ~60% tác dụng chống đông
    - Không đảo ngược hoàn toàn
    
    **Lưu ý:**
    - Có thể cần liều lặp lại
    - Theo dõi sát chảy máu
    """)


def render_no_bleeding():
    """No bleeding protocol"""
    st.success("## 🟢 INR Cao - Không Chảy Máu")
    
    st.markdown("""
    **Chỉ định đảo ngược:**
    - INR >5.0 nhưng <10.0: Có thể không cần
    - INR >10.0: Cân nhắc vitamin K
    
    **Điều trị:**
    1. **INR 5.0-9.0:**
       - Ngừng warfarin
       - Theo dõi
       - Có thể cho vitamin K 1-2.5 mg PO nếu nguy cơ cao
    
    2. **INR >9.0:**
       - Vitamin K 2.5-5 mg PO
       - Theo dõi INR sau 24 giờ
    
    **Theo dõi:**
    - INR mỗi 24 giờ
    - Dấu hiệu chảy máu
    """)


def render_mild_bleeding():
    """Mild bleeding protocol"""
    st.warning("## 🟡 Chảy Máu Nhẹ")
    
    st.markdown("""
    **Triệu chứng:**
    - Chảy máu nhỏ (chảy máu cam, chảy máu nướu)
    - Không đe dọa tính mạng
    
    **Điều trị:**
    1. **Warfarin:**
       - Ngừng warfarin
       - Vitamin K 2.5-5 mg PO hoặc 1-2 mg IV
       - Theo dõi INR
    
    2. **DOAC:**
       - Ngừng DOAC
       - Theo dõi
       - Cân nhắc PCC nếu không cầm máu
    
    3. **Heparin/LMWH:**
       - Ngừng heparin/LMWH
       - Theo dõi
    """)


def render_moderate_bleeding():
    """Moderate bleeding protocol"""
    st.error("## 🟠 Chảy Máu Trung Bình")
    
    st.markdown("""
    **Triệu chứng:**
    - Chảy máu rõ rệt
    - Có thể cần truyền máu
    - Không đe dọa tính mạng ngay
    
    **Điều trị:**
    1. **Warfarin:**
       - Ngừng warfarin
       - Vitamin K 5-10 mg IV
       - PCC 25-50 units/kg IV (ưu tiên) hoặc FFP 10-15 mL/kg
    
    2. **Dabigatran:**
       - Idarucizumab 5 g IV (nếu có)
       - Hoặc PCC 50 units/kg IV
    
    3. **Xa Inhibitors:**
       - Andexanet (nếu có)
       - Hoặc PCC 50 units/kg IV
    
    4. **Heparin:**
       - Protamine 1 mg/100 units heparin
    
    5. **LMWH:**
       - Protamine 1 mg/1 mg enoxaparin
    """)


def render_severe_bleeding():
    """Severe bleeding protocol"""
    st.error("## 🔴 Chảy Máu Nặng - Cấp cứu")
    
    st.markdown("""
    **Triệu chứng:**
    - Chảy máu đe dọa tính mạng
    - Sốc xuất huyết
    - Chảy máu nội sọ
    - Cần truyền máu ngay
    
    **Điều trị Ngay:**
    1. **ABC:** Đường thở, Hô hấp, Tuần hoàn
    2. **Truyền máu:** Nếu cần
    3. **Đảo ngược ngay:**
    
    **Warfarin:**
    - PCC 50 units/kg IV ngay (ưu tiên)
    - Vitamin K 10 mg IV
    - FFP nếu không có PCC
    
    **Dabigatran:**
    - Idarucizumab 5 g IV ngay (nếu có)
    - PCC 50 units/kg IV nếu không có
    
    **Xa Inhibitors:**
    - Andexanet (nếu có)
    - PCC 50 units/kg IV nếu không có
    
    **Heparin:**
    - Protamine 1 mg/100 units heparin
    
    **LMWH:**
    - Protamine 1 mg/1 mg enoxaparin
    
    **Theo dõi:**
    - ICU monitoring
    - INR/PTT sau 30-60 phút
    - Dấu hiệu sống liên tục
    """)

