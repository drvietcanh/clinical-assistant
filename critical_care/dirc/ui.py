"""Streamlit UI for the DIRC calculator."""

from __future__ import annotations

import streamlit as st

from .calculator import DIRCCalculator
from .drug_presets import (
    EMERGENCY_DRUG_PRESETS,
    get_drug_names,
    find_drug_key_by_name,
    get_vial_labels_for_drug,
    get_vial_info,
)


def render_dirc_calculator() -> None:
    """Render the DIRC calculator UI."""
    st.header("💉 Drug Infusion Rate Conversion (DIRC)")
    st.caption(
        "Chuyển đổi liều truyền giữa (mcg/kg/phút) và (mL/giờ) dựa trên cân nặng, nồng độ thuốc. "
        "Hỗ trợ bơm tiêm 50 mL / chai 500 mL và preset cho các thuốc cấp cứu thường dùng."
    )

    calculator = DIRCCalculator()

    # Select conversion direction
    conversion_label = st.radio(
        "Chọn loại chuyển đổi chính",
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

        # Hiển thị cân nặng chỉ với 1 số thập phân (tránh hiện 2 số 0 dư thừa)
        weight = st.number_input("Cân nặng (kg):", min_value=0.0, step=0.1, format="%.1f")
        calculator.set_input("Cân nặng", weight)

    with col2:
        # Emergency drug presets (optional)
        st.markdown("#### Thuốc cấp cứu (tùy chọn)")
        drug_display_names = ["Không chọn"] + get_drug_names()
        selected_drug_name = st.selectbox("Chọn thuốc", options=drug_display_names, index=0)
        selected_drug_key = (
            find_drug_key_by_name(selected_drug_name) if selected_drug_name != "Không chọn" else None
        )

        suggested_concentration = None

        if selected_drug_key:
            vial_labels = get_vial_labels_for_drug(selected_drug_key)
            vial_label = st.selectbox("Loại ống / hàm lượng", options=vial_labels, index=0)
            vial = get_vial_info(selected_drug_key, vial_label)

            container_label = st.selectbox(
                "Pha vào bơm/chai",
                options=[
                    "Bơm tiêm 50 mL",
                    "Chai 500 mL",
                ],
                index=0,
            )
            container_volume_ml = 50.0 if "50" in container_label else 500.0

            if vial:
                base_conc = vial["amount_mg"] / vial["volume_ml"]
                final_conc = vial["amount_mg"] / container_volume_ml
                suggested_concentration = final_conc

                st.caption(
                    f"Hàm lượng gốc: **{vial['amount_mg']} mg / {vial['volume_ml']} mL** "
                    f"(~ {base_conc:.2f} mg/mL). Pha vào **{int(container_volume_ml)} mL** → "
                    f"nồng độ ~ **{final_conc:.3f} mg/mL** (copy vào ô nồng độ bên dưới)."
                )

            dose_range = EMERGENCY_DRUG_PRESETS[selected_drug_key].get("dose_range")
            if dose_range:
                st.info(
                    f"Gợi ý liều: {dose_range.get('min_mcg_kg_min', 0):.2f} – "
                    f"{dose_range.get('max_mcg_kg_min', 0):.2f} mcg/kg/phút. "
                    f"{dose_range.get('note', '')}"
                )
        else:
            container_label = st.selectbox(
                "Loại bơm/chai",
                options=[
                    "Bơm tiêm 50 mL",
                    "Chai 500 mL",
                ],
                index=0,
            )
            container_volume_ml = 50.0 if "50" in container_label else 500.0

        # Concentration input (user can copy from suggestion above)
        default_conc = suggested_concentration if suggested_concentration is not None else 0.0
        concentration = st.number_input(
            "Nồng độ thuốc (mg/mL):",
            min_value=0.0,
            step=0.01,
            value=default_conc,
            format="%.3f",
        )
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

        # Tính thêm thời gian truyền hết bơm/chai theo mL/giờ nếu có tốc độ
        infusion_rate_ml_hr = None
        if result["unit"] == "mL/giờ":
            infusion_rate_ml_hr = float(result["value"])
        elif calculator.conversion_type == "mL/hr to mcg/kg/min":
            # Trong chiều này, tốc độ mL/giờ là input ban đầu
            infusion_rate_ml_hr = float(calculator.inputs.get("Tốc độ", 0.0))

        if infusion_rate_ml_hr and infusion_rate_ml_hr > 0:
            time_hours = container_volume_ml / infusion_rate_ml_hr
            time_minutes = time_hours * 60.0

            st.info(
                f"⏱ Thời gian truyền hết {int(container_volume_ml)} mL ở tốc độ hiện tại: "
                f"~ {time_hours:.2f} giờ (~ {time_minutes:.0f} phút)."
            )


