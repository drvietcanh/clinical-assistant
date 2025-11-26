"""
Opioid Overdose / Naloxone Protocol
AHA 2020, SAMHSA
Life-threatening opioid overdose requiring immediate reversal
"""

import streamlit as st


def render():
    """Opioid Overdose / Naloxone Protocol"""
    st.subheader("💉 Ngộ Độc Opioid / Naloxone")
    st.caption("AHA 2020, SAMHSA - Opioid overdose reversal protocol")
    
    st.error("""
    **⚠️ NGỘ ĐỘC OPIOID = CẤP CỨU Y TẾ**
    
    **Triệu Chứng Điển Hình:**
    - Ức chế hô hấp (respiratory depression)
    - Đồng tử co nhỏ (miosis)
    - Giảm ý thức, hôn mê
    - Da lạnh, ẩm
    - Nhịp tim chậm
    
    **Chẩn Đoán:** Nghi ngờ khi có tam chứng: Ức chế hô hấp + Miosis + Giảm ý thức
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử Trí Ngay Lập Tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        - **Đảm bảo đường thở:** Head-tilt, chin-lift
        - **Oxygen:** 100% qua mask
        - **Bag-mask ventilation:** Nếu không thở
        - **Chuẩn bị intubation:** Nếu cần
        
        **2. CIRCULATION**
        
        - **Monitor:** BP, HR, SpO2, ECG
        - **Truyền dịch:** NS nếu hạ huyết áp
        - **Naloxone:** Ngay lập tức
        """)
    
    with col2:
        st.warning("""
        **3. NALOXONE - Thuốc Đối Kháng**
        
        **Mục Tiêu:** Đảo ngược ức chế hô hấp
        
        **Liều ban đầu:**
        - **Người Lớn:** 0.4-2 mg IV/IM/IN
        - **Trẻ Em:** 0.01 mg/kg IV/IM/IN
        - **Lặp lại:** q2-3 phút nếu cần
        
        **Theo Dõi:** 
        - Đáp ứng trong 1-2 phút
        - Có thể cần liều cao hơn (fentanyl: 2-10 mg)
        """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Naloxone Dosing Protocol")
    
    route = st.radio(
        "**Đường dùng Naloxone:**",
        ["IV (Tĩnh mạch)", "IM (Tiêm bắp)", "IN (Qua mũi)", "Auto-injector"],
        key="naloxone_route"
    )
    
    st.markdown("---")
    
    if "IV" in route:
        render_iv_protocol()
    elif "IM" in route:
        render_im_protocol()
    elif "IN" in route:
        render_in_protocol()
    else:
        render_auto_injector_protocol()
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân Loại Mức Độ")
    
    severity = st.radio(
        "**Mức độ nghiêm trọng:**",
        ["Nhẹ (Mild)", "Trung bình (Moderate)", "Nặng (Severe)", "Ngừng thở (Respiratory Arrest)"],
        key="opioid_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_overdose()
    elif "Trung bình" in severity:
        render_moderate_overdose()
    elif "Nặng" in severity:
        render_severe_overdose()
    else:
        render_respiratory_arrest()
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Re-Narcotization (Tái Ngộ Độc)")
    
    st.warning("""
    **Nguy Cơ Tái Ngộ Độc:**
    - Naloxone có thời gian bán hủy ngắn (30-90 phút)
    - Opioid có thể tồn tại lâu hơn (đặc biệt là fentanyl, methadone)
    - Bệnh nhân có thể Tái Ngộ Độc sau khi naloxone hết tác dụng
    
    **Khuyến nghị:**
    - **Theo dõi ít nhất 2-4 giờ** sau khi đáp ứng
    - **Nếu dùng fentanyl/methadone:** Theo dõi 4-6 giờ
    - **Nếu dùng long-acting opioids:** Cân nhắc naloxone truyền tĩnh mạch
    - **Không xuất viện sớm** nếu không chắc chắn
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Naloxone Infusion Protocol")
    
    st.info("""
    **Chỉ định truyền tĩnh mạch:**
    - Cần nhiều liều naloxone
    - Long-acting opioids (methadone, buprenorphine)
    - Fentanyl overdose
    - Tái Ngộ Độc sau khi ngừng naloxone
    
    **Liều truyền:**
    - **Bolus:** 0.4-2 mg IV
    - **Truyền tĩnh mạch:** 0.4-2 mg/h
    - **Điều Chỉnh:** Theo đáp ứng hô hấp
    - **Mục Tiêu:** Duy trì RR ≥12/min, SpO2 ≥94%
    
    **Theo Dõi:**
    - RR, SpO2 mỗi 15-30 phút
    - Ý thức
    - Có thể cần tăng liều nếu Tái Ngộ Độc
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Điều Trị")
    
    checklist_items = [
        "✅ ABC: Airway, Breathing, Circulation",
        "✅ Oxygen 100%",
        "✅ Naloxone ngay lập tức (0.4-2 mg)",
        "✅ Đánh giá đáp ứng trong 1-2 phút",
        "✅ Lặp lại naloxone nếu không đáp ứng",
        "✅ Monitor RR, SpO2, ý thức",
        "✅ Theo dõi 2-4 giờ (nguy cơ Tái Ngộ Độc)",
        "✅ Cân nhắc naloxone truyền tĩnh mạch nếu cần",
        "✅ Hỗ trợ hô hấp nếu cần"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ Em:**
        - Liều: 0.01 mg/kg IV/IM/IN
        - Có thể cần liều cao hơn nếu fentanyl
        - Theo dõi sát (dễ Tái Ngộ Độc)
        
        **Phụ Nữ Có Thai:**
        - Naloxone an toàn (không qua nhau thai nhiều)
        - Ưu tiên cứu mẹ
        - Monitor thai nhi sau khi mẹ ổn định
        """)
    
    with col2:
        st.markdown("""
        **Người Cao Tuổi:**
        - Có thể nhạy cảm hơn với naloxone
        - Bắt đầu với liều thấp
        - Theo dõi huyết động (có thể tăng huyết áp)
        
        **Bệnh nhân dùng methadone/buprenorphine:**
        - Có thể cần liều cao hơn
        - Cân nhắc truyền tĩnh mạch
        - Theo dõi lâu hơn (4-6 giờ)
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục Tiêu Điều Trị")
    
    st.success("""
    **Mục Tiêu:**
    - ✅ Hồi phục hô hấp (RR ≥12/min)
    - ✅ SpO2 ≥94%
    - ✅ Hồi phục ý thức
    - ✅ Không Tái Ngộ Độc trong 2-4 giờ
    
    **Xuất viện khi:**
    - Không triệu chứng ≥2-4 giờ
    - Hô hấp ổn định
    - Ý thức bình thường
    - Có kế hoạch theo dõi
    - Tư vấn về nguy cơ Tái Ngộ Độc
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **AHA 2020 Guidelines**
       - Opioid-associated out-of-hospital cardiac arrest
    
    2. **SAMHSA Guidelines 2020**
       - Opioid Overdose Prevention Toolkit
    
    3. **UpToDate:** Opioid overdose
       - Last updated: 2024
    
    4. **Medscape:** Opioid Overdose Management
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_iv_protocol():
    """IV naloxone protocol"""
    st.success("## 💉 Naloxone IV (Tĩnh Mạch)")
    
    st.markdown("""
    **Liều:**
    - **Người Lớn:** 0.4-2 mg IV bolus
    - **Trẻ Em:** 0.01 mg/kg IV (max 2 mg)
    
    **Ưu điểm:**
    - Tác dụng nhanh nhất (30-60 giây)
    - Có thể điều chỉnh liều dễ dàng
    - Có thể truyền tĩnh mạch nếu cần
    
    **Lưu ý:**
    - Cần đường tĩnh mạch
    - Có thể gây withdrawal syndrome nếu dùng quá nhiều
    - Theo dõi đáp ứng ngay
    """)


def render_im_protocol():
    """IM naloxone protocol"""
    st.warning("## 💉 Naloxone IM (Tiêm Bắp)")
    
    st.markdown("""
    **Liều:**
    - **Người Lớn:** 0.4-2 mg IM
    - **Trẻ Em:** 0.01 mg/kg IM (max 2 mg)
    
    **Ưu điểm:**
    - Không cần đường tĩnh mạch
    - Tác dụng trong 2-5 phút
    - Dễ thực hiện
    
    **Lưu ý:**
    - Tác dụng chậm hơn IV
    - Có thể cần lặp lại
    - Vị trí: Mặt trước-bên đùi
    """)


def render_in_protocol():
    """Intranasal naloxone protocol"""
    st.info("## 💉 Naloxone IN (Qua Mũi)")
    
    st.markdown("""
    **Liều:**
    - **Người Lớn:** 2-4 mg IN (mỗi bên mũi)
    - **Trẻ Em:** 0.1 mg/kg IN (max 4 mg)
    
    **Ưu điểm:**
    - Không cần kim tiêm
    - An toàn cho nhân viên y tế
    - Có thể dùng bởi người không chuyên
    
    **Lưu ý:**
    - Cần thiết bị đặc biệt (atomizer)
    - Tác dụng trong 3-5 phút
    - Có thể cần liều cao hơn
    """)


def render_auto_injector_protocol():
    """Auto-injector naloxone protocol"""
    st.info("## 💉 Naloxone Auto-Injector")
    
    st.markdown("""
    **Liều:**
    - **Evzio:** 0.4 mg IM
    - **Narcan Nasal Spray:** 4 mg IN
    
    **Ưu điểm:**
    - Dễ sử dụng cho người không chuyên
    - An toàn
    - Có thể dùng tại nhà
    
    **Lưu ý:**
    - Cần hướng dẫn sử dụng
    - Có thể cần nhiều liều
    - Vẫn cần gọi cấp cứu
    """)


def render_mild_overdose():
    """Mild overdose protocol"""
    st.success("## 🟢 Ngộ Độc Nhẹ")
    
    st.markdown("""
    **Triệu Chứng:**
    - Buồn ngủ, giảm ý thức nhẹ
    - RR giảm nhẹ (12-16/min)
    - Miosis
    - SpO2 >90%
    
    **Điều Trị:**
    1. **Oxygen:** 100% qua mask
    2. **Naloxone:** 0.4-1 mg IV/IM/IN
    3. **Theo Dõi:** 2 giờ
    
    **Xuất viện:** Có thể sau 2 giờ nếu ổn định
    """)


def render_moderate_overdose():
    """Moderate overdose protocol"""
    st.warning("## 🟡 Ngộ Độc Trung Bình")
    
    st.markdown("""
    **Triệu Chứng:**
    - Giảm ý thức rõ rệt
    - RR 8-12/min
    - Miosis rõ
    - SpO2 85-90%
    
    **Điều Trị:**
    1. **Oxygen:** 100% qua mask
    2. **Bag-mask ventilation:** Nếu cần
    3. **Naloxone:** 1-2 mg IV/IM/IN
    4. **Lặp lại:** Nếu không đáp ứng sau 2-3 phút
    5. **Theo Dõi:** 4 giờ
    
    **Xuất viện:** Sau 4 giờ nếu ổn định
    """)


def render_severe_overdose():
    """Severe overdose protocol"""
    st.error("## 🔴 Ngộ Độc Nặng - ICU")
    
    st.markdown("""
    **Triệu Chứng:**
    - Hôn mê
    - RR <8/min hoặc ngừng thở
    - Miosis rõ
    - SpO2 <85%
    - Có thể có hạ huyết áp
    
    **Điều trị ngay:**
    1. **Airway:**
       - Intubation nếu cần
       - 100% Oxygen
       - Bag-mask ventilation
    
    2. **Naloxone:**
       - 2 mg IV bolus ngay
       - Lặp lại q2-3 phút nếu cần
       - Có thể cần 4-10 mg (fentanyl)
    
    3. **Naloxone truyền tĩnh mạch:**
       - 0.4-2 mg/h
       - Điều chỉnh theo đáp ứng
    
    4. **Hỗ trợ:**
       - Truyền dịch nếu hạ huyết áp
       - Monitor liên tục
    
    5. **Theo Dõi:** 4-6 giờ (nguy cơ Tái Ngộ Độc cao)
    """)


def render_respiratory_arrest():
    """Respiratory arrest protocol"""
    st.error("## ⚫ Ngừng Thở - ACLS + Naloxone")
    
    st.markdown("""
    **Ngừng thở do ngộ độc opioid:**
    
    **1. ACLS Protocol:**
    - CPR ngay lập tức
    - Advanced airway
    - 100% Oxygen
    
    **2. Naloxone:**
    - **Liều cao:** 2-10 mg IV bolus
    - **Lặp lại:** q2-3 phút
    - **Có thể cần:** 10-20 mg nếu fentanyl
    
    **3. Naloxone truyền tĩnh mạch:**
    - 2-10 mg/h
    - Điều chỉnh theo đáp ứng
    
    **4. Hỗ trợ:**
    - Truyền dịch
    - Vasopressor nếu cần
    
    **5. Theo dõi:**
    - ICU monitoring
    - 6-12 giờ (nguy cơ Tái Ngộ Độc rất cao)
    """)

