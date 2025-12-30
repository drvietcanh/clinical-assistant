"""Streamlit UI for the DIRC calculator."""

from __future__ import annotations

import math
from typing import Optional
import streamlit as st

from .calculator import DIRCCalculator
from .drug_presets import (
    EMERGENCY_DRUG_PRESETS,
    get_drug_names,
    find_drug_key_by_name,
    get_vial_labels_for_drug,
    get_vial_info,
)

# Mapping từ DIRC preset keys sang cardiovascular_drugs.json names
DIRC_TO_CV_DRUG_MAP = {
    "Epinephrine": "Adrenaline",
    "Norepinephrine": "Noradrenaline",
    "Dopamine": "Dopamine",
    "Dobutamine": "Dobutamine",
    "Phenylephrine": "Phenylephrine",
    "Milrinone": "Milrinone",
    "Vasopressin": "Vasopressin",
}


def _is_cardiovascular_drug(dirc_drug_key: str) -> bool:
    """Check if selected drug is a cardiovascular drug."""
    return dirc_drug_key in DIRC_TO_CV_DRUG_MAP


def _get_cv_drug_name(dirc_drug_key: str) -> Optional[str]:
    """Get cardiovascular drug name from DIRC preset key."""
    return DIRC_TO_CV_DRUG_MAP.get(dirc_drug_key)


def render_dirc_calculator() -> None:
    """Render the unified DIRC calculator UI with integrated cardiovascular drugs."""
    st.header("💉 Drug Infusion Rate Conversion (DIRC)")
    st.caption(
        "Chuyển đổi liều truyền giữa (mcg/kg/phút) và (mL/giờ) dựa trên cân nặng, nồng độ thuốc. "
        "Hỗ trợ bơm tiêm 50 mL / chai 500 mL và preset cho các thuốc cấp cứu thường dùng. "
        "Khi chọn thuốc tim mạch cấp cứu, sẽ hiển thị đầy đủ thông tin chi tiết."
    )

    # Single unified interface
    _render_unified_dirc()


def _render_unified_dirc() -> None:
    """Render unified DIRC calculator with integrated cardiovascular drug support."""
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
        st.markdown("#### 💊 Thuốc cấp cứu (tùy chọn)")
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
                    f"💡 Gợi ý liều: {dose_range.get('min_mcg_kg_min', 0):.2f} – "
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

    # Check if cardiovascular drug is selected
    is_cv_drug = selected_drug_key and _is_cardiovascular_drug(selected_drug_key)
    cv_drug_name = _get_cv_drug_name(selected_drug_key) if is_cv_drug else None

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

        # Tính thêm thời gian truyền hết bơm/chai theo mL/giờ nếu có tốc độ
        infusion_rate_ml_hr = None
        if result["unit"] == "mL/giờ":
            infusion_rate_ml_hr = float(result["value"])
        elif calculator.conversion_type == "mL/hr to mcg/kg/min":
            infusion_rate_ml_hr = float(calculator.inputs.get("Tốc độ", 0.0))

        # If cardiovascular drug, use enhanced calculation and display
        if is_cv_drug and cv_drug_name:
            _render_cardiovascular_enhanced_results(
                cv_drug_name,
                calculator,
                result,
                result_str,
                precision,
                weight,
                infusion_rate_ml_hr,
                container_volume_ml,
                container_label,
                selected_drug_key,
            )
        else:
            # Standard DIRC results
            st.success(f"Kết quả: {result_str}")

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


