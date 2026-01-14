"""
DXA Osteoporosis Interpretation
Diễn giải T-score/Z-score, phân loại loãng xương và gợi ý hành động
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


T_SCORE_MIN, T_SCORE_MAX = -6.0, 2.0


def classify_t_score(t_score: float, fragility_fracture: bool) -> tuple[str, str, str]:
    """
    Phân loại T-score; nếu đã có gãy xương do chấn thương nhẹ → coi như loãng xương lâm sàng.
    Trả về (category, color, recommendation)
    """
    if fragility_fracture:
        return (
            "Loãng xương (gãy xương do chấn thương nhẹ)",
            "error",
            "Điều trị loãng xương; đánh giá nguyên nhân thứ phát và phòng té ngã.",
        )
    if t_score <= -2.5:
        return (
            "Loãng xương",
            "error",
            "Cân nhắc điều trị thuốc, bổ sung Ca/Vit D và phòng té ngã.",
        )
    if -2.5 < t_score < -1.0:
        return (
            "Giảm mật độ xương (Osteopenia)",
            "warning",
            "Đánh giá nguy cơ (FRAX), tối ưu lối sống và canxi/vitamin D.",
        )
    return (
        "Bình thường",
        "success",
        "Duy trì lối sống lành mạnh; theo dõi lại theo khuyến cáo.",
    )


def render():
    """Render DXA interpretation calculator"""
    st.markdown(
        """
        <h2 style='text-align:center;color:#0EA5E9'>🦴 Đo loãng xương (DXA)</h2>
        <p style='text-align:center'><em>T-score/Z-score • Phân loại • Khuyến nghị</em></p>
        """,
        unsafe_allow_html=True,
    )

    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "osteoporosis_dxa":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'DXA Loãng xương')}")
        if "shared_inputs" not in st.session_state:
            st.session_state["shared_inputs"] = shared.get("inputs", {})

    st.markdown(
        """
        **Mục đích:** Diễn giải DXA nhanh, xác định **bình thường / osteopenia / loãng xương**
        và nhắc ngưỡng điều trị khi có gãy xương do chấn thương nhẹ.

        - Dùng T-score cho **nữ sau mãn kinh & nam ≥50**.
        - Z-score hữu ích ở <50 tuổi, tiền mãn kinh hoặc nam trẻ để gợi ý nguyên nhân thứ phát.
        """
    )
    st.markdown("---")

    # Smart suggestions on the side
    col_main, col_suggest = st.columns([2, 1])
    with col_suggest:
        render_suggestions(
            calculator_id="osteoporosis_dxa",
            calculator_name="Đo loãng xương (DXA)",
            category="Nội tiết",
            show_related=True,
            show_category=True,
            limit=3,
        )

    with col_main:
        col1, col2 = st.columns(2)
        age = col1.number_input(
            "Tuổi",
            min_value=18,
            max_value=100,
            value=60,
            step=1,
            help="FRAX thường áp dụng 40-90; DXA dùng cho mọi lứa tuổi cần đánh giá.",
        )
        sex = col2.radio(
            "Giới",
            options=["female", "male"],
            format_func=lambda x: "Nữ" if x == "female" else "Nam",
            horizontal=True,
        )

        st.markdown("### 📊 T-score (chọn vị trí đại diện để kết luận)")
        site = st.radio(
            "Vị trí dùng để phân loại",
            options=[
                "Cổ xương đùi",
                "Total hip",
                "Cột sống thắt lưng (L1-L4)",
            ],
            index=0,
            horizontal=False,
        )

        col_ts1, col_ts2, col_ts3 = st.columns(3)
        t_femoral = col_ts1.number_input(
            "T-score cổ xương đùi",
            min_value=T_SCORE_MIN,
            max_value=T_SCORE_MAX,
            value=-2.5,
            step=0.1,
            format="%.1f",
        )
        t_total = col_ts2.number_input(
            "T-score total hip",
            min_value=T_SCORE_MIN,
            max_value=T_SCORE_MAX,
            value=-1.8,
            step=0.1,
            format="%.1f",
        )
        t_spine = col_ts3.number_input(
            "T-score L1-L4",
            min_value=T_SCORE_MIN,
            max_value=T_SCORE_MAX,
            value=-2.9,
            step=0.1,
            format="%.1f",
        )

        st.markdown("### 🧭 Z-score (tùy chọn, hữu ích <50 tuổi hoặc tiền mãn kinh)")
        col_z1, col_z2 = st.columns(2)
        use_z = col_z1.checkbox("Nhập Z-score", value=False)
        z_score = col_z2.number_input(
            "Z-score (nếu có)",
            min_value=-6.0,
            max_value=3.0,
            value=-0.5,
            step=0.1,
            format="%.1f",
            disabled=not use_z,
            help="Z-score < -2.0 gợi ý xem xét nguyên nhân thứ phát.",
        )

        fragility_fracture = st.checkbox(
            "Đã có gãy xương do chấn thương nhẹ (cổ đùi/cột sống/cổ tay)?",
            value=False,
        )

        st.markdown("---")
        if st.button("🧮 Diễn giải DXA", type="primary", use_container_width=True):
            validation_errors = []
            ok_age, err_age = validate_age(age, 18, 100)
            if not ok_age:
                validation_errors.append(err_age)

            # pick selected site value
            site_value = {
                "Cổ xương đùi": t_femoral,
                "Total hip": t_total,
                "Cột sống thắt lưng (L1-L4)": t_spine,
            }.get(site)

            ok_t, err_t = validate_range(site_value, T_SCORE_MIN, T_SCORE_MAX, f"T-score {site}")
            if not ok_t:
                validation_errors.append(err_t)

            if validation_errors:
                render_validation_errors(validation_errors)
                return

            category, color, recommendation = classify_t_score(site_value, fragility_fracture)

            z_flag = use_z and z_score <= -2.0
            z_note = "Z-score < -2: cân nhắc nguyên nhân thứ phát (thiếu vitamin D, nội tiết, thuốc…)." if z_flag else ""

            render_result_box(
                title=f"📑 Kết luận tại {site}",
                value=category,
                subtitle=f"T-score: {site_value:.1f}",
                color=color,
                icon="✅" if color == "success" else "⚠️" if color == "warning" else "🚨",
                size="large",
            )
            st.info(
                f"""
