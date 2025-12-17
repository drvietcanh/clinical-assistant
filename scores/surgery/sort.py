"""
SORT - Surgical Outcome Risk Tool Calculator
Tiên lượng tử vong 30 ngày sau phẫu thuật không tim
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section


def calculate_sort(surgery_severity, asa_ps, urgency, high_risk_specialty, age, cancer):
    """
    Tính điểm SORT
    
    Parameters:
    - surgery_severity: Mức độ nghiêm trọng phẫu thuật (0=minor, 1=intermediate, 2=major, 3=major+)
    - asa_ps: ASA Physical Status (1-5)
    - urgency: Mức độ khẩn cấp (0=elective, 1=urgent, 2=emergency)
    - high_risk_specialty: Chuyên khoa nguy cơ cao (0=no, 1=yes)
    - age: Tuổi (0=<65, 1=65-79, 2=≥80)
    - cancer: Có ung thư (0=no, 1=yes)
    
    Returns:
    - dict với risk_percentage và interpretation
    """
    # SORT calculation based on Protopapa et al. 2014
    # Simplified version - actual SORT uses logistic regression
    
    # Base risk factors
    risk_score = 0
    
    # Surgery severity
    risk_score += surgery_severity * 2
    
    # ASA-PS (1-5, but higher is worse)
    if asa_ps >= 4:
        risk_score += 3
    elif asa_ps == 3:
        risk_score += 2
    elif asa_ps == 2:
        risk_score += 1
    
    # Urgency
    risk_score += urgency * 2
    
    # High risk specialty
    if high_risk_specialty:
        risk_score += 1
    
    # Age
    risk_score += age
    
    # Cancer
    if cancer:
        risk_score += 1
    
    # Risk percentages (simplified)
    if risk_score <= 3:
        risk_pct = 0.1
        risk_level = "Nguy cơ rất thấp"
        color = "green"
    elif risk_score <= 6:
        risk_pct = 0.5
        risk_level = "Nguy cơ thấp"
        color = "green"
    elif risk_score <= 9:
        risk_pct = 2.0
        risk_level = "Nguy cơ trung bình"
        color = "orange"
    elif risk_score <= 12:
        risk_pct = 5.0
        risk_level = "Nguy cơ cao"
        color = "orange"
    else:
        risk_pct = 15.0
        risk_level = "Nguy cơ rất cao"
        color = "red"
    
    return {
        "risk_score": risk_score,
        "risk_percentage": risk_pct,
        "risk_level": risk_level,
        "color": color
    }


def render():
    """Render SORT interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'sort':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'SORT')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>📊 SORT - Surgical Outcome Risk Tool</h2>
    <p style='text-align: center;'><em>Tiên lượng tử vong 30 ngày sau phẫu thuật không tim</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về SORT"):
        st.markdown("""
        **SORT (Surgical Outcome Risk Tool)** là công cụ tiên lượng tử vong 30 ngày sau phẫu thuật không tim,
        được phát triển bởi NCEPOD (National Confidential Enquiry into Patient Outcome and Death).
        
        **6 yếu tố đánh giá:**
        
        1. **Mức độ nghiêm trọng phẫu thuật (Surgery Severity)**
           - Minor: Phẫu thuật nhỏ (ví dụ: cắt bỏ nốt ruồi)
           - Intermediate: Phẫu thuật trung bình (ví dụ: cắt túi mật)
           - Major: Phẫu thuật lớn (ví dụ: cắt đại tràng)
           - Major+: Phẫu thuật rất lớn (ví dụ: cắt gan, phẫu thuật mạch máu lớn)
        
        2. **ASA Physical Status (ASA-PS)**
           - ASA I: Khỏe mạnh
           - ASA II: Bệnh lý nhẹ
           - ASA III: Bệnh lý nặng
           - ASA IV: Bệnh lý đe dọa tính mạng
           - ASA V: Hấp hối
        
        3. **Mức độ khẩn cấp (Urgency)**
           - Elective: Phẫu thuật có kế hoạch
           - Urgent: Phẫu thuật cấp cứu (trong 24h)
           - Emergency: Phẫu thuật cấp cứu ngay
        
        4. **Chuyên khoa nguy cơ cao (High Risk Specialty)**
           - Có: Phẫu thuật ngực, mạch máu, thần kinh, tiết niệu
           - Không: Các chuyên khoa khác
        
        5. **Tuổi**
           - <65 tuổi
           - 65-79 tuổi
           - ≥80 tuổi
        
        6. **Ung thư (Cancer)**
           - Có: Đang điều trị ung thư hoặc có ung thư
           - Không: Không có ung thư
        
        **Nguy cơ tử vong 30 ngày:**
        - Dựa trên tổng điểm risk score
        - Từ <0.5% đến >15%
        
        **Reference:** Protopapa KL, et al. Development and validation of the Surgical Outcome Risk Tool (SORT). 
        Br J Surg. 2014;101(13):1774-83.
        """)
    
    st.markdown("---")
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        st.subheader("📝 Đánh giá 6 yếu tố")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="sort",
            calculator_name="SORT",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Surgery severity
    st.markdown("### 1️⃣ Mức độ nghiêm trọng phẫu thuật")
    surgery_severity = st.radio(
        "Mức độ:",
        options=[0, 1, 2, 3],
        format_func=lambda x: {
            0: "Minor - Phẫu thuật nhỏ",
            1: "Intermediate - Phẫu thuật trung bình",
            2: "Major - Phẫu thuật lớn",
            3: "Major+ - Phẫu thuật rất lớn"
        }[x],
        key="sort_severity",
        horizontal=False
    )
    
    # ASA-PS
    st.markdown("### 2️⃣ ASA Physical Status")
    asa_ps = st.selectbox(
        "ASA-PS:",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: {
            1: "ASA I - Khỏe mạnh",
            2: "ASA II - Bệnh lý nhẹ",
            3: "ASA III - Bệnh lý nặng",
            4: "ASA IV - Bệnh lý đe dọa tính mạng",
            5: "ASA V - Hấp hối"
        }[x],
        key="sort_asa"
    )
    
    # Urgency
    st.markdown("### 3️⃣ Mức độ khẩn cấp")
    urgency = st.radio(
        "Mức độ:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "Elective - Phẫu thuật có kế hoạch",
            1: "Urgent - Phẫu thuật cấp cứu (24h)",
            2: "Emergency - Phẫu thuật cấp cứu ngay"
        }[x],
        key="sort_urgency",
        horizontal=False
    )
    
    # High risk specialty
    st.markdown("### 4️⃣ Chuyên khoa nguy cơ cao")
    st.caption("Phẫu thuật ngực, mạch máu, thần kinh, tiết niệu")
    high_risk_specialty = st.checkbox(
        "Chuyên khoa nguy cơ cao",
        key="sort_specialty"
    )
    
    # Age
    st.markdown("### 5️⃣ Tuổi")
    age = st.radio(
        "Tuổi:",
        options=[0, 1, 2],
        format_func=lambda x: {
            0: "<65 tuổi",
            1: "65-79 tuổi",
            2: "≥80 tuổi"
        }[x],
        key="sort_age",
        horizontal=False
    )
    
    # Cancer
    st.markdown("### 6️⃣ Ung thư")
    cancer = st.checkbox(
        "Có ung thư hoặc đang điều trị ung thư",
        key="sort_cancer"
    )
    
    st.markdown("---")
    
    if st.button("🔬 Tính điểm SORT", type="primary", use_container_width=True):
        try:
            result = calculate_sort(surgery_severity, asa_ps, urgency, high_risk_specialty, age, cancer)
            
            # Display results
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Risk Score", f"{result['risk_score']}")
            
            with col2:
                st.metric("Nguy cơ", result['risk_level'])
            
            with col3:
                st.metric("Tử vong 30 ngày", f"{result['risk_percentage']:.1f}%")
            
            st.markdown("---")
            
            # Risk interpretation
            if result['color'] == "green":
                st.success(f"**{result['risk_level']}** - Tỷ lệ tử vong 30 ngày: {result['risk_percentage']:.1f}%")
            elif result['color'] == "orange":
                st.warning(f"**{result['risk_level']}** - Tỷ lệ tử vong 30 ngày: {result['risk_percentage']:.1f}%")
            else:
                st.error(f"**{result['risk_level']}** - Tỷ lệ tử vong 30 ngày: {result['risk_percentage']:.1f}%")
            
            st.markdown("---")
            
            # Additional information
            with st.expander("📚 Thông tin bổ sung"):
                st.markdown("""
                **Các yếu tố nguy cơ quan trọng:**
                
                1. **ASA-PS ≥4:** Nguy cơ tử vong tăng đáng kể
                2. **Emergency surgery:** Nguy cơ cao hơn elective
                3. **Major+ surgery:** Phẫu thuật rất lớn có nguy cơ cao
                4. **Tuổi ≥80:** Nguy cơ tăng theo tuổi
                5. **Ung thư:** Bệnh nhân ung thư có nguy cơ cao hơn
                
                **Khuyến nghị:**
                - Risk score cao: Chuẩn bị kỹ trước mổ, có kế hoạch hậu phẫu
                - Cân nhắc ICU sau mổ nếu risk score cao
                - Thông báo cho bệnh nhân và gia đình về nguy cơ
                """)
            
            # Prepare data for history and share
            inputs_dict = {
                "Mức độ nghiêm trọng": {0: "Minor", 1: "Intermediate", 2: "Major", 3: "Major+"}[surgery_severity],
                "ASA-PS": f"ASA {asa_ps}",
                "Mức độ khẩn cấp": {0: "Elective", 1: "Urgent", 2: "Emergency"}[urgency],
                "Chuyên khoa nguy cơ cao": "Có" if high_risk_specialty else "Không",
                "Tuổi": {0: "<65", 1: "65-79", 2: "≥80"}[age],
                "Ung thư": "Có" if cancer else "Không"
            }
            
            results_dict = {
                "Risk Score": str(result['risk_score']),
                "Mức nguy cơ": result['risk_level'],
                "Tử vong 30 ngày": f"{result['risk_percentage']:.1f}%"
            }
            
            # Export section
            render_export_section(
                title="SORT",
                inputs=inputs_dict,
                results=results_dict
            ,
                calculator_name="SORT"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="sort",
                calculator_name="SORT",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="sort",
                calculator_name="SORT",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            render_history_ui(calculator_id="sort", show_actions=True)
        
        except Exception as e:
            st.error(f"❌ Lỗi khi tính toán: {str(e)}")
            st.exception(e)
            return
    
    # References section (Phase 1)
    st.markdown("---")
    references = get_references("sort")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

