"""
DHAKA Score (Dehydration: Assessing Kids Accurately)
=====================================================

Classifies dehydration in children <5 years with acute diarrhea.

Reference:
- Bailey B, et al. External validation of the Dehydration: Assessing Kids Accurately 
  (DHAKA) score in children with acute gastroenteritis. 
  Acad Emerg Med. 2016;23(8):908-913.

DHAKA Score Components (4 items):
1. General appearance (0-2 points)
2. Skin pinch (0-2 points)
3. Tears (0-1 point)
4. Respiratory rate (0-1 point)

Total: 0-6 points

Dehydration Categories:
- 0-3 points: No dehydration or mild (<5%)
- 4-5 points: Moderate dehydration (5-10%)
- 6 points: Severe dehydration (>10%)

Clinical Utility:
- Quick assessment of dehydration in young children
- Guides fluid replacement therapy
- Used in emergency and pediatrics
- Helps prevent complications
"""

import streamlit as st
from scores.utils.validation import validate_age
from components.ui.validation import render_validation_errors
from config.theme import COLORS
from components.ui.results import render_result_box
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_dhaka(
    general_appearance: int,
    skin_pinch: int,
    tears: int,
    respiratory_rate: int
) -> dict:
    """
    Calculate DHAKA Score
    
    Args:
        general_appearance: General appearance (0-2)
        skin_pinch: Skin pinch test (0-2)
        tears: Tears present (0-1)
        respiratory_rate: Respiratory rate (0-1)
    
    Returns:
        Dictionary with DHAKA score, dehydration category, and treatment
    """
    total_score = general_appearance + skin_pinch + tears + respiratory_rate
    
    # Dehydration category
    if total_score <= 3:
        category = "Không mất nước hoặc nhẹ"
        dehydration_percent = "<5%"
        treatment = "Điều trị tại nhà với ORS"
        color = COLORS["success"]
        icon = "✅"
    elif total_score <= 5:
        category = "Mất nước trung bình"
        dehydration_percent = "5-10%"
        treatment = "Điều trị tại bệnh viện với ORS hoặc truyền dịch"
        color = COLORS["warning"]
        icon = "⚠️"
    else:
        category = "Mất nước nặng"
        dehydration_percent = ">10%"
        treatment = "Truyền dịch tĩnh mạch ngay, nhập viện"
        color = COLORS["error"]
        icon = "🚨"
    
    return {
        "score": total_score,
        "category": category,
        "dehydration_percent": dehydration_percent,
        "treatment": treatment,
        "color": color,
        "icon": icon
    }


