"""
ICANS (Immune Effector Cell-Associated Neurotoxicity Syndrome) Consensus Grading
==================================================================================

Grades the severity of neurotoxicity caused by immune effector cell therapies 
such as CAR T-cell treatment.

Reference:
- Lee DW, et al. ASTCT Consensus Grading for Cytokine Release Syndrome and 
  Neurologic Toxicity Associated with Immune Effector Cells. Biol Blood Marrow 
  Transplant. 2019;25(4):625-638.

ICANS Grading (ASTCT Consensus):
Based on ICE (Immune Effector Cell Encephalopathy) Score and clinical features:

ICE Score Components (0-10 points):
- Orientation (0-4 points)
- Naming (0-3 points)
- Following commands (0-1 point)
- Writing (0-1 point)
- Attention (0-1 point)

Grade 1: ICE Score 7-9
Grade 2: ICE Score 3-6
Grade 3: ICE Score 0-2
Grade 4: Any seizure, motor weakness, elevated ICP, or cerebral edema

Clinical Utility:
- Standardized grading for CAR T-cell neurotoxicity
- Guides treatment decisions
- Used in oncology and neurology
- Critical for patient safety monitoring
"""

import streamlit as st
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_ice_score(
    orientation_score: int,
    naming_score: int,
    following_commands: bool,
    writing: bool,
    attention: bool
) -> int:
    """
    Calculate ICE (Immune Effector Cell Encephalopathy) Score
    
    Args:
        orientation_score: Orientation score (0-4)
        naming_score: Naming score (0-3)
        following_commands: Can follow commands (0-1)
        writing: Can write (0-1)
        attention: Attention intact (0-1)
    
    Returns:
        ICE Score (0-10)
    """
    score = orientation_score + naming_score
    if following_commands:
        score += 1
    if writing:
        score += 1
    if attention:
        score += 1
    return score


def grade_icans(
    ice_score: int,
    seizure: bool,
    motor_weakness: bool,
    elevated_icp: bool,
    cerebral_edema: bool
) -> dict:
    """
    Grade ICANS based on ICE Score and clinical features
    
    Args:
        ice_score: ICE Score (0-10)
        seizure: Any seizure
        motor_weakness: Motor weakness
        elevated_icp: Elevated intracranial pressure
        cerebral_edema: Cerebral edema
    
    Returns:
        Dictionary with ICANS grade and interpretation
    """
    grade = 0
    grade_description = ""
    details = []
    
    # Check for Grade 4 criteria first (most severe)
    if seizure or motor_weakness or elevated_icp or cerebral_edema:
        grade = 4
        grade_description = "Nặng - Đe dọa tính mạng"
        if seizure:
            details.append("Có co giật → Grade 4")
        if motor_weakness:
            details.append("Yếu vận động → Grade 4")
        if elevated_icp:
            details.append("Tăng áp lực nội sọ → Grade 4")
        if cerebral_edema:
            details.append("Phù não → Grade 4")
    elif ice_score <= 2:
        grade = 3
        grade_description = "Nặng"
        details.append(f"ICE Score {ice_score} (0-2) → Grade 3")
    elif ice_score <= 6:
        grade = 2
        grade_description = "Trung bình"
        details.append(f"ICE Score {ice_score} (3-6) → Grade 2")
    elif ice_score <= 9:
        grade = 1
        grade_description = "Nhẹ"
        details.append(f"ICE Score {ice_score} (7-9) → Grade 1")
    else:  # ICE Score 10
        grade = 0
        grade_description = "Không có triệu chứng"
        details.append(f"ICE Score {ice_score} (10) → Grade 0")
    
    # Management recommendations
    management = {
        0: "Theo dõi thường quy",
        1: "Theo dõi sát, hỗ trợ điều trị nhẹ",
        2: "Điều trị tích cực, cân nhắc tocilizumab, dexamethasone",
        3: "Điều trị tích cực, tocilizumab, dexamethasone, cân nhắc ICU",
        4: "Điều trị tại ICU, tocilizumab, dexamethasone, điều trị hỗ trợ tối đa"
    }
    
    return {
        "ice_score": ice_score,
        "grade": grade,
        "grade_description": grade_description,
        "management": management[grade],
        "details": details
    }


