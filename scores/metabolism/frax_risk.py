"""
FRAX Risk Interpretation
Nhập kết quả FRAX 10 năm (major / hip) và so sánh ngưỡng điều trị
"""

import streamlit as st
from scores.utils.validation import validate_age, validate_range
from components.ui.validation import render_validation_errors
from components.ui.results import render_result_box
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section


def classify_frax(
    major: float,
    hip: float,
    treat_major: float,
    treat_hip: float,
    very_high_major: float,
    very_high_hip: float,
    fragility_fracture: bool,
) -> tuple[str, str, str]:
    """
    Trả về (category, color, recommendation) dựa trên % FRAX và gãy xương.
    """
    if fragility_fracture or major >= very_high_major or hip >= very_high_hip:
        return (
            "Nguy cơ rất cao",
            "error",
            "Điều trị mạnh (cân nhắc thuốc tạo xương hoặc khởi trị sớm, sau đó duy trì chống hủy xương).",
        )
    if major >= treat_major or hip >= treat_hip:
        return (
            "Nguy cơ cao",
            "warning",
            "Cân nhắc điều trị thuốc chống hủy xương + Ca/Vit D + phòng té ngã; cá thể hóa theo guideline quốc gia.",
        )
    if major >= 7.5 or hip >= 1.5:
        return (
            "Nguy cơ trung bình",
            "info",
            "Tối ưu lối sống, Ca/Vit D, phòng té ngã; cân nhắc điều trị nếu có thêm yếu tố nguy cơ.",
        )
    return (
        "Nguy cơ thấp",
        "success",
        "Duy trì lối sống, tập luyện, Ca/Vit D đầy đủ và theo dõi định kỳ.",
    )


