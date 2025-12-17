"""Streamlit UI for the DIRC calculator."""

from __future__ import annotations

import streamlit as st

from .calculator import DIRCCalculator


def render_dirc_calculator() -> None:
    """Render the DIRC calculator UI."""
    st.header("💉 Drug Infusion Rate Conversion (DIRC)")
    st.caption(
        "Chuyển đổi liều truyền giữa (mcg/kg/phút) và (mL/giờ) dựa trên cân nặng và nồng độ thuốc."
    )

    calculator = DIRCCalculator()

    # Select conversion direction
    conversion_label = st.radio(
        "Chọn loại chuyển đổi",
        options=[
            "mcg/kg/phút → mL/giờ",
            "mL/giờ → mcg/kg/phút",
        ],
        horizontal=False,
    )

    if "mcg/kg/phút" in conversion_label:
        calculator.set_conversion_type("mcg/kg/min to mL/hr")
    else:
        calculator.set_conversion_type("mL/hr to mcg/kg/min")

    col1, col2 = st.columns(2)

    with col1:
        if calculator.conversion_type == "mcg/kg/min to mL/hr":
            dose = st.number_input("Liều (mcg/kg/phút):", min_value=0.0, step=0.1)
            calculator.set_input("Liều", dose)
        else:
            rate = st.number_input("Tốc độ (mL/giờ):", min_value=0.0, step=0.1)
            calculator.set_input("Tốc độ", rate)

        weight = st.number_input("Cân nặng (kg):", min_value=0.0, step=0.1)
        calculator.set_input("Cân nặng", weight)

    with col2:
        concentration = st.number_input("Nồng độ thuốc (mg/mL):", min_value=0.0, step=0.1)
        calculator.set_input("Nồng độ", concentration)

    st.markdown("---")

    if st.button("Tính toán", type="primary", use_container_width=True):
        ok, msg = calculator.validate_inputs()
        if not ok:
            st.error(msg)
            return

        try:
            result = calculator.calculate()
        except ValueError as exc:
            st.error(str(exc))
            return

        st.success(f"Kết quả: {result['value']:.2f} {result['unit']}")


