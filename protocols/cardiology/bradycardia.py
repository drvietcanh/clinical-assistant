"""
Bradycardia Protocol
AHA/ACC Guidelines
Management of symptomatic bradycardia
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Bradycardia Protocol"""
    st.subheader("💔 Nhịp chậm (Bradycardia)")
    st.caption("AHA/ACC Guidelines - Symptomatic bradycardia management")
    
    st.error("""
    **⚠️ NHỊP CHẬM CÓ TRIỆU CHỨNG = CẤP CỨU Y TẾ**
    
    **Định nghĩa:**
    - Nhịp tim <60 bpm
    - **Có triệu chứng:** Chóng mặt, ngất, khó thở, đau ngực, mệt mỏi
    - **Không có triệu chứng:** Có thể bình thường (vận động viên)
    
    **Nguyên nhân:**
    - Bệnh nút xoang (sick sinus syndrome)
    - Block nhĩ thất (AV block)
    - Thuốc (beta-blockers, calcium channel blockers, digoxin)
    - Nhồi máu cơ tim
    - Tăng áp lực nội sọ
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLASSIFICATION ==========
    st.markdown("### 📋 Phân loại")
    
    st.markdown("#### **1. Bệnh nút xoang (Sinus Node Dysfunction)**")
    
    st.info("""
    **Triệu chứng:**
    - Nhịp xoang chậm (<60 bpm)
    - Ngừng xoang (sinus pause >3 giây)
    - Nhịp chậm-xen kẽ-nhanh (bradycardia-tachycardia syndrome)
    
    **Nguyên nhân:**
    - Lão hóa
    - Bệnh tim thiếu máu cục bộ
    - Thuốc
    """)
    
    st.markdown("---")
    
    st.markdown("#### **2. Block nhĩ thất (AV Block)**")
    
    st.warning("""
    **Độ I:**
    - PR kéo dài >200 ms
    - Tất cả xung động dẫn truyền
    - Thường không triệu chứng
    
    **Độ II - Mobitz I (Wenckebach):**
    - PR kéo dài dần, sau đó mất QRS
    - Thường ở nút AV
    - Có thể không triệu chứng
    
    **Độ II - Mobitz II:**
    - PR không đổi, đột ngột mất QRS
    - Thường ở dưới nút AV
    - Có thể tiến triển thành độ III
    
    **Độ III (Complete Heart Block):**
    - Nhĩ và thất đập độc lập
    - Nhịp thất thường chậm (30-50 bpm)
    - Có triệu chứng, cần điều trị
    """)
    
    st.markdown("---")
    
    # ========== SECTION 2: IMMEDIATE MANAGEMENT ==========
    st.markdown("### 🚨 Xử trí ngay lập tức")
    
    st.error("""
    **1. ABC:**
    - Đảm bảo đường thở
    - Oxygen nếu cần
    - Monitor: ECG, BP, SpO2
    
    **2. Đánh giá triệu chứng:**
    - **Có triệu chứng:** Điều trị ngay
    - **Không triệu chứng:** Theo dõi
    
    **3. Điều trị tức thì:**
    - **Atropine:** 0.5-1 mg IV (có thể lặp lại, tối đa 3 mg)
    - **Hoặc:** Transcutaneous pacing (TCP)
    - **Hoặc:** Dopamine: 2-20 mcg/kg/min
    - **Hoặc:** Epinephrine: 2-10 mcg/min
    """)
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.markdown("#### **1. Điều trị tức thì (Nếu có triệu chứng)**")
    
    st.success("""
    **A. Atropine:**
    - **Liều:** 0.5-1 mg IV
    - **Lặp lại:** Mỗi 3-5 phút nếu cần (tối đa 3 mg)
    - **Lưu ý:** Không hiệu quả trong block AV độ II Mobitz II hoặc độ III
    - **Chống chỉ định:** Glaucoma góc đóng
    
    **B. Transcutaneous Pacing (TCP):**
    - **Chỉ định:** Không đáp ứng atropine hoặc block AV độ III
    - **Tần số:** 60-80 bpm
    - **Cường độ:** Tăng đến khi có capture
    
    **C. Dopamine:**
    - **Liều:** 2-20 mcg/kg/min IV
    - **Lưu ý:** Tăng dần đến khi có đáp ứng
    
    **D. Epinephrine:**
    - **Liều:** 2-10 mcg/min IV
    - **Lưu ý:** Nếu không có dopamine
    """)
    
    st.markdown("---")
    
    st.markdown("#### **2. Điều trị lâu dài**")
    
    st.warning("""
    **A. Đặt máy tạo nhịp (Pacemaker):**
    
    **Chỉ định:**
    - Block AV độ III có triệu chứng
    - Block AV độ II Mobitz II
    - Bệnh nút xoang có triệu chứng
    - Nhịp chậm sau nhồi máu cơ tim
    
    **Loại máy:**
    - **Tạm thời:** Qua tĩnh mạch (temporary transvenous pacing)
    - **Vĩnh viễn:** DDD, VVI, tùy chỉnh
    
    **B. Điều chỉnh thuốc:**
    - Giảm liều hoặc ngừng thuốc gây nhịp chậm
    - Beta-blockers, calcium channel blockers, digoxin
    
    **C. Điều trị nguyên nhân:**
    - Nhồi máu cơ tim
    - Tăng áp lực nội sọ
    - Rối loạn điện giải
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: SPECIAL SITUATIONS ==========
    st.markdown("### 🔍 Tình huống đặc biệt")
    
    st.markdown("#### **Nhồi máu cơ tim**")
    
    st.error("""
    **Block AV trong MI:**
    - **MI thành dưới:** Block AV độ I/II thường tự hết
    - **MI thành trước:** Block AV độ III cần đặt máy tạo nhịp ngay
    
    **Điều trị:**
    - Atropine: Có thể dùng
    - TCP: Nếu cần
    - Đặt máy tạo nhịp: Nếu block độ III
    """)
    
    st.markdown("---")
    
    st.markdown("#### **Thuốc gây nhịp chậm**")
    
    st.info("""
    **Thuốc thường gặp:**
    - Beta-blockers
    - Calcium channel blockers (verapamil, diltiazem)
    - Digoxin
    - Amiodarone
    
    **Điều trị:**
    - Ngừng thuốc
    - Atropine nếu có triệu chứng
    - Đặt máy tạo nhịp nếu cần
    - Điều trị quá liều (nếu có)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Cần theo dõi:**
    - **ECG:** Liên tục
    - **Dấu hiệu sinh tồn:** Mỗi 15-30 phút
    - **Triệu chứng:** Chóng mặt, ngất, khó thở
    - **Máy tạo nhịp:** Nếu có (capture, sensing)
    
    **Dấu hiệu cải thiện:**
    - Tăng nhịp tim
    - Hết triệu chứng
    - Cải thiện huyết động
    
    **Dấu hiệu xấu đi:**
    - Nhịp chậm hơn
    - Triệu chứng nặng hơn
    - Huyết động không ổn định
    - Cần đặt máy tạo nhịp
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: REFERENCES ==========
    references = get_references("Bradycardia")
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
        1. **AHA/ACC/HRS Guidelines** - Bradycardia and Cardiac Conduction Delay (2018)
        2. **UpToDate:** Approach to the patient with bradycardia - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

