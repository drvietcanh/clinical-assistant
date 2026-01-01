"""
EREFS (Eosinophilic Esophagitis Endoscopic Reference Score)
===========================================================

Evaluates severity of endoscopic findings in patients with eosinophilic esophagitis (EoE).

Reference:
- Hirano I, et al. Endoscopic assessment of the oesophagus: 
  Eosinophilic oesophagitis and other eosinophilic oedema. 
  Nat Rev Gastroenterol Hepatol. 2013;10(3):142-152.

EREFS Components (5 features):
- E: Exudates (white plaques) - 0-2
- R: Rings (trachealization) - 0-3
- E: Edema (loss of vascular pattern) - 0-1
- F: Furrows (vertical lines) - 0-1
- S: Strictures (narrowing) - 0-1

Total: 0-8 points

Severity:
- 0-2: Mild
- 3-5: Moderate
- 6-8: Severe

Clinical Utility:
- Standardized endoscopic assessment of EoE
- Monitors treatment response
- Guides therapy decisions
- Used in gastroenterology
"""

from config.theme import COLORS
from components.ui.validation import render_validation_errors
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_erefs(
    exudates: int,
    rings: int,
    edema: int,
    furrows: int,
    strictures: int
) -> dict:
    """
    Calculate EREFS Score
    
    Args:
        exudates: Exudates score (0-2)
        rings: Rings score (0-3)
        edema: Edema score (0-1)
        furrows: Furrows score (0-1)
        strictures: Strictures score (0-1)
    
    Returns:
        Dictionary with EREFS score, severity, and interpretation
    """
    total_score = exudates + rings + edema + furrows + strictures
    
    # Severity
    if total_score <= 2:
        severity = "Nhẹ"
        interpretation = "Tổn thương nội soi nhẹ"
        recommendation = "Điều trị theo tiêu chuẩn, theo dõi"
    elif total_score <= 5:
        severity = "Trung bình"
        interpretation = "Tổn thương nội soi trung bình"
        recommendation = "Điều trị tích cực, theo dõi sát"
    else:
        severity = "Nặng"
        interpretation = "Tổn thương nội soi nặng"
        recommendation = "Điều trị tích cực, có thể cần nong thực quản"
    
    return {
        "exudates": exudates,
        "rings": rings,
        "edema": edema,
        "furrows": furrows,
        "strictures": strictures,
        "total_score": total_score,
        "severity": severity,
        "interpretation": interpretation,
        "recommendation": recommendation
    }


