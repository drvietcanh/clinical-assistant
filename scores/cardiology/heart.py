"""
HEART Score Calculator
"""

import streamlit as st


def render():
    """HEART Score Calculator"""
    st.subheader("❤️ HEART Score")
    st.caption("Đánh giá Nguy Cơ ACS Trong Đau Ngực Cấp")
    
    st.info("""
    **HEART Score** dự đoán nguy cơ MACE (Major Adverse Cardiac Events) trong 6 tuần ở bệnh nhân đau ngực cấp.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        # History
        st.markdown("#### H - History (Tiền sử)")
        history_score = st.radio(
            "Đặc điểm đau ngực:",
            [
                "0 - Ít nguy cơ (không điển hình)",
                "1 - Nguy cơ trung bình (hơi điển hình)",
                "2 - Nguy cơ cao (rất điển hình cho ACS)"
            ],
            key="heart_history"
        )
        history = int(history_score[0])
        
        # ECG
        st.markdown("#### E - ECG")
        ecg_score = st.radio(
            "Kết quả ECG:",
            [
                "0 - Bình thường",
                "1 - Bất thường không đặc hiệu (đảo T, ST chênh không đặc hiệu)",
                "2 - ST chênh đặc hiệu (ST chênh ≥1mm hoặc LBBB mới)"
            ],
            key="heart_ecg"
        )
        ecg = int(ecg_score[0])
        
        # Age
        st.markdown("#### A - Age (Tuổi)")
        age_score = st.radio(
            "Nhóm tuổi:",
            [
                "0 - < 45 tuổi",
                "1 - 45-64 tuổi",
                "2 - ≥ 65 tuổi"
            ],
            key="heart_age"
        )
        age = int(age_score[0])
        
        # Risk factors
        st.markdown("#### R - Risk Factors (Yếu tố nguy cơ)")
        st.caption("Đếm số lượng: THA, ĐTĐ, hút thuốc, cholesterol cao, béo phì, tiền sử gia đình")
        
        risk_factors = []
        col_rf1, col_rf2 = st.columns(2)
        with col_rf1:
            if st.checkbox("Tăng huyết áp", key="rf_htn"):
                risk_factors.append("THA")
            if st.checkbox("Đái tháo đường", key="rf_dm"):
                risk_factors.append("ĐTĐ")
            if st.checkbox("Hút thuốc", key="rf_smoke"):
                risk_factors.append("Hút thuốc")
        
        with col_rf2:
            if st.checkbox("Cholesterol cao", key="rf_chol"):
                risk_factors.append("Cholesterol")
            if st.checkbox("Béo phì", key="rf_obesity"):
                risk_factors.append("Béo phì")
            if st.checkbox("Tiền sử gia đình", key="rf_fhx"):
                risk_factors.append("TSGĐ")
        
        if st.checkbox("Tiền sử bệnh mạch vành đã biết", key="rf_cad"):
            risk_factors.append("CAD")
        
        num_rf = len(risk_factors)
        if num_rf == 0 or (num_rf == 1 and "CAD" not in risk_factors):
            risk = 0
        elif num_rf >= 3 or "CAD" in risk_factors:
            risk = 2
        else:
            risk = 1
        
        # Troponin
        st.markdown("#### T - Troponin")
        troponin_score = st.radio(
            "Troponin:",
            [
                "0 - Bình thường (≤ ngưỡng bình thường)",
                "1 - Tăng nhẹ (1-3 lần giới hạn trên)",
                "2 - Tăng cao (> 3 lần giới hạn trên)"
            ],
            key="heart_troponin"
        )
        troponin = int(troponin_score[0])
        
        if st.button("🧮 Tính HEART Score", type="primary", key="heart_calc"):
            total_score = history + ecg + age + risk + troponin
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                if total_score <= 3:
                    st.success(f"## HEART = {total_score}")
                    st.success("✅ Nguy cơ THẤP")
                    mace_risk = "0.9-1.7%"
                    color = "success"
                elif total_score <= 6:
                    st.warning(f"## HEART = {total_score}")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH")
                    mace_risk = "12-16.6%"
                    color = "warning"
                else:
                    st.error(f"## HEART = {total_score}")
                    st.error("🚨 Nguy cơ CAO")
                    mace_risk = "50-65%"
                    color = "error"
            
            st.markdown("### 💡 Chi tiết Điểm")
            st.write(f"- **H** (History): {history} điểm")
            st.write(f"- **E** (ECG): {ecg} điểm")
            st.write(f"- **A** (Age): {age} điểm")
            st.write(f"- **R** (Risk factors): {risk} điểm ({num_rf} yếu tố: {', '.join(risk_factors) if risk_factors else 'Không có'})")
            st.write(f"- **T** (Troponin): {troponin} điểm")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo Xử Trí")
            
            if total_score <= 3:
                st.success("""
                **Nguy cơ MACE thấp ({})** trong 6 tuần
                
                **Khuyến cáo:**
                - ✅ Có thể xuất viện an toàn
                - Theo dõi ngoại trú
                - Giáo dục bệnh nhân về các triệu chứng cần tái khám
                - Kiểm soát yếu tố nguy cơ
                - Cân nhắc stress test ngoại trú
                """.format(mace_risk))
            
            elif total_score <= 6:
                st.warning("""
                **Nguy cơ MACE trung bình ({})** trong 6 tuần
                
                **Khuyến cáo:**
                - ⚠️ Theo dõi tại bệnh viện
                - Serial troponin (0h, 3h, 6h)
                - Cân nhắc stress test hoặc CT coronary angiography
                - Hội chẩn tim mạch
                - Điều trị kháng kết tập tiểu cầu nếu được
                """.format(mace_risk))
            
            else:
                st.error("""
                **Nguy cơ MACE cao ({})** trong 6 tuần
                
                **Khuyến cáo:**
                - 🚨 Nhập viện ngay
                - Xử trí theo protocol ACS
                - DAPT (Aspirin + P2Y12 inhibitor)
                - Anticoagulation (heparin/LMWH)
                - Hội chẩn tim mạch khẩn cấp
                - Cân nhắc can thiệp mạch vành sớm
                - ICU/CCU monitoring
                """.format(mace_risk))
            
            with st.expander("📚 Tài liệu tham khảo"):
                st.markdown("""
                **HEART Score for Major Cardiac Events**
                
                **Components:**
                - **H** = History (0-2)
                - **E** = ECG (0-2)
                - **A** = Age (0-2)
                - **R** = Risk factors (0-2)
                - **T** = Troponin (0-2)
                
                **Total Score: 0-10**
                
                **Risk Stratification:**
                - **0-3**: Low risk (0.9-1.7% MACE)
                - **4-6**: Moderate risk (12-16.6% MACE)
                - **7-10**: High risk (50-65% MACE)
                
                **MACE = Major Adverse Cardiac Events:**
                - AMI (acute myocardial infarction)
                - PCI (percutaneous coronary intervention)
                - CABG (coronary artery bypass grafting)
                - Death
                
                **Validation Studies:**
                - Backus BE et al. Int J Cardiol. 2013;168(3):2153-2158.
                - Six AJ et al. Neth Heart J. 2008;16(6):191-196.
                
                **Link:**
                - Original: https://www.mdcalc.com/heart-score-major-cardiac-events
                """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")
