"""Main DIRC calculator logic."""

from __future__ import annotations

from typing import Dict, Tuple

from .conversions import mcg_kg_min_to_ml_hr, ml_hr_to_mcg_kg_min
from .validation import validate_positive
from .utils import summarize_result


class DIRCCalculator:
    """Main DIRC Calculator class."""

    def __init__(self) -> None:
        self.conversion_type: str | None = None
        self.inputs: Dict[str, float] = {}
        self.results: Dict[str, float | str] = {}

    def set_conversion_type(self, type_: str) -> None:
        """Set the conversion type."""
        self.conversion_type = type_

    def set_input(self, key: str, value: float) -> None:
        """Set input value."""
        self.inputs[key] = value

    def validate_inputs(self) -> Tuple[bool, str]:
        """Validate current inputs for positivity."""
        try:
            for key, value in self.inputs.items():
                validate_positive(value, key)
        except ValueError as exc:
            return False, str(exc)
        return True, "Valid"

    def calculate(self) -> Dict[str, float | str]:
        """Perform the calculation based on `conversion_type`."""
        ok, msg = self.validate_inputs()
        if not ok:
            raise ValueError(msg)

        if self.conversion_type == "mcg/kg/min to mL/hr":
            dose = self.inputs.get("Liều")
            weight = self.inputs.get("Cân nặng")
            concentration = self.inputs.get("Nồng độ")
            if dose is None or weight is None or concentration is None:
                raise ValueError("Thiếu dữ liệu: cần đủ Liều, Cân nặng và Nồng độ")
            value = mcg_kg_min_to_ml_hr(dose, weight, concentration)
            self.results = summarize_result(value, "mL/giờ")

        elif self.conversion_type == "mL/hr to mcg/kg/min":
            rate = self.inputs.get("Tốc độ")
            weight = self.inputs.get("Cân nặng")
            concentration = self.inputs.get("Nồng độ")
            if rate is None or weight is None or concentration is None:
                raise ValueError("Thiếu dữ liệu: cần đủ Tốc độ, Cân nặng và Nồng độ")
            value = ml_hr_to_mcg_kg_min(rate, weight, concentration)
            self.results = summarize_result(value, "mcg/kg/phút")

        else:
            raise ValueError("Chưa chọn loại chuyển đổi hợp lệ cho DIRC")

        return self.results


