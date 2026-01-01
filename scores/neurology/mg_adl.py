"""
MG-ADL (Myasthenia Gravis Activities of Daily Living)
=====================================================

Assesses disease severity in patients with myasthenia gravis (MG).

Reference:
- Wolfe GI, et al. Development of a quality-of-life instrument for 
  myasthenia gravis. Neurology. 1999;52(7):1481-1489.

MG-ADL Components (8 items, 0-3 points each):
1. Talking
2. Chewing
3. Swallowing
4. Breathing
5. Impairment of ability to brush teeth or comb hair
6. Impairment of ability to arise from a chair
7. Double vision
8. Eyelid droop

Total: 0-24 points

Severity:
- 0-5: Mild
- 6-11: Moderate
- 12-17: Severe
- 18-24: Very severe

Clinical Utility:
- Assesses MG impact on daily activities
- Monitors treatment response
- Guides therapy adjustments
- Used in neurology
"""

import streamlit as st
from config.theme import COLORS
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_mg_adl(
    talking: int,
    chewing: int,
    swallowing: int,
    breathing: int,
    brushing_combing: int,
    arising_chair: int,
    double_vision: int,
    eyelid_droop: int
) -> dict:
    """
    Calculate MG-ADL Score
    
    Args:
        talking: Talking score (0-3)
        chewing: Chewing score (0-3)
        swallowing: Swallowing score (0-3)
        breathing: Breathing score (0-3)
        brushing_combing: Brushing/combing score (0-3)
        arising_chair: Arising from chair score (0-3)
        double_vision: Double vision score (0-3)
        eyelid_droop: Eyelid droop score (0-3)
    
    Returns:
        Dictionary with MG-ADL score, severity, and interpretation
    """
    total_score = (
        talking +
        chewing +
        swallowing +
        breathing +
        brushing_combing +
        arising_chair +
        double_vision +
        eyelid_droop
    )
    
    # Severity
    if total_score <= 5:
        severity = "Nhẹ"
        interpretation = "Tác động nhẹ lên hoạt động hàng ngày"
        recommendation = "Điều trị duy trì, theo dõi"
    elif total_score <= 11:
        severity = "Trung bình"
        interpretation = "Tác động trung bình lên hoạt động hàng ngày"
        recommendation = "Điều chỉnh điều trị, tăng liều hoặc thêm thuốc"
    elif total_score <= 17:
        severity = "Nặng"
        interpretation = "Tác động nặng lên hoạt động hàng ngày"
        recommendation = "Điều trị tích cực, cân nhắc IVIG/plasma exchange"
    else:
        severity = "Rất nặng"
        interpretation = "Tác động rất nặng lên hoạt động hàng ngày"
        recommendation = "Điều trị tích cực ngay, IVIG/plasma exchange, cân nhắc ICU"
    
    return {
        "total_score": total_score,
        "severity": severity,
        "interpretation": interpretation,
        "recommendation": recommendation,
        "details": {
            "talking": talking,
            "chewing": chewing,
            "swallowing": swallowing,
            "breathing": breathing,
            "brushing_combing": brushing_combing,
            "arising_chair": arising_chair,
            "double_vision": double_vision,
            "eyelid_droop": eyelid_droop
        }
    }


