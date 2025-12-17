"""
Hỗ trợ quyết định (Decision Support)
- Flowcharts quyết định lâm sàng
- An toàn thai kỳ & cho con bú
- Tính liều Nhi khoa
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

# Phase 2 imports
from components.flowchart import render_flowchart
from components.flowcharts.clinical_rules import (
    create_wells_pe_flowchart,
    create_perc_flowchart,
    create_cha2ds2vasc_flowchart,
    create_sepsis_flowchart,
    create_stroke_flowchart,
    create_aki_flowchart,
    create_curb65_flowchart
)
from components.pregnancy_lactation_display import render_pregnancy_lactation_section
from scores.pediatrics.pediatric_dosing import render_pediatric_dosing_calculator

# Standard page setup
setup_page(
    page_title="Hỗ trợ quyết định",
    page_icon="🧭",
    description="Flowcharts, thai kỳ/cho bú, liều Nhi khoa"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📂 Chọn nội dung")
    
    feature_options = [
        "🔄 Flowcharts quyết định lâm sàng",
        "🤰 An toàn thai kỳ & cho con bú",
        "👶 Tính liều Nhi khoa"
    ]
    
    last_feature = st.session_state.get("phase2_feature_selector", feature_options[0])
    default_index = feature_options.index(last_feature) if last_feature in feature_options else 0
    
    selected_feature = st.selectbox(
        "Tính năng:",
        feature_options,
        index=default_index,
        key="phase2_feature_selector"
    )
    
    st.markdown("---")
    st.info("""
    **📚 Hỗ trợ quyết định:**
    
    **🔄 Flowcharts**
    - Quy trình ra quyết định theo bước
    - Trực quan, dễ theo dõi
    
    **🤰 Thai kỳ & cho con bú**
    - Thông tin an toàn theo thai kỳ/cho bú (tóm tắt thực hành)
    
    **👶 Liều Nhi khoa**
    - Tính liều theo cân nặng/BSA
    - Gợi ý liều thường dùng
    """)

# ========== MAIN CONTENT ==========

if selected_feature == feature_options[0]:
    st.header("🔄 Flowcharts quyết định lâm sàng")
    st.caption("Flowcharts tương tác cho các clinical decision rules quan trọng")
    
    # Algorithm selector
    algorithms = {
        "Wells PE Score": create_wells_pe_flowchart,
        "PERC Rule": create_perc_flowchart,
        "CHA₂DS₂-VASc Score": create_cha2ds2vasc_flowchart,
        "Sepsis-3 Protocol": create_sepsis_flowchart,
        "Acute Stroke": create_stroke_flowchart,
        "AKI Diagnostic": create_aki_flowchart,
        "CURB-65": create_curb65_flowchart
    }
    
    selected_algorithm = st.selectbox(
        "Chọn flowchart:",
        list(algorithms.keys()),
        key="algorithm_selector"
    )
    
    st.markdown("---")
    
    # Render flowchart
    if selected_algorithm in algorithms:
        nodes, edges = algorithms[selected_algorithm]()
        
        # Adjust size based on algorithm
        size_map = {
            "Wells PE Score": (900, 700),
            "PERC Rule": (900, 600),
            "CHA₂DS₂-VASc Score": (800, 500),
            "Sepsis-3 Protocol": (900, 700),
            "Acute Stroke": (900, 700),
            "AKI Diagnostic": (800, 600),
            "CURB-65": (800, 500)
        }
        
        width, height = size_map.get(selected_algorithm, (800, 600))
        
        render_flowchart(
            nodes=nodes,
            edges=edges,
            title=f"{selected_algorithm} - Clinical Algorithm",
            width=width,
            height=height,
            interactive=True
        )
        
        # Algorithm description
        st.markdown("---")
        with st.expander("ℹ️ Giải thích Algorithm"):
            if selected_algorithm == "Wells PE Score":
                st.markdown("""
                **Wells PE Score Algorithm:**
                
                1. Tính Wells Score dựa trên các tiêu chí lâm sàng
                2. Phân loại nguy cơ: Thấp (≤4), Trung bình (5-6), Cao (≥7)
                3. Nguy cơ thấp/trung bình → D-dimer
                4. Nguy cơ cao → CTPA trực tiếp
                5. D-dimer (+) → CTPA
                6. D-dimer (-) → Loại trừ PE
                7. CTPA (+) → Điều trị PE
                8. CTPA (-) → Loại trừ PE
                """)
            elif selected_algorithm == "PERC Rule":
                st.markdown("""
                **PERC Rule Algorithm:**
                
                1. Đánh giá 8 tiêu chí PERC
                2. PERC = 0 (tất cả âm) → Loại trừ PE, không cần test
                3. PERC ≥ 1 → Tính Wells Score
                4. Wells ≤ 4 → D-dimer
                5. Wells > 4 → CTPA
                6. D-dimer (+) → CTPA
                7. D-dimer (-) → Loại trừ PE
                """)
            elif selected_algorithm == "CHA₂DS₂-VASc Score":
                st.markdown("""
                **CHA₂DS₂-VASc Score Algorithm:**
                
                1. Tính CHA₂DS₂-VASc Score
                2. Score = 0 (Nam) → Không kháng đông
                3. Score = 1 (Nam) → Cân nhắc kháng đông
                4. Score ≥ 2 → Tính HAS-BLED → Khuyến cáo kháng đông
                """)
            elif selected_algorithm == "Sepsis-3 Protocol":
                st.markdown("""
                **Sepsis-3 Protocol:**
                
                1. Nghi ngờ nhiễm trùng
                2. Tính qSOFA (screening)
                3. qSOFA ≥ 2 → Tính SOFA
                4. qSOFA < 2 → Nguy cơ thấp
                5. SOFA ≥ 2 → SEPSIS
                6. Septic Shock? → 1-Hour Bundle
                7. Theo dõi
                """)
            elif selected_algorithm == "Acute Stroke":
                st.markdown("""
                **Acute Stroke Algorithm:**
                
                1. Đột quỵ cấp
                2. Thời gian khởi phát?
                3. < 4.5h → tPA
                4. 4.5-24h → Thrombectomy
                5. > 24h → Điều trị hỗ trợ
                6. CT não → ICH?
                7. Không ICH → tPA/Thrombectomy
                8. Có ICH → Điều trị hỗ trợ
                """)
            elif selected_algorithm == "AKI Diagnostic":
                st.markdown("""
                **AKI Diagnostic Algorithm:**
                
                1. Nghi ngờ AKI
                2. Phân loại AKI (KDIGO Stage 1, 2, 3)
                3. Tính FENa
                4. FENa < 1% → Prerenal
                5. FENa > 2% → Intrinsic Renal
                6. Check obstruction → Postrenal
                7. Điều trị theo nguyên nhân
                """)
            elif selected_algorithm == "CURB-65":
                st.markdown("""
                **CURB-65 Algorithm:**
                
                1. Viêm phổi cộng đồng
                2. Tính CURB-65 Score
                3. Score 0 → Điều trị ngoại trú
                4. Score 1-2 → Nhập viện
                5. Score 3-5 → ICU
                """)

elif selected_feature == feature_options[1]:
    st.header("🤰 An toàn thai kỳ & cho con bú")
    st.caption("Thông tin an toàn thai kỳ và cho con bú cho thuốc")
    
    # Drug search
    from drugs.pregnancy_lactation_safety import PREGNANCY_SAFETY, LACTATION_SAFETY
    
    all_drugs = sorted(set(list(PREGNANCY_SAFETY.keys()) + list(LACTATION_SAFETY.keys())))
    
    selected_drug = st.selectbox(
        "Chọn thuốc:",
        all_drugs,
        key="pregnancy_drug_selector"
    )
    
    if selected_drug:
        render_pregnancy_lactation_section(selected_drug)
    
    # Add new drug form
    st.markdown("---")
    with st.expander("➕ Thêm thuốc mới (Admin)"):
        st.info("💡 Tính năng này sẽ được mở rộng để thêm thuốc mới vào database.")

elif selected_feature == feature_options[2]:
    render_pediatric_dosing_calculator()

# Footer
render_standard_footer()

