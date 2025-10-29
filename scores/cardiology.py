"""
Cardiology Scoring Systems
All cardiac risk calculators in one module
"""

import streamlit as st


def render_cha2ds2vasc():
    """CHA₂DS₂-VASc Score Calculator"""
    st.subheader("❤️ CHA₂DS₂-VASc Score")
    st.caption("Đánh Giá Nguy Cơ Đột Quỵ Trong Rung Nhĩ")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu Chí Đánh Giá")
        
        chf = st.checkbox(
            "**C** - Suy tim sung huyết / Rối loạn chức năng thất trái",
            help="Tiền sử suy tim hoặc EF <40%"
        )
        
        htn = st.checkbox(
            "**H** - Tăng huyết áp",
            help="Đang điều trị tăng huyết áp hoặc BP >140/90 mmHg"
        )
        
        age_group = st.radio(
            "**A** - Tuổi",
            ["< 65 tuổi", "65-74 tuổi", "≥ 75 tuổi"],
            horizontal=True
        )
        
        dm = st.checkbox(
            "**D** - Đái tháo đường",
            help="Đang điều trị hoặc HbA1c ≥6.5%"
        )
        
        stroke = st.checkbox(
            "**S** - Tiền sử Đột quỵ / TIA / Huyết khối",
            help="Đột quỵ, TIA hoặc tắc mạch hệ thống trước đây"
        )
        
        vasc = st.checkbox(
            "**V** - Bệnh mạch máu",
            help="Nhồi máu cơ tim, bệnh động mạch ngoại biên, plaque động mạch chủ"
        )
        
        sex = st.radio(
            "**Sc** - Giới tính",
            ["Nam", "Nữ"],
            horizontal=True
        )
        
        if st.button("🧮 Tính Điểm", type="primary", key="cha2ds2vasc_calc"):
            score = 0
            details = []
            
            if chf:
                score += 1
                details.append("✓ Suy tim (+1)")
            if htn:
                score += 1
                details.append("✓ Tăng huyết áp (+1)")
            if age_group == "65-74 tuổi":
                score += 1
                details.append("✓ Tuổi 65-74 (+1)")
            elif age_group == "≥ 75 tuổi":
                score += 2
                details.append("✓ Tuổi ≥75 (+2)")
            if dm:
                score += 1
                details.append("✓ Đái tháo đường (+1)")
            if stroke:
                score += 2
                details.append("✓ Tiền sử đột quỵ/TIA (+2)")
            if vasc:
                score += 1
                details.append("✓ Bệnh mạch máu (+1)")
            if sex == "Nữ":
                score += 1
                details.append("✓ Giới tính nữ (+1)")
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if score == 0:
                    st.success(f"## CHA₂DS₂-VASc = {score}")
                    st.success("✅ Nguy cơ THẤP")
                    risk = "0-0.2%/năm"
                elif score == 1:
                    st.warning(f"## CHA₂DS₂-VASc = {score}")
                    st.warning("⚡ Nguy cơ TRUNG BÌNH")
                    risk = "0.6-2.0%/năm"
                elif score == 2:
                    st.warning(f"## CHA₂DS₂-VASc = {score}")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH-CAO")
                    risk = "2.2%/năm"
                else:
                    st.error(f"## CHA₂DS₂-VASc = {score}")
                    st.error("🚨 Nguy cơ CAO")
                    if score <= 5:
                        risk = f"{2.2 + (score-2)*1.5:.1f}%/năm"
                    else:
                        risk = ">10%/năm"
            
            st.markdown("### 💡 Giải Thích & Khuyến Cáo")
            st.markdown(f"**Nguy cơ đột quỵ hàng năm:** {risk}")
            
            st.markdown("**Chi tiết điểm:**")
            if details:
                for detail in details:
                    st.write(f"- {detail}")
            else:
                st.write("- Không có yếu tố nguy cơ")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo Điều Trị")
            
            if score == 0 and sex == "Nam":
                st.info("""
                **Không cần kháng đông** (hoặc có thể dùng Aspirin)
                - Nguy cơ đột quỵ rất thấp
                - Cân nhắc lại định kỳ
                """)
            elif score == 1 and sex == "Nam":
                st.warning("""
                **Cân nhắc kháng đông** (ưu tiên NOAC/Warfarin)
                - Thảo luận với bệnh nhân về lợi ích/nguy cơ
                - Đánh giá nguy cơ chảy máu (HAS-BLED)
                """)
            elif score >= 1:
                st.error("""
                **KHUYẾN CÁO KHÁNG ĐÔNG** (NOAC hoặc Warfarin)
                
                **Lựa chọn ưu tiên:**
                - **NOAC (Kháng đông trực tiếp):**
                  - Apixaban 5mg x 2 lần/ngày
                  - Rivaroxaban 20mg x 1 lần/ngày
                  - Edoxaban 60mg x 1 lần/ngày
                  - Dabigatran 150mg x 2 lần/ngày
                
                - **Warfarin:**
                  - Mục tiêu INR 2.0-3.0
                  - Khi không dùng được NOAC
                
                **Chống chỉ định NOAC:**
                - Suy thận nặng (CrCl <15-30)
                - Bệnh van tim nặng
                - Thai kỳ
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **ESC Guidelines 2020 - Atrial Fibrillation**
                
                **Cách tính điểm:**
                - **C** = Congestive heart failure/LV dysfunction (+1)
                - **H** = Hypertension (+1)
                - **A₂** = Age ≥75 years (+2)
                - **D** = Diabetes mellitus (+1)
                - **S₂** = Prior Stroke/TIA/thromboembolism (+2)
                - **V** = Vascular disease (+1)
                - **A** = Age 65-74 years (+1)
                - **Sc** = Sex category (female) (+1)
                
                **Tổng điểm:** 0-9
                
                **Validation:**
                - Euro Heart Survey on AF
                - Danish National Patient Registry
                
                **Link:**
                - ESC 2020: https://academic.oup.com/eurheartj/article/42/5/373/5899003
                """)


