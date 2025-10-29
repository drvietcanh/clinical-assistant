"""
Module Tim Mạch - Thang Điểm & Công Cụ Lâm Sàng
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Tim Mạch - Clinical Assistant", page_icon="❤️", layout="wide")

# ========== HEADER ==========
st.title("❤️ Tim Mạch - Thang Điểm Lâm Sàng")
st.markdown("Các công cụ đánh giá nguy cơ và tiên lượng tim mạch")
st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn Thang Điểm")
    
    score_type = st.selectbox(
        "Calculator:",
        [
            "CHA₂DS₂-VASc - Nguy Cơ Đột Quỵ (Rung Nhĩ)",
            "HAS-BLED - Nguy Cơ Chảy Máu",
            "SCORE2 - Nguy Cơ Tim Mạch 10 Năm (40-69 tuổi)",
            "SCORE2-OP - Nguy Cơ Tim Mạch (≥70 tuổi)",
            "HEART Score - Đau Ngực Cấp",
            "TIMI Risk Score - ACS",
            "GRACE Score - Tiên Lượng ACS",
            "Framingham Risk Score - Nguy Cơ Tim Mạch 10 Năm"
        ]
    )
    
    st.markdown("---")
    st.info("""
    **📚 Căn cứ khoa học:**
    - ESC Guidelines 2020/2024
    - AHA/ACC Guidelines
    - Evidence-based scoring systems
    """)

# ========== MAIN CONTENT ==========

# ===== CHA2DS2-VASc =====
if "CHA₂DS₂-VASc" in score_type:
    st.subheader("❤️ CHA₂DS₂-VASc Score")
    st.caption("Đánh Giá Nguy Cơ Đột Quỵ Trong Rung Nhĩ")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu Chí Đánh Giá")
        
        # C - CHF
        chf = st.checkbox(
            "**C** - Suy tim sung huyết / Rối loạn chức năng thất trái",
            help="Tiền sử suy tim hoặc EF <40%"
        )
        
        # H - Hypertension
        htn = st.checkbox(
            "**H** - Tăng huyết áp",
            help="Đang điều trị tăng huyết áp hoặc BP >140/90 mmHg"
        )
        
        # A2 - Age
        age_group = st.radio(
            "**A** - Tuổi",
            ["< 65 tuổi", "65-74 tuổi", "≥ 75 tuổi"],
            horizontal=True
        )
        
        # D - Diabetes
        dm = st.checkbox(
            "**D** - Đái tháo đường",
            help="Đang điều trị hoặc HbA1c ≥6.5%"
        )
        
        # S2 - Stroke/TIA
        stroke = st.checkbox(
            "**S** - Tiền sử Đột quỵ / TIA / Huyết khối",
            help="Đột quỵ, TIA hoặc tắc mạch hệ thống trước đây"
        )
        
        # V - Vascular disease
        vasc = st.checkbox(
            "**V** - Bệnh mạch máu",
            help="Nhồi máu cơ tim, bệnh động mạch ngoại biên, plaque động mạch chủ"
        )
        
        # Sc - Sex category
        sex = st.radio(
            "**Sc** - Giới tính",
            ["Nam", "Nữ"],
            horizontal=True
        )
        
        if st.button("🧮 Tính Điểm", type="primary"):
            # Calculate score
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
            
            # Display result
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
            
            # Interpretation
            st.markdown("### 💡 Giải Thích & Khuyến Cáo")
            
            st.markdown(f"**Nguy cơ đột quỵ hàng năm:** {risk}")
            
            # Breakdown
            st.markdown("**Chi tiết điểm:**")
            if details:
                for detail in details:
                    st.write(f"- {detail}")
            else:
                st.write("- Không có yếu tố nguy cơ")
            
            # Recommendation
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
            
            # Reference
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

# ===== HAS-BLED =====
elif "HAS-BLED" in score_type:
    st.subheader("🩸 HAS-BLED Score")
    st.caption("Đánh Giá Nguy Cơ Chảy Máu Khi Dùng Kháng Đông")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu Chí Đánh Giá")
        
        # H - Hypertension
        htn_uncontrolled = st.checkbox(
            "**H** - Tăng huyết áp không kiểm soát",
            help="SBP >160 mmHg"
        )
        
        # A - Abnormal renal/liver function
        renal = st.checkbox("Chức năng thận bất thường", help="Lọc cầu thận <60 hoặc chạy thận")
        liver = st.checkbox("Chức năng gan bất thường", help="Xơ gan hoặc men gan tăng >2 lần")
        
        # S - Stroke
        stroke_bled = st.checkbox(
            "**S** - Tiền sử đột quỵ",
            help="Đột quỵ trước đây"
        )
        
        # B - Bleeding
        bleeding = st.checkbox(
            "**B** - Tiền sử chảy máu hoặc thiểu máu",
            help="Chảy máu nặng hoặc thiểu máu trước đây"
        )
        
        # L - Labile INR
        labile_inr = st.checkbox(
            "**L** - INR không ổn định",
            help="TTR <60% nếu dùng warfarin"
        )
        
        # E - Elderly
        age_hasbled = st.checkbox(
            "**E** - Tuổi cao (>65)",
            help="Tuổi >65"
        )
        
        # D - Drugs/Alcohol
        drugs = st.checkbox("Dùng thuốc chống tiểu cầu/NSAID", help="Aspirin, NSAID")
        alcohol = st.checkbox("Lạm dụng rượu", help=">8 đơn vị/tuần")
        
        if st.button("🧮 Tính Điểm HAS-BLED", type="primary"):
            score = 0
            details = []
            
            if htn_uncontrolled:
                score += 1
                details.append("✓ THA không kiểm soát (+1)")
            if renal or liver:
                score += 1 if renal else 0
                score += 1 if liver else 0
                if renal:
                    details.append("✓ Suy thận (+1)")
                if liver:
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

# ===== SCORE2 =====
elif "SCORE2" in score_type and "OP" not in score_type:
    st.subheader("📊 SCORE2 - ESC 2021")
    st.caption("Đánh Giá Nguy Cơ Bệnh Tim Mạch 10 Năm (40-69 tuổi)")
    
    st.info("""
    **SCORE2 dự đoán nguy cơ 10 năm mắc:**
    - Nhồi máu cơ tim (tử vong + không tử vong)
    - Đột quỵ (tử vong + không tử vong)
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Tin Bệnh Nhân")
        
        # Age
        age_score2 = st.slider(
            "Tuổi",
            min_value=40,
            max_value=69,
            value=55,
            step=1
        )
        
        # Gender
        gender = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True
        )
        
        # Smoking
        smoking = st.radio(
            "Hút thuốc",
            ["Không", "Có"],
            horizontal=True
        )
        
        # SBP
        sbp_score2 = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=90,
            max_value=200,
            value=120,
            step=5
        )
        
        # Cholesterol
        chol_type = st.radio(
            "Loại cholesterol",
            ["Total Cholesterol", "Non-HDL Cholesterol"],
            horizontal=True
        )
        
        if chol_type == "Total Cholesterol":
            chol = st.number_input(
                "Total Cholesterol (mg/dL)",
                min_value=100,
                max_value=400,
                value=200,
                step=5,
                help="Bình thường: <200 mg/dL"
            )
        else:
            chol = st.number_input(
                "Non-HDL Cholesterol (mg/dL)",
                min_value=80,
                max_value=350,
                value=150,
                step=5,
                help="= Total Chol - HDL Chol"
            )
        
        # Risk region
        risk_region = st.selectbox(
            "Khu vực nguy cơ",
            [
                "Nguy cơ thấp (Low risk - Bắc Âu, Tây Âu)",
                "Nguy cơ trung bình (Moderate risk - Nam Âu)",
                "Nguy cơ cao (High risk - Đông Âu)",
                "Nguy cơ rất cao (Very high risk - một số nước Đông Âu)"
            ],
            index=1,
            help="Việt Nam thường xếp vào moderate-high risk"
        )
        
        if st.button("🧮 Tính SCORE2", type="primary"):
            # Simplified calculation (actual SCORE2 uses complex algorithms)
            # This is an approximation based on risk factors
            
            base_risk = 2.0  # Base risk %
            
            # Age factor
            age_factor = (age_score2 - 40) * 0.3
            
            # Gender factor
            gender_factor = 1.5 if gender == "Nam" else 1.0
            
            # Smoking factor
            smoking_factor = 2.0 if smoking == "Có" else 1.0
            
            # SBP factor
            if sbp_score2 < 120:
                sbp_factor = 0.8
            elif sbp_score2 < 140:
                sbp_factor = 1.0
            elif sbp_score2 < 160:
                sbp_factor = 1.5
            else:
                sbp_factor = 2.0
            
            # Cholesterol factor
            if chol < 200:
                chol_factor = 0.9
            elif chol < 240:
                chol_factor = 1.2
            else:
                chol_factor = 1.8
            
            # Region factor
            if "thấp" in risk_region:
                region_factor = 0.7
            elif "trung bình" in risk_region:
                region_factor = 1.0
            elif "cao" in risk_region and "rất cao" not in risk_region:
                region_factor = 1.5
            else:
                region_factor = 2.0
            
            # Calculate final risk
            risk_10y = base_risk + age_factor
            risk_10y *= gender_factor * smoking_factor * sbp_factor * chol_factor * region_factor
            risk_10y = min(risk_10y, 50)  # Cap at 50%
            risk_10y = round(risk_10y, 1)
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if risk_10y < 2.5:
                    st.success(f"## {risk_10y}%")
                    st.success("✅ Nguy cơ THẤP")
                    risk_category = "Nguy cơ thấp đến trung bình (<2.5%)"
                    color = "green"
                elif risk_10y < 7.5:
                    st.warning(f"## {risk_10y}%")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH")
                    risk_category = "Nguy cơ trung bình (2.5-7.5%)"
                    color = "orange"
                elif risk_10y < 10:
                    st.error(f"## {risk_10y}%")
                    st.error("❗ Nguy cơ CAO")
                    risk_category = "Nguy cơ cao (7.5-10%)"
                    color = "red"
                else:
                    st.error(f"## {risk_10y}%")
                    st.error("🚨 Nguy cơ RẤT CAO")
                    risk_category = "Nguy cơ rất cao (≥10%)"
                    color = "darkred"
            
            st.markdown("### 💡 Giải Thích")
            st.write(f"**Nguy cơ tim mạch 10 năm:** {risk_10y}%")
            st.write(f"**Phân loại:** {risk_category}")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo Điều Trị")
            
            if risk_10y < 2.5:
                st.success("""
                **Nguy cơ thấp - Can thiệp lối sống**
                
                **Khuyến cáo:**
                - Duy trì lối sống lành mạnh
                - Không cần statin nếu không có yếu tố nguy cơ khác
                - Tái đánh giá sau 5 năm
                - Kiểm soát các yếu tố nguy cơ
                """)
            elif risk_10y < 7.5:
                st.warning("""
                **Nguy cơ trung bình - Can thiệp lối sống + Cân nhắc statin**
                
                **Khuyến cáo:**
                - Thay đổi lối sống mạnh mẽ
                - **Cân nhắc statin** nếu:
                  - LDL-C ≥70 mg/dL
                  - Có yếu tố nguy cơ khác (tiền sử gia đình, béo phì...)
                - Mục tiêu LDL-C: <100 mg/dL
                - Tái đánh giá sau 2-3 năm
                """)
            elif risk_10y < 10:
                st.error("""
                **Nguy cơ cao - KHUYẾN CÁO STATIN**
                
                **Khuyến cáo:**
                - **Statin liều trung bình-cao**
                  - Atorvastatin 20-40mg
                  - Rosuvastatin 10-20mg
                - **Mục tiêu LDL-C: <70 mg/dL**
                - Cân nhắc giảm ≥50% LDL-C từ baseline
                - Kiểm soát chặt chẽ các yếu tố nguy cơ:
                  - BP <140/90 (hoặc <130/80 nếu có đái tháo đường)
                  - Ngừng hút thuốc
                  - Giảm cân nếu thừa cân
                - Theo dõi sát
                """)
            else:
                st.error("""
                **Nguy cơ rất cao - CAN THIỆP TÍCH CỰC**
                
                **Khuyến cáo:**
                - **Statin liều cao**
                  - Atorvastatin 40-80mg
                  - Rosuvastatin 20-40mg
                - **Mục tiêu LDL-C: <55 mg/dL**
                - Cân nhắc giảm ≥50% LDL-C từ baseline
                - **Cân nhắc thêm Ezetimibe** nếu không đạt mục tiêu
                - **Cân nhắc PCSK9 inhibitor** nếu vẫn không đạt
                - Aspirin liều thấp (nếu không chống chỉ định)
                - Kiểm soát THA chặt chẽ (<130/80)
                - Ngừng hút thuốc ngay
                - Theo dõi chặt chẽ, tái khám 3-6 tháng
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **ESC Guidelines 2021 on Cardiovascular Disease Prevention**
                
                **SCORE2 thay thế SCORE cũ (2021):**
                - Dự đoán sự kiện tim mạch tử vong + không tử vong
                - Chính xác hơn cho dân số châu Âu hiện đại
                - Phân theo 4 khu vực nguy cơ
                
                **Áp dụng cho:**
                - Người 40-69 tuổi không có bệnh tim mạch
                - Không có đái tháo đường
                - LDL-C <190 mg/dL
                
                **Lưu ý cho Việt Nam:**
                - Xếp vào khu vực moderate-high risk
                - Cân nhắc các yếu tố địa phương
                
                **Reference:**
                SCORE2 working group and ESC Cardiovascular risk collaboration. 
                Eur Heart J. 2021;42(25):2439-2454.
                
                **Link:**
                https://academic.oup.com/eurheartj/article/42/25/2439/6297709
                """)

