"""
Unit tests cho Vancomycin dosing calculator.

Mục tiêu:
- Kiểm tra IBW/ABW, CrCl và liều gợi ý trong một số kịch bản điển hình.
"""

from antibiotics.vancomycin import calculate_vancomycin_dose


def test_non_obese_normal_renal_function():
    """Bệnh nhân không béo phì, thận bình thường → liều hợp lý."""
    result = calculate_vancomycin_dose(
        age=40,
        weight_kg=70.0,
        height_cm=170.0,
        sex="Nam",
        scr_mgdl=1.0,
        indication="Nhiễm khuẩn da và mô mềm",
    )

    # IBW khoảng 66kg, không dùng ABW
    assert 65 <= result["ibw"] <= 67
    assert 69 <= result["dosing_weight"] <= 71

    # CrCl khoảng > 90 mL/phút
    assert result["crcl"] > 90

    # Loading dose 25mg/kg, làm tròn bội số 250mg
    assert result["loading_dose_mg_kg"] == 25
    assert result["loading_dose_mg"] % 250 == 0

    # Maintenance q12h cho chức năng thận bình thường
    assert result["interval_h"] == 12
    assert result["maintenance_dose_mg"] % 250 == 0


def test_obese_patient_uses_adjusted_body_weight():
    """Bệnh nhân béo phì → dùng ABW cho tính liều."""
    result = calculate_vancomycin_dose(
        age=50,
        weight_kg=120.0,
        height_cm=170.0,
        sex="Nam",
        scr_mgdl=1.0,
        indication="Nhiễm khuẩn nặng/phức tạp (MRSA)",
    )

    ibw = result["ibw"]
    dosing_weight = result["dosing_weight"]

    # Xác nhận đang dùng ABW (giữa IBW và thực)
    assert dosing_weight > ibw
    assert dosing_weight < 120.0

    # Nhiễm khuẩn nặng → loading 30mg/kg
    assert result["loading_dose_mg_kg"] == 30
    assert result["loading_dose_mg"] % 250 == 0


def test_renal_failure_long_interval():
    """Suy thận nặng (CrCl rất thấp) → khoảng cách liều dài hơn."""
    result = calculate_vancomycin_dose(
        age=70,
        weight_kg=60.0,
        height_cm=160.0,
        sex="Nữ",
        scr_mgdl=5.0,
        indication="Nhiễm khuẩn nặng/phức tạp (MRSA)",
    )

    # CrCl rất thấp
    assert result["crcl"] < 20
    # Khoảng cách liều nên ≥24h
    assert result["interval_h"] >= 24

