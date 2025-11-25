"""
Acute Alcohol Withdrawal Protocol
ASAM 2020, CIWA-Ar Protocol
Management of alcohol withdrawal syndrome and delirium tremens
"""

import streamlit as st


def render():
    """Acute Alcohol Withdrawal Protocol"""
    st.subheader("🍺 Cai Rượu Cấp (Alcohol Withdrawal)")
    st.caption("ASAM 2020, CIWA-Ar Protocol - Alcohol withdrawal syndrome management")
    
    st.info("""
    **Hội chứng cai rượu (Alcohol Withdrawal Syndrome):**
    - Xảy ra 6-24 giờ sau khi ngừng uống rượu
    - Triệu chứng: Run tay, lo âu, mất ngủ, buồn nôn
    - Có thể tiến triển thành: Co giật, Ảo giác, Delirium tremens
    
    **Yếu tố nguy cơ:**
    - Uống rượu lâu ngày
    - Uống nhiều rượu
    - Có tiền sử co giật/DT
    - Có bệnh lý kèm theo
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 CIWA-Ar Score (Clinical Institute Withdrawal Assessment)")
    
    st.warning("""
    **CIWA-Ar Score:** Đánh giá mức độ cai rượu (0-67 điểm)
    
    **Các tiêu chí (mỗi tiêu chí 0-7 điểm):**
    1. **Nausea & Vomiting** (Buồn nôn & Nôn)
    2. **Tremor** (Run tay)
    3. **Paroxysmal Sweats** (Vã mồ hôi)
    4. **Anxiety** (Lo âu)
    5. **Agitation** (Kích động)
    6. **Tactile Disturbances** (Rối loạn xúc giác)
    7. **Auditory Disturbances** (Rối loạn thính giác)
    8. **Visual Disturbances** (Rối loạn thị giác)
    9. **Headache** (Đau đầu)
    10. **Orientation** (Định hướng)
    
    **Đánh Giá:**
    - **0-9 điểm:** Nhẹ - Có thể không cần benzodiazepine
    - **10-19 điểm:** Trung bình - Cần benzodiazepine
    - **≥20 điểm:** Nặng - Cần điều trị tích cực
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều Trị Benzodiazepine")
    
    treatment_approach = st.radio(
        "**Phương pháp điều trị:**",
        [
            "Symptom-Triggered (Theo triệu chứng)",
            "Fixed-Schedule (Lịch cố định)",
            "Front-Loading (Tải liều ban đầu)"
        ],
        key="bzd_approach"
    )
    
    st.markdown("---")
    
    if "Symptom" in treatment_approach:
        render_symptom_triggered()
    elif "Fixed" in treatment_approach:
        render_fixed_schedule()
    else:
        render_front_loading()
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân Loại Mức Độ")
    
    severity = st.radio(
        "**Mức độ cai rượu:**",
        ["Nhẹ (Mild)", "Trung bình (Moderate)", "Nặng (Severe)", "Delirium Tremens"],
        key="withdrawal_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_withdrawal()
    elif "Trung bình" in severity:
        render_moderate_withdrawal()
    elif "Nặng" in severity:
        render_severe_withdrawal()
    else:
        render_delirium_tremens()
    
    st.markdown("---")
    
    st.markdown("### 💉 Thuốc Điều Trị")
    
    st.info("""
    **1. Benzodiazepines (Thuốc đầu tay):**
    
    **Lorazepam (Ưu tiên):**
    - **Liều:** 1-4 mg PO/IV q1-4h
    - **Ưu điểm:** Không chuyển hóa qua gan (an toàn cho suy gan)
    - **Dùng khi:** Suy gan, Người Cao Tuổi
    
    **Diazepam:**
    - **Liều:** 5-20 mg PO/IV q1-4h
    - **Ưu điểm:** Tác dụng kéo dài, ít cần lặp lại
    - **Dùng khi:** Chức năng gan bình thường
    
    **Chlordiazepoxide:**
    - **Liều:** 25-100 mg PO q4-6h
    - **Ưu điểm:** Tác dụng kéo dài
    - **Chỉ dùng:** PO, không có IV
    
    **2. Thiamine (Vitamin B1):**
    - **Liều:** 100 mg IV/IM qd x 3-5 ngày
    - **Sau đó:** 100 mg PO qd
    - **Mục đích:** Phòng ngừa Wernicke-Korsakoff
    
    **3. Folate & Multivitamin:**
    - **Folate:** 1 mg PO qd
    - **Multivitamin:** PO qd
    - **Mục đích:** Bổ sung thiếu hụt
    
    **4. Magnesium:**
    - **Liều:** 2-4 g IV nếu thiếu hụt
    - **Mục đích:** Phòng ngừa co giật
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Co Giật (Seizures)")
    
    st.error("""
    **Co giật do cai rượu:**
    - Thường xảy ra 6-48 giờ sau ngừng rượu
    - Thường là co giật toàn thân
    - Có thể tái phát
    
    **Điều Trị:**
    1. **Benzodiazepine:** Lorazepam 2-4 mg IV
    2. **Nếu tái phát:** Phenytoin 15-20 mg/kg IV
    3. **Dự phòng:** Benzodiazepine đủ liều
    
    **Lưu ý:**
    - Co giật thường tự hết
    - Cần điều trị nguyên nhân (cai rượu)
    - Không cần điều trị dài hạn
    """)
    
    st.markdown("---")
    
    st.markdown("### 🚨 Delirium Tremens (DT)")
    
    st.error("""
    **Delirium Tremens:**
    - Xảy ra 48-96 giờ sau ngừng rượu
    - Tỷ lệ tử vong: 5-15% nếu không điều trị
    - Triệu chứng: Sốt, mạch nhanh, tăng huyết áp, rối loạn ý thức, ảo giác
    
    **Điều Trị:**
    1. **Benzodiazepine liều cao:**
       - Lorazepam: 2-4 mg IV q15-30min
       - Hoặc Diazepam: 5-20 mg IV q15-30min
       - Mục tiêu: An thần nhẹ (RASS -2 đến 0)
    
    2. **ICU care:**
       - Monitor liên tục
       - Hỗ trợ hô hấp nếu cần
       - Điều chỉnh điện giải
    
    3. **Haloperidol (nếu cần):**
       - 2-5 mg IV q4-6h
       - Chỉ dùng nếu kích động nặng, không đáp ứng benzodiazepine
    
    4. **Theo Dõi:** 5-7 ngày
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Điều Trị")
    
    checklist_items = [
        "✅ Đánh giá CIWA-Ar score",
        "✅ Bắt đầu benzodiazepine nếu CIWA-Ar ≥10",
        "✅ Thiamine 100 mg IV/IM ngay",
        "✅ Folate & multivitamin",
        "✅ Điều chỉnh điện giải (Mg, K, P)",
        "✅ Monitor dấu hiệu sống",
        "✅ Theo dõi CIWA-Ar q4-6h",
        "✅ Điều chỉnh liều benzodiazepine",
        "✅ Chuẩn bị cho DT nếu nguy cơ cao"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người Cao Tuổi:**
        - Bắt đầu với liều thấp
        - Ưu tiên lorazepam (ít tích lũy)
        - Cẩn thận với hô hấp
        - Theo dõi sát
        
        **Suy gan:**
        - Chỉ dùng lorazepam (không chuyển hóa qua gan)
        - Tránh diazepam, chlordiazepoxide
        - Giảm liều nếu cần
        """)
    
    with col2:
        st.markdown("""
        **Suy thận:**
        - Không cần điều chỉnh liều benzodiazepine
        - Cẩn thận với tích lũy
        - Theo dõi chức năng thận
        
        **Phụ Nữ Có Thai:**
        - Benzodiazepine có thể dùng (nguy cơ thấp)
        - Ưu tiên cứu mẹ
        - Thiamine an toàn
        - Monitor thai nhi
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục Tiêu Điều Trị")
    
    st.success("""
    **Mục Tiêu:**
    - ✅ CIWA-Ar <10 điểm
    - ✅ Không co giật
    - ✅ Không DT
    - ✅ Dấu hiệu sống ổn định
    - ✅ Bổ sung đủ vitamin
    
    **Xuất viện khi:**
    - CIWA-Ar <10 trong 24 giờ
    - Không triệu chứng nặng
    - Có kế hoạch theo dõi
    - Tư vấn về cai rượu
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **ASAM 2020 Guidelines**
       - American Society of Addiction Medicine
    
    2. **CIWA-Ar Protocol**
       - Clinical Institute Withdrawal Assessment for Alcohol
    
    3. **UpToDate:** Alcohol withdrawal
       - Last updated: 2024
    
    4. **Medscape:** Alcohol Withdrawal Management
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_symptom_triggered():
    """Symptom-triggered protocol"""
    st.success("## 🟢 Symptom-Triggered (Theo Triệu Chứng)")
    
    st.markdown("""
    **Chỉ Định:**
    - CIWA-Ar ≥10 điểm
    - Có thể theo dõi sát
    
    **Liều:**
    - **Lorazepam:** 1-4 mg PO/IV khi CIWA-Ar ≥10
    - **Lặp lại:** q1h nếu CIWA-Ar vẫn ≥10
    - **Ngừng:** Khi CIWA-Ar <10
    
    **Ưu điểm:**
    - Ít dùng thuốc hơn
    - Thời gian điều trị ngắn hơn
    - Ít tác dụng phụ
    
    **Nhược điểm:**
    - Cần theo dõi sát
    - Cần nhân viên được đào tạo
    """)


def render_fixed_schedule():
    """Fixed-schedule protocol"""
    st.warning("## 🟡 Fixed-Schedule (Lịch Cố Định)")
    
    st.markdown("""
    **Chỉ Định:**
    - Không thể theo dõi sát
    - CIWA-Ar ≥10
    
    **Liều:**
    - **Ngày 1:** Lorazepam 2 mg PO q6h
    - **Ngày 2:** Lorazepam 1 mg PO q6h
    - **Ngày 3:** Lorazepam 0.5 mg PO q6h
    - **Ngừng:** Sau ngày 3
    
    **Hoặc Diazepam:**
    - **Ngày 1:** 10 mg PO q6h
    - **Ngày 2:** 5 mg PO q6h
    - **Ngày 3:** 2.5 mg PO q6h
    
    **Ưu điểm:**
    - Dễ thực hiện
    - Không cần theo dõi sát
    
    **Nhược điểm:**
    - Có thể dùng quá nhiều hoặc quá ít
    """)


def render_front_loading():
    """Front-loading protocol"""
    st.info("## 🔵 Front-Loading (Tải Liều Ban Đầu)")
    
    st.markdown("""
    **Chỉ Định:**
    - CIWA-Ar ≥20 (nặng)
    - Nguy cơ DT cao
    
    **Liều:**
    - **Lorazepam:** 2-4 mg IV q1h cho đến khi an thần nhẹ
    - **Sau đó:** Giảm dần 25-50% mỗi ngày
    
    **Hoặc Diazepam:**
    - **Liều:** 10-20 mg IV q1h cho đến khi an thần
    - **Sau đó:** Giảm dần
    
    **Ưu điểm:**
    - Kiểm soát nhanh triệu chứng
    - Giảm nguy cơ DT
    
    **Nhược điểm:**
    - Cần monitor sát
    - Có thể quá liều
    """)


def render_mild_withdrawal():
    """Mild withdrawal protocol"""
    st.success("## 🟢 Cai Rượu Nhẹ")
    
    st.markdown("""
    **Triệu Chứng:**
    - CIWA-Ar 0-9 điểm
    - Run tay nhẹ
    - Lo âu nhẹ
    - Không có co giật/DT
    
    **Điều Trị:**
    1. **Theo Dõi:** CIWA-Ar q4-6h
    2. **Thiamine:** 100 mg PO qd
    3. **Folate & multivitamin:** PO qd
    4. **Benzodiazepine:** Chỉ khi CIWA-Ar ≥10
    
    **Xuất viện:** Có thể nếu ổn định
    """)


def render_moderate_withdrawal():
    """Moderate withdrawal protocol"""
    st.warning("## 🟡 Cai Rượu Trung Bình")
    
    st.markdown("""
    **Triệu Chứng:**
    - CIWA-Ar 10-19 điểm
    - Run tay rõ
    - Lo âu, kích động
    - Có thể có buồn nôn
    
    **Điều Trị:**
    1. **Benzodiazepine:**
       - Lorazepam 1-2 mg PO/IV q4-6h
       - Hoặc Diazepam 5-10 mg PO q6h
    
    2. **Thiamine:** 100 mg IV/IM qd
    
    3. **Folate & multivitamin:** PO qd
    
    4. **Theo Dõi:** CIWA-Ar q4-6h
    
    5. **Điều chỉnh liều:** Theo CIWA-Ar
    
    **Xuất viện:** Sau 2-3 ngày nếu ổn định
    """)


def render_severe_withdrawal():
    """Severe withdrawal protocol"""
    st.error("## 🔴 Cai Rượu Nặng - ICU")
    
    st.markdown("""
    **Triệu Chứng:**
    - CIWA-Ar ≥20 điểm
    - Run tay nặng
    - Kích động nặng
    - Có thể có co giật
    - Nguy cơ DT cao
    
    **Điều Trị:**
    1. **Benzodiazepine liều cao:**
       - Lorazepam 2-4 mg IV q1-2h
       - Hoặc Diazepam 10-20 mg IV q1-2h
       - Mục tiêu: An thần nhẹ
    
    2. **Thiamine:** 100 mg IV qd
    
    3. **Folate & multivitamin:** IV/PO
    
    4. **Magnesium:** 2-4 g IV nếu thiếu
    
    5. **ICU monitoring:**
       - Dấu hiệu sống liên tục
       - CIWA-Ar q2-4h
       - Chuẩn bị cho DT
    
    6. **Theo Dõi:** 5-7 ngày
    """)


def render_delirium_tremens():
    """Delirium tremens protocol"""
    st.error("## ⚫ Delirium Tremens - ICU")
    
    st.markdown("""
    **Triệu Chứng:**
    - Sốt, mạch nhanh, tăng huyết áp
    - Rối loạn ý thức
    - Ảo giác (thị giác, thính giác)
    - Kích động nặng
    
    **Điều trị ngay:**
    1. **Benzodiazepine liều cao:**
       - Lorazepam 2-4 mg IV q15-30min
       - Hoặc Diazepam 5-20 mg IV q15-30min
       - Mục tiêu: An thần (RASS -2 đến 0)
       - Có thể cần 50-100 mg/ngày
    
    2. **Haloperidol (nếu cần):**
       - 2-5 mg IV q4-6h
       - Chỉ khi kích động nặng, không đáp ứng benzodiazepine
    
    3. **ICU care:**
       - Intubation nếu cần
       - Monitor liên tục
       - Điều chỉnh điện giải
       - Hạ sốt
    
    4. **Thiamine:** 100 mg IV qd
    
    5. **Theo Dõi:** 5-7 ngày (tỷ lệ tử vong 5-15%)
    """)

