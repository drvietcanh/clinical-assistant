"""
Wells Score for Pulmonary Embolism
Đánh giá xác suất tắc mạch phổi
"""

import streamlit as st


def render():
    """Wells PE Score Calculator"""
    st.subheader("🫁 Wells PE Score")
    st.caption("Wells Score - Xác Suất Tắc Mạch Phổi")
    
    st.info("""
    **Wells PE Score** đánh giá xác suất tiền test của tắc mạch phổi (PE).
    
    - Sử dụng kết hợp với D-dimer để quyết định chụp CTPA
    - Validated rộng rãi trong thực hành lâm sàng
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu Chí Lâm Sàng")
        
        # Clinical signs of DVT
        dvt_signs = st.checkbox(
            "**Dấu hiệu lâm sàng của huyết khối tĩnh mạch sâu (DVT)**",
            help="Chân sưng, đau, ấn đau dọc tĩnh mạch (+3 điểm)"
        )
        
        # PE most likely diagnosis
        pe_likely = st.checkbox(
            "**Tắc mạch phổi là chẩn đoán khả năng nhất**",
            help="Không có chẩn đoán khác hợp lý hơn (+3 điểm)"
        )
        
        # Heart rate
        hr = st.number_input(
            "**Nhịp tim** (lần/phút)",
            min_value=0,
            max_value=250,
            value=80,
            step=5,
            help=">100/phút: +1.5 điểm"
        )
        
        # Immobilization/Surgery
        immobilization = st.checkbox(
            "**Nằm bất động ≥3 ngày HOẶC phẫu thuật trong 4 tuần qua**",
            help="+1.5 điểm"
        )
        
        # Previous DVT/PE
        previous_vte = st.checkbox(
            "**Tiền sử DVT hoặc PE**",
            help="+1.5 điểm"
        )
        
        # Hemoptysis
        hemoptysis = st.checkbox(
            "**Ho ra máu**",
            help="+1 điểm"
        )
        
        # Malignancy
        malignancy = st.checkbox(
            "**Ung thư**",
            help="Đang điều trị hoặc điều trị trong 6 tháng qua, hoặc paLiative (+1 điểm)"
        )
        
        st.markdown("---")
        
        if st.button("🧮 Tính Wells PE Score", type="primary", use_container_width=True):
            # Calculate score
            score = 0.0
            details = []
            
            if dvt_signs:
                score += 3.0
                details.append("Dấu hiệu DVT: +3")
            
            if pe_likely:
                score += 3.0
                details.append("PE khả năng nhất: +3")
            
            if hr > 100:
                score += 1.5
                details.append(f"Nhịp tim >100 ({hr}): +1.5")
            
            if immobilization:
                score += 1.5
                details.append("Nằm bất động/Phẫu thuật: +1.5")
            
            if previous_vte:
                score += 1.5
                details.append("Tiền sử DVT/PE: +1.5")
            
            if hemoptysis:
                score += 1.0
                details.append("Ho ra máu: +1")
            
            if malignancy:
                score += 1.0
                details.append("Ung thư: +1")
            
            # Determine probability
            if score < 2:
                probability = "THẤP"
                pe_prevalence = "3.6%"
                color = "success"
                recommendation = "Xét nghiệm D-dimer"
                detail = "D-dimer âm tính → Loại trừ PE (không cần CTPA)"
            elif score <= 6:
                probability = "TRUNG BÌNH"
                pe_prevalence = "20.5%"
                color = "warning"
                recommendation = "Xét nghiệm D-dimer"
                detail = "D-dimer dương tính → Chụp CTPA"
            else:
                probability = "CAO"
                pe_prevalence = "66.7%"
                color = "error"
                recommendation = "Chụp CTPA ngay"
                detail = "Không cần D-dimer - chụp CTPA trực tiếp"
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if color == "success":
                    st.success(f"## Wells Score: {score}")
                    st.success(f"**Xác suất {probability}**")
                elif color == "warning":
                    st.warning(f"## Wells Score: {score}")
                    st.warning(f"**Xác suất {probability}**")
                else:
                    st.error(f"## Wells Score: {score}")
                    st.error(f"**Xác suất {probability}**")
                
                st.markdown(f"""
                **Tỷ lệ PE thực tế:** {pe_prevalence}
                """)
            
            st.markdown("---")
            st.markdown("### 💡 Chi Tiết Tính Điểm")
            
            if details:
                for d in details:
                    st.write(f"• {d}")
            else:
                st.write("• Không có tiêu chí nào (+0)")
            
            st.markdown(f"**Tổng điểm: {score}**")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến cáo xét nghiệm")
            
            if color == "success":
                st.success(f"""
                **Xác suất THẤP (Score <2) - PE: {pe_prevalence}**
                
                **Khuyến cáo:**
                1. ✅ Xét nghiệm **D-dimer**
                2. ❌ **D-dimer âm tính** (<0.5 µg/mL):
                   → **Loại trừ PE** - Không cần CTPA
                   → Tìm chẩn đoán khác
                
                3. ✅ **D-dimer dương tính**:
                   → Chuyển sang xác suất trung bình
                   → Chụp CTPA
                
                **Lưu ý:** D-dimer có độ nhạy cao, độ đặc hiệu thấp
                """)
            elif color == "warning":
                st.warning(f"""
                **Xác suất TRUNG BÌNH (Score 2-6) - PE: {pe_prevalence}**
                
                **Khuyến cáo:**
                1. ✅ Xét nghiệm **D-dimer**
                2. ❌ **D-dimer âm tính** (<0.5 µg/mL):
                   → Xem xét loại trừ PE
                   → Đánh giá lại lâm sàng
                
                3. ✅ **D-dimer dương tính** (≥0.5 µg/mL):
                   → **Chụp CTPA** (CT Pulmonary Angiography)
                   → Hoặc V/Q scan nếu không chụp được CTPA
                
                4. ⚠️ Cân nhắc khởi đầu **heparin** trong khi chờ kết quả nếu:
                   - Bệnh nhân không ổn định
                   - Nguy cơ cao thực sự
                """)
            else:
                st.error(f"""
                **Xác suất CAO (Score >6) - PE: {pe_prevalence}**
                
                **Khuyến cáo:**
                1. 🚨 **Chụp CTPA NGAY** - KHÔNG cần D-dimer
                2. ✅ **Khởi đầu anticoagulation** trong khi chờ:
                   - LMWH (Enoxaparin) SC
                   - Hoặc Heparin IV nếu bệnh nhân nặng
                
                3. ⚠️ Nếu **không ổn định huyết động**:
                   → Xem xét **thrombolysis**
                   → ICU monitoring
                   → Echo đánh giá right heart strain
                
                4. 📋 **Contraindication tuyệt đối với CTPA:**
                   → V/Q scan
                   → Hoặc Echo + Lower extremity doppler
                
                **⚠️ MASSIVE PE - Dấu hiệu nguy hiểm:**
                - Shock (SBP <90 mmHg)
                - Cần vasopressor
                - Cardiac arrest
                → Xem xét thrombolysis ngay!
                """)
            
            st.markdown("---")
            st.markdown("### 🔬 Về D-dimer")
            
            st.info("""
            **D-dimer là gì?**
            - Sản phẩm phân hủy fibrin
            - Tăng trong huyết khối, DIC
            
            **Giá trị ngưỡng:**
            - **<0.5 µg/mL (FEU):** Âm tính
            - **≥0.5 µg/mL:** Dương tính
            - **Age-adjusted:** >50 tuổi: tuổi × 10 ng/mL
            
            **Độ nhạy & đặc hiệu:**
            - **Độ nhạy:** ~95-98% (rất cao)
            - **Độ đặc hiệu:** ~40-50% (thấp)
            
            **Ý nghĩa:**
            - ✅ **D-dimer âm + Wells thấp** → Loại trừ PE an toàn
            - ❌ **D-dimer dương tính** → Không chẩn đoán PE (cần imaging)
            
            **Nguyên nhân D-dimer tăng khác:**
            - Phẫu thuật, chấn thương gần đây
            - Ung thư
            - Thai kỳ
            - Nhiễm trùng, DIC
            - Cao tuổi
            - Nhồi máu cơ tim
            """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown(f"""
                **Wells Score for Pulmonary Embolism**
                
                **Phân tầng nguy cơ:**
                
                | Score | Xác suất | Tỷ lệ PE | Khuyến cáo |
                |-------|----------|----------|------------|
                | <2 | Thấp | 3.6% | D-dimer → nếu (-) loại trừ PE |
                | 2-6 | Trung bình | 20.5% | D-dimer → nếu (+) CTPA |
                | >6 | Cao | 66.7% | CTPA trực tiếp |
                
                **Kết quả của bạn:** {probability} ({score} điểm) - {pe_prevalence} có PE
                
                **Tiêu chí tính điểm:**
                
                | Tiêu chí | Điểm |
                |----------|------|
                | Dấu hiệu lâm sàng DVT | +3.0 |
                | PE là chẩn đoán khả năng nhất | +3.0 |
                | Nhịp tim >100/phút | +1.5 |
                | Nằm bất động ≥3 ngày hoặc phẫu thuật trong 4 tuần | +1.5 |
                | Tiền sử DVT/PE | +1.5 |
                | Ho ra máu | +1.0 |
                | Ung thư (đang điều trị hoặc <6 tháng, hoặc palliative) | +1.0 |
                
                **Simplified Wells (2-tier):**
                - ≤4: PE unlikely (12%)
                - >4: PE likely (37%)
                
                **Ưu điểm:**
                - Đơn giản, nhanh
                - Validated rộng rãi
                - Kết hợp tốt với D-dimer
                - Giảm số lượng CTPA không cần thiết
                
                **Nhược điểm:**
                - Phụ thuộc đánh giá chủ quan ("PE khả năng nhất")
                - Không đánh giá mức độ nặng của PE
                
                **Alternatives:**
                - PERC Rule (Pulmonary Embolism Rule-out Criteria)
                - Geneva Score
                - YEARS Algorithm
                
                **References:**
                1. Wells PS, et al. Derivation of a simple clinical model to categorize patients probability of pulmonary embolism: increasing the models utility with the SimpliRED D-dimer. Thromb Haemost. 2000;83(3):416-420.
                
                2. Van Belle A, et al. Effectiveness of managing suspected pulmonary embolism using an algorithm combining clinical probability, D-dimer testing, and computed tomography. JAMA. 2006;295(2):172-179.
                
                **Guidelines:**
                - ESC Guidelines for PE (2019)
                - ACCP Guidelines (2016)
                - NICE Guidelines (2020)
                """)
            
            st.markdown("---")
            st.warning("""
            ⚠️ **Lưu ý quan trọng:**
            
            - Wells Score CHỈ đánh giá **xác suất tiền test**
            - KHÔNG thay thế imaging để chẩn đoán xác định
            - Luôn kết hợp với **lâm sàng, D-dimer, imaging**
            - Với massive PE/instability → Chẩn đoán và điều trị ngay!
            - Anticoagulation có nguy cơ chảy máu → Đánh giá cẩn thận
            """)


