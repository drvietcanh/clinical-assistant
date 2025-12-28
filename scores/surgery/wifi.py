"""
WIFI Classification (Wound, Ischemia, foot Infection)
======================================================

Assesses severity of limb threat in patients with lower extremity disease.

Reference:
- Mills JL Sr, et al. The Society for Vascular Surgery Lower Extremity 
  Threatened Limb Classification System: risk stratification based on wound, 
  ischemia, and foot infection (WIfI). J Vasc Surg. 2014;59(1):220-234.

WIFI Components (3 categories):
1. Wound (W) - 0-3
2. Ischemia (I) - 0-3
3. foot Infection (fI) - 0-3

Each category scored 0-3
Total: 0-9 (but interpreted by category, not sum)

Clinical Stage:
- Stage 1: Very low risk (0-1 in each category)
- Stage 2: Low risk (2 in any category)
- Stage 3: Moderate risk (3 in any category)
- Stage 4: High risk (Multiple 3s or combination)

Amputation Risk:
- Stage 1: <5% at 1 year
- Stage 2: 5-10% at 1 year
- Stage 3: 10-25% at 1 year
- Stage 4: >25% at 1 year

Clinical Utility:
- Risk stratification for limb salvage vs amputation
- Guides revascularization decisions
- Used in vascular surgery
- Helps predict amputation risk
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


def classify_wifi(
    wound_score: int,
    ischemia_score: int,
    infection_score: int
) -> dict:
    """
    Classify WIFI Stage
    
    Args:
        wound_score: Wound score (0-3)
        ischemia_score: Ischemia score (0-3)
        infection_score: Foot infection score (0-3)
    
    Returns:
        Dictionary with WIFI stage, amputation risk, and recommendation
    """
    max_score = max(wound_score, ischemia_score, infection_score)
    total_score = wound_score + ischemia_score + infection_score
    
    # Determine stage
    if max_score <= 1 and total_score <= 3:
        stage = 1
        stage_name = "Nguy cơ rất thấp"
        amputation_risk = "<5% tại 1 năm"
        recommendation = "Điều trị bảo tồn, theo dõi"
    elif max_score == 2:
        stage = 2
        stage_name = "Nguy cơ thấp"
        amputation_risk = "5-10% tại 1 năm"
        recommendation = "Điều trị bảo tồn, cân nhắc can thiệp"
    elif max_score == 3 and total_score <= 6:
        stage = 3
        stage_name = "Nguy cơ trung bình"
        amputation_risk = "10-25% tại 1 năm"
        recommendation = "Cân nhắc can thiệp mạch máu"
    else:  # Multiple 3s or high total
        stage = 4
        stage_name = "Nguy cơ cao"
        amputation_risk = ">25% tại 1 năm"
        recommendation = "Can thiệp mạch máu tích cực hoặc cân nhắc cắt cụt"
    
    return {
        "wound_score": wound_score,
        "ischemia_score": ischemia_score,
        "infection_score": infection_score,
        "max_score": max_score,
        "total_score": total_score,
        "stage": stage,
        "stage_name": stage_name,
        "amputation_risk": amputation_risk,
        "recommendation": recommendation
    }


def render():
    """Render WIFI Classification interface"""
    import streamlit as st
    
    st.set_page_config(page_title="WIFI Classification", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🦶 WIFI Classification</h2>
    <p style='text-align: center; color: #6B7280;'>
    Wound, Ischemia, foot Infection Classification<br>
    Đánh giá mức độ nặng đe dọa chi ở bệnh nhân bệnh chi dưới
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về WIFI Classification"):
        st.markdown("""
        **WIFI Classification (Wound, Ischemia, foot Infection)** là hệ thống phân loại 
        đánh giá mức độ nặng đe dọa chi ở bệnh nhân bệnh chi dưới.
        
        ### Các thành phần (3 mục, mỗi mục 0-3 điểm):
        
        **1. Wound (Vết thương) - 0-3:**
        - 0 = Không có vết thương
        - 1 = Vết thương nhỏ, nông
        - 2 = Vết thương sâu, có thể đến gân/xương
        - 3 = Vết thương rộng, sâu, hoại tử mô
        
        **2. Ischemia (Thiếu máu) - 0-3:**
        - 0 = Không thiếu máu (ABI ≥0.8, toe pressure ≥60)
        - 1 = Thiếu máu nhẹ (ABI 0.6-0.79, toe pressure 40-59)
        - 2 = Thiếu máu trung bình (ABI 0.4-0.59, toe pressure 30-39)
        - 3 = Thiếu máu nặng (ABI <0.4, toe pressure <30, hoặc không đo được)
        
        **3. foot Infection (Nhiễm trùng bàn chân) - 0-3:**
        - 0 = Không nhiễm trùng
        - 1 = Nhiễm trùng nhẹ (da, mô dưới da)
        - 2 = Nhiễm trùng trung bình (lan đến cơ, gân, khớp)
        - 3 = Nhiễm trùng nặng (viêm xương tủy, hoại thư)
        
        ### Phân loại giai đoạn:
        - **Stage 1:** Nguy cơ rất thấp (<5% cắt cụt tại 1 năm)
        - **Stage 2:** Nguy cơ thấp (5-10%)
        - **Stage 3:** Nguy cơ trung bình (10-25%)
        - **Stage 4:** Nguy cơ cao (>25%)
        
        ### Ứng dụng lâm sàng:
        - Phân tầng nguy cơ: bảo tồn chi vs cắt cụt
        - Hướng dẫn quyết định can thiệp mạch máu
        - Dùng trong phẫu thuật mạch máu
        - Giúp dự đoán nguy cơ cắt cụt
        """)
    
    # Input section
    st.markdown("### 📊 Đánh giá WIFI")
    
    st.markdown("#### 1. Wound (Vết thương) - 0-3 điểm")
    wound_score = st.selectbox(
        "Mức độ vết thương",
        [
            "0 = Không có vết thương",
            "1 = Vết thương nhỏ, nông",
            "2 = Vết thương sâu, có thể đến gân/xương",
            "3 = Vết thương rộng, sâu, hoại tử mô"
        ],
        key="wifi_wound"
    )
    wound_score_value = int(wound_score.split("=")[0].strip())
    
    st.markdown("#### 2. Ischemia (Thiếu máu) - 0-3 điểm")
    ischemia_score = st.selectbox(
        "Mức độ thiếu máu",
        [
            "0 = Không thiếu máu (ABI ≥0.8, toe pressure ≥60)",
            "1 = Thiếu máu nhẹ (ABI 0.6-0.79, toe pressure 40-59)",
            "2 = Thiếu máu trung bình (ABI 0.4-0.59, toe pressure 30-39)",
            "3 = Thiếu máu nặng (ABI <0.4, toe pressure <30, hoặc không đo được)"
        ],
        key="wifi_ischemia"
    )
    ischemia_score_value = int(ischemia_score.split("=")[0].strip())
    
    st.markdown("#### 3. foot Infection (Nhiễm trùng bàn chân) - 0-3 điểm")
    infection_score = st.selectbox(
        "Mức độ nhiễm trùng",
        [
            "0 = Không nhiễm trùng",
            "1 = Nhiễm trùng nhẹ (da, mô dưới da)",
            "2 = Nhiễm trùng trung bình (lan đến cơ, gân, khớp)",
            "3 = Nhiễm trùng nặng (viêm xương tủy, hoại thư)"
        ],
        key="wifi_infection"
    )
    infection_score_value = int(infection_score.split("=")[0].strip())
    
    if st.button("🔬 Phân loại WIFI", type="primary", use_container_width=True):
        result = classify_wifi(
            wound_score=wound_score_value,
            ischemia_score=ischemia_score_value,
            infection_score=infection_score_value
        )
        
        # Display results
        st.markdown("---")
        st.markdown("### 📋 Kết quả WIFI Classification")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Wound", f"{result['wound_score']}/3")
        
        with col2:
            st.metric("Ischemia", f"{result['ischemia_score']}/3")
        
        with col3:
            st.metric("Infection", f"{result['infection_score']}/3")
        
        with col4:
            st.metric("Stage", f"Stage {result['stage']}")
        
        st.markdown("### 📊 Phân loại")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Giai đoạn", result['stage_name'])
        
        with col2:
            st.metric("Nguy cơ cắt cụt 1 năm", result['amputation_risk'])
        
        # Clinical recommendations
        st.markdown("### 💡 Khuyến nghị lâm sàng")
        
        if result['stage'] == 1:
            st.success(f"**Stage {result['stage']} - {result['stage_name']}**")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown("""
            - Điều trị bảo tồn chi
            - Chăm sóc vết thương
            - Kiểm soát yếu tố nguy cơ
            - Theo dõi định kỳ
            """)
        elif result['stage'] == 2:
            st.info(f"**Stage {result['stage']} - {result['stage_name']}**")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown("""
            - Điều trị bảo tồn tích cực
            - Cân nhắc can thiệp mạch máu nếu có chỉ định
            - Chăm sóc vết thương chuyên khoa
            - Theo dõi sát
            """)
        elif result['stage'] == 3:
            st.warning(f"**Stage {result['stage']} - {result['stage_name']}**")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown("""
            - **Cân nhắc can thiệp mạch máu ngay**
            - Đánh giá đa chuyên khoa (mạch máu, chỉnh hình, nhiễm trùng)
            - Điều trị nhiễm trùng tích cực
            - Chăm sóc vết thương chuyên khoa
            - Theo dõi sát tại bệnh viện
            """)
        else:
            st.error(f"**Stage {result['stage']} - {result['stage_name']}**")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown("""
            - **Can thiệp mạch máu tích cực** hoặc
            - **Cân nhắc cắt cụt** nếu không thể cứu chi
            - Đánh giá đa chuyên khoa ngay
            - Điều trị nhiễm trùng tích cực
            - Tư vấn bệnh nhân và gia đình về tiên lượng
            - Có thể cần cắt cụt để cứu mạng sống
            """)
        
        # Save to history
        save_calculation_to_history(
            calculator_id="wifi",
            calculator_name="WIFI Classification",
            inputs={
                "Wound": f"{result['wound_score']}/3",
                "Ischemia": f"{result['ischemia_score']}/3",
                "Infection": f"{result['infection_score']}/3"
            },
            result={
                "Stage": f"Stage {result['stage']}",
                "Nguy cơ": result['stage_name'],
                "Nguy cơ cắt cụt": result['amputation_risk']
            }
        )
        
        # Share and export
        render_share_section(
            calculator_id="wifi",
            calculator_name="WIFI Classification"
        )
        
        render_export_section(
            calculator_id="wifi",
            calculator_name="WIFI Classification",
            data={
                "inputs": {
                    "wound_score": result['wound_score'],
                    "ischemia_score": result['ischemia_score'],
                    "infection_score": result['infection_score']
                },
                "result": result
            }
        )
    
    # History
    render_history_ui(calculator_id="wifi", show_actions=True)
    
    # References
    references = get_references("WIFI Classification")
    if references:
        render_references_section(references)