def render():
    """Render ICANS Consensus Grading interface"""
    import streamlit as st
    
    st.set_page_config(page_title="ICANS Grading", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🧠 ICANS Consensus Grading</h2>
    <p style='text-align: center; color: #6B7280;'>
    Immune Effector Cell-Associated Neurotoxicity Syndrome<br>
    Phân độ mức độ nặng của độc tính thần kinh gây ra bởi liệu pháp tế bào hiệu ứng miễn dịch
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về ICANS Consensus Grading"):
        st.markdown("""
        **ICANS (Immune Effector Cell-Associated Neurotoxicity Syndrome)** là hệ thống phân độ 
        chuẩn hóa cho độc tính thần kinh liên quan đến liệu pháp tế bào hiệu ứng miễn dịch như CAR T-cell.
        
        ### ICE Score Components (0-10 điểm):
        1. **Orientation (0-4 điểm):** Định hướng (năm, tháng, thành phố, bệnh viện)
        2. **Naming (0-3 điểm):** Đặt tên (3 đồ vật)
        3. **Following commands (0-1 điểm):** Thực hiện lệnh
        4. **Writing (0-1 điểm):** Viết câu
        5. **Attention (0-1 điểm):** Chú ý
        
        ### Phân độ ICANS:
        - **Grade 0:** ICE Score 10 - Không có triệu chứng
        - **Grade 1:** ICE Score 7-9 - Nhẹ
        - **Grade 2:** ICE Score 3-6 - Trung bình
        - **Grade 3:** ICE Score 0-2 - Nặng
        - **Grade 4:** Co giật, yếu vận động, tăng áp lực nội sọ, phù não - Đe dọa tính mạng
        
        ### Ứng dụng lâm sàng:
        - Theo dõi độc tính thần kinh trong điều trị CAR T-cell
        - Hướng dẫn quyết định điều trị
        - Dùng trong ung thư học và thần kinh
        - Quan trọng cho an toàn bệnh nhân
        """)
    
    # Input section
    st.markdown("### 📊 Đánh giá ICE Score")
    
    st.markdown("#### 1. Orientation (Định hướng) - 0-4 điểm")
    orientation_score = st.slider(
        "Điểm định hướng",
        min_value=0,
        max_value=4,
        value=4,
        step=1,
        key="icans_orientation",
        help="0: Không định hướng, 1: Định hướng 1/4, 2: Định hướng 2/4, 3: Định hướng 3/4, 4: Định hướng đầy đủ"
    )
    
    st.markdown("#### 2. Naming (Đặt tên) - 0-3 điểm")
    naming_score = st.slider(
        "Điểm đặt tên",
        min_value=0,
        max_value=3,
        value=3,
        step=1,
        key="icans_naming",
        help="0: Không đặt tên được, 1: Đặt tên 1/3, 2: Đặt tên 2/3, 3: Đặt tên đầy đủ"
    )
    
    st.markdown("#### 3. Following Commands (Thực hiện lệnh) - 0-1 điểm")
    following_commands = st.checkbox(
        "Có thể thực hiện lệnh đơn giản",
        value=True,
        key="icans_commands"
    )
    
    st.markdown("#### 4. Writing (Viết) - 0-1 điểm")
    writing = st.checkbox(
        "Có thể viết câu đơn giản",
        value=True,
        key="icans_writing"
    )
    
    st.markdown("#### 5. Attention (Chú ý) - 0-1 điểm")
    attention = st.checkbox(
        "Chú ý còn nguyên vẹn",
        value=True,
        key="icans_attention"
    )
    
    # Calculate ICE Score
    ice_score = calculate_ice_score(
        orientation_score=orientation_score,
        naming_score=naming_score,
        following_commands=following_commands,
        writing=writing,
        attention=attention
    )
    
    st.markdown("---")
    st.markdown("### 🚨 Các dấu hiệu nặng (Grade 4)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        seizure = st.checkbox("Co giật", key="icans_seizure")
        motor_weakness = st.checkbox("Yếu vận động", key="icans_motor")
    
    with col2:
        elevated_icp = st.checkbox("Tăng áp lực nội sọ", key="icans_icp")
        cerebral_edema = st.checkbox("Phù não", key="icans_edema")
    
    if st.button("🔬 Phân độ ICANS", type="primary", use_container_width=True):
        result = grade_icans(
            ice_score=ice_score,
            seizure=seizure,
            motor_weakness=motor_weakness,
            elevated_icp=elevated_icp,
            cerebral_edema=cerebral_edema
        )
        
        # Display results
        st.markdown("---")
        st.markdown("### 📋 Kết quả ICANS Grading")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("ICE Score", f"{result['ice_score']}/10")
        
        with col2:
            st.metric(
                "ICANS Grade",
                f"Grade {result['grade']}"
            )
        
        with col3:
            st.metric(
                "Mức độ",
                result['grade_description']
            )
        
        # Details
        st.markdown("### 📝 Chi tiết")
        for detail in result['details']:
            st.markdown(f"- {detail}")
        
        # Management
        st.markdown("### 💡 Khuyến nghị điều trị")
        
        if result['grade'] == 0:
            st.success(f"**Grade {result['grade']} - {result['grade_description']}**")
            st.markdown(f"**Điều trị:** {result['management']}")
        elif result['grade'] == 1:
            st.info(f"**Grade {result['grade']} - {result['grade_description']}**")
            st.markdown(f"**Điều trị:** {result['management']}")
            st.markdown("""
            - Theo dõi sát dấu hiệu thần kinh
            - Hỗ trợ điều trị triệu chứng
            - Đánh giá lại định kỳ
            """)
        elif result['grade'] == 2:
            st.warning(f"**Grade {result['grade']} - {result['grade_description']}**")
            st.markdown(f"**Điều trị:** {result['management']}")
            st.markdown("""
            - **Tocilizumab:** 8 mg/kg IV (nếu chưa dùng)
            - **Dexamethasone:** 10 mg IV q6h
            - Theo dõi sát tại bệnh viện
            - Cân nhắc chuyển ICU nếu xấu đi
            """)
        elif result['grade'] == 3:
            st.error(f"**Grade {result['grade']} - {result['grade_description']}**")
            st.markdown(f"**Điều trị:** {result['management']}")
            st.markdown("""
            - **Tocilizumab:** 8 mg/kg IV (nếu chưa dùng)
            - **Dexamethasone:** 10 mg IV q6h hoặc cao hơn
            - **Cân nhắc ICU** ngay lập tức
            - Điều trị hỗ trợ tích cực
            - Chụp CT/MRI não nếu cần
            """)
        else:  # Grade 4
            st.error(f"**Grade {result['grade']} - {result['grade_description']}**")
            st.markdown(f"**Điều trị:** {result['management']}")
            st.markdown("""
            - **Điều trị tại ICU** ngay lập tức
            - **Tocilizumab:** 8 mg/kg IV
            - **Dexamethasone:** 10-20 mg IV q6h
            - Điều trị hỗ trợ tối đa
            - Chụp CT/MRI não khẩn cấp
            - Cân nhắc điều trị phù não
            - Hỗ trợ hô hấp nếu cần
            """)
        
        # Save to history
        save_calculation_to_history(
            calculator_id="icans",
            calculator_name="ICANS Consensus Grading",
            inputs={
                "ICE Score": f"{ice_score}/10",
                "Co giật": "Có" if seizure else "Không",
                "Yếu vận động": "Có" if motor_weakness else "Không",
                "Tăng áp lực nội sọ": "Có" if elevated_icp else "Không",
                "Phù não": "Có" if cerebral_edema else "Không"
            },
            result={
                "ICE Score": f"{result['ice_score']}/10",
                "ICANS Grade": f"Grade {result['grade']}",
                "Mức độ": result['grade_description']
            }
        )
        
        # Share and export
        render_share_section(
            calculator_id="icans",
            calculator_name="ICANS Consensus Grading"
        )
        
        render_export_section(
            calculator_id="icans",
            calculator_name="ICANS Consensus Grading",
            data={
                "inputs": {
                    "ice_score": ice_score,
                    "seizure": seizure,
                    "motor_weakness": motor_weakness,
                    "elevated_icp": elevated_icp,
                    "cerebral_edema": cerebral_edema
                },
                "result": result
            }
        )
    
    # History
    render_history_ui(calculator_id="icans", show_actions=True)
    
    # References
    references = get_references("ICANS Consensus Grading")
    if references:
        render_references_section(references)