**Khuyến nghị:** {recommendation}

{z_note}
"""
            )

            st.markdown("### 🗂️ Chi tiết nhập")
            st.markdown(
                f"- Tuổi/Giới: **{age}**, {'Nữ' if sex=='female' else 'Nam'}\n"
                f"- T-score: Cổ đùi {t_femoral:.1f} • Total hip {t_total:.1f} • L1-L4 {t_spine:.1f}\n"
                f"- Gãy xương do chấn thương nhẹ: {'Có' if fragility_fracture else 'Không'}"
            )
            if use_z:
                st.markdown(f"- Z-score: **{z_score:.1f}**")

            inputs_dict = {
                "Age": age,
                "Sex": "Nữ" if sex == "female" else "Nam",
                "Site": site,
                "T-score (FN)": round(t_femoral, 1),
                "T-score (Total hip)": round(t_total, 1),
                "T-score (Spine)": round(t_spine, 1),
                "Fragility fracture": fragility_fracture,
                "Z-score": round(z_score, 1) if use_z else None,
            }
            results_dict = {
                "Classification": category,
                "Site used": site,
                "T-score used": round(site_value, 1),
                "Recommendation": recommendation,
                "Z-score flag": "Z < -2, xem xét thứ phát" if z_flag else "",
            }

            render_export_section(
                title=f"DXA: {category}",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="Đo loãng xương (DXA)",
                filename="dxa_osteoporosis",
            )

            save_calculation_to_history(
                calculator_id="osteoporosis_dxa",
                calculator_name="Đo loãng xương (DXA)",
                inputs=inputs_dict,
                results=results_dict,
            )
            render_share_section(
                calculator_id="osteoporosis_dxa",
                calculator_name="Đo loãng xương (DXA)",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True,
            )

            st.markdown("---")
            render_history_ui(calculator_id="osteoporosis_dxa", show_actions=True)

    st.markdown("---")
    st.subheader("📋 Ngưỡng diễn giải nhanh")
    st.markdown(
        """
| Phân loại | T-score | Hành động gợi ý |
|-----------|---------|------------------|
| Bình thường | ≥ -1.0 | Duy trì lối sống, theo dõi |
| Osteopenia | -1.0 đến > -2.5 | Đánh giá FRAX, tối ưu Ca/Vit D, phòng té ngã |
| Loãng xương | ≤ -2.5 **hoặc** gãy xương do chấn thương nhẹ | Điều trị thuốc + phòng té ngã + tìm nguyên nhân |
"""
    )

    references = get_references("Osteoporosis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True,
        )


if __name__ == "__main__":
    render()