def render_hasbled():
    """HAS-BLED Score Calculator"""
    st.subheader("🩸 HAS-BLED Score")
    st.caption("Đánh Giá Nguy Cơ Chảy Máu Khi Dùng Kháng Đông")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu Chí Đánh Giá")
        
        htn_uncontrolled = st.checkbox(
            "**H** - Tăng huyết áp không kiểm soát",
            help="SBP >160 mmHg"
        )
        
        renal = st.checkbox("Chức năng thận bất thường", help="Lọc cầu thận <60 hoặc chạy thận")
        liver = st.checkbox("Chức năng gan bất thường", help="Xơ gan hoặc men gan tăng >2 lần")
        
        stroke_bled = st.checkbox(
            "**S** - Tiền sử đột quỵ",
            help="Đột quỵ trước đây"
        )
        
        bleeding = st.checkbox(
            "**B** - Tiền sử chảy máu hoặc thiểu máu",
            help="Chảy máu nặng hoặc thiểu máu trước đây"
        )
        
        labile_inr = st.checkbox(
            "**L** - INR không ổn định",
            help="TTR <60% nếu dùng warfarin"
        )
        
        age_hasbled = st.checkbox(
            "**E** - Tuổi cao (>65)",
            help="Tuổi >65"
        )
        
        drugs = st.checkbox("Dùng thuốc chống tiểu cầu/NSAID", help="Aspirin, NSAID")
        alcohol = st.checkbox("Lạm dụng rượu", help=">8 đơn vị/tuần")
        
        if st.button("🧮 Tính Điểm HAS-BLED", type="primary", key="hasbled_calc"):
            score = 0
            details = []
            
            if htn_uncontrolled:
                score += 1
                details.append("✓ THA không kiểm soát (+1)")
            if renal:
                score += 1
                details.append("✓ Suy thận (+1)")
            if liver:
                score += 1
                details.append("✓ Suy gan (+1)")
            if stroke_bled:
                score += 1
                details.append("✓ Tiền sử đột quỵ (+1)")
            if bleeding:
                score += 1
                details.append("✓ Tiền sử chảy máu (+1)")
            if labile_inr:
                score += 1
                details.append("✓ INR không ổn định (+1)")
            if age_hasbled:
                score += 1
                details.append("✓ Tuổi >65 (+1)")
            if drugs:
                score += 1
                details.append("✓ Dùng chống tiểu cầu/NSAID (+1)")
            if alcohol:
                score += 1
                details.append("✓ Lạm dụng rượu (+1)")
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if score <= 2:
                    st.success(f"## HAS-BLED = {score}")
                    st.success("✅ Nguy cơ chảy máu THẤP")
                elif score == 3:
                    st.warning(f"## HAS-BLED = {score}")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH")
                else:
                    st.error(f"## HAS-BLED = {score}")
                    st.error("🚨 Nguy cơ chảy máu CAO")
            
            st.markdown("### 💡 Giải Thích")
            
            if details:
                for d in details:
                    st.write(f"- {d}")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo")
            
            if score <= 2:
                st.success("""
                **Nguy cơ chảy máu chấp nhận được**
                - Có thể dùng kháng đông an toàn
                - Theo dõi định kỳ
                """)
            elif score == 3:
                st.warning("""
                **Cẩn thận khi dùng kháng đông**
                - Kiểm soát các yếu tố nguy cơ có thể sửa
                - Theo dõi sát hơn
                - Cân nhắc NOAC thay vì warfarin
                """)
            else:
                st.error("""
                **Nguy cơ chảy máu cao - Thận trọng!**
                
                **KHÔNG PHẢI CHỐNG CHỈ ĐỊNH kháng đông!**
                
                **Cần làm:**
                - Kiểm soát THA tốt hơn
                - Ngừng NSAID/aspirin nếu được
                - Giảm rượu
                - Cân nhắc dùng PPI bảo vệ dạ dày
                - Ưu tiên NOAC hơn warfarin
                - Theo dõi sát sao
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **HAS-BLED Score**
                
                **Tiêu chí (1 điểm mỗi mục):**
                - **H**: Hypertension (SBP >160 mmHg)
                - **A**: Abnormal renal/liver function (1-2 điểm)
                - **S**: Stroke (tiền sử đột quỵ)
                - **B**: Bleeding history/predisposition
                - **L**: Labile INR (TTR <60%)
                - **E**: Elderly (>65 tuổi)
                - **D**: Drugs (antiplatelet/NSAID) or Alcohol
                
                **Giải thích:**
                - 0-2: Nguy cơ chảy máu thấp
                - ≥3: Nguy cơ cao (cần thận trọng, KHÔNG chống chỉ định)
                
                **Reference:**
                Pisters R, et al. Chest. 2010;138(5):1093-1100.
                """)


