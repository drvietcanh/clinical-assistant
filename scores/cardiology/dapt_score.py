"""
DAPT Score Calculator
======================

Determines optimal duration of dual antiplatelet therapy (DAPT) after PCI

Reference:
- Yeh RW, et al. Development and validation of a prediction rule for benefit 
  and harm of dual antiplatelet therapy beyond 1 year after percutaneous coronary 
  intervention. JAMA. 2016;315(16):1735-1749.

DAPT Score Components (9 factors):
1. Age ≥75 years (1 point)
2. Age 65-74 years (1 point)
3. Current cigarette smoking (1 point)
4. Diabetes mellitus (1 point)
5. Myocardial infarction at presentation (1 point)
6. Prior PCI or prior MI (1 point)
7. Paclitaxel-eluting stent (1 point)
8. Stent diameter <3 mm (1 point)
9. Congestive heart failure or LVEF <30% (2 points)

Total: 0-9 points

Interpretation:
- ≥2 points: Benefit from extended DAPT (30 months) > Risk
- <2 points: Standard DAPT (12 months) sufficient

Clinical Utility:
- Used daily in cardiology practice
- Guides DAPT duration after PCI
- Balances ischemic benefit vs bleeding risk
- Helps personalize antiplatelet therapy
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_dapt_score(
    age: int,
    current_smoking: bool,
    diabetes: bool,
    mi_at_presentation: bool,
    prior_pci_or_mi: bool,
    paclitaxel_stent: bool,
    stent_diameter_lt_3mm: bool,
    chf_or_lvef_lt_30: bool
) -> dict:
    """
    Calculate DAPT Score
    
    Args:
        age: Age (years)
        current_smoking: Current cigarette smoking
        diabetes: Diabetes mellitus
        mi_at_presentation: MI at presentation
        prior_pci_or_mi: Prior PCI or prior MI
        paclitaxel_stent: Paclitaxel-eluting stent
        stent_diameter_lt_3mm: Stent diameter <3 mm
        chf_or_lvef_lt_30: CHF or LVEF <30%
    
    Returns:
        Dictionary with score and DAPT duration recommendation
    """
    score = 0
    details = []
    
    # Age
    if age >= 75:
        score += 1
        details.append(f"Tuổi ≥75 ({age} tuổi) → +1 điểm")
    elif age >= 65:
        score += 1
        details.append(f"Tuổi 65-74 ({age} tuổi) → +1 điểm")
    else:
        details.append(f"Tuổi <65 ({age} tuổi) → 0 điểm")
    
    # Current smoking
    if current_smoking:
        score += 1
        details.append("Hút thuốc hiện tại → +1 điểm")
    else:
        details.append("Không hút thuốc → 0 điểm")
    
    # Diabetes
    if diabetes:
        score += 1
        details.append("Đái tháo đường → +1 điểm")
    else:
        details.append("Không đái tháo đường → 0 điểm")
    
    # MI at presentation
    if mi_at_presentation:
        score += 1
        details.append("Nhồi máu cơ tim khi nhập viện → +1 điểm")
    else:
        details.append("Không có MI khi nhập viện → 0 điểm")
    
    # Prior PCI or MI
    if prior_pci_or_mi:
        score += 1
        details.append("Tiền sử PCI hoặc MI → +1 điểm")
    else:
        details.append("Không có tiền sử PCI/MI → 0 điểm")
    
    # Paclitaxel stent
    if paclitaxel_stent:
        score += 1
        details.append("Stent phủ paclitaxel → +1 điểm")
    else:
        details.append("Stent không phải paclitaxel → 0 điểm")
    
    # Stent diameter <3 mm
    if stent_diameter_lt_3mm:
        score += 1
        details.append("Đường kính stent <3 mm → +1 điểm")
    else:
        details.append("Đường kính stent ≥3 mm → 0 điểm")
    
    # CHF or LVEF <30%
    if chf_or_lvef_lt_30:
        score += 2
        details.append("Suy tim hoặc LVEF <30% → +2 điểm")
    else:
        details.append("Không suy tim, LVEF ≥30% → 0 điểm")
    
    # Risk stratification
    if score >= 2:
        recommendation = "DAPT kéo dài 30 tháng"
        benefit = "Lợi ích > Nguy cơ"
        risk_class = "EXTENDED"
        color = "success"
    else:
        recommendation = "DAPT tiêu chuẩn 12 tháng"
        benefit = "DAPT 12 tháng đủ"
        risk_class = "STANDARD"
        color = "info"
    
    return {
        'total_score': score,
        'recommendation': recommendation,
        'benefit': benefit,
        'risk_class': risk_class,
        'color': color,
        'details': details
    }


def render():
    """Render DAPT Score calculator"""
    
    st.title("💊 DAPT Score")
    st.markdown("**Thời gian dùng DAPT sau PCI (DÙNG HÀNG NGÀY)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'dapt_score':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **DAPT Score** xác định thời gian tối ưu của DAPT sau PCI:
        - Dùng hàng ngày trong phòng khám tim mạch
        - Cân bằng lợi ích (giảm thiếu máu) vs nguy cơ (chảy máu)
        - Kết hợp với PRECISE-DAPT Score
        
        ### 🎯 9 Yếu tố
        
        1. **Tuổi ≥75** (1 điểm)
        2. **Tuổi 65-74** (1 điểm)
        3. **Hút thuốc hiện tại** (1 điểm)
        4. **Đái tháo đường** (1 điểm)
        5. **MI khi nhập viện** (1 điểm)
        6. **Tiền sử PCI/MI** (1 điểm)
        7. **Stent paclitaxel** (1 điểm)
        8. **Stent <3 mm** (1 điểm)
        9. **Suy tim hoặc LVEF <30%** (2 điểm)
        
        ### 📊 Phân loại
        
        - **≥2 điểm:** Lợi ích > Nguy cơ → DAPT 30 tháng
        - **<2 điểm:** DAPT 12 tháng đủ
        
        ### ⚠️ Lưu ý
        
        - Cần kết hợp với PRECISE-DAPT Score
        - Cân nhắc nguy cơ thiếu máu vs chảy máu
        - Stent thế hệ mới có thể cho phép DAPT ngắn hơn
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="dapt_score",
            calculator_name="DAPT Score",
            category="Tim mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Thông tin Bệnh nhân")
        age = st.number_input("Tuổi", 0, 120, 65, 1, format="%d")
        
        current_smoking = st.checkbox(
            "**Hút thuốc hiện tại**",
            help="Đang hút thuốc lá"
        )
        
        diabetes = st.checkbox(
            "**Đái tháo đường**",
            help="Đái tháo đường type 1 hoặc type 2"
        )
        
        chf_or_lvef_lt_30 = st.checkbox(
            "**Suy tim hoặc LVEF <30%**",
            help="Suy tim hoặc phân suất tống máu <30%"
        )
    
    with col2:
        st.markdown("#### 🏥 Thông tin PCI & Stent")
        mi_at_presentation = st.checkbox(
            "**Nhồi máu cơ tim khi nhập viện**",
            help="MI là chỉ định cho PCI"
        )
        
        prior_pci_or_mi = st.checkbox(
            "**Tiền sử PCI hoặc MI**",
            help="Đã từng PCI hoặc MI trước đó"
        )
        
        paclitaxel_stent = st.checkbox(
            "**Stent phủ paclitaxel**",
            help="Paclitaxel-eluting stent (Taxus)"
        )
        
        stent_diameter_lt_3mm = st.checkbox(
            "**Đường kính stent <3 mm**",
            help="Stent có đường kính <3 mm"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính DAPT Score", type="primary", use_container_width=True):
        result = calculate_dapt_score(
            age=age,
            current_smoking=current_smoking,
            diabetes=diabetes,
            mi_at_presentation=mi_at_presentation,
            prior_pci_or_mi=prior_pci_or_mi,
            paclitaxel_stent=paclitaxel_stent,
            stent_diameter_lt_3mm=stent_diameter_lt_3mm,
            chf_or_lvef_lt_30=chf_or_lvef_lt_30
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                "**DAPT Score**",
                f"{result['total_score']}"
            )
            st.caption(f"Ngưỡng: 2")
        
        with col_r2:
            st.markdown(f"### {result['recommendation']}")
            st.caption(f"{result['benefit']}")
        
        # Score breakdown
        with st.expander("📋 Chi tiết điểm số", expanded=True):
            for detail in result['details']:
                st.markdown(f"- {detail}")
            st.markdown(f"**Tổng điểm: {result['total_score']}**")
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Diễn giải")
        
        if result['risk_class'] == "EXTENDED":
            st.success(f"""
            **✅ DAPT KÉO DÀI 30 THÁNG (Score = {result['total_score']} ≥ 2):**
            
            **Khuyến cáo:**
            - **DAPT kéo dài 30 tháng** (sau 12 tháng tiêu chuẩn)
            - Lợi ích giảm thiếu máu > Nguy cơ chảy máu
            - Aspirin + P2Y12 inhibitor (clopidogrel/prasugrel/ticagrelor)
            - Theo dõi sát dấu hiệu chảy máu
            - Đánh giá lại sau 12 tháng
            """)
        else:
            st.info(f"""
            **ℹ️ DAPT TIÊU CHUẨN 12 THÁNG (Score = {result['total_score']} < 2):**
            
            **Khuyến cáo:**
            - **DAPT tiêu chuẩn 12 tháng** đủ
            - Không cần kéo dài thêm
            - Aspirin + P2Y12 inhibitor (clopidogrel/prasugrel/ticagrelor)
            - Sau 12 tháng: Chuyển sang aspirin đơn độc
            - Theo dõi sát dấu hiệu chảy máu
            """)
        
        st.warning("""
        **⚠️ QUAN TRỌNG - Kết hợp với PRECISE-DAPT Score:**
        
        - **DAPT Score** đánh giá lợi ích (giảm thiếu máu)
        - **PRECISE-DAPT Score** đánh giá nguy cơ (chảy máu)
        - Quyết định cuối cùng cần cân bằng cả hai:
          * Nếu DAPT Score ≥2 VÀ PRECISE-DAPT <25: DAPT 30 tháng
          * Nếu DAPT Score <2 HOẶC PRECISE-DAPT ≥25: DAPT 12 tháng
          * Nếu PRECISE-DAPT ≥25: Cân nhắc DAPT ngắn 3-6 tháng
        """)
        
        # Prepare inputs and results
        inputs_dict = {
            "Age": f"{age} tuổi",
            "Current Smoking": "Có" if current_smoking else "Không",
            "Diabetes": "Có" if diabetes else "Không",
            "MI at Presentation": "Có" if mi_at_presentation else "Không",
            "Prior PCI/MI": "Có" if prior_pci_or_mi else "Không",
            "Paclitaxel Stent": "Có" if paclitaxel_stent else "Không",
            "Stent <3 mm": "Có" if stent_diameter_lt_3mm else "Không",
            "CHF or LVEF <30%": "Có" if chf_or_lvef_lt_30 else "Không"
        }
        
        results_dict = {
            "DAPT Score": f"{result['total_score']}",
            "Recommendation": result['recommendation'],
            "Benefit": result['benefit']
        }
        
        # Export section
        render_export_section(
            title="DAPT Score",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="DAPT Score"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="dapt_score",
            calculator_name="DAPT Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="dapt_score",
            calculator_name="DAPT Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="dapt_score", show_actions=True)
        
        # References section
        references = get_references("DAPT Score")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['dapt_score_result'] = result
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("DAPT Score")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            **DAPT Score**
            
            **Reference:**
            Yeh RW, Secemsky EA, Kereiakes DJ, et al. Development and validation of a 
            prediction rule for benefit and harm of dual antiplatelet therapy beyond 1 year 
            after percutaneous coronary intervention. JAMA. 2016;315(16):1735-1749.
            
            **9 Factors:**
            1. Age ≥75 years (1 point)
            2. Age 65-74 years (1 point)
            3. Current cigarette smoking (1 point)
            4. Diabetes mellitus (1 point)
            5. MI at presentation (1 point)
            6. Prior PCI or prior MI (1 point)
            7. Paclitaxel-eluting stent (1 point)
            8. Stent diameter <3 mm (1 point)
            9. CHF or LVEF <30% (2 points)
            
            **Total: 0-9 points**
            
            **Interpretation:**
            - ≥2: Extended DAPT (30 months)
            - <2: Standard DAPT (12 months)
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