def render():
    """Render DHAKA Score interface"""
    import streamlit as st
    
    st.set_page_config(page_title="DHAKA Score", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown(f"<h2 style='text-align: center; color: {COLORS['success']};'>👶 DHAKA Score</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center;'>Dehydration: Assessing Kids Accurately - Phân loại mất nước ở trẻ em <5 tuổi bị tiêu chảy cấp</p>", unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về DHAKA Score"):
        st.markdown("""
        **DHAKA Score (Dehydration: Assessing Kids Accurately)** là thang điểm đánh giá 
        nhanh mất nước ở trẻ em <5 tuổi bị tiêu chảy cấp.
        
        ### Các thành phần (4 mục):
        1. **General Appearance (Tổng trạng):** 0-2 điểm
           - 0 = Bình thường, vui vẻ
           - 1 = Khó chịu, quấy khóc
           - 2 = Lờ đờ, hôn mê
        
        2. **Skin Pinch (Nếp véo da):** 0-2 điểm
           - 0 = Trở lại ngay (<1 giây)
           - 1 = Trở lại chậm (1-2 giây)
           - 2 = Trở lại rất chậm (>2 giây)
        
        3. **Tears (Nước mắt):** 0-1 điểm
           - 0 = Có nước mắt
           - 1 = Không có nước mắt
        
        4. **Respiratory Rate (Tần số thở):** 0-1 điểm
           - 0 = Bình thường
           - 1 = Tăng
        
        ### Phân loại mất nước:
        - **0-3 điểm:** Không mất nước hoặc nhẹ (<5%)
        - **4-5 điểm:** Mất nước trung bình (5-10%)
        - **6 điểm:** Mất nước nặng (>10%)
        
        ### Ứng dụng lâm sàng:
        - Đánh giá nhanh mất nước ở trẻ nhỏ
        - Hướng dẫn điều trị bù dịch
        - Dùng trong cấp cứu và nhi khoa
        - Giúp phòng ngừa biến chứng
        """)
    
    # Input section
    st.markdown("### 📊 Đánh giá lâm sàng")
    
    st.markdown("#### 1. General Appearance (Tổng trạng)")
    general_appearance = st.selectbox(
        "Tổng trạng",
        ["Bình thường, vui vẻ (0 điểm)", "Khó chịu, quấy khóc (1 điểm)", "Lờ đờ, hôn mê (2 điểm)"],
        key="dhaka_appearance"
    )
    general_appearance_score = general_appearance.split("(")[1].split(" điểm")[0]
    general_appearance_score = int(general_appearance_score)
    
    st.markdown("#### 2. Skin Pinch (Nếp véo da)")
    skin_pinch = st.selectbox(
        "Nếp véo da",
        ["Trở lại ngay <1 giây (0 điểm)", "Trở lại chậm 1-2 giây (1 điểm)", "Trở lại rất chậm >2 giây (2 điểm)"],
        key="dhaka_skin"
    )
    skin_pinch_score = int(skin_pinch.split("(")[1].split(" điểm")[0])
    
    st.markdown("#### 3. Tears (Nước mắt)")
    tears = st.selectbox(
        "Nước mắt",
        ["Có nước mắt (0 điểm)", "Không có nước mắt (1 điểm)"],
        key="dhaka_tears"
    )
    tears_score = int(tears.split("(")[1].split(" điểm")[0])
    
    st.markdown("#### 4. Respiratory Rate (Tần số thở)")
    respiratory_rate = st.selectbox(
        "Tần số thở",
        ["Bình thường (0 điểm)", "Tăng (1 điểm)"],
        key="dhaka_rr"
    )
    respiratory_rate_score = int(respiratory_rate.split("(")[1].split(" điểm")[0])
    
    if st.button("🔬 Tính điểm DHAKA", type="primary", use_container_width=True):
        result = calculate_dhaka(
            general_appearance=general_appearance_score,
            skin_pinch=skin_pinch_score,
            tears=tears_score,
            respiratory_rate=respiratory_rate_score
        )
        
        # Display results
        st.markdown("---")
        st.markdown("### 📋 Kết quả DHAKA Score")
        
        render_result_box(
            title="DHAKA Score",
            value=f"{result['score']}/6",
            subtitle=result['category'],
            color=result['color'],
            icon=result['icon'],
            size="large"
        )
        
        col1, col2 = st.columns(2)
        with col1:
             st.metric("Tỷ lệ mất nước", result['dehydration_percent'])
        with col2:
             st.metric("Phân loại", result['category'])
        
        # Treatment recommendations
        st.markdown("### 💡 Khuyến nghị điều trị")
        
        if result['score'] <= 3:
            st.success(f"**{result['category']}** - Mất nước {result['dehydration_percent']}")
            st.markdown(f"**Điều trị:** {result['treatment']}")
            st.markdown("""
            - Điều trị tại nhà với ORS (Oral Rehydration Solution)
            - Cho uống ORS sau mỗi lần đi tiêu chảy
            - Tiếp tục cho bú/ăn bình thường
            - Theo dõi tại nhà
            - Tái khám nếu không cải thiện hoặc xấu đi
            """)
        elif result['score'] <= 5:
            st.warning(f"**{result['category']}** - Mất nước {result['dehydration_percent']}")
            st.markdown(f"**Điều trị:** {result['treatment']}")
            st.markdown("""
            - Điều trị tại bệnh viện
            - ORS đường uống nếu trẻ có thể uống
            - Hoặc truyền dịch tĩnh mạch (NaCl 0.9% hoặc Ringer Lactate)
            - Liều: 50-100 mL/kg trong 2-4 giờ đầu
            - Theo dõi sát tại bệnh viện
            - Đánh giá lại sau 2-4 giờ
            """)
        else:
            st.error(f"**{result['category']}** - Mất nước {result['dehydration_percent']}")
            st.markdown(f"**Điều trị:** {result['treatment']}")
            st.markdown("""
            - **Truyền dịch tĩnh mạch ngay lập tức**
            - Nhập viện
            - Liều: 100 mL/kg trong 2-4 giờ đầu
            - Dung dịch: NaCl 0.9% hoặc Ringer Lactate
            - Theo dõi sát tại bệnh viện
            - Đánh giá lại mỗi 1-2 giờ
            - Cân nhắc bù kali nếu cần
            - Theo dõi điện giải
            """)
        
        # Save to history
        save_calculation_to_history(
            calculator_id="dhaka",
            calculator_name="DHAKA Score",
            inputs={
                "Tổng trạng": general_appearance,
                "Nếp véo da": skin_pinch,
                "Nước mắt": tears,
                "Tần số thở": respiratory_rate
            },
            result={
                "Điểm": f"{result['score']}/6",
                "Mức độ": result['category'],
                "Tỷ lệ mất nước": result['dehydration_percent']
            }
        )
        
        # Share and export
        render_share_section(
            calculator_id="dhaka",
            calculator_name="DHAKA Score"
        )
        
        render_export_section(
            calculator_id="dhaka",
            calculator_name="DHAKA Score",
            data={
                "inputs": {
                    "general_appearance": general_appearance_score,
                    "skin_pinch": skin_pinch_score,
                    "tears": tears_score,
                    "respiratory_rate": respiratory_rate_score
                },
                "result": result
            }
        )
    
    # History
    render_history_ui(calculator_id="dhaka", show_actions=True)
    
    # References
    references = get_references("DHAKA Score")
    if references:
        render_references_section(references)