def _render_cardiovascular_enhanced_results(
    cv_drug_name: str,
    calculator: DIRCCalculator,
    result: dict,
    result_str: str,
    precision: int,
    weight: float,
                infusion_rate_ml_hr: Optional[float],
    container_volume_ml: float,
    container_label: str,
    selected_drug_key: str,
) -> None:
    """Render enhanced results for cardiovascular drugs with full information."""
    try:
        from drugs.cardiovascular_calculator import (
            get_drug_info,
            calculate_complete_infusion,
            validate_dose_range,
        )
        from components.ui.results import render_result_card, render_result_box
        from components.ui.alerts import render_info_alert, render_warning_alert

        # Get drug info
        drug_info = get_drug_info(cv_drug_name)
        if not drug_info:
            # Fallback to standard DIRC display
            st.success(f"Kết quả: {result_str}")
            return

        # Determine infusion method from container
        infusion_method = "syringe_pump_50ml" if "50" in container_label else "iv_bag_500ml"

        # Get dose for calculation
        if calculator.conversion_type == "mcg/kg/min to mL/hr":
            dose_mcg_kg_min = calculator.inputs.get("Liều", 0)
        else:
            # Reverse calculation: mL/hr → mcg/kg/min
            dose_mcg_kg_min = result["value"] if result["unit"] == "mcg/kg/phút" else 0

        if dose_mcg_kg_min <= 0:
            st.success(f"Kết quả: {result_str}")
            return

        # Calculate complete infusion details
        try:
            drop_factor = 20 if infusion_method == "iv_bag_500ml" else None
            results = calculate_complete_infusion(
                cv_drug_name,
                dose_mcg_kg_min,
                weight,
                infusion_method,
                drop_factor,
            )

            st.markdown("---")
            st.markdown("### 📊 Kết quả tính toán")

            # Main results
            metrics = [
                {
                    "label": "Tổng liều/phút",
                    "value": f"{results['total_dose_mcg_min']:.2f} µg/min",
                    "icon": "⏱️",
                },
                {
                    "label": "Tổng liều/giờ",
                    "value": f"{results['total_dose_mcg_hour']:.2f} µg/h",
                    "icon": "💉",
                },
                {
                    "label": "Tốc độ truyền",
                    "value": f"{results['infusion_rate_ml_hour']:.2f} ml/h",
                    "icon": "💧",
                },
            ]

            # Add drop rate if applicable
            if results.get("drop_rate_gtt_min"):
                metrics.append(
                    {
                        "label": "Giọt/phút",
                        "value": f"{results['drop_rate_gtt_min']:.1f} gtt/min",
                        "icon": "💧",
                    }
                )

            render_result_card("Kết quả tính toán", metrics, color="primary")

            # Infusion time
            st.markdown("---")
            st.markdown("### ⏰ Thời gian truyền")
            col1, col2 = st.columns(2)

            with col1:
                render_result_box(
                    "Thời gian",
                    results["time_formatted"],
                    color="info",
                    icon="⏱️",
                )

            with col2:
                render_result_box(
                    "Thể tích",
                    f"{results['volume_ml']} ml",
                    color="info",
                )

            # Preparation instructions
            st.markdown("---")
            st.markdown("### 📋 Hướng dẫn pha thuốc")
            render_info_alert(
                results.get("preparation_instructions", "Không có hướng dẫn"),
                title="Cách pha",
            )

            # Drug information
            st.markdown("---")
            st.markdown("### 💊 Thông tin thuốc")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Chỉ định:**")
                st.info(drug_info.get("indication", "N/A"))

                st.markdown("**Theo dõi:**")
                monitoring = drug_info.get("monitoring", "")
                if monitoring:
                    for item in monitoring.split(", "):
                        st.markdown(f"- ✅ {item}")

            with col2:
                st.markdown("**Liều khuyến nghị:**")
                st.markdown(f"- **Khởi đầu:** {drug_info.get('initial_dose', 'N/A')}")
                st.markdown(f"- **Thông thường:** {drug_info.get('dose_range', 'N/A')}")
                st.markdown(f"- **Tối đa:** {drug_info.get('max_dose', 'N/A')}")

                if drug_info.get("side_effects"):
                    st.markdown("**Tác dụng phụ:**")
                    st.warning(drug_info.get("side_effects"))

            # Notes
            if drug_info.get("notes"):
                st.markdown("---")
                st.markdown("### 💡 Lưu ý")
                render_info_alert(drug_info.get("notes"), title="Thông tin quan trọng")

            # Validate dose range
            validation = validate_dose_range(cv_drug_name, dose_mcg_kg_min)
            if not validation["is_valid"]:
                st.markdown("---")
                render_warning_alert(validation["warning"], title="Cảnh báo liều dùng")

            # Vial Management (if available)
            try:
                from components.vial_selector import render_vial_selector, render_preparation_calculator

                st.markdown("---")
                st.markdown("### 📦 Quản lý ống thuốc")

                # Calculate total dose needed for 24 hours
                total_dose_mcg = results["total_dose_mcg_hour"] * 24
                total_dose_mg = total_dose_mcg / 1000

                # Render vial selector
                vial_result = render_vial_selector(cv_drug_name, total_dose_mg)

                # Preparation calculator
                if vial_result:
                    st.markdown("---")
                    render_preparation_calculator(
                        cv_drug_name,
                        vial_result["total_available_mg"],
                        vial_result.get("selected_vial"),
                    )
            except ImportError:
                pass

            # Copy result
            st.markdown("---")
            st.text_input("Copy kết quả", value=result_str, key="dirc_copy_result_cv")

        except Exception as e:
            st.error(f"Lỗi tính toán chi tiết: {str(e)}")
            st.success(f"Kết quả cơ bản: {result_str}")

    except ImportError:
        # Fallback to standard DIRC display
        st.success(f"Kết quả: {result_str}")
