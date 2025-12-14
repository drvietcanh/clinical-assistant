"""
CHA₂DS₂-VASc Score Calculator
Stroke risk assessment in atrial fibrillation
"""

import streamlit as st
from scores.references_config import get_references
from components.references import render_references_section


def render():
    """CHA₂DS₂-VASc Score Calculator"""
    st.subheader("❤️ CHA₂DS₂-VASc Score")
    st.caption("Đánh giá Nguy cơ Đột Quỵ Trong Rung Nhĩ")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
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
                st.markdown("### 📊 Kết quả")
                
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
            
            st.markdown("### 💡 Giải thích & Khuyến cáo")
            st.markdown(f"**Nguy cơ đột quỵ hàng năm:** {risk}")
            
            st.markdown("**Chi tiết điểm:**")
            if details:
                for detail in details:
                    st.write(f"- {detail}")
            else:
                st.write("- Không có yếu tố nguy cơ")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến cáo điều trị")
            
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
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            
            # Prepare inputs for export
            inputs_dict = {
                "CHF": "Có" if chf else "Không",
                "Hypertension": "Có" if htn else "Không",
                "Age Group": age_group,
                "Diabetes": "Có" if dm else "Không",
                "Stroke/TIA": "Có" if stroke else "Không",
                "Vascular Disease": "Có" if vasc else "Không",
                "Sex": sex
            }
            
            # Prepare results for export
            results_dict = {
                "CHA₂DS₂-VASc Score": f"{score} điểm",
                "Stroke Risk": risk,
                "Risk Level": "THẤP" if score == 0 else "TRUNG BÌNH" if score == 1 else "CAO",
                "Details": "\n".join(details) if details else "Không có yếu tố nguy cơ"
            }
            
            render_export_section(
                title=f"CHA₂DS₂-VASc = {score} điểm",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="CHA₂DS₂-VASc Score",
                filename="cha2ds2vasc_result"
            )
            
            # References section
            references = get_references("CHA2DS2-VASc")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
    
    # Always show references at the bottom (even before calculation)
    references = get_references("CHA2DS2-VASc")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