def render():
    """Render EREFS interface"""
    import streamlit as st
    
    st.set_page_config(page_title="EREFS", layout="wide")
    
    # Check for shared result
    shared = load_shared_result_from_url()
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩺 EREFS</h3>
    <p style='text-align: center; color: #6B7280;'>
    Eosinophilic Esophagitis Endoscopic Reference Score<br>
    Đánh giá mức độ nặng của các phát hiện nội soi ở bệnh nhân viêm thực quản tăng bạch cầu ái toan (EoE)
    </p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về EREFS"):
        st.markdown("""
        **EREFS (Eosinophilic Esophagitis Endoscopic Reference Score)** là hệ thống đánh giá 
        chuẩn hóa mức độ nặng của các phát hiện nội soi ở bệnh nhân viêm thực quản tăng bạch cầu ái toan (EoE).
        
        ### Các thành phần (5 đặc điểm):
        1. **E - Exudates (Xuất tiết):** Mảng trắng - 0-2 điểm
        2. **R - Rings (Vòng):** Hình ảnh khí quản hóa - 0-3 điểm
        3. **E - Edema (Phù nề):** Mất mẫu mạch máu - 0-1 điểm
        4. **F - Furrows (Rãnh):** Đường dọc - 0-1 điểm
        5. **S - Strictures (Hẹp):** Hẹp thực quản - 0-1 điểm
        
        ### Phân loại mức độ:
        - **0-2 điểm:** Nhẹ
        - **3-5 điểm:** Trung bình
        - **6-8 điểm:** Nặng
        
        ### Ứng dụng lâm sàng:
        - Đánh giá chuẩn hóa nội soi EoE
        - Theo dõi đáp ứng điều trị
        - Hướng dẫn quyết định điều trị
        - Dùng trong tiêu hóa
        """)
    
    # Input section
    st.markdown("### 📊 Đánh giá nội soi")
    
    st.markdown("#### E - Exudates (Xuất tiết - Mảng trắng)")
    exudates = st.selectbox(
        "Mức độ xuất tiết",
        ["0 = Không có", "1 = Nhẹ (<10% diện tích)", "2 = Nặng (≥10% diện tích)"],
        key="erefs_exudates"
    )
    exudates_score = int(exudates.split("=")[0].strip())
    
    st.markdown("#### R - Rings (Vòng - Hình ảnh khí quản hóa)")
    rings = st.selectbox(
        "Mức độ vòng",
        ["0 = Không có", "1 = Nhẹ (một vài vòng)", "2 = Trung bình (nhiều vòng)", "3 = Nặng (vòng dày đặc)"],
        key="erefs_rings"
    )
    rings_score = int(rings.split("=")[0].strip())
    
    st.markdown("#### E - Edema (Phù nề - Mất mẫu mạch máu)")
    edema = st.selectbox(
        "Phù nề",
        ["0 = Không có", "1 = Có"],
        key="erefs_edema"
    )
    edema_score = int(edema.split("=")[0].strip())
    
    st.markdown("#### F - Furrows (Rãnh - Đường dọc)")
    furrows = st.selectbox(
        "Rãnh",
        ["0 = Không có", "1 = Có"],
        key="erefs_furrows"
    )
    furrows_score = int(furrows.split("=")[0].strip())
    
    st.markdown("#### S - Strictures (Hẹp thực quản)")
    strictures = st.selectbox(
        "Hẹp",
        ["0 = Không có", "1 = Có"],
        key="erefs_strictures"
    )
    strictures_score = int(strictures.split("=")[0].strip())
    
    if st.button("🔬 Tính điểm EREFS", type="primary", use_container_width=True):
        result = calculate_erefs(
            exudates=exudates_score,
            rings=rings_score,
            edema=edema_score,
            furrows=furrows_score,
            strictures=strictures_score
        )
        
        # Display results
        # Determine color and icon based on severity
        if result['total_score'] <= 2:
            color = COLORS['success']
            icon = "🟢"
        elif result['total_score'] <= 5:
            color = COLORS['warning']
            icon = "🟡"
        else:
            color = COLORS['error']
            icon = "🔴"

        # Display results with render_score_result
        st.markdown("---")
        st.markdown("### 📋 Kết quả EREFS")
        
        render_score_result(
            title="EREFS Score",
            score=f"{result['total_score']}/8",
            interpretation=f"{result['severity']} - {result['interpretation']}",
            mortality=result['recommendation'],
            color=color,
            icon=icon,
            size="large"
        )
        
        # Breakdown
        st.markdown("### 📝 Chi tiết")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"- **Exudates:** {result['exudates']}/2")
            st.markdown(f"- **Rings:** {result['rings']}/3")
            st.markdown(f"- **Edema:** {result['edema']}/1")
        
        with col2:
            st.markdown(f"- **Furrows:** {result['furrows']}/1")
            st.markdown(f"- **Strictures:** {result['strictures']}/1")
        
        # Clinical recommendations (Detailed)
        st.markdown("### 💡 Khuyến nghị lâm sàng")
        
        if result['total_score'] <= 2:
            st.markdown("""
            - Điều trị theo tiêu chuẩn EoE
            - PPI, thuốc ức chế miễn dịch tại chỗ (fluticasone, budesonide)
            - Chế độ ăn loại trừ nếu cần
            - Theo dõi định kỳ
            - Nội soi lại sau 8-12 tuần điều trị
            """)
        elif result['total_score'] <= 5:
            st.markdown("""
            - Điều trị tích cực EoE
            - PPI + thuốc ức chế miễn dịch tại chỗ
            - Có thể cần chế độ ăn loại trừ nghiêm ngặt
            - Theo dõi sát
            - Nội soi lại sau 6-8 tuần điều trị
            - Cân nhắc điều trị toàn thân nếu không đáp ứng
            """)
        else:
            st.markdown("""
            - **Điều trị tích cực ngay**
            - PPI + thuốc ức chế miễn dịch tại chỗ liều cao
            - Chế độ ăn loại trừ nghiêm ngặt
            - Có thể cần điều trị toàn thân (corticosteroid)
            - **Cân nhắc nong thực quản** nếu có hẹp
            - Theo dõi sát
            - Nội soi lại sau 4-6 tuần điều trị
            - Tư vấn chuyên khoa tiêu hóa
            """)
        
        # Save to history
        save_calculation_to_history(
            calculator_id="erefs",
            calculator_name="EREFS",
            inputs={
                "Exudates": f"{result['exudates']}/2",
                "Rings": f"{result['rings']}/3",
                "Edema": f"{result['edema']}/1",
                "Furrows": f"{result['furrows']}/1",
                "Strictures": f"{result['strictures']}/1"
            },
            result={
                "Điểm": f"{result['total_score']}/8",
                "Mức độ": result['severity']
            }
        )
        
        # Share and export
        render_share_section(
            calculator_id="erefs",
            calculator_name="EREFS"
        )
        
        render_export_section(
            calculator_id="erefs",
            calculator_name="EREFS",
            data={
                "inputs": {
                    "exudates": result['exudates'],
                    "rings": result['rings'],
                    "edema": result['edema'],
                    "furrows": result['furrows'],
                    "strictures": result['strictures']
                },
                "result": result
            }
        )
    
    # History
    render_history_ui(calculator_id="erefs", show_actions=True)
    
    # References
    references = get_references("EREFS")
    if references:
        render_references_section(references)

