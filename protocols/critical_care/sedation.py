"""
ICU Sedation & Analgesia Protocol
SCCM 2018 Guidelines
Evidence-based sedation and analgesia management in ICU
"""

import streamlit as st


def render():
    """ICU Sedation & Analgesia Protocol"""
    st.subheader("💤 An Thần & Giảm Đau ICU (ICU Sedation & Analgesia)")
    st.caption("SCCM 2018 Guidelines - Sedation and analgesia in critically ill patients")
    
    st.info("""
    **Nguyên tắc an thần & giảm đau ICU:**
    - **Analgesia First:** Giảm đau trước, sau đó mới an thần nếu cần
    - **Light Sedation:** An thần nhẹ (RASS -2 đến 0) khi có thể
    - **Daily Interruption:** Ngừng an thần hàng ngày để đánh giá
    - **RASS-based:** Điều chỉnh theo RASS score
    - **Mục tiêu:** Tỉnh táo, hợp tác, không đau, không kích động
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 RASS (Richmond Agitation-Sedation Scale)")
    
    st.success("""
    **RASS Scale (-5 đến +4):**
    
    **+4:** Combative - Kích động, bạo lực
    **+3:** Very Agitated - Kéo ống, catheter; hung dữ
    **+2:** Agitated - Vận động không mục đích, chống máy thở
    **+1:** Restless - Lo âu nhưng không hung dữ
    **0:** Alert and Calm - Tỉnh táo, bình tĩnh ⭐ Mục tiêu
    **-1:** Drowsy - Buồn ngủ nhưng đáp ứng giọng nói (>10 giây)
    **-2:** Light Sedation - Tỉnh dậy ngắn với giọng nói (<10 giây) ⭐ Mục tiêu
    **-3:** Moderate Sedation - Cử động hoặc mở mắt với giọng nói
    **-4:** Deep Sedation - Không đáp ứng giọng nói, chỉ đáp ứng kích thích vật lý
    **-5:** Unarousable - Không đáp ứng giọng nói hoặc kích thích vật lý
    
    **Mục Tiêu RASS:**
    - **Hầu hết bệnh nhân:** -2 đến 0
    - **Cai máy thở:** 0 đến -1
    - **ARDS, sốc:** -2 đến -3
    - **Tránh:** RASS < -3 (trừ khi cần thiết)
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Chọn Thuốc")
    
    medication_type = st.radio(
        "**Loại thuốc:**",
        [
            "Analgesia (Giảm Đau) - Ưu tiên",
            "Sedation (An Thần)",
            "Combined (Kết Hợp)"
        ],
        key="medication_type"
    )
    
    st.markdown("---")
    
    if "Analgesia" in medication_type:
        render_analgesia()
    elif "Sedation" in medication_type and "Combined" not in medication_type:
        render_sedation()
    else:
        render_combined()
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân Loại Mức Độ")
    
    sedation_level = st.radio(
        "**Mức độ an thần cần thiết:**",
        ["Light Sedation (RASS -2 đến 0)", "Moderate Sedation (RASS -3)", "Deep Sedation (RASS -4 đến -5)"],
        key="sedation_level"
    )
    
    st.markdown("---")
    
    if "Light" in sedation_level:
        render_light_sedation()
    elif "Moderate" in sedation_level:
        render_moderate_sedation()
    else:
        render_deep_sedation()
    
    st.markdown("---")
    
    st.markdown("### ⏱️ Daily Sedation Interruption (DSI)")
    
    st.warning("""
    **Daily Sedation Interruption:**
    - Ngừng an thần hàng ngày để đánh giá
    - Mục đích: Giảm thời gian an thần, giảm thời gian thở máy
    - Thời gian: Mỗi sáng, ngừng an thần trong 1-2 giờ
    
    **Quy trình:**
    1. Ngừng an thần (giữ analgesia nếu cần)
    2. Đánh giá RASS, ý thức
    3. Đánh giá khả năng cai máy thở
    4. Đánh giá đau
    5. Quyết định: Tiếp tục an thần hay không
    
    **Chống Chỉ Định:**
    - Sốc không ổn định
    - ICP tăng
    - ARDS nặng
    - Co giật
    - Kích động nguy hiểm
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Điều Trị")
    
    checklist_items = [
        "✅ Đánh giá đau trước (NRS/VAS)",
        "✅ Bắt đầu với analgesia nếu đau",
        "✅ Đánh giá RASS thường xuyên (q2-4h)",
        "✅ Điều chỉnh liều theo RASS mục tiêu",
        "✅ Daily sedation interruption (nếu có thể)",
        "✅ Đánh giá khả năng cai máy thở",
        "✅ Theo dõi tác dụng phụ",
        "✅ Tránh an thần quá sâu (RASS < -3)",
        "✅ Giảm dần khi cải thiện",
        "✅ Đánh giá lại đau thường xuyên"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người Cao Tuổi:**
        - Nhạy cảm hơn với thuốc
        - Giảm liều 25-50%
        - Tránh benzodiazepine nếu có thể
        - Ưu tiên dexmedetomidine
        
        **Suy thận:**
        - Tránh morphine (tích lũy)
        - Ưu tiên fentanyl, hydromorphone
        - Điều chỉnh liều midazolam
        - Theo dõi tích lũy
        """)
    
    with col2:
        st.markdown("""
        **Suy gan:**
        - Tránh midazolam, lorazepam (tích lũy)
        - Ưu tiên propofol, dexmedetomidine
        - Cẩn thận với fentanyl
        - Theo dõi chức năng gan
        
        **Trẻ Em:**
        - Liều tính theo kg
        - Cẩn thận propofol infusion syndrome
        - Ưu tiên dexmedetomidine
        - Theo dõi sát
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục Tiêu Điều Trị")
    
    st.success("""
    **Mục Tiêu:**
    - ✅ RASS -2 đến 0 (khi có thể)
    - ✅ Không đau (NRS ≤3)
    - ✅ Hợp tác, tỉnh táo
    - ✅ Không kích động
    - ✅ Giảm thời gian thở máy
    - ✅ Giảm thời gian nằm ICU
    
    **Theo Dõi:**
    - RASS q2-4h
    - Đánh giá đau thường xuyên
    - Dấu hiệu sống
    - Tác dụng phụ thuốc
    - Khả năng cai máy thở
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **SCCM 2018 Guidelines**
       - Society of Critical Care Medicine
       - Clinical Practice Guidelines for the Prevention and Management of Pain, Agitation/Sedation, Delirium, Immobility, and Sleep Disruption
    
    2. **UpToDate:** Sedation in the ICU
       - Last updated: 2024
    
    3. **Medscape:** ICU Sedation Management
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_analgesia():
    """Analgesia protocol"""
    st.success("## 💉 Analgesia (Giảm Đau) - Ưu tiên")
    
    st.markdown("""
    **Nguyên tắc: Analgesia First**
    - Đau thường gây kích động
    - Giảm đau trước, sau đó mới an thần nếu cần
    - Multimodal analgesia (kết hợp nhiều thuốc)
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Fentanyl")
    
    st.info("""
    **Chỉ định:** ⭐ Ưu tiên cho ICU
    
    **Liều:**
    - **Loading:** 1-2 µg/kg IV
    - **Maintenance:** 0.5-2 µg/kg/h (25-100 µg/h ở Người Lớn)
    - **Bolus:** 25-50 µg IV q30-60min nếu cần
    
    **Ưu điểm:**
    - Khởi phát nhanh (1-2 phút)
    - Thời gian bán hủy ngắn (30-60 phút)
    - Ít tích lũy (ban đầu)
    - Không giải phóng histamine
    
    **Nhược điểm:**
    - Tích lũy ở suy thận (sau 24-48h)
    - Độ cứng ngực (liều cao)
    - Ức chế hô hấp
    
    **Theo Dõi:**
    - Đau (NRS/VAS)
    - RASS
    - Huyết áp, nhịp tim
    - Độ cứng ngực
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Morphine")
    
    st.info("""
    **Chỉ định:** Giảm đau ICU
    
    **Liều:**
    - **Loading:** 0.05-0.1 mg/kg IV
    - **Maintenance:** 0.01-0.05 mg/kg/h (0.5-5 mg/h ở Người Lớn)
    - **Bolus:** 2-5 mg IV q2-4h nếu cần
    
    **Ưu điểm:**
    - Rẻ tiền
    - Hiệu quả
    
    **Nhược điểm:**
    - Tích lũy ở suy thận (morphine-6-glucuronide)
    - Giải phóng histamine (hạ huyết áp)
    - Thời gian bán hủy dài
    
    **Chống Chỉ Định:**
    - Suy thận nặng
    - Dị ứng morphine
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Hydromorphone")
    
    st.info("""
    **Chỉ định:** Giảm đau ICU (thay thế morphine)
    
    **Liều:**
    - **Loading:** 0.01-0.02 mg/kg IV
    - **Maintenance:** 0.003-0.015 mg/kg/h (0.2-1.5 mg/h ở Người Lớn)
    - **Bolus:** 0.5-1 mg IV q2-4h nếu cần
    
    **Ưu điểm:**
    - Mạnh hơn morphine 5-7 lần
    - Ít tích lũy ở suy thận
    - Ít giải phóng histamine
    
    **Nhược điểm:**
    - Đắt tiền hơn morphine
    - Cần liều chính xác (mạnh)
    """)


def render_sedation():
    """Sedation protocol"""
    st.warning("## 💤 Sedation (An Thần)")
    
    st.markdown("""
    **Chỉ định an thần:**
    - Kích động, không hợp tác
    - Chống máy thở
    - Cần an thần để điều trị
    - ARDS, sốc (cần an thần sâu hơn)
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Propofol")
    
    st.success("""
    **Chỉ định:** ⭐ Ưu tiên cho an thần ngắn hạn
    
    **Liều:**
    - **Loading:** 0.5-1 mg/kg IV (tùy chọn)
    - **Maintenance:** 5-50 µg/kg/min (0.3-3 mg/kg/h)
    - **Mục tiêu RASS:** -2 đến -3
    
    **Ưu điểm:**
    - Khởi phát nhanh (30-60 giây)
    - Thời gian bán hủy ngắn (5-10 phút)
    - Dễ điều chỉnh
    - Không tích lũy
    
    **Nhược điểm:**
    - Hạ huyết áp
    - Propofol infusion syndrome (liều cao >4 mg/kg/h >48h)
    - Tăng triglyceride
    
    **Chống Chỉ Định:**
    - Dị ứng propofol
    - Tăng lipid máu nặng
    - Propofol infusion syndrome
    
    **Theo Dõi:**
    - RASS
    - Huyết áp
    - Triglyceride (nếu dùng lâu)
    - Creatine kinase (nếu nghi ngờ propofol infusion syndrome)
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Midazolam")
    
    st.info("""
    **Chỉ định:** An thần ICU
    
    **Liều:**
    - **Loading:** 0.05-0.1 mg/kg IV (max 5 mg)
    - **Maintenance:** 0.02-0.1 mg/kg/h (0.5-5 mg/h ở Người Lớn)
    - **Bolus:** 2-5 mg IV q30-60min nếu cần
    - **Mục tiêu RASS:** -2 đến -3
    
    **Ưu điểm:**
    - An thần tốt
    - Có thể dùng kết hợp với opioid
    
    **Nhược điểm:**
    - Tích lũy ở suy gan/thận
    - Thời gian bán hủy dài (sau tích lũy)
    - Tăng nguy cơ delirium
    - Khó điều chỉnh
    
    **Chống Chỉ Định:**
    - Suy gan nặng
    - Dị ứng benzodiazepine
    
    **Theo Dõi:**
    - RASS
    - Tích lũy (thời gian bán hủy tăng)
    - Delirium
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Dexmedetomidine")
    
    st.success("""
    **Chỉ định:** ⭐ Ưu tiên cho an thần nhẹ, cai máy thở
    
    **Liều:**
    - **Loading:** 1 µg/kg trong 10 phút (tùy chọn)
    - **Maintenance:** 0.2-1.4 µg/kg/h
    - **Mục tiêu RASS:** 0 đến -2 (awake sedation)
    
    **Ưu điểm:**
    - An thần tỉnh táo (awake sedation)
    - Ít ức chế hô hấp
    - Giảm nguy cơ delirium
    - Tốt cho cai máy thở
    
    **Nhược điểm:**
    - Nhịp chậm, hạ huyết áp
    - Đắt tiền
    - Cần truyền tĩnh mạch liên tục
    
    **Chống Chỉ Định:**
    - Block AV độ cao
    - Nhịp chậm nặng
    
    **Theo Dõi:**
    - RASS
    - Nhịp tim, huyết áp
    """)


def render_combined():
    """Combined analgesia and sedation"""
    st.warning("## 💊 Combined (Kết Hợp Analgesia + Sedation)")
    
    st.markdown("""
    **Nguyên tắc:**
    - Bắt đầu với analgesia
    - Thêm sedation nếu cần
    - Điều chỉnh từng thuốc riêng biệt
    - Multimodal approach
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Phác Đồ Kết Hợp Thường Dùng")
    
    st.info("""
    **1. Fentanyl + Propofol:**
    - Fentanyl: 0.5-2 µg/kg/h
    - Propofol: 5-30 µg/kg/min
    - Mục tiêu RASS: -2 đến 0
    
    **2. Fentanyl + Dexmedetomidine:**
    - Fentanyl: 0.5-2 µg/kg/h
    - Dexmedetomidine: 0.2-1.4 µg/kg/h
    - Mục tiêu RASS: 0 đến -2 (awake sedation)
    
    **3. Morphine + Midazolam:**
    - Morphine: 0.01-0.05 mg/kg/h
    - Midazolam: 0.02-0.1 mg/kg/h
    - Mục tiêu RASS: -2 đến -3
    
    **Lưu ý:**
    - Điều chỉnh từng thuốc riêng
    - Giảm liều khi cải thiện
    - Daily interruption nếu có thể
    """)


def render_light_sedation():
    """Light sedation protocol"""
    st.success("## 🟢 Light Sedation (RASS -2 đến 0)")
    
    st.markdown("""
    **Mục Tiêu:**
    - RASS -2 đến 0
    - Tỉnh táo, hợp tác
    - Không đau
    - Không kích động
    
    **Điều Trị:**
    1. **Analgesia:**
       - Fentanyl: 0.5-1 µg/kg/h
       - Hoặc Morphine: 0.01-0.03 mg/kg/h
    
    2. **Sedation (nếu cần):**
       - Dexmedetomidine: 0.2-0.7 µg/kg/h ⭐ Ưu tiên
       - Hoặc Propofol: 5-15 µg/kg/min
    
    3. **Theo Dõi:**
       - RASS q2-4h
       - Đánh giá đau thường xuyên
       - Khả năng cai máy thở
    
    **Lợi ích:**
    - Giảm thời gian thở máy
    - Giảm nguy cơ delirium
    - Dễ đánh giá thần kinh
    - Dễ giao tiếp
    """)


def render_moderate_sedation():
    """Moderate sedation protocol"""
    st.warning("## 🟡 Moderate Sedation (RASS -3)")
    
    st.markdown("""
    **Mục Tiêu:**
    - RASS -3
    - An thần vừa phải
    - Vẫn đáp ứng kích thích
    
    **Chỉ định:**
    - ARDS
    - Sốc
    - Cần an thần để điều trị
    
    **Điều Trị:**
    1. **Analgesia:**
       - Fentanyl: 1-2 µg/kg/h
       - Hoặc Morphine: 0.03-0.05 mg/kg/h
    
    2. **Sedation:**
       - Propofol: 15-30 µg/kg/min ⭐ Ưu tiên
       - Hoặc Midazolam: 0.05-0.1 mg/kg/h
    
    3. **Theo Dõi:**
       - RASS q2-4h
       - Huyết động
       - Đánh giá khả năng giảm an thần
    """)


def render_deep_sedation():
    """Deep sedation protocol"""
    st.error("## 🔴 Deep Sedation (RASS -4 đến -5)")
    
    st.markdown("""
    **Mục Tiêu:**
    - RASS -4 đến -5
    - An thần sâu
    - Chỉ đáp ứng kích thích vật lý
    
    **Chỉ định:**
    - ARDS nặng
    - Sốc không ổn định
    - ICP tăng
    - Cần an thần sâu để điều trị
    
    **Điều Trị:**
    1. **Analgesia:**
       - Fentanyl: 1-2 µg/kg/h
       - Hoặc Morphine: 0.03-0.05 mg/kg/h
    
    2. **Sedation:**
       - Propofol: 30-50 µg/kg/min
       - Hoặc Midazolam: 0.1 mg/kg/h
       - Có thể kết hợp
    
    3. **Theo Dõi:**
       - RASS q2-4h
       - Huyết động liên tục
       - EEG (nếu nghi ngờ co giật)
       - Đánh giá khả năng giảm an thần
    
    **Lưu ý:**
    - Chỉ dùng khi thực sự cần
    - Giảm dần khi cải thiện
    - Tránh kéo dài
    """)

