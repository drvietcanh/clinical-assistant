"""
Alvarado Score Calculator
=========================

Predicts acute appendicitis risk

Reference:
- Alvarado A. A practical score for the early diagnosis of acute appendicitis. 
  Ann Emerg Med. 1986;15(5):557-564.

Alvarado Score Components (8 factors, 10 points total):
1. Migration of pain (1 point)
2. Anorexia (1 point)
3. Nausea/vomiting (1 point)
4. Tenderness in RLQ (2 points)
5. Rebound tenderness (1 point)
6. Elevated temperature (1 point)
7. Leukocytosis (2 points)
8. Shift to left (1 point)

Total: 0-10 points

Interpretation:
- 0-4: Low probability - Observe or discharge
- 5-6: Moderate probability - Observe, consider imaging
- 7-10: High probability - Surgery/appendectomy

Clinical Utility:
- Used daily in emergency departments
- Helps decide on imaging vs surgery
- Reduces unnecessary CT scans
- Guides clinical decision making
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


def calculate_alvarado_score(
    migration: bool,
    anorexia: bool,
    nausea_vomiting: bool,
    rlq_tenderness: bool,
    rebound: bool,
    fever: bool,
    leukocytosis: bool,
    left_shift: bool
) -> dict:
    """
    Calculate Alvarado Score
    
    Args:
        migration: Migration of pain to RLQ
        anorexia: Loss of appetite
        nausea_vomiting: Nausea or vomiting
        rlq_tenderness: Tenderness in right lower quadrant
        rebound: Rebound tenderness
        fever: Temperature >37.3°C
        leukocytosis: WBC >10,000/μL
        left_shift: Neutrophils >75%
    
    Returns:
        Dictionary with score and interpretation
    """
    score = 0
    details = []
    
    # Migration of pain (1 point)
    if migration:
        score += 1
        details.append("✓ Di chuyển đau → RLQ (+1 điểm)")
    else:
        details.append("✗ Không có di chuyển đau → 0 điểm")
    
    # Anorexia (1 point)
    if anorexia:
        score += 1
        details.append("✓ Chán ăn (+1 điểm)")
    else:
        details.append("✗ Không chán ăn → 0 điểm")
    
    # Nausea/vomiting (1 point)
    if nausea_vomiting:
        score += 1
        details.append("✓ Buồn nôn/nôn (+1 điểm)")
    else:
        details.append("✗ Không buồn nôn/nôn → 0 điểm")
    
    # RLQ tenderness (2 points)
    if rlq_tenderness:
        score += 2
        details.append("✓ Đau khi ấn vùng hố chậu phải (+2 điểm)")
    else:
        details.append("✗ Không đau khi ấn RLQ → 0 điểm")
    
    # Rebound tenderness (1 point)
    if rebound:
        score += 1
        details.append("✓ Đau phản hồi (+1 điểm)")
    else:
        details.append("✗ Không có đau phản hồi → 0 điểm")
    
    # Fever (1 point)
    if fever:
        score += 1
        details.append("✓ Sốt >37.3°C (+1 điểm)")
    else:
        details.append("✗ Không sốt → 0 điểm")
    
    # Leukocytosis (2 points)
    if leukocytosis:
        score += 2
        details.append("✓ Bạch cầu >10,000/μL (+2 điểm)")
    else:
        details.append("✗ Bạch cầu ≤10,000/μL → 0 điểm")
    
    # Left shift (1 point)
    if left_shift:
        score += 1
        details.append("✓ Chuyển trái (neutrophils >75%) (+1 điểm)")
    else:
        details.append("✗ Không chuyển trái → 0 điểm")
    
    # Risk stratification
    if score <= 4:
        probability = "Thấp"
        risk_class = "LOW"
        recommendation = "Quan sát hoặc xuất viện"
        color = "success"
    elif score <= 6:
        probability = "Trung bình"
        risk_class = "MODERATE"
        recommendation = "Quan sát, cân nhắc chụp CT"
        color = "warning"
    else:
        probability = "Cao"
        risk_class = "HIGH"
        recommendation = "Phẫu thuật/cắt ruột thừa"
        color = "error"
    
    return {
        'total_score': score,
        'probability': probability,
        'risk_class': risk_class,
        'recommendation': recommendation,
        'color': color,
        'details': details
    }


def render():
    """Render Alvarado Score calculator"""
    
    st.title("🔪 Alvarado Score")
    st.markdown("**Dự đoán nguy cơ viêm ruột thừa cấp (DÙNG HÀNG NGÀY)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'alvarado':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Alvarado Score** dự đoán nguy cơ viêm ruột thừa cấp:
        - Dùng hàng ngày trong khoa cấp cứu
        - 8 yếu tố lâm sàng và xét nghiệm
        - Tổng điểm: 0-10
        
        ### 🎯 8 Yếu tố
        
        1. **Di chuyển đau** → RLQ (1 điểm)
        2. **Chán ăn** (1 điểm)
        3. **Buồn nôn/nôn** (1 điểm)
        4. **Đau khi ấn RLQ** (2 điểm)
        5. **Đau phản hồi** (1 điểm)
        6. **Sốt** >37.3°C (1 điểm)
        7. **Bạch cầu** >10,000/μL (2 điểm)
        8. **Chuyển trái** (neutrophils >75%) (1 điểm)
        
        ### 📊 Phân loại
        
        - **0-4 điểm:** Nguy cơ thấp → Quan sát hoặc xuất viện
        - **5-6 điểm:** Nguy cơ trung bình → Quan sát, cân nhắc CT
        - **7-10 điểm:** Nguy cơ cao → Phẫu thuật/cắt ruột thừa
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="alvarado",
            calculator_name="Alvarado Score",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🩺 Triệu chứng Lâm sàng")
        migration = st.checkbox(
            "**Di chuyển đau** → Vùng hố chậu phải (RLQ)",
            help="Đau bắt đầu ở vùng thượng vị/quanh rốn, sau đó di chuyển xuống RLQ"
        )
        
        anorexia = st.checkbox(
            "**Chán ăn**",
            help="Mất cảm giác thèm ăn"
        )
        
        nausea_vomiting = st.checkbox(
            "**Buồn nôn hoặc nôn**",
            help="Có buồn nôn hoặc đã nôn"
        )
        
        rlq_tenderness = st.checkbox(
            "**Đau khi ấn vùng hố chậu phải (RLQ)**",
            help="Đau khi ấn vào điểm McBurney hoặc vùng RLQ"
        )
        
        rebound = st.checkbox(
            "**Đau phản hồi (Rebound tenderness)**",
            help="Đau tăng khi thả tay đột ngột sau khi ấn"
        )
    
    with col2:
        st.markdown("#### 🔬 Xét nghiệm")
        fever = st.checkbox(
            "**Sốt** >37.3°C",
            help="Nhiệt độ >37.3°C (99.1°F)"
        )
        
        leukocytosis = st.checkbox(
            "**Bạch cầu tăng** >10,000/μL",
            help="WBC >10,000/μL (hoặc >10 ×10³/μL)"
        )
        
        left_shift = st.checkbox(
            "**Chuyển trái** (Neutrophils >75%)",
            help="Tỷ lệ bạch cầu đa nhân trung tính >75%"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính Alvarado Score", type="primary", use_container_width=True):
        result = calculate_alvarado_score(
            migration=migration,
            anorexia=anorexia,
            nausea_vomiting=nausea_vomiting,
            rlq_tenderness=rlq_tenderness,
            rebound=rebound,
            fever=fever,
            leukocytosis=leukocytosis,
            left_shift=left_shift
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                "**Alvarado Score**",
                f"{result['total_score']}/10"
            )
        
        with col_r2:
            st.markdown(f"### {result['probability'].upper()}")
            st.caption(f"Nguy cơ viêm ruột thừa: {result['probability']}")
        
        # Score breakdown
        with st.expander("📋 Chi tiết điểm số", expanded=True):
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Diễn giải")
        
        if result['risk_class'] == "LOW":
            st.success(f"""
            **✅ Nguy cơ THẤP ({result['total_score']} điểm):**
            
            **Khuyến cáo:**
            - Quan sát tại khoa cấp cứu 4-6 giờ
            - Có thể xuất viện nếu cải thiện
            - Hướng dẫn tái khám nếu đau tăng
            - Không cần chụp CT ngay
            """)
        elif result['risk_class'] == "MODERATE":
            st.warning(f"""
            **⚠️ Nguy cơ TRUNG BÌNH ({result['total_score']} điểm):**
            
            **Khuyến cáo:**
            - Quan sát tại khoa cấp cứu
            - Cân nhắc chụp CT bụng (đặc biệt phụ nữ trẻ)
            - Hội chẩn ngoại khoa
            - Theo dõi sát diễn biến
            - Có thể cần siêu âm bụng trước
            """)
        else:
            st.error(f"""
            **🚨 Nguy cơ CAO ({result['total_score']} điểm):**
            
            **Khuyến cáo:**
            - **Hội chẩn ngoại khoa ngay**
            - Chuẩn bị phẫu thuật/cắt ruột thừa
            - Có thể chụp CT để xác định (nếu cần)
            - Không cần chờ đợi nếu lâm sàng rõ
            - Điều trị kháng sinh trước mổ (nếu có chỉ định)
            """)
        
        st.info("""
        **📌 Lưu ý quan trọng:**
        
        - Alvarado Score chỉ là công cụ hỗ trợ, không thay thế đánh giá lâm sàng
        - Phụ nữ trẻ: Cân nhắc chụp CT để tránh phẫu thuật không cần thiết
        - Trẻ em: Có thể cần điều chỉnh ngưỡng
        - Người già: Triệu chứng có thể không điển hình
        - Quyết định cuối cùng thuộc về bác sĩ lâm sàng
        """)
        
        # Prepare inputs and results
        inputs_dict = {
            "Migration of Pain": "Có" if migration else "Không",
            "Anorexia": "Có" if anorexia else "Không",
            "Nausea/Vomiting": "Có" if nausea_vomiting else "Không",
            "RLQ Tenderness": "Có" if rlq_tenderness else "Không",
            "Rebound Tenderness": "Có" if rebound else "Không",
            "Fever >37.3°C": "Có" if fever else "Không",
            "Leukocytosis >10,000/μL": "Có" if leukocytosis else "Không",
            "Left Shift (Neutrophils >75%)": "Có" if left_shift else "Không"
        }
        
        results_dict = {
            "Alvarado Score": f"{result['total_score']}/10",
            "Probability": result['probability'],
            "Risk Class": result['risk_class'],
            "Recommendation": result['recommendation']
        }
        
        # Export section
        render_export_section(
            title="Alvarado Score",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="Alvarado Score"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="alvarado",
            calculator_name="Alvarado Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="alvarado",
            calculator_name="Alvarado Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="alvarado", show_actions=True)
        
        # References section
        references = get_references("Alvarado")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['alvarado_result'] = result
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("Alvarado")
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
            **Alvarado Score**
            
            **Reference:**
            Alvarado A. A practical score for the early diagnosis of acute appendicitis. 
            Ann Emerg Med. 1986;15(5):557-564.
            
            **8 Factors (10 points total):**
            1. Migration of pain to RLQ (1 point)
            2. Anorexia (1 point)
            3. Nausea/vomiting (1 point)
            4. Tenderness in RLQ (2 points)
            5. Rebound tenderness (1 point)
            6. Elevated temperature >37.3°C (1 point)
            7. Leukocytosis >10,000/μL (2 points)
            8. Shift to left (neutrophils >75%) (1 point)
            
            **Interpretation:**
            - 0-4: Low probability
            - 5-6: Moderate probability
            - 7-10: High probability
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