def render():
    """Render MG-ADL interface"""
    import streamlit as st
    
    # st.set_page_config(page_title="MG-ADL", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 MG-ADL (Myasthenia Gravis Activities of Daily Living)</h3>
    <p style='text-align: center; color: #6B7280;'>
    Đánh giá mức độ nặng bệnh ở bệnh nhân nhược cơ (MG)
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về MG-ADL"):
        st.markdown("""
        **MG-ADL (Myasthenia Gravis Activities of Daily Living)** là thang điểm đánh giá 
        mức độ nặng bệnh ở bệnh nhân nhược cơ dựa trên tác động lên hoạt động hàng ngày.
        
        ### Các thành phần (8 mục, mỗi mục 0-3 điểm):
        1. **Talking (Nói):** 0 = Bình thường, 3 = Không thể nói
        2. **Chewing (Nhai):** 0 = Bình thường, 3 = Không thể nhai
        3. **Swallowing (Nuốt):** 0 = Bình thường, 3 = Không thể nuốt
        4. **Breathing (Thở):** 0 = Bình thường, 3 = Khó thở nặng
        5. **Brushing/Combing (Chải răng/Chải tóc):** 0 = Bình thường, 3 = Không thể
        6. **Arising from chair (Đứng dậy từ ghế):** 0 = Bình thường, 3 = Không thể
        7. **Double vision (Nhìn đôi):** 0 = Không, 3 = Liên tục
        8. **Eyelid droop (Sụp mi):** 0 = Không, 3 = Nặng, che mắt
        
        ### Phân loại mức độ:
        - **0-5 điểm:** Nhẹ
        - **6-11 điểm:** Trung bình
        - **12-17 điểm:** Nặng
        - **18-24 điểm:** Rất nặng
        
        ### Ứng dụng lâm sàng:
        - Đánh giá tác động MG lên hoạt động hàng ngày
        - Theo dõi đáp ứng điều trị
        - Hướng dẫn điều chỉnh điều trị
        - Dùng trong thần kinh
        """)
    
    # Input section
    st.markdown("### 📊 Đánh giá hoạt động hàng ngày (mỗi mục 0-3 điểm)")
    st.markdown("**Hướng dẫn:** 0 = Bình thường/Không, 1 = Nhẹ, 2 = Trung bình, 3 = Nặng/Không thể")
    
    col1, col2 = st.columns(2)
    
    with col1:
        talking = st.slider(
            "1. Talking (Nói)",
            min_value=0,
            max_value=3,
            value=0,
            step=1,
            key="mg_adl_talking"
        )
        
        chewing = st.slider(
            "2. Chewing (Nhai)",
            min_value=0,
            max_value=3,
            value=0,
            step=1,
            key="mg_adl_chewing"
        )
        
        swallowing = st.slider(
            "3. Swallowing (Nuốt)",
            min_value=0,
            max_value=3,
            value=0,
            step=1,
            key="mg_adl_swallowing"
        )
        
        breathing = st.slider(
            "4. Breathing (Thở)",
            min_value=0,
            max_value=3,
            value=0,
            step=1,
            key="mg_adl_breathing"
        )
    
    with col2:
        brushing_combing = st.slider(
            "5. Brushing/Combing (Chải răng/Chải tóc)",
            min_value=0,
            max_value=3,
            value=0,
            step=1,
            key="mg_adl_brushing"
        )
        
        arising_chair = st.slider(
            "6. Arising from chair (Đứng dậy từ ghế)",
            min_value=0,
            max_value=3,
            value=0,
            step=1,
            key="mg_adl_arising"
        )
        
        double_vision = st.slider(
            "7. Double vision (Nhìn đôi)",
            min_value=0,
            max_value=3,
            value=0,
            step=1,
            key="mg_adl_double"
        )
        
        eyelid_droop = st.slider(
            "8. Eyelid droop (Sụp mi)",
            min_value=0,
            max_value=3,
            value=0,
            step=1,
            key="mg_adl_eyelid"
        )
    
    if st.button("🔬 Tính điểm MG-ADL", type="primary", use_container_width=True):
        result = calculate_mg_adl(
            talking=talking,
            chewing=chewing,
            swallowing=swallowing,
            breathing=breathing,
            brushing_combing=brushing_combing,
            arising_chair=arising_chair,
            double_vision=double_vision,
            eyelid_droop=eyelid_droop
        )
        
        # Display results
        st.markdown("---")
        st.subheader("📋 Kết quả")
        
        if result['total_score'] <= 5:
            color = COLORS["success"]
            icon = "✅"
            severity_class = "Nhẹ"
        elif result['total_score'] <= 11:
            color = COLORS["info"]
            icon = "ℹ️"
            severity_class = "Trung bình"
        elif result['total_score'] <= 17:
            color = COLORS["warning"]
            icon = "⚠️"
            severity_class = "Nặng"
        else:
            color = COLORS["error"]
            icon = "🚨"
            severity_class = "Rất nặng"

        render_score_result(
            title="MG-ADL Score",
            score=result['total_score'],
            interpretation=f"{result['severity']}\n({result['interpretation']})",
            color=color,
            icon=icon
        )
        
        st.info(f"**{result['interpretation']}**")
        
        # Details
        st.markdown("### 📝 Chi tiết")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"- **Nói:** {result['details']['talking']}/3")
            st.markdown(f"- **Nhai:** {result['details']['chewing']}/3")
            st.markdown(f"- **Nuốt:** {result['details']['swallowing']}/3")
            st.markdown(f"- **Thở:** {result['details']['breathing']}/3")
        
        with col2:
            st.markdown(f"- **Chải răng/tóc:** {result['details']['brushing_combing']}/3")
            st.markdown(f"- **Đứng dậy:** {result['details']['arising_chair']}/3")
            st.markdown(f"- **Nhìn đôi:** {result['details']['double_vision']}/3")
            st.markdown(f"- **Sụp mi:** {result['details']['eyelid_droop']}/3")
        
        # Clinical recommendations
        st.markdown("### 💡 Khuyến nghị điều trị")
        
        if result['total_score'] <= 5:
            st.success(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
        elif result['total_score'] <= 11:
            st.info(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
        elif result['total_score'] <= 17:
            st.warning(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
        else:
            st.error(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
        
        # Save to history
        save_calculation_to_history(
            calculator_id="mg_adl",
            calculator_name="MG-ADL",
            inputs={
                "Nói": f"{talking}",
                "Nhai": f"{chewing}",
                "Nuốt": f"{swallowing}",
                "Thở": f"{breathing}",
                "Chải răng/tóc": f"{brushing_combing}",
                "Đứng dậy": f"{arising_chair}",
                "Nhìn đôi": f"{double_vision}",
                "Sụp mi": f"{eyelid_droop}"
            },
            result={
                "Điểm": f"{result['total_score']}/24",
                "Mức độ": result['severity']
            }
        )
        
        # Share and export
        render_share_section(
            calculator_id="mg_adl",
            calculator_name="MG-ADL"
        )
        
        render_export_section(
            calculator_id="mg_adl",
            calculator_name="MG-ADL",
            data={
                "inputs": result['details'],
                "result": {
                    "total_score": result['total_score'],
                    "severity": result['severity'],
                    "interpretation": result['interpretation']
                }
            }
        )
    
    # History
    render_history_ui(calculator_id="mg_adl", show_actions=True)
    
    # References
    references = get_references("MG-ADL")
    if references:
        render_references_section(references)

