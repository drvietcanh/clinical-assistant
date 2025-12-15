"""
Tachycardia Protocol
AHA/ACC Guidelines
Management of tachyarrhythmias
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Tachycardia Protocol"""
    st.subheader("💔 Nhịp nhanh (Tachycardia)")
    st.caption("AHA/ACC Guidelines - Tachyarrhythmia management")
    
    st.error("""
    **⚠️ NHỊP NHANH CÓ TRIỆU CHỨNG = CẤP CỨU Y TẾ**
    
    **Định nghĩa:**
    - Nhịp tim >100 bpm
    - **Có triệu chứng:** Chóng mặt, ngất, khó thở, đau ngực, huyết động không ổn định
    - **Phân loại:** Nhịp nhanh trên thất (SVT) hoặc nhịp nhanh thất (VT)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLASSIFICATION ==========
    st.markdown("### 📋 Phân loại")
    
    st.markdown("#### **1. Nhịp nhanh trên thất (SVT)**")
    
    st.info("""
    **Phân loại:**
    - **Nhịp nhanh xoang:** Nhịp xoang >100 bpm (thường do sốt, đau, lo âu)
    - **Nhịp nhanh nhĩ (AT):** Nhịp nhĩ >100 bpm, P wave bất thường
    - **Rung nhĩ (AF):** Nhịp nhĩ không đều, không có P wave rõ
    - **Cuồng nhĩ (AFL):** Sóng flutter đặc trưng
    - **Nhịp nhanh vào lại nút nhĩ thất (AVNRT):** Phổ biến nhất
    - **Nhịp nhanh vào lại nhĩ thất (AVRT):** Có đường phụ (WPW)
    
    **Đặc điểm ECG:**
    - QRS hẹp (<120 ms) - thường
    - Nhịp đều (trừ AF)
    - Tần số: 150-250 bpm
    """)
    
    st.markdown("---")
    
    st.markdown("#### **2. Nhịp nhanh thất (VT)**")
    
    st.warning("""
    **Phân loại:**
    - **VT không bền bỉ (NSVT):** <30 giây, tự hết
    - **VT bền bỉ:** ≥30 giây hoặc cần chuyển nhịp
    - **VT đa hình:** QRS thay đổi hình dạng
    - **Rung thất (VF):** Rối loạn nhịp thất, không có QRS
    
    **Đặc điểm ECG:**
    - QRS rộng (>120 ms)
    - Nhịp thường đều
    - Tần số: 100-250 bpm
    - AV dissociation (phân ly nhĩ thất)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 2: IMMEDIATE MANAGEMENT ==========
    st.markdown("### 🚨 Xử trí ngay lập tức")
    
    st.error("""
    **1. Đánh giá huyết động:**
    - **Ổn định:** Có thể dùng thuốc
    - **Không ổn định:** Sốc điện ngay
    
    **2. ABC:**
    - Đảm bảo đường thở
    - Oxygen nếu cần
    - Monitor: ECG, BP, SpO2
    
    **3. Sốc điện (Nếu không ổn định):**
    - **SVT:** 50-100 J (synchronized)
    - **VT/VF:** 120-200 J (defibrillation)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 3: SVT TREATMENT ==========
    st.markdown("### 💊 Điều trị SVT (Nếu huyết động ổn định)")
    
    st.success("""
    **Bước 1: Vagal Maneuvers:**
    - Valsalva maneuver
    - Massage xoang cảnh (cẩn thận nếu có bệnh mạch máu)
    - Nhúng mặt vào nước lạnh
    
    **Bước 2: Adenosine:**
    - **Liều:** 6 mg IV bolus nhanh, sau đó 12 mg nếu cần
    - **Lưu ý:** Tác dụng ngắn, có thể gây ngừng tim tạm thời
    - **Chống chỉ định:** WPW với AF, hen nặng
    
    **Bước 3: Nếu không đáp ứng:**
    - **Verapamil:** 2.5-5 mg IV (có thể lặp lại)
    - **Hoặc:** Diltiazem: 0.25 mg/kg IV
    - **Hoặc:** Beta-blockers: Metoprolol 2.5-5 mg IV
    
    **Bước 4: Nếu vẫn không đáp ứng:**
    - Sốc điện đồng bộ
    - Hoặc Amiodarone: 150 mg IV trong 10 phút
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: VT TREATMENT ==========
    st.markdown("### 💊 Điều trị VT")
    
    st.warning("""
    **VT không ổn định:**
    - **Sốc điện ngay:** 120-200 J (defibrillation)
    - Sau đó: CPR nếu cần
    
    **VT ổn định:**
    - **Amiodarone:** 150 mg IV trong 10 phút, sau đó 1 mg/min
    - **Hoặc:** Lidocaine: 1-1.5 mg/kg IV, sau đó 0.5-0.75 mg/kg q5-10 phút
    - **Hoặc:** Procainamide: 20-50 mg/min IV (tối đa 17 mg/kg)
    - **Hoặc:** Sotalol: 1.5 mg/kg IV trong 5 phút
    
    **VT đa hình:**
    - Điều trị như VF
    - Sốc điện
    - Amiodarone hoặc Lidocaine
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: ATRIAL FIBRILLATION ==========
    st.markdown("### 💊 Điều trị Rung nhĩ (AF)")
    
    st.info("""
    **AF mới khởi phát (<48 giờ):**
    - **Chuyển nhịp:** Sốc điện đồng bộ hoặc thuốc
    - **Thuốc:** Flecainide, Propafenone, Amiodarone
    - **Chống đông:** Heparin trước chuyển nhịp
    
    **AF kéo dài (>48 giờ):**
    - **Kiểm soát tần số:** Beta-blockers, Calcium channel blockers, Digoxin
    - **Chống đông:** Warfarin hoặc DOACs (dựa trên CHA2DS2-VASc)
    - **Chuyển nhịp:** Sau 3 tuần chống đông hoặc TEE
    
    **AF với WPW:**
    - **Tránh:** Digoxin, Verapamil, Diltiazem
    - **Dùng:** Procainamide, Amiodarone
    - **Hoặc:** Sốc điện
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Cần theo dõi:**
    - **ECG:** Liên tục
    - **Dấu hiệu sinh tồn:** Mỗi 15-30 phút
    - **Triệu chứng:** Chóng mặt, ngất, khó thở, đau ngực
    - **Huyết động:** BP, tưới máu
    
    **Dấu hiệu cải thiện:**
    - Chuyển về nhịp xoang
    - Hết triệu chứng
    - Cải thiện huyết động
    
    **Dấu hiệu xấu đi:**
    - Nhịp nhanh hơn
    - Triệu chứng nặng hơn
    - Huyết động không ổn định
    - Cần sốc điện
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: REFERENCES ==========
    references = get_references("Tachycardia")
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
        1. **AHA/ACC/HRS Guidelines** - Management of Patients With Atrial Fibrillation (2019)
        2. **AHA Guidelines** - Advanced Cardiac Life Support (2020)
        3. **UpToDate:** Approach to the patient with tachycardia - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