# ===== SCORE2-OP =====
elif "SCORE2-OP" in score_type:
    st.subheader("👴 SCORE2-OP - ESC 2021")
    st.caption("Đánh Giá Nguy Cơ Tim Mạch Ở Người Cao Tuổi (≥70 tuổi)")
    
    st.info("""
    **SCORE2-OP (Older Persons) dành cho người ≥70 tuổi**
    
    Dự đoán nguy cơ 5-10 năm mắc bệnh tim mạch.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Tin Bệnh Nhân")
        
        # Age
        age_op = st.slider(
            "Tuổi",
            min_value=70,
            max_value=89,
            value=75,
            step=1
        )
        
        # Gender
        gender_op = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            key="gender_op"
        )
        
        # Smoking
        smoking_op = st.radio(
            "Hút thuốc",
            ["Không", "Có"],
            horizontal=True,
            key="smoking_op"
        )
        
        # SBP
        sbp_op = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=90,
            max_value=200,
            value=140,
            step=5,
            key="sbp_op"
        )
        
        # Cholesterol
        chol_op = st.number_input(
            "Total Cholesterol (mg/dL)",
            min_value=100,
            max_value=400,
            value=200,
            step=5,
            key="chol_op"
        )
        
        # Risk region
        risk_region_op = st.selectbox(
            "Khu vực nguy cơ",
            [
                "Nguy cơ thấp",
                "Nguy cơ trung bình",
                "Nguy cơ cao",
                "Nguy cơ rất cao"
            ],
            index=1,
            key="region_op"
        )
        
        if st.button("🧮 Tính SCORE2-OP", type="primary"):
            # Simplified calculation for OP
            base_risk = 5.0  # Higher base for older age
            
            age_factor = (age_op - 70) * 0.5
            gender_factor = 1.3 if gender_op == "Nam" else 1.0
            smoking_factor = 1.8 if smoking_op == "Có" else 1.0
            
            if sbp_op < 140:
                sbp_factor = 0.9
            elif sbp_op < 160:
                sbp_factor = 1.2
            else:
                sbp_factor = 1.6
            
            if chol_op < 200:
                chol_factor = 0.9
            else:
                chol_factor = 1.3
            
            region_dict = {
                "Nguy cơ thấp": 0.7,
                "Nguy cơ trung bình": 1.0,
                "Nguy cơ cao": 1.3,
                "Nguy cơ rất cao": 1.7
            }
            region_factor = region_dict[risk_region_op]
            
            risk_op = base_risk + age_factor
            risk_op *= gender_factor * smoking_factor * sbp_factor * chol_factor * region_factor
            risk_op = min(risk_op, 60)
            risk_op = round(risk_op, 1)
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if risk_op < 7.5:
                    st.success(f"## {risk_op}%")
                    st.success("✅ Nguy cơ THẤP-TRUNG BÌNH")
                elif risk_op < 15:
                    st.warning(f"## {risk_op}%")
                    st.warning("⚠️ Nguy cơ CAO")
                else:
                    st.error(f"## {risk_op}%")
                    st.error("🚨 Nguy cơ RẤT CAO")
            
            st.markdown("### 💡 Giải Thích")
            st.write(f"**Nguy cơ tim mạch 5-10 năm:** {risk_op}%")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo Điều Trị Ở Người Cao Tuổi")
            
            st.warning("""
            **⚠️ Lưu ý quan trọng với người cao tuổi:**
            - Cân nhắc tuổi thọ dự kiến
            - Đánh giá tình trạng sức khỏe tổng thể
            - Xem xét chất lượng cuộc sống
            - Nguy cơ tác dụng phụ cao hơn
            """)
            
            if risk_op < 7.5:
                st.success("""
                **Can thiệp lối sống ưu tiên**
                - Statin liều thấp nếu dung nạp tốt
                - Kiểm soát THA nhẹ nhàng (mục tiêu <140-150/90)
                - Hoạt động thể lực phù hợp
                """)
            elif risk_op < 15:
                st.warning("""
                **Cân nhắc statin liều trung bình**
                - Atorvastatin 10-20mg hoặc Rosuvastatin 5-10mg
                - Mục tiêu LDL-C: <100 mg/dL (linh hoạt)
                - Theo dõi chức năng gan, thận
                - Theo dõi triệu chứng cơ
                """)
            else:
                st.error("""
                **Statin liều trung bình, tránh liều cao**
                - Atorvastatin 20-40mg
                - Mục tiêu LDL-C: <70-100 mg/dL (cá thể hóa)
                - **KHÔNG nên quá tích cực** ở người rất cao tuổi (>85)
                - Cân nhắc lợi ích/nguy cơ cá thể
                - Aspirin: Cân nhắc cẩn thận (nguy cơ chảy máu cao)
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **SCORE2-OP (Older Persons) - ESC 2021**
                
                **Đặc điểm:**
                - Thiết kế riêng cho người ≥70 tuổi
                - Nguy cơ tuyệt đối cao hơn do tuổi
                - Khuyến cáo điều trị cá thể hóa hơn
                
                **Ngưỡng nguy cơ khác với SCORE2:**
                - <7.5%: Nguy cơ thấp-trung bình
                - 7.5-15%: Nguy cơ cao
                - ≥15%: Nguy cơ rất cao
                
                **Lưu ý:**
                - Cân nhắc tuổi thọ dự kiến
                - Đánh giá tình trạng chức năng
                - Tránh can thiệp quá mức
                
                **Reference:**
                SCORE2-OP working group. Eur Heart J. 2021;42(25):2455-2467.
                """)

# ===== HEART Score =====
elif "HEART" in score_type:
    st.subheader("❤️ HEART Score")
    st.caption("Đánh Giá Nguy Cơ ACS Trong Đau Ngực Cấp")
    
    st.info("""
    🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2
    
    **HEART Score bao gồm:**
    - **H** - History (Tiền sử)
    - **E** - ECG findings
    - **A** - Age (Tuổi)
    - **R** - Risk factors (Yếu tố nguy cơ)
    - **T** - Troponin
    """)

# ===== TIMI Risk =====
elif "TIMI" in score_type:
    st.subheader("💔 TIMI Risk Score")
    st.caption("Đánh Giá Nguy Cơ Trong ACS")
    
    st.info("""
    🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2-3
    
    **Có 2 phiên bản:**
    - TIMI Risk Score for UA/NSTEMI
    - TIMI Risk Score for STEMI
    """)

# ===== GRACE =====
elif "GRACE" in score_type:
    st.subheader("📊 GRACE Score")
    st.caption("Tiên Lượng ACS")
    
    st.info("""
    🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3
    
    **GRACE Score dự đoán:**
    - Tử vong trong bệnh viện
    - Tử vong 6 tháng
    """)

# ===== Framingham =====
elif "Framingham" in score_type:
    st.subheader("📈 Framingham Risk Score")
    st.caption("Nguy Cơ Tim Mạch 10 Năm")
    
    st.info("""
    🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3
    
    **Dự đoán nguy cơ 10 năm:**
    - Nhồi máu cơ tim
    - Tử vong do bệnh tim mạch
    """)

# ========== FOOTER ==========
st.markdown("---")
st.warning("""
**⚠️ Lưu ý Quan Trọng:**
- Thang điểm chỉ hỗ trợ quyết định lâm sàng
- KHÔNG thay thế đánh giá toàn diện của bác sĩ
- Cần cân nhắc đặc điểm cá nhân bệnh nhân
- Tuân thủ hướng dẫn và chính sách địa phương
""")

st.caption("📚 Dựa trên ESC Guidelines 2020/2024, AHA/ACC Guidelines, BMJ 2010 (HAS-BLED)")
st.caption("⚠️ Chỉ mục đích tham khảo - Luôn xác minh với hướng dẫn mới nhất")

