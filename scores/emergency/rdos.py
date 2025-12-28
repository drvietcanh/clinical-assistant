"""
RDOS (Respiratory Distress Observation Scale)
==============================================

Quantifies respiratory distress in patients unable to self-report symptoms.

Reference:
- Campbell ML. Psychometric testing of a respiratory distress observation scale. 
  J Palliat Med. 2008;11(1):44-50.

RDOS Components (8 items, 0-2 points each):
1. Restlessness (0-2)
2. Accessory muscle use (0-2)
3. Paradoxical breathing pattern (0-2)
4. Nasal flaring (0-2)
5. Look of fear (0-2)
6. Grunting at end-expiration (0-2)
7. Heart rate (0-2)
8. Respiratory rate (0-2)

Total: 0-16 points

Interpretation:
- 0-3: No respiratory distress
- 4-6: Mild respiratory distress
- 7-10: Moderate respiratory distress
- 11-16: Severe respiratory distress

Clinical Utility:
- Assesses respiratory distress in non-verbal patients
- Used in ICU, emergency, and palliative care
- Helps guide treatment decisions
- Monitors response to treatment
"""

import streamlit as st
from scores.utils.validation import validate_age
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_rdos(
    restlessness: int,
    accessory_muscles: int,
    paradoxical_breathing: int,
    nasal_flaring: int,
    look_of_fear: int,
    grunting: int,
    heart_rate: int,
    respiratory_rate: int
) -> dict:
    """
    Calculate RDOS Score
    
    Args:
        restlessness: Restlessness score (0-2)
        accessory_muscles: Accessory muscle use score (0-2)
        paradoxical_breathing: Paradoxical breathing score (0-2)
        nasal_flaring: Nasal flaring score (0-2)
        look_of_fear: Look of fear score (0-2)
        grunting: Grunting score (0-2)
        heart_rate: Heart rate score (0-2)
        respiratory_rate: Respiratory rate score (0-2)
    
    Returns:
        Dictionary with RDOS score, severity, and interpretation
    """
    score = (
        restlessness +
        accessory_muscles +
        paradoxical_breathing +
        nasal_flaring +
        look_of_fear +
        grunting +
        heart_rate +
        respiratory_rate
    )
    
    # Severity interpretation
    if score <= 3:
        severity = "Không có suy hô hấp"
        interpretation = "Bệnh nhân không có dấu hiệu suy hô hấp"
        recommendation = "Tiếp tục theo dõi"
    elif score <= 6:
        severity = "Suy hô hấp nhẹ"
        interpretation = "Có dấu hiệu suy hô hấp nhẹ"
        recommendation = "Theo dõi sát, cung cấp oxy nếu cần"
    elif score <= 10:
        severity = "Suy hô hấp trung bình"
        interpretation = "Có dấu hiệu suy hô hấp trung bình"
        recommendation = "Cung cấp oxy, cân nhắc hỗ trợ hô hấp"
    else:
        severity = "Suy hô hấp nặng"
        interpretation = "Có dấu hiệu suy hô hấp nặng"
        recommendation = "Hỗ trợ hô hấp ngay, cân nhắc thở máy"
    
    return {
        "score": score,
        "severity": severity,
        "interpretation": interpretation,
        "recommendation": recommendation
    }