def render_score2():
    """SCORE2 Calculator"""
    st.subheader("📊 SCORE2 - ESC 2021")
    st.caption("Đánh Giá Nguy Cơ Bệnh Tim Mạch 10 Năm (40-69 tuổi)")
    
    st.info("""
    **SCORE2 dự đoán nguy cơ 10 năm mắc:**
    - Nhồi máu cơ tim (tử vong + không tử vong)
    - Đột quỵ (tử vong + không tử vong)
    """)
    
    st.warning("🚧 **Đang phát triển** - Sẽ sớm hoàn thành với đầy đủ tính năng chuyển đổi đơn vị!")


def render_score2_op():
    """SCORE2-OP Calculator"""
    st.subheader("👴 SCORE2-OP - ESC 2021")
    st.caption("Đánh Giá Nguy Cơ Tim Mạch Ở Người Cao Tuổi (≥70 tuổi)")
    
    st.info("""
    **SCORE2-OP (Older Persons) dành cho người ≥70 tuổi**
    
    Dự đoán nguy cơ 5-10 năm mắc bệnh tim mạch.
    """)
    
    st.warning("🚧 **Đang phát triển** - Sẽ sớm hoàn thành!")


def render_heart_score():
    """HEART Score Calculator"""
    st.subheader("❤️ HEART Score")
    st.caption("Đánh Giá Nguy Cơ ACS Trong Đau Ngực Cấp")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2-3")
    
    st.info("""
    **HEART Score** đang được phát triển.
    
    Sẽ sớm ra mắt với đầy đủ tính năng!
    """)


def render_timi_risk():
    """TIMI Risk Score Calculator"""
    st.subheader("💔 TIMI Risk Score")
    st.caption("Đánh Giá Nguy Cơ Trong ACS")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2-3")


def render_grace_score():
    """GRACE Score Calculator"""
    st.subheader("📊 GRACE Score")
    st.caption("Tiên Lượng ACS")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")


def render_framingham():
    """Framingham Risk Score Calculator"""
    st.subheader("📈 Framingham Risk Score")
    st.caption("Nguy Cơ Tim Mạch 10 Năm")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")


# Router function to call the appropriate calculator
def render_cardiology_calculator(calculator_id):
    """
    Route to the correct cardiology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    calculators = {
        "CHA2DS2-VASc": render_cha2ds2vasc,
        "HAS-BLED": render_hasbled,
        "SCORE2": render_score2,
        "SCORE2-OP": render_score2_op,
        "HEART Score": render_heart_score,
        "TIMI Risk": render_timi_risk,
        "GRACE Score": render_grace_score,
        "Framingham": render_framingham,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")

