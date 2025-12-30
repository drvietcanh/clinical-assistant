"""Streamlit UI for the DIRC calculator."""

from __future__ import annotations

import math
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
    
    # Tab selection: General DIRC or Cardiovascular Drugs
    tab1, tab2 = st.tabs([
        "📝 Chuyển đổi tổng quát",
        "💉 Thuốc tim mạch cấp cứu"
    ])
    
    with tab1:
        _render_general_dirc()
    
    with tab2:
        _render_cardiovascular_dirc()


def _render_general_dirc() -> None:
    """Render general DIRC calculator (original functionality)."""
    calculator = DIRCCalculator()

    # Select conversion direction
    if "dirc_precision" not in st.session_state:
        st.session_state["dirc_precision"] = 2

    conversion_label = st.radio(
        "Chọn loại chuyển đổi chính",
        options=[
            "mcg/kg/phút → mL/giờ",
            "mL/giờ → mcg/kg/phút",
        ],
        index=0 if st.session_state.get("dirc_conversion") != "mL/hr to mcg/kg/min" else 1,
        horizontal=False,
        key="dirc_conversion_label",
    )

    if "mcg/kg/phút" in conversion_label:
        calculator.set_conversion_type("mcg/kg/min to mL/hr")
        st.session_state["dirc_conversion"] = "mcg/kg/min to mL/hr"
    else:
        calculator.set_conversion_type("mL/hr to mcg/kg/min")
        st.session_state["dirc_conversion"] = "mL/hr to mcg/kg/min"

    col1, col2 = st.columns(2)

    with col1:
        if calculator.conversion_type == "mcg/kg/min to mL/hr":
            dose = st.number_input(
                "Liều (mcg/kg/phút):",
                min_value=0.0,
                step=0.1,
                help="Đơn vị: mcg/kg/phút",
                key="dirc_dose",
            )
            calculator.set_input("Liều", dose)
        else:
            rate = st.number_input(
                "Tốc độ (mL/giờ):",
                min_value=0.0,
                step=0.1,
                help="Đơn vị: mL/giờ",
                key="dirc_rate",
            )
            calculator.set_input("Tốc độ", rate)

        # Hiển thị cân nặng chỉ với 1 số thập phân (tránh hiện 2 số 0 dư thừa)
        weight = st.number_input(
            "Cân nặng (kg):",
            min_value=0.0,
            step=0.1,
            format="%.1f",
            help="Cảnh báo khi <3 kg hoặc >200 kg",
            value=st.session_state.get("dirc_weight", 50.0),
            key="dirc_weight",
        )
        calculator.set_input("Cân nặng", weight)
        if 0 < weight < 3 or weight > 200:
            st.warning("Cân nặng nhập có vẻ bất thường, vui lòng kiểm tra lại.")

    with col2:
        # Emergency drug presets (optional)
        st.markdown("#### Thuốc cấp cứu (tùy chọn)")
        drug_display_names = ["Không chọn"] + get_drug_names()
        selected_drug_name = st.selectbox(
            "Chọn thuốc",
            options=drug_display_names,
            index=st.session_state.get("dirc_drug_index", 0),
            key="dirc_drug",
        )
        st.session_state["dirc_drug_index"] = drug_display_names.index(selected_drug_name)
        selected_drug_key = (
            find_drug_key_by_name(selected_drug_name) if selected_drug_name != "Không chọn" else None
        )

        suggested_concentration = None
        container_volume_ml = st.session_state.get("dirc_container_volume", 50.0)
        vial_label = None
        vial = None

        if selected_drug_key:
            vial_labels = get_vial_labels_for_drug(selected_drug_key)
            vial_index = st.session_state.get("dirc_vial_index", 0)
            vial_label = st.selectbox(
                "Loại ống / hàm lượng",
                options=vial_labels,
                index=min(vial_index, len(vial_labels) - 1),
                key="dirc_vial",
            )
            st.session_state["dirc_vial_index"] = vial_labels.index(vial_label)
            vial = get_vial_info(selected_drug_key, vial_label)

            container_label = st.selectbox(
                "Pha vào bơm/chai",
                options=[
                    "Bơm tiêm 50 mL",
                    "Chai 500 mL",
                    "Tùy chỉnh",
                ],
                index=st.session_state.get("dirc_container_index", 0),
                key="dirc_container",
            )
            st.session_state["dirc_container_index"] = ["Bơm tiêm 50 mL", "Chai 500 mL", "Tùy chỉnh"].index(
                container_label
            )
            if container_label == "Tùy chỉnh":
                container_volume_ml = st.number_input(
                    "Thể tích pha (mL)",
                    min_value=1.0,
                    step=1.0,
                    value=float(container_volume_ml or 50.0),
                    key="dirc_custom_volume",
                )
            else:
                container_volume_ml = 50.0 if "50" in container_label else 500.0
                st.session_state["dirc_custom_volume"] = container_volume_ml

            st.session_state["dirc_container_volume"] = container_volume_ml

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
                    "Tùy chỉnh",
                ],
                index=st.session_state.get("dirc_container_index", 0),
                key="dirc_container_no_drug",
            )
            st.session_state["dirc_container_index"] = ["Bơm tiêm 50 mL", "Chai 500 mL", "Tùy chỉnh"].index(
                container_label
            )
            if container_label == "Tùy chỉnh":
                container_volume_ml = st.number_input(
                    "Thể tích pha (mL)",
                    min_value=1.0,
                    step=1.0,
                    value=float(container_volume_ml or 50.0),
                    key="dirc_custom_volume_no_drug",
                )
            else:
                container_volume_ml = 50.0 if "50" in container_label else 500.0
                st.session_state["dirc_custom_volume_no_drug"] = container_volume_ml
            st.session_state["dirc_container_volume"] = container_volume_ml

        # Concentration input (user can copy from suggestion above)
        default_conc = suggested_concentration if suggested_concentration is not None else 0.0

        # Tự động điền nồng độ khi đổi thuốc/ống/chai
        last_key = f"{selected_drug_key}_{vial_label}_{container_volume_ml}" if selected_drug_key else None
        if last_key and st.session_state.get("dirc_last_key") != last_key and suggested_concentration:
            st.session_state["dirc_concentration"] = round(suggested_concentration, 3)
            st.session_state["dirc_last_key"] = last_key
        concentration_value = st.session_state.get("dirc_concentration", default_conc)

        concentration = st.number_input(
            "Nồng độ thuốc (mg/mL):",
            min_value=0.0,
            step=0.01,
            value=concentration_value,
            format="%.3f",
            help="Đơn vị: mg/mL",
            key="dirc_concentration",
        )
        calculator.set_input("Nồng độ", concentration)
        if concentration >= 10:
            st.warning("Nồng độ cao bất thường, hãy kiểm tra lại pha loãng.")
        if vial and concentration > 0 and vial["amount_mg"] > 0 and container_volume_ml > 0:
            vials_needed = (concentration * container_volume_ml) / vial["amount_mg"]
            st.caption(
                f"Số ống cần pha (ước tính): {vials_needed:.2f} ống "
                f"(~ {math.ceil(vials_needed)} ống nếu làm tròn lên)."
            )

    st.markdown("---")

    precision = st.select_slider(
        "Số chữ số thập phân hiển thị kết quả",
        options=[0, 1, 2, 3],
        value=st.session_state.get("dirc_precision", 2),
        key="dirc_precision",
    )

    col_run, col_reset = st.columns([3, 1])

    def reset_dirc():
        for key in list(st.session_state.keys()):
            if key.startswith("dirc_"):
                del st.session_state[key]

    if col_reset.button("Reset nhanh"):
        reset_dirc()
        st.experimental_rerun()

    if col_run.button("Tính toán", type="primary", use_container_width=True):
        ok, msg = calculator.validate_inputs()
        if not ok:
            st.error(msg)
            return

        try:
            result = calculator.calculate()
        except ValueError as exc:
            st.error(str(exc))
            return

        result_value = result["value"]
        result_str = f"{result_value:.{precision}f} {result['unit']}"
        st.success(f"Kết quả: {result_str}")

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

        # Cảnh báo nếu vượt khoảng liều gợi ý (khi có preset)
        if selected_drug_key:
            dose_range = EMERGENCY_DRUG_PRESETS[selected_drug_key].get("dose_range")
            if dose_range:
                min_dose = dose_range.get("min_mcg_kg_min", 0) or 0
                max_dose = dose_range.get("max_mcg_kg_min", 0) or 0
                if calculator.conversion_type == "mcg/kg/min to mL/hr":
                    entered_dose = calculator.inputs.get("Liều", 0)
                    if max_dose and entered_dose > max_dose:
                        st.warning("Liều nhập vượt khuyến cáo tối đa, hãy rà soát lại.")
                    elif min_dose and entered_dose < min_dose:
                        st.warning("Liều nhập thấp hơn khuyến cáo, hãy cân nhắc hiệu chỉnh.")
                else:
                    mcg_per_kg_min = result_value if result["unit"] == "mcg/kg/phút" else 0
                    if max_dose and mcg_per_kg_min > max_dose:
                        st.warning("Tốc độ hiện tại tương đương liều vượt khuyến cáo tối đa.")
                    elif min_dose and mcg_per_kg_min < min_dose:
                        st.info("Tốc độ hiện tại tương đương liều thấp hơn khuyến cáo (có thể cần titrate).")

        # Cho phép copy kết quả
        st.text_input("Copy kết quả", value=result_str, key="dirc_copy_result")


def _render_cardiovascular_dirc() -> None:
    """Render cardiovascular drugs calculator integrated into DIRC."""
    try:
        from components.cardiovascular_calculator import render_cardiovascular_calculator
        render_cardiovascular_calculator()
    except ImportError:
        st.error("Không thể tải cardiovascular calculator. Vui lòng kiểm tra file components/cardiovascular_calculator.py")
        st.info("Sử dụng tab 'Chuyển đổi tổng quát' để tính toán với thuốc bất kỳ.")