def render():
    """Render RDOS interface"""
    import streamlit as st
    
    st.set_page_config(page_title="RDOS", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown("""
    <h2 style='text-align: center; color: #10B981;'>🫁 RDOS</h2>
    <p style='text-align: center; color: #6B7280;'>
    Respiratory Distress Observation Scale<br>
    Định lượng suy hô hấp ở bệnh nhân không thể tự báo cáo triệu chứng
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về RDOS"):
        st.markdown("""
        **RDOS (Respiratory Distress Observation Scale)** là thang điểm đánh giá suy hô hấp 
        ở bệnh nhân không thể tự báo cáo triệu chứng (ví dụ: trẻ em, bệnh nhân hôn mê, 
        bệnh nhân chăm sóc giảm nhẹ).
        
        ### Các thành phần (8 mục, mỗi mục 0-2 điểm):
        1. **Restlessness (Bồn chồn):** 0 = Không, 1 = Nhẹ, 2 = Nặng
        2. **Accessory muscle use (Dùng cơ phụ):** 0 = Không, 1 = Nhẹ, 2 = Nặng
        3. **Paradoxical breathing (Thở nghịch thường):** 0 = Không, 1 = Có
        4. **Nasal flaring (Phập phồng cánh mũi):** 0 = Không, 1 = Có
        5. **Look of fear (Vẻ sợ hãi):** 0 = Không, 1 = Có
        6. **Grunting (Rên rỉ):** 0 = Không, 1 = Có
        7. **Heart rate (Nhịp tim):** 0 = Bình thường, 1 = Tăng nhẹ, 2 = Tăng nhiều
        8. **Respiratory rate (Tần số thở):** 0 = Bình thường, 1 = Tăng nhẹ, 2 = Tăng nhiều
        
        ### Phân loại:
        - **0-3 điểm:** Không có suy hô hấp
        - **4-6 điểm:** Suy hô hấp nhẹ
        - **7-10 điểm:** Suy hô hấp trung bình
        - **11-16 điểm:** Suy hô hấp nặng
        
        ### Ứng dụng lâm sàng:
        - Đánh giá suy hô hấp ở bệnh nhân không thể tự báo cáo
        - Dùng trong ICU, cấp cứu, và chăm sóc giảm nhẹ
        - Hướng dẫn quyết định điều trị
        - Theo dõi đáp ứng điều trị
        """)
    
    # Input section
    st.markdown("### 📊 Đánh giá lâm sàng")
    
    st.markdown("#### 1. Restlessness (Bồn chồn)")
    restlessness = st.slider(
        "Mức độ bồn chồn",
        min_value=0,
        max_value=2,
        value=0,
        step=1,
        key="rdos_restlessness",
        help="0 = Không, 1 = Nhẹ, 2 = Nặng"
    )
    
    st.markdown("#### 2. Accessory Muscle Use (Dùng cơ phụ)")
    accessory_muscles = st.slider(
        "Dùng cơ phụ hô hấp",
        min_value=0,
        max_value=2,
        value=0,
        step=1,
        key="rdos_accessory",
        help="0 = Không, 1 = Nhẹ, 2 = Nặng"
    )
    
    st.markdown("#### 3. Paradoxical Breathing (Thở nghịch thường)")
    paradoxical_breathing = st.selectbox(
        "Thở nghịch thường",
        [0, 1],
        key="rdos_paradoxical",
        help="0 = Không, 1 = Có"
    )
    
    st.markdown("#### 4. Nasal Flaring (Phập phồng cánh mũi)")
    nasal_flaring = st.selectbox(
        "Phập phồng cánh mũi",
        [0, 1],
        key="rdos_nasal",
        help="0 = Không, 1 = Có"
    )
    
    st.markdown("#### 5. Look of Fear (Vẻ sợ hãi)")
    look_of_fear = st.selectbox(
        "Vẻ sợ hãi",
        [0, 1],
        key="rdos_fear",
        help="0 = Không, 1 = Có"
    )
    
    st.markdown("#### 6. Grunting (Rên rỉ khi thở ra)")
    grunting = st.selectbox(
        "Rên rỉ khi thở ra",
        [0, 1],
        key="rdos_grunting",
        help="0 = Không, 1 = Có"
    )
    
    st.markdown("#### 7. Heart Rate (Nhịp tim)")
    heart_rate = st.slider(
        "Nhịp tim",
        min_value=0,
        max_value=2,
        value=0,
        step=1,
        key="rdos_hr",
        help="0 = Bình thường, 1 = Tăng nhẹ, 2 = Tăng nhiều"
    )
    
    st.markdown("#### 8. Respiratory Rate (Tần số thở)")
    respiratory_rate = st.slider(
        "Tần số thở",
        min_value=0,
        max_value=2,
        value=0,
        step=1,
        key="rdos_rr",
        help="0 = Bình thường, 1 = Tăng nhẹ, 2 = Tăng nhiều"
    )
    
    if st.button("🔬 Tính điểm RDOS", type="primary", use_container_width=True):
        result = calculate_rdos(
            restlessness=restlessness,
            accessory_muscles=accessory_muscles,
            paradoxical_breathing=paradoxical_breathing,
            nasal_flaring=nasal_flaring,
            look_of_fear=look_of_fear,
            grunting=grunting,
            heart_rate=heart_rate,
            respiratory_rate=respiratory_rate
        )
        
        # Display results
        st.markdown("---")
        st.markdown("### 📋 Kết quả RDOS")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Điểm RDOS", f"{result['score']}/16")
        
        with col2:
            st.metric(
                "Mức độ",
                result['severity']
            )
        
        # Interpretation
        st.markdown("### 💡 Diễn giải và khuyến nghị")
        
        if result['score'] <= 3:
            st.success(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
        elif result['score'] <= 6:
            st.info(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown("""
            - Cung cấp oxy nếu SpO2 <94%
            - Theo dõi sát
            - Đánh giá lại sau 30-60 phút
            """)
        elif result['score'] <= 10:
            st.warning(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown("""
            - Cung cấp oxy (có thể cần mask có túi)
            - Cân nhắc hỗ trợ hô hấp không xâm lấn (NIV)
            - Theo dõi sát tại bệnh viện
            - Đánh giá nguyên nhân
            """)
        else:
            st.error(f"**{result['severity']}** - {result['interpretation']}")
            st.markdown(f"**Khuyến nghị:** {result['recommendation']}")
            st.markdown("""
            - **Hỗ trợ hô hấp ngay lập tức**
            - Cân nhắc thở máy
            - Đánh giá nguyên nhân khẩn cấp
            - Theo dõi tại ICU
            - Có thể cần đặt nội khí quản
            """)
        
        # Save to history
        save_calculation_to_history(
            calculator_id="rdos",
            calculator_name="RDOS",
            inputs={
                "Bồn chồn": f"{restlessness}",
                "Dùng cơ phụ": f"{accessory_muscles}",
                "Thở nghịch thường": f"{paradoxical_breathing}",
                "Phập phồng cánh mũi": f"{nasal_flaring}",
                "Vẻ sợ hãi": f"{look_of_fear}",
                "Rên rỉ": f"{grunting}",
                "Nhịp tim": f"{heart_rate}",
                "Tần số thở": f"{respiratory_rate}"
            },
            result={
                "Điểm": f"{result['score']}/16",
                "Mức độ": result['severity']
            }
        )
        
        # Share and export
        render_share_section(
            calculator_id="rdos",
            calculator_name="RDOS"
        )
        
        render_export_section(
            calculator_id="rdos",
            calculator_name="RDOS",
            data={
                "inputs": {
                    "restlessness": restlessness,
                    "accessory_muscles": accessory_muscles,
                    "paradoxical_breathing": paradoxical_breathing,
                    "nasal_flaring": nasal_flaring,
                    "look_of_fear": look_of_fear,
                    "grunting": grunting,
                    "heart_rate": heart_rate,
                    "respiratory_rate": respiratory_rate
                },
                "result": result
            }
        )
    
    # History
    render_history_ui(calculator_id="rdos", show_actions=True)
    
    # References
    references = get_references("RDOS")
    if references:
        render_references_section(references)