def render():
    """Render FRAX interpretation"""
    st.markdown(
        """
        <h2 style='text-align:center;color:#0EA5E9'>🦴 Ước tính nguy cơ gãy xương (FRAX)</h2>
        <p style='text-align:center'><em>Nhập % FRAX 10 năm → Phân loại nguy cơ & gợi ý hành động</em></p>
        """,
        unsafe_allow_html=True,
    )

    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "frax":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'FRAX')}")
        if "shared_inputs" not in st.session_state:
            st.session_state["shared_inputs"] = shared.get("inputs", {})

    st.markdown(
        """
        **Lưu ý:**
        - FRAX áp dụng tốt nhất cho người **chưa điều trị** và **40–90 tuổi**.
        - Ngưỡng điều trị thay đổi theo quốc gia; mặc định dùng NOF (Major ≥20% hoặc Hip ≥3%). Có thể chỉnh bên dưới.
        """
    )
    st.markdown("---")

    col_main, col_suggest = st.columns([2, 1])
    with col_suggest:
        render_suggestions(
            calculator_id="frax",
            calculator_name="Ước tính nguy cơ gãy xương (FRAX)",
            category="Nội tiết",
            show_related=True,
            show_category=True,
            limit=3,
        )

    with col_main:
        col1, col2 = st.columns(2)
        age = col1.number_input(
            "Tuổi",
            min_value=40,
            max_value=95,
            value=65,
            step=1,
            help="FRAX được chuẩn hóa cho 40–90 tuổi.",
        )
        sex = col2.radio(
            "Giới",
            options=["female", "male"],
            format_func=lambda x: "Nữ" if x == "female" else "Nam",
            horizontal=True,
        )

        st.markdown("### 📥 Nhập kết quả FRAX (10 năm)")
        major = st.number_input(
            "Major osteoporotic fracture (%)",
            min_value=0.0,
            max_value=80.0,
            value=15.0,
            step=0.1,
            format="%.1f",
            help="Gãy chính: đốt sống lâm sàng, cổ đùi, cẳng tay gần, vai gần.",
        )
        hip = st.number_input(
            "Hip fracture (%)",
            min_value=0.0,
            max_value=50.0,
            value=2.5,
            step=0.1,
            format="%.1f",
        )

        st.markdown("### 🎯 Ngưỡng điều trị (có thể chỉnh)")
        col_t1, col_t2, col_t3 = st.columns(3)
        treat_major = col_t1.number_input(
            "Ngưỡng điều trị Major (%)",
            min_value=5.0,
            max_value=50.0,
            value=20.0,
            step=0.5,
        )
        treat_hip = col_t2.number_input(
            "Ngưỡng điều trị Hip (%)",
            min_value=1.0,
            max_value=15.0,
            value=3.0,
            step=0.1,
        )
        very_high_factor = col_t3.number_input(
            "Hệ số 'rất cao' (× ngưỡng)",
            min_value=1.0,
            max_value=3.0,
            value=1.5,
            step=0.1,
            help="Mặc định 1.5 lần ngưỡng điều trị.",
        )
        very_high_major = treat_major * very_high_factor
        very_high_hip = treat_hip * very_high_factor

        fragility_fracture = st.checkbox(
            "Đã có gãy xương do chấn thương nhẹ (đốt sống/cổ đùi/cổ tay)?",
            value=False,
        )

        st.markdown("---")
        if st.button("🧮 Đánh giá nguy cơ FRAX", type="primary", use_container_width=True):
            validation_errors = []
            ok_age, err_age = validate_age(age, 40, 95)
            if not ok_age:
                validation_errors.append(err_age)
            ok_major, err_major = validate_range(major, 0.0, 80.0, "FRAX Major (%)")
            if not ok_major:
                validation_errors.append(err_major)
            ok_hip, err_hip = validate_range(hip, 0.0, 50.0, "FRAX Hip (%)")
            if not ok_hip:
                validation_errors.append(err_hip)

            if validation_errors:
                render_validation_errors(validation_errors)
                return

            category, color, rec = classify_frax(
                major=major,
                hip=hip,
                treat_major=treat_major,
                treat_hip=treat_hip,
                very_high_major=very_high_major,
                very_high_hip=very_high_hip,
                fragility_fracture=fragility_fracture,
            )

            icon = "✅" if color == "success" else "⚠️" if color in ("warning", "info") else "🚨"
            render_result_box(
                title="Kết luận FRAX",
                value=category,
                subtitle=f"Major: {major:.1f}% | Hip: {hip:.1f}%",
                color=color,
                icon=icon,
                size="large",
            )
            st.info(rec)
            st.markdown(
                f"""
**Ngưỡng đang dùng:** Major ≥ {treat_major:.1f}% hoặc Hip ≥ {treat_hip:.1f}%.

- Gãy xương do chấn thương nhẹ: {'Có' if fragility_fracture else 'Không'}
- Giới/tuổi: {'Nữ' if sex=='female' else 'Nam'}, {age} tuổi
- Ngưỡng 'rất cao': Major ≥ {very_high_major:.1f}% hoặc Hip ≥ {very_high_hip:.1f}%
"""
            )

            inputs_dict = {
                "Age": age,
                "Sex": "Nữ" if sex == "female" else "Nam",
                "FRAX Major (%)": major,
                "FRAX Hip (%)": hip,
                "Fragility fracture": fragility_fracture,
                "Treat Major (%)": treat_major,
                "Treat Hip (%)": treat_hip,
                "Very high Major (%)": very_high_major,
                "Very high Hip (%)": very_high_hip,
            }
            results_dict = {
                "Category": category,
                "Recommendation": rec,
                "Major (%)": round(major, 1),
                "Hip (%)": round(hip, 1),
            }

            render_export_section(
                title=f"FRAX: {category}",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="Ước tính nguy cơ gãy xương (FRAX)",
                filename="frax_risk",
            )

            save_calculation_to_history(
                calculator_id="frax",
                calculator_name="Ước tính nguy cơ gãy xương (FRAX)",
                inputs=inputs_dict,
                results=results_dict,
            )
            render_share_section(
                calculator_id="frax",
                calculator_name="Ước tính nguy cơ gãy xương (FRAX)",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True,
            )
            st.markdown("---")
            render_history_ui(calculator_id="frax", show_actions=True)

    st.markdown("---")
    st.subheader("📋 Tóm tắt ngưỡng (có thể thay đổi)")
    st.markdown(
        """
| Mức nguy cơ | Gợi ý hành động |
|-------------|-----------------|
| Rất cao | Gãy xương do chấn thương nhẹ **hoặc** FRAX vượt ~1.5× ngưỡng điều trị |
| Cao | Major ≥ ngưỡng điều trị **hoặc** Hip ≥ ngưỡng điều trị |
| Trung bình | Major 7.5–<ngưỡng điều trị **hoặc** Hip 1.5–<ngưỡng điều trị |
| Thấp | Dưới các mức trên |
"""
    )

    references = get_references("FRAX")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True,
        )


if __name__ == "__main__":
    render()


