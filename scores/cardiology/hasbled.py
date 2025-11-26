"""
HAS-BLED Score Calculator
Bleeding risk assessment in patients on anticoagulation
"""

import streamlit as st


def render():
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
                st.markdown("### 📊 Kết quả")
                
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
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

